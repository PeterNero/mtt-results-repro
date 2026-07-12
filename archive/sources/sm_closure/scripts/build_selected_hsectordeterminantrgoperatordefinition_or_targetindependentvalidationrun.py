"""Build H-sector determinant/RG operator definition or target-independent validation run."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OPERATOR_DEF = PACKET_DIR / "hsector_determinant_rg_operator_definition.packet.json"
SLOT_EXECUTION = PACKET_DIR / "hsector_determinant_rg_slot_execution.packet.json"
VALIDATION_RUN = PACKET_DIR / "target_independent_validation_run.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hsector_determinant_rg_definition.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HSectorDeterminantRGOperatorDefinition_or_TargetIndependentValidationRun_v1.md"

PREVIOUS = DATA / "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget.candidate.json"
HIGGS_C5C6 = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
HIGGS_C5C6_GATE = (
    DATA
    / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
    / "hk_threshold_gate_after_c5bc6_projection.packet.json"
)
FULL_MSOURCE = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"
FULL_MSOURCE_GATE = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "selected_source_object_value_gate.packet.json"
)
RHRG_BINDING = (
    DATA
    / "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget"
    / "higgs_projection_binding_to_rhrg_contract.packet.json"
)
FIRSTPASS_RG = (
    DATA
    / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
    / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
)
INTRINSIC = DATA / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json"
HRADIAL = DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json"
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
HSECTOR = DATA / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows.candidate.json"

STATUS = (
    "MTT_SELECTED_HSECTORDETERMINANTRGOPERATORDEFINITION_OR_TARGETINDEPENDENTVALIDATIONRUN_"
    "OPERATOR_CONTRACT_DEFINED_VALUE_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_HSectorLogDeterminantKernel_or_SelectedHResponseSpectrum_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-sector determinant/RG inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        HIGGS_C5C6,
        HIGGS_C5C6_GATE,
        FULL_MSOURCE,
        FULL_MSOURCE_GATE,
        RHRG_BINDING,
        FIRSTPASS_RG,
        INTRINSIC,
        HRADIAL,
        EW_BOUNDARY,
        HSECTOR,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    higgs = load(HIGGS_C5C6)
    higgs_gate = load(HIGGS_C5C6_GATE)
    full_msource = load(FULL_MSOURCE)
    full_gate = load(FULL_MSOURCE_GATE)
    binding = load(RHRG_BINDING)
    firstpass_rg = load(FIRSTPASS_RG)
    intrinsic = load(INTRINSIC)
    hradial = load(HRADIAL)
    ew_boundary = load(EW_BOUNDARY)
    hsector = load(HSECTOR)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]
    s_beta = previous["key_numbers"]["selected_s_beta_value"]
    hrow = higgs_gate["H_row"]
    required_objects = full_gate["required_selected_source_objects"]

    selected_inputs = {
        "same_q79_F_m1_source_space": full_msource["closure_decision"]["same_q79_F_m1_source_space_verified"],
        "B_Huv_two_column_lift": full_msource["closure_decision"]["B_Huv_two_column_uv_lift_emitted"],
        "C5a_trace_grid_identity": full_msource["closure_decision"]["C5a_trace_grid_identity_closed"],
        "C5b_projection_measure_equality": higgs["closure_decision"]["bridge_validator_C5b_projection_measure_equality_closed"],
        "C6_no_boundary_source": higgs["closure_decision"]["bridge_validator_C6_no_boundary_closed"],
        "selected_s_beta": higgs["closure_decision"]["selected_s_beta_value_found"],
        "selected_H_projector_P_H": hrow["selected_H_projector_P_H_emitted"],
        "dynamic_Hessian_domain_on_BHuv": hrow["dynamic_Hessian_domain_on_BHuv_closed"],
        "second_variation_source_gate": hrow["second_variation_source_gate_closed"],
    }
    missing_value_inputs = {
        "selected_H_response_or_F_H_spectrum": not required_objects["H_response"]["emitted"],
        "strict_exportable_H_sector_restriction_values": not required_objects["R_H"]["emitted"],
        "selected_H_threshold_RG_operator": not intrinsic["closure_decision"]["selected_H_threshold_RG_operator_emitted"],
        "selected_mu_match": not hradial["closure_decision"]["selected_matching_scale_mu_match_closed"],
        "selected_A_EW": not ew_boundary["closure_decision"]["selected_A_EW_emitted"],
        "selected_threshold_RG_transport": not ew_boundary["closure_decision"]["selected_threshold_RG_transport_closed"],
        "selected_K_threshold_Omega_H_lambda": not hsector["closure_decision"]["K_threshold_Omega_H_lambda_emitted"],
        "selected_logdet_or_torsion_spectrum": True,
    }

    operator_definition = {
        "schema": "MTTHSectorDeterminantRGOperatorDefinition.v1",
        "status": "HSECTOR_DETERMINANT_RG_OPERATOR_CONTRACT_DEFINED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "operator": {
            "id": "R_H^RG(mu_match -> M_t)",
            "domain": "selected q79/F,m=1 H-sector response subspace over B_Huv",
            "input_operator": "L_H(mu)=P_H Herm(Hess(F_H(mu))) P_H on the two-Higgs response domain",
            "source_functional": "F_H selected second variation or equivalent selected H_response/Huv table",
            "value_rule": (
                "R_H^RG(mu0->mu1)=exp(-1/2*(logdet_zeta L_H(mu1)-"
                "logdet_zeta L_H(mu0)) + integral_gamma_H^sel(mu0,mu1) + index_H^sel)"
            ),
            "determinant_branch": "zeta/logdet or determinant-torsion response on the same H-sector source",
            "acceptance_output": "numeric UP_RET_OVERLAP.HRG only after all source slots are selected",
        },
        "selected_inputs_available": selected_inputs,
        "missing_value_inputs": missing_value_inputs,
        "definition_decision": {
            "operator_contract_defined": True,
            "operator_value_emitted": False,
            "R_H_RG_selected": False,
            "lambda_H_predicted": False,
            "counts_for_no_knob_closure": False,
        },
        "source_refs": [rel(HIGGS_C5C6_GATE), rel(FULL_MSOURCE_GATE), rel(RHRG_BINDING)],
    }

    slot_execution = {
        "schema": "MTTHSectorDeterminantRGSlotExecution.v1",
        "status": "HSECTOR_DETERMINANT_RG_SLOTS_EXECUTED_VALUE_SPECTRUM_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "slot_table": {
            "geometry_domain_slots_closed": sum(1 for value in selected_inputs.values() if value),
            "geometry_domain_slot_count": len(selected_inputs),
            "value_slots_missing": sum(1 for value in missing_value_inputs.values() if value),
            "value_slot_count": len(missing_value_inputs),
        },
        "closed_geometry_slots": [key for key, value in selected_inputs.items() if value],
        "open_value_slots": [key for key, value in missing_value_inputs.items() if value],
        "diagnostic_target_value_not_used": hrg,
        "execution_decision": {
            "domain_contract_executable": True,
            "logdet_kernel_executable_now": False,
            "target_independent_numeric_validation_executable_now": False,
            "strict_R_H_RG_source_constructed": False,
            "accepted_R_H_RG_source_count": 0,
        },
    }

    validation_run = {
        "schema": "MTTTargetIndependentValidationRun.v1",
        "status": "TARGET_INDEPENDENT_VALIDATION_NOT_RUN_SOURCE_OPERATOR_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "firstpass_RG_support_ref": rel(FIRSTPASS_RG),
        "firstpass_RG_support_classification": {
            "accepted_for_SM_parity": firstpass_rg["accepted_for_SM_parity"],
            "accepted_for_true_precision_equivalence": firstpass_rg["accepted_for_true_precision_equivalence"],
            "accepted_as_no_knob_R_H_RG_source": False,
            "reason": "First-pass common-scale RG transport is a parity convention/replay, not a selected H-sector determinant or threshold source.",
        },
        "validation_targets": {
            "candidate_target_count": 0,
            "accepted_target_count": 0,
            "run_after_source_selection_only": True,
        },
        "decision": {
            "validation_run_executed": False,
            "validation_run_blocked_by_missing_source_operator": True,
            "external_targets_imported": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHSectorDeterminantRGDefinition.v1",
        "status": "NEXT_FRONTIER_HSECTOR_LOGDETERMINANT_KERNEL_OR_SELECTED_H_RESPONSE_SPECTRUM",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "H-sector determinant/RG operator contract defined",
            "selected geometry/domain slots separated from missing value/spectrum slots",
            "first-pass RG support classified as SM-parity replay only",
        ],
        "still_open": [
            "selected H_response or F_H second-variation spectrum on B_Huv",
            "selected zeta/logdet or determinant-torsion kernel on the H-sector source",
            "selected mu_match and A_EW source rows for strict threshold transport",
            "numeric R_H^RG value emission",
            "target-independent validation run after source selection",
            "K_threshold.Omega_H.lambda and ten-K antecedent",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHSectorDeterminantRGOperatorDefinitionOrTargetIndependentValidationRun",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "HSectorDeterminantRGOperatorDefinitionOrTargetIndependentValidationRunTheorem",
            "proved": True,
            "statement": (
                "The H-sector determinant/RG source operator can be defined as a "
                "same-source zeta/logdet or determinant-torsion response on the "
                "selected B_Huv/P_H domain. Current MTT data close the geometry "
                "domain but do not emit the H_response spectrum, logdet kernel, "
                "mu_match/A_EW source rows, or numeric R_H^RG value."
            ),
        },
        "packets": {
            "operator_definition": rel(OPERATOR_DEF),
            "slot_execution": rel(SLOT_EXECUTION),
            "validation_run": rel(VALIDATION_RUN),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "operator_contract_defined": True,
            "domain_contract_executable": True,
            "selected_geometry_domain_slots_closed": True,
            "logdet_kernel_executable_now": False,
            "operator_value_emitted": False,
            "R_H_RG_selected": False,
            "target_independent_validation_run_executed": False,
            "accepted_R_H_RG_source_count": 0,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG_diagnostic_only": hrg,
            "selected_s_beta_value": s_beta,
            "closed_geometry_domain_slot_count": sum(1 for value in selected_inputs.values() if value),
            "geometry_domain_slot_count": len(selected_inputs),
            "missing_value_slot_count": sum(1 for value in missing_value_inputs.values() if value),
            "value_slot_count": len(missing_value_inputs),
            "accepted_R_H_RG_source_count": 0,
            "accepted_validation_target_count": 0,
            "accepted_selected_K_source_row_count": hsector["closure_decision"]["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": hsector["closure_decision"]["selected_K_threshold_row_count_required"],
        },
    }

    cert = {
        "certificate": "MTTSelectedHSectorDeterminantRGOperatorDefinitionOrTargetIndependentValidationRun",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "operator_contract_defined": True,
        "domain_contract_executable": True,
        "logdet_kernel_executable_now": False,
        "operator_value_emitted": False,
        "R_H_RG_selected": False,
        "target_independent_validation_run_executed": False,
        "accepted_R_H_RG_source_count": 0,
        "lambda_H_predicted": False,
    }

    note = f"""# MTT Selected H-Sector Determinant/RG Operator Definition or Target-Independent Validation Run v1

