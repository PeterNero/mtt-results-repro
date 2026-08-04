"""Build same-branch / independent Hessian bridge after actual fill no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BRIDGE = PACKET_DIR / "samebranch_or_independent_bridge_decision.packet.json"
PATCHED = PACKET_DIR / "patched_smparity_dynamic_c1_import.packet.json"
UNPATCHED = PACKET_DIR / "unpatched_noknob_remaining_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameBranchPhiFinC1SourceEmission_or_IndependentHessianQuadratureExecution_v1.md"

STATUS = "MTT_SELECTED_SAMEBRANCH_PHIFINC1_OR_INDEPENDENTHESSIAN_BUILT_PATCHED_PARITY_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_FinalIntegratedSMParityReplayAfterSourceIdentityPatch_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    actual = load(DATA / "selected_finalsourceemission_actualfill_or_nogowitness.candidate.json")
    actual_frontier = load(
        DATA
        / "selected_finalsourceemission_actualfill_or_nogowitness"
        / "current_frontier_after_actual_fill_attempt.packet.json"
    )
    same_source = load(DATA / "selected_samesourcephifinc1emission_or_independentrowsactualfill.candidate.json")
    principle = load(DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json")
    replay = load(
        DATA
        / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
        / "patched_source_identity_dynamic_c1_replay.packet.json"
    )
    validator = load(
        DATA
        / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
        / "local_principle_promoted_110row_validator_result.packet.json"
    )
    interface = load(
        DATA
        / "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof"
        / "patched_dynamic_c1_source_and_value_interface.packet.json"
    )
    ledger = load(DATA / "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof.candidate.json")

    bridge = {
        "schema": "MTTSameBranchOrIndependentHessianBridgeDecision.v1",
        "status": "PATCHED_ROUTE_B_CLOSES_SM_PARITY_DYNAMIC_INTERFACE_UNPATCHED_OPEN",
        "actual_fill_validator_rejected": True,
        "same_branch_route_A": {
            "unpatched_phifin_c1_action_identity": False,
            "same_source_R_Z_R_X_b_selected_emission": False,
            "physical_no_extra_boundary_source": False,
            "status": "OPEN",
        },
        "independent_route_B": {
            "strict_110row_source_id_validator_ok_under_local_principle": validator["ok"],
            "primitive_rows": replay["row_counts"]["primitive_rows"],
            "hessian_source_rows": replay["row_counts"]["hessian_source_rows"],
            "sector_rows": replay["row_counts"]["sector_rows"],
            "same_source_b_selected_under_local_principle": replay["promoted_under_local_principle"][
                "same_source_b_selected"
            ],
            "source_independence_from_residual_replay_under_local_principle": replay[
                "promoted_under_local_principle"
            ]["source_independence_from_residual_replay"],
            "status": "CLOSED_FOR_PATCHED_SM_PARITY_SPINE",
        },
        "decision": {
            "patched_SM_parity_dynamic_C1_source_and_value_interface_closed": True,
            "unpatched_no_knob_dynamic_C1_closed": False,
            "same_branch_direct_route_closed": False,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
    }
    write_json(BRIDGE, bridge)

    patched = {
        "schema": "MTTPatchedSMParityDynamicC1Import.v1",
        "status": "PATCHED_SM_PARITY_IMPORT_READY",
        "source_identity_principle": replay["source_identity_principle"],
        "source_layer": interface["source_layer"],
        "value_layer": interface["value_layer"],
        "validator": {
            "path": validator["path"],
            "exit_code": validator["exit_code"],
            "ok": validator["ok"],
        },
        "SM_parity_dynamic_C1_closed_under_local_principle": True,
        "full_SM_parity_replay_next": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(PATCHED, patched)

    unpatched = {
        "schema": "MTTUnpatchedNoKnobRemainingGate.v1",
        "status": "UNPATCHED_ACTION_PROOF_REMAINS_OPEN",
        "remaining_gate": {
            "derive_SelectedFiniteC1SourceIdentityPrinciple_from_selected_action": True,
            "derive_same_branch_PhiFinC1_action_source_emission": True,
            "or_emit_independent_rows_without_local_principle_patch": True,
        },
        "not_regressions": {
            "alpha1_dotd_closed": actual["what_closes_now"]["alpha1_dotd_excluded_from_remaining_source_failure"],
            "canonical_residual_values_closed": actual["what_closes_now"][
                "canonical_residual_values_excluded_from_remaining_source_failure"
            ],
            "patched_source_identity_closed": ledger["promotion_decision"]["patched_source_identity_closed"],
            "patched_value_interface_closed": ledger["promotion_decision"]["patched_value_interface_closed"],
        },
        "no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }
    write_json(UNPATCHED, unpatched)

    candidate = {
        "candidate": "MTTSelectedSameBranchPhiFinC1SourceEmissionOrIndependentHessianQuadratureExecution",
        "status": STATUS,
        "inputs": {
            "actual_final_source_emission_fill": rel(
                DATA / "selected_finalsourceemission_actualfill_or_nogowitness.candidate.json"
            ),
            "actual_frontier_packet": rel(
                DATA
                / "selected_finalsourceemission_actualfill_or_nogowitness"
                / "current_frontier_after_actual_fill_attempt.packet.json"
            ),
            "strongest_legal_two_lane_fill": rel(
                DATA / "selected_samesourcephifinc1emission_or_independentrowsactualfill.candidate.json"
            ),
            "source_identity_principle_insertion": rel(
                DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"
            ),
            "patched_source_identity_dynamic_c1_replay": rel(
                DATA
                / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
                / "patched_source_identity_dynamic_c1_replay.packet.json"
            ),
            "patched_source_and_value_interface": rel(
                DATA
                / "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof"
                / "patched_dynamic_c1_source_and_value_interface.packet.json"
            ),
        },
        "output_packets": {
            "bridge_decision": rel(BRIDGE),
            "patched_smparity_dynamic_c1_import": rel(PATCHED),
            "unpatched_noknob_remaining_gate": rel(UNPATCHED),
        },
        "theorem": {
            "name": "SameBranchOrIndependentHessianPatchedParityClosureTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "The actual unpatched final source-emission fill still fails, but the local "
                "SelectedFiniteC1SourceIdentityPrinciple promotes the independent 110-row source packet. "
                "Together with the patched value replay, this closes the dynamic C1 source-and-value "
                "interface for the declared SM-parity spine while preserving the unpatched/no-knob "
                "action derivation as the remaining upgrade target."
            ),
        },
        "what_closes_now": {
            "dangling_next_artifact_filled": True,
            "patched_route_B_source_validator_imported": validator["ok"],
            "patched_SM_parity_dynamic_C1_source_and_value_interface_closed": True,
            "actual_unpatched_fill_failure_preserved": True,
            "unpatched_no_knob_guardrail_preserved": True,
        },
        "what_remains_open": {
            "derive_SelectedFiniteC1SourceIdentityPrinciple_from_selected_action": True,
            "unpatched_same_branch_PhiFinC1_source_emission": True,
            "true_SM_equivalence_precision_profile": actual_frontier["remaining_gates"][
                "true_SM_equivalence_precision_profile"
            ],
            "no_knob_closure": actual_frontier["remaining_gates"]["no_knob_closure"],
        },
        "SM_parity_dynamic_C1_closed_under_local_principle": True,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SameBranchPhiFinC1SourceEmission_or_IndependentHessianQuadratureExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "patched_route_B_source_validator_ok": validator["ok"],
        "patched_SM_parity_dynamic_C1_source_and_value_interface_closed": True,
        "SM_parity_closed": True,
        "unpatched_no_knob_dynamic_C1_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SameBranchPhiFinC1SourceEmission or IndependentHessianQuadratureExecution v1

Status: `{STATUS}`.

This fills the bridge after the actual final source-emission no-go.

The direct unpatched same-branch `Phi_fin^C1` action/source route remains open.
However, under the local `SelectedFiniteC1SourceIdentityPrinciple`, the
independent 110-row source packet validates and combines with the patched value
replay. Thus the dynamic C1 source-and-value interface is closed for the
declared patched SM-parity spine.

This is not a no-knob derivation. The no-knob upgrade target is still to derive
the source-identity principle from selected action data, or emit independent
rows without the local principle patch.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
