from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
HESSIAN = VALIDATED / "hessian"
PRECISION = HESSIAN / "precision.manifest.json"
TAIL = HESSIAN / "tailH.manifest.json"
CHECKPOINT = HESSIAN / "remaining_hessian_job.checkpoint.json"
OUTPUT = HESSIAN / "remaining_hessian_job.exit.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRemainingHessianJobExit_v1.md"

QUEUE = ROOT / "scripts" / "run_q79_height4_affine_basis_precision_queue.py"
PRECISION_BUILDER = ROOT / "scripts" / "run_q79_height4_precision_hessian_queue.py"
TAIL_BUILDER = ROOT / "scripts" / "run_q79_height4_tail_hessian_queue.py"
PRECISION_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79heightfourprecisionhessianmanifest_audit.py"
)
TAIL_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79heightfouralltargettailhessianinterval_audit.py"
)
EXIT_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79heightfourremaininghessianjobexit_audit.py"
)
A373 = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # The validated-transport root is close to Windows' legacy MAX_PATH limit.
    # Keep the sibling temporary name short while retaining atomic replacement.
    temporary = path.parent / ".job.tmp"
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_status() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.splitlines()


def run(*arguments: object) -> None:
    rendered = [str(value) for value in arguments]
    print("$ " + " ".join(rendered), flush=True)
    subprocess.run(rendered, cwd=ROOT, check=True)


def manifest_state() -> dict:
    packet = load(PRECISION)
    pending = [
        int(row["distinguished_index"])
        for row in packet["targets"]
        if not row.get("full_budget_pass", False)
    ]
    return {
        "sha256": sha256(PRECISION),
        "status": packet["status"],
        "full_budget_count": int(packet["counts"]["full_budget"]),
        "current_main_count": int(packet["counts"]["main_certificates_current"]),
        "current_tail_count": int(packet["counts"]["tail_certificates_current"]),
        "remaining_count": int(packet["remaining_full_budget_count"]),
        "pending_indices": pending,
    }


def checkpoint(phase: str, initial: dict, **extra: object) -> None:
    atomic_dump(
        CHECKPOINT,
        {
            "schema": "MTTQ79HeightFourRemainingHessianJobCheckpoint.v1",
            "phase": phase,
            "updated_at_utc": now(),
            "initial_manifest": initial,
            "current_manifest": manifest_state(),
            **extra,
        },
    )
    print(f"checkpoint phase={phase} path={relative(CHECKPOINT)}", flush=True)


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--indices", type=int, nargs="+")
    value.add_argument("--dps", type=int, default=150)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--stage-steps", type=int, default=40)
    value.add_argument("--maximum-stages", type=int, default=24)
    return value


