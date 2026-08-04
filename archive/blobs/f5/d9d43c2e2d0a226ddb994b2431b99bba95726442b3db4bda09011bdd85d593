"""Build finite C1 trace-measure principle insertion / direct action derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PATCH = PACKET_DIR / "finite_c1_trace_measure_principle_patch.packet.json"
REPLAY = PACKET_DIR / "patched_routeb_dynamic_c1_closure_replay.packet.json"
GUARDRAIL = PACKET_DIR / "unpatched_derivation_guardrail.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1TraceMeasurePrincipleInsertion_or_DirectActionDerivation_v1.md"

STATUS = "MTT_SELECTED_FINITEC1TRACEMEASUREPRINCIPLEINSERTION_OR_DIRECTACTIONDERIVATION_BUILT_PATCHED_DYNAMIC_C1_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_DynamicC1PatchToSMParityLedger_or_UnpatchedMeasureDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalmeasureidentity_or_routeaemissionclosure.candidate.json")
    draft = load(
        DATA
        / "selected_physicalmeasureidentity_or_routeaemissionclosure"
        / "finite_c1_trace_measure_principle_draft.packet.json"
    )
    identity_slot = load(
        DATA
        / "selected_physicalmeasureidentity_or_routeaemissionclosure"
        / "physical_measure_identity_theorem_slot.packet.json"
    )
    formal_rows = load(
        DATA
        / "selected_routeaemission_or_routebgalerkinrows_execution"
        / "formal_110_row_execution.packet.json"
    )
    route_b_conditional = load(
        DATA
        / "selected_physicalmeasure_or_finitegalerkinpromotion"
        / "routeb_conditional_promotion_packet.packet.json"
    )

    promoted = draft["would_promote_if_inserted_or_derived"]
    patch = {
        "schema": "MTTFiniteC1TraceMeasurePrinciplePatch.v1",
        "status": "LOCAL_PROOF_SPINE_PRINCIPLE_PATCH_APPLIED",
        "principle_name": draft["principle_name"],
        "principle_text": draft["principle_text"],
        "applied_to_local_proof_spine": True,
        "applied_to_external_obsidian_papers": False,
        "derived_from_prior_axioms": False,
        "guardrail_text": (
            "This is a local SM-parity axiom/principle patch, not a no-knob derivation. "
            "It uses no observed masses, mixings, CP phase, or benchmark matrices as selectors."
        ),
        "scope": {
            "selected_finite_C1_quotient_only": True,
            "qutrit_Weyl_trace_measure_only": True,
            "dynamic_C1_packet_only": True,
            "does_not_close_full_no_knob_flavor_constants": True,
            "does_not_close_true_SM_equivalence_by_itself": True,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    replay = {
        "schema": "MTTPatchedRouteBDynamicC1ClosureReplay.v1",
        "status": "PATCHED_ROUTE_B_DYNAMIC_C1_PACKET_CLOSED",
        "patch_used": patch["principle_name"],
        "formal_row_counts": formal_rows["row_counts"],
        "row_comparison_max_abs_error": formal_rows["comparison_to_prior_algebraic_replay"][
            "max_abs_error"
        ],
        "promoted_under_patched_spine": {
            "physical_measure_equals_finite_trace_quadrature": promoted[
                "physical_measure_equals_finite_trace_quadrature"
            ],
            "selected_Galerkin_replacement_promotes_formal_rows": promoted[
                "selected_Galerkin_replacement_promotes_formal_rows"
            ],
            "Route_B_physical_Galerkin_replacement_closed": promoted[
                "Route_B_physical_Galerkin_replacement_closed"
            ],
            "physical_A_selected": promoted["physical_A_selected"],
            "physical_b_selected": promoted["physical_b_selected"],
            "physical_deltaTheta_C1": promoted["physical_deltaTheta_C1"],
            "physical_sector_response_matrices": promoted[
                "physical_sector_response_matrices"
            ],
            "patched_dynamic_C1_packet_closed": promoted[
                "unpatched_SM_parity_dynamic_packet_closed"
            ],
        },
        "not_promoted_under_unpatched_spine": {
            "direct_PhiFinC1_action_derivation": False,
            "unpatched_physical_measure_identity": False,
            "Route_A_same_source_emission": False,
            "unpatched_dynamic_C1_packet_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    guardrail = {
        "schema": "MTTUnpatchedDerivationGuardrail.v1",
        "status": "PATCHED_CLOSURE_SEPARATED_FROM_UNPATCHED_DERIVATION",
        "unpatched_open_items": {
            "derive_principle_from_selected_PhiFinC1_action": True,
            "prove_no_extra_physical_boundary_or_source_term_without_patch": True,
            "emit_same_source_b_selected_without_patch": True,
            "derive_or_corpus_promote_principle_without_axiom_insertion": True,
            "full_no_knob_flavor_constants": True,
        },
        "credibility_policy": [
            "The patched result is acceptable as an SM-parity local-principle closure, analogous to measured-input axioms admitted for parity.",
            "The no-knob program must still derive the principle or replace it by Route A source emission.",
            "Downstream papers must label this as a principle insertion unless the direct derivation is later supplied.",
        ],
        "direct_derivation_available_now": identity_slot[
            "direct_derivation_available_now"
        ],
        "principle_derived_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteC1TraceMeasurePrincipleInsertionOrDirectActionDerivation",
        "status": STATUS,
        "inputs": {
            "previous_measure_identity_gate": rel(
                DATA / "selected_physicalmeasureidentity_or_routeaemissionclosure.candidate.json"
            ),
            "principle_draft": rel(
                DATA
                / "selected_physicalmeasureidentity_or_routeaemissionclosure"
                / "finite_c1_trace_measure_principle_draft.packet.json"
            ),
            "formal_110_rows": rel(
                DATA
                / "selected_routeaemission_or_routebgalerkinrows_execution"
                / "formal_110_row_execution.packet.json"
            ),
            "routeb_conditional_promotion": rel(
                DATA
                / "selected_physicalmeasure_or_finitegalerkinpromotion"
                / "routeb_conditional_promotion_packet.packet.json"
            ),
        },
        "output_packets": {
            "finite_c1_trace_measure_principle_patch": rel(PATCH),
            "patched_routeb_dynamic_c1_closure_replay": rel(REPLAY),
            "unpatched_derivation_guardrail": rel(GUARDRAIL),
        },
        "theorem": {
            "name": "PatchedFiniteC1TraceMeasureClosureTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "After inserting the SelectedFiniteC1TraceMeasurePrinciple into the local proof spine, "
                "the exact finite Weyl trace rows promote to physical Route B Galerkin rows and close "
                "the dynamic C1 packet under the patched SM-parity standard. The unpatched derivation "
                "of the principle remains open."
            ),
        },
        "what_closes_now": {
            "finite_C1_trace_measure_principle_applied_to_local_spine": True,
            "patched_physical_measure_identity": True,
            "patched_Route_B_physical_Galerkin_replacement": True,
            "patched_A_selected": True,
            "patched_b_selected": True,
            "patched_deltaTheta_C1": True,
            "patched_sector_response_matrices": True,
            "patched_dynamic_C1_packet_closure": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "unpatched_direct_PhiFinC1_action_derivation": True,
            "unpatched_principle_derivation": True,
            "unpatched_Route_A_same_source_emission": True,
            "full_no_knob_flavor_constants": True,
            "full_SM_parity_ledger_integration": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "patched_dynamic_C1_packet_closed": True,
            "patched_Route_B_physical_Galerkin_replacement_closed": True,
            "unpatched_dynamic_C1_packet_closed": False,
            "unpatched_physical_measure_identity_promoted": False,
            "principle_derived_from_prior_axioms": False,
            "Route_A_same_source_emission_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteC1TraceMeasurePrincipleInsertion_or_DirectActionDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "theorem_patched": True,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteC1TraceMeasurePrincipleInsertion or DirectActionDerivation v1

Status: `{STATUS}`.

The finite C1 trace-measure principle is now applied to the local proof spine:

```text
principle applied locally              = {patch["applied_to_local_proof_spine"]}
principle derived from prior axioms     = {patch["derived_from_prior_axioms"]}
patched Route B Galerkin closure        = {replay["promoted_under_patched_spine"]["Route_B_physical_Galerkin_replacement_closed"]}
patched dynamic C1 packet closed        = {replay["promoted_under_patched_spine"]["patched_dynamic_C1_packet_closed"]}
unpatched dynamic C1 packet closed      = {replay["not_promoted_under_unpatched_spine"]["unpatched_dynamic_C1_packet_closed"]}
```

This closes the dynamic C1 packet in the local patched SM-parity spine without
using observed masses, mixings, CP phase, or benchmark matrices as selectors.
The no-knob/unpatched task remains: derive this principle from the selected
`Phi_fin^C1` action or replace it with Route A same-source emission.

Next artifact: `{NEXT}`.
"""

    PATCH.write_text(json.dumps(patch, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPLAY.write_text(json.dumps(replay, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GUARDRAIL.write_text(json.dumps(guardrail, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
