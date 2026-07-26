from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PROFILES = ROOT / ".scratch" / "ralph-loop" / "profiles"
FILES = {
    "orchestrator": PROFILES / "jzgreekorch-SOUL.md",
    "implementer": PROFILES / "jzgreekimpl-SOUL.md",
    "reviewer": PROFILES / "jzgreekrev-SOUL.md",
    "visual_reviewer": PROFILES / "jzgreekvisualrev-SOUL.md",
    "readme": PROFILES / "README.md",
}
SCENARIO_FIXTURE = ROOT / ".scratch" / "ralph-loop" / "tests" / "fixtures" / "jz_orchestrator_scenarios.json"


def scenarios() -> list[dict[str, object]]:
    fixture = json.loads(SCENARIO_FIXTURE.read_text(encoding="utf-8"))
    return fixture["scenarios"]


def text(name: str) -> str:
    return FILES[name].read_text(encoding="utf-8")


class JzRoleContractTests(unittest.TestCase):
    def test_all_four_named_profile_contracts_are_tracked(self) -> None:
        for name, path in FILES.items():
            with self.subTest(name=name):
                self.assertTrue(path.is_file(), path)
        readme = text("readme")
        for profile in ("jzgreekorch", "jzgreekimpl", "jzgreekrev", "jzgreekvisualrev"):
            self.assertIn(f"`{profile}`", readme)

    def test_orchestrator_reads_authority_handoff_and_knowledge(self) -> None:
        contract = text("orchestrator")
        for required in (
            "AGENTS.md",
            "NEXT.md",
            ".scratch/features/001-greek-essence-showcase/AGENTS.md",
            ".scratch/ralph-loop/RALPH_LOOP.md",
            ".scratch/ralph-loop/HANDOFF.md",
            ".scratch/ralph-loop/KNOWLEDGE.md",
        ):
            self.assertIn(required, contract)

    def test_orchestrator_runs_stable_cli_commands_at_start_and_end(self) -> None:
        contract = text("orchestrator")
        docs = "features-cli docs current --feature greek-essence-showcase"
        progress = "features-cli progress --feature greek-essence-showcase --json"
        self.assertGreaterEqual(contract.count(docs), 2)
        self.assertGreaterEqual(contract.count(progress), 2)
        self.assertIn("iteration start", contract.lower())
        self.assertIn("iteration end", contract.lower())

    def test_cli_frontier_is_authoritative_and_iteration_has_one_action_boundary(self) -> None:
        contract = text("orchestrator").lower()
        self.assertIn("cli frontier is authoritative", contract)
        self.assertIn("reconcile stale `next.md` or `handoff.md`", contract)
        self.assertIn("exactly one frontier action", contract)
        self.assertIn("never start the successor frontier action", contract)

    def test_orchestrator_loads_live_jz_skill_and_delegates_fresh_roles(self) -> None:
        contract = text("orchestrator")
        self.assertIn("Recommended skill", contract)
        self.assertIn("load its `SKILL.md` and every reference it identifies as required", contract)
        for profile in ("jzgreekimpl", "jzgreekrev", "jzgreekvisualrev"):
            self.assertRegex(contract, rf"fresh[^\n]*`{profile}`")

    def test_tdd_topology_is_explicit(self) -> None:
        contract = text("orchestrator")
        self.assertIn("`tdd-solo`", contract)
        self.assertIn("one fresh `jzgreekimpl` session owns RED → GREEN", contract)
        self.assertIn("`tdd-ping-pong`", contract)
        self.assertIn("two separate fresh `jzgreekimpl` sessions", contract)
        self.assertIn("RED session", contract)
        self.assertIn("GREEN session", contract)

    def test_all_roles_strictly_respect_resolved_engineering_depth(self) -> None:
        for role in ("orchestrator", "implementer", "reviewer", "visual_reviewer"):
            contract = text(role)
            with self.subTest(role=role):
                self.assertIn("Engineering-depth discipline", contract)
                self.assertIn("Tier 2 — Prototype", contract)
                self.assertIn("direct operator instruction", contract)
                self.assertIn("implementation_depth", contract)
                self.assertRegex(contract, r"(?i)never (?:promote or demote|raise or lower)")
                self.assertRegex(contract, r"(?i)(effort|review) proportion")
                self.assertRegex(contract, r"(?i)stop")

        orchestrator = text("orchestrator")
        self.assertIn("Include the resolved tier in every child brief", orchestrator)
        self.assertIn("All delegated work inherits it", orchestrator)
        self.assertIn("effort, breadth, defensive depth, test breadth, and time spent", orchestrator)

        implementer = text("implementer")
        self.assertIn("smallest maintainable working solution", implementer)
        self.assertIn("Stop when the prototype works", implementer)

        reviewer = text("reviewer")
        self.assertIn("higher-tier improvements in non-blocking suggestions", reviewer)
        visual = text("visual_reviewer")
        self.assertIn("optional refinements as non-blocking", visual)

    def test_profiles_override_conflicting_generic_skills_and_calibrate_tier_two(self) -> None:
        for role in ("orchestrator", "implementer", "reviewer", "visual_reviewer"):
            contract = text(role)
            with self.subTest(role=role):
                self.assertIn("Profile authority and prototype calibration", contract)
                self.assertRegex(contract, r"(?i)profile.*priority|priority.*profile")
                self.assertIn("make it work without embarrassing yourself", contract)

        self.assertIn("record Tier-3/4 requests as non-blocking", text("orchestrator"))
        self.assertIn("Low-impact edge cases may be documented instead of fixed", text("implementer"))
        self.assertIn("Review the working prototype, not an imagined perfect product", text("reviewer"))
        self.assertIn("Do not demand every viewport", text("visual_reviewer"))

    def test_practicality_policy_has_exact_non_waivable_safeguards(self) -> None:
        contract = text("orchestrator")
        for classification in (
            "Material regression → repair",
            "Invalid/stale/flaky evidence → bounded diagnosis",
            "Understood low-impact exception",
        ):
            self.assertIn(classification, contract)
        for safeguard in (
            "security",
            "privacy",
            "accessibility",
            "data integrity",
            "accepted user behavior",
            "core bilingual parity",
            "unusable builds",
            "unsupported claims",
        ):
            self.assertRegex(contract, rf"(?is)non-waivable.*{re.escape(safeguard)}")
        self.assertIn("exact failure, evidence, impact, and bounded attempts", contract)
        self.assertIn("Never report a failed command as passing", contract)

    def test_orchestrator_exit_completion_pause_and_email_rules_are_bounded(self) -> None:
        contract = text("orchestrator")
        self.assertIn("before every normal exit", contract)
        self.assertIn("KNOWLEDGE.md` only for durable", contract)
        self.assertIn("Email only after verified full-feature completion or a genuine human-required blocker", contract)
        self.assertIn("completion-signal.json` true only", contract)
        self.assertIn("pause-signal.json` true only", contract)
        self.assertIn("keep completion false", contract)
        self.assertIn("ordinary implementation, gate, or in-contract review failure is not a blocker", contract)

    def test_worker_role_boundaries_and_evidence_are_explicit(self) -> None:
        implementer = text("implementer")
        for phase in ("RED-only", "GREEN-only", "RED → GREEN"):
            self.assertIn(phase, implementer)
        self.assertIn("preserve all existing review evidence", implementer)
        self.assertIn("exact commands, exit codes, and result counts", implementer)
        self.assertIn("Never self-review", implementer)
        self.assertIn("select the next frontier", implementer)

        reviewer = text("reviewer")
        self.assertIn("independent", reviewer.lower())
        self.assertIn("new immutable", reviewer)
        self.assertIn("Never repair", reviewer)

        visual = text("visual_reviewer")
        self.assertIn("playwright-cli", visual)
        self.assertIn("vision inspection", visual)
        self.assertIn("English and Greek", visual)
        self.assertIn("390 × 844", visual)
        self.assertIn("1440 × 1024", visual)
        self.assertIn("new immutable", visual)
        self.assertIn("Never repair", visual)

    def test_practicality_scenarios_define_all_ten_deterministic_transitions(self) -> None:
        expected_ids = {
            "locale-parity-material",
            "accessibility-affected-surface",
            "sensitive-failure-not-repairable",
            "stale-contract-conflicting-test",
            "windows-environmental-failure",
            "marginal-non-contract-metric",
            "in-contract-review-failure",
            "genuine-credential-requirement",
            "frontier-advance-after-implementation",
            "frontier-advance-after-review",
        }
        fixture_scenarios = scenarios()
        self.assertEqual({scenario["id"] for scenario in fixture_scenarios}, expected_ids)
        for scenario in fixture_scenarios:
            with self.subTest(scenario=scenario["id"]):
                transition = scenario["transition"]
                self.assertEqual(transition[-1], "stop")
                self.assertTrue(scenario["required_clauses"])
                self.assertIsInstance(scenario["forbidden"], list)

    def test_practicality_scenarios_bind_transitions_to_orchestrator_invariants(self) -> None:
        contract = text("orchestrator")
        for scenario in scenarios():
            with self.subTest(scenario=scenario["id"]):
                for clause in scenario["required_clauses"]:
                    self.assertIn(clause, contract)

        by_id = {scenario["id"]: scenario for scenario in scenarios()}
        self.assertEqual(
            by_id["locale-parity-material"]["transition"],
            ["failure", "repair", "verify", "frontier-check", "stop"],
        )
        self.assertEqual(
            by_id["accessibility-affected-surface"]["transition"],
            ["failure", "repair", "verify", "frontier-check", "stop"],
        )
        self.assertEqual(
            by_id["sensitive-failure-not-repairable"]["transition"],
            ["failure", "bounded-recovery", "pause-escalate", "handoff", "email", "stop"],
        )
        self.assertEqual(
            by_id["genuine-credential-requirement"]["transition"],
            ["failure", "handoff", "email", "pause", "completion-false", "stop"],
        )
        for scenario_id in ("frontier-advance-after-implementation", "frontier-advance-after-review"):
            self.assertEqual(
                by_id[scenario_id]["transition"][-2:],
                ["end-check", "stop"],
            )

    def test_contracts_contain_no_stale_bootstrap_ids_roles_or_model_names(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in FILES.values())
        for stale_role in ("greekroot", "greekimpl", "greekreview"):
            self.assertIsNone(re.search(rf"(?<![A-Za-z0-9]){stale_role}(?![A-Za-z0-9])", combined))
        self.assertIsNone(re.search(r"\bB\d{2}(?:-\d{2})?\b", combined))
        self.assertIsNone(re.search(r"\bgpt-[A-Za-z0-9.-]+\b", combined, re.IGNORECASE))
        for stale_model in ("Sol/low", "Luna/high", "Terra/high"):
            self.assertNotIn(stale_model, combined)


if __name__ == "__main__":
    unittest.main()
