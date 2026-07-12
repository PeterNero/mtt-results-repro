"""Build the Qa/SU3 twisted section-basis or operator-exit construction gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT_FILL = CERTS / "selected_qa_su3_twisted_gerbe_source_packet_fill_attempt_certificate.json"
Q79_S3 = Q79_REPO / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
Q79_GS = Q79_REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
Q79_RHOE = Q79_REPO / "certificates" / "visible_rhoE_source_ansatz_search_certificate.json"
Q79_OPERATOR = Q79_REPO / "certificates" / "visible_operator_source_blocker_resolution_certificate.json"
Q79_ROUTE_C_NOTE = Q79_REPO / "proof_corpus" / "Iwasawa_Route_C_Finite_Selected_Connection_Solve_Scaffold_v1.md"
OUTPUT_CERT = CERTS / "selected_qa_su3_twisted_section_basis_or_operator_exit_construction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def note_contains_route_c_contract() -> bool:
    text = Q79_ROUTE_C_NOTE.read_text(encoding="utf-8")
    required = [
        "validate_iwasawa_route_c_residuals.py",
        "rho_E",
        "D_E",
        "Riesz",
        "reduced Green",
        "dotD_alpha1",
        "no observed-flavor inputs",
    ]
    return all(item in text for item in required)


def main() -> None:
    fill = load(INPUT_FILL)
    s3 = load(Q79_S3)
    gs = load(Q79_GS)
    rhoe = load(Q79_RHOE)
    operator = load(Q79_OPERATOR)

    selected_gerbe_source_closed = (
        fill["filled_fields"]["selected_s3_flat_deligne_class"] is True
        and fill["filled_fields"]["map_to_qutrit_central_cocycle"] is True
        and fill["filled_fields"]["period_denominator"] == 3
        and s3["what_this_closes"]["selected_S3_flat_Deligne_class"] is True
        and s3["what_this_closes"]["selected_S3_pullback_restriction_table"] is True
    )
    curvature_source_closed = (
        gs["calculation_results"]["visible_green_schwarz_curvature_verified"] is True
        and gs["calculation_results"]["symbolic_iwasawa_row_validated"] is True
        and gs["calculation_results"]["required_visible_TrF_row_inserted"] is True
    )
    section_basis_exit_closed = (
        fill["fill_result"]["twisted_section_ring_filled"] is True
        and fill["fill_result"]["operator_exit_available"] is True
    )
    selected_operator_exit_closed = (
        operator["calculation_results"]["source_hunt_found_selected_D_E"] is True
        and operator["guardrails"]["claims_selected_D_E_constructed"] is True
    )

    retired_routes = {
        "ordinary_constant_rhoE_carriers": rhoe["calculation_results"]["ordinary_constant_carriers_blocked"] is True,
        "qutrit_central_absorption_as_ordinary_rhoE": rhoe["calculation_results"][
            "qutrit_projective_central_absorption_as_ordinary_rhoE_blocked"
        ]
        is True,
        "recombine_existing_certificates_as_operator_source": operator["calculation_results"][
            "blocker_resolved_by_existing_data"
        ]
        is False,
        "section_basis_claim_without_bases_or_constants": section_basis_exit_closed is False,
    }
    live_routes = {
        "typed_twisted_section_ring": {
            "status": "OPEN",
            "needed": [
                "ordinary a,b factor model",
                "twisted section dimensions and bases",
                "numeric twisted multiplication constants",
                "coherent spectral projector retention",
            ],
        },
        "projective_rhoE_or_fixed_gerbe_representative": {
            "status": "OPEN",
            "needed": rhoe["minimal_next_packet"],
        },
        "finite_selected_connection_solve_route_c": {
            "status": "PRIMARY_NEXT_CONSTRUCTION",
            "contract_available": note_contains_route_c_contract(),
            "needed": operator["minimal_new_data_that_would_close"],
        },
    }

    output = {
        "certificate": "SelectedQaSU3TwistedSectionBasisOrOperatorExitConstruction",
        "status": "QA_SU3_TWISTED_SECTION_BASIS_OR_OPERATOR_EXIT_CONSTRUCTION_REDUCED_TO_ROUTE_C_SOURCE_PACKET",
        "inputs": {
            "twisted_gerbe_fill_attempt": str(INPUT_FILL.relative_to(ROOT)),
            "q79_selected_s3_closure": str(Q79_S3),
            "q79_visible_gs_curvature_closure": str(Q79_GS),
            "q79_rhoE_ansatz_search": str(Q79_RHOE),
            "q79_visible_operator_blocker_resolution": str(Q79_OPERATOR),
            "q79_route_c_scaffold": str(Q79_ROUTE_C_NOTE),
        },
        "closed_now": {
            "selected_period_3_gerbe_source": selected_gerbe_source_closed,
            "smooth_s3_freed_witten_and_block_sector_source": fill["filled_fields"][
                "smooth_freed_witten"
            ]
            is True
            and fill["filled_fields"]["block_sector_projector_retention"] is True,
            "visible_green_schwarz_curvature_level_source": curvature_source_closed,
            "route_c_executable_contract_identified": live_routes["finite_selected_connection_solve_route_c"][
                "contract_available"
            ]
            is True,
        },
        "not_closed": {
            "ordinary_ab_factor_model": fill["unfilled_fields"]["ordinary_ab_factor_model_certified"] is None,
            "twisted_section_bases": fill["fill_result"]["twisted_section_ring_filled"] is False,
            "twisted_product_constants": fill["fill_result"]["twisted_section_ring_filled"] is False,
            "selected_visible_operator_source": operator["guardrails"]["claims_visible_operator_source_constructed"]
            is False,
            "selected_D_E_dotD_Riesz_Green": operator["guardrails"]["claims_selected_D_E_constructed"] is False,
            "primitive_C1_contractions": gs["still_open"]["primitive_C1_contractions"] is True,
        },
        "retired_routes": retired_routes,
        "live_routes": live_routes,
        "decision": {
            "primary_next_artifact": "Selected_Qa_SU3_Finite_Selected_Connection_Solve_Packet_v1",
            "why": "The selected gerbe and curvature sources are available, while the honest q79 audit says no existing selected D_E/operator packet exists. Route C is therefore the shortest non-circular route: solve the finite selected connection source equations and emit rho_E, D_E, Riesz, Green, dotD, and projector data from the same branch.",
            "forbidden_shortcuts": [
                "do not promote diagnostic rho_E or HYM smoke packets to selected sources",
                "do not use observed masses, mixings, or benchmark flavor entries",
                "do not treat the period-3 central cocycle as an ordinary c1 carrier",
                "do not claim a section-ring determinant until bases and product constants are numeric",
            ],
        },
        "gate_result": {
            "qa_su3_fully_closed": False,
            "operator_exit_available_now": selected_operator_exit_closed,
            "section_basis_exit_available_now": section_basis_exit_closed,
            "target_fitting_used": False,
            "next_gate_is_sharp": all(retired_routes.values())
            and live_routes["finite_selected_connection_solve_route_c"]["contract_available"] is True,
        },
    }

    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
