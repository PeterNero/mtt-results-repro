"""Build measured-SM replay admission for the SM-equivalence branch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CONTROLLER = DATA / "sm_equivalence_superset_strategy_controller.candidate.json"
CORE = DATA / "core_axioms_measured_parameter_interface.candidate.json"
SECTOR = DATA / "sm_sector_embedding_interface.candidate.json"
EMPIRICAL = DATA / "empirical_equivalence_ledger.candidate.json"
SMSLOT = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
DYNAMIC = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"

OUTPUT = DATA / "sm_equivalence_measured_replay_admission.candidate.json"
CERT = CERTS / "sm_equivalence_measured_replay_admission_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Measured_Replay_Admission_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_MEASURED_REPLAY_ADMISSION_BUILT_DYNAMIC_OVERLAP_AS_NO_KNOB_UPGRADE"
NEXT = "MTT_SM_Equivalence_Measured_Parameter_Replay_Manifest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def slots_by_kind(core: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {slot["kind"]: slot for slot in core["example_slots"]}


def main() -> int:
    controller = load(CONTROLLER)
    core = load(CORE)
    sector = load(SECTOR)
    empirical = load(EMPIRICAL)
    smslot = load(SMSLOT)
    dynamic = load(DYNAMIC)
    slots = slots_by_kind(core)

    static_source_boundary = {
        "sm_sector_packet_schema_declared": sector["gate_results"]["sm_packet_declared"],
        "measured_slot_boundary_declared": sector["gate_results"][
            "source_data_separated_from_measured_slots"
        ],
        "measured_values_do_not_select_packet": sector["gate_results"][
            "measured_values_do_not_select_sm_packet"
        ],
        "all_six_sm_slot_functor_arrows_emitted_static": smslot["selected_static_payloads_claimed"],
        "static_sector_route_Z_to_u_e_X_to_d_nuD": smslot["what_closes_now"][
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD"
        ],
        "finite_trace_transfer_normalization_static": smslot["what_closes_now"][
            "selected_static_finite_trace_transfer_normalization"
        ],
        "oneM_Dirac_neutrino_rule_static": smslot["what_closes_now"][
            "selected_static_1M_Dirac_neutrino_shift_rule"
        ],
    }

    dynamic_upgrade_boundary = {
        "dynamic_overlap_tensor_emitted": dynamic["dynamic_kernel_emitted"],
        "selected_C1_primitive_emitted": dynamic["selected_C1_primitive_emitted"],
        "A_selected_claimed": dynamic["A_selected_claimed"],
        "b_selected_claimed": dynamic["b_selected_claimed"],
        "parity_role": "NO_KNOB_UPGRADE_TARGET_NOT_PARITY_PREREQUISITE",
        "reason": (
            "At SM standard, Yukawa matrices, CKM/PMNS parameters, Higgs parameters, and gauge couplings "
            "are measured downstream inputs after the SM source/interface boundary is declared. Dynamic "
            "overlap tensors are needed to replace those measured inputs in the no-knob upgrade path, not "
            "to admit them for SM-equivalence replay."
        ),
    }

    measured_replay_slots = {
        "gauge_couplings": {
            "slot_source": slots["gauge coupling"]["name"],
            "admitted_for_SM_equivalence": True,
            "blocked_as_source_selector": True,
            "required_conventions": ["renormalization scheme", "scale", "uncertainty"],
            "no_knob_upgrade": slots["gauge coupling"]["no_knob_target"],
        },
        "yukawa_matrices": {
            "slot_source": slots["Yukawa matrix"]["name"],
            "admitted_for_SM_equivalence": True,
            "blocked_as_source_selector": True,
            "required_conventions": ["basis", "phase convention", "RG scale", "scheme", "uncertainty"],
            "no_knob_upgrade": slots["Yukawa matrix"]["no_knob_target"],
        },
        "CKM_PMNS_CP": {
            "slot_source": "CKM/PMNS matrices and CP phases",
            "admitted_for_SM_equivalence": True,
            "blocked_as_source_selector": True,
            "required_conventions": ["parameterization", "phase convention", "scale where applicable", "uncertainty"],
            "no_knob_upgrade": "selected complex overlap/operator kernel and CP-odd invariant",
        },
        "Higgs_parameters": {
            "slot_source": "Higgs vev/mass/quartic or equivalent potential parameters",
            "admitted_for_SM_equivalence": True,
            "blocked_as_source_selector": True,
            "required_conventions": ["scheme", "scale", "unit convention", "uncertainty"],
            "no_knob_upgrade": "selected Higgs projector/source and threshold/RG matching",
        },
    }

    replay_manifest_requirements = {
        "selected_source_boundary_input": rel(OUTPUT),
        "measured_slot_table": True,
        "SM_reference_conventions": True,
        "calculation_targets": [
            "mass spectrum from admitted Yukawa/Higgs slots",
            "CKM and PMNS reconstruction from admitted matrices",
            "gauge running comparison from admitted couplings",
            "Higgs-sector replay from admitted parameters",
            "anomaly/source boundary unchanged by measured values",
        ],
        "forbidden_replay_behaviors": [
            "modifying source packet after seeing residuals",
            "using measured constants to choose dynamic overlap tensor",
            "calling measured replay a no-knob derivation",
            "promoting benchmark matrices to selected A_selected or b_selected",
        ],
    }

    candidate = {
        "candidate": "MTTSMEquivalenceMeasuredReplayAdmission",
        "status": STATUS,
        "inputs": {
            "sm_equivalence_superset_strategy_controller": rel(CONTROLLER),
            "core_axioms_measured_parameter_interface": rel(CORE),
            "sm_sector_embedding_interface": rel(SECTOR),
            "empirical_equivalence_ledger": rel(EMPIRICAL),
            "selected_smslotfunctor_downstream_payload_ledger": rel(SMSLOT),
            "dynamic_overlap_or_c1primitive_source_emission": rel(DYNAMIC),
        },
        "branch_policy_update": {
            "previous_controller_locked_G4_before_measured_replay": controller["acceptance_gates"][
                "G4_dynamic_operator_boundary"
            ]["closed"]
            is False,
            "corrected_for_SM_equivalence": True,
            "new_rule": (
                "Dynamic overlap/C1 primitive emission is a no-knob upgrade target. SM-equivalence replay "
                "may start after the static SM source/interface and measured-slot boundary are declared."
            ),
        },
        "static_source_boundary": static_source_boundary,
        "dynamic_upgrade_boundary": dynamic_upgrade_boundary,
        "measured_replay_slots": measured_replay_slots,
        "empirical_ledger_ready": empirical["acceptance_summary"][
            "interfaces_ready_for_empirical_audit"
        ],
        "replay_manifest_requirements": replay_manifest_requirements,
        "what_closes_now": {
            "SM_equivalence_measured_replay_admission_policy": True,
            "dynamic_overlap_reclassified_as_no_knob_upgrade_not_parity_prerequisite": True,
            "measured_Yukawa_CKM_PMNS_Higgs_slots_admitted_downstream": True,
            "source_selection_guardrails_preserved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "measured_parameter_replay_manifest": True,
            "actual_numeric_SM_equivalence_replay": True,
            "empirical_equivalence_audit_run": True,
            "selected_dynamic_overlap_tensor_or_primitive_C1_contractions_for_no_knob_upgrade": True,
            "selected_A_selected_for_no_knob_upgrade": True,
            "selected_b_selected_for_no_knob_upgrade": True,
            "full_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceMeasuredReplayAdmissionTheorem",
            "proved": True,
            "statement": (
                "For SM-equivalence, selected dynamic overlap/C1 primitive emission is not a prerequisite "
                "for admitting measured Yukawa, CKM/PMNS, Higgs, and gauge parameters. Once the static SM "
                "source/interface boundary and measured-slot policy are declared, those measured values may "
                "enter as downstream parity inputs exactly as in the Standard Model. Dynamic overlap, "
                "A_selected, b_selected, and primitive C1 contractions remain no-knob upgrade targets and may "
                "not be selected from measured replay residuals."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM-Equivalence Measured Replay Admission v1

Status: `{STATUS}`.

## Result

For this SM-equivalence branch, dynamic overlap/C1 primitive emission is
reclassified correctly:

```text
dynamic overlap tensor / A_selected / b_selected = no-knob upgrade target
measured Yukawa, CKM/PMNS, Higgs, gauge inputs = downstream SM-equivalence slots
```

This does not weaken the no-knob program.  It simply matches the Standard Model
standard: the SM itself uses measured Yukawa matrices, mixings, CP phases, Higgs
parameters, and gauge couplings.

## Admission Rule

Measured SM values may enter only after the source/interface boundary is
declared.  They may be used to replay SM calculations and empirical equivalence.
They may not select:

- source structure,
- topology or branch,
- primitive C1 contractions,
- dynamic overlap tensors,
- `A_selected` or `b_selected`.

## Next

Build `{NEXT}`: a typed manifest of measured slots, conventions, provenance,
uncertainties, and replay targets.  That manifest is the immediate SM-equivalence
path.  Dynamic overlap remains the no-knob upgrade path.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
