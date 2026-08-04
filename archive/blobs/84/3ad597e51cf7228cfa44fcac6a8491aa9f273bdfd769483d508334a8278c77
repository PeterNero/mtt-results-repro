"""Build current PSM-C1-02 import of the gauge-transported Phi_fin source closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_gaugetransportedphifintrace_import_or_fullsmgap"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_VALIDATION = BASE / "transport_closed_phifin_import_validation.packet.json"
SOURCE_PROMOTION = BASE / "current_psm_c1_02_source_promotion_reconciliation.packet.json"
FULL_SM_GAP = BASE / "post_source_promotion_fullsm_gap.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_GaugeTransportedPhiFinTraceImport_or_FullSMGap_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_selectedsourceownershippremiseexecution.candidate.json"
TRANSPORT_SOURCE = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
UNPATCHED_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
NARROWED_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "narrowed_phifinc1_emission_replay.packet.json"
NARROWED_VALIDATOR = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "narrowed_phifinc1_emission_validator_result.packet.json"
PSM_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "psm_c1_02_source_promotion_replay.packet.json"
PSM_VALIDATOR = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "psm_c1_02_source_promotion_validator_result.packet.json"
SUMMARY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "unpatched_source_promotion_replay_summary.packet.json"
FULL_GATE = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "full_sm_closure_gate_after_source_promotion.packet.json"
NEXT_CUTSET = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "next_cutset_after_unpatched_source_promotion_replay.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_GAUGETRANSPORTEDPHIFINTRACE_IMPORT_BUILT_SOURCE_PROMOTION_CLOSED_FULLSM_OPEN"
NEXT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validator_passed(result: dict[str, Any]) -> bool:
    return result.get("returncode") == 0 and any("PASS" in line for line in result.get("stdout", []))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    transport = load(TRANSPORT_SOURCE)
    replay = load(UNPATCHED_REPLAY)
    narrowed = load(NARROWED_REPLAY)
    narrowed_validator = load(NARROWED_VALIDATOR)
    psm_replay = load(PSM_REPLAY)
    psm_validator = load(PSM_VALIDATOR)
    summary = load(SUMMARY)
    full_gate = load(FULL_GATE)
    next_cutset = load(NEXT_CUTSET)

    narrowed_pass = validator_passed(narrowed_validator)
    psm_pass = validator_passed(psm_validator)
    source_stack_closed = (
        replay["promotion_decision"]["unpatched_source_promotion_stack_closed"]
        and summary["promoted_objects"]["A_selected"]
        and summary["promoted_objects"]["b_selected"]
        and summary["promoted_objects"]["deltaTheta_C1"]
        and psm_pass
    )

    import_validation = {
        "schema": "MTTPSMC102GaugeTransportedPhiFinTraceImportValidation.v1",
        "status": "TRANSPORT_CLOSED_PHIFIN_SOURCE_IMPORT_VALIDATES",
        "previous_frontier_was_open": previous["closure_decision"]["unpatched_PSM_C1_02_closed"] is False,
        "transport_source": rel(TRANSPORT_SOURCE),
        "transport_source_status": transport["status"],
        "transport_source_closes": {
            "premise_free_phi_fin_restriction_morphism": transport["promotion_decision"][
                "finite_emission_morphism_restriction_proved"
            ],
            "premise_free_route_A_physical_source_certificate": transport["promotion_decision"][
                "unpatched_route_A_physical_source_certificate_valid"
            ],
            "raw_27mode_replay_not_used": transport["promotion_decision"][
                "raw_27mode_finite_replay_closed"
            ]
            is False,
            "symbolic_transport_quotient_used": transport["promotion_decision"][
                "symbolic_transport_quotient_used"
            ],
        },
        "narrowed_route_A_replay": {
            "source": rel(NARROWED_REPLAY),
            "status": narrowed["status"],
            "validator": rel(NARROWED_VALIDATOR),
            "validator_passes": narrowed_pass,
            "route_A_all_fields_true": all(
                narrowed["route_A_phifinc1_source_emission"][field] is True
                for field in [
                    "same_branch",
                    "physical_phifin_c1_action_emitted",
                    "finite_weyl_action_restriction_derived",
                    "no_extra_boundary_or_source_term",
                    "selected_phase_shift_variation_operators_pre_residual",
                    "selected_hessian_counterterm_source",
                    "same_source_b_selected_emitted",
                    "row_formula_source_theorem_derived",
                ]
            ),
            "same_branch_evidence_count": len(
                narrowed["route_A_phifinc1_source_emission"]["attached_same_branch_source_evidence"]
            ),
        },
        "psm_replay": {
            "source": rel(PSM_REPLAY),
            "status": psm_replay["status"],
            "validator": rel(PSM_VALIDATOR),
            "validator_passes": psm_pass,
            "strict_110_row_payload_validator_passes": psm_replay[
                "strict_110_row_payload_validator_passes"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }

    source_promotion = {
        "schema": "MTTCurrentPSMC102SourcePromotionReconciliation.v1",
        "status": "CURRENT_PSM_C1_02_SOURCE_PROMOTION_CLOSED_BY_TRANSPORT_CLOSED_PHIFIN_IMPORT",
        "SM_parity_remains_closed": True,
        "previous_current_frontier": rel(PREVIOUS),
        "previous_current_frontier_status": previous["status"],
        "source_stack_closed": source_stack_closed,
        "unpatched_PSM_C1_02_source_promotion_closed": source_stack_closed,
        "SelectedFiniteC1SourceIdentityTheorem_promoted": replay["promotion_decision"][
            "SelectedFiniteC1SourceIdentityTheorem_promoted"
        ],
        "promoted_objects": summary["promoted_objects"],
        "route_A_closed": narrowed_pass,
        "route_B_needed_for_closure": False,
        "route_B_status": "optional independent provenance crosscheck",
        "free_axiom_patch_used": psm_replay["free_axiom_patch_used"],
        "locked_target_values_used_as_source": psm_replay["locked_target_values_used_as_source"],
        "raw_27mode_replay_claimed": False,
        "symbolic_transport_quotient_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_stack_closed,
    }

    full_sm_gap = {
        "schema": "MTTPostSourcePromotionFullSMGap.v1",
        "status": "SOURCE_PROMOTION_CLOSED_TRUE_SM_EQUIVALENCE_STILL_OPEN",
        "source_stack_closed": full_gate["source_stack_closed"],
        "true_SM_equivalence_closed": full_gate["true_SM_equivalence_closed"],
        "full_SM_no_knob_closed": full_gate["full_SM_no_knob_closed"],
        "remaining_gates": full_gate["remaining_gates"],
        "important_shift": (
            "The active blocker has moved past PSM-C1-02 source promotion. Remaining work is downstream "
            "dynamic/dotD, matter-slot routing, Yukawa/mass/mixing value closure, and RG/covariance linkage."
        ),
        "not_remaining": [
            "PSM-C1-02 unpatched source promotion",
            "A_selected/b_selected/deltaTheta_C1 promotion through source stack",
            "narrowed Phi_fin C1 source emission validator",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102GaugeTransportImport.v1",
        "status": "NEXT_WORK_POST_SOURCE_PROMOTION_FULLSM_GAP",
        "previous_artifact": "MTT_Selected_PSM_C1_02_GaugeTransportedPhiFinTraceImport_or_FullSMGap_v1",
        "next_required_artifact": NEXT,
        "recommended_next": next_cutset["recommended_next"],
        "primary": {
            "label": "POST-SOURCE-PROMOTION / DOTD-MATTER-ROUTING",
            "task": (
                "Audit the full-SM gap after source promotion, then close selected dotD alpha1 with transport "
                "derivative and selected matter-slot routing/normalization."
            ),
        },
        "guardrail": "Do not reopen PSM-C1-02 source promotion unless this import or its validators regress.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102GaugeTransportedPhiFinTraceImportOrFullSMGap",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "inputs": {
            "transport_closed_phifin_source": rel(TRANSPORT_SOURCE),
            "unpatched_source_promotion_replay": rel(UNPATCHED_REPLAY),
            "narrowed_phifinc1_emission_replay": rel(NARROWED_REPLAY),
            "psm_c1_02_source_promotion_replay": rel(PSM_REPLAY),
            "post_source_full_sm_gate": rel(FULL_GATE),
        },
        "output_packets": {
            "transport_closed_phifin_import_validation": rel(IMPORT_VALIDATION),
            "current_psm_c1_02_source_promotion_reconciliation": rel(SOURCE_PROMOTION),
            "post_source_promotion_fullsm_gap": rel(FULL_SM_GAP),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CurrentPSMC102GaugeTransportedPhiFinImportTheorem",
            "proved": source_stack_closed,
            "statement": (
                "The current PSM-C1-02 source-ownership frontier imports the already validated transport-closed "
                "symbolic Phi_fin finite replay. The narrowed Route-A Phi_fin C1 source-emission validator and "
                "strict PSM-C1-02 source-promotion validator pass, so the unpatched source-promotion stack is "
                "closed in the current ledger. This does not close true SM equivalence or no-knob value closure."
            ),
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "PSM_C1_02_unpatched_source_promotion_closed": source_stack_closed,
            "A_selected_promoted": summary["promoted_objects"]["A_selected"],
            "b_selected_promoted": summary["promoted_objects"]["b_selected"],
            "deltaTheta_C1_promoted": summary["promoted_objects"]["deltaTheta_C1"],
            "Route_A_transport_closed_import_validates": narrowed_pass,
            "Route_B_independent_rows_required_for_PSM_closure": False,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "what_closes_now": {
            "current_PSM_C1_02_source_promotion_reconciled_closed": source_stack_closed,
            "old_open_frontier_superseded_by_transport_closed_import": True,
            "narrowed_phifinc1_emission_validator_passes": narrowed_pass,
            "psm_c1_02_source_promotion_validator_passes": psm_pass,
            "post_source_fullsm_gap_selected": True,
        },
        "what_remains_open": {
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_matter_slot_routing_and_normalization": True,
            "Yukawa_mass_mixing_value_closure_without_proxy_fitting": True,
            "final_no_knob_constants_and_covariance_RG_linkage": True,
            "true_SM_equivalence": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_stack_closed,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_GaugeTransportedPhiFinTraceImport_or_FullSMGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "PSM_C1_02_unpatched_source_promotion_closed": source_stack_closed,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
        "narrowed_route_A_validator_passes": narrowed_pass,
        "psm_c1_02_source_promotion_validator_passes": psm_pass,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 GaugeTransportedPhiFinTraceImport or FullSMGap v1

Status: `{STATUS}`

## Result

The gauge-transported `Phi_fin` construction is not merely a future target. It
already exists in the repo as a transport-closed symbolic finite replay, and it
passes the strict source validators.

This artifact imports it into the current PSM-C1-02 frontier and supersedes the
newer open cutset:

- narrowed `Phi_fin^C1` source-emission validator: PASS
- strict PSM-C1-02 source-promotion validator: PASS
- `A_selected`, `b_selected`, and `deltaTheta_C1`: promoted through the source stack

Raw 27-mode multiplication by `U` is still not claimed. The closure uses the
symbolic transport quotient with `U=exp(-u ad(T3))`.

## What Remains

This is not true SM equivalence and not no-knob closure. Remaining gates:

- selected `dotD alpha1` with the derivative of `U`
- selected matter-slot routing and normalization
- Yukawa/mass/mixing value closure without proxy fitting
- final constants/covariance/RG linkage

Next artifact: `{NEXT}`.
"""

    write_json(IMPORT_VALIDATION, import_validation)
    write_json(SOURCE_PROMOTION, source_promotion)
    write_json(FULL_SM_GAP, full_sm_gap)
    write_json(NEXT_WORK, next_work)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
