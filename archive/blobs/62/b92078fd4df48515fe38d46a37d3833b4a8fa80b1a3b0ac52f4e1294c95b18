"""Build dynamic C1 patch to SM-parity ledger / unpatched measure derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEDGER = PACKET_DIR / "dynamic_c1_sm_parity_status_update.packet.json"
UPGRADE = PACKET_DIR / "no_knob_upgrade_boundary_after_patch.packet.json"
NEXTSTEPS = PACKET_DIR / "post_patch_sm_parity_next_steps.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1PatchToSMParityLedger_or_UnpatchedMeasureDerivation_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1PATCHTOSMPARITYLEDGER_OR_UNPATCHEDMEASUREDERIVATION_BUILT_PATCHED_LEDGER_UPDATED"
NEXT = "MTT_Selected_PatchedDynamicC1EmpiricalReplayIntegration_or_NoKnobDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    patch_gate = load(DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json")
    replay = load(
        DATA
        / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
        / "patched_routeb_dynamic_c1_closure_replay.packet.json"
    )
    guardrail = load(
        DATA
        / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
        / "unpatched_derivation_guardrail.packet.json"
    )
    admission = load(DATA / "sm_equivalence_measured_replay_admission.candidate.json")
    sm_ledger = load(DATA / "sm_parity_closure_ledger.candidate.json")

    ledger = {
        "schema": "MTTDynamicC1SMParityStatusUpdate.v1",
        "status": "PATCHED_DYNAMIC_C1_STATUS_IMPORTED_TO_SM_PARITY_LEDGER",
        "before_patch_status": {
            "dynamic_overlap_role": admission["dynamic_upgrade_boundary"]["parity_role"],
            "A_selected_claimed": admission["dynamic_upgrade_boundary"]["A_selected_claimed"],
            "b_selected_claimed": admission["dynamic_upgrade_boundary"]["b_selected_claimed"],
            "selected_C1_primitive_emitted": admission["dynamic_upgrade_boundary"][
                "selected_C1_primitive_emitted"
            ],
        },
        "after_patch_status": {
            "patched_dynamic_C1_packet_closed": replay["promoted_under_patched_spine"][
                "patched_dynamic_C1_packet_closed"
            ],
            "patched_A_selected": replay["promoted_under_patched_spine"][
                "physical_A_selected"
            ],
            "patched_b_selected": replay["promoted_under_patched_spine"][
                "physical_b_selected"
            ],
            "patched_deltaTheta_C1": replay["promoted_under_patched_spine"][
                "physical_deltaTheta_C1"
            ],
            "patched_sector_response_matrices": replay["promoted_under_patched_spine"][
                "physical_sector_response_matrices"
            ],
            "patch_used": replay["patch_used"],
        },
        "ledger_interpretation": (
            "For SM-parity, the dynamic C1 packet is now closed in the local patched proof spine. "
            "For no-knob closure, the same object remains open until the finite C1 trace-measure "
            "principle is derived or Route A emits the same-source physical source packet."
        ),
        "full_SM_parity_ledger_closed_now": False,
        "true_SM_equivalence_closed_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    upgrade = {
        "schema": "MTTNoKnobUpgradeBoundaryAfterPatch.v1",
        "status": "PATCHED_PARITY_CLOSED_NO_KNOB_DERIVATION_OPEN",
        "patched_spine_closures": {
            "dynamic_C1_packet": True,
            "Route_B_physical_Galerkin_replacement": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
        },
        "no_knob_upgrade_targets_remaining": guardrail["unpatched_open_items"],
        "credibility_policy": guardrail["credibility_policy"],
        "measured_replay_policy_unchanged": {
            "measured_values_do_not_select_packet": admission["static_source_boundary"][
                "measured_values_do_not_select_packet"
            ],
            "observed_data_used_as_selector": admission[
                "observed_data_used_as_selector"
            ],
            "target_fitting_used": admission["target_fitting_used"],
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    nextsteps = {
        "schema": "MTTPostPatchSMParityNextSteps.v1",
        "status": "NEXT_STEPS_REDUCED_AFTER_PATCHED_DYNAMIC_C1_CLOSURE",
        "patched_dynamic_C1_no_longer_blocks": [
            "SM-parity measured replay admission",
            "patched A_selected/b_selected interface",
            "patched dynamic C1 sector response interface",
        ],
        "remaining_for_full_SM_parity_or_true_equivalence": {
            "final_integrated_empirical_replay_audit": True,
            "common_RG_and_covariance_completion": True,
            "selected_SM_packet_certificate_integration": True,
            "local_QFT_functor_or_observable_suite": True,
            "GR_QM_measurement_interfaces": True,
            "unpatched_no_knob_derivation_optional_for_SM_parity_but_required_for_no_knob": True,
        },
        "recommended_next_artifact": NEXT,
        "current_global_ledger_status": sm_ledger["status"],
        "full_sm_parity_closed_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1PatchToSMParityLedgerOrUnpatchedMeasureDerivation",
        "status": STATUS,
        "inputs": {
            "patched_dynamic_c1_gate": rel(
                DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json"
            ),
            "patched_routeb_replay": rel(
                DATA
                / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
                / "patched_routeb_dynamic_c1_closure_replay.packet.json"
            ),
            "sm_equivalence_measured_replay_admission": rel(
                DATA / "sm_equivalence_measured_replay_admission.candidate.json"
            ),
            "sm_parity_closure_ledger": rel(
                DATA / "sm_parity_closure_ledger.candidate.json"
            ),
        },
        "output_packets": {
            "dynamic_c1_sm_parity_status_update": rel(LEDGER),
            "no_knob_upgrade_boundary_after_patch": rel(UPGRADE),
            "post_patch_sm_parity_next_steps": rel(NEXTSTEPS),
        },
        "theorem": {
            "name": "PatchedDynamicC1SMParityLedgerUpdateTheorem",
            "proved": True,
            "statement": (
                "The explicit finite C1 trace-measure principle patch closes the dynamic C1 packet "
                "for the local patched SM-parity spine and updates the no-knob boundary: dynamic C1 "
                "is no longer a patched parity blocker, but the unpatched derivation remains a no-knob target."
            ),
        },
        "what_closes_now": {
            "patched_dynamic_C1_status_imported_to_SM_parity_ledger": True,
            "patched_A_b_deltaTheta_sector_response_interface_available": True,
            "no_knob_boundary_after_patch_declared": True,
            "post_patch_next_steps_reduced": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "full_SM_parity_ledger_integration": True,
            "final_integrated_empirical_replay_audit": True,
            "common_RG_and_covariance_completion": True,
            "selected_SM_packet_certificate_integration": True,
            "local_QFT_functor_or_observable_suite": True,
            "GR_QM_measurement_interfaces": True,
            "unpatched_no_knob_measure_derivation": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "patched_dynamic_C1_no_longer_blocks_SM_parity": True,
            "full_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "unpatched_no_knob_dynamic_C1_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_claimed": patch_gate["patched_spine_closure_claimed"],
        "previous_status": patch_gate["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1PatchToSMParityLedger_or_UnpatchedMeasureDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_claimed": candidate["patched_spine_closure_claimed"],
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1PatchToSMParityLedger or UnpatchedMeasureDerivation v1

Status: `{STATUS}`.

The patched dynamic C1 closure is now imported into the SM-parity ledger layer:

```text
patched dynamic C1 no longer blocks parity = True
patched A_selected                         = {replay["promoted_under_patched_spine"]["physical_A_selected"]}
patched b_selected                         = {replay["promoted_under_patched_spine"]["physical_b_selected"]}
patched deltaTheta_C1                      = {replay["promoted_under_patched_spine"]["physical_deltaTheta_C1"]}
full SM parity closed now                  = False
unpatched no-knob dynamic C1 closed        = False
```

This is a meaningful SM-parity checkpoint, not a no-knob claim. The next step is
to integrate this with the final empirical/replay ledger and keep the unpatched
measure derivation as a separate upgrade target.

Next artifact: `{NEXT}`.
"""

    LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    UPGRADE.write_text(json.dumps(upgrade, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXTSTEPS.write_text(json.dumps(nextsteps, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
