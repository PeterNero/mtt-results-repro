from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_tt_domain_boundary_condition_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    require(
        cert["status"] == "TT_DOMAIN_BOUNDARY_CONSTRAINTS_SOURCED_SELECTION_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    closed = cert["closed_now"]
    result = cert["selection_result"]
    candidates = cert["candidate_domain_classification"]
    next_gate = cert["next_gate"]
    guards = cert["guardrails"]

    require(source["qg_i_allows_bounded_domain"] is True, "bounded domain should be sourced")
    require(source["qg_i_allows_dirichlet_or_mixed"] is True, "Dirichlet/mixed should be sourced")
    require(source["qg_i_requires_TT_well_posed"] is True, "TT well-posed condition should be sourced")
    require(source["qg_ii_requires_no_boundary_BRST_terms"] is True, "BRST boundary condition should be sourced")
    require(source["source_selects_periodic_T3"] is False, "periodic T3 must not be selected")
    require(source["source_selects_dimensionless_L"] is False, "dimensionless length must remain open")
    require(all(closed.values()), "closed_now fields should be true")
    require(result["selected_TT_domain_closed"] is False, "selected domain must remain open")
    require(result["selected_boundary_condition_closed"] is False, "selected boundary must remain open")
    require(result["selected_lambda_TT_closed"] is False, "lambda must remain open")
    require(len(candidates) == 3, "expected three candidate domains")
    require(all(candidate["selected"] is False for candidate in candidates), "no candidate should be selected")
    require(next_gate["name"] == "TT_Domain_Selection_From_MTT_Fixed_Point_or_Internal_Quotient", "wrong next gate")
    require(packet["open_selection_data"]["selected_domain_topology"] is None, "packet must not select domain")
    require(guards["claims_periodic_T3_selected"] is False, "must not claim periodic selected")
    require(guards["claims_lambda_TT_numeric_selected"] is False, "must not claim numeric lambda")
    require(guards["claims_physical_modal_gap"] is False, "must not claim physical gap")

    print("AUDIT_PASS: TT domain/boundary constraints sourced; selection remains open")


if __name__ == "__main__":
    main()
