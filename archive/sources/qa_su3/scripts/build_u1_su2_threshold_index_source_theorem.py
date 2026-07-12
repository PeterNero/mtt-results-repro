"""Build the U1/SU2 threshold-index source theorem.

The theorem explains the source meaning of the motivated 2/3 U1 weight:
if the selected U1 threshold carrier has three isotropic modal directions and
one direction is the shared central-circle universal mode removed by the
physical quotient, the normalized U1 threshold trace weight is 2/3.

This is deliberately conditional.  The current corpus supports the central
circle neutrality principle, but it has not yet supplied the selected U1
threshold carrier/operator/spectrum that would promote the theorem to
electroweak closure.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PREVIOUS = DATA / "u1_su2_source_response_or_normalization_index_run.candidate.json"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

CENTRAL_FILTER = Q79 / "candidate_data" / "central_circle_neutral_terminal_lane_filter.candidate.json"
STACK_STATUS = NONSM / "certificates" / "selected_stack_determinant_source_status_certificate.json"
SU2_GHOST = NONSM / "certificates" / "selected_su2_nonabelian_ghost_quotient_determinant_certificate.json"
HYPERCHARGE = NONSM / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json"

OUTPUT_DATA = DATA / "u1_su2_threshold_index_source_theorem.candidate.json"
OUTPUT_CERT = CERTS / "u1_su2_threshold_index_source_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_SU2_Threshold_Index_Source_Selector_or_Operator_Spectrum_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def trace_quotient_weight(total_directions: int, universal_shared_directions: int) -> Fraction:
    if total_directions <= 0:
        raise ValueError("total_directions must be positive")
    if universal_shared_directions < 0 or universal_shared_directions > total_directions:
        raise ValueError("universal_shared_directions must be between 0 and total_directions")
    return Fraction(total_directions - universal_shared_directions, total_directions)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    previous = load(PREVIOUS)
    central = load(CENTRAL_FILTER)
    stack = load(STACK_STATUS)
    su2 = load(SU2_GHOST)
    hypercharge = load(HYPERCHARGE)

    weight = trace_quotient_weight(3, 1)
    source_theorem = {
        "name": "SharedCentralCircleQuotientSelectsTwoThirdsU1ThresholdWeight",
        "statement": (
            "For a selected U1 threshold carrier with three isotropic modal directions, "
            "if exactly one direction is the shared central-circle universal mode and "
            "the physical quotient removes that universal mode before determinant "
            "evaluation, then the normalized U1 threshold index is (3-1)/3=2/3."
        ),
        "proof_steps": [
            "Model the raw U1 threshold carrier as a 3-dimensional isotropic trace space V.",
            "Let s be the selected shared central-circle universal direction.",
            "The physical quotient for weak-split thresholds uses P_perp = I - |s><s|/<s,s>.",
            "The normalized trace weight is Tr(P_perp)/Tr(I_V).",
            "Since rank(P_perp)=2 and dim(V)=3, the weight is 2/3.",
            "This quotient is source-based only if s is selected before electroweak comparison and the selected U1 operator uses this quotient trace.",
        ],
        "derived_weight": {
            "U1": f"{weight.numerator}/{weight.denominator}",
            "SU2": "1/1",
        },
    }

    corpus_support = {
        "central_circle_neutrality": {
            "source": str(CENTRAL_FILTER),
            "status": central["status"],
            "supports_unique_shared_channel": central["corpus_support"]["checks"]["central_circle_unique_shared_channel"],
            "supports_gauge_neutrality": central["corpus_support"]["checks"]["gauge_forces_do_not_strain_central_circle"],
            "selector_still_open": central["what_this_does_not_close"]["actual_terminal_monad_lane_source_principle"] is False,
        },
        "hypercharge_structure": {
            "source": str(HYPERCHARGE),
            "status": hypercharge["status"],
            "selected_embedding": hypercharge["source_formula"]["hypercharge_embedding"],
            "determinant_amplitudes_selected": hypercharge["verdict"]["determinant_amplitudes_selected"],
        },
        "stack_determinants": {
            "source": str(STACK_STATUS),
            "status": stack["status"],
            "hypercharge_structure_source_certified": stack["verdict"]["hypercharge_structure_source_certified"],
            "stack_determinant_values_source_certified": stack["verdict"]["stack_determinant_values_source_certified"],
        },
        "su2_quotient": {
            "source": str(SU2_GHOST),
            "status": su2["status"],
            "su2_ghost_quotient_closed": su2["verdict"]["su2_ghost_quotient_closed"],
            "flat_zero_extra_branch_identified": su2["verdict"]["flat_zero_extra_branch_identified"],
        },
    }

    promotion_hypotheses = [
        {
            "id": "H1_three_direction_u1_threshold_carrier",
            "required": "selected U1 threshold carrier is a 3-direction isotropic modal trace space",
            "current_status": "OPEN",
            "reason": "current sources describe circle/lens/nil and hypercharge structure but do not emit the selected U1 threshold trace carrier",
        },
        {
            "id": "H2_exactly_one_shared_central_universal_mode",
            "required": "one and only one U1 threshold direction is the shared central-circle universal mode",
            "current_status": "PARTIAL_SUPPORT",
            "reason": "central-circle neutrality is source-supported, but not yet tied to the U1 threshold operator domain",
        },
        {
            "id": "H3_physical_quotient_removes_shared_mode",
            "required": "the weak-split determinant quotient removes the universal shared mode before finite determinant evaluation",
            "current_status": "OPEN",
            "reason": "the current physical quotient/projector schema is built, but the selected U1 kernel/projector is not supplied",
        },
        {
            "id": "H4_SU2_unit_index_or_selected_spectrum",
            "required": "SU2 threshold weight is selected as 1 in this index comparison, or the selected SU2 spectrum replaces the index model",
            "current_status": "OPEN",
            "reason": "SU2 flat/universal FP branch is identified but not selected; non-flat branch still requires spectrum",
        },
        {
            "id": "H5_no_target_selection",
            "required": "the quotient and index are selected without using lambda_12 or measured electroweak data",
            "current_status": "CLOSED_FOR_THIS_THEOREM",
            "reason": "the theorem derives 2/3 from rank quotient only and does not use the diagnostic target",
        },
    ]

    all_required_promoted = all(item["current_status"] in {"CLOSED", "CLOSED_FOR_THIS_THEOREM"} for item in promotion_hypotheses)
    decision = {
        "source_theorem_built": True,
        "derived_U1_weight": "2/3",
        "derived_SU2_weight": "1/1",
        "uses_electroweak_target": False,
        "central_circle_support_present": True,
        "promoted_to_selected_threshold_index": all_required_promoted,
        "I_1_I_2_payloads_filled": False,
        "measured_electroweak_closure": False,
        "documentation_for_later": "Use this theorem as the promotion test for any future claim that 2/3 is source-selected.",
        "next_required_object": "Selected_U1_Threshold_Carrier_Projector_or_SU2_Operator_Spectrum_v1",
    }

    candidate = {
        "candidate": "SelectedU1SU2ThresholdIndexSourceTheorem",
        "status": "U1_SU2_TWO_THIRDS_SOURCE_THEOREM_BUILT_PROMOTION_HYPOTHESES_OPEN",
        "inputs": {
            "previous_index_run": str(PREVIOUS.relative_to(ROOT)),
            "central_circle_filter": str(CENTRAL_FILTER),
            "stack_status": str(STACK_STATUS),
            "su2_ghost_quotient": str(SU2_GHOST),
            "hypercharge_interface": str(HYPERCHARGE),
        },
        "source_theorem": source_theorem,
        "corpus_support": corpus_support,
        "promotion_hypotheses": promotion_hypotheses,
        "comparison_to_previous_index_run": {
            "previous_best_source_motivated_index": previous["decision"]["best_source_motivated_index"],
            "previous_best_source_motivated_residual": previous["decision"]["best_source_motivated_residual"],
            "theorem_explains_candidate": previous["decision"]["best_source_motivated_index"] == "complex_nesting_or_shared_circle_2_3",
            "theorem_promotes_candidate_now": decision["promoted_to_selected_threshold_index"],
        },
        "decision": decision,
        "guardrails": [
            "This theorem is not an electroweak fit and does not use lambda_12 as input.",
            "Do not promote 2/3 until the selected U1 threshold carrier/projector is supplied.",
            "Do not assume SU2 weight 1 if the selected SU2 operator spectrum or FP quotient changes it.",
            "Target-near rational hits remain rejected unless a separate source theorem selects them.",
        ],
        "later_documentation_contract": {
            "when_to_use": "Use when a future artifact claims 2/3 from shared-circle or complex-nesting structure.",
            "must_cite": str(OUTPUT_NOTE.relative_to(ROOT)),
            "must_fill_before_promotion": [item["id"] for item in promotion_hypotheses if item["current_status"] not in {"CLOSED", "CLOSED_FOR_THIS_THEOREM"}],
        },
        "closure_claimed": True,
        "closure_scope": "conditional_source_theorem_for_2_3_index_and_later_promotion_contract",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1SU2ThresholdIndexSourceTheorem",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "conditional_2_3_source_theorem": True,
            "rank_quotient_derivation": "Tr(P_perp)/Tr(I)=2/3",
            "central_circle_support_imported": True,
            "later_promotion_contract_documented": True,
        },
        "what_remains_open": {
            "selected_U1_threshold_carrier_projector": True,
            "selected_U1_operator_spectrum_or_determinant": True,
            "selected_SU2_unit_index_or_operator_spectrum": True,
            "K_gauge_anchor": True,
            "I1_I2_payloads": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    theorem = candidate["source_theorem"]
    decision = candidate["decision"]
    hypotheses = "\n".join(
        f"- `{item['id']}`: {item['current_status']} - {item['required']}\n  Reason: {item['reason']}"
        for item in candidate["promotion_hypotheses"]
    )
    proof = "\n".join(f"- {item}" for item in theorem["proof_steps"])
    support = "\n".join(
        f"- `{key}`: {value['status'] if isinstance(value, dict) and 'status' in value else value}"
        for key, value in candidate["corpus_support"].items()
    )
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    later = candidate["later_documentation_contract"]
    missing = "\n".join(f"- `{item}`" for item in later["must_fill_before_promotion"])
    return f"""# Selected U1/SU2 Threshold Index Source Selector or Operator Spectrum v1

