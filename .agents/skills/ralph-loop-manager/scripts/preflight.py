#!/usr/bin/env python3
"""Read-only mechanical launch preflight for the Greek Essence Ralph controller."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from email.utils import parseaddr
from pathlib import Path
from typing import Any

FEATURE = "greek-essence-showcase"
FEATURES_CLI_VERSION = "0.3.0"
PNPM_VERSION = "11.17.0"
REQUIRED_PROFILES = ("jzgreekorch", "jzgreekimpl", "jzgreekrev", "jzgreekvisualrev")
ISSUE_FRONTIER_KINDS = frozenset({"contract-issue", "implement-issue", "review-issue"})
NON_ISSUE_FRONTIER_KINDS = frozenset({
    "migration-required", "write-prd", "grill-and-consolidate-decisions", "design-ready",
    "write-spec", "plan-milestones", "decompose-milestone", "blocked", "feature-review", "archived",
})
ARTIFACT_OPTIONAL_FRONTIER_KINDS = frozenset({
    "implement-issue", "review-issue", "design-ready", "feature-review", "blocked", "archived",
})
REQUIRED_FILES = (
    ".scratch/ralph-loop/tools/ralph_loop.py",
    ".scratch/ralph-loop/RALPH_LOOP.md",
    ".scratch/ralph-loop/completion-signal.json",
    ".scratch/ralph-loop/pause-signal.json",
)
OWNED_REPOSITORY = Path(__file__).resolve().parents[4]


def run(command: list[str], cwd: Path, timeout: float = 20) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace",
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as exc:
        captured = exc.stdout if isinstance(exc.stdout, str) else ""
        return subprocess.CompletedProcess(command, 124, stdout=f"{captured}\nTimed out after {timeout} seconds".strip())
    except OSError as exc:
        return subprocess.CompletedProcess(command, 126, stdout=f"Could not start command: {type(exc).__name__}: {exc}")


def pid_is_running(pid: int) -> bool | None:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except (OSError, SystemError):
        return None
    return True


def runtime_lock_status(lock: Path) -> tuple[bool, str, str | None]:
    """Return launch compatibility without mutating controller ownership evidence."""
    if not lock.exists():
        return True, f"absent: {lock}", None

    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for name, value in pairs:
            if name in result:
                raise ValueError(f"duplicate property: {name}")
            result[name] = value
        return result

    try:
        payload = json.loads(lock.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return False, str(exc), "INVALID_RUNTIME_OWNERSHIP_RECORD"
    root_pid = payload.get("root_pid") if isinstance(payload, dict) else None
    launch_state = payload.get("launch_state") if isinstance(payload, dict) else None
    valid_root = root_pid is None or (type(root_pid) is int and root_pid > 0)
    valid_state = launch_state in {"idle", "starting", "running", "cleanup_ambiguous"}
    state_matches_root = (
        (launch_state in {"idle", "starting"} and root_pid is None)
        or (launch_state in {"running", "cleanup_ambiguous"} and type(root_pid) is int and root_pid > 0)
    )
    if (not isinstance(payload, dict) or set(payload) != {"controller_pid", "root_pid", "launch_state"}
            or type(payload.get("controller_pid")) is not int or payload["controller_pid"] <= 0
            or not valid_root or not valid_state or not state_matches_root):
        return False, "strict controller/root/launch-state ownership record required", "INVALID_RUNTIME_OWNERSHIP_RECORD"
    controller = pid_is_running(payload["controller_pid"])
    if controller is True:
        return False, f"controller_pid={payload['controller_pid']}; active=true", "ACTIVE_CONTROLLER_LOCK"
    if controller is None:
        return False, f"controller_pid={payload['controller_pid']}; active=unknown", "AMBIGUOUS_SURVIVING_ROOT_PROCESS"
    if launch_state != "idle":
        root = pid_is_running(root_pid) if root_pid is not None else None
        state = "true" if root is True else "false" if root is False else "unknown"
        return False, (
            f"dead_controller; launch_state={launch_state}; root_pid={root_pid}; active={state}"
        ), "AMBIGUOUS_SURVIVING_ROOT_PROCESS"
    return True, f"stale controller_pid={payload['controller_pid']}; root_pid=none; launch_state=idle", None


def is_contained_regular_file(path: Path, root: Path) -> bool:
    try:
        resolved = path.resolve(strict=True)
        canonical_root = root.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError):
        return False
    return path.is_file() and not path.is_symlink()


def exact_signal(path: Path, key: str) -> bool:
    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for name, value in pairs:
            if name in result:
                raise ValueError(f"duplicate property: {name}")
            result[name] = value
        return result

    payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    if not isinstance(payload, dict) or set(payload) != {key} or type(payload[key]) is not bool:
        raise ValueError(f"must contain exactly one Boolean property: {key}")
    return payload[key]


def validate_progress(text: str) -> tuple[bool, str]:
    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for name, value in pairs:
            if name in result:
                raise ValueError(f"duplicate property: {name}")
            result[name] = value
        return result

    try:
        payload = json.loads(text, object_pairs_hook=reject_duplicates)
    except (json.JSONDecodeError, ValueError) as exc:
        return False, f"invalid JSON: {exc}"
    if not isinstance(payload, dict):
        return False, "progress is not an object"
    feature = payload.get("feature")
    warnings = payload.get("warnings")
    frontier = payload.get("frontier")
    slug = feature.get("slug") if isinstance(feature, dict) else None
    if slug != FEATURE:
        return False, f"feature={slug!r}"
    if warnings != []:
        return False, f"warnings={warnings!r}"
    if not isinstance(frontier, dict):
        return False, "frontier is not an object"
    kind = frontier.get("kind")
    if not isinstance(kind, str) or kind not in ISSUE_FRONTIER_KINDS | NON_ISSUE_FRONTIER_KINDS:
        return False, "frontier kind is missing or unknown"
    artifact_path = frontier.get("artifactPath")
    if artifact_path is None:
        if kind not in ARTIFACT_OPTIONAL_FRONTIER_KINDS:
            return False, "frontier artifactPath is required for this frontier kind"
    elif not isinstance(artifact_path, str) or not artifact_path:
        return False, "frontier artifactPath is missing or invalid"
    issue_id = frontier.get("issueId")
    if kind in ISSUE_FRONTIER_KINDS:
        if type(issue_id) is not int or issue_id <= 0:
            return False, "issue frontier kind requires a positive issueId"
    elif "issueId" in frontier:
        return False, "non-issue frontier kind must not include issueId"
    return True, kind


def validate_dry_run_route(text: str) -> tuple[bool, str]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return False, f"invalid JSON: {exc}"
    if not isinstance(payload, dict) or payload.get("launch_performed") is not False:
        return False, "dry-run did not prove no launch"
    owner = payload.get("log_owner")
    run_dir = payload.get("log_run_directory")
    log_path = payload.get("iteration_log")
    if not all(isinstance(value, str) and value for value in (owner, run_dir, log_path)):
        return False, "dry-run did not report a resolved frontier log route"
    return True, f"owner={owner}; run_dir={run_dir}; log={log_path}"


def email_skill_candidates(_repo: Path) -> list[Path]:
    local = os.environ.get("LOCALAPPDATA")
    if not local:
        return []
    base = Path(local) / "hermes" / "skills"
    return [base / "email" / "email-notification", base / "email-notification"]


def validate_email_environment() -> tuple[bool, list[str]]:
    problems: list[str] = []
    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    sender = os.environ.get("RESEND_FROM_EMAIL", "").strip()
    if not api_key:
        problems.append("RESEND_API_KEY missing")
    elif not api_key.startswith("re_") or len(api_key) < 10 or any(char.isspace() for char in api_key):
        problems.append("RESEND_API_KEY has an invalid shape")
    if not sender:
        problems.append("RESEND_FROM_EMAIL missing")
    else:
        _, address = parseaddr(sender)
        domain = address.rpartition("@")[2].lower()
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", address) or domain in {
            "example.com", "example.org", "example.net"
        } or domain.endswith((".invalid", ".test")):
            problems.append("RESEND_FROM_EMAIL is malformed or a placeholder")
    return not problems, problems


def add_check(checks: list[dict[str, Any]], name: str, ok: bool, evidence: str) -> None:
    checks.append({"name": name, "ok": ok, "evidence": evidence})


def stop(hard_stops: list[dict[str, str]], code: str, problem: str, remediation: str) -> None:
    hard_stops.append({"code": code, "problem": problem, "remediation": remediation})


def emit(repo: Path, checks: list[dict[str, Any]], warnings: list[dict[str, str]],
         hard_stops: list[dict[str, str]]) -> int:
    print(json.dumps({
        "status": "HARD_STOP" if hard_stops else "PASS",
        "repository": str(repo), "feature": FEATURE, "checks": checks,
        "warnings": warnings, "hard_stops": hard_stops, "launch_performed": False,
    }, indent=2, ensure_ascii=False))
    return 2 if hard_stops else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--target", required=True)
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    checks: list[dict[str, Any]] = []
    warnings: list[dict[str, str]] = []
    hard_stops: list[dict[str, str]] = []

    if not repo.is_dir():
        stop(hard_stops, "REPOSITORY_DIRECTORY_MISSING", f"Repository is missing: {repo}", "Pass the canonical repository root.")
        return emit(repo, checks, warnings, hard_stops)
    if repo != OWNED_REPOSITORY or args.target != FEATURE:
        stop(hard_stops, "PROJECT_SCOPE_MISMATCH", "Preflight is project- and feature-specific.",
             f"Use --repo {OWNED_REPOSITORY} --target {FEATURE}.")
        return emit(repo, checks, warnings, hard_stops)

    git = shutil.which("git")
    git_probe = run(["git", "rev-parse", "--show-toplevel"], repo) if git else None
    git_ok = bool(git and git_probe and git_probe.returncode == 0 and Path(git_probe.stdout.strip()).resolve() == repo)
    add_check(checks, "git", git_ok, git_probe.stdout.strip() if git_probe else "missing")
    if not git_ok:
        stop(hard_stops, "GIT_OR_ROOT_INVALID", "Git or the canonical Git root is unavailable.", "Repair Git and run at the repository root.")

    bad_files = [name for name in REQUIRED_FILES if not is_contained_regular_file(repo / name, repo)]
    add_check(checks, "required-files", not bad_files, "invalid=" + json.dumps(bad_files))
    if bad_files:
        stop(hard_stops, "REQUIRED_FILES_INVALID", "Required controller, protocol, or signal files are unsafe or missing.", "Restore contained regular files.")

    python_ok = sys.version_info >= (3, 11)
    add_check(checks, "python", python_ok, sys.version.split()[0])
    if not python_ok:
        stop(hard_stops, "PYTHON_UNSUPPORTED", "Python 3.11+ is required.", "Use Python 3.11 or newer.")

    for command in ("hermes", "bun", "pnpm"):
        executable = shutil.which(command)
        probe = run([executable, "--version"], repo) if executable else None
        available = bool(probe and probe.returncode == 0)
        version = probe.stdout.strip() if probe else "missing"
        name = command
        ok = available
        if command == "pnpm":
            ok = available and version == PNPM_VERSION

        add_check(checks, name, ok, version)
        if not ok:
            stop(hard_stops, f"{command.upper().replace('-', '_')}_UNAVAILABLE", f"Required {command} version is unavailable.", "Install or expose the required stable command.")

    features_cli = shutil.which("features-cli")
    pnpm = shutil.which("pnpm")
    installed = run([pnpm, "list", "-g", "--depth", "0", "--json"], repo) if pnpm else None
    stable_version = None
    if installed and installed.returncode == 0:
        try:
            listings = json.loads(installed.stdout)
            stable_version = listings[0]["dependencies"]["@jz/ai-arsenal-features-cli"]["version"]
        except (json.JSONDecodeError, KeyError, IndexError, TypeError):
            pass
    stable_ok = bool(features_cli and stable_version == FEATURES_CLI_VERSION)
    add_check(checks, "features-cli-stable", stable_ok, str(stable_version or "missing"))
    if not stable_ok:
        stop(hard_stops, "FEATURES_CLI_UNAVAILABLE", "Stable features-cli 0.3.0 is unavailable.", "Install the stable global package and expose its launcher.")

    docs = run([features_cli, "docs", "current", "--feature", FEATURE], repo) if features_cli else None
    docs_ok = bool(docs and docs.returncode == 0)
    add_check(checks, "features-docs-current", docs_ok, f"exit={docs.returncode}" if docs else "not run")
    if not docs_ok:
        stop(hard_stops, "FEATURE_DOCS_FAILED", "features-cli docs current failed.", "Repair stable features-cli or feature state.")

    progress = run([features_cli, "progress", "--feature", FEATURE, "--json"], repo) if features_cli else None
    progress_ok, progress_evidence = validate_progress(progress.stdout) if progress and progress.returncode == 0 else (False, "command failed")
    add_check(checks, "features-progress", progress_ok, progress_evidence)
    if not progress_ok:
        stop(hard_stops, "FEATURE_PROGRESS_INVALID", "Feature progress is unavailable, wrong-feature, or has warnings.", "Repair feature state before launch.")

    missing_profiles: list[str] = []
    hermes = shutil.which("hermes")
    if hermes:
        for profile in REQUIRED_PROFILES:
            shown = run([hermes, "profile", "show", profile], repo)
            if shown.returncode != 0:
                missing_profiles.append(profile)
    else:
        missing_profiles = list(REQUIRED_PROFILES)
    add_check(checks, "profiles", not missing_profiles, "missing=" + json.dumps(missing_profiles))
    if missing_profiles:
        stop(hard_stops, "PROFILES_MISSING", "Required Hermes profiles are missing: " + ", ".join(missing_profiles), "Create the four role profiles before launch.")

    state_base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    lock = state_base / "hermes" / "ralph" / "greek-essence" / "ralph.lock"
    lock_ok, evidence, lock_code = runtime_lock_status(lock)
    add_check(checks, "runtime-lock", lock_ok, evidence)
    if not lock_ok:
        code = lock_code or "INVALID_RUNTIME_OWNERSHIP_RECORD"
        stop(hard_stops, code, "Controller ownership cannot be proven safe for another launch.",
             "Preserve the ownership record and inspect the controller/root process; do not launch another.")

    for relative, key, name in ((REQUIRED_FILES[2], "isEverythingDone", "completion-signal"),
                                (REQUIRED_FILES[3], "isPaused", "pause-signal")):
        try:
            value = exact_signal(repo / relative, key)
            compatible = value is False
            add_check(checks, name, compatible, f"{key}={str(value).lower()}")
            if not compatible:
                code = "COMPLETION_NOT_LAUNCH_COMPATIBLE" if key == "isEverythingDone" else "PAUSE_NOT_LAUNCH_COMPATIBLE"
                stop(hard_stops, code, f"{key} must be false for a live launch.", "Use only the documented authorized activation/resume procedure.")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            add_check(checks, name, False, str(exc))
            stop(hard_stops, "INVALID_SIGNAL", f"Invalid {name}: {exc}", "Restore the exact Boolean schema.")

    email_dir = next((candidate for candidate in email_skill_candidates(repo) if (candidate / "SKILL.md").is_file()), None)
    email_script = email_dir / "scripts" / "send_notification.py" if email_dir else None
    env_ok, env_problems = validate_email_environment()
    help_probe = run([sys.executable, str(email_script), "--help"], repo) if email_script and email_script.is_file() else None
    email_ok = bool(help_probe and help_probe.returncode == 0 and "--dry-run" in help_probe.stdout and env_ok)
    add_check(checks, "email-readiness", email_ok,
              f"skill={email_dir or 'missing'}; script={bool(email_script and email_script.is_file())}; dry_run_supported={bool(help_probe and '--dry-run' in help_probe.stdout)}; environment_problems={json.dumps(env_problems)}")
    if not email_ok:
        stop(hard_stops, "EMAIL_NOT_READY", "Email skill, script, dry-run interface, or environment shape is not ready.", "Prepare notification support; the manager must run the intended-recipient dry-run before activation.")

    if git_ok:
        status = run(["git", "status", "--porcelain=v1", "--untracked-files=all"], repo)
        observed = status.returncode == 0
        dirty = observed and bool(status.stdout.strip())
        add_check(checks, "worktree-observed", observed, status.stdout.strip() or "clean")
        if not observed:
            stop(hard_stops, "WORKTREE_STATUS_FAILED", "Git worktree status is not observable.", "Repair Git access before launch.")
        elif dirty:
            warnings.append({"code": "DIRTY_WORKTREE", "message": "Worktree changes observed for manager attribution before launch."})

    controller = repo / REQUIRED_FILES[0]
    if is_contained_regular_file(controller, repo):
        dry = run([sys.executable, str(controller), "--repo", str(repo), "--dry-run"], repo)
        dry_ok = dry.returncode == 0
        add_check(checks, "controller-dry-run", dry_ok, f"exit={dry.returncode}; output={dry.stdout.strip()[:1000]}")
        if not dry_ok:
            stop(hard_stops, "CONTROLLER_DRY_RUN_FAILED", "Controller dry-run failed.", "Repair the mechanical controller before launch.")
        route_ok, route_evidence = validate_dry_run_route(dry.stdout) if dry_ok else (False, "controller dry-run failed")
        add_check(checks, "frontier-log-route", route_ok, route_evidence)
        if not route_ok:
            stop(hard_stops, "FRONTIER_LOG_ROUTE_INVALID", "Controller dry-run did not prove a safe frontier log route.", "Repair features-cli progress output or the controller route validation before launch.")

    return emit(repo, checks, warnings, hard_stops)


if __name__ == "__main__":
    raise SystemExit(main())
