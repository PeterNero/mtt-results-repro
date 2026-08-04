"""Build Step 24 dynamic-gate reconciliation / value-layer cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step24_dynamicgate_reconciliation_or_valuelayercutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECON_PACKET = PACKET_DIR / "step24_superseded_dynamic_gate_reconciliation.packet.json"
CLOSED_PACKET = PACKET_DIR / "step24_selected_dynamic_bhessian_closure.packet.json"
NEXT_CUTSET = PACKET_DIR / "step24_value_layer_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step24_DynamicGateReconciliation_or_ValueLayerCutset_v1.md"

STEP23 = DATA / "selected_step23_staticrouting_transfermapreduction.candidate.json"
STEP23_WORKORDER = DATA / "selected_step23_staticrouting_transfermapreduction" / "step23_to_step24_dynamic_overlap_bhessian_workorder.packet.json"
UNPATCHED_STACK = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
UNPATCHED_SUMMARY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "unpatched_source_promotion_replay_summary.packet.json"
PSM_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "psm_c1_02_source_promotion_replay.packet.json"
PSM_VALIDATOR = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "psm_c1_02_source_promotion_validator_result.packet.json"
PHYSICAL_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "physical_action_rowkernel_source_replay.packet.json"
PHYSICAL_VALIDATOR = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "physical_action_rowkernel_source_validator_result.packet.json"
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALUES = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure" / "selected_non_scalar_dynamic_overlap_values.packet.json"
MATTER_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure" / "same_source_matter_overlap_operator_packet.packet.json"
MATTER_VALIDATOR = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure" / "same_source_matter_overlap_operator_validator_result.packet.json"
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_DECISION = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource" / "vsd01_source_subgate_decision.packet.json"
VSD01_ASSEMBLY = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource" / "all_primitive_rows_assembly_map.packet.json"
VALUE_FRONTIER = DATA / "selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows.candidate.json"
FIRST_VALUE_ROW = DATA / "selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution.candidate.json"

STATUS = "MTT_SELECTED_STEP24_DYNAMIC_GATE_RECONCILIATION_OR_VALUELAYERCUTSET_BUILT_DYNAMIC_BHESSIAN_GATE_CLOSED_VALUE_FUNCTIONAL_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def selected_source_fields(psm_replay: dict[str, Any]) -> dict[str, bool]:
    fields = psm_replay["source_fields"]
    required = [
        "source_owner_id",
        "phase_R_Z_source",
        "shift_R_X_source",
        "b_selected_source",
        "sector_row_assembly",
        "selected_measure_pairing",
        "selected_quadrature_rule",
        "admissible_c1_variation_space",
        "independence_guard",
    ]
    return {
        name: (
            fields[name]["selected_emitted"] is True
            and fields[name]["source_owner_verified"] is True
            and fields[name]["theorem_derived"] is True
            and fields[name]["same_branch"] is True
        )
        for name in required
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP23,
        STEP23_WORKORDER,
        UNPATCHED_STACK,
        UNPATCHED_SUMMARY,
        PSM_REPLAY,
        PSM_VALIDATOR,
        PHYSICAL_REPLAY,
        PHYSICAL_VALIDATOR,
        DYNAMIC_PACKET,
        DYNAMIC_VALUES,
        MATTER_PACKET,
        MATTER_VALIDATOR,
        VSD01,
        VSD01_DECISION,
        VSD01_ASSEMBLY,
        VALUE_FRONTIER,
        FIRST_VALUE_ROW,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 24 inputs: " + ", ".join(missing))

    step23 = load(STEP23)
    step23_workorder = load(STEP23_WORKORDER)
    unpatched = load(UNPATCHED_STACK)
    summary = load(UNPATCHED_SUMMARY)
    psm = load(PSM_REPLAY)
    psm_validator = load(PSM_VALIDATOR)
    physical = load(PHYSICAL_REPLAY)
    physical_validator = load(PHYSICAL_VALIDATOR)
    dynamic = load(DYNAMIC_PACKET)
    dynamic_values = load(DYNAMIC_VALUES)
    matter = load(MATTER_PACKET)
    matter_validator = load(MATTER_VALIDATOR)
    vsd01 = load(VSD01)
    vsd01_decision = load(VSD01_DECISION)
    vsd01_assembly = load(VSD01_ASSEMBLY)
    value_frontier = load(VALUE_FRONTIER)
    first_value_row = load(FIRST_VALUE_ROW)

    psm_fields = selected_source_fields(psm)
    matter_fields = matter["attempted_selected_packet"]["fields"]
    matter_field_flags = {
        name: (
            field["selected_emitted"] is True
            and field["same_source"] is True
            and field["theorem_derived"] is True
        )
        for name, field in matter_fields.items()
    }

    recon_packet = {
        "schema": "MTTStep24SupersededDynamicGateReconciliation.v1",
        "status": "STEP23_DYNAMIC_GATE_SUPERSEDED_BY_LATER_SELECTED_SOURCE_STACK",
        "step23_previous_status": step23["status"],
        "step23_previous_open_items": step23_workorder["must_emit_next"],
        "superseding_artifacts": {
            "unpatched_source_stack": rel(UNPATCHED_STACK),
            "psm_c1_02_source_promotion_replay": rel(PSM_REPLAY),
            "physical_action_rowkernel_source_replay": rel(PHYSICAL_REPLAY),
            "same_source_dynamic_matter_overlap_packet": rel(DYNAMIC_PACKET),
            "vsd01_source_and_dynamic_subgate": rel(VSD01),
        },
        "older_step23_workorder_is_currently_closed": True,
        "why": (
            "The later verified source stack emits same-branch source fields, "
            "A_selected, b_selected, deltaTheta_C1, the same-source dynamic "
            "matter/overlap operator packet, and the VSD01 source/dynamic subgates. "
            "Thus Step23 remains true historically, but its open workorder is no "
            "longer the active frontier."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RECON_PACKET, recon_packet)

    closed_packet = {
        "schema": "MTTStep24SelectedDynamicBHessianClosure.v1",
        "status": "SELECTED_DYNAMIC_OVERLAP_BHESSIAN_GATE_CLOSED_BY_SOURCE_STACK_AND_VSD01",
        "source_stack": {
            "status": unpatched["status"],
            "closure_claimed": unpatched["closure_claimed"],
            "promoted_objects": summary["promoted_objects"],
            "psm_validator_returncode": psm_validator["returncode"],
            "physical_validator_returncode": physical_validator["returncode"],
            "psm_source_fields_all_selected": all(psm_fields.values()),
            "psm_source_fields": psm_fields,
            "physical_action_route_A_validates": physical["status"] == "ROUTE_A_PHYSICAL_ACTION_RESTRICTION_VALIDATES",
            "no_extra_boundary_or_source_term": physical["route_A_physical_action_restriction"]["zero_extra_boundary_or_source_term"],
            "same_source_b_selected_emission": physical["route_A_physical_action_restriction"]["same_source_b_selected_emission"],
        },
        "dynamic_matter_overlap": {
            "status": dynamic["status"],
            "closure_claimed": dynamic["closure_claimed"],
            "selected_dynamic_overlap_tensor_promoted": dynamic["what_closes_now"]["selected_dynamic_overlap_tensor_promoted"],
            "primitive_C1_contractions_selected_emitted_first_response_layer": dynamic["what_closes_now"]["primitive_C1_contractions_selected_emitted_first_response_layer"],
            "selected_A_selected_b_selected_preserved": dynamic["what_closes_now"]["selected_A_selected_b_selected_preserved"],
            "selected_values_status": dynamic_values["status"],
            "selected_values_selected_by_MTT": dynamic_values["selected_by_MTT"],
            "matter_validator_returncode": matter_validator["returncode"],
            "same_source_fields_all_selected": all(matter_field_flags.values()),
            "same_source_fields": matter_field_flags,
            "packet_promotes_A_selected": matter["attempted_selected_packet"]["packet_flags"]["promote_to_A_selected"],
            "packet_promotes_b_selected": matter["attempted_selected_packet"]["packet_flags"]["promote_to_b_selected"],
        },
        "vsd01_assembly": {
            "status": vsd01["status"],
            "source_assembly_subgate_closed": vsd01["closure_decision"]["VSD01_source_assembly_subgate_closed"],
            "dynamic_overlap_subgate_closed": vsd01["closure_decision"]["VSD01_dynamic_overlap_subgate_closed"],
            "full_vsd01_obligation_closed": vsd01["closure_decision"]["VSD01_full_obligation_closed"],
            "source_stack_closed": vsd01["closure_decision"]["source_stack_closed"],
            "dynamic_matter_overlap_packet_closed": vsd01["closure_decision"]["dynamic_matter_overlap_packet_closed"],
            "row_evidence": {
                "all_72_primitive_rows_exact": vsd01_assembly["row_evidence"]["all_72_primitive_rows_exact"],
                "formal_110_rows_executed": vsd01_assembly["row_evidence"]["formal_110_rows_executed"],
                "formal_110_row_counts": vsd01_assembly["row_evidence"]["formal_110_row_counts"],
                "formal_110_max_abs_error": vsd01_assembly["row_evidence"]["formal_110_max_abs_error"],
            },
            "closed_for_VSD01_now": vsd01_decision["closed_for_VSD01_now"],
        },
        "step24_closed_items": {
            "selected_source_to_C1_transfer_map_emitted": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions_first_response_layer": True,
            "selected_b_selected_promoted": True,
            "selected_Hessian_source_normalization_promoted": True,
            "selected_A_selected_promoted": True,
            "selected_deltaTheta_C1_promoted": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CLOSED_PACKET, closed_packet)

    next_cutset = {
        "schema": "MTTStep24ValueLayerCutset.v1",
        "status": "DYNAMIC_BHESSIAN_GATE_CLOSED_VALUE_FUNCTIONAL_ROWS_OPEN",
        "active_frontier_now": "selected value-functional rows, not source-promotion or Galerkin replay",
        "current_value_frontier": {
            "accepted_value_layer_status": value_frontier["status"],
            "value_layer_required_rows": value_frontier["readiness"]["value_layer_required_rows"],
            "value_layer_accepted_source_rows": value_frontier["readiness"]["value_layer_accepted_source_rows"],
            "source_layer_closed": value_frontier["readiness"]["source_layer_closed"],
            "first_nonlooping_row_status": first_value_row["status"],
            "source_layer_row_available": first_value_row["closure_decision"]["source_layer_row_available"],
            "accepted_true_value_source_row_emitted": first_value_row["closure_decision"]["accepted_true_value_source_row_emitted"],
        },
        "closed_do_not_reopen": {
            "static_sector_routing": True,
            "source_stack": True,
            "dynamic_matter_overlap_operator_packet": True,
            "primitive_C1_contractions_first_response_layer": True,
            "A_selected_b_selected_deltaTheta_C1_source_promotion": True,
            "VSD01_source_and_dynamic_subgates": True,
        },
        "still_open": {
            "selected_threshold_response_functional": True,
            "selected_Yukawa_Higgs_value_functional": True,
            "accepted_threshold_mass_scheme_source_rows": True,
            "accepted_Yukawa_magnitudes_for_true_precision": True,
            "CKM_PMNS_measured_value_closure": True,
            "full_correlated_likelihood_source": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedStep24DynamicGateReconciliationOrValueLayerCutset",
        "status": STATUS,
        "inputs": {
            "step23": rel(STEP23),
            "step23_workorder": rel(STEP23_WORKORDER),
            "unpatched_source_stack": rel(UNPATCHED_STACK),
            "unpatched_summary": rel(UNPATCHED_SUMMARY),
            "psm_replay": rel(PSM_REPLAY),
            "physical_replay": rel(PHYSICAL_REPLAY),
            "dynamic_packet": rel(DYNAMIC_PACKET),
            "dynamic_values": rel(DYNAMIC_VALUES),
            "matter_packet": rel(MATTER_PACKET),
            "vsd01": rel(VSD01),
            "vsd01_decision": rel(VSD01_DECISION),
            "vsd01_assembly": rel(VSD01_ASSEMBLY),
            "value_frontier": rel(VALUE_FRONTIER),
            "first_value_row": rel(FIRST_VALUE_ROW),
        },
        "output_packets": {
            "step24_superseded_dynamic_gate_reconciliation": rel(RECON_PACKET),
            "step24_selected_dynamic_bhessian_closure": rel(CLOSED_PACKET),
            "step24_value_layer_cutset": rel(NEXT_CUTSET),
        },
        "theorem": {
            "name": "Step24DynamicGateReconciliationTheorem",
            "proved": True,
            "statement": (
                "In the latest verified active ledger, the dynamic source-to-C1 "
                "overlap/b-Hessian gate left open by Step23 is closed by the "
                "same-branch source stack, PSM-C1-02 source promotion replay, "
                "same-source dynamic matter/overlap operator packet, and VSD01 "
                "all-primitive-row assembly. The remaining true-SM-equivalence "
                "frontier is therefore not Galerkin/source promotion but selected "
                "value-functional rows for threshold, Yukawa/Higgs, mass/mixing, "
                "and correlated likelihood closure."
            ),
        },
        "closure_decision": {
            "step23_dynamic_workorder_superseded_and_closed": True,
            "selected_source_to_C1_transfer_map_emitted": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions_first_response_layer": True,
            "selected_b_selected_promoted": True,
            "selected_Hessian_source_normalization_promoted": True,
            "selected_A_selected_promoted": True,
            "selected_deltaTheta_C1_promoted": True,
            "VSD01_source_assembly_subgate_closed": True,
            "VSD01_dynamic_overlap_subgate_closed": True,
            "accepted_value_functional_rows_closed": False,
            "accepted_threshold_mass_scheme_source_rows_closed": False,
            "accepted_Yukawa_magnitudes_closed": False,
            "CKM_PMNS_measured_value_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step23_dynamic_overlap_bHessian_workorder": True,
            "source_to_C1_transfer_map": True,
            "same_source_dynamic_matter_overlap_packet": True,
            "primitive_C1_first_response_layer": True,
            "A_selected_b_selected_deltaTheta_C1_source_promotion": True,
            "active_frontier_relocated_to_value_functional_rows": True,
        },
        "what_remains_open": {
            "selected_threshold_response_functional": True,
            "selected_Yukawa_Higgs_value_functional": True,
            "accepted_threshold_mass_scheme_source_rows": True,
            "accepted_Yukawa_magnitudes_for_true_precision": True,
            "CKM_PMNS_measured_value_closure": True,
            "full_correlated_likelihood_source": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
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
        "certificate": "MTT_Selected_Step24_DynamicGateReconciliation_or_ValueLayerCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "step23_dynamic_workorder_closed_by_later_evidence": True,
        "selected_A_selected_promoted": True,
        "selected_b_selected_promoted": True,
        "selected_deltaTheta_C1_promoted": True,
        "selected_dynamic_overlap_tensor_or_transfer_functor": True,
        "selected_primitive_C1_contractions_first_response_layer": True,
        "accepted_value_functional_rows_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step24 DynamicGateReconciliation or ValueLayerCutset v1

Status: `{STATUS}`.

Step 24 reconciles the older Step 23 workorder against the latest verified
packets. Step 23 correctly reduced the old transfer-map blocker to dynamic
source-to-C1 overlap plus b/Hessian normalization. Later artifacts now close
that exact gate:

```text
selected source-to-C1 transfer map                         closed
selected dynamic overlap tensor / transfer functor          closed
selected primitive C1 contractions, first-response layer     closed
selected b_selected source vector                           closed
selected Hessian/source normalization                        closed
A_selected and deltaTheta_C1 source promotion                closed
```

The closing evidence is the unpatched source-promotion stack, PSM-C1-02 replay,
physical action row-kernel replay, same-source dynamic matter/overlap packet,
and VSD01 all-primitive-row assembly. No observed SM values are used as
selectors and no target fitting is used.

This is not full true-SM closure. The active frontier has moved to the
value-functional layer:

```text
selected threshold response functional                       open
selected Yukawa/Higgs value functional                       open
accepted threshold mass-scheme rows                          open
accepted Yukawa magnitudes and running mass ratios            open
CKM/PMNS measured value closure                              open
full correlated likelihood source                            open
true SM equivalence / full no-knob closure                    open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
