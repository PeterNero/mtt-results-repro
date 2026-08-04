"""Evaluate the standard-embedding selector versus Phi_fin emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_GATE = DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json"
INPUT_MONAD = DATA / "ext_stability_source_search.candidate.json"
OUTPUT_DATA = DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_standard_embedding_selector_or_phifin_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_StandardEmbeddingSelector_or_PhiFin_Gate_v1.md"

STATUS = "HETEROTIC_STANDARD_EMBEDDING_SELECTOR_RETIRED_PHIFIN_DIRECT_OPERATOR_PRIMARY"
NEXT = "Selected_Heterotic_PhiFin_DirectOperatorEmission_or_BundleConnection_SourceSolve_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    gate = load(INPUT_GATE)
    monad = load(INPUT_MONAD)
    monad_topology = monad.get("monad_chern_data", monad["monad_computation"])

    standard_embedding_eval = {
        "route": "A_conditional_standard_embedding",
        "conditional_packet_valid": True,
        "selected_now": False,
        "retired_as_current_proof_source": True,
        "reason": [
            "the selected Qa/SU3 source branch carries the rank-three Iwasawa SU(3) monad/endomorphism problem",
            "that source recomputes c1(E)=0, c2(E)=0, integral c3(E)=6",
            "the computed R+ curvature is nonzero and belongs to the tangent/Bismut geometry block",
            "setting A=GammaPlus would replace the selected monad/bundle source with a tangent-bundle standard embedding not emitted by MTT",
            "there is no same-branch theorem identifying End(E) threshold one-forms with the tangent-bundle spin-connection representation",
        ],
        "what_would_be_needed_to_reopen": [
            "a source theorem selecting the tangent/standard-embedding bundle rather than the monad/End(E) branch",
            "a representation map from R+ into the exact Qa/SU3 gauge algebra used by the threshold operator",
            "a quotient/kernel and finite-part theorem for the resulting operator domain",
        ],
    }

    phifin_eval = {
        "route": "B_direct_finite_operator",
        "primary_now": True,
        "selected_now": False,
        "why_primary": [
            "it preserves the selected monad/End(E)/Strominger-HYM source type",
            "it asks for actual rho_E, D_E, Riesz/gap, Green, E_Qa or finite zero-order data instead of substituting the tangent connection",
            "it is aligned with the sibling Route-C reduction to the finite emission morphism Phi_fin",
        ],
        "minimal_payload": gate["routes"]["B_direct_finite_operator"]["required_payload"],
    }

    candidate = {
        "candidate": "SelectedHeteroticStandardEmbeddingSelectorOrPhiFinGate",
        "status": STATUS,
        "inputs": {
            "bundle_curvature_trace_gate": rel(INPUT_GATE),
            "monad_topology": rel(INPUT_MONAD),
        },
        "input_statuses": {
            "bundle_curvature_trace_gate": gate["status"],
            "monad_topology": monad["status"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "monad_topology": {
            "rank": monad_topology.get("rank", 3),
            "c1_zero": monad_topology["c1_zero"],
            "c2_zero": monad_topology["c2_zero"],
            "c3_integral": monad_topology["c3_integral"],
            "c3_integral_equals_6": monad_topology["c3_integral_equals_6"],
        },
        "standard_embedding_evaluation": standard_embedding_eval,
        "phifin_direct_operator_evaluation": phifin_eval,
        "decision": {
            "standard_embedding_retired_as_current_proof_source": True,
            "phifin_or_direct_operator_primary": True,
            "bundle_tensor_payload_filled": False,
            "direct_finite_operator_emitted": False,
            "E_Qa_computed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "guardrails": {
            "declares_standard_embedding_false_in_general": False,
            "promotes_standard_embedding_without_selector": False,
            "promotes_phi_fin_without_values": False,
            "promotes_monad_topology_as_operator": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "CurrentSourceStandardEmbeddingRetirementTheorem",
            "proved": True,
            "statement": (
                "The standard-embedding packet is a valid conditional mathematical route, "
                "but it is not the current selected Qa/SU3 proof source. The current source "
                "selects the rank-three Iwasawa SU(3) monad/End(E) threshold branch with "
                "c1=0, c2=0, c3=6, while A=GammaPlus would substitute the tangent/Bismut "
                "connection. Therefore the primary remaining route is a same-source "
                "Phi_fin/direct finite operator emission or an explicit selected bundle "
                "connection source solve."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "standard_embedding_retired_as_current_proof_source": True,
        "phifin_or_direct_operator_primary": True,
        "bundle_tensor_payload_filled": False,
        "direct_finite_operator_emitted": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic StandardEmbeddingSelector or PhiFin Gate v1

## Result

```text
status = {STATUS}
standard_embedding_retired_as_current_proof_source = true
phifin_or_direct_operator_primary = true
bundle_tensor_payload_filled = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Reason

The standard embedding route remains a valid conditional mathematical route.
But the current selected Qa/SU3 source is the rank-three Iwasawa `SU(3)` monad:

```json
{json.dumps(candidate["monad_topology"], indent=2, sort_keys=True)}
```

The computed `R+` curvature belongs to the tangent/Bismut geometry block.
Promoting `A=GammaPlus` would replace the selected monad/`End(E)` threshold
source with a tangent-bundle standard embedding. The corpus has not selected
that replacement.

## The Remaining Primary Route

The primary route is now:

```text
Phi_fin / direct finite operator emission
```

with the minimal payload:

```json
{json.dumps(phifin_eval["minimal_payload"], indent=2)}
```

This does not close the physical threshold. It removes one tempting shortcut and
leaves a sharper source-solve problem: emit the selected bundle connection or
emit the finite operator directly from the same Strominger/HYM branch.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
