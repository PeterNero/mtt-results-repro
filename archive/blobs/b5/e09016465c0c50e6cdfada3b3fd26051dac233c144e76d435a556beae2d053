from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_tt_qsector_eigenpacket_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    require(
        cert["status"] == "TT_QSECTOR_MODEL_EIGENPACKET_COMPUTED_SELECTED_DOMAIN_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    model = cert["model_computation"]
    status = cert["candidate_status"]
    remaining = cert["remaining_gate"]
    guards = cert["guardrails"]

    require(source["qg_i_uses_bounded_geometry_finite_slab"] is True, "finite slab/domain should be sourced")
    require(source["qg_i_uses_TT_sector"] is True, "TT sector should be sourced")
    require(source["source_selects_unique_TT_slab_size"] is False, "slab size must remain open")
    require(source["source_selects_boundary_conditions"] is False, "boundary conditions must remain open")
    require(source["source_computes_lowest_TT_eigenvalue"] is False, "selected eigenvalue must remain open")
    require(abs(model["unit_radius_L_2pi_value"] - 1.0) < 1e-15, "unit-radius eigenvalue should be one")
    require(model["computed_as_selected_MTT_value"] is False, "model must not be selected")
    require(len(model["rows"]) == 3, "expected model rows")
    require(status["flat_periodic_unit_radius_matches_closure_metric_1"] is True, "unit model should match closure one")
    require(status["selected_by_current_corpus"] is False, "model should not be selected")
    require(status["same_branch_with_Z64"] is False, "must not identify with Z64")
    require(remaining["name"] == "Selected_TT_Domain_and_Boundary_Condition_Theorem", "wrong remaining gate")
    require(packet["open_selected_data"]["selected_TT_background_or_finite_quotient"] is None, "packet must not select domain")
    require(guards["claims_flat_periodic_model_selected"] is False, "must not claim model selected")
    require(guards["claims_lambda_TT_equals_1"] is False, "must not claim lambda one")
    require(guards["claims_physical_modal_gap"] is False, "must not claim physical gap")

    print("AUDIT_PASS: TT Q-sector model eigenpacket computed; selected domain remains open")


if __name__ == "__main__":
    main()
