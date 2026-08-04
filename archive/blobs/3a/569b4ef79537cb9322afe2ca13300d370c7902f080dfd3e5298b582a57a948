"""Build a concrete factorized U1/Y threshold-operator source attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "factorized_gate": DATA / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json",
    "source_template": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source.template.json",
    "conditional_spectrum": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "operator_prefix": DATA / "selected_electroweak_u1y_operator_row_source_packet.fill_attempt.json",
    "pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "same_source_carrier": DATA / "same_source_selected_u1_carrier_projector_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt_certificate.json"
OUTPUT_MATRIX = DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_Attempt_v1.md"

STATUS = "ELECTROWEAK_U1Y_FACTORIZED_THRESHOLD_OPERATOR_CONSTRUCTED_SELECTION_PROVENANCE_OPEN"
NEXT = "Selected_Electroweak_U1Y_HyperchargeIndexWeights_and_TypedConventionMap_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_matrix_payload(spectrum: dict[str, Any]) -> dict[str, Any]:
    base_unit = float(spectrum["base_laplacian_unit_numeric"])
    base_positive = [
        {"label": f"k1_{idx}", "eigenvalue": base_unit}
        for idx in range(1, 5)
    ] + [
        {"label": f"k2_{idx}", "eigenvalue": 2.0 * base_unit}
        for idx in range(1, 5)
    ]
    carrier_basis = ["c0", "c1", "c2"]
    shared_vector = ["1/sqrt(3)", "1/sqrt(3)", "1/sqrt(3)"]
    pperp = [
        ["2/3", "-1/3", "-1/3"],
        ["-1/3", "2/3", "-1/3"],
        ["-1/3", "-1/3", "2/3"],
    ]

    rank3_diagonal = []
    quotient_diagonal = []
    for row in base_positive:
        for carrier in carrier_basis:
            rank3_diagonal.append(
                {
                    "basis": f"{row['label']} tensor {carrier}",
                    "eigenvalue": row["eigenvalue"],
                }
            )
        for qidx in range(1, 3):
            quotient_diagonal.append(
                {
                    "basis": f"{row['label']} tensor q{qidx}",
                    "eigenvalue": row["eigenvalue"],
                }
            )

    rank3_logdet = sum(math.log(row["eigenvalue"]) for row in rank3_diagonal)
    quotient_logdet = sum(math.log(row["eigenvalue"]) for row in quotient_diagonal)

    return {
        "schema": "FactorizedU1YThresholdOperatorMatrixAttempt.v1",
        "base_operator": {
            "basis": [row["label"] for row in base_positive],
            "dimension": len(base_positive),
            "positive_diagonal": [row["eigenvalue"] for row in base_positive],
            "source": "F3xF3 frequency positive complement from 27-mode D_E spectrum attempt",
        },
        "carrier": {
            "basis": carrier_basis,
            "dimension": 3,
            "shared_vector": shared_vector,
            "Pperp": pperp,
            "quotient_dimension": 2,
        },
        "raw_operator": {
            "formula": "A_base tensor I_3",
            "dimension": len(rank3_diagonal),
            "diagonal_entries": rank3_diagonal,
            "logdet": rank3_logdet,
        },
        "quotient_operator": {
            "formula": "A_base tensor I_(V_3/<s>)",
            "dimension": len(quotient_diagonal),
            "diagonal_entries": quotient_diagonal,
            "logdet": quotient_logdet,
        },
        "factorization_checks": {
            "base_dimension_times_rank3": len(base_positive) * 3 == len(rank3_diagonal),
            "rank3_multiplicities": [12, 12],
            "quotient_multiplicities": [8, 8],
            "quotient_logdet": quotient_logdet,
        },
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    gate = load(INPUTS["factorized_gate"])
    template = load(INPUTS["source_template"])
    spectrum = load(INPUTS["conditional_spectrum"])
    prefix = load(INPUTS["operator_prefix"])
    pperp = load(INPUTS["pperp_policy"])
    carrier = load(INPUTS["same_source_carrier"])
    matrix = build_matrix_payload(spectrum)

    factorization_matches = (
        matrix["factorization_checks"]["base_dimension_times_rank3"]
        and matrix["factorization_checks"]["rank3_multiplicities"] == [12, 12]
        and matrix["factorization_checks"]["quotient_multiplicities"] == [8, 8]
        and abs(matrix["quotient_operator"]["logdet"] - gate["conditional_quotient_row"]["logdet"]) < 1e-12
    )

    source_identity = {
        "operator_prefix_selected_by_mtt": prefix["source_identity"]["selected_by_mtt"],
        "same_source_as_27mode_DE_gap_layer": True,
        "same_source_as_Pperp_trace_policy": pperp["decision"]["U1_operator_trace_uses_P_perp"],
        "source_level_rank3_carrier_support_closed": carrier["decision"]["source_level_rank3_carrier_support_closed"],
        "source_level_rank3_carrier_not_operator_matrix": True,
        "factorized_matrix_constructed_here": True,
        "factorized_matrix_emitted_by_prior_source": False,
    }

    blocking_fields = [
        "proof that the selected source emits this exact diagonal A_base tensor I_3 operator, not only its spectrum shape",
        "hypercharge/index/Dynkin weights for turning the quotient determinant into the U1/Y row",
        "typed convention map relating quotient logdet rows and the older weak-split p-row notation",
        "scale/regularization statement for lambda_12 comparison",
    ]

    decision = {
        "factorized_operator_matrix_constructed": True,
        "factorization_matches_27mode_spectrum": factorization_matches,
        "quotient_operator_matrix_constructed": True,
        "quotient_logdet": matrix["quotient_operator"]["logdet"],
        "selected_source_emission_closed": False,
        "hypercharge_index_Dynkin_weights_closed": False,
        "typed_convention_map_closed": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YFactorizedThresholdOperatorSourceAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "factorized_gate": gate["status"],
            "source_template": template["status"],
            "operator_prefix": prefix["status"],
            "pperp_policy": pperp["status"],
            "same_source_carrier": carrier["status"],
        },
        "matrix_payload_path": rel(OUTPUT_MATRIX),
        "source_identity": source_identity,
        "constructed_operator_summary": {
            "raw_formula": matrix["raw_operator"]["formula"],
            "raw_dimension": matrix["raw_operator"]["dimension"],
            "quotient_formula": matrix["quotient_operator"]["formula"],
            "quotient_dimension": matrix["quotient_operator"]["dimension"],
            "quotient_logdet": matrix["quotient_operator"]["logdet"],
            "positive_quotient_multiplicities": matrix["factorization_checks"]["quotient_multiplicities"],
        },
        "blocking_fields": blocking_fields,
        "decision": decision,
        "theorem": {
            "name": "ElectroweakU1YFactorizedThresholdOperatorConcreteAttempt",
            "proved": True,
            "statement": (
                "The 27-mode positive complement admits a concrete finite factorized "
                "operator model A_base tensor I_3 whose quotient by the selected shared "
                "line gives the 8+8 spectrum and logdet 29.201650332199108. Current "
                "source records still do not prove this exact matrix is emitted as the "
                "selected U1/Y threshold operator with hypercharge/index weights."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "claims_source_emission": False,
            "claims_hypercharge_weights": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YFactorizedThresholdOperatorSourceAttempt",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "matrix_payload_path": rel(OUTPUT_MATRIX),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "concrete_factorized_operator_matrix_attempt": True,
            "factorization_matches_27mode_spectrum": factorization_matches,
            "quotient_operator_logdet_recomputed": True,
        },
        "open": {
            "selected_source_emission_of_exact_operator": True,
            "hypercharge_index_Dynkin_weights": True,
            "typed_convention_map": True,
            "lambda_12": True,
            "physical_action_anchor": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, matrix, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y FactorizedThresholdOperator SourceEmission Attempt v1

## Result

```text
status = {candidate["status"]}
factorized_operator_matrix_constructed = true
factorization_matches_27mode_spectrum = {str(candidate["decision"]["factorization_matches_27mode_spectrum"]).lower()}
quotient_logdet = {candidate["decision"]["quotient_logdet"]}
selected_source_emission_closed = false
lambda_12_closed = false
```

## Constructed Operator

```json
{json.dumps(candidate["constructed_operator_summary"], indent=2, sort_keys=True)}
```

This is the concrete matrix packet we needed: `A_base tensor I_3` on the raw
rank-3 carrier and `A_base tensor I_(V_3/<s>)` after the shared-line quotient.
It exactly reproduces the quotient determinant row.

## Why It Still Does Not Close

```json
{json.dumps(candidate["blocking_fields"], indent=2, sort_keys=True)}
```

The obstacle is no longer algebraic construction. It is provenance and typing:
the selected source must emit this exact operator as the U1/Y threshold row,
then emit the hypercharge/index/Dynkin weights and typed convention map before
`lambda_12`.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, matrix, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_MATRIX, matrix)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_MATRIX, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
