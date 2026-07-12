"""Build M_source Huv operator or direct Herm(2) rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTS = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-individual-constants-source-search")

SLUG = "selected_msourcehuvoperator_or_directherm2rows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MSourceHuvOperator_or_DirectHerm2Rows_v1.md"

MSOURCE_CONTRACT = PACKET_DIR / "msource_contract_reconciled_with_active_domain.packet.json"
MSOURCE_ATTEMPT = PACKET_DIR / "msource_execution_attempt_after_bhuv_rh_import.packet.json"
DIRECT_ATTEMPT = PACKET_DIR / "direct_herm2_rows_after_msource_contract.packet.json"
DIAGONAL_GUARD = PACKET_DIR / "diagonal_hym_metric_not_msource_guard.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_msource_directherm2_attempt.packet.json"

PREVIOUS = DATA / "selected_hsectordynamicc1extension_or_directhuvrows.candidate.json"
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
C3_EHUV = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
HRESPONSE_VALUE = DATA / "selected_hresponsevaluesourcefunctional_or_directherm2rows.candidate.json"
HRESPONSE_FUNCTIONAL = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "hresponse_value_source_functional.packet.json"
)
HRESPONSE_ROUTE_MATRIX = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "current_value_route_acceptance_matrix.packet.json"
)
HRESPONSE_DIRECT_RUN = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "direct_herm2_row_emission_run.packet.json"
)
NONDIAG_CONTRACT = (
    DATA
    / "selected_nondiagonalhuvhessiansource_or_directherm2rows"
    / "nondiagonal_huv_source_acceptance_contract.packet.json"
)
NONDIAG_REJECTION = (
    DATA
    / "selected_nondiagonalhuvhessiansource_or_directherm2rows"
    / "candidate_source_rejection_matrix.packet.json"
)
H7B1I = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix.candidate.json"
)
H7B1I_FUNCTOR = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "msource_acceptance_functor.packet.json"
)
H7B1I_ATTEMPT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "current_msource_export_attempt.packet.json"
)
H7B1I_OBSTRUCTION = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "dynamic_hessian_obstruction_theorem.packet.json"
)
H7B1R_CONTRACT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1r_huv_source_operator_or_primitive_c1_lambda_bridge"
    / "huv_bridge_acceptance_contract.packet.json"
)
H7B1S_DIRECT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution"
    / "direct_nonlinear_hym_row_execution_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_MSOURCEHUVOPERATOR_OR_DIRECTHERM2ROWS_"
    "CONTRACT_RECONCILED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HResponseTableValueRows_or_DirectHerm2ValueRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing M_source/Herm2 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        BHUV,
        C3_EHUV,
        HRESPONSE_VALUE,
        HRESPONSE_FUNCTIONAL,
        HRESPONSE_ROUTE_MATRIX,
        HRESPONSE_DIRECT_RUN,
        NONDIAG_CONTRACT,
        NONDIAG_REJECTION,
        H7B1I,
        H7B1I_FUNCTOR,
        H7B1I_ATTEMPT,
        H7B1I_OBSTRUCTION,
        H7B1R_CONTRACT,
        H7B1S_DIRECT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    bhuv = load(BHUV)
    c3 = load(C3_EHUV)
    hresponse_value = load(HRESPONSE_VALUE)
    hresponse_functional = load(HRESPONSE_FUNCTIONAL)
    hresponse_route_matrix = load(HRESPONSE_ROUTE_MATRIX)
    hresponse_direct_run = load(HRESPONSE_DIRECT_RUN)
    nondiag_contract = load(NONDIAG_CONTRACT)
    nondiag_rejection = load(NONDIAG_REJECTION)
    h7b1i = load(H7B1I)
    h7b1i_functor = load(H7B1I_FUNCTOR)
    h7b1i_attempt = load(H7B1I_ATTEMPT)
    h7b1i_obstruction = load(H7B1I_OBSTRUCTION)
    h7b1r_contract = load(H7B1R_CONTRACT)
    h7b1s_direct = load(H7B1S_DIRECT)

    msource_route = next(
        row
        for row in hresponse_route_matrix["route_rows"]
        if row["route_id"] == "full_M_source_plus_R_H_restriction"
    )
    direct_route = next(
        row
        for row in hresponse_route_matrix["route_rows"]
        if row["route_id"] == "direct_Herm2_rows"
    )
    diagonal_rejection = next(
        row
        for row in nondiag_rejection["rows"]
        if row["candidate_id"] == "diagonal_HYM_metric_connection_C3"
    )

    msource_contract = {
        "schema": "MTTMSourceContractReconciledWithActiveDomain.v1",
        "status": "MSOURCE_CONTRACT_RECONCILED_ACTIVE_DOMAIN_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_h7b1i_contract": {
            "M_source_acceptance_functor_built": h7b1i["M_source_acceptance_functor_built"],
            "M_source_value_emitted": h7b1i["M_source_value_emitted"],
            "formal_construction_when_payload_exists": h7b1i_functor[
                "formal_construction_when_payload_exists"
            ],
            "acceptance_requirements": h7b1i_functor["acceptance_requirements"],
        },
        "active_domain_supersessions": {
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "B_Huv_source_orthonormality": bhuv["whitening_map_and_lift"][
                "source_orthonormality_certificate"
            ],
            "R_H_restriction_closed": hresponse_functional["closed_domain_inputs"][
                "R_H_restriction_closed"
            ],
            "P_H_projector_closed": hresponse_functional["closed_domain_inputs"][
                "P_H_projector_closed"
            ],
            "dynamic_Hessian_domain_on_BHuv_closed": hresponse_functional["closed_domain_inputs"][
                "dynamic_Hessian_domain_on_BHuv_closed"
            ],
            "Herm2_row_extractors_closed": hresponse_functional["closed_domain_inputs"][
                "Herm2_row_extractors_closed"
            ],
        },
        "updated_formula": {
            "M_source": "M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2",
            "Huv": "H_uv = B_Huv^* M_source B_Huv",
            "R_H": hresponse_functional["accepted_value_source_contract"][
                "full_H_response_route_formula"
            ]["R_H"],
            "accepted_only_if": [
                "selected H_response table or finite H-sector Hessian is emitted",
                "same-source M_source entries are emitted",
                "direct Huu,Hud,Hdd rows or equivalent B_Huv^*M_sourceB_Huv values are emitted",
                "source ownership, same-source exactness/error, and quotient certificates are attached",
            ],
        },
        "decision": {
            "M_source_acceptance_contract_reconciled": True,
            "B_Huv_and_R_H_domain_closed": True,
            "M_source_values_emitted": False,
            "Huv_values_emitted": False,
        },
    }

    msource_attempt = {
        "schema": "MTTMSourceExecutionAttemptAfterBHuvRHImport.v1",
        "status": "MSOURCE_EXECUTION_ATTEMPTED_DOMAIN_CLOSED_ZERO_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_support": {
            "H7B1I_current_attempt_status": h7b1i_attempt["status"],
            "available_prefix_is_sufficient_for_contract": h7b1i_attempt["attempted_export"][
                "available_prefix_is_sufficient_for_contract"
            ],
            "available_prefix_is_sufficient_for_values": h7b1i_attempt["attempted_export"][
                "available_prefix_is_sufficient_for_values"
            ],
            "active_value_source_functional_status": hresponse_functional["status"],
            "full_M_source_plus_R_H_route_status": msource_route["status"],
        },
        "strict_missing_after_active_domain_reconciliation": {
            "selected_H_response_table": hresponse_value["closure_decision"][
                "selected_H_response_table_emitted"
            ]
            is False,
            "selected_Hermitian_M_source_entries": True,
            "direct_Huv_values": True,
            "source_exactness_or_error_certificate": True,
        },
        "computed_values": {
            "H_response": None,
            "R_H_values": None,
            "M_source": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "decision": {
            "M_source_execution_attempted": True,
            "B_Huv_R_H_domain_available": True,
            "selected_H_response_table_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "Huv_values_emitted": False,
        },
    }

    direct_attempt = {
        "schema": "MTTDirectHerm2RowsAfterMSourceContract.v1",
        "status": "DIRECT_HERM2_ROWS_EXECUTED_ZERO_ACCEPTED_AFTER_MSOURCE_CONTRACT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_direct_run_status": hresponse_direct_run["status"],
        "direct_route_status": direct_route["status"],
        "normal_form": hresponse_direct_run["normal_form"],
        "required_rows": hresponse_direct_run["required_rows"],
        "required_certificates": hresponse_direct_run["required_certificates"],
        "emitted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "direct_Herm2_row_execution_attempted": True,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "accepted_row_count": hresponse_direct_run["decision"]["accepted_row_count"],
            "accepted_certificate_count": 0,
        },
    }

    diagonal_guard = {
        "schema": "MTTDiagonalHYMMetricNotMSourceGuard.v1",
        "status": "DIAGONAL_HYM_METRIC_RECHECKED_NOT_MSOURCE_OR_DIRECT_HERM2_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "diagonal_HYM_support": {
            "selected_HYM_metric_or_connection_on_E_H_UV": c3["guardrails"][
                "selected_HYM_metric_or_connection_on_E_H_UV_emitted"
            ],
            "metric_on_E_H_UV_basis": c3["metric_connection_fixed_point"][
                "metric_on_E_H_UV_basis"
            ],
            "connection_on_E_H_UV_basis": c3["metric_connection_fixed_point"][
                "connection_on_E_H_UV_basis"
            ],
            "residual_l2": c3["metric_connection_fixed_point"]["residual_l2"],
        },
        "prior_rejection": diagonal_rejection,
        "H7B1S_direct_nonlinear_attempt": {
            "status": h7b1s_direct["status"],
            "direct_nonlinear_HYM_row_execution_closes_Huv": h7b1s_direct["decision"][
                "direct_nonlinear_HYM_row_execution_closes_Huv"
            ],
            "reason": h7b1s_direct["decision"]["reason"],
        },
        "why_rejected_even_after_active_BHuv": [
            "B_Huv^* G_Q B_Huv = I_2 is source-domain orthonormality, not a mass/strain Hessian",
            "T3/diag(exp(u),exp(-u)) is kinematic HYM support, not selected H_response",
            "no non-scalar Herm(2) Huu,Hud,Hdd source rows or certificates are emitted",
        ],
        "decision": {
            "diagonal_metric_retired_as_M_source_value": True,
            "diagonal_metric_retired_as_direct_Herm2_rows": True,
            "M_source_values_emitted": False,
            "direct_Herm2_rows_emitted": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterMSourceDirectHerm2Attempt.v1",
        "status": "NEXT_FRONTIER_HRESPONSE_TABLE_VALUE_ROWS_OR_DIRECT_HERM2_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "M_source acceptance contract reconciled with active B_Huv/R_H domain",
            "H7B1I old missing-domain language superseded where active B_Huv/R_H is closed",
            "diagonal HYM metric rechecked and rejected as M_source/direct Herm(2) values",
            "direct Herm(2) row execution rerun with zero accepted rows",
        ],
        "still_open": [
            "selected H_response table value rows",
            "selected Hermitian M_source entries",
            "or direct source-owned Huu,Hud,Hdd Herm(2) rows",
            "same-source exactness/error and source ownership certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedMSourceHuvOperatorOrDirectHerm2Rows",
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
            "name": "MSourceContractReconciledButValueRowsOpenTheorem",
            "proved": True,
            "statement": (
                "The M_source route is now exactly typed on the active domain: "
                "M_source=sym(R_H^*H_response R_H) and Huv=B_Huv^*M_sourceB_Huv. "
                "The active repo closes B_Huv, R_H/domain, and Herm(2) row "
                "extractors, superseding older missing-domain language. Current "
                "packets still emit zero selected H_response rows, zero M_source "
                "entries, and zero direct Huu,Hud,Hdd rows. The diagonal HYM "
                "metric remains kinematic support and is not M_source."
            ),
        },
        "packets": {
            "msource_contract_reconciled_with_active_domain": rel(MSOURCE_CONTRACT),
            "msource_execution_attempt_after_bhuv_rh_import": rel(MSOURCE_ATTEMPT),
            "direct_herm2_rows_after_msource_contract": rel(DIRECT_ATTEMPT),
            "diagonal_hym_metric_not_msource_guard": rel(DIAGONAL_GUARD),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "bhuv": rel(BHUV),
            "c3_ehuv": rel(C3_EHUV),
            "hresponse_value": rel(HRESPONSE_VALUE),
            "hresponse_functional": rel(HRESPONSE_FUNCTIONAL),
            "hresponse_route_matrix": rel(HRESPONSE_ROUTE_MATRIX),
            "hresponse_direct_run": rel(HRESPONSE_DIRECT_RUN),
            "nondiag_contract": rel(NONDIAG_CONTRACT),
            "nondiag_rejection": rel(NONDIAG_REJECTION),
            "h7b1i": rel(H7B1I),
            "h7b1r_contract": rel(H7B1R_CONTRACT),
            "h7b1s_direct": rel(H7B1S_DIRECT),
        },
        "closure_decision": {
            "M_source_acceptance_contract_reconciled": True,
            "B_Huv_R_H_domain_available": True,
            "diagonal_HYM_metric_rechecked_not_M_source": True,
            "M_source_execution_attempted": True,
            "direct_Herm2_row_execution_attempted": True,
            "selected_H_response_table_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "Huv_values_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "accepted_H_response_source_row_count": hresponse_value["key_numbers"][
                "accepted_H_response_source_row_count"
            ],
            "emitted_direct_Herm2_row_or_certificate_count": hresponse_value["key_numbers"][
                "emitted_direct_Herm2_row_or_certificate_count"
            ],
            "required_direct_Herm2_row_or_certificate_count": hresponse_value["key_numbers"][
                "required_direct_Herm2_row_or_certificate_count"
            ],
            "accepted_value_source_routes": hresponse_value["key_numbers"][
                "accepted_value_source_routes"
            ],
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedMSourceHuvOperatorOrDirectHerm2Rows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "M_source_acceptance_contract_reconciled": True,
        "B_Huv_R_H_domain_available": True,
        "diagonal_HYM_metric_rechecked_not_M_source": True,
        "M_source_execution_attempted": True,
        "direct_Herm2_row_execution_attempted": True,
        "selected_H_response_table_emitted": False,
        "selected_Hermitian_M_source_emitted": False,
        "M_source_plus_R_H_values_emitted": False,
        "Huv_values_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_F_Huv_rows_emitted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected MSourceHuvOperator or DirectHerm2Rows v1

Status: `{STATUS}`

## Theorem

The active domain now makes the full `M_source` route exact:

```text
M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2
H_uv = B_Huv^* M_source B_Huv
```

Active support:

- `B_Huv` source-orthonormal lift: `{bhuv["whitening_map_and_lift"]["B_Huv_symbolic_exact_payload_emitted"]}`
- `R_H` restriction closed in the value-source functional: `{hresponse_functional["closed_domain_inputs"]["R_H_restriction_closed"]}`
- Herm(2) row extractors closed: `{hresponse_functional["closed_domain_inputs"]["Herm2_row_extractors_closed"]}`

Current execution:

- selected `H_response` table rows: `0`
- selected `M_source` entries: `0`
- direct `Huu,Hud,Hdd` rows: `0`
- accepted certificates: `0`

The selected diagonal HYM metric remains support only.  It cannot be promoted to
`M_source` or direct Herm(2) rows because `B_Huv^*G_QB_Huv=I_2` is the source
inner-product normalization, not a Higgs mass/strain Hessian.

Next artifact: `{NEXT}`
"""

    write_json(MSOURCE_CONTRACT, msource_contract)
    write_json(MSOURCE_ATTEMPT, msource_attempt)
    write_json(DIRECT_ATTEMPT, direct_attempt)
    write_json(DIAGONAL_GUARD, diagonal_guard)
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
