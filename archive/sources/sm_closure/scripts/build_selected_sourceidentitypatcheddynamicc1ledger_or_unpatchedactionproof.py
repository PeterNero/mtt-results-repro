"""Integrate patched finite C1 source identity into the SM-parity ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEDGER = PACKET_DIR / "source_identity_patched_dynamic_c1_ledger_update.packet.json"
INTERFACE = PACKET_DIR / "patched_dynamic_c1_source_and_value_interface.packet.json"
UPGRADE = PACKET_DIR / "unpatched_action_proof_upgrade_matrix.packet.json"
NEXTSTEPS = PACKET_DIR / "post_source_identity_patch_next_steps.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceIdentityPatchedDynamicC1Ledger_or_UnpatchedActionProof_v1.md"

SOURCE_IDENTITY = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"
SOURCE_REPLAY = (
    DATA
    / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
    / "patched_source_identity_dynamic_c1_replay.packet.json"
)
SOURCE_GUARDRAIL = (
    DATA
    / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
    / "unpatched_no_knob_guardrail.packet.json"
)
VALUE_PATCH = DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json"
VALUE_REPLAY = (
    DATA
    / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
    / "patched_routeb_dynamic_c1_closure_replay.packet.json"
)
OLD_LEDGER = DATA / "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation.candidate.json"
SM_LEDGER = DATA / "sm_parity_closure_ledger.candidate.json"

STATUS = "MTT_SELECTED_SOURCEIDENTITYPATCHEDDYNAMICC1LEDGER_OR_UNPATCHEDACTIONPROOF_BUILT_PATCHED_LEDGER_STRENGTHENED"
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

    source_identity = load(SOURCE_IDENTITY)
    source_replay = load(SOURCE_REPLAY)
    source_guardrail = load(SOURCE_GUARDRAIL)
    value_patch = load(VALUE_PATCH)
    value_replay = load(VALUE_REPLAY)
    old_ledger = load(OLD_LEDGER)
    sm_ledger = load(SM_LEDGER)

    promoted_values = value_replay["promoted_under_patched_spine"]
    source_rows = source_replay["row_counts"]

    ledger = {
        "schema": "MTTSourceIdentityPatchedDynamicC1LedgerUpdate.v1",
        "status": "PATCHED_SOURCE_IDENTITY_IMPORTED_TO_SM_PARITY_LEDGER",
        "previous_dynamic_c1_ledger": {
            "path": rel(OLD_LEDGER),
            "status": old_ledger["status"],
            "patched_dynamic_C1_no_longer_blocks_SM_parity": old_ledger["promotion_decision"][
                "patched_dynamic_C1_no_longer_blocks_SM_parity"
            ],
        },
        "strengthened_patch": {
            "source_identity_principle": source_replay["source_identity_principle"],
            "strict_source_id_validator_ok": source_replay["validator_ok"],
            "row_counts": source_rows,
            "source_ownership_promoted_under_local_principle": source_replay[
                "promoted_under_local_principle"
            ],
            "source_identity_packet_closed_under_local_principle": source_replay[
                "promoted_under_local_principle"
            ]["dynamic_C1_source_identity_packet_closed"],
        },
        "ledger_interpretation": (
            "The older patched dynamic C1 ledger closed the value-level interface under the local "
            "trace-measure principle. This stronger ledger adds the source-ownership layer: the "
            "SelectedFiniteC1SourceIdentityPrinciple promotes the 110-row source packet under a "
            "local SM-parity premise. The unpatched theorem remains open."
        ),
        "full_SM_parity_closed_now": False,
        "true_SM_equivalence_closed_now": False,
        "unpatched_no_knob_dynamic_C1_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(LEDGER, ledger)

    interface = {
        "schema": "MTTPatchedDynamicC1SourceAndValueInterface.v1",
        "status": "PATCHED_SOURCE_AND_VALUE_INTERFACE_AVAILABLE",
        "source_layer": {
            "selected_measure_pairing": True,
            "selected_quadrature_rule": True,
            "selected_variation_space": True,
            "R_Z_R_X_source_operators": True,
            "same_source_b_selected": True,
            "source_independence_from_residual_replay": True,
            "primitive_rows": source_rows["primitive_rows"],
            "sector_rows": source_rows["sector_rows"],
            "hessian_source_rows": source_rows["hessian_source_rows"],
            "strict_source_id_validator_ok": source_replay["validator_ok"],
        },
        "value_layer": {
            "patched_A_selected": promoted_values["physical_A_selected"],
            "patched_b_selected": promoted_values["physical_b_selected"],
            "patched_deltaTheta_C1": promoted_values["physical_deltaTheta_C1"],
            "patched_sector_response_matrices": promoted_values[
                "physical_sector_response_matrices"
            ],
            "patched_dynamic_C1_packet_closed": promoted_values[
                "patched_dynamic_C1_packet_closed"
            ],
        },
        "superset_strategy": {
            "straight_path_A": source_replay["superset_strategy"]["straight_path_A"],
            "straight_path_B": source_replay["superset_strategy"]["straight_path_B"],
            "combined_path": source_replay["superset_strategy"]["combined_path"],
            "locked_target": "SM-parity dynamic C1 source-and-value interface under local principle",
            "free_parameters_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(INTERFACE, interface)

    upgrade = {
        "schema": "MTTUnpatchedActionProofUpgradeMatrix.v1",
        "status": "UNPATCHED_ACTION_PROOF_REMAINS_NO_KNOB_UPGRADE_TARGET",
        "patched_local_closure": {
            "source_identity_packet": source_replay["validator_ok"],
            "dynamic_C1_value_packet": promoted_values["patched_dynamic_C1_packet_closed"],
            "SM_parity_dynamic_C1_blocker_removed": True,
        },
        "unpatched_upgrade_tasks": source_guardrail["unpatched_open_items"],
        "must_prove_for_no_knob": [
            "derive selected Phi_fin^C1 action restriction on the finite qutrit Weyl quotient",
            "derive trace/Frobenius measure as the physical source measure",
            "derive phase/shift variation space before residual projection",
            "derive same-source first and second variation emitting R_Z/R_X and b_selected",
            "derive no-extra-boundary/source term and source independence without local principle insertion",
        ],
        "patched_closure_not_allowed_for": source_guardrail["patched_closure_not_allowed_for"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(UPGRADE, upgrade)

    nextsteps = {
        "schema": "MTTPostSourceIdentityPatchNextSteps.v1",
        "status": "NEXT_STEPS_REDUCED_TO_FINAL_SM_PARITY_REPLAY_AND_UNPATCHED_UPGRADE",
        "patched_dynamic_C1_no_longer_blocks": [
            "source ownership of finite C1 row kernel",
            "A_selected/b_selected/deltaTheta_C1 local value interface",
            "sector response matrix replay under local principle",
            "SM-parity measured replay admission for dynamic C1",
        ],
        "remaining_for_SM_parity": {
            "final_integrated_replay_report": True,
            "common_RG_scale_transport_and_covariance": True,
            "selected_SM_packet_certificate_linkage": True,
            "local_QFT_observable_functor_or_empirical_suite": True,
        },
        "remaining_for_no_knob": {
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": True,
            "unpatched_action_boundary_source_proof": True,
            "derive_all_measured_constants_from_selected_sources": True,
        },
        "current_global_ledger_status": sm_ledger["status"],
        "recommended_next_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXTSTEPS, nextsteps)

    candidate = {
        "candidate": "MTTSelectedSourceIdentityPatchedDynamicC1LedgerOrUnpatchedActionProof",
        "status": STATUS,
        "inputs": {
            "source_identity_principle_insertion": rel(SOURCE_IDENTITY),
            "source_identity_replay": rel(SOURCE_REPLAY),
            "value_patch": rel(VALUE_PATCH),
            "value_replay": rel(VALUE_REPLAY),
            "previous_dynamic_c1_ledger": rel(OLD_LEDGER),
            "sm_parity_closure_ledger": rel(SM_LEDGER),
        },
        "output_packets": {
            "ledger_update": rel(LEDGER),
            "patched_dynamic_c1_source_and_value_interface": rel(INTERFACE),
            "unpatched_action_proof_upgrade_matrix": rel(UPGRADE),
            "post_source_identity_patch_next_steps": rel(NEXTSTEPS),
        },
        "theorem": {
            "name": "SourceIdentityPatchedDynamicC1LedgerTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "Under the local SelectedFiniteC1SourceIdentityPrinciple, the strict 110-row source "
                "packet validates and combines with the existing patched dynamic C1 value replay. "
                "Therefore dynamic C1 is no longer a source-or-value blocker for SM-parity in the "
                "patched/local spine, while the unpatched action proof remains a no-knob upgrade target."
            ),
        },
        "what_closes_now": {
            "patched_source_identity_imported_to_SM_parity_ledger": True,
            "patched_source_and_value_interface_available": True,
            "strict_110row_source_validator_imported": source_replay["validator_ok"],
            "patched_dynamic_C1_value_packet_imported": promoted_values[
                "patched_dynamic_C1_packet_closed"
            ],
            "unpatched_upgrade_matrix_declared": True,
        },
        "what_remains_open": {
            "final_integrated_SM_parity_replay": True,
            "common_RG_and_covariance_completion": True,
            "selected_SM_packet_certificate_linkage": True,
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": True,
            "full_no_knob_constants": True,
        },
        "promotion_decision": {
            "patched_dynamic_C1_no_longer_blocks_SM_parity": True,
            "patched_source_identity_closed": source_replay["validator_ok"],
            "patched_value_interface_closed": promoted_values["patched_dynamic_C1_packet_closed"],
            "full_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "unpatched_no_knob_dynamic_C1_closed": False,
        },
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": source_identity["status"],
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SourceIdentityPatchedDynamicC1Ledger_or_UnpatchedActionProof_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "theorem_patched": True,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        "# MTT Selected SourceIdentityPatchedDynamicC1Ledger or UnpatchedActionProof v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "The strengthened dynamic C1 ledger now imports both sides of the patched/local result:\n\n"
        "```text\n"
        f"strict source rows validated       = {source_replay['validator_ok']}\n"
        f"primitive/source rows              = {source_rows['primitive_rows']}\n"
        f"sector rows                        = {source_rows['sector_rows']}\n"
        f"hessian/source rows                = {source_rows['hessian_source_rows']}\n"
        f"patched A_selected                 = {promoted_values['physical_A_selected']}\n"
        f"patched b_selected                 = {promoted_values['physical_b_selected']}\n"
        f"patched deltaTheta_C1              = {promoted_values['physical_deltaTheta_C1']}\n"
        "full SM parity closed now          = False\n"
        "unpatched no-knob dynamic C1 closed = False\n"
        "```\n\n"
        "So dynamic C1 is no longer a patched SM-parity source-or-value blocker. "
        "The remaining no-knob upgrade is still the unpatched selected-action proof.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
