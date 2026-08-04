"""Build the selected C1 response-operator emission audit.

This is the gate after the DeltaTheta solve specification.  It checks whether
the selected artifacts emit the finite linear response operator A_selected and
source vector b_selected needed to solve the splitter equation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"
Q79_CERTS = Q79 / "certificates"

PREVIOUS = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
PHIFIN = DATA / "selected_phifin_alpha1_payload.candidate.json"
C1_TEMPLATE = Q79_CERTS / "selected_c1_response_data_certificate.template.json"
C1_ATTEMPT = Q79_CERTS / "selected_c1_response_extraction_attempt_certificate.json"
CANONICAL_ZERO = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"

OUTPUT = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
CERT = CERTS / "selected_routec_selected_c1_response_operator_emission_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
NEXT = "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def present(path: Path) -> bool:
    return path.exists()


def missing_nulls(items: dict[str, Any]) -> dict[str, bool]:
    return {key: value is None for key, value in items.items()}


def response_matrix_nonzero(matrix_packet: dict[str, Any]) -> bool:
    for sector in ("u", "d", "e", "nuD"):
        sector_packet = matrix_packet["c1_response_matrices"][sector]
        if sector_packet["max_abs_entry"] != 0:
            return True
    return False


def main() -> None:
    previous = load(PREVIOUS)
    phifin = load(PHIFIN)
    template = load(C1_TEMPLATE) if present(C1_TEMPLATE) else {}
    attempt = load(C1_ATTEMPT) if present(C1_ATTEMPT) else {}
    canonical = load(CANONICAL_ZERO)
    noninv = load(NONINV)

    missing = phifin["payload_slots"]["finite_Hessian_C1_source"]["missing"]
    attempt_missing = attempt.get("missing_selected_operator_data", {})
    attempt_result = attempt.get("attempt_result", {})
    template_operator = template.get("operator_data", {})
    template_responses = template.get("response_matrices", {})
    solve_gate = previous["selected_deltatheta_c1_solve_gate"]

    required_operator_slots = {
        "evaluated_grad_V_C1_alpha1_source_vector": missing["evaluated_grad_V_C1_alpha1_source_vector"] is not None,
        "full_lower_order_Hess_Xi_blocks": missing["full_lower_order_Hess_Xi_blocks"] is not None,
        "selected_deltaTheta_C1_solution": missing["selected_deltaTheta_C1_solution"] is not None,
        "explicit_dotD_Q_u_d_L_e_N_H": missing["explicit_dotD_Q_u_d_L_e_N_H"] is not None,
        "selected_zero_mode_basis_Q_u_d_L_e_N_H": missing["selected_zero_mode_basis_Q_u_d_L_e_N_H"] is not None,
        "selected_L2_Gram_Schmidt_rule": missing["selected_L2_Gram_Schmidt_rule"] is not None,
        "evaluated_zero_mode_response_integrals": missing["evaluated_zero_mode_response_integrals"] is not None,
        "sector_response_matrices_M_u_M_d_M_e_M_nuD": missing["sector_response_matrices_M_u_M_d_M_e_M_nuD"] is not None,
    }
    selected_operator_emitted = all(required_operator_slots.values())

    canonical_nonzero = response_matrix_nonzero(canonical)
    noninv_nonzero = noninv["calculation_results"]["nonzero_unselected_candidates_found"] > 0

    emission_audit = {
        "target_dimension_from_previous": solve_gate["target_real_dimension"],
        "required_operator_slots": required_operator_slots,
        "selected_operator_A_selected_emitted": selected_operator_emitted,
        "selected_source_vector_b_selected_emitted": required_operator_slots["evaluated_grad_V_C1_alpha1_source_vector"],
        "rank_test_now_computable": selected_operator_emitted,
        "least_squares_now_computable": selected_operator_emitted,
        "template_schema_present": present(C1_TEMPLATE),
        "template_status": template.get("status"),
        "template_driver_row_present": bool(template.get("selected_driver_row")),
        "template_principal_hessian_blocks_present": bool(
            template_operator.get("Hess_Xi_blocks", {}).get("principal_symbol_blocks")
        ),
        "template_response_matrices_null": {
            key: value is None
            for key, value in template_responses.items()
        },
        "extraction_attempt_present": present(C1_ATTEMPT),
        "extraction_attempt_status": attempt.get("status"),
        "extraction_attempt_result": attempt_result,
        "extraction_attempt_missing_nulls": missing_nulls(attempt_missing),
    }

    lanes = {
        "straight_selected_c1_response": {
            "status": "BLOCKED_VALUES_OPEN",
            "usable_as_proof": False,
            "reason": "The selected template names the driver and principal Hessian support, but selected finite blocks and response matrices are null.",
        },
        "canonical_smooth_bn_response": {
            "status": "COMPUTED_ZERO_RESPONSE",
            "usable_as_proof": False,
            "nonzero_response_found": canonical_nonzero,
            "reason": "The canonical mode-conserving smooth B_N one-response calculation is selected-shape support, but produces zero C1 matrices.",
        },
        "noninvariant_candidate_response": {
            "status": "NONZERO_UNSELECTED_CANDIDATES",
            "usable_as_proof": False,
            "nonzero_unselected_candidates_found": noninv["calculation_results"]["nonzero_unselected_candidates_found"],
            "can_close_selected_C1_now": noninv["calculation_results"]["can_close_selected_C1_now"],
            "reason": "The active-shift non-invariant candidates are algebraically useful but no selected source theorem emits their primitive/fiber rule.",
        },
    }

    operator_emission_contract = {
        "name": "SelectedC1ResponseOperatorEmissionContract",
        "operator_equation": "A_selected deltaTheta_C1 = b_selected, then project to b_splitter acceptance tests.",
        "domain_must_include": [
            "selected C1 deformation coordinates after gauge fixing",
            "selected Hessian lower-order finite blocks",
            "selected alpha1 source vector",
            "selected dotD operators for Q,u,d,L,e,N,H",
            "selected zero-mode bases and L2 Gram-Schmidt rule",
            "selected primitive C1 overlap contractions",
        ],
        "codomain_real_dimension": solve_gate["target_real_dimension"],
        "validators_after_emission": [
            "rank(A_selected) and consistency of the splitter target",
            "least-squares residual if overdetermined",
            "sector response matrices M_u, M_d, M_e, M_nuD",
            "mass split traceless norm tests",
            "CKM and PMNS commutator tests",
            "complex CP-odd invariant test",
        ],
        "forbidden_shortcuts": attempt.get("forbidden_shortcuts", []),
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedC1ResponseOperatorEmission",
        "status": STATUS,
        "inputs": {
            "selected_deltatheta_c1_solve_gate": rel(PREVIOUS),
            "selected_phifin_alpha1_payload": rel(PHIFIN),
            "q79_c1_response_template": rel(C1_TEMPLATE),
            "q79_c1_response_extraction_attempt": rel(C1_ATTEMPT),
            "canonical_smooth_bn_c1_response": rel(CANONICAL_ZERO),
            "noninvariant_c1_primitive_search": rel(NONINV),
        },
        "emission_audit": emission_audit,
        "response_lanes": lanes,
        "operator_emission_contract": operator_emission_contract,
        "what_closes_now": {
            "selected_response_operator_schema_audited": True,
            "q79_template_and_extraction_attempt_imported": True,
            "canonical_zero_response_separated_from_nonzero_unselected_candidates": True,
            "A_selected_emission_blocker_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_A_selected": True,
            "emit_selected_b_selected": True,
            "selected_Hess_Xi_finite_blocks": True,
            "selected_dotD_Q_u_d_L_e_N_H": True,
            "selected_zero_mode_bases_and_Gram_Schmidt": True,
            "selected_primitive_C1_contractions": True,
            "selected_sector_response_matrices": True,
            "solve_or_reject_splitter_equation": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SelectedC1ResponseOperatorEmissionAuditTheorem",
            "proved": True,
            "statement": (
                "The selected C1 response-operator emission gate is audited. Existing artifacts provide the "
                "curvature driver, response-chain formula, principal Hessian-symbol support, a zero canonical "
                "smooth B_N response, and nonzero unselected non-invariant candidates. They do not emit the "
                "selected finite response operator A_selected or selected source vector b_selected. Therefore "
                "the branch now reduces to a source/operator rebuild that emits these selected finite blocks "
                "before any honest DeltaTheta solve or flavor closure test can run."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Selected C1 Response Operator Emission

Status: `MTT_SELECTED_ROUTEC_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED`

This artifact asks whether the selected finite response operator required by

```text
A_selected * deltaTheta_C1 = b_splitter
```

is emitted by the current selected Route-C/Phi_fin/Galerkin stack.

## Result

It is not emitted yet.

The q79 C1 template and extraction attempt provide useful structure: the
alpha1 driver row, the Strominger/Heterotic C1 curvature source, the response
chain, and principal Hessian-symbol blocks.  But the selected finite data are
still null: finite Hessian blocks, selected source vector, `deltaTheta_C1`,
dotD operators, zero-mode bases, primitive contractions, and sector response
matrices.

## Lane Separation

- The canonical smooth B_N C1 response is computed but zero.
- The non-invariant primitive search finds nonzero candidates, but they are not
  selected by a source theorem.
- The selected C1 template is the correct schema, but it has not emitted
  `A_selected` or `b_selected`.

## Next Gate

The next artifact must rebuild the selected C1 operator source or Galerkin
payload so it emits:

- selected finite Hessian blocks,
- selected alpha1 source vector,
- selected dotD operators,
- selected zero-mode bases and L2 Gram-Schmidt rule,
- selected primitive C1 contractions,
- selected sector matrices `M_u`, `M_d`, `M_e`, `M_nuD`.

Next artifact: `MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