def main() -> int:
    arguments = parser().parse_args()
    initial = manifest_state()
    initial_git_head = git_head()
    initial_git_status = git_status()
    selected = arguments.indices or initial["pending_indices"]
    if not selected and initial["full_budget_count"] != 76:
        raise AssertionError("manifest has no pending list but is not complete")
    checkpoint(
        "starting",
        initial,
        selected_indices=selected,
        git_head=initial_git_head,
        git_dirty_entry_count=len(initial_git_status),
    )

    queue_arguments: list[object] = [
        sys.executable,
        QUEUE,
        "--dps",
        arguments.dps,
        "--order",
        arguments.order,
        "--stage-steps",
        arguments.stage_steps,
        "--maximum-stages",
        arguments.maximum_stages,
        "--keep-going",
    ]
    if selected:
        queue_arguments.extend(["--indices", *selected])
    checkpoint("running_target_queue", initial, selected_indices=selected)
    run(*queue_arguments)

    checkpoint("refreshing_aggregate_manifests", initial, selected_indices=selected)
    run(sys.executable, TAIL_BUILDER, "--manifest-only")
    run(sys.executable, PRECISION_BUILDER, "--manifest-only")

    final = manifest_state()
    if (
        final["status"] != "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED"
        or final["full_budget_count"] != 76
        or final["current_main_count"] != 76
        or final["current_tail_count"] != 76
        or final["remaining_count"] != 0
        or final["pending_indices"]
    ):
        checkpoint("strict_manifest_gate_failed", initial, selected_indices=selected)
        raise AssertionError(f"strict 76-target gate failed: {final}")

    checkpoint("running_nested_audits", initial, selected_indices=selected)
    run(sys.executable, TAIL_AUDIT)
    run(sys.executable, PRECISION_AUDIT)

    NOTE.write_text(
        "# MTT q79 Height-Four Remaining Hessian Job Exit v1\n\n"
        "This execution certificate records completion of the strict A380-A382 "
        "target-Hessian queue from the controlling precision manifest. All 76 "
        "coefficient-weighted full budgets, main certificates, and tail "
        "certificates pass their dedicated nested audits.\n\n"
        "This is a numerical execution certificate. It does not prove A384 "
        "residual-Jacobian nonsingularity, an A385 Krawczyk zero, a physical "
        "observable map, or Standard Model closure.\n",
        encoding="utf-8",
    )
    environment = {
        "python": sys.version,
        "platform": platform.platform(),
    }
    try:
        import flint

        environment["python_flint"] = getattr(flint, "__version__", "unknown")
    except Exception as error:
        environment["python_flint"] = f"unavailable: {type(error).__name__}"

    payload = {
        "schema": "MTTQ79HeightFourRemainingHessianJobExit.v1",
        "status": "ALL_76_STRICT_TARGET_HESSIAN_BUDGETS_VERIFIED",
        "artifact": "JOBEXIT.Q79.HEIGHT4.HESSIAN76",
        "completed_at_utc": now(),
        "selected_indices_at_job_start": selected,
        "initial_manifest": initial,
        "final_manifest": final,
        "environment": environment,
        "git": {
            "head_before": initial_git_head,
            "head_after": git_head(),
            "dirty_entry_count_before": len(initial_git_status),
            "dirty_entry_count_after": len(git_status()),
        },
        "authority": {
            "A373_target_inventory": authority(A373),
            "A231_integer_chain": authority(A231),
            "affine_queue_runner": authority(QUEUE),
            "tail_manifest_builder": authority(TAIL_BUILDER),
            "precision_manifest_builder": authority(PRECISION_BUILDER),
            "tail_manifest": authority(TAIL),
            "precision_manifest": authority(PRECISION),
            "tail_nested_audit": authority(TAIL_AUDIT),
            "precision_nested_audit": authority(PRECISION_AUDIT),
            "exit_packet_audit": authority(EXIT_AUDIT),
            "job_wrapper": authority(Path(__file__).resolve()),
            "theorem_note": authority(NOTE),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_full_target_Hessian_budgets_closed": True,
            "all_76_main_certificates_current": True,
            "all_76_tail_certificates_current": True,
            "nested_tail_audit_passed": True,
            "nested_precision_audit_passed": True,
            "process_success_is_not_ledger_promotion": True,
            "A384_residual_Jacobian_nonsingularity_closed": False,
            "A385_interval_Newton_or_Krawczyk_zero_closed": False,
            "physical_observable_map_closed": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "build and independently audit A384 from the same completed 76-target "
            "precision manifest"
        ),
    }
    atomic_dump(OUTPUT, payload)
    checkpoint("running_exit_packet_audit", initial, selected_indices=selected)
    run(sys.executable, EXIT_AUDIT)
    checkpoint(
        "complete",
        initial,
        selected_indices=selected,
        exit_packet={"path": relative(OUTPUT), "sha256": sha256(OUTPUT)},
    )
    print(json.dumps(payload["final_manifest"], indent=2), flush=True)
    print(f"exit_packet={relative(OUTPUT)} sha256={sha256(OUTPUT)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
