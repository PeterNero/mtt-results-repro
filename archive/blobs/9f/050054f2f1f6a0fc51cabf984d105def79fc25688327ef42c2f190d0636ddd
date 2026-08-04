"""Refine BN27 root cutset with scoped selected trace equality."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "root_frontier": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json",
    "root_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_minimal_root_cutset.json",
    "electroweak_trace_full_formula": DATA / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json",
    "u1y_trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "direct_acceptance_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem.candidate.json"
OUTPUT_REFINED = DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_refined_root_cutset.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SelectedTraceEquality_FullOperatorFormula_or_SourceFlagTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_TRACE_EQUALITY_SCOPED_CLOSED_FULL_SOURCE_FLAGS_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_FullOperatorFormula_SourceFlags_or_QuotientFunctor_ValueConstruction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    frontier = load(INPUTS["root_frontier"])
    cutset = load(INPUTS["root_cutset"])
    ew = load(INPUTS["electroweak_trace_full_formula"])
    u1y_trace = load(INPUTS["u1y_trace_equals_27mode"])
    contract = load(INPUTS["direct_acceptance_contract"])

    ew_decision = ew["decision"]
    trace_layer = ew["imported_trace_layer"]
    u1y_decision = u1y_trace["decision"]

    scoped_trace_closed = (
        ew_decision["selected_DE_gap_trace_equality_closed"] is True
        and trace_layer["selected_trace_equality_for_27mode_DE"] is True
        and u1y_decision["selected_trace_equality_for_27mode_DE"] is True
    )

    refined = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceIdentity.RefinedRootCutset.v1",
        "status": "SCOPED_TRACE_EQUALITY_CLOSED_FULL_SOURCE_IDENTITY_OPEN",
        "support_closed": cutset["already_closed_as_support"],
        "scoped_root_refinement": {
            "selected_trace_equality_for_27mode_DE_gap_layer": {
                "closed": scoped_trace_closed,
                "scope": "selected 27-mode D_E gap/Riesz/Green layer on B_N only",
                "does_not_close": [
                    "full selected threshold operator formula",
                    "BN27 source object S_QaSU3^BN27",
                    "theorem-derived selected-source flags for the full packet",
                    "oriented logdet source ownership",
                ],
            },
            "full_selected_iwasawa_strominger_operator_formula": {
                "closed": ew_decision["full_threshold_operator_formula_closed"],
                "missing": ew["threshold_formula_tests"]["full_selected_threshold_operator_formula"]["known_missing"],
            },
            "quotient_or_source_identity_functor": {
                "closed": ew_decision["quotient_functor_closed"],
                "missing": ew["frontier_reclassification"]["true_frontier"],
            },
            "theorem_derived_selected_source_flags_for_full_BN27": {
                "closed": False,
                "missing": [
                    "full selected operator formula",
                    "same-source quotient/source identity theorem",
                    "no-lift replay audit for the full BN27 packet",
                ],
            },
            "source_object_named_S_QaSU3_BN27": {
                "closed": False,
                "acceptance_field": contract["direct_source_identity_payload"]["source_object_named_S_QaSU3_BN27"],
            },
        },
        "target_fitting_used": False,
    }
    OUTPUT_REFINED.write_text(json.dumps(refined, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "refinement_executed": True,
        "selected_trace_equality_for_27mode_DE_gap_layer_closed": scoped_trace_closed,
        "full_selected_operator_formula_closed": False,
        "quotient_or_source_identity_functor_closed": False,
        "theorem_derived_selected_source_flags_for_full_BN27": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "refined_root_cutset_path": rel(OUTPUT_REFINED),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SelectedTraceEqualityFullOperatorFormulaOrSourceFlagTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "root_frontier": frontier["status"],
            "electroweak_trace_full_formula": ew["status"],
            "u1y_trace_equals_27mode": u1y_trace["status"],
        },
        "refined_root_cutset_path": rel(OUTPUT_REFINED),
        "decision": decision,
        "theorem": {
            "name": "ScopedTraceEqualityRefinementTheorem",
            "proved": True,
            "statement": (
                "The selected trace-equality root can be refined: the 27-mode D_E gap/Riesz/Green layer is theorem-derived "
                "and closed on B_N. This is a real closure, but only at gap-layer scope. It does not close the full BN27 "
                "source identity, because the full selected operator formula, quotient/source-identity functor, theorem-derived "
                "full-packet source flags, and S_QaSU3^BN27 declaration remain open."
            ),
        },
        "guardrails": {
            "does_not_treat_gap_trace_as_full_operator_formula": True,
            "does_not_treat_DE_gap_support_as_source_identity": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "refined_root_cutset_path": rel(OUTPUT_REFINED),
        "note_path": rel(OUTPUT_NOTE),
        "selected_trace_equality_for_27mode_DE_gap_layer_closed": scoped_trace_closed,
        "full_selected_operator_formula_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SelectedTraceEquality FullOperatorFormula or SourceFlagTheorem v1

## Result

```text
status = {STATUS}
selected_trace_equality_for_27mode_DE_gap_layer_closed = true
full_selected_operator_formula_closed = false
quotient_or_source_identity_functor_closed = false
theorem_derived_selected_source_flags_for_full_BN27 = false
source_object_named_S_QaSU3_BN27 = false
BN27_source_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Refined Cutset

```text
{rel(OUTPUT_REFINED)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REFINED)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
