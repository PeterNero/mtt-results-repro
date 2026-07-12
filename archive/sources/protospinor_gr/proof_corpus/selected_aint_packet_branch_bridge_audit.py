from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(cert["status"] == "AINT_PACKET_BRANCHES_CLASSIFIED_SELECTED_BRANCH_BRIDGE_OPEN", "unexpected status")
    source = cert["source_tests"]
    decisions = cert["import_decisions"]
    guards = cert["guardrails"]
    branches = {row["branch"]: row for row in cert["branch_gap_table"]}

    require(source["qg_defines_global_aint_packet"] is True, "QG A_int packet should be sourced")
    require(source["theta_nil_saturates_floor_in_benchmark"] is True, "Theta nil saturation should be sourced")
    require(source["theta_warns_explicit_realizations_need_not_saturate"] is True, "Theta saturation warning should be sourced")
    require(source["z64_exact_branch_has_lambda_15"] is True, "Z64 lambda 15 should be sourced")
    require(source["physical_action_marks_lambda15_internal_only"] is True, "lambda 15 should be internal only")
    require(abs(branches["theta_nil_floor_benchmark"]["sqrt_lambda_star"] - 0.5) < 1e-15, "nil sqrt gap mismatch")
    require(abs(branches["z64_central_circle_exact_branch"]["sqrt_lambda_star"] - (15.0 ** 0.5)) < 1e-15, "Z64 sqrt gap mismatch")
    require(decisions["can_import_z64_lambda15_as_internal_exact_branch_value"] is True, "should import internal Z64 value")
    require(decisions["can_import_z64_lambda15_as_physical_modal_gap"] is False, "must not import as physical gap")
    require(decisions["can_replace_GR_modal_gap_with_z64_without_bridge"] is False, "must not substitute without bridge")
    require(guards["claims_lambda15_is_GR_modal_gap"] is False, "must not claim lambda15 is GR modal gap")
    require(guards["forbids_cross_branch_substitution_without_bridge"] is True, "cross-branch guard required")

    print("AUDIT_PASS: A_int branches classified; selected branch bridge remains open")


if __name__ == "__main__":
    main()
