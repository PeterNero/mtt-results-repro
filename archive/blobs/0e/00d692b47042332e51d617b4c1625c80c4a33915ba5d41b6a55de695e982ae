from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HESSIAN = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "hessian"
)
PACKET = HESSIAN / "remaining_hessian_job.exit.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_authorities(packet: dict) -> None:
    rows = packet.get("authority", {})
    require(bool(rows), "job exit authority is empty")
    for name, row in rows.items():
        path = ROOT / row.get("path", "")
        require(path.is_file(), f"job exit authority is absent: {name}")
        require(sha256(path) == row.get("sha256"), f"job exit authority is stale: {name}")


def main() -> int:
    packet = load(PACKET)
    require(
        packet.get("schema") == "MTTQ79HeightFourRemainingHessianJobExit.v1",
        "job exit schema changed",
    )
    require(
        packet.get("status") == "ALL_76_STRICT_TARGET_HESSIAN_BUDGETS_VERIFIED",
        "job exit is not complete",
    )
    require(
        packet.get("artifact") == "JOBEXIT.Q79.HEIGHT4.HESSIAN76",
        "job exit artifact changed",
    )
    final = packet["final_manifest"]
    require(
        final["status"] == "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED",
        "final precision status changed",
    )
    require(int(final["full_budget_count"]) == 76, "full budget count changed")
    require(int(final["current_main_count"]) == 76, "main count changed")
    require(int(final["current_tail_count"]) == 76, "tail count changed")
    require(int(final["remaining_count"]) == 0, "remaining count is nonzero")
    require(final["pending_indices"] == [], "pending index list is nonempty")

    precision = load(HESSIAN / "precision.manifest.json")
    tail = load(HESSIAN / "tailH.manifest.json")
    require(
        precision["status"] == "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED",
        "live precision manifest is incomplete",
    )
    require(int(precision["counts"]["full_budget"]) == 76, "live precision count changed")
    require(int(precision["remaining_full_budget_count"]) == 0, "live precision remainder changed")
    require(tail["status"] == "ALL_76_TAIL_HESSIANS_CERTIFIED", "tail manifest is incomplete")
    require(int(tail["completed_count"]) == 76, "tail completed count changed")

    scope = packet["strict_scope"]
    for key in (
        "all_76_full_target_Hessian_budgets_closed",
        "all_76_main_certificates_current",
        "all_76_tail_certificates_current",
        "nested_tail_audit_passed",
        "nested_precision_audit_passed",
        "process_success_is_not_ledger_promotion",
    ):
        require(scope[key] is True, f"job exit lost {key}")
    require(scope["observed_SM_values_used"] is False, "job exit imported observed SM values")
    for key in (
        "A384_residual_Jacobian_nonsingularity_closed",
        "A385_interval_Newton_or_Krawczyk_zero_closed",
        "physical_observable_map_closed",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"job exit overclaims {key}")
    audit_authorities(packet)
    print(
        "PASS: durable q79 height-four job exit binds the audited 76-target "
        "precision and tail manifests without promoting A384/A385/SM closure"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
