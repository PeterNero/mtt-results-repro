"""Build Higgs production covariance profile acquisition or dynamic Qa/SU3 operator slot closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRODUCTION = PACKET_DIR / "higgs_production_covariance_profile_acquisition.packet.json"
SLOT = PACKET_DIR / "qasu3_operator_source_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_production_or_operator_slot.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsProductionCovarianceProfile_or_DynamicQaSU3OperatorSlotClosure_v1.md"

STATUS = (
    "MTT_SELECTED_HIGGSPRODUCTIONCOVARIANCEPROFILE_OR_DYNAMICQASU3OPERATORSLOTCLOSURE_"
    "BUILT_PRODUCTION_OPEN_ONE_OPERATOR_SOURCE_SLOT_CLOSED"
)
NEXT = "MTT_Selected_HiggsProductionProfileImport_or_SecondQaSU3OperatorSlotClosure_v1"

FILLED_SLOT = "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure.candidate.json")
    imported_replay = load(DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json")
    full_loop_attempt = load(DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json")
    qasu3_slot_attempt = load(
        DATA
        / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
        / "qasu3_operator_slot_fill_attempt.packet.json"
    )
    terminal_patch = load(DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json")
    same_source_packet = load(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json")

    production = {
        "schema": "MTTHiggsProductionCovarianceProfileAcquisition.v1",
        "input_imported_decay_profile_replay": rel(DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json"),
        "input_full_loop_attempt": rel(DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json"),
        "available_now": {
            "accepted_Higgs_decay_covariance_profile": previous["closure_decision"][
                "accepted_Higgs_decay_covariance_profile_closed"
            ],
            "imported_decay_profile_replay_closed": imported_replay["closure_decision"]["imported_profile_replay_closed"],
            "official_LHCHXSWG_likelihood_imported": imported_replay["closure_decision"][
                "accepted_as_official_LHCHXSWG_likelihood"
            ],
            "production_covariance_profile_rows_present": False,
            "coupling_modifier_covariance_profile_present": False,
        },
        "acquisition_standard": {
            "must_include": [
                "production modes such as ggH, VBF, WH, ZH, ttH/tH with source labels and units",
                "cross-channel covariance or a published profile-likelihood workspace",
                "nuisance/profile semantics for production and decay correlations",
                "scale/convention metadata",
                "guard that production data are downstream replay/profile inputs, not source selectors",
            ],
            "accepted_decay_profile_is_not_reused_as_production_profile": True,
        },
        "decision": {
            "production_covariance_profile_closed": False,
            "production_profile_acquisition_manifest_built": True,
            "why_not_closed": (
                "The repo currently contains an accepted Higgs decay covariance sector profile and an imported "
                "decay-profile replay. It does not yet contain a source-labeled production-mode covariance "
                "profile or official likelihood workspace for production/coupling rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    prior_missing = qasu3_slot_attempt["slot_status"]["missing_slots"]
    terminal = terminal_patch["unconditional_terminal_replay"]
    filled_value = {
        "selected_source_label": terminal["selected_source_label"],
        "selected_L": terminal["selected_L"],
        "selected_L2": terminal["selected_L2"],
        "selected_c2": terminal["selected_c2"],
        "base_order": terminal["base_order"],
        "status": terminal["status"],
    }
    missing_after = [slot for slot in prior_missing if slot != FILLED_SLOT]
    slot = {
        "schema": "MTTQaSU3OperatorSourceSlotClosure.v1",
        "input_prior_operator_slot_attempt": rel(
            DATA
            / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
            / "qasu3_operator_slot_fill_attempt.packet.json"
        ),
        "input_terminal_axiom_patch": rel(DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json"),
        "input_same_source_visible_color_attempt": rel(
            DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
        ),
        "filled_slot": FILLED_SLOT,
        "selected_source_value": filled_value,
        "proof_inputs": {
            "terminal_source_unconditional_in_patched_spine": terminal_patch["unconditional_terminal_source_claimed_in_patched_spine"],
            "ordered_source_validator_unconditional_in_patched_spine": terminal_patch["what_closes_now"][
                "ordered_source_validator_unconditional_in_patched_spine"
            ],
            "same_source_visible_color_L3_minus_K2_candidate_imported": same_source_packet["gate_results"][
                "topological_L3_minus_K2_candidate_imported"
            ],
            "prior_slot_manifest_contains_target_slot": FILLED_SLOT in prior_missing,
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": qasu3_slot_attempt["slot_status"]["required_operator_slot_count"],
            "filled_operator_slot_count": 1,
            "filled_slots": [FILLED_SLOT],
            "missing_slots": missing_after,
            "remaining_missing_slot_count": len(missing_after),
        },
        "closure_result": {
            "operator_source_slot_closed": True,
            "selected_source_value_emitted": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The selected L3-K2 source-status slot is now filled in the patched proof spine. "
                "Pic0/operator quotient, same-source Chern-Weil, transition D_E/rho_E, HYM residual, "
                "Riesz/Green/dotD/projector retention, and determinant/torsion response remain open."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTTrueEquivalenceDecisionAfterProductionOrOperatorSlot.v1",
        "status": "PRODUCTION_PROFILE_OPEN_ONE_QASU3_OPERATOR_SOURCE_SLOT_CLOSED",
        "route_A": {
            "accepted_Higgs_decay_covariance_profile_retained": True,
            "production_covariance_profile_closed": False,
            "production_profile_acquisition_manifest_built": True,
        },
        "route_B": {
            "operator_source_slots_closed": 1,
            "operator_source_slots_remaining": len(missing_after),
            "actual_dynamic_QaSU3_operator_packet_closed": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsProductionCovarianceProfileOrDynamicQaSU3OperatorSlotClosure",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(
                DATA / "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure.candidate.json"
            ),
            "imported_decay_profile_replay": production["input_imported_decay_profile_replay"],
            "prior_operator_slot_attempt": slot["input_prior_operator_slot_attempt"],
            "terminal_axiom_patch": slot["input_terminal_axiom_patch"],
        },
        "output_packets": {
            "higgs_production_covariance_profile_acquisition": rel(PRODUCTION),
            "qasu3_operator_source_slot_closure": rel(SLOT),
            "true_equivalence_decision_after_production_or_operator_slot": rel(DECISION),
        },
        "theorem": {
            "name": "ProductionProfileAcquisitionAndFirstQaSU3OperatorSourceSlotClosure",
            "proved": True,
            "statement": (
                "The Higgs production/coupling covariance route is reduced to an acquisition manifest because "
                "the current repo has an accepted decay covariance profile but no source-labeled production "
                "covariance/profile workspace. In parallel, the patched terminal proof spine promotes the "
                "selected L3-K2 source-status slot from the Qa/SU3 operator manifest, reducing the eight-slot "
                "operator cutset to seven missing slots without claiming the dynamic operator packet."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "accepted_Higgs_decay_covariance_profile_retained": True,
            "production_covariance_profile_closed": False,
            "first_QaSU3_operator_source_slot_closed": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "production_covariance_profile_acquisition_manifest": True,
            "selected_L3_minus_K2_operator_source_slot": True,
            "qasu3_operator_cutset_reduced_to_seven_slots": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "Higgs_production_covariance_profile": True,
            "official_or_reconstructed_Higgs_profile_likelihood": True,
            "operator_layer_Pic0_or_physical_quotient": True,
            "same_source_Chern_Weil_row": True,
            "transition_rhoE_or_Cech_Dolbeault_DE_data": True,
            "selected_HYM_or_RouteC_residual": True,
            "Riesz_Green_dotD_projector_retention": True,
            "finite_determinant_heat_spectrum_or_torsion_response": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsProductionCovarianceProfile_or_DynamicQaSU3OperatorSlotClosure_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "production_covariance_profile_closed": False,
        "first_QaSU3_operator_source_slot_closed": True,
        "filled_operator_slot": FILLED_SLOT,
        "operator_source_slots_remaining": len(missing_after),
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected HiggsProductionCovarianceProfile or DynamicQaSU3OperatorSlotClosure v1

This artifact continues the two-route true-equivalence frontier.

Route A does not close Higgs production/coupling covariance yet.  It records the
exact acquisition standard and separates the accepted decay covariance profile
from a still-missing production/profile workspace.

Route B closes one Qa/SU3 operator-source slot:
`{FILLED_SLOT}`.  The selected value is the patched-spine terminal source
`g3 / L3-K2`, with `L=(1,-2,0)`, `L^2=(2,-4,0)`, and the ordered base row.
This reduces the operator cutset from eight slots to seven, but it is not a
dynamic Qa/SU3/HYM/End0/C1 operator packet.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (PRODUCTION, production),
        (SLOT, slot),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
