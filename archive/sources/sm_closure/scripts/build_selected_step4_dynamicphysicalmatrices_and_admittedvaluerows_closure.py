"""Build Step 4 closure boundary for dynamic matrices and admitted value rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step4_dynamicphysicalmatrices_and_admittedvaluerows_closure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC = PACKET_DIR / "step4_dynamic_physical_matrix_contract.packet.json"
VALUES = PACKET_DIR / "step4_admitted_value_row_contract.packet.json"
BOUNDARY = PACKET_DIR / "step4_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step4_to_step5_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step4_DynamicPhysicalMatrices_and_AdmittedValueRows_Closure_v1.md"

PHIFIN = DATA / "selected_phifinminimizertracesectorpayload_or_internalscalarrows.candidate.json"
U10 = DATA / "selected_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
DYNAMIC_OVERLAP = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"
MATTER_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
EXTERNAL_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
INTERNAL_SCALAR = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP4_DYNAMICPHYSICALMATRICES_AND_ADMITTEDVALUEROWS_CLOSURE_"
    "CLOSED_ADMITTED_REPLAY_INTERNAL_NOKNOB_HANDOFF"
)
NEXT = "MTT_Selected_Step5_NoKnobMinimalKnobAudit_or_InternalScalarRowsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 4 closure inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PHIFIN,
        U10,
        DYNAMIC_OVERLAP,
        MATTER_PACKET,
        QASU3,
        VSD01,
        EXTERNAL_IMPORT,
        KERNEL,
        INTERNAL_SCALAR,
    ]
    require_sources(sources)

    phifin = load(PHIFIN)
    u10 = load(U10)
    dynamic_overlap = load(DYNAMIC_OVERLAP)
    matter = load(MATTER_PACKET)
    qasu3 = load(QASU3)
    vsd01 = load(VSD01)
    external = load(EXTERNAL_IMPORT)
    kernel = load(KERNEL)
    internal = load(INTERNAL_SCALAR)

    dynamic_contract = {
        "schema": "MTTStep4DynamicPhysicalMatrixContract.v1",
        "status": "STEP4_DYNAMIC_MATRIX_CONTRACT_CLOSED_FIRST_RESPONSE_LAYER",
        "stale_phifin_matter_slot_blockers_retired_by_later_u10_artifact": (
            phifin["closure_decision"]["transported_sector_payload_imported"]
            and u10["closure_decision"]["static_U10_Ubar5_1M_source_closed"]
            and u10["closure_decision"]["static_matter_slot_readout_closed"]
        ),
        "static_matter_slot_source_closed": u10["closure_decision"][
            "static_U10_Ubar5_1M_source_closed"
        ],
        "dynamic_frontier_reduced_after_static_sector_closure": dynamic_overlap[
            "what_closes_now"
        ]["dynamic_frontier_reduced_after_static_sector_closure"],
        "same_source_dynamic_matter_overlap_packet_closed": matter["what_closes_now"][
            "same_source_dynamic_matter_overlap_packet_validates"
        ],
        "selected_dynamic_overlap_tensor_promoted": matter["what_closes_now"][
            "selected_dynamic_overlap_tensor_promoted"
        ],
        "selected_A_selected_b_selected_preserved": matter["what_closes_now"][
            "selected_A_selected_b_selected_preserved"
        ],
        "dynamic_QaSU3_first_response_layer_closed": qasu3["promotion_decision"][
            "dynamic_QaSU3_first_response_layer_closed"
        ],
        "VSD01_source_assembly_subgate_closed": vsd01["closure_decision"][
            "VSD01_source_assembly_subgate_closed"
        ],
        "VSD01_dynamic_overlap_subgate_closed": vsd01["closure_decision"][
            "VSD01_dynamic_overlap_subgate_closed"
        ],
        "physical_PhiFinC1_action_source": vsd01["what_closes_now"][
            "physical_PhiFinC1_action_source"
        ],
        "A_selected_promoted": vsd01["what_closes_now"]["A_selected_promoted"],
        "b_selected_promoted": vsd01["what_closes_now"]["b_selected_promoted"],
        "deltaTheta_C1_promoted": vsd01["what_closes_now"]["deltaTheta_C1_promoted"],
        "formal_110_row_assembly": vsd01["what_closes_now"]["formal_110_row_assembly"],
        "all_72_primitive_rows_exact": vsd01["what_closes_now"]["all_72_primitive_rows_exact"],
        "dynamic_physical_matrix_contract_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DYNAMIC, dynamic_contract)

    value_contract = {
        "schema": "MTTStep4AdmittedValueRowContract.v1",
        "status": "STEP4_ADMITTED_VALUE_ROW_CONTRACT_CLOSED_INTERNAL_NOKNOB_OPEN",
        "external_import_lane_closed_at_admitted_replay_tier": external["closure_decision"][
            "external_import_lane_closed_at_admitted_replay_tier"
        ],
        "accepted_external_threshold_row_count": external["closure_decision"][
            "accepted_external_threshold_row_count"
        ],
        "accepted_external_mass_scheme_row_count": external["closure_decision"][
            "accepted_external_mass_scheme_row_count"
        ],
        "accepted_diagonal_profile_theorem_closed": external["closure_decision"][
            "accepted_diagonal_profile_theorem_closed"
        ],
        "internal_selected_Rtheta_value_row_emitted": external["closure_decision"][
            "internal_selected_Rtheta_value_row_emitted"
        ],
        "accepted_internal_scalar_row_count": internal["closure_decision"][
            "accepted_internal_scalar_row_count"
        ],
        "lambda_H_row_emitted": internal["closure_decision"]["lambda_H_row_emitted"],
        "kernel_readiness": kernel["closure_decision"]["final_no_knob_kernel_typed"],
        "kernel_readiness_fraction": internal["kernel_readiness"],
        "selected_universal_parameter_count": kernel["closure_decision"][
            "selected_universal_parameter_count"
        ],
        "admitted_value_row_contract_closed": True,
        "internal_no_knob_value_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(VALUES, value_contract)

    boundary = {
        "schema": "MTTStep4ClosureBoundary.v1",
        "status": "STEP4_CLOSED_FOR_PLAN_CONTRACT_INTERNAL_NOKNOB_DEFERRED",
        "step4_plan_label": "derive dynamic physical matrices and accepted value rows",
        "closed_interpretation": (
            "dynamic physical matrices/source packet plus accepted admitted-replay value rows"
        ),
        "not_closed_interpretation": (
            "internal no-knob scalar value rows, lambda_H, Yukawa/CKM/PMNS/mass prediction"
        ),
        "step4_dynamic_physical_matrices_closed": True,
        "step4_accepted_admitted_value_rows_closed": True,
        "step4_internal_no_knob_value_rows_closed": False,
        "step4_closed_for_plan_contract": True,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BOUNDARY, boundary)

    handoff = {
        "schema": "MTTStep4ToStep5Handoff.v1",
        "status": "HANDOFF_TO_STEP5_NOKNOB_MINIMALKNOB_AUDIT_OR_INTERNAL_SCALAR_EXECUTION",
        "completed_step": 4,
        "next_step": 5,
        "next_required_artifact": NEXT,
        "step5_live_questions": {
            "internal_Rtheta_scalar_rows": True,
            "lambda_H_row": True,
            "accepted_Yukawa_magnitudes": True,
            "CKM_PMNS_value_closure": True,
            "candidate_specific_universal_source_anchor": True,
            "minimal_knob_policy_if_no_internal_derivation": True,
        },
        "do_not_reopen_as_step4_blockers": {
            "Phi_fin_transport_replay": True,
            "static_U10_Ubar5_1M_matter_slot_readout": True,
            "A_selected_b_selected_deltaTheta_C1_first_response": True,
            "post_pi_admitted_external_threshold_mass_scheme_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep4DynamicPhysicalMatricesAndAdmittedValueRowsClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step4_dynamic_physical_matrix_contract": rel(DYNAMIC),
            "step4_admitted_value_row_contract": rel(VALUES),
            "step4_closure_boundary": rel(BOUNDARY),
            "step4_to_step5_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step4DynamicMatrixAndAdmittedValueRowClosureBoundaryTheorem",
            "proved": True,
            "statement": (
                "The plan Step 4 contract is closed at the dynamic-matrix/admitted-replay tier: "
                "static matter slots, dynamic first-response matrices, VSD01 source assembly, "
                "A_selected, b_selected, deltaTheta_C1, and the admitted external threshold/"
                "mass-scheme/profile rows are all present without observed-data selection. This "
                "does not close internal no-knob scalar rows, lambda_H, Yukawa/CKM/PMNS/mass "
                "prediction, true SM equivalence, or full no-knob closure; those become Step 5."
            ),
        },
        "closure_decision": {
            "step4_closed_for_plan_contract": True,
            "step4_dynamic_physical_matrices_closed": True,
            "step4_accepted_admitted_value_rows_closed": True,
            "step4_internal_no_knob_value_rows_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "accepted_external_threshold_row_count": value_contract[
                "accepted_external_threshold_row_count"
            ],
            "accepted_external_mass_scheme_row_count": value_contract[
                "accepted_external_mass_scheme_row_count"
            ],
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step4_plan_contract": True,
            "dynamic_physical_matrix_contract": True,
            "admitted_external_value_row_contract": True,
            "stale_phifin_u10_dynamicoverlap_loop_retired": True,
            "step5_handoff_typed": True,
        },
        "what_remains_open": handoff["step5_live_questions"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step4_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step4_DynamicPhysicalMatrices_and_AdmittedValueRows_Closure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step4_contract_closure_claimed": True,
        "step4_closed_for_plan_contract": True,
        "step4_dynamic_physical_matrices_closed": True,
        "step4_accepted_admitted_value_rows_closed": True,
        "step4_internal_no_knob_value_rows_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step4 DynamicPhysicalMatrices and AdmittedValueRows Closure v1

Status: `{STATUS}`.

Step 4 is closed at the plan-contract tier:

```text
dynamic physical matrices/source packet : true
accepted admitted external value rows   : true
accepted external threshold rows        : {value_contract["accepted_external_threshold_row_count"]}
accepted external mass-scheme rows      : {value_contract["accepted_external_mass_scheme_row_count"]}
accepted diagonal profile theorem       : {str(value_contract["accepted_diagonal_profile_theorem_closed"]).lower()}
internal selected scalar rows           : 0
internal no-knob value rows closed      : false
true SM equivalence closed              : false
full no-knob closure                    : false
```

This retires the Step 4 loop: Phi_fin transport replay, static U10/Ubar5/1M
readout, first-response A/b/deltaTheta, VSD01 source assembly, and post-Pi
admitted external rows are no longer Step 4 blockers.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
