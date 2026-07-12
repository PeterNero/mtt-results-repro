"""Build BN27 full-operator/source-flags/quotient-functor value construction gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "refined_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_refined_root_cutset.json",
    "scoped_trace_refinement": DATA / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem.candidate.json",
    "ew_quotient_functor": DATA / "selected_electroweak_qastack_quotient_functor_and_abase_identity.candidate.json",
    "ew_determinant_gate": DATA / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json",
    "ew_finitepart_policy": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "heterotic_orientedbn_functor": DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json",
    "direct_acceptance_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction.candidate.json"
OUTPUT_TRANSFER = DATA / "selected_heterotic_orientedphifin_bn27_quotient_finitepart_transfer_boundary.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_FullOperatorFormula_SourceFlags_or_QuotientFunctor_ValueConstruction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_QUOTIENT_FINITEPART_SUPPORT_IMPORTED_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_DirectFinitePartFunctional_or_SourceOwnedLogdetTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    cutset = load(INPUTS["refined_cutset"])
    scoped = load(INPUTS["scoped_trace_refinement"])
    ew_quotient = load(INPUTS["ew_quotient_functor"])
    ew_det = load(INPUTS["ew_determinant_gate"])
    ew_finite = load(INPUTS["ew_finitepart_policy"])
    heterotic_functor = load(INPUTS["heterotic_orientedbn_functor"])
    contract = load(INPUTS["direct_acceptance_contract"])

    transfer = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.QuotientFinitePartTransferBoundary.v1",
        "status": "SUPPORT_TRANSFER_BOUNDARY_BUILT_SOURCE_IDENTITY_OPEN",
        "importable_as_support": {
            "selected_27mode_DE_gap_trace_equality": scoped["decision"]["selected_trace_equality_for_27mode_DE_gap_layer_closed"],
            "Pperp_domain_policy_closed": ew_quotient["decision"]["Pperp_domain_policy_closed"],
            "tensor_identity_quotient_functor_closed_conditionally": ew_quotient["decision"]["tensor_identity_quotient_functor_closed"],
            "quotient_determinant_lemma_closed_conditionally": ew_quotient["decision"]["quotient_determinant_lemma_closed"],
            "electroweak_internal_finitepart_policy_closed": ew_finite["decision"]["selected_p_a_internal_promoted"],
            "electroweak_internal_p_a_value": ew_finite["decision"]["selected_p_a_internal_value"],
        },
        "not_importable_as_BN27_source_identity": {
            "selected_BN_to_threshold_functor_closed": ew_quotient["decision"]["selected_BN_to_threshold_functor_closed"],
            "A_base_tensor_I3_identity_closed": ew_quotient["decision"]["A_base_tensor_I3_identity_closed"],
            "selected_A_base_tensor_I3_emission": not ew_det["what_remains_open"]["selected_A_base_tensor_I3_emission"],
            "heterotic_oriented_BN_carrier_functor_closed": heterotic_functor["decision"]["EndE_or_rhoE_to_oriented_BN_functor_closed"],
            "source_object_named_S_QaSU3_BN27": contract["direct_source_identity_payload"]["source_object_named_S_QaSU3_BN27"] is not None,
        },
        "scope_warning": "Electroweak internal p_a lives on the Qa-stack V/<s> quotient row. It is not the heterotic oriented BN27 logdet source theorem.",
        "target_fitting_used": False,
    }
    OUTPUT_TRANSFER.write_text(json.dumps(transfer, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lanes = {
        "lane_A_full_operator_formula": {
            "closed_now": False,
            "support_imported": {
                "DE_gap_trace": True,
                "tensor_identity_quotient_conditional": True,
                "internal_finitepart_policy_electroweak": True,
            },
            "first_missing": "same-source theorem identifying selected B_N/PhiFin operator with the full threshold operator",
            "why_not_closed": "The quotient theorem is conditional on an emitted A_base tensor I_3 or direct determinant functional; heterotic BN27 still has only gap-layer trace ownership.",
        },
        "lane_B_theorem_derived_full_source_flags": {
            "closed_now": False,
            "first_missing": "full selected operator formula or direct source-owned finitepart functional",
            "required_no_lift_replay": contract["typed_or_connection_payload"]["no_lifted_flags_replay_audit"],
            "why_not_closed": "The D_E source flags are theorem-derived only for the gap/Riesz/Green layer, not the full oriented BN27 packet.",
        },
        "lane_C_quotient_functor_value_construction": {
            "closed_now": False,
            "support_imported": {
                "Pperp_domain_policy": True,
                "tensor_identity_quotient": True,
            },
            "first_missing": "selected_BN_to_threshold_functor or heterotic EndE/rhoE-to-oriented-BN functor",
            "why_not_closed": heterotic_functor["theorem"]["statement"],
        },
        "lane_D_direct_finitepart_functional_on_BN27": {
            "closed_now": False,
            "ranked_next": True,
            "reason": "It avoids proving equality to A_base tensor I_3 and attacks the source-owned finitepart directly on the selected BN27/PhiFin quotient.",
            "must_emit": [
                "source-owned positive spectrum/finitepart rule on oriented BN27",
                "kernel/shared-circle policy as source-owned, not replay-only",
                "index weights and determinant scale for the BN27 oriented row",
                "proof that log(92160000) is consumed by the selected source, not only support",
            ],
        },
    }

    decision = {
        "attempt_executed": True,
        "quotient_finitepart_support_imported": True,
        "electroweak_internal_finitepart_policy_closed": ew_finite["decision"]["selected_p_a_internal_promoted"],
        "electroweak_internal_p_a_value_carried_as_support": ew_finite["decision"]["selected_p_a_internal_value"],
        "full_selected_operator_formula_closed_for_BN27": False,
        "theorem_derived_selected_source_flags_for_full_BN27": False,
        "quotient_or_source_identity_functor_closed_for_BN27": False,
        "direct_finitepart_functional_on_BN27_closed": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "transfer_boundary_path": rel(OUTPUT_TRANSFER),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27FullOperatorFormulaSourceFlagsOrQuotientFunctorValueConstruction",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "scoped_trace_refinement": scoped["status"],
            "ew_quotient_functor": ew_quotient["status"],
            "ew_determinant_gate": ew_det["status"],
            "ew_finitepart_policy": ew_finite["status"],
            "heterotic_orientedbn_functor": heterotic_functor["status"],
        },
        "refined_cutset_status": cutset["status"],
        "transfer_boundary_path": rel(OUTPUT_TRANSFER),
        "lane_evaluation": lanes,
        "decision": decision,
        "theorem": {
            "name": "BN27QuotientFinitePartSupportTransferBoundaryTheorem",
            "proved": True,
            "statement": (
                "The electroweak Qa-stack quotient and internal finitepart results can be imported as support for the BN27 "
                "frontier: Pperp quotient algebra, tensor-identity quotient determinant, and internal V/<s> finitepart policy "
                "are closed in their scope. They do not close heterotic BN27 source identity or promote log(92160000), because "
                "the selected B_N-to-threshold functor, full operator formula, theorem-derived full-packet source flags, and "
                "S_QaSU3^BN27 source declaration remain open. The best next attack is a direct source-owned finitepart "
                "functional/logdet theorem on oriented BN27."
            ),
        },
        "guardrails": {
            "does_not_import_electroweak_p_a_as_BN27_logdet": True,
            "does_not_treat_conditional_quotient_as_source_identity": True,
            "does_not_treat_gap_trace_as_full_operator_formula": True,
            "does_not_promote_log92160000": True,
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
        "transfer_boundary_path": rel(OUTPUT_TRANSFER),
        "note_path": rel(OUTPUT_NOTE),
        "quotient_finitepart_support_imported": True,
        "full_selected_operator_formula_closed_for_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 FullOperatorFormula SourceFlags or QuotientFunctor ValueConstruction v1

## Result

```text
status = {STATUS}
quotient_finitepart_support_imported = true
full_selected_operator_formula_closed_for_BN27 = false
theorem_derived_selected_source_flags_for_full_BN27 = false
quotient_or_source_identity_functor_closed_for_BN27 = false
direct_finitepart_functional_on_BN27_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Transfer Boundary

```text
{rel(OUTPUT_TRANSFER)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TRANSFER)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
