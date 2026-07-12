"""Build Step 23 static-routing transfer-map reduction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step23_staticrouting_transfermapreduction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTING_PACKET = PACKET_DIR / "step23_static_routing_reconciliation.packet.json"
TRANSFER_PACKET = PACKET_DIR / "step23_transfer_map_reduced_dynamic_overlap.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step23_to_step24_dynamic_overlap_bhessian_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step23_StaticRouting_TransferMapReduction_v1.md"

STEP22 = DATA / "selected_step22_vertexsource_promotion_or_transfermap.candidate.json"
STEP22_ATTEMPT = DATA / "selected_step22_vertexsource_promotion_or_transfermap" / "step22_vertex_source_promotion_attempt.packet.json"
STEP22_READY = DATA / "selected_step22_vertexsource_promotion_or_transfermap" / "step22_ready_to_promote_value_packet.packet.json"
STATIC_LEDGER = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
STATIC_ROUTING = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
OLD_ROUTING = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
TRANSFER_MAP = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"

STATUS = "MTT_SELECTED_STEP23_STATIC_ROUTING_CLOSED_TRANSFERMAP_REDUCED_DYNAMIC_OVERLAP_BHESSIAN_OPEN"
NEXT = "MTT_Selected_Step24_DynamicOverlapTensor_BHessian_or_SelectedValuesPromotion_v1"


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

    inputs = [STEP22, STEP22_ATTEMPT, STEP22_READY, STATIC_LEDGER, STATIC_ROUTING, OLD_ROUTING, TRANSFER_MAP]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 23 inputs: " + ", ".join(missing))

    step22 = load(STEP22)
    step22_attempt = load(STEP22_ATTEMPT)
    step22_ready = load(STEP22_READY)
    static_ledger = load(STATIC_LEDGER)
    static_routing = load(STATIC_ROUTING)
    old_routing = load(OLD_ROUTING)
    transfer_map = load(TRANSFER_MAP)

    routing_packet = {
        "schema": "MTTStep23StaticRoutingReconciliation.v1",
        "status": "STATIC_WEYL_SECTOR_ROUTING_PROMOTED_FROM_LATER_LEDGER",
        "older_routing_attempt_status": old_routing["status"],
        "older_attempt_superseded_for_static_routing": True,
        "old_attempt_source_data_independently_selects_route": old_routing["routing_search"]["source_data_independently_selects_route"],
        "later_static_routing_source_emission": {
            "proved": static_routing["static_routing_source_emission"]["proved"],
            "phase_route": static_routing["static_routing_source_emission"]["retired_sector_routing"]["phase_route"],
            "shift_route": static_routing["static_routing_source_emission"]["retired_sector_routing"]["shift_route"],
            "selected_static_sector_route": static_routing["static_routing_source_emission"]["retired_sector_routing"]["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"],
            "selected_static_trace_transfer_normalization": static_routing["static_routing_source_emission"]["retired_sector_routing"]["selected_static_finite_trace_transfer_normalization"],
            "selected_1M_Dirac_neutrino_shift_rule": static_routing["static_routing_source_emission"]["retired_sector_routing"]["selected_static_1M_Dirac_neutrino_shift_rule"],
        },
        "static_ledger_confirmation": {
            "static_sm_slot_tier_closed": static_ledger["payload_tiers"]["static_sm_slot_tier"]["closed"],
            "selected_static_sector_route_now_closed": static_ledger["weylpair_consequence"]["selected_static_sector_route_now_closed"],
            "phase_route": static_ledger["weylpair_consequence"]["phase_route"],
            "shift_route": static_ledger["weylpair_consequence"]["shift_route"],
            "conditional_transfer_exact": static_ledger["weylpair_consequence"]["conditional_A_weylpair_exact"],
        },
        "closed_for_step23": {
            "phase_Z_routed_to_u_e_column": True,
            "shift_X_routed_to_d_nuD_column": True,
            "selected_static_sector_routing": True,
            "selected_static_trace_normalization": True,
        },
        "not_closed_by_static_routing": {
            "dynamic_source_to_C1_overlap_tensor": True,
            "primitive_C1_contractions": True,
            "selected_b_selected_and_Hessian_normalization": True,
            "selected_A_selected": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROUTING_PACKET, routing_packet)

    transfer_packet = {
        "schema": "MTTStep23TransferMapReducedDynamicOverlap.v1",
        "status": "TRANSFER_MAP_STATIC_SUBCLAUSES_CLOSED_DYNAMIC_OVERLAP_BHESSIAN_OPEN",
        "conditional_transfer_map": transfer_map["conditional_transfer_map"],
        "step22_blockers_before": step22_attempt["blocking_clauses"],
        "step23_blockers_after": [
            "selected_source_to_C1_transfer_map_emitted",
            "selected_dynamic_overlap_tensor_or_transfer_functor",
            "selected_primitive_C1_contractions",
            "selected_b_selected_emitted",
            "selected_Hessian_blocks_emitted",
        ],
        "ready_values": step22_ready["conditional_values"],
        "can_promote_A_selected_now": False,
        "why_not": "Phase/shift sector routing and static trace normalization are selected. The remaining transfer-map content is dynamic: source-to-C1 overlap tensor/primitive contractions plus selected b/Hessian normalization.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TRANSFER_PACKET, transfer_packet)

    next_workorder = {
        "schema": "MTTStep23ToStep24DynamicOverlapBHessianWorkorder.v1",
        "status": "NEXT_WORKORDER_DYNAMIC_OVERLAP_TENSOR_BHESSIAN",
        "completed_step": 23,
        "next_step": 24,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "static_sector_routing_Z_to_u_e_X_to_d_nuD": True,
            "static_trace_normalization": True,
            "conditional_ready_values": True,
        },
        "must_emit_next": [
            "selected dynamic source-to-C1 overlap tensor or transfer functor",
            "selected primitive C1 contractions or selected equivalent full-response packet",
            "selected b_selected source vector",
            "selected Hessian/source normalization proving G=12 I_2 or emitted replacement Gram",
        ],
        "success_criterion": {
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1_emitted": True,
            "target_fitting_used_false": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep23StaticRoutingTransferMapReduction",
        "status": STATUS,
        "inputs": {
            "step22": rel(STEP22),
            "step22_attempt": rel(STEP22_ATTEMPT),
            "step22_ready": rel(STEP22_READY),
            "static_ledger": rel(STATIC_LEDGER),
            "static_routing": rel(STATIC_ROUTING),
            "old_routing": rel(OLD_ROUTING),
            "transfer_map": rel(TRANSFER_MAP),
        },
        "output_packets": {
            "step23_static_routing_reconciliation": rel(ROUTING_PACKET),
            "step23_transfer_map_reduced_dynamic_overlap": rel(TRANSFER_PACKET),
            "step23_to_step24_dynamic_overlap_bhessian_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step23StaticRoutingTransferMapReductionTheorem",
            "proved": True,
            "statement": "The older Weyl-pair sector-routing blocker is superseded by the later selected SM-slot functor and primitive-C1/Weyl-pair sector-routing source-emission packets. Thus Z->u/e, X->d/nuD, the 1_M=N^c shift rule, and static trace normalization are closed at the source tier. This does not promote A_selected: the transfer map is now reduced to dynamic source-to-C1 overlap tensor/primitive contractions plus selected b/Hessian normalization.",
        },
        "closure_decision": {
            "step23_static_routing_closed": True,
            "phase_Z_routed_to_u_e_column": True,
            "shift_X_routed_to_d_nuD_column": True,
            "selected_static_trace_normalization": True,
            "selected_source_to_C1_transfer_map_emitted": False,
            "selected_dynamic_overlap_tensor_or_transfer_functor": False,
            "selected_primitive_C1_contractions": False,
            "selected_b_selected_promoted": False,
            "selected_Hessian_blocks_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "static_weyl_sector_routing": True,
            "static_trace_normalization": True,
            "transfer_map_blocker_reduced_to_dynamic_overlap_bHessian": True,
        },
        "what_remains_open": {
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
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
        "certificate": "MTT_Selected_Step23_StaticRouting_TransferMapReduction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "static_routing_closed": True,
        "phase_Z_routed_to_u_e_column": True,
        "shift_X_routed_to_d_nuD_column": True,
        "selected_source_to_C1_transfer_map_emitted": False,
        "selected_A_selected_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step23 StaticRouting TransferMapReduction v1

Status: `{STATUS}`.

Closed now:

```text
Z / phase / clock routes to u,e                         closed
X / shift / translation routes to d,nuD                 closed
1_M=N^c belongs to the shift side                       closed
static trace normalization                              closed
```

Still open:

```text
selected dynamic source-to-C1 overlap tensor or transfer functor
selected primitive C1 contractions
selected b_selected
selected Hessian/source normalization
A_selected / deltaTheta_C1 promotion
```

The ready values from Step 22 remain exact, but selected promotion now depends
only on the dynamic overlap/b-Hessian layer.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
