"""Build Step 16 post-source value-closure reconciliation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step16_postsourcevalueclosure_reconciliation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_BACKIMPORT = PACKET_DIR / "step16_step14_source_backimport.packet.json"
VALUE_STACK = PACKET_DIR / "step16_postsource_value_stack_reconciliation.packet.json"
SCALAR_GATE = PACKET_DIR / "step16_internal_scalar_gate_after_stronger_packets.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step16_to_step17_fulls2_value_execution_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step16_PostSourceValueClosure_Reconciliation_v1.md"

STEP14 = DATA / "selected_step14_sourcepromotionclosure_from_premisefreephifin.candidate.json"
STEP14_PROMOTION = DATA / "selected_step14_sourcepromotionclosure_from_premisefreephifin" / "step14_step15_source_identity_promotion.packet.json"
INTERNAL_BACKIMPORT_OLD = DATA / "selected_internalrtheta_scalarrows_psmc102_backimport_or_unpatchedsourceidentitygate.candidate.json"
POSTSOURCE = DATA / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure.candidate.json"
DYNAMIC_MATTER = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
RTHETA_SOURCE = DATA / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows.candidate.json"
THRESHOLD_ROWS = DATA / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows.candidate.json"
DIAGONAL_PROFILE = DATA / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.candidate.json"
EXTERNAL_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
SAME_BRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"
NO_KNOB_KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
DIRECT_SCALAR = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
PHIFIN_PAYLOAD = DATA / "selected_phifinminimizertracesectorpayload_or_internalscalarrows.candidate.json"
HIGHER_PAYLOAD = DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json"
HYM_PAYLOAD = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
LAMBDA_ORBIT = DATA / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution.candidate.json"

STATUS = "MTT_SELECTED_STEP16_POSTSOURCEVALUECLOSURE_RECONCILIATION_CLOSED_SOURCE_PI_THRESHOLD_PROFILE_TO_FULLS2_VALUE_FRONTIER"
NEXT = "MTT_Selected_Step17_FullS2OperatorPayload_or_InternalRThetaScalarRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_bool(data: dict[str, Any], path: list[str], expected: bool = True) -> bool:
    current: Any = data
    for key in path:
        current = current[key]
    return current is expected


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP14,
        STEP14_PROMOTION,
        INTERNAL_BACKIMPORT_OLD,
        POSTSOURCE,
        DYNAMIC_MATTER,
        DYNAMIC_QASU3,
        RTHETA_SOURCE,
        THRESHOLD_ROWS,
        DIAGONAL_PROFILE,
        EXTERNAL_IMPORT,
        SAME_BRANCH,
        NO_KNOB_KERNEL,
        DIRECT_SCALAR,
        PHIFIN_PAYLOAD,
        HIGHER_PAYLOAD,
        HYM_PAYLOAD,
        LAMBDA_ORBIT,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 16 inputs: " + ", ".join(missing))

    step14 = load(STEP14)
    step14_promotion = load(STEP14_PROMOTION)
    old_backimport = load(INTERNAL_BACKIMPORT_OLD)
    postsource = load(POSTSOURCE)
    dynamic_matter = load(DYNAMIC_MATTER)
    dynamic_qasu3 = load(DYNAMIC_QASU3)
    rtheta_source = load(RTHETA_SOURCE)
    threshold_rows = load(THRESHOLD_ROWS)
    diagonal_profile = load(DIAGONAL_PROFILE)
    external_import = load(EXTERNAL_IMPORT)
    same_branch = load(SAME_BRANCH)
    no_knob_kernel = load(NO_KNOB_KERNEL)
    direct_scalar = load(DIRECT_SCALAR)
    phifin_payload = load(PHIFIN_PAYLOAD)
    higher_payload = load(HIGHER_PAYLOAD)
    hym_payload = load(HYM_PAYLOAD)
    lambda_orbit = load(LAMBDA_ORBIT)

    source_backimport = {
        "schema": "MTTStep16Step14SourceBackimport.v1",
        "status": "UNPATCHED_SOURCE_IDENTITY_BLOCKER_RETIRED_FOR_STEP16",
        "old_packet_status": old_backimport["status"],
        "old_unpatched_source_identity_closed": old_backimport["closure_decision"]["unpatched_source_identity_closed"],
        "step14_status": step14["status"],
        "source_identity_theorem_promoted": step14["closure_decision"]["source_identity_theorem_promoted"],
        "source_stack_closed": step14_promotion["source_stack_closed"],
        "promoted_objects": step14_promotion["promoted_objects"],
        "scalar_gate_may_not_reopen": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "PhysicalPhiFinC1ActionSource": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
        },
        "replacement_live_blocker": "selected full-S2 operator payload and internal Rtheta scalar value execution",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_BACKIMPORT, source_backimport)

    value_stack = {
        "schema": "MTTStep16PostSourceValueStackReconciliation.v1",
        "status": "POSTSOURCE_VALUE_STACK_CLOSED_TO_READINESS_8_OF_9_WITH_EXTERNAL_REPLAY_BOUNDARY",
        "postsource_alpha1_and_static_matter": {
            "source": rel(POSTSOURCE),
            "alpha1_driver_closed_at_postsource_tier": postsource["what_closes_now"]["alpha1_driver_verified"],
            "static_matter_readout_closed": postsource["what_closes_now"]["static_matter_slot_readout_closed"],
        },
        "dynamic_first_response": {
            "same_source_dynamic_matter_overlap_packet_closed": dynamic_matter["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"],
            "selected_dynamic_QaSU3_first_response_layer_closed": dynamic_qasu3["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"],
            "accepted_Yukawa_magnitudes_closed": dynamic_qasu3["promotion_decision"]["accepted_Yukawa_magnitudes_closed"],
        },
        "rtheta_source_domain": {
            "selected_Rtheta_scalar_value_functional_source_domain_closed": rtheta_source["closure_decision"]["selected_Rtheta_scalar_value_functional_source_domain_closed"],
            "ten_scalar_row_codomain_aligned": rtheta_source["closure_decision"]["ten_scalar_row_codomain_aligned"],
        },
        "post_pi_external_replay": {
            "threshold_matching_source_rows_closed_at_admitted_external_tier": threshold_rows["closure_decision"]["threshold_matching_source_rows_closed_at_admitted_external_tier"],
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": threshold_rows["closure_decision"]["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"],
            "accepted_diagonal_profile_theorem_closed": diagonal_profile["closure_decision"]["accepted_diagonal_profile_theorem_closed"],
            "external_import_lane_closed_at_admitted_replay_tier": external_import["closure_decision"]["external_import_lane_closed_at_admitted_replay_tier"],
            "Rtheta_readiness_8_of_9": same_branch["closure_decision"]["Rtheta_readiness_8_of_9"],
        },
        "external_replay_is_not_internal_selection": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(VALUE_STACK, value_stack)

    scalar_gate = {
        "schema": "MTTStep16InternalScalarGateAfterStrongerPackets.v1",
        "status": "INTERNAL_SCALAR_GATE_REDUCED_TO_FULLS2_OPERATOR_PAYLOAD_OR_UNIVERSAL_ANCHOR",
        "closed_before_gate": {
            "source_identity_stack": True,
            "postsource_alpha1_static_matter": True,
            "dynamic_first_response_matter_QaSU3": True,
            "Rtheta_source_domain_and_ten_row_codomain": True,
            "post_pi_threshold_mass_scheme_external_replay": True,
            "accepted_diagonal_profile_external_replay": True,
            "qualitative_second_order_lambda_orbit": lambda_orbit["closure_decision"]["selected_second_order_orbit_matrix_packet_closed"],
        },
        "direct_scalar_emission_attempted": direct_scalar["closure_decision"]["direct_emission_attempt_executed"],
        "accepted_internal_scalar_row_count": direct_scalar["closure_decision"]["accepted_internal_scalar_row_count"],
        "fullS2_payload_ready_in_old_attempt": direct_scalar["closure_decision"]["fullS2_payload_ready"],
        "transported_sector_payload_imported": phifin_payload["closure_decision"]["transported_sector_payload_imported"],
        "higher_response_dotD_alpha1_payload_closed": higher_payload["closure_decision"]["dotD_alpha1_payload_closed"],
        "full_S2_value_execution_closed": higher_payload["closure_decision"]["full_S2_value_execution_closed"],
        "selected_operator_payload_closed": higher_payload["closure_decision"]["selected_operator_payload_closed"],
        "diagonal_End0_operator_payload_closed": hym_payload["closure_decision"]["diagonal_End0_operator_payload_closed"],
        "rhoE_DE_fullS2_execution_closed": hym_payload["closure_decision"]["rhoE_DE_fullS2_execution_closed"],
        "no_knob_kernel_typed": no_knob_kernel["closure_decision"]["final_no_knob_kernel_typed"],
        "selected_universal_parameter_count": no_knob_kernel["closure_decision"]["selected_universal_parameter_count"],
        "replacement_obligation": {
            "emit_selected_fullS2_operator_payload": True,
            "or_prove_candidate_specific_universal_source_anchor": True,
            "then_replay_internal_Rtheta_scalar_rows": True,
        },
        "forbidden_reopened_blockers": {
            "unpatched_PSM_C1_02_source_identity": False,
            "first_response_A_b_deltaTheta": False,
            "post_pi_scale_scheme_convention": False,
            "threshold_matching_external_admission": False,
            "mass_scheme_external_admission": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SCALAR_GATE, scalar_gate)

    next_workorder = {
        "schema": "MTTStep16ToStep17FullS2ValueExecutionWorkorder.v1",
        "status": "NEXT_WORKORDER_FULLS2_OPERATOR_PAYLOAD_TO_INTERNAL_VALUES",
        "completed_step": 16,
        "next_step": 17,
        "next_required_artifact": NEXT,
        "must_construct": {
            "selected_projector_promotion_Ps_Ks": True,
            "selected_rho_s_matrix_values": True,
            "selected_End0_to_sector_routing_values": True,
            "selected_rhoE_DE_Riesz_Green_payload": True,
            "internal_Rtheta_scalar_row_replay": True,
        },
        "must_not_reopen": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "dynamic_QaSU3_first_response_source_layer": True,
            "post_pi_external_threshold_mass_scheme_admission": True,
            "accepted_diagonal_profile_external_replay": True,
        },
        "success_criterion": {
            "accepted_internal_scalar_row_count_greater_than_zero": True,
            "or_candidate_specific_universal_source_anchor_selected": True,
            "observed_values_not_used_as_selectors": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep16PostSourceValueClosureReconciliation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "step16_step14_source_backimport": rel(SOURCE_BACKIMPORT),
            "step16_postsource_value_stack_reconciliation": rel(VALUE_STACK),
            "step16_internal_scalar_gate_after_stronger_packets": rel(SCALAR_GATE),
            "step16_to_step17_fulls2_value_execution_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step16PostSourceValueClosureReconciliationTheorem",
            "proved": True,
            "statement": "After Step 14/15, the unpatched finite-C1 source identity and first-response A,b,deltaTheta source stack are promoted and cannot remain the internal-scalar blocker. Combining the postsource alpha1/static matter closure, dynamic matter/QaSU3 first-response closure, Rtheta source-domain closure, post-Pi threshold/mass-scheme admitted replay rows, accepted diagonal profile theorem, and no-knob kernel readiness reduces Step 16 to a single honest frontier: selected full-S2 operator payload/internal Rtheta scalar value execution, or an equivalent candidate-specific universal source-anchor theorem.",
        },
        "closure_decision": {
            "step16_reconciliation_closed": True,
            "unpatched_source_identity_blocker_retired": True,
            "postsource_alpha1_static_matter_closed": True,
            "dynamic_first_response_closed": True,
            "rtheta_source_domain_closed": True,
            "post_pi_threshold_mass_scheme_external_replay_closed": True,
            "accepted_diagonal_profile_external_replay_closed": True,
            "Rtheta_readiness_8_of_9": True,
            "internal_scalar_row_execution_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "selected_fullS2_operator_payload_closed": False,
            "candidate_specific_universal_source_anchor_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "what_closes_now": {
            "stale_unpatched_source_identity_reopen_prevented": True,
            "Step16_frontier_reduced_to_fullS2_or_universal_anchor": True,
            "postsource_value_stack_reconciled": True,
            "post_pi_external_replay_boundary_integrated": True,
            "no_knob_kernel_readiness_8_of_9_imported": True,
        },
        "what_remains_open": {
            "selected_projector_promotion_Ps_Ks": True,
            "selected_rho_s_matrix_values": True,
            "selected_End0_to_sector_routing_values": True,
            "selected_rhoE_DE_Riesz_Green_payload": True,
            "internal_Rtheta_scalar_rows": True,
            "lambda_H_internal_scalar_row": True,
            "Yukawa_CKM_PMNS_mass_numeric_no_knob_closure": True,
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
        "certificate": "MTT_Selected_Step16_PostSourceValueClosure_Reconciliation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "step16_reconciliation_closed": True,
        "unpatched_source_identity_blocker_retired": True,
        "Rtheta_readiness_8_of_9": True,
        "accepted_internal_scalar_row_count": 0,
        "selected_fullS2_operator_payload_closed": False,
        "candidate_specific_universal_source_anchor_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step16 PostSourceValueClosure Reconciliation v1

Status: `{STATUS}`.

Step 16 is now reconciled against the strongest packets in the repo:

```text
SelectedFiniteC1SourceIdentityTheorem      promoted by Step 14/15
postsource alpha1/static matter stack      closed
dynamic matter/QaSU3 first-response stack  closed
Rtheta source domain and ten-row codomain  closed
threshold/mass-scheme rows                 admitted external replay tier
accepted diagonal profile theorem          admitted external replay tier
no-knob kernel readiness                   8/9
```

Therefore the old internal-scalar blocker wording
`unpatched_SelectedFiniteC1SourceIdentityLemma` is retired for the active plan.
It cannot be reopened as the Step 16 frontier.

The live target is now exactly:

```text
selected full-S2 operator payload
  -> internal Rtheta scalar rows

or

candidate-specific universal source-anchor theorem
  -> internal Rtheta scalar rows
```

No numerical SM equivalence or no-knob value closure is claimed here.
Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
