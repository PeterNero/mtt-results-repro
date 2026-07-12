"""Audit selected-source promotion attempts for the C1 rebuild frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
SM = TEXPAPERS / "mtt-sm-parity-closure"
GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"

OUTPUT_CERT = CERTS / "selected_c1_source_promotion_iteration_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_C1_Source_Promotion_Iteration_v1.md"

INPUTS = {
    "local_rebuild_attempt": CERTS / "selected_c1_operator_source_rebuild_attempt_certificate.json",
    "q79_promotion_gate": Q79 / "certificates" / "iwasawa_selected_source_promotion_gate_certificate.json",
    "q79_valpha_sufficiency": Q79
    / "certificates"
    / "selected_valpha_operator_source_sufficiency_certificate.json",
    "q79_m1_deresponse_target": Q79 / "candidate_data" / "time_oriented_m1_deresponse_target.candidate.json",
    "sm_source_origin_lemma": SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json",
    "gr_paper_lemma": GR / "certificates" / "routec_selected_source_origin_paper_lemma_certificate.json",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def present_inputs() -> dict[str, dict[str, Any]]:
    return {
        name: {
            "path": str(path),
            "present": path.exists(),
        }
        for name, path in INPUTS.items()
    }


def classify_inputs() -> dict[str, dict[str, Any]]:
    local = load_json(INPUTS["local_rebuild_attempt"])
    gate = load_json(INPUTS["q79_promotion_gate"])
    valpha = load_json(INPUTS["q79_valpha_sufficiency"])
    deresponse = load_json(INPUTS["q79_m1_deresponse_target"])
    source_lemma = load_json(INPUTS["sm_source_origin_lemma"])
    paper = load_json(INPUTS["gr_paper_lemma"])

    return {
        "local_rebuild_attempt": {
            "classification": "negative_rebuild_attempt",
            "usable_as_selected_source": False,
            "status": local["status"],
            "reason": "It classifies all slots but emits neither A_selected nor b_selected.",
            "key_open_items": [
                "emit_selected_A_selected",
                "emit_selected_b_selected",
                "selected_source_certificate",
                "selected_D_E_Riesz_Green_dotD",
            ],
        },
        "q79_promotion_gate": {
            "classification": "validator_gate_not_source",
            "usable_as_selected_source": False,
            "status": gate["status"],
            "reason": (
                "It defines the checks that selected packets must pass and explicitly leaves "
                "actual selected rho_E, D_E, and dotD data open."
            ),
            "still_open": gate["still_open"],
        },
        "q79_valpha_sufficiency": {
            "classification": "conditional_sufficiency_theorem",
            "usable_as_selected_source": False,
            "status": valpha["status"],
            "reason": valpha["verdict"]["honest_answer"],
            "actual_packet_validation": valpha["actual_packet_validation"],
            "does_not_close": valpha["what_this_does_not_close"],
        },
        "q79_m1_deresponse_target": {
            "classification": "conditional_lifted_consistency_check",
            "usable_as_selected_source": False,
            "status": deresponse["status"],
            "reason": deresponse["verdict"]["honest_answer"],
            "current_honest_packets_fail": deresponse["calculation_results"]["honest_current_hym_source_fails"]
            and deresponse["calculation_results"]["honest_current_promotion_fails"],
            "still_open": deresponse["still_open"],
        },
        "sm_source_origin_lemma": {
            "classification": "reduction_to_phi_fin",
            "usable_as_selected_source": False,
            "status": source_lemma["status"],
            "reason": source_lemma["theorem"]["statement"],
            "open_sublemma": source_lemma["lemma_evaluation"]["open_sublemma"],
            "next_required_artifact": source_lemma["next_required_artifact"],
        },
        "gr_paper_lemma": {
            "classification": "conditional_paper_lemma",
            "usable_as_selected_source": False,
            "status": paper["status"],
            "reason": paper["proof_boundary"]["why_not_unconditional"],
            "open_payload_premises": paper["open_payload_premises"],
        },
    }


def build_certificate() -> dict[str, Any]:
    classified = classify_inputs()
    usable = [name for name, row in classified.items() if row["usable_as_selected_source"]]
    cycle = {
        "source_promotion_needs": [
            "theorem-derived selected_source_verified",
            "selected D_E/Riesz/Green/dotD payload",
            "nonzero same-branch dotD/source response",
        ],
        "c1_payload_rebuild_needs": [
            "selected source certificate",
            "selected D_E/Riesz/Green/dotD payload",
            "selected primitive C1 contractions",
            "selected sector response matrices",
            "selected Hessian blocks",
        ],
        "cycle_detected": True,
        "why": (
            "Current artifacts can validate a packet after selected-source flags are supplied, "
            "but the C1 rebuild needs exactly those selected-source and operator payloads before "
            "it can emit A_selected and b_selected."
        ),
    }
    breakpoints = [
        {
            "name": "FiniteEmissionMorphism_Phi_fin_with_selected_payload",
            "rank": 1,
            "why_non_circular": (
                "It starts from the selected Strominger/HYM minimizer in the fixed q79/F,m=1 "
                "S3/GS sector and emits finite rho_E, D_E, Riesz/Green, dotD, and C1 data as "
                "images of that source, rather than importing selected flags from validators."
            ),
            "must_emit": [
                "selected non-identity rho_E or equivalent connection",
                "finite selected D_E blocks",
                "Riesz gaps and reduced Green operators with error/gap control",
                "same-branch dotD_alpha1 matrices and source vector b_selected",
                "primitive C1 overlap tensors",
                "sector response matrices giving A_selected",
            ],
        },
        {
            "name": "Typed Cech/monad transition source theorem",
            "rank": 2,
            "why_non_circular": (
                "It would derive the same operator payload directly from selected V_alpha/L3-K2 "
                "transition data, Pic0 quotient or selection, and same-source S3/GS support."
            ),
            "must_emit": [
                "selected transition functions or section-ring multiplication constants",
                "Pic0 quotient/selection proof",
                "same-source Chern-Weil row",
                "operator exit into the Route-C validator basis",
            ],
        },
    ]
    return {
        "certificate": "SelectedC1SourcePromotionIteration",
        "status": "SELECTED_C1_SOURCE_PROMOTION_ITERATED_PHI_FIN_BREAKPOINT_IDENTIFIED",
        "input_status": present_inputs(),
        "classified_inputs": classified,
        "usable_selected_source_imports": usable,
        "all_imported_selected_source_candidates_rejected_as_proof_sources": len(usable) == 0,
        "cycle_analysis": cycle,
        "solution_direction": {
            "shortest_non_circular_breakpoint": breakpoints[0]["name"],
            "alternative_breakpoint": breakpoints[1]["name"],
            "breakpoints": breakpoints,
            "next_artifact_to_construct": "Selected_PhiFin_C1_Emission_Packet_v1",
        },
        "acceptance_tests_for_solution": [
            "does not set selected_source_verified by hand",
            "does not use hypothetical_selected packets",
            "does not use observed masses, mixings, gauge constants, or benchmark residuals",
            "emits A_selected and b_selected from one branch source",
            "passes D_E, Riesz/gap, reduced Green, dotD, and C1 response audits honestly",
        ],
        "what_closes_now": {
            "false_selected_source_imports_eliminated": True,
            "circularity_exposed": True,
            "non_circular_breakpoint_identified": True,
            "next_payload_contract_sharpened": True,
        },
        "what_remains_open": {
            "Selected_PhiFin_C1_Emission_Packet_v1": True,
            "actual_A_selected": True,
            "actual_b_selected": True,
            "full_selected_C1_operator_source": True,
        },
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }


def render_note(cert: dict[str, Any]) -> str:
    rows = cert["classified_inputs"]
    table = "\n".join(
        f"| `{name}` | `{row['classification']}` | `{row['status']}` | no |"
        for name, row in rows.items()
    )
    cycle_needs = "\n".join(f"- {item}" for item in cert["cycle_analysis"]["source_promotion_needs"])
    rebuild_needs = "\n".join(f"- {item}" for item in cert["cycle_analysis"]["c1_payload_rebuild_needs"])
    bp = cert["solution_direction"]["breakpoints"][0]
    must_emit = "\n".join(f"- {item}" for item in bp["must_emit"])
    tests = "\n".join(f"- {item}" for item in cert["acceptance_tests_for_solution"])
    return f"""# Selected C1 Source Promotion Iteration v1

## Result

The iteration did not find a legal selected-source import.  It did find the
precise circularity blocking the C1 rebuild:

```text
source promotion wants selected D_E/dotD/Riesz/Green payload
C1 rebuild wants selected source plus selected D_E/dotD/Riesz/Green payload
```

Therefore the next step cannot be another flag lift.  The non-circular break
point is `FiniteEmissionMorphism_Phi_fin_with_selected_payload`, implemented as
`Selected_PhiFin_C1_Emission_Packet_v1`.

## Imported Candidates

| input | classification | status | usable as proof source |
| --- | --- | --- | --- |
{table}

## Cycle

Source promotion currently needs:

{cycle_needs}

The C1 payload rebuild currently needs:

{rebuild_needs}

This is why the conditional and hypothetical packets validate cleanly while the
honest packets fail: the validators are not the missing theorem.

## Solution Breakpoint

`{bp["name"]}`

{bp["why_non_circular"]}

It must emit:

{must_emit}

## Acceptance Tests

{tests}
"""


def main() -> int:
    cert = build_certificate()
    if "--write" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
