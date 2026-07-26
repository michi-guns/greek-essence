#!/usr/bin/env python3
"""Run bounded fresh Greek Essence Ralph orchestrator iterations."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import subprocess
import sys
import threading
import time
import uuid
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Callable

sys.dont_write_bytecode = True

ROOT_PROFILE = "jzgreekorch"
DEFAULT_MAX_ITERATIONS = 100
DEFAULT_ITERATION_TIMEOUT = 3 * 60 * 60
COMPLETION_SIGNAL = Path(".scratch/ralph-loop/completion-signal.json")
PAUSE_SIGNAL = Path(".scratch/ralph-loop/pause-signal.json")
MAX_LOG_BYTES = 2 * 1024 * 1024
LOG_TRUNCATION_MARKER = "\n[ralph iteration output truncated; retained tail follows]\n"


class RalphError(RuntimeError):
    """Base class for mechanical controller failures."""


class CompletionSignalError(RalphError):
    pass


class PauseSignalError(RalphError):
    pass


class HermesProcessError(RalphError):
    pass


class IterationTimeout(RalphError):
    pass


class LockConflict(RalphError):
    pass


class ProcessTreeError(RalphError):
    pass


class FrontierRouteError(RalphError):
    pass


class LoopOutcome(str, Enum):
    COMPLETE = "COMPLETE"
    BLOCKED = "BLOCKED"
    LIMIT_REACHED = "LIMIT_REACHED"


class LifecycleLogger:
    """Best-effort JSONL containing only bounded mechanical metadata."""

    def __init__(self, path: Path) -> None:
        self.path = path
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

    def emit(self, event: str, **fields: object) -> None:
        payload = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "event": event,
            **fields,
        }
        try:
            if self.path.exists() and self.path.stat().st_size >= MAX_LOG_BYTES:
                return
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        except (OSError, TypeError, ValueError):
            pass


def default_state_dir() -> Path:
    base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    return base / "hermes" / "ralph" / "greek-essence"


def _strict_json(text: str) -> object:
    def pairs(values: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in values:
            if key in result:
                raise ValueError(f"duplicate property: {key}")
            result[key] = value
        return result

    try:
        return json.loads(text, object_pairs_hook=pairs)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc


def _read_signal(repo: Path, relative: Path, key: str, error_type: type[RalphError]) -> bool:
    path = repo.resolve() / relative
    try:
        payload = _strict_json(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise error_type(f"Invalid signal {path}: {exc}") from exc
    if not isinstance(payload, dict) or set(payload) != {key} or type(payload[key]) is not bool:
        raise error_type(f"Signal {path} must contain exactly one Boolean property: {key}")
    return payload[key]


def read_completion_signal(repo: Path) -> bool:
    return _read_signal(repo, COMPLETION_SIGNAL, "isEverythingDone", CompletionSignalError)


def read_pause_signal(repo: Path) -> bool:
    return _read_signal(repo, PAUSE_SIGNAL, "isPaused", PauseSignalError)


def root_prompt() -> str:
    return """You are the fresh Greek Essence JZ workflow orchestrator. Read AGENTS.md, NEXT.md, .scratch/features/001-greek-essence-showcase/AGENTS.md, .scratch/ralph-loop/RALPH_LOOP.md, .scratch/ralph-loop/HANDOFF.md, and .scratch/ralph-loop/KNOWLEDGE.md. Query the live features-cli frontier at the start and end. Complete exactly one frontier action, including required delegation, repair, verification, and review, update HANDOFF.md, then stop. Never begin the successor frontier action in this iteration. Set completion true only when the entire campaign is proven complete; set pause true only for a genuine human-required blocker while completion remains false."""


def build_hermes_command(repo: Path, iteration: int) -> list[str]:
    del repo, iteration
    return [
        "hermes", "-p", ROOT_PROFILE, "chat", "-Q", "--yolo",
        "--pass-session-id", "--source", "ralph", "-q", root_prompt(),
    ]


def _pid_is_running(pid: int) -> bool | None:
    """Return None when process liveness cannot be established safely."""
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


RUNTIME_LAUNCH_STATES = {"idle", "starting", "running", "cleanup_ambiguous"}


def _read_runtime_record(lock: Path) -> dict[str, int | str | None]:
    try:
        payload = _strict_json(lock.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise LockConflict(f"Ralph loop has an unreadable ownership record: {lock}") from exc
    root_pid = payload.get("root_pid") if isinstance(payload, dict) else None
    launch_state = payload.get("launch_state") if isinstance(payload, dict) else None
    valid_root = root_pid is None or (type(root_pid) is int and root_pid > 0)
    valid_state = launch_state in RUNTIME_LAUNCH_STATES
    state_matches_root = (
        (launch_state in {"idle", "starting"} and root_pid is None)
        or (launch_state in {"running", "cleanup_ambiguous"} and type(root_pid) is int and root_pid > 0)
    )
    if (not isinstance(payload, dict) or set(payload) != {"controller_pid", "root_pid", "launch_state"}
            or type(payload.get("controller_pid")) is not int or payload["controller_pid"] <= 0
            or not valid_root or not valid_state or not state_matches_root):
        raise LockConflict(f"Ralph loop has an invalid ownership record: {lock}")
    return {
        "controller_pid": payload["controller_pid"], "root_pid": root_pid,
        "launch_state": launch_state,
    }


def _write_runtime_record(lock: Path, controller_pid: int, root_pid: int | None, launch_state: str) -> None:
    if (controller_pid <= 0 or launch_state not in RUNTIME_LAUNCH_STATES
            or (launch_state in {"idle", "starting"} and root_pid is not None)
            or (launch_state in {"running", "cleanup_ambiguous"}
                and (type(root_pid) is not int or root_pid <= 0))):
        raise LockConflict("Ralph loop cannot write an invalid ownership record")
    replacement = lock.with_suffix(".next")
    try:
        replacement.write_text(
            json.dumps({
                "controller_pid": controller_pid, "root_pid": root_pid,
                "launch_state": launch_state,
            }), encoding="utf-8"
        )
        os.replace(replacement, lock)
    except OSError as exc:
        replacement.unlink(missing_ok=True)
        raise LockConflict(f"Ralph loop cannot update ownership record: {lock}") from exc


def _acquire_lock(state_dir: Path, lifecycle: LifecycleLogger | None = None) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    lock = state_dir / "ralph.lock"
    for attempt in range(2):
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError as exc:
            record = _read_runtime_record(lock)
            controller_state = _pid_is_running(record["controller_pid"])
            if controller_state is True:
                raise LockConflict(f"Ralph loop is already locked by controller PID {record['controller_pid']}: {lock}") from exc
            if controller_state is None:
                raise LockConflict(f"Ralph loop controller ownership is ambiguous: {lock}") from exc
            launch_state = record["launch_state"]
            if launch_state != "idle":
                root_pid = record["root_pid"]
                if root_pid is not None:
                    root_state = _pid_is_running(root_pid)
                    if root_state is True:
                        raise LockConflict(f"Ralph loop has a surviving root PID {root_pid}; recovery is unsafe: {lock}") from exc
                    if root_state is None:
                        raise LockConflict(f"Ralph loop root ownership is ambiguous for PID {root_pid}: {lock}") from exc
                raise LockConflict(
                    f"Ralph loop has unresolved launch state {launch_state!r}; recovery is unsafe: {lock}"
                ) from exc
            if attempt:
                raise LockConflict(f"Ralph loop could not acquire lock: {lock}") from exc
            if lifecycle:
                lifecycle.emit("stale_lock_remove_start", controller_pid=record["controller_pid"])
            lock.unlink()
            if lifecycle:
                lifecycle.emit("stale_lock_remove_complete", controller_pid=record["controller_pid"])
    else:
        raise LockConflict(f"Ralph loop could not acquire lock: {lock}")
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        json.dump({"controller_pid": os.getpid(), "root_pid": None, "launch_state": "idle"}, handle)
    return lock


def terminate_process_tree(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    if os.name == "nt":
        pid = getattr(process, "pid", None)
        if not isinstance(pid, int) or pid <= 0:
            raise ProcessTreeError("Owned Windows process PID is unavailable; cleanup is ambiguous")
        try:
            result = subprocess.run(
                ["taskkill", "/PID", str(pid), "/T", "/F"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                timeout=10, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ProcessTreeError(f"Owned process tree cleanup for PID {pid} is ambiguous: {exc}") from exc
        if result.returncode != 0:
            raise ProcessTreeError(f"Owned process tree for PID {pid} may still be running: {result.stdout.strip()}")
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired as exc:
            raise ProcessTreeError(f"Owned process tree for PID {pid} survived taskkill") from exc
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def _iteration_log(state_dir: Path, iteration: int) -> Path:
    logs = state_dir / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    return logs / f"iteration-{iteration:04d}.log"


def _progress_command(repo: Path) -> subprocess.CompletedProcess[str]:
    executable = shutil.which("features-cli")
    if not executable:
        return subprocess.CompletedProcess(["features-cli"], 126, stdout="features-cli is unavailable")
    return subprocess.run(
        [executable, "progress", "--feature", "greek-essence-showcase", "--json"],
        cwd=repo, text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )


ISSUE_FRONTIER_KINDS = frozenset({"contract-issue", "implement-issue", "review-issue"})
NON_ISSUE_FRONTIER_KINDS = frozenset({
    "migration-required", "write-prd", "grill-and-consolidate-decisions", "design-ready",
    "write-spec", "plan-milestones", "decompose-milestone", "blocked", "feature-review", "archived",
})


def _is_reparse_point(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise FrontierRouteError(f"cannot inspect frontier path component: {path}") from exc
    return path.is_symlink() or bool(
        getattr(metadata, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    )


def _reject_reparse_components(root: Path, parts: tuple[str, ...], label: str) -> None:
    if _is_reparse_point(root):
        raise FrontierRouteError(f"{label} must not use a reparse-point repository root")
    current = root
    for part in parts:
        current /= part
        if _is_reparse_point(current):
            raise FrontierRouteError(f"{label} must not resolve through a symlink, junction, or reparse point")


def _require_contained_destination(repo: Path, owner: Path, destination: Path) -> None:
    try:
        canonical_repo = repo.resolve(strict=True)
        canonical_owner = owner.resolve(strict=True)
        canonical_destination = destination.resolve(strict=False)
        canonical_owner.relative_to(canonical_repo)
        canonical_destination.relative_to(canonical_owner)
    except (OSError, RuntimeError, ValueError) as exc:
        raise FrontierRouteError("frontier log destination escapes its contained owner") from exc


def _validate_log_chain(repo: Path, owner: Path, run_dir: Path) -> None:
    ralph_dir = owner / ".Ralph"
    runs_dir = ralph_dir / "runs"
    for path in (owner, ralph_dir, runs_dir, run_dir):
        if _is_reparse_point(path):
            raise FrontierRouteError("frontier log path must not use a symlink, junction, or reparse point")
        if path.exists() and not path.is_dir():
            raise FrontierRouteError(f"frontier log path component must be a directory: {path}")
        _require_contained_destination(repo, owner, path)


ARTIFACT_OPTIONAL_FRONTIER_KINDS = frozenset({
    "implement-issue", "review-issue", "design-ready", "feature-review", "blocked", "archived",
})
FEATURE_SLUG = "greek-essence-showcase"


def _contained_feature_owner(repo: Path, slug: str) -> Path:
    if slug != FEATURE_SLUG:
        raise FrontierRouteError("features-cli progress did not identify greek-essence-showcase")
    features_root = repo / ".scratch" / "features"
    _reject_reparse_components(repo, (".scratch", "features"), "feature workspace")
    candidates = list(features_root.glob(f"*-{slug}")) if features_root.is_dir() else []
    owners: list[Path] = []
    for candidate in candidates:
        _reject_reparse_components(repo, candidate.relative_to(repo).parts, "feature workspace")
        if candidate.is_dir() and not _is_reparse_point(candidate):
            _require_contained_destination(repo, candidate, candidate)
            owners.append(candidate)
    if len(owners) != 1:
        raise FrontierRouteError("frontier feature slug must resolve to exactly one contained feature directory")
    return owners[0]


def _contained_issue_owner(repo: Path, feature_owner: Path, issue_id: int) -> Path:
    issues_root = feature_owner / "issues"
    _reject_reparse_components(repo, issues_root.relative_to(repo).parts, "issue workspace")
    candidates = list(issues_root.glob(f"{issue_id:02d}-*")) if issues_root.is_dir() else []
    owners: list[Path] = []
    for candidate in candidates:
        _reject_reparse_components(repo, candidate.relative_to(repo).parts, "issue workspace")
        if candidate.is_dir() and not _is_reparse_point(candidate):
            _require_contained_destination(repo, candidate, candidate)
            owners.append(candidate)
    if len(owners) != 1:
        raise FrontierRouteError("issue frontier must resolve to exactly one contained issue directory")
    return owners[0]


def _contained_artifact(repo: Path, artifact_path: object) -> Path:
    if not isinstance(artifact_path, str) or not artifact_path or "\\" in artifact_path:
        raise FrontierRouteError("frontier artifactPath must be a non-empty relative POSIX path")
    pure_path = PurePosixPath(artifact_path)
    windows_path = PureWindowsPath(artifact_path)
    if pure_path.is_absolute() or windows_path.is_absolute() or windows_path.drive or any(part in {"", ".", ".."} for part in pure_path.parts):
        raise FrontierRouteError("frontier artifactPath must not be absolute or traverse directories")
    _reject_reparse_components(repo, pure_path.parts, "frontier artifactPath")
    artifact = repo.joinpath(*pure_path.parts)
    _require_contained_destination(repo, repo, artifact)
    return artifact


def _frontier_artifact_owner(repo: Path, output: str) -> Path:
    try:
        payload = _strict_json(output)
    except ValueError as exc:
        raise FrontierRouteError(f"features-cli progress returned invalid JSON: {exc}") from exc
    feature = payload.get("feature") if isinstance(payload, dict) else None
    frontier = payload.get("frontier") if isinstance(payload, dict) else None
    slug = feature.get("slug") if isinstance(feature, dict) else None
    if not isinstance(slug, str):
        raise FrontierRouteError("features-cli progress did not identify greek-essence-showcase")
    if payload.get("warnings") != [] or not isinstance(frontier, dict):
        raise FrontierRouteError("features-cli progress has warnings or no frontier object")
    kind = frontier.get("kind")
    if not isinstance(kind, str) or kind not in ISSUE_FRONTIER_KINDS | NON_ISSUE_FRONTIER_KINDS:
        raise FrontierRouteError("frontier kind must be a known routable kind")
    feature_owner = _contained_feature_owner(repo, slug)
    issue_id = frontier.get("issueId")
    if kind in ISSUE_FRONTIER_KINDS:
        if type(issue_id) is not int or issue_id <= 0:
            raise FrontierRouteError("issue frontier kind requires a positive issueId")
        owner = _contained_issue_owner(repo, feature_owner, issue_id)
    else:
        if "issueId" in frontier:
            raise FrontierRouteError("non-issue frontier kind must not include issueId")
        owner = feature_owner
    artifact_path = frontier.get("artifactPath")
    if artifact_path is None:
        if kind not in ARTIFACT_OPTIONAL_FRONTIER_KINDS:
            raise FrontierRouteError("frontier artifactPath is required for this frontier kind")
    else:
        if kind == "decompose-milestone" and artifact_path == "SPEC.md":
            artifact = owner / artifact_path
            _reject_reparse_components(
                repo, artifact.relative_to(repo).parts, "frontier artifactPath",
            )
            _require_contained_destination(repo, owner, artifact)
        else:
            artifact = _contained_artifact(repo, artifact_path)
            _require_contained_destination(repo, owner, artifact)
    if not owner.is_dir() or _is_reparse_point(owner):
        raise FrontierRouteError("frontier log owner must be a contained regular directory")
    return owner


def resolve_frontier_log_location(
    repo: Path, iteration: int, run_id: str, *, create: bool,
    command_runner: Callable[[Path], subprocess.CompletedProcess[str]] | None = None,
    invocation_run_dirs: set[Path] | None = None,
) -> tuple[Path, Path, Path]:
    if iteration <= 0 or not run_id or not run_id.replace("-", "").replace("_", "").isalnum():
        raise FrontierRouteError("iteration and run identifier are invalid")
    repo = repo.resolve()
    result = (command_runner or _progress_command)(repo)
    if result.returncode != 0:
        raise FrontierRouteError(f"features-cli progress failed with exit {result.returncode}")
    owner = _frontier_artifact_owner(repo, result.stdout)
    run_dir = owner / ".Ralph" / "runs" / run_id
    if create:
        _validate_log_chain(repo, owner, run_dir)
        established = invocation_run_dirs is not None and run_dir in invocation_run_dirs
        if established:
            if not run_dir.is_dir():
                raise FrontierRouteError(f"Ralph invocation run directory is unavailable: {run_dir}")
        else:
            try:
                run_dir.mkdir(parents=True, exist_ok=False)
            except FileExistsError as exc:
                raise FrontierRouteError(f"Ralph run directory already exists: {run_dir}") from exc
            except OSError as exc:
                raise FrontierRouteError(f"Ralph run directory cannot be created: {run_dir}") from exc
            if invocation_run_dirs is not None:
                invocation_run_dirs.add(run_dir)
        _validate_log_chain(repo, owner, run_dir)
    return owner, run_dir, run_dir / f"iteration-{iteration:04d}.log"


class _BoundedIterationCapture:
    """Continuously materialize one bounded diagnostic tail while draining output."""

    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        self.tail = bytearray()
        self.total = 0
        self.truncated = False
        self.log_path.write_bytes(b"")

    def _materialize(self) -> None:
        marker = LOG_TRUNCATION_MARKER.encode("utf-8") if self.truncated else b""
        marker = marker[:MAX_LOG_BYTES]
        tail_limit = max(0, MAX_LOG_BYTES - len(marker))
        self.log_path.write_bytes(marker + self.tail[-tail_limit:])

    def append(self, chunk: bytes) -> None:
        self.total += len(chunk)
        if not self.truncated and self.total <= MAX_LOG_BYTES:
            self.tail.extend(chunk)
            self._materialize()
            return
        self.truncated = True
        tail_limit = max(0, MAX_LOG_BYTES - len(LOG_TRUNCATION_MARKER.encode("utf-8")))
        self.tail.extend(chunk)
        if len(self.tail) > tail_limit:
            del self.tail[:-tail_limit]
        self._materialize()

    def finalize(self) -> None:
        self._materialize()


def hermes_executor(
    repo: Path, state_dir: Path, iteration: int, timeout: float | None,
    *, lifecycle: LifecycleLogger | None = None, lock: Path | None = None,
    log_path: Path | None = None,
) -> Path:
    timeout = DEFAULT_ITERATION_TIMEOUT if timeout is None else timeout
    log_path = log_path or _iteration_log(state_dir, iteration)
    capture = _BoundedIterationCapture(log_path)
    if lock is not None:
        _write_runtime_record(lock, os.getpid(), None, "starting")
    process = subprocess.Popen(
        build_hermes_command(repo, iteration), cwd=repo, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, text=False,
    )
    if lock is not None:
        recorded = False
        for attempt in range(25):
            try:
                _write_runtime_record(lock, os.getpid(), process.pid, "running")
                recorded = True
                break
            except LockConflict:
                if attempt < 24:
                    time.sleep(0.25)
        if not recorded:
            try:
                terminate_process_tree(process)
                if process.poll() is None:
                    raise ProcessTreeError(f"Started process root {process.pid} exit could not be verified")
            except BaseException as cleanup_exc:
                try:
                    _write_runtime_record(lock, os.getpid(), process.pid, "cleanup_ambiguous")
                except BaseException as evidence_exc:
                    if lifecycle:
                        lifecycle.emit("cleanup_ambiguous", iteration=iteration, root_pid=process.pid,
                                       error=f"{cleanup_exc}; ownership evidence failed: {evidence_exc}")
                    raise ProcessTreeError(
                        f"Started process root {process.pid} could not be durably recorded or safely cleaned up"
                    ) from evidence_exc
                if lifecycle:
                    lifecycle.emit("cleanup_ambiguous", iteration=iteration, root_pid=process.pid, error=str(cleanup_exc))
                raise ProcessTreeError(
                    f"Started process root {process.pid} could not be durably recorded or safely cleaned up"
                ) from cleanup_exc
            _write_runtime_record(lock, os.getpid(), None, "idle")
            raise LockConflict(f"Started process root {process.pid} could not be durably recorded")
    if lifecycle:
        lifecycle.emit("root_started", iteration=iteration, root_pid=process.pid, log_path=str(log_path))

    def drain() -> None:
        if process.stdout is None:
            return
        reader = getattr(process.stdout, "read1", process.stdout.read)
        while chunk := reader(64 * 1024):
            capture.append(chunk)

    reader = threading.Thread(target=drain, daemon=True)
    reader.start()
    verified_exit = False
    try:
        code = process.wait(timeout=timeout)
        verified_exit = True
    except subprocess.TimeoutExpired as exc:
        try:
            terminate_process_tree(process)
            verified_exit = process.poll() is not None
            if not verified_exit:
                raise ProcessTreeError(f"Owned process root {process.pid} exit could not be verified")
        except BaseException as cleanup_exc:
            if lifecycle:
                lifecycle.emit("cleanup_ambiguous", iteration=iteration, root_pid=process.pid, error=str(cleanup_exc))
            exc.add_note(f"owned tree cleanup failed: {type(cleanup_exc).__name__}: {cleanup_exc}")
            raise
        raise IterationTimeout(f"Ralph iteration {iteration} timed out; log: {log_path}") from exc
    except BaseException as exc:
        if process.poll() is None:
            try:
                terminate_process_tree(process)
                verified_exit = process.poll() is not None
            except BaseException as cleanup_exc:
                if lifecycle:
                    lifecycle.emit("cleanup_ambiguous", iteration=iteration, root_pid=process.pid, error=str(cleanup_exc))
                exc.add_note(f"owned tree cleanup failed: {type(cleanup_exc).__name__}: {cleanup_exc}")
                raise
        raise
    finally:
        reader.join(timeout=5)
        if process.stdout is not None:
            process.stdout.close()
        capture.finalize()
        if verified_exit and lock is not None:
            _write_runtime_record(lock, os.getpid(), None, "idle")
        if lifecycle and verified_exit:
            lifecycle.emit("root_exited", iteration=iteration, root_pid=process.pid, log_path=str(log_path))
    if code != 0:
        raise HermesProcessError(f"Hermes iteration {iteration} exited {code}; log: {log_path}")
    return log_path


def run_loop(
    repo: Path,
    *,
    max_iterations: int = DEFAULT_MAX_ITERATIONS,
    iteration_timeout: float | None = DEFAULT_ITERATION_TIMEOUT,
    read_signal_fn: Callable[[Path], bool] | None = None,
    execute_fn: Callable[[int, float | None], object] | None = None,
    state_dir: Path | None = None,
) -> LoopOutcome:
    if max_iterations < 0:
        raise ValueError("max_iterations must be zero or greater")
    if iteration_timeout is not None and iteration_timeout <= 0:
        raise ValueError("iteration_timeout must be greater than zero")
    repo = repo.resolve()
    state_dir = (state_dir or default_state_dir()).resolve()
    completion = read_signal_fn or read_completion_signal
    lifecycle = LifecycleLogger(state_dir / "logs" / f"controller-lifecycle-{os.getpid()}.jsonl")
    run_id = uuid.uuid4().hex
    invocation_run_dirs: set[Path] = set()
    lock: Path | None = None
    try:
        lock = _acquire_lock(state_dir, lifecycle)
        lifecycle.emit("controller_start", controller_pid=os.getpid(), max_iterations=max_iterations)
        for iteration in range(1, max_iterations + 1):
            if completion(repo):
                return LoopOutcome.COMPLETE
            if read_pause_signal(repo):
                return LoopOutcome.BLOCKED
            lifecycle.emit("iteration_start", iteration=iteration)
            if execute_fn:
                execute_fn(iteration, iteration_timeout)
            else:
                _, _, log_path = resolve_frontier_log_location(
                    repo, iteration, run_id, create=True, invocation_run_dirs=invocation_run_dirs,
                )
                hermes_executor(repo, state_dir, iteration, iteration_timeout, lifecycle=lifecycle, lock=lock, log_path=log_path)
            lifecycle.emit("iteration_complete", iteration=iteration)
        if completion(repo):
            return LoopOutcome.COMPLETE
        if read_pause_signal(repo):
            return LoopOutcome.BLOCKED
        return LoopOutcome.LIMIT_REACHED
    finally:
        if lock is not None:
            try:
                record = _read_runtime_record(lock)
            except LockConflict:
                lifecycle.emit("ownership_record_preserved", controller_pid=os.getpid())
            else:
                if record["launch_state"] == "idle":
                    lock.unlink(missing_ok=True)
                else:
                    lifecycle.emit(
                        "ownership_record_preserved", controller_pid=os.getpid(),
                        root_pid=record["root_pid"], launch_state=record["launch_state"],
                    )
        lifecycle.emit("controller_exit", controller_pid=os.getpid())


def _print_error(outcome: str, error: BaseException) -> None:
    print(json.dumps({"outcome": outcome, "error": str(error)}, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--max-iterations", type=int, default=DEFAULT_MAX_ITERATIONS)
    parser.add_argument("--iteration-timeout", type=float, default=DEFAULT_ITERATION_TIMEOUT)
    parser.add_argument("--state-dir", type=Path, default=default_state_dir())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.dry_run:
            repo = args.repo.resolve()
            run_id = uuid.uuid4().hex
            owner, run_dir, log_path = resolve_frontier_log_location(repo, 1, run_id, create=False)
            print(json.dumps({
                "repo": str(repo),
                "completion_signal": {"isEverythingDone": read_completion_signal(repo)},
                "pause_signal": {"isPaused": read_pause_signal(repo)},
                "profile": ROOT_PROFILE,
                "command": build_hermes_command(repo, 1),
                "iteration_timeout": args.iteration_timeout,
                "max_iterations": args.max_iterations,
                "log_owner": str(owner),
                "log_run_directory": str(run_dir),
                "iteration_log": str(log_path),
                "launch_performed": False,
            }, indent=2, ensure_ascii=False))
            return 0
        outcome = run_loop(
            args.repo, max_iterations=args.max_iterations,
            iteration_timeout=args.iteration_timeout, state_dir=args.state_dir,
        )
        print(json.dumps({"outcome": outcome.value}, indent=2))
        return 0 if outcome is LoopOutcome.COMPLETE else 2
    except (CompletionSignalError, PauseSignalError) as exc:
        _print_error("INVALID_SIGNAL", exc); return 3
    except HermesProcessError as exc:
        _print_error("HERMES_FAILED", exc); return 4
    except IterationTimeout as exc:
        _print_error("TIMEOUT", exc); return 5
    except LockConflict as exc:
        _print_error("LOCK_CONFLICT", exc); return 6
    except ProcessTreeError as exc:
        _print_error("ERROR", exc); return 7
    except KeyboardInterrupt as exc:
        _print_error("INTERRUPTED", exc); return 130
    except Exception as exc:
        _print_error("ERROR", exc); return 1


if __name__ == "__main__":
    sys.exit(main())