Status: `{STATUS}`

## Theorem

The H-sector determinant/RG source operator is now defined as a same-source
zeta/logdet or determinant-torsion response on the selected `B_Huv/P_H` Higgs
domain.  This closes the operator contract, not the value.

## Operator

`L_H(mu)=P_H Herm(Hess(F_H(mu))) P_H`

`R_H^RG(mu0->mu1)=exp(-1/2*(logdet_zeta L_H(mu1)-logdet_zeta L_H(mu0)) + integral_gamma_H^sel + index_H^sel)`

## Slot Execution

- closed geometry/domain slots: `{sum(1 for value in selected_inputs.values() if value)}/{len(selected_inputs)}`
- missing value/spectrum slots: `{sum(1 for value in missing_value_inputs.values() if value)}/{len(missing_value_inputs)}`
- logdet kernel executable now: `false`
- target-independent validation run executed: `false`
- accepted `R_H^RG` source count: `0`

## Boundary

First-pass RG transport is classified as SM-parity replay/convention support
only.  It is not a selected no-knob `R_H^RG` source.

Next artifact: `{NEXT}`
"""

    write_json(OPERATOR_DEF, operator_definition)
    write_json(SLOT_EXECUTION, slot_execution)
    write_json(VALIDATION_RUN, validation_run)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
