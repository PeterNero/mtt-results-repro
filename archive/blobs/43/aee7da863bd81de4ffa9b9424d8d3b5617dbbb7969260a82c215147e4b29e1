"""Build the Qa-stack determinant or direct U1/Y-row promotion gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "typed_hypercharge_gate": DATA / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
    "factorized_operator_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "local_det_interface": NONSM / "certificates" / "selected_local_determinant_computation_interface_certificate.json",
    "qaqcsu2_heat_table": NONSM / "certificates" / "selected_qaqcsu2_operator_spectra_or_heat_coefficients_certificate.json",
    "qa_nil_reduction": NONSM / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json",
    "qa_brst_weitz": NONSM / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_determinant_or_u1yrow_promotion.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_determinant_or_u1yrow_promotion_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_electroweak_qastack_or_u1yrow_source_payload.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_Determinant_SourceEmission_or_U1YRowPromotion_v1.md"

STATUS = "ELECTROWEAK_QASTACK_OR_U1YROW_PROMOTION_GATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Electroweak_QaStack_or_U1YRow_SourcePayload_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedElectroweakQaStackOrU1YRowSourcePayload.v1",
        "status": "OPEN_SELECTED_QASTACK_OR_U1YROW_SOURCE_PAYLOAD_REQUIRED",
        "allowed_promotion_routes": {
            "Qa_stack_route": {
                "required_source_identity": None,
                "required_operator": "source-emitted factorized quotient operator as p_a",
                "required_formula": "p_Y = p_a/36 + p_c/4",
                "required_regularization": "same p-row zeta/heat finite-part convention as Qc and SU2",
            },
            "direct_pY_route": {
                "required_source_identity": None,
                "required_operator": "source-emitted hypercharge-normalized U1/Y threshold operator",
                "required_formula": "lambda_12 = p_Y - p_SU2",
                "must_not_bypass_Qa_Qc_map_without_source": True,
            },
        },
        "must_not_use": [
            "observed lambda_12, weak angle, alpha_EM, masses, or residuals",
            "proxy scalar Nil spectrum as selected Qa determinant",
            "target-required p_a as selected value",
            "direct quotient logdet as p_Y without source typing",
            "Qa/SU3 log(2008) internal determinant as hypercharge determinant",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    typed = load(INPUTS["typed_hypercharge_gate"])
    factorized = load(INPUTS["factorized_operator_attempt"])
    local = load(INPUTS["local_det_interface"])
    heat = load(INPUTS["qaqcsu2_heat_table"])
    nil = load(INPUTS["qa_nil_reduction"])
    brst = load(INPUTS["qa_brst_weitz"])
    template = build_template()

    conditional = typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]
    heat_q_a = heat["block_status"]["D_Qa"]
    closest = brst["closest_unforbidden_candidate"]
    forbidden_ref = brst["forbidden_reference"]

    route_tests = {
        "new_factorized_quotient_as_Qa_stack": {
            "status": "CONDITIONAL_NOT_PROMOTED",
            "accepted": False,
            "p_a": conditional["conditional_p_a"],
            "lambda_12": conditional["conditional_lambda_12"],
            "needed": [
                "source emits exact A_base tensor I_3 matrix as Qa stack threshold operator",
                "regularization identifies quotient logdet with p_a finite part",
            ],
            "current_blocker": factorized["blocking_fields"][0],
        },
        "direct_hypercharge_normalized_pY_row": {
            "status": "OPEN_NO_SOURCE_ROW",
            "accepted": False,
            "reason": "No source-emitted p_Y operator row exists; direct use of the quotient logdet as p_Y was rejected by the typed convention gate.",
        },
        "old_Qa_heat_proxy_table": {
            "status": heat_q_a["spectrum_or_heat_data_status"],
            "accepted": False,
            "p_a_candidate": heat_q_a["heat_weighted_finite_part_candidate"],
            "reason": "Useful comparator, but its own certificate says exact selected Qa spectra/weights are missing.",
        },
        "old_nil_reduction": {
            "status": nil["status"],
            "accepted": False,
            "old_proxy_heat_weighted_p_a": nil["old_proxy_comparison"]["heat_weighted_proxy_p_a"],
            "reason": "It computes diagnostic oscillator branches and exact target-required Qa, but does not select compact Nil multiplicities or the Qa gauge/ghost quotient.",
        },
        "old_BRST_Weitzenbock_table": {
            "status": brst["status"],
            "accepted": False,
            "closest_unforbidden": closest,
            "forbidden_target_reference": forbidden_ref["name"],
            "reason": "The closest candidate is diagnostic and the exact target reference is explicitly forbidden target insertion.",
        },
    }

    decision = {
        "promotion_gate_built": True,
        "Qa_stack_route_promoted": False,
        "direct_pY_route_promoted": False,
        "local_determinant_accounting_interface_closed": local["verdict"]["determinant_accounting_interface_closed"],
        "selected_Qa_or_pY_source_payload_found": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackDeterminantOrU1YRowPromotion",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "typed_hypercharge_gate": typed["status"],
            "factorized_operator_attempt": factorized["status"],
            "local_det_interface": local["status"],
            "qaqcsu2_heat_table": heat["status"],
            "qa_nil_reduction": nil["status"],
            "qa_brst_weitz": brst["status"],
        },
        "route_tests": route_tests,
        "source_payload_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "ElectroweakQaStackOrU1YRowPromotionGate",
            "proved": True,
            "statement": (
                "With Qc, SU2, and the typed hypercharge map closed, lambda_12 now "
                "requires exactly one missing source payload: either the constructed "
                "factorized quotient determinant is emitted as the selected Qa stack "
                "p_a, or a distinct source emits an already hypercharge-normalized p_Y "
                "row. Current proxy/BRST/Nil tables do not close either route."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "promotes_proxy_Qa_table": False,
            "promotes_target_required_Qa": False,
            "promotes_quotient_logdet_as_p_a": False,
            "promotes_direct_pY": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackDeterminantOrU1YRowPromotion",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "promotion_gate": True,
            "old_proxy_routes_rejected_for_closure": True,
            "source_payload_template_written": True,
        },
        "open": {
            "Qa_stack_source_payload": True,
            "direct_pY_source_payload": True,
            "lambda_12": True,
            "physical_action_anchor": True,
            "RG_matching_scheme": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak QaStack Determinant SourceEmission or U1YRowPromotion v1

## Result

```text
status = {candidate["status"]}
Qa_stack_route_promoted = false
direct_pY_route_promoted = false
lambda_12_closed = false
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

The promotion problem is now a single source-payload problem. Either the new
factorized quotient determinant must be emitted as selected `p_a`, or a
separate source must emit a typed hypercharge-normalized `p_Y` row.

## Next Payload

```text
{candidate["decision"]["next_required_artifact"]}
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
