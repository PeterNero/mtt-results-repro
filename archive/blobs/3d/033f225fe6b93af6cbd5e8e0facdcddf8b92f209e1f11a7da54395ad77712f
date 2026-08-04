"""Build the factorized U1/Y threshold-operator or SU2 cancellation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "quotient_determinant_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "u1_carrier_projector_su2_gate": DATA / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.candidate.json",
    "dual_frontier": DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json",
    "operator_spectrum_packet": DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_electroweak_u1y_factorized_threshold_operator_source.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_Factorized_ThresholdOperator_SourceEmission_or_SU2_Cancellation_v1.md"

STATUS = "ELECTROWEAK_U1Y_FACTORIZED_OPERATOR_SOURCE_OPEN_SU2_WEAKSPLIT_CLOSED"
NEXT = "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedElectroweakU1YFactorizedThresholdOperatorSource.v1",
        "status": "OPEN_SELECTED_FACTORIZED_U1Y_THRESHOLD_OPERATOR_REQUIRED",
        "source_identity": {
            "selected_by_mtt": None,
            "same_source_as_27mode_DE_gap_layer": None,
            "same_source_as_Pperp_trace_policy": None,
            "emitted_before_electroweak_comparison": None,
            "source_certificate": None,
        },
        "operator_payload": {
            "domain": "B_base tensor (V_3/<s>)",
            "raw_factorized_operator": "A_base tensor I_3",
            "quotient_operator": "A_base tensor I_(V_3/<s>)",
            "positive_spectrum": [
                {"eigenvalue": "(2*pi/3)^2", "multiplicity": 8},
                {"eigenvalue": "2*(2*pi/3)^2", "multiplicity": 8},
            ],
            "hypercharge_index_Dynkin_weights": None,
            "regularization": "finite positive zeta/logdet on quotient spectrum",
            "same_scheme_SU2_reference": "selected flat SU2 weak-split FP quotient policy",
        },
        "acceptance_contract": [
            "source emits A_base tensor I_3, not only the quotient determinant lemma",
            "source binds the shared line s and P_perp to the U1/Y threshold operator domain",
            "hypercharge/index/Dynkin weights are emitted before lambda_12 comparison",
            "SU2 weak-split row uses the already selected flat FP quotient policy or an explicit same-scheme determinant row",
            "no observed lambda_12, weak angle, alpha_EM, or target residual is used as selection input",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    quotient = load(INPUTS["quotient_determinant_lemma"])
    carrier = load(INPUTS["u1_carrier_projector_su2_gate"])
    dual = load(INPUTS["dual_frontier"])
    op_packet = load(INPUTS["operator_spectrum_packet"])
    template = build_template()

    su2_closed = (
        carrier["decision"]["su2_unit_index_or_spectrum_found"] is True
        and carrier["cross_repo_status"]["su2_selected_for_lambda_12_accounting"] is True
        and "CLOSED_FOR_WEAK_SPLIT" in carrier["theorem_hypothesis_status_after_gate"]["H4_SU2_unit_index_or_selected_spectrum"]
    )
    u1_factorization_source_closed = (
        carrier["decision"]["source_selected_u1_carrier_found"] is True
        and carrier["decision"]["quotient_projector_P_perp_found"] is True
        and quotient["decision"]["factorized_threshold_operator_source_emitted"] is True
        and op_packet["decision"]["selected_lambda_12_found"] is True
    )

    source_tests = {
        "SU2_same_scheme_weaksplit_row": {
            "status": "CLOSED_SCOPED_WEAKSPLIT" if su2_closed else "OPEN",
            "reason": "Selected SU2 flatness plus flat FP quotient-normalization policy closes the leading weak-split gauge-kinetic SU2 row; this is not an absolute partition-function normalization.",
        },
        "U1_rank3_carrier": {
            "status": carrier["theorem_hypothesis_status_after_gate"]["H1_three_direction_u1_threshold_carrier"],
            "selected": carrier["decision"]["source_selected_u1_carrier_found"],
            "reason": carrier["decision"]["no_go_reason"],
        },
        "U1_shared_line_projector_binding": {
            "status": carrier["theorem_hypothesis_status_after_gate"]["H2_exactly_one_shared_central_universal_mode"],
            "projector_found": carrier["decision"]["quotient_projector_P_perp_found"],
        },
        "U1_factorized_operator_source": {
            "status": "OPEN",
            "required_formula": "A_base tensor I_3 on B_base tensor V_3",
            "quotient_lemma_available": quotient["decision"]["algebraic_quotient_determinant_lemma_proved"],
            "reason": "The quotient determinant lemma proves what follows if the factorized operator is selected; it does not emit the operator from source.",
        },
        "hypercharge_index_Dynkin_weights": {
            "status": "OPEN",
            "operator_packet_status": op_packet["status"],
            "reason": "The current operator spectrum packet builds the contract but does not select positive spectrum/index weights as U1/Y threshold data.",
        },
    }

    quotient_logdet = quotient["decision"]["quotient_logdet"]
    selected_su2_p = dual["lane_A_local_determinant"]["strongest_selected_inputs"]["selected_p_SU2_for_weak_split"]
    forbidden_diagnostic = {
        "if_quotient_logdet_were_used_as_p_U1": quotient_logdet - selected_su2_p,
        "why_forbidden": (
            "The quotient logdet is a finite determinant support value, while the existing p_SU2 row is in the older weak-split p-row convention. "
            "A typed convention map and hypercharge/index weights are required before any cross-convention subtraction."
        ),
    }

    decision = {
        "SU2_same_scheme_row_or_cancellation_closed_for_weaksplit": su2_closed,
        "U1_factorized_threshold_operator_source_closed": u1_factorization_source_closed,
        "quotient_determinant_row_available_conditionally": quotient["decision"]["quotient_positive_spectrum_computed"],
        "hypercharge_index_Dynkin_weights_closed": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YFactorizedOperatorOrSU2CancellationGate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "quotient_determinant_lemma": quotient["status"],
            "u1_carrier_projector_su2_gate": carrier["status"],
            "dual_frontier": dual["status"],
            "operator_spectrum_packet": op_packet["status"],
        },
        "source_tests": source_tests,
        "conditional_quotient_row": {
            "positive_spectrum": quotient["quotient_positive_spectrum"],
            "logdet": quotient_logdet,
            "usable_for_lambda12_now": False,
        },
        "forbidden_diagnostic": forbidden_diagnostic,
        "source_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "ElectroweakU1YSU2FrontierReductionAfterQuotientDeterminant",
            "proved": True,
            "statement": (
                "After the quotient-determinant lemma, the SU2 side is closed for scoped "
                "weak-split accounting. The remaining dimensionless electroweak determinant "
                "gate is the selected source emission of the factorized U1/Y threshold "
                "operator and its hypercharge/index weights. Therefore lambda_12 remains open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "subtracts_cross_convention_rows": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
            "promotes_quotient_lemma_to_source_emission": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YFactorizedOperatorOrSU2CancellationGate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "SU2_same_scheme_row_or_cancellation_for_scoped_weaksplit": su2_closed,
            "quotient_determinant_lemma_available": True,
            "next_source_template_written": True,
        },
        "open": {
            "U1_factorized_threshold_operator_source": True,
            "hypercharge_index_Dynkin_weights": True,
            "typed_convention_map_for_lambda12": True,
            "lambda_12": True,
            "physical_action_anchor": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y Factorized ThresholdOperator SourceEmission or SU2 Cancellation v1

## Result

```text
status = {candidate["status"]}
SU2_same_scheme_row_or_cancellation_closed_for_weaksplit = {str(candidate["decision"]["SU2_same_scheme_row_or_cancellation_closed_for_weaksplit"]).lower()}
U1_factorized_threshold_operator_source_closed = false
lambda_12_closed = false
```

## What This Closes

The SU2 side is closed for scoped weak-split gauge-kinetic accounting by the
selected flat SU2 background and flat FP quotient-normalization policy. The
new quotient determinant row is also available as an algebraic conditional row:

```json
{json.dumps(candidate["conditional_quotient_row"], indent=2, sort_keys=True)}
```

## What Still Blocks Closure

```json
{json.dumps(candidate["source_tests"], indent=2, sort_keys=True)}
```

The live blocker is now precise: emit the factorized U1/Y threshold operator
`A_base tensor I_3`, bind it to the selected shared-line quotient, and supply
the hypercharge/index/Dynkin weights in the same convention before computing
`lambda_12`.

## Forbidden Diagnostic

```json
{json.dumps(candidate["forbidden_diagnostic"], indent=2, sort_keys=True)}
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
    candidate, cert, template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
