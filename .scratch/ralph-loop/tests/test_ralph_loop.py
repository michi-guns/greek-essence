from __future__ import annotations

import importlib.util
import io
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import sys

TOOLS = Path(__file__).resolve().parents[1] / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import ralph_loop as ralph  # noqa: E402

PREFLIGHT_SCRIPT = Path(__file__).resolve().parents[3] / ".agents/skills/ralph-loop-manager/scripts/preflight.py"
PREFLIGHT_SPEC = importlib.util.spec_from_file_location("ralph_manager_preflight_for_loop_test", PREFLIGHT_SCRIPT)
assert PREFLIGHT_SPEC and PREFLIGHT_SPEC.loader
preflight = importlib.util.module_from_spec(PREFLIGHT_SPEC)
PREFLIGHT_SPEC.loader.exec_module(preflight)


class FakeLifecycle:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, object]]] = []

    def emit(self, event: str, **fields: object) -> None:
        self.events.append((event, fields))


class FakeProcess:
    def __init__(self, *, pid: int = 43210, returncode: int | None = None) -> None:
        self.pid = pid
        self.returncode = returncode
        self.terminated = False
        self.killed = False
        self.stdout = io.BytesIO()

    def poll(self) -> int | None:
        return self.returncode

    def wait(self, timeout: float | None = None) -> int:
        if self.returncode is None:
            raise subprocess.TimeoutExpired("hermes", timeout)
        return self.returncode

    def terminate(self) -> None:
        self.terminated = True
        self.returncode = 0

    def kill(self) -> None:
        self.killed = True
        self.returncode = 0


class ThinLoopContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.state_dir = self.repo / "runtime"
        self.write_completion({"isEverythingDone": False})
        self.write_pause({"isPaused": False})

    def write_completion(self, value: object, *, raw: bool = False) -> None:
        path = self.repo / ".scratch" / "ralph-loop" / "completion-signal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(value) if raw else json.dumps(value), encoding="utf-8")

    def write_pause(self, value: object, *, raw: bool = False) -> None:
        path = self.repo / ".scratch" / "ralph-loop" / "pause-signal.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(value) if raw else json.dumps(value), encoding="utf-8")

    def test_completion_signal_has_exact_boolean_schema(self) -> None:
        for boolean in (False, True):
            self.write_completion({"isEverythingDone": boolean})
            with self.subTest(valid=boolean):
                self.assertIs(boolean, ralph.read_completion_signal(self.repo))
        invalid = [
            "[]", "{}", '"true"', '{"isEverythingDone": 1}',
            '{"isEverythingDone": "false"}',
            '{"isEverythingDone": false, "extra": 1}',
            '{"isEverythingDone": false, "isEverythingDone": true}',
        ]
        for text in invalid:
            self.write_completion(text, raw=True)
            with self.subTest(invalid=text), self.assertRaises(ralph.CompletionSignalError):
                ralph.read_completion_signal(self.repo)

    def test_true_at_startup_launches_nothing(self) -> None:
        self.write_completion({"isEverythingDone": True})
        launches: list[int] = []
        outcome = ralph.run_loop(
            self.repo,
            execute_fn=lambda iteration, timeout: launches.append(iteration),
            state_dir=self.state_dir,
        )
        self.assertEqual(ralph.LoopOutcome.COMPLETE, outcome)
        self.assertEqual([], launches)

    def test_false_launches_only_jzgreekorch_without_overrides_or_resume(self) -> None:
        command = ralph.build_hermes_command(self.repo, 1)
        self.assertEqual(["hermes", "-p", "jzgreekorch"], command[:3])
        for forbidden in ("-m", "--model", "--provider", "--resume"):
            self.assertNotIn(forbidden, command)
        launches: list[int] = []
        outcome = ralph.run_loop(
            self.repo, max_iterations=1,
            execute_fn=lambda iteration, timeout: launches.append(iteration),
            state_dir=self.state_dir,
        )
        self.assertEqual([1], launches)
        self.assertEqual(ralph.LoopOutcome.LIMIT_REACHED, outcome)

    def test_every_false_iteration_builds_a_fresh_command_and_session(self) -> None:
        commands: list[list[str]] = []
        outcome = ralph.run_loop(
            self.repo, max_iterations=2,
            execute_fn=lambda iteration, timeout: commands.append(
                ralph.build_hermes_command(self.repo, iteration)
            ),
            state_dir=self.state_dir,
        )
        self.assertEqual(ralph.LoopOutcome.LIMIT_REACHED, outcome)
        self.assertEqual(2, len(commands))
        self.assertIsNot(commands[0], commands[1])
        self.assertEqual(commands[0], commands[1])
        self.assertNotIn("--resume", commands[0])

    def test_completion_after_iteration_stops_before_another_launch(self) -> None:
        launches: list[int] = []

        def execute(iteration: int, timeout: float | None) -> None:
            launches.append(iteration)
            self.write_completion({"isEverythingDone": True})

        outcome = ralph.run_loop(
            self.repo, max_iterations=100, execute_fn=execute, state_dir=self.state_dir
        )
        self.assertEqual(ralph.LoopOutcome.COMPLETE, outcome)
        self.assertEqual([1], launches)

    def test_default_cap_is_100_and_explicit_one_is_supported(self) -> None:
        self.assertEqual(100, ralph.DEFAULT_MAX_ITERATIONS)
        launches: list[int] = []
        outcome = ralph.run_loop(
            self.repo, max_iterations=1,
            execute_fn=lambda iteration, timeout: launches.append(iteration),
            state_dir=self.state_dir,
        )
        self.assertEqual([1], launches)
        self.assertEqual(ralph.LoopOutcome.LIMIT_REACHED, outcome)

    def test_limit_reached_is_a_distinct_cli_non_success(self) -> None:
        with patch.object(ralph, "run_loop", return_value=ralph.LoopOutcome.LIMIT_REACHED):
            output = io.StringIO()
            with redirect_stdout(output):
                code = ralph.main(["--repo", str(self.repo), "--state-dir", str(self.state_dir), "--max-iterations", "1"])
        self.assertNotEqual(0, code)
        self.assertEqual("LIMIT_REACHED", json.loads(output.getvalue())["outcome"])

    def test_nonzero_exit_is_hermes_failed_and_cites_iteration_log(self) -> None:
        error = ralph.HermesProcessError(
            f"Hermes iteration 1 exited 7; log: {self.state_dir / 'logs' / 'iteration-0001.log'}"
        )
        with patch.object(ralph, "run_loop", side_effect=error):
            output = io.StringIO()
            with redirect_stdout(output):
                code = ralph.main(["--repo", str(self.repo), "--state-dir", str(self.state_dir), "--max-iterations", "1"])
        payload = json.loads(output.getvalue())
        self.assertNotEqual(0, code)
        self.assertEqual("HERMES_FAILED", payload["outcome"])
        self.assertIn("iteration-0001", payload["error"])
        self.assertIn("log:", payload["error"])

    def test_timeout_cleans_only_owned_root_tree_and_returns_timeout(self) -> None:
        process = FakeProcess(pid=54321)
        def successful_taskkill(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            process.returncode = 0
            return subprocess.CompletedProcess([], 0, stdout="SUCCESS")

        with patch.object(ralph.os, "name", "nt"), patch.object(
            ralph.subprocess, "run", side_effect=successful_taskkill
        ) as taskkill:
            ralph.terminate_process_tree(process)
        self.assertEqual(["taskkill", "/PID", "54321", "/T", "/F"], taskkill.call_args.args[0])
        error = ralph.IterationTimeout("Ralph iteration 1 timed out; log: iteration-0001.log")
        with patch.object(ralph, "run_loop", side_effect=error):
            output = io.StringIO()
            with redirect_stdout(output):
                code = ralph.main(["--repo", str(self.repo), "--state-dir", str(self.state_dir)])
        self.assertNotEqual(0, code)
        self.assertEqual("TIMEOUT", json.loads(output.getvalue())["outcome"])

    def test_ambiguous_windows_tree_cleanup_fails_closed(self) -> None:
        process = FakeProcess(pid=54321)
        failed = subprocess.CompletedProcess([], 1, stdout="Access is denied")
        with patch.object(ralph.os, "name", "nt"), patch.object(
            ralph.subprocess, "run", return_value=failed
        ), self.assertRaises(ralph.ProcessTreeError):
            ralph.terminate_process_tree(process)
        self.assertIsNone(process.poll())

    def test_live_lock_blocks_launch_and_stale_lock_recovery_is_evidenced(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        with self.assertRaises(ralph.LockConflict):
            ralph._acquire_lock(self.state_dir)
        lock.write_text(json.dumps({"controller_pid": 2147483647, "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        lifecycle = FakeLifecycle()
        with patch.object(ralph, "_pid_is_running", return_value=False):
            acquired = ralph._acquire_lock(self.state_dir, lifecycle)
        self.addCleanup(acquired.unlink, missing_ok=True)
        names = [name for name, _ in lifecycle.events]
        self.assertIn("stale_lock_remove_start", names)
        self.assertIn("stale_lock_remove_complete", names)
        self.assertEqual({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}, json.loads(acquired.read_text(encoding="utf-8")))

    def test_dead_controller_without_root_recovers_only_evidenced_stale_lock(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": 2147483647, "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        lifecycle = FakeLifecycle()
        with patch.object(ralph, "_pid_is_running", return_value=False):
            acquired = ralph._acquire_lock(self.state_dir, lifecycle)
        self.addCleanup(acquired.unlink, missing_ok=True)
        self.assertEqual(
            {"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"},
            json.loads(acquired.read_text(encoding="utf-8")),
        )
        self.assertIn("stale_lock_remove_complete", [name for name, _ in lifecycle.events])

    def test_dead_controller_with_live_root_hard_stops_without_unlink_or_launch(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        original = {"controller_pid": 2147483647, "root_pid": os.getpid(), "launch_state": "running"}
        lock.write_text(json.dumps(original), encoding="utf-8")
        launches: list[int] = []
        with patch.object(ralph, "_pid_is_running", side_effect=lambda pid: pid == os.getpid()), self.assertRaisesRegex(ralph.LockConflict, "surviving root"):
            ralph.run_loop(
                self.repo, max_iterations=1, state_dir=self.state_dir,
                execute_fn=lambda iteration, timeout: launches.append(iteration),
            )
        self.assertEqual([], launches)
        self.assertEqual(original, json.loads(lock.read_text(encoding="utf-8")))

    def test_malformed_or_ambiguous_root_ownership_hard_stops_without_unlink(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        for payload in (
            {"controller_pid": 2147483647, "root_pid": "not-a-pid"},
            {"controller_pid": 2147483647, "root_pid": 98765},
        ):
            with self.subTest(payload=payload):
                lock.write_text(json.dumps(payload), encoding="utf-8")
                with patch.object(
                    ralph, "_pid_is_running", side_effect=lambda pid: False if pid == 2147483647 else None
                ), self.assertRaises(ralph.LockConflict):
                    ralph._acquire_lock(self.state_dir)
                self.assertEqual(payload, json.loads(lock.read_text(encoding="utf-8")))

    def test_root_ownership_clears_only_after_verified_normal_exit(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        process = FakeProcess(pid=54321, returncode=0)
        with patch.object(ralph.subprocess, "Popen", return_value=process), patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ):
            ralph.hermes_executor(self.repo, self.state_dir, 1, 1, lock=lock)
        self.assertIsNone(json.loads(lock.read_text(encoding="utf-8"))["root_pid"])

    def test_verified_timeout_clears_root_ownership(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        process = FakeProcess(pid=54321)

        def verified_cleanup(owned: FakeProcess) -> None:
            owned.returncode = 0

        with patch.object(ralph.subprocess, "Popen", return_value=process), patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ), patch.object(ralph, "terminate_process_tree", side_effect=verified_cleanup), self.assertRaises(ralph.IterationTimeout):
            ralph.hermes_executor(self.repo, self.state_dir, 1, 0.01, lock=lock)
        self.assertIsNone(json.loads(lock.read_text(encoding="utf-8"))["root_pid"])

    def test_cleanup_ambiguity_preserves_recorded_root_and_is_visible(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        process = FakeProcess(pid=54321)
        lifecycle = FakeLifecycle()
        with patch.object(ralph.subprocess, "Popen", return_value=process), patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ), patch.object(ralph, "terminate_process_tree", side_effect=ralph.ProcessTreeError("ambiguous cleanup")), self.assertRaises(ralph.ProcessTreeError):
            ralph.hermes_executor(self.repo, self.state_dir, 1, 0.01, lifecycle=lifecycle, lock=lock)
        self.assertEqual(54321, json.loads(lock.read_text(encoding="utf-8"))["root_pid"])
        self.assertIn("cleanup_ambiguous", [name for name, _ in lifecycle.events])

    def test_run_loop_preserves_ambiguous_root_record_and_blocks_reacquisition(self) -> None:
        process = FakeProcess(pid=54321)
        with patch.object(ralph.subprocess, "Popen", return_value=process), patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ), patch.object(
            ralph, "resolve_frontier_log_location", return_value=(self.repo, self.state_dir, self.state_dir / "logs" / "iteration-0001.log")
        ), patch.object(
            ralph, "terminate_process_tree", side_effect=ralph.ProcessTreeError("ambiguous cleanup")
        ), self.assertRaises(ralph.ProcessTreeError):
            ralph.run_loop(self.repo, max_iterations=1, iteration_timeout=0.01, state_dir=self.state_dir)
        lock = self.state_dir / "ralph.lock"
        self.assertEqual(
            {"controller_pid": os.getpid(), "root_pid": 54321, "launch_state": "running"},
            json.loads(lock.read_text(encoding="utf-8")),
        )
        launches: list[int] = []
        with patch.object(
            ralph, "_pid_is_running", side_effect=lambda pid: False if pid == os.getpid() else True
        ), self.assertRaises(ralph.LockConflict):
            ralph.run_loop(
                self.repo, max_iterations=1, state_dir=self.state_dir,
                execute_fn=lambda iteration, timeout: launches.append(iteration),
            )
        self.assertEqual([], launches)
        self.assertTrue(lock.exists())

    def test_ownership_write_failure_and_ambiguous_cleanup_preserve_pid_blocking_evidence(self) -> None:
        process = FakeProcess(pid=54321)
        writes: list[tuple[int | None, str | None]] = []
        original_write = ralph._write_runtime_record

        def fail_running_write(
            lock: Path, controller_pid: int, root_pid: int | None, launch_state: str | None = None,
        ) -> None:
            writes.append((root_pid, launch_state))
            if root_pid == process.pid and launch_state != "cleanup_ambiguous":
                raise ralph.LockConflict("record write failed")
            if launch_state is None:
                original_write(lock, controller_pid, root_pid)
            else:
                original_write(lock, controller_pid, root_pid, launch_state)

        with patch.object(ralph.subprocess, "Popen", return_value=process) as launches, patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ), patch.object(
            ralph, "resolve_frontier_log_location", return_value=(self.repo, self.state_dir, self.state_dir / "logs" / "iteration-0001.log")
        ), patch.object(ralph, "_write_runtime_record", side_effect=fail_running_write), patch.object(
            ralph, "terminate_process_tree", side_effect=ralph.ProcessTreeError("cleanup ambiguous")
        ) as cleanup, self.assertRaises(ralph.ProcessTreeError):
            ralph.run_loop(self.repo, max_iterations=1, iteration_timeout=1, state_dir=self.state_dir)

        lock = self.state_dir / "ralph.lock"
        self.assertIsNone(process.poll(), "ambiguous cleanup leaves the started child unverified")
        self.assertEqual(
            {"controller_pid": os.getpid(), "root_pid": 54321, "launch_state": "cleanup_ambiguous"},
            json.loads(lock.read_text(encoding="utf-8")),
        )
        self.assertIn((None, "starting"), writes)
        self.assertEqual(25, sum(state == "running" for _, state in writes))
        cleanup.assert_called_once_with(process)
        self.assertEqual(1, launches.call_count)

        with patch.object(preflight, "pid_is_running", side_effect=lambda pid: False if pid == os.getpid() else True):
            compatible, _, code = preflight.runtime_lock_status(lock)
        self.assertFalse(compatible)
        self.assertEqual("AMBIGUOUS_SURVIVING_ROOT_PROCESS", code)

        second_launches: list[int] = []
        with patch.object(ralph, "_pid_is_running", side_effect=lambda pid: False if pid == os.getpid() else True), self.assertRaises(
            ralph.LockConflict
        ):
            ralph.run_loop(
                self.repo, max_iterations=1, state_dir=self.state_dir,
                execute_fn=lambda iteration, timeout: second_launches.append(iteration),
            )
        self.assertEqual([], second_launches)
        self.assertEqual(1, launches.call_count, "no second launch or name-based cleanup is permitted")

    def test_record_write_failure_terminates_started_child_before_propagating(self) -> None:
        self.state_dir.mkdir(parents=True)
        lock = self.state_dir / "ralph.lock"
        lock.write_text(json.dumps({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}), encoding="utf-8")
        process = FakeProcess(pid=54321)

        def verified_cleanup(owned: FakeProcess) -> None:
            owned.returncode = 0

        original_write = ralph._write_runtime_record

        def fail_running_write(
            lock_path: Path, controller_pid: int, root_pid: int | None, launch_state: str,
        ) -> None:
            if root_pid == process.pid and launch_state == "running":
                raise ralph.LockConflict("record write failed")
            original_write(lock_path, controller_pid, root_pid, launch_state)

        with patch.object(ralph.subprocess, "Popen", return_value=process), patch.object(
            ralph, "build_hermes_command", return_value=["hermes"]
        ), patch.object(
            ralph, "_write_runtime_record", side_effect=fail_running_write
        ), patch.object(ralph, "terminate_process_tree", side_effect=verified_cleanup) as cleanup, self.assertRaises(
            ralph.LockConflict
        ):
            ralph.hermes_executor(self.repo, self.state_dir, 1, 1, lock=lock)
        cleanup.assert_called_once_with(process)
        self.assertIsNotNone(process.poll())

    def test_iteration_log_is_bounded_during_capture_keeps_tail_and_does_not_deadlock(self) -> None:
        source = "import sys; sys.stdout.write('A' * 20000 + 'TAIL-MARKER\\n'); sys.stdout.flush()"
        with patch.object(ralph, "MAX_LOG_BYTES", 512), patch.object(
            ralph, "build_hermes_command", return_value=[sys.executable, "-c", source]
        ):
            log_path = ralph.hermes_executor(self.repo, self.state_dir, 1, 5)
        evidence = log_path.read_text(encoding="utf-8")
        self.assertLessEqual(log_path.stat().st_size, 512)
        self.assertIn(ralph.LOG_TRUNCATION_MARKER.strip(), evidence)
        self.assertIn("TAIL-MARKER", evidence)

    def test_iteration_log_materializes_flushed_output_before_child_exit(self) -> None:
        source = (
            "import sys, time; print('EARLY-EVIDENCE', flush=True); "
            "time.sleep(0.4); print('TAIL-EVIDENCE', flush=True)"
        )
        result: dict[str, object] = {}

        def execute() -> None:
            result["log_path"] = ralph.hermes_executor(self.repo, self.state_dir, 1, 5)

        with patch.object(ralph, "MAX_LOG_BYTES", 512), patch.object(
            ralph, "build_hermes_command", return_value=[sys.executable, "-c", source]
        ):
            worker = __import__("threading").Thread(target=execute)
            worker.start()
            log_path = self.state_dir / "logs" / "iteration-0001.log"
            deadline = __import__("time").monotonic() + 2
            while __import__("time").monotonic() < deadline:
                if log_path.exists() and "EARLY-EVIDENCE" in log_path.read_text(encoding="utf-8"):
                    break
                __import__("time").sleep(0.02)
            self.assertTrue(log_path.exists())
            self.assertTrue(worker.is_alive(), "early evidence must be visible before child exit")
            self.assertIn("EARLY-EVIDENCE", log_path.read_text(encoding="utf-8"))
            self.assertLessEqual(log_path.stat().st_size, 512)
            worker.join(timeout=2)
        self.assertFalse(worker.is_alive())
        self.assertIn("TAIL-EVIDENCE", Path(result["log_path"]).read_text(encoding="utf-8"))

    def test_nonzero_and_timeout_cite_usable_bounded_iteration_logs(self) -> None:
        nonzero = "import sys; sys.stdout.write('X' * 5000 + 'NONZERO-TAIL\\n'); sys.exit(7)"
        timeout = "import sys, time; print('TIMEOUT-TAIL', flush=True); time.sleep(10)"
        with patch.object(ralph, "MAX_LOG_BYTES", 512), patch.object(
            ralph, "build_hermes_command", return_value=[sys.executable, "-c", nonzero]
        ), self.assertRaises(ralph.HermesProcessError) as failed:
            ralph.hermes_executor(self.repo, self.state_dir, 1, 5)
        failed_log = Path(str(failed.exception).split("log: ", 1)[1])
        self.assertLessEqual(failed_log.stat().st_size, 512)
        self.assertIn("NONZERO-TAIL", failed_log.read_text(encoding="utf-8"))
        with patch.object(ralph, "MAX_LOG_BYTES", 512), patch.object(
            ralph, "build_hermes_command", return_value=[sys.executable, "-c", timeout]
        ), self.assertRaises(ralph.IterationTimeout) as timed_out:
            ralph.hermes_executor(self.repo, self.state_dir, 2, 0.05)
        timeout_log = Path(str(timed_out.exception).split("log: ", 1)[1])
        self.assertLessEqual(timeout_log.stat().st_size, 512)
        self.assertIn("TIMEOUT-TAIL", timeout_log.read_text(encoding="utf-8"))

    def test_exception_and_keyboard_interrupt_release_lock(self) -> None:
        for failure in (RuntimeError("boom"), KeyboardInterrupt()):
            with self.subTest(failure=type(failure).__name__):
                with self.assertRaises(type(failure)):
                    ralph.run_loop(
                        self.repo, max_iterations=1,
                        execute_fn=lambda iteration, timeout, exc=failure: (_ for _ in ()).throw(exc),
                        state_dir=self.state_dir,
                    )
                self.assertFalse((self.state_dir / "ralph.lock").exists())

    def test_strict_pause_returns_blocked_without_mutating_completion(self) -> None:
        completion = self.repo / ".scratch" / "ralph-loop" / "completion-signal.json"
        original = completion.read_bytes()
        self.write_pause({"isPaused": True})
        launches: list[int] = []
        outcome = ralph.run_loop(
            self.repo, max_iterations=1,
            execute_fn=lambda iteration, timeout: launches.append(iteration),
            state_dir=self.state_dir,
        )
        self.assertEqual(ralph.LoopOutcome.BLOCKED, outcome)
        self.assertEqual([], launches)
        self.assertEqual(original, completion.read_bytes())
        for text in ("[]", "{}", '{"isPaused": 1}', '{"isPaused": false, "extra": true}'):
            self.write_pause(text, raw=True)
            with self.subTest(invalid=text), self.assertRaises(ralph.PauseSignalError):
                ralph.read_pause_signal(self.repo)


class FrontierLogRoutingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.artifact = self.repo / ".scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/change-contract.md"
        self.artifact.parent.mkdir(parents=True)
        self.artifact.write_text("contract", encoding="utf-8")
        signals = self.repo / ".scratch" / "ralph-loop"
        signals.mkdir(parents=True, exist_ok=True)
        (signals / "completion-signal.json").write_text('{"isEverythingDone": false}', encoding="utf-8")
        (signals / "pause-signal.json").write_text('{"isPaused": false}', encoding="utf-8")

    def progress(
        self, artifact_path: str | None = None, *, issue_id: object = 2,
        kind: str = "contract-issue", returncode: int = 0, raw: str | None = None,
    ) -> subprocess.CompletedProcess[str]:
        payload = raw if raw is not None else json.dumps({
            "feature": {"slug": "greek-essence-showcase"}, "warnings": [],
            "frontier": {
                "kind": kind, "issueId": issue_id,
                "artifactPath": artifact_path or str(self.artifact.relative_to(self.repo)).replace("\\", "/"),
            },
        })
        return subprocess.CompletedProcess(["features-cli"], returncode, stdout=payload, stderr="")

    def test_issue_frontier_routes_to_exact_issue_Ralph_directory(self) -> None:
        owner, run_dir, log_path = ralph.resolve_frontier_log_location(
            self.repo, 1, "run-a", create=True,
            command_runner=lambda *_: self.progress(),
        )
        self.assertEqual(self.artifact.parent.resolve(), owner)
        self.assertEqual(owner / ".Ralph" / "runs" / "run-a", run_dir)
        self.assertEqual(run_dir / "iteration-0001.log", log_path)
        self.assertTrue(run_dir.is_dir())

    def test_two_controller_invocations_iteration_one_preserve_independent_logs(self) -> None:
        first_process = FakeProcess(returncode=0)
        second_process = FakeProcess(returncode=0)
        with patch.object(ralph, "_progress_command", return_value=self.progress()), patch.object(
            ralph.subprocess, "Popen", side_effect=[first_process, second_process]
        ):
            ralph.run_loop(self.repo, max_iterations=1, state_dir=self.repo / "state-one")
            first_log = next(self.artifact.parent.glob(".Ralph/runs/*/iteration-0001.log"))
            first_log.write_text("first evidence", encoding="utf-8")
            ralph.run_loop(self.repo, max_iterations=1, state_dir=self.repo / "state-two")
        logs = list(self.artifact.parent.glob(".Ralph/runs/*/iteration-0001.log"))
        self.assertEqual(2, len(logs))
        second_log = next(path for path in logs if path != first_log)
        second_log.write_text("second evidence", encoding="utf-8")
        self.assertEqual("first evidence", first_log.read_text(encoding="utf-8"))
        self.assertEqual("second evidence", second_log.read_text(encoding="utf-8"))

    def test_no_clobber_unique_run_directory_rejects_existing_run_id(self) -> None:
        ralph.resolve_frontier_log_location(self.repo, 1, "occupied", create=True, command_runner=lambda *_: self.progress())
        with self.assertRaises(ralph.FrontierRouteError):
            ralph.resolve_frontier_log_location(self.repo, 1, "occupied", create=True, command_runner=lambda *_: self.progress())

    def test_changed_frontier_owner_between_iterations_routes_each_log_to_its_owner(self) -> None:
        second_artifact = self.repo / ".scratch/features/001-greek-essence-showcase/issues/03-review-naxos/review.md"
        second_artifact.parent.mkdir(parents=True)
        second_artifact.write_text("review", encoding="utf-8")
        first = ralph.resolve_frontier_log_location(self.repo, 1, "campaign", create=True, command_runner=lambda *_: self.progress())
        second = ralph.resolve_frontier_log_location(
            self.repo, 2, "campaign", create=True,
            command_runner=lambda *_: self.progress(str(second_artifact.relative_to(self.repo)).replace("\\", "/"), issue_id=3),
        )
        self.assertEqual(self.artifact.parent.resolve(), first[0])
        self.assertEqual(second_artifact.parent.resolve(), second[0])
        self.assertNotEqual(first[1], second[1])

    def test_invalid_progress_never_creates_or_launches(self) -> None:
        invalid_cases = {
            "nonzero": lambda: self.progress(returncode=2),
            "duplicate": lambda: self.progress(raw='{"frontier":{"artifactPath":"x","artifactPath":"y"}}'),
            "absolute": lambda: self.progress("C:/outside.md"),
            "traversal": lambda: self.progress("../outside.md"),
            "outside": lambda: self.progress(".scratch/features/../../outside.md"),
            "missing-frontier": lambda: self.progress(raw=json.dumps({"feature": {"slug": "greek-essence-showcase"}, "warnings": []})),
        }
        for name, result in invalid_cases.items():
            with self.subTest(name=name), self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(self.repo, 1, f"bad-{name}", create=True, command_runner=lambda *_args, value=result: value())
        self.assertFalse(any(path.name == ".Ralph" for path in self.repo.rglob("*")))

    def test_dry_resolution_reports_owner_and_run_path_without_creating_directories(self) -> None:
        owner, run_dir, log_path = ralph.resolve_frontier_log_location(
            self.repo, 1, "dry-run", create=False, command_runner=lambda *_: self.progress(),
        )
        self.assertEqual(self.artifact.parent.resolve(), owner)
        self.assertEqual(owner / ".Ralph" / "runs" / "dry-run", run_dir)
        self.assertEqual(run_dir / "iteration-0001.log", log_path)
        self.assertFalse((owner / ".Ralph").exists())

    def test_same_owner_two_iterations_reuse_only_this_invocations_run_directory(self) -> None:
        first = FakeProcess(returncode=0)
        first.stdout = io.BytesIO(b"FIRST-ITERATION\n")
        second = FakeProcess(returncode=0)
        second.stdout = io.BytesIO(b"SECOND-ITERATION\n")
        with patch.object(ralph, "_progress_command", return_value=self.progress()), patch.object(
            ralph.subprocess, "Popen", side_effect=[first, second]
        ) as launches:
            outcome = ralph.run_loop(self.repo, max_iterations=2, state_dir=self.repo / "same-owner-state")
        self.assertEqual(ralph.LoopOutcome.LIMIT_REACHED, outcome)
        self.assertEqual(2, launches.call_count)
        runs = list(self.artifact.parent.glob(".Ralph/runs/*"))
        self.assertEqual(1, len(runs))
        self.assertEqual("FIRST-ITERATION\n", (runs[0] / "iteration-0001.log").read_text(encoding="utf-8"))
        self.assertEqual("SECOND-ITERATION\n", (runs[0] / "iteration-0002.log").read_text(encoding="utf-8"))

    def test_preexisting_run_directory_still_rejects_before_popen_or_new_artifact_creation(self) -> None:
        existing = self.artifact.parent / ".Ralph" / "runs" / "occupied"
        existing.mkdir(parents=True)
        with patch.object(ralph.uuid, "uuid4", return_value=type("RunId", (), {"hex": "occupied"})()), patch.object(
            ralph, "_progress_command", return_value=self.progress()
        ), patch.object(ralph.subprocess, "Popen") as launches, self.assertRaises(ralph.FrontierRouteError):
            ralph.run_loop(self.repo, max_iterations=1, state_dir=self.repo / "collision-state")
        self.assertEqual(0, launches.call_count)
        self.assertEqual([existing], list(self.artifact.parent.glob(".Ralph/runs/*")))

    def test_actual_artifactless_issue_shapes_route_consecutive_review_and_resume_iterations(self) -> None:
        def artifactless(kind: str) -> subprocess.CompletedProcess[str]:
            return subprocess.CompletedProcess(
                ["features-cli"], 0, stdout=json.dumps({
                    "feature": {"slug": "greek-essence-showcase"}, "warnings": [],
                    "frontier": {"kind": kind, "summary": f"{kind} issue 2.", "issueId": 2},
                }), stderr="",
            )

        review = FakeProcess(returncode=0)
        review.stdout = io.BytesIO(b"review\n")
        resumed = FakeProcess(returncode=0)
        resumed.stdout = io.BytesIO(b"resume\n")
        with patch.object(ralph, "_progress_command", side_effect=[artifactless("review-issue"), artifactless("implement-issue")]), patch.object(
            ralph.subprocess, "Popen", side_effect=[review, resumed]
        ) as launches:
            outcome = ralph.run_loop(self.repo, max_iterations=2, state_dir=self.repo / "artifactless-issues")
        self.assertEqual(ralph.LoopOutcome.LIMIT_REACHED, outcome)
        self.assertEqual(2, launches.call_count)
        runs = list(self.artifact.parent.glob(".Ralph/runs/*"))
        self.assertEqual(1, len(runs))
        self.assertEqual("review\n", (runs[0] / "iteration-0001.log").read_text(encoding="utf-8"))
        self.assertEqual("resume\n", (runs[0] / "iteration-0002.log").read_text(encoding="utf-8"))

    def test_decompose_milestone_SPEC_routes_to_feature_owner(self) -> None:
        feature = self.artifact.parents[2]
        (feature / "SPEC.md").write_text("spec", encoding="utf-8")
        payload = json.dumps({
            "feature": {"slug": "greek-essence-showcase"},
            "warnings": [],
            "frontier": {
                "kind": "decompose-milestone",
                "summary": "Decompose milestone complete-resilient-trip-request.",
                "milestoneSlug": "complete-resilient-trip-request",
                "artifactPath": "SPEC.md",
            },
        })

        owner, run_dir, log_path = ralph.resolve_frontier_log_location(
            self.repo, 1, "decompose-spec", create=False,
            command_runner=lambda *_: subprocess.CompletedProcess(
                ["features-cli"], 0, stdout=payload, stderr="",
            ),
        )

        self.assertEqual(feature.resolve(), owner)
        self.assertEqual(owner / ".Ralph" / "runs" / "decompose-spec", run_dir)
        self.assertEqual(run_dir / "iteration-0001.log", log_path)
        self.assertFalse((feature / ".Ralph").exists())

    def test_actual_artifactless_feature_shapes_dry_route_without_creation(self) -> None:
        feature = self.artifact.parents[2]
        for kind in ("design-ready", "feature-review", "blocked", "archived"):
            payload = json.dumps({
                "feature": {"slug": "greek-essence-showcase"}, "warnings": [],
                "frontier": {"kind": kind, "summary": f"{kind} exact stable shape"},
            })
            with self.subTest(kind=kind):
                owner, run_dir, _ = ralph.resolve_frontier_log_location(
                    self.repo, 1, f"dry-{kind}", create=False,
                    command_runner=lambda *_args, text=payload: subprocess.CompletedProcess(["features-cli"], 0, stdout=text),
                )
                self.assertEqual(feature.resolve(), owner)
                self.assertEqual(owner / ".Ralph" / "runs" / f"dry-{kind}", run_dir)
                self.assertFalse((feature / ".Ralph").exists())

    def test_artifactless_routes_reject_missing_or_ambiguous_or_unsafe_identity_before_creation(self) -> None:
        def payload(*, slug: object = "greek-essence-showcase", issue_id: object = 2,
                    artifact_path: str | None = None) -> str:
            frontier: dict[str, object] = {"kind": "review-issue", "summary": "Review issue 2.", "issueId": issue_id}
            if artifact_path is not None:
                frontier["artifactPath"] = artifact_path
            return json.dumps({"feature": {"slug": slug}, "warnings": [], "frontier": frontier})

        for name, text in (
            ("invalid-slug", payload(slug="../escape")),
            ("invalid-id", payload(issue_id=0)),
            ("inconsistent-artifact", payload(artifact_path=".scratch/features/001-greek-essence-showcase/issues/03-other/issue.md")),
        ):
            with self.subTest(name=name), self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(
                    self.repo, 1, f"reject-{name}", create=True,
                    command_runner=lambda *_args, raw=text: subprocess.CompletedProcess(["features-cli"], 0, stdout=raw),
                )
        moved = self.artifact.parent.with_name("04-other")
        self.artifact.parent.rename(moved)
        try:
            with self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(
                    self.repo, 1, "reject-zero", create=True,
                    command_runner=lambda *_args: subprocess.CompletedProcess(["features-cli"], 0, stdout=payload()),
                )
        finally:
            moved.rename(self.artifact.parent)
        duplicate = self.artifact.parent.with_name("02-duplicate")
        duplicate.mkdir()
        try:
            with self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(
                    self.repo, 1, "reject-multiple", create=True,
                    command_runner=lambda *_args: subprocess.CompletedProcess(["features-cli"], 0, stdout=payload()),
                )
        finally:
            duplicate.rmdir()
        self.assertFalse(any(path.name == ".Ralph" for path in self.repo.rglob("*")))

    def test_invalid_frontier_schema_never_creates_or_launches(self) -> None:
        prefix = {"feature": {"slug": "greek-essence-showcase"}, "warnings": []}
        cases = {
            "missing-kind": {**prefix, "frontier": {"issueId": 2, "artifactPath": str(self.artifact.relative_to(self.repo)).replace("\\", "/")}},
            "unknown-kind": {**prefix, "frontier": {"kind": "unknown", "issueId": 2, "artifactPath": str(self.artifact.relative_to(self.repo)).replace("\\", "/")}},
            "issue-without-id": {**prefix, "frontier": {"kind": "contract-issue", "artifactPath": str(self.artifact.relative_to(self.repo)).replace("\\", "/")}},
            "non-issue-with-id": {**prefix, "frontier": {"kind": "plan-milestones", "issueId": 2, "artifactPath": str(self.artifact.relative_to(self.repo)).replace("\\", "/")}},
            "duplicate-kind": '{"feature":{"slug":"greek-essence-showcase"},"warnings":[],"frontier":{"kind":"contract-issue","kind":"review-issue","issueId":2,"artifactPath":".scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/change-contract.md"}}',
        }
        for name, value in cases.items():
            raw = value if isinstance(value, str) else json.dumps(value)
            with self.subTest(name=name), patch.object(ralph, "_progress_command", return_value=self.progress(raw=raw)), patch.object(
                ralph.subprocess, "Popen"
            ) as launches, self.assertRaises(ralph.FrontierRouteError):
                ralph.run_loop(self.repo, max_iterations=1, state_dir=self.repo / f"invalid-{name}")
            self.assertEqual(0, launches.call_count)
            self.assertFalse((self.artifact.parent / ".Ralph").exists())

    @unittest.skipUnless(os.name == "nt", "Windows junction coverage")
    def test_windows_junctions_are_rejected_before_outside_creation(self) -> None:
        def junction(link: Path, target: Path) -> None:
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

        outside = Path(f"{self.temp.name}-outside")
        outside.mkdir()
        self.addCleanup(shutil.rmtree, outside, ignore_errors=True)
        linked_artifact_root = outside / "artifact-owner"
        linked_artifact_root.mkdir()
        (linked_artifact_root / "change-contract.md").write_text("outside", encoding="utf-8")
        artifact_link = self.repo / "artifact-link"
        junction(artifact_link, linked_artifact_root)
        with self.assertRaises(ralph.FrontierRouteError):
            ralph.resolve_frontier_log_location(
                self.repo, 1, "artifact-junction", create=True,
                command_runner=lambda *_: self.progress("artifact-link/change-contract.md"),
            )
        self.assertFalse((outside / ".Ralph").exists())

        linked_issues = outside / "issues"
        linked_owner = linked_issues / "02-owner"
        linked_owner.mkdir(parents=True)
        (linked_owner / "change-contract.md").write_text("outside", encoding="utf-8")
        owner_link_root = self.repo / "owner-link"
        owner_link_root.mkdir()
        junction(owner_link_root / "issues", linked_issues)
        try:
            with self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(
                    self.repo, 1, "owner-junction", create=True,
                    command_runner=lambda *_: self.progress("owner-link/issues/02-owner/change-contract.md"),
                )
            self.assertFalse((linked_owner / ".Ralph").exists())
        finally:
            os.rmdir(owner_link_root / "issues")

        owner = self.artifact.parent
        ralph_link = owner / ".Ralph"
        junction(ralph_link, outside)
        try:
            with self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(self.repo, 1, "ralph-junction", create=True, command_runner=lambda *_: self.progress())
            self.assertFalse((outside / "runs" / "ralph-junction").exists())
        finally:
            os.rmdir(ralph_link)

        runs_root = owner / ".Ralph"
        runs_root.mkdir()
        runs_link = runs_root / "runs"
        junction(runs_link, outside)
        try:
            with self.assertRaises(ralph.FrontierRouteError):
                ralph.resolve_frontier_log_location(self.repo, 1, "runs-junction", create=True, command_runner=lambda *_: self.progress())
            self.assertFalse((outside / "runs-junction").exists())
        finally:
            os.rmdir(runs_link)


if __name__ == "__main__":
    unittest.main(verbosity=2)
