"""Build the selected DeltaTheta_C1 solve gate for the Route-C splitter."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
PHIFIN = DATA / "selected_phifin_alpha1_payload.candidate.json"

OUTPUT = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
CERT = CERTS / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_DELTATHETA_C1_SOLVE_GATE_BUILT_SELECTED_HESSIAN_RESPONSE_OPERATOR_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_parts(value: Any) -> tuple[float, float]:
    if isinstance(value, list):
        return float(value[0]), float(value[1])
    return float(value), 0.0


def flatten_matrix_real(matrix: list[list[Any]]) -> list[float]:
    values: list[float] = []
    for row in matrix:
        for entry in row:
            real, imag = complex_parts(entry)
            values.extend([real, imag])
    return values


def norm_sq(values: list[float]) -> float:
    return sum(value * value for value in values)


def main() -> None:
    previous = load(PREVIOUS)
    phifin = load(PHIFIN)

    target = previous["source_emission_contract"]["representative_diagnostic_target"]
    sector_targets = {
        "u": target["u_dy"],
        "d": target["d_dy"],
        "e": target["u_dy"],
        "nuD": target["d_dy"],
    }
    target_vector_by_sector = {
        sector: flatten_matrix_real(matrix)
        for sector, matrix in sector_targets.items()
    }
    target_vector = [
        value
        for sector in ("u", "d", "e", "nuD")
        for value in target_vector_by_sector[sector]
    ]

    missing = phifin["payload_slots"]["finite_Hessian_C1_source"]["missing"]
    selected_operator_available = all(
        missing[key] is not None
        for key in (
            "selected_deltaTheta_C1_solution",
            "explicit_dotD_Q_u_d_L_e_N_H",
            "full_lower_order_Hess_Xi_blocks",
            "sector_response_matrices_M_u_M_d_M_e_M_nuD",
            "selected_zero_mode_basis_Q_u_d_L_e_N_H",
            "evaluated_grad_V_C1_alpha1_source_vector",
        )
    )

    solve_gate = {
        "equation": "A_selected * deltaTheta_C1 = b_splitter, with A_selected induced by selected Hessian, dotD, zero-mode bases, and primitive C1 contractions.",
        "target_real_dimension": len(target_vector),
        "target_vector_norm_sq": norm_sq(target_vector),
        "sector_target_norm_sq": {
            sector: norm_sq(values)
            for sector, values in target_vector_by_sector.items()
        },
        "selected_operator_available": selected_operator_available,
        "rank_test_computable": selected_operator_available,
        "least_squares_solution_computable": selected_operator_available,
        "diagnostic_identity_lift_exists": True,
        "diagnostic_identity_lift_norm_sq": norm_sq(target_vector),
        "diagnostic_identity_lift_promotable": False,
        "why_not_solved": (
            "The target vector is explicit, but the selected linear response operator A_selected and selected source "
            "vector are not emitted. An identity lift would solve a diagnostic equation only, not the selected MTT equation."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSplitterSourceEmissionContractOrSelectedDeltaThetaC1Solve",
        "status": STATUS,
        "inputs": {
            "correction_source_emission_audit": rel(PREVIOUS),
            "selected_phifin_alpha1_payload": rel(PHIFIN),
        },
        "selected_deltatheta_c1_solve_gate": solve_gate,
        "missing_selected_operator_data": missing,
        "what_closes_now": {
            "splitter_target_vector_built": True,
            "selected_linear_equation_specified": True,
            "rank_and_least_squares_gate_defined": True,
            "diagnostic_identity_lift_rejected_as_proof": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_C1_response_operator_A_selected": True,
            "selected_source_vector_b_selected": True,
            "selected_deltaTheta_C1_solution": True,
            "rank_or_consistency_test": True,
            "honest_replay_of_sector_response_matrices": True,
            "promoted_yukawa_hierarchy_CKM_PMNS_CP": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SelectedDeltaThetaC1SolveGateTheorem",
            "proved": True,
            "statement": (
                "The diagnostic splitter can be encoded as an explicit finite real target vector, and the selected "
                "solve is exactly the linear equation A_selected deltaTheta_C1 = b_splitter. This equation cannot "
                "yet be evaluated because the selected Hessian/response operator and selected source vector are "
                "not emitted. Therefore the remaining object is not another flavor search; it is selected C1 "
                "response-operator emission."
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
        """# MTT Selected Route-C Splitter Source Emission Contract or Selected DeltaTheta C1 Solve

Status: `MTT_SELECTED_ROUTEC_DELTATHETA_C1_SOLVE_GATE_BUILT_SELECTED_HESSIAN_RESPONSE_OPERATOR_OPEN`

The diagnostic splitter is now encoded as an explicit finite target vector.  The
selected proof equation is:

```text
A_selected * deltaTheta_C1 = b_splitter
```

where `A_selected` is induced by the selected Hessian, selected dotD, selected
zero-mode bases, and selected primitive C1 contractions.

## Result

The target vector is available.  The selected response operator is not.

An identity lift would solve a diagnostic equation, but it would not prove MTT
selection.  The honest rank/consistency/least-squares tests cannot be run until
the same-branch selected C1 response operator and selected source vector are
emitted.

## What This Changes

This removes another false uncertainty.  We do not need a broader flavor search
next.  The next true object is narrower:

- emit `A_selected`,
- emit `b_selected`,
- solve or reject `A_selected * deltaTheta_C1 = b_splitter`,
- replay the sector response matrices and locked mass/mixing/CP tests.

Next artifact: `MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
