from __future__ import annotations

import io
import json
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


class ThinLoopAcceptanceTests(unittest.TestCase):
    def make_repo(self, root: Path) -> None:
        signals = root / ".scratch" / "ralph-loop"
        signals.mkdir(parents=True)
        (signals / "completion-signal.json").write_text(
            '{"isEverythingDone": false}', encoding="utf-8"
        )
        (signals / "pause-signal.json").write_text(
            '{"isPaused": false}', encoding="utf-8"
        )

    def test_dry_run_reports_resolved_mechanics_and_never_launches(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            self.make_repo(repo)
            output = io.StringIO()
            feature = repo / ".scratch" / "features" / "001-greek-essence-showcase"
            artifact = feature / "SPEC.md"
            artifact.parent.mkdir(parents=True)
            artifact.write_text("frontier", encoding="utf-8")
            progress = subprocess.CompletedProcess(
                ["features-cli"], 0,
                stdout=json.dumps({
                    "feature": {"slug": "greek-essence-showcase"}, "warnings": [],
                    "frontier": {"kind": "plan-milestones", "artifactPath": str(artifact.relative_to(repo)).replace("\\", "/")},
                }),
            )
            with patch.object(
                ralph.subprocess, "Popen", side_effect=AssertionError("dry-run launched Hermes")
            ), patch.object(ralph, "_progress_command", return_value=progress), redirect_stdout(output):
                code = ralph.main(["--repo", str(repo), "--dry-run"])
        self.assertEqual(0, code)
        payload = json.loads(output.getvalue())
        self.assertEqual(str(repo.resolve()), payload["repo"])
        self.assertEqual({"isEverythingDone": False}, payload["completion_signal"])
        self.assertEqual({"isPaused": False}, payload["pause_signal"])
        self.assertEqual("jzgreekorch", payload["profile"])
        self.assertEqual(["hermes", "-p", "jzgreekorch"], payload["command"][:3])
        self.assertGreater(payload["iteration_timeout"], 0)
        self.assertEqual(100, payload["max_iterations"])
        self.assertEqual(str(feature.resolve()), payload["log_owner"])
        self.assertTrue(payload["log_run_directory"].endswith(".Ralph\\runs\\" + Path(payload["log_run_directory"]).name))
        self.assertTrue(payload["iteration_log"].endswith("iteration-0001.log"))
        self.assertFalse((repo / ".Ralph").exists())
        self.assertIs(False, payload["launch_performed"])

    def test_controller_exposes_no_semantic_state_or_profile_overrides(self) -> None:
        forbidden_api = (
            "ControllerState", "CampaignIdentity", "TransitionResult", "Diagnosis",
            "save_controller_state", "load_controller_state", "transition_campaign_state",
            "run_readonly_assessor", "health_prompt", "diagnosis_prompt", "build_retry_prompt",
            "ROOT_MODEL", "ROOT_PROVIDER", "ASSESSOR_PROFILE", "ASSESSOR_MODEL",
        )
        for name in forbidden_api:
            with self.subTest(name=name):
                self.assertFalse(hasattr(ralph, name), f"legacy semantic controller API remains: {name}")

        source = Path(ralph.__file__).read_text(encoding="utf-8")
        for forbidden_text in (
            "controller-state.json", "campaign_id", "task_id", "assessor",
            "diagnosis", "transition_campaign", "--campaign-id", "--task-id",
            "--resolved-tier", "-m\", ROOT_MODEL", "--provider",
        ):
            with self.subTest(text=forbidden_text):
                self.assertNotIn(forbidden_text, source)

        command = ralph.build_hermes_command(Path("C:/fixture"), 1)
        for forbidden_flag in ("-m", "--model", "--provider", "--resume"):
            self.assertNotIn(forbidden_flag, command)


if __name__ == "__main__":
    unittest.main(verbosity=2)
