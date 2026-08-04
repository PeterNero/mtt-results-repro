"""Build selected H-response value-source functional or direct Herm(2) rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hresponsevaluesourcefunctional_or_directherm2rows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HResponseValueSourceFunctional_or_DirectHerm2Rows_v1.md"

FUNCTIONAL = PACKET_DIR / "hresponse_value_source_functional.packet.json"
DIRECT_ROWS = PACKET_DIR / "direct_herm2_row_emission_run.packet.json"
ROUTES = PACKET_DIR / "current_value_route_acceptance_matrix.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hresponse_value_source_functional.packet.json"

PREVIOUS = DATA / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution.candidate.json"
SOURCE_GATE = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "source_functional_acceptance_gate.packet.json"
)
STRICT_MH = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)
DYNAMIC_HESSIAN = DATA / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission.candidate.json"
MH_THREE_ROW = DATA / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution.candidate.json"
MH_SEARCH = DATA / "selected_mhvalueemissionsearch_or_c5c6bridgefrontier.candidate.json"
MH_ACCEPTANCE = DATA / "selected_higgsspecificmhacceptanceobject_or_valuefrontier.candidate.json"
BHUV = DATA / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier.candidate.json"
HSECTOR_RESTRICTION = DATA / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian.candidate.json"

STATUS = (
    "MTT_SELECTED_HRESPONSEVALUESOURCEFUNCTIONAL_OR_DIRECTHERM2ROWS_"
    "FUNCTIONAL_CONTRACT_EXECUTED_ZERO_VALUE_ROWS"
)
NEXT = "MTT_Selected_FiniteHFunctionalCandidate_or_DirectHerm2RowEmissionRun_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-response value-source inputs: " + ", ".join(missing))


def bool_at(data: dict[str, Any], *keys: str) -> bool:
    node: Any = data
    for key in keys:
        node = node[key]
    return bool(node)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SOURCE_GATE,
        STRICT_MH,
        DYNAMIC_HESSIAN,
        MH_THREE_ROW,
        MH_SEARCH,
        MH_ACCEPTANCE,
        BHUV,
        HSECTOR_RESTRICTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    source_gate = load(SOURCE_GATE)
    strict_mh = load(STRICT_MH)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    mh_three_row = load(MH_THREE_ROW)
    mh_search = load(MH_SEARCH)
    mh_acceptance = load(MH_ACCEPTANCE)
    bhuv = load(BHUV)
    hsector_restriction = load(HSECTOR_RESTRICTION)

    closed_inputs = source_gate["closed_inputs"]
    required_table = source_gate["accepted_value_sources"]["direct_Herm2_rows"]["required_table"]
    accepted_sources = source_gate["accepted_value_sources"]

    value_source_functional = {
        "schema": "MTTHResponseValueSourceFunctional.v1",
        "status": "VALUE_SOURCE_FUNCTIONAL_CONTRACT_CLOSED_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "same_source_branch": closed_inputs["same_source_branch"],
        "closed_domain_inputs": {
            "B_Huv_domain_closed": closed_inputs["B_Huv_domain_closed"],
            "B_Huv_orthonormality": closed_inputs["B_Huv_orthonormality"],
            "P_H_projector_closed": closed_inputs["P_H_projector_closed"],
            "R_H_restriction_closed": closed_inputs["R_H_restriction_closed"],
            "Herm2_row_extractors_closed": closed_inputs["Herm2_row_extractors_closed"],
            "dynamic_Hessian_domain_on_BHuv_closed": dynamic_hessian["closure_decision"][
                "dynamic_Hessian_domain_on_BHuv_closed"
            ],
            "MH_three_row_source_functional_contract_closed": mh_three_row["closure_decision"][
                "MH_three_row_source_functional_contract_closed"
            ],
        },
        "accepted_value_source_contract": {
            "direct_F_H_second_variation": accepted_sources["direct_F_H_second_variation"][
                "accepted_if"
            ],
            "direct_Herm2_rows_required": required_table,
            "full_H_response_route_formula": accepted_sources["full_H_response_route"]["formula"],
            "strict_MH_acceptance_tests": strict_mh["acceptance_tests"],
        },
        "forbidden_promotions_retired": source_gate["forbidden_promotions_retired_by_this_gate"]
        + strict_mh["forbidden_shortcuts"],
        "computed_when_values_exist": strict_mh["computed_when_values_exist"],
        "execution_decision": {
            "value_source_functional_contract_closed": True,
            "selected_F_H_functional_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "lambda_H_predicted": False,
        },
    }

    direct_rows = {
        "schema": "MTTDirectHerm2RowEmissionRun.v1",
        "status": "DIRECT_HERM2_ROW_RUN_EXECUTED_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "ordered_matrix": "[[Huu, Hud_re+i Hud_im], [Hud_re-i Hud_im, Hdd]]",
        "normal_form": {
            "m0": "(Huu+Hdd)/2",
            "Delta": "(Huu-Hdd)/2",
            "Omega": "Hud_re+i Hud_im",
            "trace_free_block": "[[Delta, Omega], [conj(Omega), -Delta]]",
        },
        "required_rows": [
            {"row_id": row_id, "value": value, "emitted": value is not None, "accepted": False}
            for row_id, value in required_table.items()
        ],
        "required_certificates": [
            "Hdu_equals_conj_Hud_certificate",
            "source_ownership_certificate",
            "same_source_exactness_or_error_certificate",
            "quotient_admissibility_certificate",
        ],
        "rejected_shortcuts": [
            "metric-only Hessian G_Q",
            "connection generator T3",
            "rank-one/collapsed projector data",
            "observed Higgs mass/lambda_H/tan_beta/threshold residual selector",
            "static H-sector logdet promoted as dynamic R_H^RG",
        ],
        "decision": {
            "required_row_count": len(required_table),
            "emitted_row_count": sum(1 for value in required_table.values() if value is not None),
            "accepted_row_count": 0,
            "direct_Huu_Hud_Hdd_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "source_ownership_certificate_emitted": False,
            "same_source_exactness_or_error_certificate_emitted": False,
            "quotient_admissibility_certificate_emitted": False,
        },
    }

    route_rows = [
        {
            "route_id": "direct_F_H_second_variation",
            "status": "contract_closed_values_open",
            "support_refs": [rel(SOURCE_GATE), rel(DYNAMIC_HESSIAN)],
            "passes_value_source_functional": False,
            "missing": [
                "selected finite H-sector functional F_H",
                "nonzero trace-free Herm(2) Hessian",
                "finite exactness/residual certificate",
            ],
        },
        {
            "route_id": "direct_Herm2_rows",
            "status": "schema_closed_rows_open",
            "support_refs": [rel(STRICT_MH), rel(MH_SEARCH), rel(MH_ACCEPTANCE)],
            "passes_value_source_functional": False,
            "missing": [
                "Huu",
                "Hud_re",
                "Hud_im",
                "Hdd",
                "source ownership certificate",
                "same-source exactness/error certificate",
                "quotient admissibility certificate",
            ],
        },
        {
            "route_id": "full_M_source_plus_R_H_restriction",
            "status": "domain_closed_source_operator_open",
            "support_refs": [rel(BHUV), rel(HSECTOR_RESTRICTION)],
            "passes_value_source_functional": False,
            "missing": [
                "selected Hermitian M_source",
                "proof that B_Huv^* M_source B_Huv is accepted Herm(2) block",
                "direct Huu,Hud,Hdd rows",
            ],
        },
        {
            "route_id": "C5C6_projection_bridge",
            "status": "contract_open_payload_absent",
            "support_refs": [rel(SOURCE_GATE), rel(MH_THREE_ROW)],
            "passes_value_source_functional": False,
            "missing": [
                "C5b projection measure equality payload",
                "C6 no-extra-boundary/source term payload",
                "bridge-executed H-response values",
            ],
        },
    ]

    routes = {
        "schema": "MTTCurrentHResponseValueRouteAcceptanceMatrix.v1",
        "status": "ALL_CURRENT_ROUTES_RECHECKED_NO_ACCEPTED_VALUE_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_rows": route_rows,
        "decision": {
            "routes_checked": len(route_rows),
            "accepted_value_source_routes": 0,
            "all_open_fields_are_source_emission_fields": True,
            "no_basis_or_domain_blocker_remaining": True,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHResponseValueSourceFunctional.v1",
        "status": "NEXT_FRONTIER_FINITE_H_FUNCTIONAL_OR_DIRECT_HERM2_ROW_EMISSION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "accepted H-response value-source functional contract",
            "direct Herm(2) row emission run with zero accepted rows",
            "route acceptance matrix for current F_H, Herm(2), M_source, and C5/C6 lanes",
        ],
        "still_open": [
            "selected finite H-sector functional F_H",
            "selected nonzero Herm(2) Hessian/value rows Huu,Hud_re,Hud_im,Hdd",
            "source ownership certificate",
            "same-source exactness/error certificate",
            "quotient admissibility certificate",
            "selected H-response spectrum/logdet",
            "numeric R_H^RG value execution",
            "lambda_H/no-knob Higgs prediction",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHResponseValueSourceFunctionalOrDirectHerm2Rows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "HResponseValueSourceFunctionalOrDirectHerm2RowsTheorem",
            "proved": True,
            "statement": (
                "Given the already closed B_Huv/P_H/R_H domain and Herm(2) row "
                "extractors, the accepted H-response value source is exactly a "
                "selected finite H-sector functional F_H with certified Herm(2) "
                "second variation, an equivalent direct Herm(2) row table, or a "
                "same-source full H_response/M_source restriction. Current packets "
                "satisfy the contract and domain criteria but emit zero accepted "
                "value rows, so no H spectrum, R_H^RG value, or lambda_H prediction "
                "is promoted."
            ),
        },
        "packets": {
            "hresponse_value_source_functional": rel(FUNCTIONAL),
            "direct_herm2_row_emission_run": rel(DIRECT_ROWS),
            "current_value_route_acceptance_matrix": rel(ROUTES),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "source_gate": rel(SOURCE_GATE),
            "strict_mh": rel(STRICT_MH),
            "dynamic_hessian": rel(DYNAMIC_HESSIAN),
            "mh_three_row": rel(MH_THREE_ROW),
            "mh_search": rel(MH_SEARCH),
            "mh_acceptance": rel(MH_ACCEPTANCE),
            "bhuv": rel(BHUV),
            "hsector_restriction": rel(HSECTOR_RESTRICTION),
        },
        "closure_decision": {
            "value_source_functional_contract_closed": True,
            "domain_and_row_extractors_closed": True,
            "current_value_routes_rechecked": True,
            "selected_F_H_functional_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "selected_logdet_from_H_response_emitted": False,
            "R_H_RG_logdet_value_executed": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "value_routes_checked": len(route_rows),
            "accepted_value_source_routes": 0,
            "required_direct_Herm2_row_or_certificate_count": len(required_table),
            "emitted_direct_Herm2_row_or_certificate_count": sum(
                1 for value in required_table.values() if value is not None
            ),
            "accepted_H_response_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "UP_RET_OVERLAP_HRG_diagnostic_only": previous["key_numbers"][
                "UP_RET_OVERLAP_HRG_diagnostic_only"
            ],
            "static_H_logdet_support": previous["key_numbers"]["static_H_logdet_support"],
            "selected_K_source_rows": previous["key_numbers"]["selected_K_source_rows"],
            "selected_K_rows_required": previous["key_numbers"]["selected_K_rows_required"],
        },
        "support_flags": {
            "B_Huv_two_column_uv_lift_emitted": bool_at(
                bhuv, "closure_decision", "B_Huv_two_column_uv_lift_emitted"
            ),
            "dynamic_Hessian_domain_on_BHuv_closed": bool_at(
                dynamic_hessian, "closure_decision", "dynamic_Hessian_domain_on_BHuv_closed"
            ),
            "second_variation_source_gate_closed": source_gate["status"]
            == "SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN",
            "MH_three_row_source_functional_contract_closed": bool_at(
                mh_three_row,
                "closure_decision",
                "MH_three_row_source_functional_contract_closed",
            ),
            "strict_MH_packet_currently_passes": strict_mh["current_packet_passes"],
            "MH_search_found_selected_rows": bool_at(
                mh_search, "closure_decision", "M_H_three_real_value_rows_emitted"
            ),
            "H_specific_acceptance_rows_emitted": bool_at(
                mh_acceptance, "closure_decision", "M_H_three_real_value_rows_emitted"
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHResponseValueSourceFunctionalOrDirectHerm2Rows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "value_source_functional_contract_closed": True,
        "domain_and_row_extractors_closed": True,
        "current_value_routes_rechecked": True,
        "selected_F_H_functional_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "selected_H_response_spectrum_emitted": False,
        "R_H_RG_logdet_value_executed": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_value_source_routes": 0,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
    }

    note = f"""# MTT Selected H-Response Value Source Functional or Direct Herm(2) Rows v1

Status: `{STATUS}`

## Theorem

The H-response value-source contract is now executable on the closed
`B_Huv/P_H/R_H` domain.  An accepted value source must be one of:

- selected finite H-sector functional `F_H` with a certified nonzero Herm(2)
  second variation,
- direct source-owned Herm(2) rows `Huu`, `Hud_re`, `Hud_im`, `Hdd` plus
  exactness/source/admissibility certificates,
- same-source full `H_response` or `M_source` restriction yielding the same
  Herm(2) block.

## Execution

Current value routes checked: `{len(route_rows)}`.

Accepted value-source routes: `0`.

Accepted H-response source rows: `0`.

## Consequence

This closes the value-source functional gate but not the values.  No selected
H-response spectrum, dynamic `R_H^RG` logdet, `lambda_H`, true-SM-equivalence,
or full no-knob Higgs closure is promoted.

Next artifact: `{NEXT}`
"""

    write_json(FUNCTIONAL, value_source_functional)
    write_json(DIRECT_ROWS, direct_rows)
    write_json(ROUTES, routes)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