## Result

This artifact adds the source theorem for the motivated `2/3` U1 threshold
index.  It does not yet promote `2/3` to selected electroweak closure.

Derived source index:

```text
U1 = {theorem["derived_weight"]["U1"]}
SU2 = {theorem["derived_weight"]["SU2"]}
```

## Source Theorem

```text
{theorem["name"]}
```

Statement:

```text
{theorem["statement"]}
```

Proof:

{proof}

## Corpus Support

{support}

## Promotion Hypotheses

{hypotheses}

## Decision

```text
source_theorem_built = {str(decision["source_theorem_built"]).lower()}
derived_U1_weight = {decision["derived_U1_weight"]}
uses_electroweak_target = {str(decision["uses_electroweak_target"]).lower()}
promoted_to_selected_threshold_index = {str(decision["promoted_to_selected_threshold_index"]).lower()}
I_1_I_2_payloads_filled = {str(decision["I_1_I_2_payloads_filled"]).lower()}
measured_electroweak_closure = {str(decision["measured_electroweak_closure"]).lower()}
```

## Documentation Contract For Later

When a later artifact claims that `2/3` is selected by shared-circle or
complex-nesting structure, it must cite this theorem and fill:

{missing}

## Guardrails

{guardrails}

## Next Required Object

```text
{decision["next_required_object"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
