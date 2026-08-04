from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_correction_source_emission_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_deltatheta_c1_solve_gate_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_deltatheta_c1_solve_gate_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_DeltaTheta_C1_Solve_Gate_Import_v1.md"

STATUS = "ROUTEC_DELTATHETA_C1_SOLVE_GATE_IMPORTED_SELECTED_RESPONSE_OPERATOR_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    gate = src["selected_deltatheta_c1_solve_gate"]
    missing = src["missing_selected_operator_data"]

    closed_now = {
        "previous_source_emission_contract_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "splitter_target_vector_built": src_cert["what_closes"]["splitter_target_vector_built"],
        "selected_linear_equation_specified": src_cert["what_closes"][
            "selected_linear_equation_specified"
        ],
        "rank_and_least_squares_gate_defined": src_cert["what_closes"][
            "rank_and_least_squares_gate_defined"
        ],
        "diagnostic_identity_lift_rejected_as_proof": src_cert["what_closes"][
            "diagnostic_identity_lift_rejected_as_proof"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    target_checks = {
        "target_real_dimension_72": gate["target_real_dimension"] == 72,
        "target_vector_norm_sq_positive": gate["target_vector_norm_sq"] > 0,
        "target_vector_norm_sq_24": gate["target_vector_norm_sq"] == 24.0,
        "sector_targets_all_norm_sq_6": all(value == 6.0 for value in gate["sector_target_norm_sq"].values()),
        "equation_names_A_selected": "A_selected" in gate["equation"],
        "equation_names_deltaTheta_C1": "deltaTheta_C1" in gate["equation"],
        "equation_names_b_splitter": "b_splitter" in gate["equation"],
    }

    selected_operator_checks = {
        "selected_operator_not_available": gate["selected_operator_available"] is False,
        "rank_test_not_computable": gate["rank_test_computable"] is False,
        "least_squares_not_computable": gate["least_squares_solution_computable"] is False,
        "selected_deltaTheta_missing": missing["selected_deltaTheta_C1_solution"] is None,
        "sector_response_matrices_missing": missing["sector_response_matrices_M_u_M_d_M_e_M_nuD"] is None,
        "selected_zero_modes_missing": missing["selected_zero_mode_basis_Q_u_d_L_e_N_H"] is None,
        "selected_dotD_missing": missing["explicit_dotD_Q_u_d_L_e_N_H"] is None,
        "hessian_blocks_missing": missing["full_lower_order_Hess_Xi_blocks"] is None,
    }

    diagnostic_checks = {
        "diagnostic_identity_lift_exists": gate["diagnostic_identity_lift_exists"] is True,
        "diagnostic_identity_lift_norm_matches_target": gate["diagnostic_identity_lift_norm_sq"]
        == gate["target_vector_norm_sq"],
        "diagnostic_identity_lift_not_promotable": gate["diagnostic_identity_lift_promotable"] is False,
    }

    open_gate_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_selected_c1_response_operator": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCDeltaThetaC1SolveGateImportTheorem",
        "proved": all(closed_now.values())
        and all(target_checks.values())
        and all(selected_operator_checks.values())
        and all(diagnostic_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported DeltaTheta C1 solve gate builds the explicit 72-real-dimensional "
            "splitter target and specifies the selected proof equation "
            "A_selected deltaTheta_C1 = b_splitter. The equation cannot yet be "
            "evaluated because selected A_selected and b_selected are not emitted. "
            "The identity lift is rejected as diagnostic only, so the next object is "
            "selected C1 response-operator emission."
        ),
    }

    verdict = {
        "splitter_target_vector_built": True,
        "target_real_dimension": gate["target_real_dimension"],
        "target_vector_norm_sq": gate["target_vector_norm_sq"],
        "selected_operator_available": False,
        "rank_test_computable": False,
        "least_squares_solution_computable": False,
        "diagnostic_identity_lift_promotable": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "target_checks": target_checks,
        "selected_operator_checks": selected_operator_checks,
        "diagnostic_checks": diagnostic_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "selected_deltatheta_c1_solve_gate": gate,
        "missing_selected_operator_data": missing,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C DeltaTheta C1 Solve Gate Import v1

## Result

The diagnostic splitter is now encoded as an explicit finite real target vector.
The selected proof equation is:

```text
A_selected * deltaTheta_C1 = b_splitter
```

The target has real dimension `72` and norm square `24`, with four sector target
blocks of norm square `6`.

## Boundary

The selected response operator is not available. The rank, consistency, and
least-squares tests cannot be run until `A_selected` and `b_selected` are
emitted from selected Hessian, selected dotD, selected zero-mode bases, and
selected primitive C1 contractions.

The identity lift is diagnostic only and is rejected as proof data.

## Status

```text
ROUTEC_DELTATHETA_C1_SOLVE_GATE_IMPORTED_SELECTED_RESPONSE_OPERATOR_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_deltatheta_c1_solve_gate_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_correction_source_emission_import": str(PREV_IMPORT),
                    "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "target_checks": target_checks,
                "selected_operator_checks": selected_operator_checks,
                "diagnostic_checks": diagnostic_checks,
                "open_gate_checks": open_gate_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
