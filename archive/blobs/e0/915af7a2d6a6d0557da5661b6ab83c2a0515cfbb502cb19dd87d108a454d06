from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "TT_STIFFNESS_INTERNAL_COMPUTED_MODAL_GAP_IDENTIFICATION_OPEN",
        "unexpected status",
    )

    stiffness = cert["computed_internal_tt_stiffness"]
    modal = cert["modal_gap_candidates_in_same_audit_context"]
    decision = cert["interface_decision"]
    theorem = cert["next_required_theorem"]
    guards = cert["guardrails"]

    require(stiffness["all_positive"] is True, "TT stiffness rows should be positive")
    require(len(stiffness["rows"]) >= 3, "expected internal N rows")
    require(modal["dimensionless_operator_shape_closed"] is True, "operator shape should remain closed")
    require(modal["selected_global_Aint_packet_closed"] is False, "selected global Aint packet must remain open")
    require(modal["theta_nil_floor_benchmark"]["can_replace_GR_gap"] is False, "nil floor must not replace GR gap")
    require(modal["z64_central_circle_exact_branch"]["can_replace_GR_gap"] is False, "Z64 must not replace GR gap")
    require(decision["tt_response_stiffness_computed_in_internal_units"] is True, "TT stiffness should be computed")
    require(decision["tt_response_stiffness_identified_with_modal_gap"] is False, "stiffness/gap identity must remain open")
    require(decision["can_use_kappa_STF_as_Aint_lowest_eigenvalue"] is False, "must not use kappa as Aint eigenvalue")
    require(decision["gr_tt_Aint_identified_with_z64_tower"] is False, "Z64 identity must remain open")
    require("GR_TT_Response_to_Aint_Spectral_Interface_Theorem" == theorem["name"], "wrong next theorem")
    require(guards["claims_kappa_STF_is_lambda_star"] is False, "must not claim kappa equals lambda")
    require(guards["claims_z64_lambda15_is_GR_gap"] is False, "must not claim Z64 is GR gap")
    require(guards["claims_physical_modal_gap"] is False, "must not claim physical modal gap")

    print("AUDIT_PASS: TT stiffness computed internally; modal-gap identification remains open")


if __name__ == "__main__":
    main()
