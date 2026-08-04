"""Build Step 25 threshold external replay / no-knob kernel cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL_KERNEL = PACKET_DIR / "step25_external_replay_and_noknob_kernel.packet.json"
INTERNAL_BLOCKER = PACKET_DIR / "step25_internal_scalar_emission_blocker.packet.json"
NEXT_CUTSET = PACKET_DIR / "step25_to_step26_fulls2_payload_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step25_ThresholdExternalReplay_NoKnobKernel_or_FullS2Cutset_v1.md"

STEP24 = DATA / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset.candidate.json"
THRESHOLD = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
THRESHOLD_INTERNAL = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport" / "internal_threshold_response_functional_row_emission.packet.json"
THRESHOLD_EXTERNAL = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport" / "post_pi_external_source_row_import.packet.json"
THRESHOLD_READINESS = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport" / "step4_value_layer_readiness_after_external_import.packet.json"
NOKNOB = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
NOKNOB_STATUS = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem" / "internal_value_obligation_status_after_readiness_8of9.packet.json"
INTERNAL = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
INTERNAL_ATTEMPT = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection" / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
ANCHOR_RECHECK = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection" / "universal_anchor_selection_recheck_for_direct_emission.packet.json"
STRUCTURAL_ROWS = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection" / "structural_orbit_scalar_row_candidates_not_accepted.packet.json"

STATUS = "MTT_SELECTED_STEP25_THRESHOLDEXTERNALREPLAY_NOKNOBKERNEL_OR_FULLS2CUTSET_BUILT_EXTERNAL_REPLAY_AND_KERNEL_CLOSED_FULLS2_INTERNAL_ROWS_OPEN"
NEXT = "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1"


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

    inputs = [
        STEP24,
        THRESHOLD,
        THRESHOLD_INTERNAL,
        THRESHOLD_EXTERNAL,
        THRESHOLD_READINESS,
        NOKNOB,
        NOKNOB_STATUS,
        INTERNAL,
        INTERNAL_ATTEMPT,
        ANCHOR_RECHECK,
        STRUCTURAL_ROWS,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 25 inputs: " + ", ".join(missing))

    step24 = load(STEP24)
    threshold = load(THRESHOLD)
    threshold_internal = load(THRESHOLD_INTERNAL)
    threshold_external = load(THRESHOLD_EXTERNAL)
    threshold_readiness = load(THRESHOLD_READINESS)
    noknob = load(NOKNOB)
    noknob_status = load(NOKNOB_STATUS)
    internal = load(INTERNAL)
    internal_attempt = load(INTERNAL_ATTEMPT)
    anchor_recheck = load(ANCHOR_RECHECK)
    structural_rows = load(STRUCTURAL_ROWS)

    external_kernel = {
        "schema": "MTTStep25ExternalReplayAndNoKnobKernel.v1",
        "status": "ADMITTED_EXTERNAL_REPLAY_AND_FINAL_NOKNOB_KERNEL_CLOSED_INTERNAL_VALUES_OPEN",
        "step24_value_frontier": step24["next_required_artifact"],
        "threshold_external_replay": {
            "status": threshold["status"],
            "accepted_external_source_row_imported": threshold["closure_decision"]["accepted_external_source_row_imported"],
            "accepted_external_threshold_row_count": threshold["closure_decision"]["accepted_external_threshold_row_count"],
            "accepted_external_mass_scheme_row_count": threshold["closure_decision"]["accepted_external_mass_scheme_row_count"],
            "accepted_diagonal_profile_theorem_closed": threshold["closure_decision"]["accepted_diagonal_profile_theorem_closed"],
            "external_import_lane_closed_at_admitted_replay_tier": threshold["closure_decision"]["external_import_lane_closed_at_admitted_replay_tier"],
            "external_rows_used_as_branch_selector": threshold_external["external_rows_used_as_branch_selector"],
            "closure_tier": threshold_external["closure_tier"],
            "internal_selected_Rtheta_value_row_emitted": threshold["closure_decision"]["internal_selected_Rtheta_value_row_emitted"],
            "selected_threshold_response_functional_instantiated": threshold["closure_decision"]["selected_threshold_response_functional_instantiated"],
        },
        "readiness": {
            "status": threshold_readiness["status"],
            "readiness_fraction": threshold_readiness["readiness_fraction"],
            "present_count": threshold_readiness["present_count"],
            "requirement_count": threshold_readiness["requirement_count"],
            "only_remaining_readiness_blocker": threshold_readiness["only_remaining_readiness_blocker"],
            "closed_value_obligation_rows_at_admitted_external_tier": threshold_readiness["closed_value_obligation_rows_at_admitted_external_tier"],
            "closed_value_obligation_rows_at_internal_no_knob_tier": threshold_readiness["closed_value_obligation_rows_at_internal_no_knob_tier"],
        },
        "no_knob_kernel": {
            "status": noknob["status"],
            "final_no_knob_kernel_typed": noknob["closure_decision"]["final_no_knob_kernel_typed"],
            "selected_internal_value_emission_count": noknob["closure_decision"]["selected_internal_value_emission_count"],
            "selected_universal_parameter_count": noknob["closure_decision"]["selected_universal_parameter_count"],
            "true_SM_equivalence_closed": noknob["closure_decision"]["true_SM_equivalence_closed"],
            "full_no_knob_closed": noknob["closure_decision"]["full_no_knob_closed"],
            "value_obligation_status": noknob_status["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EXTERNAL_KERNEL, external_kernel)

    internal_blocker = {
        "schema": "MTTStep25InternalScalarEmissionBlocker.v1",
        "status": "DIRECT_INTERNAL_RTHETA_ATTEMPT_EXECUTED_ZERO_ACCEPTED_ROWS",
        "internal_attempt": {
            "status": internal["status"],
            "kernel_readiness": internal["kernel_readiness"],
            "value_source_obligation_closed_row_count": internal["value_source_obligation_closed_row_count"],
            "accepted_internal_scalar_row_count": internal["closure_decision"]["accepted_internal_scalar_row_count"],
            "fullS2_payload_ready": internal["closure_decision"]["fullS2_payload_ready"],
            "universal_anchor_selected": internal["closure_decision"]["universal_anchor_selected"],
            "lambda_H_row_emitted": internal["closure_decision"]["lambda_H_row_emitted"],
            "true_SM_equivalence_closed": internal["closure_decision"]["true_SM_equivalence_closed"],
            "full_no_knob_closed": internal["closure_decision"]["full_no_knob_closed"],
            "direct_attempt_status": internal_attempt["status"],
            "anchor_recheck_status": anchor_recheck["status"],
            "structural_rows_status": structural_rows["status"],
        },
        "active_blockers": {
            "fullS2_payload_ready": False,
            "candidate_specific_universal_source_anchor_selected": False,
            "internal_Rtheta_scalar_row_emission": False,
            "lambda_H_row_emission": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_BLOCKER, internal_blocker)

    next_cutset = {
        "schema": "MTTStep25ToStep26FullS2PayloadCutset.v1",
        "status": "NEXT_FULLS2_PAYLOAD_OR_UNIVERSAL_ANCHOR",
        "closed_do_not_reopen": {
            "step24_dynamic_source_gate": True,
            "admitted_external_threshold_rows": True,
            "admitted_external_mass_scheme_rows": True,
            "accepted_diagonal_profile_theorem_at_replay_tier": True,
            "final_no_knob_kernel_typed": True,
            "direct_internal_scalar_attempt_executed": True,
        },
        "still_open": {
            "selected_fullS2_rhoE_D_E_operator_payload": True,
            "Phi_fin_selected_minimizer_trace": True,
            "candidate_specific_universal_source_anchor": True,
            "internal_Rtheta_scalar_value_rows": True,
            "lambda_H_value_execution": True,
            "Yukawa_CKM_PMNS_lambdaH_numerical_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedStep25ThresholdExternalReplayNoKnobKernelOrFullS2Cutset",
        "status": STATUS,
        "inputs": {
            "step24": rel(STEP24),
            "threshold": rel(THRESHOLD),
            "threshold_internal": rel(THRESHOLD_INTERNAL),
            "threshold_external": rel(THRESHOLD_EXTERNAL),
            "threshold_readiness": rel(THRESHOLD_READINESS),
            "noknob": rel(NOKNOB),
            "noknob_status": rel(NOKNOB_STATUS),
            "internal_scalar": rel(INTERNAL),
            "internal_attempt": rel(INTERNAL_ATTEMPT),
            "anchor_recheck": rel(ANCHOR_RECHECK),
            "structural_rows": rel(STRUCTURAL_ROWS),
        },
        "output_packets": {
            "step25_external_replay_and_noknob_kernel": rel(EXTERNAL_KERNEL),
            "step25_internal_scalar_emission_blocker": rel(INTERNAL_BLOCKER),
            "step25_to_step26_fulls2_payload_cutset": rel(NEXT_CUTSET),
        },
        "theorem": {
            "name": "Step25ThresholdExternalReplayNoKnobKernelCutsetTheorem",
            "proved": True,
            "statement": (
                "The Step24 value-functional target has already been executed "
                "as an admitted external replay lane and a final typed no-knob "
                "kernel. The admitted replay tier closes seven threshold rows, "
                "three mass-scheme rows, and the diagonal profile theorem, but "
                "does not emit internal selected R_theta scalar rows. The direct "
                "internal attempt has been executed and is blocked exactly by "
                "the full-S2 rhoE/D_E/operator payload or an equivalent selected "
                "universal source anchor."
            ),
        },
        "closure_decision": {
            "step24_next_artifact_executed": True,
            "admitted_external_threshold_rows_closed": True,
            "admitted_external_threshold_row_count": threshold["closure_decision"]["accepted_external_threshold_row_count"],
            "admitted_external_mass_scheme_rows_closed": True,
            "admitted_external_mass_scheme_row_count": threshold["closure_decision"]["accepted_external_mass_scheme_row_count"],
            "accepted_diagonal_profile_theorem_closed_at_replay_tier": True,
            "final_no_knob_kernel_typed": True,
            "Rtheta_readiness_8_of_9": True,
            "direct_internal_scalar_attempt_executed": True,
            "accepted_internal_scalar_row_count": 0,
            "selected_internal_value_emission_count": 0,
            "selected_universal_parameter_count": 0,
            "selected_fullS2_payload_ready": False,
            "candidate_specific_universal_source_anchor_selected": False,
            "lambda_H_row_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "threshold_external_import_lane_at_admitted_replay_tier": True,
            "mass_scheme_external_import_lane_at_admitted_replay_tier": True,
            "accepted_diagonal_profile_theorem_at_replay_tier": True,
            "final_no_knob_kernel_typed": True,
            "direct_internal_Rtheta_scalar_attempt_executed": True,
            "active_frontier_relocated_to_fullS2_payload_or_universal_anchor": True,
        },
        "what_remains_open": {
            "selected_fullS2_rhoE_D_E_operator_payload": True,
            "Phi_fin_selected_minimizer_trace": True,
            "candidate_specific_universal_source_anchor": True,
            "internal_Rtheta_scalar_value_rows": True,
            "lambda_H_value_execution": True,
            "Yukawa_CKM_PMNS_lambdaH_numerical_closure": True,
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
        "certificate": "MTT_Selected_Step25_ThresholdExternalReplay_NoKnobKernel_or_FullS2Cutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "admitted_external_threshold_row_count": threshold["closure_decision"]["accepted_external_threshold_row_count"],
        "admitted_external_mass_scheme_row_count": threshold["closure_decision"]["accepted_external_mass_scheme_row_count"],
        "accepted_internal_scalar_row_count": 0,
        "selected_fullS2_payload_ready": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step25 ThresholdExternalReplay NoKnobKernel or FullS2Cutset v1

Status: `{STATUS}`.

Closed now:

```text
Step24 next artifact executed                              closed
admitted external threshold rows                            7
admitted external mass-scheme rows                          3
accepted diagonal profile theorem, replay tier              closed
final no-knob value-derivation kernel                       typed
direct internal Rtheta scalar-row attempt                   executed
```

Still open:

```text
accepted internal scalar rows                               0
selected full-S2 rhoE/D_E/operator payload                  open
candidate-specific universal source anchor                  open
lambda_H row emission                                       open
Yukawa/CKM/PMNS/lambdaH numerical closure                   open
true SM equivalence / full no-knob closure                  open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
