"""Build the hypercharge weights and typed convention gate for the U1/Y row."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "factorized_operator_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "hypercharge_interface": NONSM / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json",
    "hypercharge_embedding_gate": NONSM / "certificates" / "hypercharge_embedding_gate_certificate.json",
    "qc_circle": NONSM / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json",
    "su2_flat_fp": NONSM / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_HyperchargeWeights_TypedConvention_Gate_v1.md"

STATUS = "ELECTROWEAK_U1Y_TYPED_HYPERCHARGE_MAP_CLOSED_STACK_DETERMINANT_SOURCE_OPEN"
NEXT = "Selected_Electroweak_QaStack_Determinant_SourceEmission_or_U1YRowPromotion_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    attempt = load(INPUTS["factorized_operator_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    hyper = load(INPUTS["hypercharge_interface"])
    embedding = load(INPUTS["hypercharge_embedding_gate"])
    qc = load(INPUTS["qc_circle"])
    su2 = load(INPUTS["su2_flat_fp"])

    p_candidate = float(matrix["quotient_operator"]["logdet"])
    p_qc = float(qc["selected_values"]["selected_p_Qc_for_weak_split"])
    p_su2 = float(su2["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"])
    v1_tilde = float(hyper["selected_values"]["v1_tilde"])

    p_y_if_qa = p_candidate / 36.0 + p_qc / 4.0
    lambda_if_qa = p_y_if_qa - p_su2
    delta_g_if_qa = v1_tilde * lambda_if_qa / (4.0 * math.pi)

    direct_lambda = p_candidate - p_su2

    convention_map = {
        "hypercharge_embedding": hyper["source_formula"]["hypercharge_embedding"],
        "threshold_combination": hyper["source_formula"]["threshold_combination"],
        "weak_split": hyper["source_formula"]["weak_split"],
        "Delta_G_12": hyper["source_formula"]["Delta_G_12"],
        "selected_weights": {
            "Qa_stack_weight_in_pY": "1/36",
            "Qc_circle_weight_in_pY": "1/4",
            "SU2_weight_in_lambda12": "-1",
        },
        "selected_structurally": hyper["verdict"]["hypercharge_embedding_selected_structurally"],
    }

    route_tests = {
        "typed_hypercharge_stack_map": {
            "status": "CLOSED_STRUCTURAL_MAP",
            "accepted": True,
            "reason": "The selected hypercharge interface emits Y=(1/6)Qa-(1/2)Qc and p_Y=p_a/36+p_c/4 before electroweak comparison.",
        },
        "direct_U1Y_row_shortcut": {
            "status": "REJECTED_UNTYPED_DIRECT_ROW",
            "accepted": False,
            "diagnostic_lambda_if_used": direct_lambda,
            "reason": "The constructed quotient logdet is not source-typed as an already hypercharge-normalized p_Y row. Treating it as p_Y would bypass the selected Qa/Qc hypercharge map.",
        },
        "Qa_stack_interpretation_of_quotient_operator": {
            "status": "CONDITIONAL_NOT_PROMOTED",
            "accepted": False,
            "conditional_p_a": p_candidate,
            "conditional_p_Y": p_y_if_qa,
            "conditional_lambda_12": lambda_if_qa,
            "conditional_Delta_G_12": delta_g_if_qa,
            "reason": "This is the legal convention if the constructed factorized quotient operator is source-emitted as the Qa stack determinant. That source-emission/provenance remains open.",
        },
        "Qc_and_SU2_rows": {
            "status": "CLOSED_FOR_WEAK_SPLIT",
            "accepted": True,
            "p_Qc": p_qc,
            "p_SU2": p_su2,
            "reason": "Qc circle and SU2 flat FP quotient rows are selected for weak-split threshold accounting.",
        },
    }

    blocking_fields = [
        "selected source must emit the constructed quotient operator as the Qa stack determinant p_a, or emit a separately typed hypercharge-normalized p_Y row",
        "selected source emission of the exact A_base tensor I_3 matrix is still open",
        "regularization/scale statement must identify the quotient logdet convention with the p-row convention",
        "physical action anchor and RG/matching scale remain separate two-key requirements for measured electroweak closure",
    ]

    decision = {
        "typed_hypercharge_convention_map_closed": True,
        "hypercharge_index_weights_closed_structurally": True,
        "Qc_row_closed_for_weaksplit": True,
        "SU2_row_closed_for_weaksplit": True,
        "direct_U1Y_row_promoted": False,
        "Qa_stack_p_a_source_closed": False,
        "conditional_lambda12_if_quotient_is_p_a": lambda_if_qa,
        "conditional_Delta_G12_if_quotient_is_p_a": delta_g_if_qa,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YHyperchargeWeightsTypedConventionGate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "factorized_operator_attempt": attempt["status"],
            "hypercharge_interface": hyper["status"],
            "hypercharge_embedding_gate": embedding["status"],
            "qc_circle": qc["status"],
            "su2_flat_fp": su2["status"],
        },
        "typed_convention_map": convention_map,
        "route_tests": route_tests,
        "blocking_fields": blocking_fields,
        "decision": decision,
        "theorem": {
            "name": "ElectroweakU1YTypedHyperchargeConventionReduction",
            "proved": True,
            "statement": (
                "The hypercharge/index convention is structurally selected as "
                "p_Y=p_a/36+p_c/4 and lambda_12=p_Y-p_SU2. Qc and SU2 rows are "
                "closed for weak-split accounting. The constructed quotient determinant "
                "can enter this theorem only if source-emitted as p_a, or if a distinct "
                "source emits it as an already hypercharge-normalized p_Y row. Neither "
                "promotion is currently closed, so lambda_12 remains open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "promotes_direct_U1Y_row": False,
            "promotes_quotient_logdet_as_p_a": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YHyperchargeWeightsTypedConventionGate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "typed_hypercharge_convention_map": True,
            "hypercharge_index_weights_structural": True,
            "Qc_row_for_weaksplit": True,
            "SU2_row_for_weaksplit": True,
        },
        "open": {
            "Qa_stack_p_a_source_emission": True,
            "direct_hypercharge_normalized_pY_source_emission": True,
            "regularization_scale_p_row_identification": True,
            "lambda_12": True,
            "physical_action_anchor": True,
        },
        "conditional_lambda12_if_quotient_is_p_a": lambda_if_qa,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y HyperchargeWeights TypedConvention Gate v1

## Result

```text
status = {candidate["status"]}
typed_hypercharge_convention_map_closed = true
hypercharge_index_weights_closed_structurally = true
Qa_stack_p_a_source_closed = false
lambda_12_closed = false
```

## Typed Map

```json
{json.dumps(candidate["typed_convention_map"], indent=2, sort_keys=True)}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

The direct-row shortcut is rejected. The legal path is now precise: promote the
constructed quotient determinant as the selected `p_a` stack determinant, or
emit a distinct source-typed hypercharge-normalized `p_Y` row.

## Remaining Blockers

```json
{json.dumps(candidate["blocking_fields"], indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
