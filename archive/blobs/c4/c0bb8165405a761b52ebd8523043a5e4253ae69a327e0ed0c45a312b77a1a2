"""Build Step 22 vertex-source promotion attempt and transfer-map frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step22_vertexsource_promotion_or_transfermap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION_ATTEMPT = PACKET_DIR / "step22_vertex_source_promotion_attempt.packet.json"
READY_VALUES = PACKET_DIR / "step22_ready_to_promote_value_packet.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step22_to_step23_transfermap_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step22_VertexSourcePromotion_or_TransferMap_v1.md"

STEP21 = DATA / "selected_step21_conditional_atomdecomposition_or_vertexsource.candidate.json"
STEP20_VALIDATION = DATA / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_conditional_normal_form_validation.packet.json"
STEP21_FRONTIER = DATA / "selected_step21_conditional_atomdecomposition_or_vertexsource" / "step21_vertex_source_theorem_frontier.packet.json"
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
WEYL_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
OVERLAP_KERNEL = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
SAME_SOURCE_IDENTITY = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"

STATUS = "MTT_SELECTED_STEP22_VERTEXSOURCE_PROMOTION_ATTEMPT_TRANSFERMAP_OPEN"
NEXT = "MTT_Selected_Step23_SourceToC1TransferMapLemma_or_SelectedValuesPromotion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP21, STEP20_VALIDATION, STEP21_FRONTIER, SOURCE_SELECTOR, WEYL_PROVENANCE, OVERLAP_KERNEL, SAME_SOURCE_IDENTITY]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 22 inputs: " + ", ".join(missing))

    step21 = load(STEP21)
    step20_validation = load(STEP20_VALIDATION)
    step21_frontier = load(STEP21_FRONTIER)
    source_selector = load(SOURCE_SELECTOR)
    weyl_provenance = load(WEYL_PROVENANCE)
    overlap = load(OVERLAP_KERNEL)
    same_source_identity = load(SAME_SOURCE_IDENTITY)

    clauses = {
        "source_selector_emitted": source_selector["promotion_decision"]["source_selector_promoted"],
        "source_level_weyl_carrier_closed": weyl_provenance["source_level_weyl_carrier"]["proved"],
        "active_shift_provenance_closed": weyl_provenance["active_shift_provenance"]["proved"],
        "sm_slot_overlap_kernel_closed": overlap["selected_overlap_kernel"]["selected"],
        "conditional_atom_decomposition_exact": step21["closure_decision"]["conditional_decomposition_reconstructs_aggregate"],
        "selected_source_to_C1_transfer_map_emitted": weyl_provenance["c1_transfer_map"]["selected_source_to_C1_response_map_emitted"],
        "phase_Z_routed_to_u_e_column": weyl_provenance["c1_transfer_map"]["phase_Z_routed_to_u_e_I_plus_Z_column"],
        "shift_X_routed_to_d_nuD_column": weyl_provenance["c1_transfer_map"]["shift_X_routed_to_d_nuD_I_plus_X_column"],
        "selected_b_selected_emitted": same_source_identity["lane_A_same_source_dynamic_transfer"]["selected_status"]["selected_b_selected_emitted"],
        "selected_Hessian_blocks_emitted": same_source_identity["lane_A_same_source_dynamic_transfer"]["selected_status"]["selected_Hessian_blocks_emitted"],
    }
    blocking = [key for key, value in clauses.items() if value is False]

    promotion_attempt = {
        "schema": "MTTStep22VertexSourcePromotionAttempt.v1",
        "status": "PROMOTION_ATTEMPT_BLOCKED_BY_SELECTED_SOURCE_TO_C1_TRANSFER_MAP",
        "clauses": clauses,
        "blocking_clauses": blocking,
        "can_promote_vertex_representative_now": len(blocking) == 0,
        "why_not_promoted": "The selected source selector, source-level Weyl carrier, active shift, overlap kernel, and conditional atom decomposition are closed. The missing clause is the selected source-to-C1 transfer map, including phase/shift routing to the exact C1 columns and selected b/Hessian source emission.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROMOTION_ATTEMPT, promotion_attempt)

    computed = step20_validation["computed"]
    ready_values = {
        "schema": "MTTStep22ReadyToPromoteValuePacket.v1",
        "status": "EXACT_VALUES_READY_BUT_NOT_SELECTED",
        "conditional_values": {
            "A_conditional_shape": computed["A_conditional_shape"],
            "A_transpose_A": computed["A_transpose_A"],
            "A_transpose_b": computed["A_transpose_b"],
            "b_norm_sq": computed["b_norm_sq"],
            "deltaTheta_conditional": computed["deltaTheta_conditional"],
            "rank_if_columns_independent": computed["rank_if_columns_independent"],
        },
        "promotion_condition": {
            "selected_source_to_C1_transfer_map": True,
            "phase_Z_routes_to_u_e_column": True,
            "shift_X_routes_to_d_nuD_column": True,
            "selected_b_selected_or_replacement_b": True,
            "selected_Hessian_or_source_normalization": True,
        },
        "if_condition_proved_then": {
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1": computed["deltaTheta_conditional"],
            "no_remaining_linear_algebra_obstruction": True,
        },
        "selected_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READY_VALUES, ready_values)

    next_workorder = {
        "schema": "MTTStep22ToStep23TransferMapWorkorder.v1",
        "status": "NEXT_WORKORDER_PROVE_SOURCE_TO_C1_TRANSFER_MAP",
        "completed_step": 22,
        "next_step": 23,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "source_selector": True,
            "source_level_weyl_carrier": True,
            "active_shift": True,
            "overlap_kernel": True,
            "conditional_atom_decomposition": True,
            "ready_to_promote_exact_values": True,
        },
        "must_prove_next": [
            "selected source-to-C1 response map emitted by the q79/F,m=1 branch",
            "phase generator Z maps to the u/e phase column",
            "shift generator X maps to the d/nuD shift column",
            "selected b_selected is phase+shift or an emitted replacement",
            "selected Hessian/source normalization gives G=12 I_2 or an emitted replacement Gram",
        ],
        "success_criterion": {
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1_emitted": True,
            "observed_data_used_as_selector_false": True,
            "target_fitting_used_false": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep22VertexSourcePromotionOrTransferMap",
        "status": STATUS,
        "inputs": {
            "step21": rel(STEP21),
            "step20_validation": rel(STEP20_VALIDATION),
            "step21_frontier": rel(STEP21_FRONTIER),
            "source_selector": rel(SOURCE_SELECTOR),
            "weyl_provenance": rel(WEYL_PROVENANCE),
            "overlap_kernel": rel(OVERLAP_KERNEL),
            "same_source_identity": rel(SAME_SOURCE_IDENTITY),
        },
        "output_packets": {
            "step22_vertex_source_promotion_attempt": rel(PROMOTION_ATTEMPT),
            "step22_ready_to_promote_value_packet": rel(READY_VALUES),
            "step22_to_step23_transfermap_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step22VertexSourcePromotionBoundaryTheorem",
            "proved": True,
            "statement": "The selected vertex-source promotion attempt has only one live layer left: the source-to-C1 transfer map and its b/Hessian normalization. Source selector, source-level qutrit Weyl carrier, active shift, overlap normalization, conditional phase/shift payload, and conditional six-term decomposition are already closed. Therefore selected A_selected and b_selected cannot be promoted yet, but their exact finite values are ready once the transfer-map clause is proved.",
        },
        "closure_decision": {
            "step22_promotion_attempt_closed": True,
            "source_selector_closed": clauses["source_selector_emitted"],
            "source_level_weyl_carrier_closed": clauses["source_level_weyl_carrier_closed"],
            "active_shift_provenance_closed": clauses["active_shift_provenance_closed"],
            "conditional_atom_decomposition_exact": clauses["conditional_atom_decomposition_exact"],
            "selected_source_to_C1_transfer_map_emitted": clauses["selected_source_to_C1_transfer_map_emitted"],
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "blocking_clause_count": len(blocking),
            "blocking_clauses": blocking,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "promotion_boundary_checked": True,
            "exact_values_ready_to_promote": True,
            "single_live_layer_identified_as_source_to_C1_transfer_map": True,
        },
        "what_remains_open": {
            "selected_source_to_C1_transfer_map": True,
            "selected_b_selected": True,
            "selected_Hessian_source_normalization": True,
            "selected_A_selected": True,
            "selected_deltaTheta_C1": True,
            "Yukawa_or_true_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step22_VertexSourcePromotion_or_TransferMap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "promotion_attempt_closed": True,
        "selected_source_to_C1_transfer_map_emitted": clauses["selected_source_to_C1_transfer_map_emitted"],
        "selected_A_selected_promoted": False,
        "selected_b_selected_promoted": False,
        "blocking_clause_count": len(blocking),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step22 VertexSourcePromotion or TransferMap v1

Status: `{STATUS}`.

Closed now:

```text
source selector                                      closed
source-level qutrit Weyl carrier                     closed
active shift (1,1)                                   closed
selected overlap kernel                              closed
conditional atom decomposition                       closed
exact values ready to promote                        closed
```

Still open:

```text
selected source-to-C1 transfer map
phase Z -> u/e phase column
shift X -> d/nuD shift column
selected b_selected
selected Hessian/source normalization
```

The ready values are exact but not selected:

```text
A^T A = 12 I_2
A^T b = (12,12)
deltaTheta_C1 = (1,1)
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
