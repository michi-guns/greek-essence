from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[3] / ".agents/skills/ralph-loop-manager/scripts/preflight.py"
SPEC = importlib.util.spec_from_file_location("ralph_manager_preflight", SCRIPT)
assert SPEC and SPEC.loader
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)


class MechanicalHelpersTests(unittest.TestCase):
    def test_exact_signals_accept_only_named_boolean(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "signal.json"
            path.write_text('{"isPaused": false}', encoding="utf-8")
            self.assertFalse(preflight.exact_signal(path, "isPaused"))
            for text in ('{"isPaused": 0}', '{"isPaused": false, "extra": 1}',
                         '{"isPaused": false, "isPaused": true}'):
                path.write_text(text, encoding="utf-8")
                with self.subTest(text=text), self.assertRaises(ValueError):
                    preflight.exact_signal(path, "isPaused")

    def test_containment_rejects_outside_and_symlink_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve() / "root"
            root.mkdir()
            regular = root / "regular"
            regular.write_text("ok", encoding="utf-8")
            outside = root.parent / "outside"
            outside.write_text("no", encoding="utf-8")
            self.assertTrue(preflight.is_contained_regular_file(regular, root))
            self.assertFalse(preflight.is_contained_regular_file(outside, root))
            link = root / "link"
            try:
                link.symlink_to(outside)
            except OSError:
                self.skipTest("file symlinks unavailable")
            self.assertFalse(preflight.is_contained_regular_file(link, root))

    def test_progress_requires_correct_feature_and_empty_warnings(self) -> None:
        good = {"feature": {"slug": preflight.FEATURE}, "warnings": [], "frontier": {"kind": "implement-issue", "issueId": 2, "artifactPath": "issues/02-example/issue.md"}}
        self.assertEqual((True, "implement-issue"), preflight.validate_progress(json.dumps(good)))
        for payload in ({"feature": {"slug": "other"}, "warnings": []},
                        {"feature": {"slug": preflight.FEATURE}, "warnings": ["stale"]}):
            with self.subTest(payload=payload):
                self.assertFalse(preflight.validate_progress(json.dumps(payload))[0])

    def test_progress_requires_duplicate_free_routable_frontier_schema(self) -> None:
        prefix = {"feature": {"slug": preflight.FEATURE}, "warnings": []}
        cases = {
            "missing-kind": {**prefix, "frontier": {"artifactPath": "issues/02-example/issue.md", "issueId": 2}},
            "unknown-kind": {**prefix, "frontier": {"kind": "unknown", "artifactPath": "issues/02-example/issue.md", "issueId": 2}},
            "issue-without-id": {**prefix, "frontier": {"kind": "implement-issue", "artifactPath": "issues/02-example/issue.md"}},
            "non-issue-with-id": {**prefix, "frontier": {"kind": "plan-milestones", "artifactPath": "SPEC.md", "issueId": 2}},
            "duplicate-kind": '{"feature":{"slug":"greek-essence-showcase"},"warnings":[],"frontier":{"kind":"implement-issue","kind":"review-issue","issueId":2,"artifactPath":"issues/02-example/issue.md"}}',
        }
        for name, value in cases.items():
            text = value if isinstance(value, str) else json.dumps(value)
            with self.subTest(name=name):
                self.assertFalse(preflight.validate_progress(text)[0])

    def test_progress_accepts_actual_artifactless_stable_shapes(self) -> None:
        prefix = {"feature": {"slug": preflight.FEATURE}, "warnings": []}
        for kind, issue_id in (("review-issue", 2), ("implement-issue", 2),
                               ("design-ready", None), ("feature-review", None),
                               ("blocked", None), ("archived", None)):
            frontier: dict[str, object] = {"kind": kind, "summary": f"{kind} exact stable shape"}
            if issue_id is not None:
                frontier["issueId"] = issue_id
            with self.subTest(kind=kind):
                self.assertEqual((True, kind), preflight.validate_progress(json.dumps({**prefix, "frontier": frontier})))

    def test_email_environment_checks_shape_without_exposing_values(self) -> None:
        valid = {"RESEND_API_KEY": "re_test_value_only", "RESEND_FROM_EMAIL": "Hermes <notify@resend.dev>"}
        with patch.dict(preflight.os.environ, valid, clear=True):
            self.assertEqual((True, []), preflight.validate_email_environment())
        with patch.dict(preflight.os.environ, {"RESEND_API_KEY": "bad", "RESEND_FROM_EMAIL": "notify@example.com"}, clear=True):
            ok, problems = preflight.validate_email_environment()
        self.assertFalse(ok)
        self.assertTrue(problems)
        self.assertNotIn("bad", json.dumps(problems))

    def test_runtime_lock_requires_duplicate_free_exact_ownership_record(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            lock = Path(temp) / "ralph.lock"
            invalid = (
                '{"controller_pid": 2147483647, "controller_pid": 9, "root_pid": null}',
                '{"controller_pid": 2147483647, "root_pid": 54321, "root_pid": null}',
                '{"controller_pid": 2147483647, "root_pid": null, "extra": true}',
                '{"controller_pid":',
            )
            for payload in invalid:
                with self.subTest(payload=payload):
                    lock.write_text(payload, encoding="utf-8")
                    compatible, _, code = preflight.runtime_lock_status(lock)
                    self.assertFalse(compatible)
                    self.assertEqual("INVALID_RUNTIME_OWNERSHIP_RECORD", code)
            lock.write_text('{"controller_pid": 2147483647, "root_pid": null, "launch_state": "idle"}', encoding="utf-8")
            with patch.object(preflight, "pid_is_running", return_value=False):
                self.assertEqual(
                    (True, "stale controller_pid=2147483647; root_pid=none; launch_state=idle", None),
                    preflight.runtime_lock_status(lock),
                )
    def test_cleanup_ambiguity_is_launch_blocking_even_when_liveness_later_reports_dead(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            lock = Path(temp) / "ralph.lock"
            lock.write_text(
                '{"controller_pid": 2147483647, "root_pid": 54321, "launch_state": "cleanup_ambiguous"}',
                encoding="utf-8",
            )
            with patch.object(preflight, "pid_is_running", return_value=False):
                compatible, evidence, code = preflight.runtime_lock_status(lock)
        self.assertFalse(compatible)
        self.assertEqual("AMBIGUOUS_SURVIVING_ROOT_PROCESS", code)
        self.assertIn("launch_state=cleanup_ambiguous", evidence)


class PreflightCliTests(unittest.TestCase):
    def _run(self, *, profiles: set[str] | None = None, dirty: bool = True,
             completion: bool = False, pause: bool = False,
             runtime_lock: dict[str, object] | None = None,
             root_status: bool | None = False) -> tuple[int, dict[str, object], list[list[str]]]:
        profiles = set(preflight.REQUIRED_PROFILES) if profiles is None else profiles
        calls: list[list[str]] = []

        def fake_run(command: list[str], cwd: Path, timeout: float = 20) -> subprocess.CompletedProcess[str]:
            calls.append(command)
            if command[:2] == ["git", "rev-parse"]:
                return subprocess.CompletedProcess(command, 0, stdout=str(preflight.OWNED_REPOSITORY))
            if command[:2] == ["git", "status"]:
                return subprocess.CompletedProcess(command, 0, stdout=" M preserved.txt\n" if dirty else "")
            if command[:2] == ["features-cli", "docs"]:
                return subprocess.CompletedProcess(command, 0, stdout="current")
            if command[:2] == ["features-cli", "progress"]:
                payload = {"feature": {"slug": preflight.FEATURE}, "warnings": [], "frontier": {"kind": "implement-issue", "issueId": 2, "artifactPath": "issues/02-example/issue.md"}}
                return subprocess.CompletedProcess(command, 0, stdout=json.dumps(payload))
            if command[:3] == ["hermes", "profile", "show"]:
                return subprocess.CompletedProcess(command, 0 if command[3] in profiles else 2, stdout="")
            if command[:3] == ["pnpm", "list", "-g"]:
                payload = [{"dependencies": {"@jz/ai-arsenal-features-cli": {"version": "0.3.0"}}}]
                return subprocess.CompletedProcess(command, 0, stdout=json.dumps(payload))
            if command[0] == preflight.sys.executable and command[-1] == "--help":
                return subprocess.CompletedProcess(command, 0, stdout="usage: sender --dry-run")
            if command[0] == preflight.sys.executable and "--dry-run" in command:
                return subprocess.CompletedProcess(command, 0, stdout=json.dumps({
                    "launch_performed": False,
                    "log_owner": "C:/fixture/issue",
                    "log_run_directory": "C:/fixture/issue/.Ralph/runs/run",
                    "iteration_log": "C:/fixture/issue/.Ralph/runs/run/iteration-0001.log",
                }))
            versions = {"git": "git version 2.50", "hermes": "Hermes 0.1", "bun": "1.2.0",
                        "pnpm": "11.17.0", "features-cli": "0.3.0"}
            return subprocess.CompletedProcess(command, 0, stdout=versions.get(command[0], ""))

        signals = {
            preflight.OWNED_REPOSITORY / ".scratch/ralph-loop/completion-signal.json": {"isEverythingDone": completion},
            preflight.OWNED_REPOSITORY / ".scratch/ralph-loop/pause-signal.json": {"isPaused": pause},
        }
        original_read = Path.read_text

        def fake_read(path: Path, *args: object, **kwargs: object) -> str:
            if path in signals:
                return json.dumps(signals[path])
            return original_read(path, *args, **kwargs)

        output = io.StringIO()
        valid_env = {
            "RESEND_API_KEY": "re_test_value_only",
            "RESEND_FROM_EMAIL": "Hermes <notify@resend.dev>",
        }
        with tempfile.TemporaryDirectory() as runtime:
            email_script = Path(runtime) / "hermes" / "skills" / "email" / "email-notification" / "scripts" / "send_notification.py"
            email_script.parent.mkdir(parents=True)
            (email_script.parent.parent / "SKILL.md").write_text("skill", encoding="utf-8")
            email_script.write_text("# fake", encoding="utf-8")
            if runtime_lock is not None:
                lock = Path(runtime) / "hermes" / "ralph" / "greek-essence" / "ralph.lock"
                lock.parent.mkdir(parents=True)
                lock.write_text(json.dumps(runtime_lock), encoding="utf-8")
            valid_env["LOCALAPPDATA"] = runtime
            with (patch.object(preflight, "run", side_effect=fake_run),
                  patch.object(preflight.shutil, "which", side_effect=lambda name: name),
                  patch.object(preflight.Path, "read_text", fake_read),
                  patch.object(
                      preflight, "pid_is_running",
                      side_effect=lambda pid: root_status if pid == 54321 else False,
                  ),
                  patch.dict(preflight.os.environ, valid_env, clear=False), redirect_stdout(output)):
                code = preflight.main(["--repo", str(preflight.OWNED_REPOSITORY), "--target", preflight.FEATURE])
        return code, json.loads(output.getvalue()), calls

    def test_green_path_checks_mechanics_and_dry_runs_controller(self) -> None:
        code, payload, calls = self._run()
        self.assertEqual(0, code)
        self.assertEqual("PASS", payload["status"])
        self.assertEqual([], payload["hard_stops"])
        self.assertEqual([{"code": "DIRTY_WORKTREE", "message": "Worktree changes observed for manager attribution before launch."}], payload["warnings"])
        names = {item["name"] for item in payload["checks"]}
        self.assertTrue({"required-files", "git", "python", "hermes", "bun", "pnpm", "features-cli-stable",
                         "features-docs-current", "features-progress", "profiles", "runtime-lock",
                         "completion-signal", "pause-signal", "email-readiness", "worktree-observed",
                         "frontier-log-route", "controller-dry-run"}.issubset(names))
        flattened = " ".join(" ".join(call) for call in calls)
        self.assertNotIn("model.default", flattened)
        self.assertNotIn("model.provider", flattened)
        self.assertNotIn("reasoning", flattened)
        self.assertNotIn("semantic_requirements", payload)

    def test_missing_fourth_profile_is_hard_stop_without_config_inspection(self) -> None:
        code, payload, calls = self._run(profiles=set(preflight.REQUIRED_PROFILES[:-1]))
        self.assertEqual(2, code)
        self.assertIn("PROFILES_MISSING", [item["code"] for item in payload["hard_stops"]])
        self.assertFalse(any("config" in call for call in calls))
        self.assertTrue(any("--dry-run" in call for call in calls))
        self.assertIn("controller-dry-run", [item["name"] for item in payload["checks"]])

    def test_completion_true_or_pause_true_is_not_launch_compatible(self) -> None:
        for completion, pause, expected in ((True, False, "COMPLETION_NOT_LAUNCH_COMPATIBLE"),
                                             (False, True, "PAUSE_NOT_LAUNCH_COMPATIBLE")):
            with self.subTest(completion=completion, pause=pause):
                code, payload, _ = self._run(completion=completion, pause=pause)
                self.assertEqual(2, code)
                self.assertIn(expected, [item["code"] for item in payload["hard_stops"]])

    def test_dead_controller_with_surviving_or_ambiguous_root_hard_stops_preflight(self) -> None:
        for root_status in (True, None):
            with self.subTest(root_status=root_status):
                code, payload, _ = self._run(
                    runtime_lock={"controller_pid": 2147483647, "root_pid": 54321, "launch_state": "running"},
                    root_status=root_status,
                )
                self.assertEqual(2, code)
                self.assertIn(
                    "AMBIGUOUS_SURVIVING_ROOT_PROCESS",
                    [item["code"] for item in payload["hard_stops"]],
                )

    def test_malformed_runtime_ownership_record_hard_stops_preflight(self) -> None:
        code, payload, _ = self._run(
            runtime_lock={"controller_pid": 2147483647, "root_pid": "unknown"},
        )
        self.assertEqual(2, code)
        self.assertIn(
            "INVALID_RUNTIME_OWNERSHIP_RECORD",
            [item["code"] for item in payload["hard_stops"]],
        )

    def test_missing_repository_is_structured_hard_stop(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            missing = Path(temp) / "missing"
            output = io.StringIO()
            with redirect_stdout(output):
                code = preflight.main(["--repo", str(missing), "--target", preflight.FEATURE])
        self.assertEqual(2, code)
        self.assertEqual("REPOSITORY_DIRECTORY_MISSING", json.loads(output.getvalue())["hard_stops"][0]["code"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
