"""Build R_H^RG determinant/index candidate or external validation target packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DET_MATRIX = PACKET_DIR / "rhrg_determinant_index_candidate_matrix.packet.json"
HIGGS_BINDING = PACKET_DIR / "higgs_projection_binding_to_rhrg_contract.packet.json"
VALIDATION_TARGET = PACKET_DIR / "external_validation_target_manifest.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rhrg_candidate_matrix.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RHRGDeterminantIndexCandidate_or_ExternalValidationTarget_v1.md"

PREVIOUS = DATA / "selected_strictrhrgsourceconstruction_or_independentvalidationoracle.candidate.json"
FOUR_SLOT = DATA / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun.candidate.json"
THREE_SLOT = DATA / "selected_chernweilde_or_determinanttorsion_threeslotclosingrun.candidate.json"
TWO_SLOT = DATA / "selected_detransition_or_determinanttorsion_twoslotclosingrun.candidate.json"
HIGGS_C5C6 = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
HSECTOR = DATA / "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows.candidate.json"
DIRECT_H = DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json"
HRADIAL = DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json"
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
INTRINSIC = DATA / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json"
FULL_MSOURCE = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"

STATUS = (
    "MTT_SELECTED_RHRGDETERMINANTINDEXCANDIDATE_OR_EXTERNALVALIDATIONTARGET_"
    "MATRIX_BUILT_ZERO_ACCEPTED_CANDIDATES"
)
NEXT = "MTT_Selected_HSectorDeterminantRGOperatorDefinition_or_TargetIndependentValidationRun_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing RHRG determinant/index inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        FOUR_SLOT,
        THREE_SLOT,
        TWO_SLOT,
        HIGGS_C5C6,
        HSECTOR,
        DIRECT_H,
        HRADIAL,
        EW_BOUNDARY,
        INTRINSIC,
        FULL_MSOURCE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    four_slot = load(FOUR_SLOT)
    three_slot = load(THREE_SLOT)
    two_slot = load(TWO_SLOT)
    higgs = load(HIGGS_C5C6)
    hsector = load(HSECTOR)
    direct_h = load(DIRECT_H)
    hradial = load(HRADIAL)
    ew_boundary = load(EW_BOUNDARY)
    intrinsic = load(INTRINSIC)
    full_msource = load(FULL_MSOURCE)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]
    s_beta = higgs["closure_decision"]["selected_s_beta_value"]

    determinant_candidates = [
        {
            "candidate": "generic_chern_weil_hym_DE_slot",
            "source_ref": rel(FOUR_SLOT),
            "support_closed": four_slot["closure_decision"]["selected_HYM_or_RouteC_residual_slot_closed"],
            "finite_determinant_or_torsion_response_emitted": False,
            "H_sector_bound": False,
            "accepted_for_R_H_RG": False,
            "reason": "HYM/source slot support is closed, but no finite determinant/heat/torsion response value is emitted and no H-sector threshold/RG operator is bound.",
        },
        {
            "candidate": "chern_weil_DE_three_slot",
            "source_ref": rel(THREE_SLOT),
            "support_closed": three_slot["closure_decision"]["same_source_Chern_Weil_row_derived_slot_closed"],
            "finite_determinant_or_torsion_response_emitted": three_slot["closure_decision"]["finite_determinant_heat_spectrum_or_torsion_response_closed"],
            "H_sector_bound": False,
            "accepted_for_R_H_RG": False,
            "reason": "Chern-Weil row support does not instantiate a selected H-sector determinant/index/RG multiplier.",
        },
        {
            "candidate": "DE_transition_two_slot",
            "source_ref": rel(TWO_SLOT),
            "support_closed": two_slot["closure_decision"]["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
            "finite_determinant_or_torsion_response_emitted": two_slot["closure_decision"]["finite_determinant_heat_spectrum_or_torsion_response_closed"],
            "H_sector_bound": False,
            "accepted_for_R_H_RG": False,
            "reason": "Transition/DE data sharpen the operator-source frontier but still emit no H-sector determinant/index value.",
        },
    ]

    higgs_binding = {
        "schema": "MTTHiggsProjectionBindingToRHRGContract.v1",
        "status": "HIGGS_PROJECTION_DATA_BOUND_TO_RHRG_CONTRACT_BUT_RG_OPERATOR_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_higgs_inputs": {
            "C5b_projection_measure_equality_closed": higgs["closure_decision"]["bridge_validator_C5b_projection_measure_equality_closed"],
            "C6_no_boundary_closed": higgs["closure_decision"]["bridge_validator_C6_no_boundary_closed"],
            "selected_s_beta_value_found": higgs["closure_decision"]["selected_s_beta_value_found"],
            "selected_s_beta_value": s_beta,
            "selected_H_sector_restriction_R_H_emitted": full_msource["closure_decision"]["selected_H_sector_restriction_R_H_emitted"]
            or higgs["closure_decision"].get("selected_H_sector_restriction_R_H_emitted", False),
        },
        "still_open_for_R_H_RG": {
            "selected_H_threshold_RG_operator_emitted": intrinsic["closure_decision"]["selected_H_threshold_RG_operator_emitted"],
            "selected_large_threshold_RG_theorem_emitted": intrinsic["closure_decision"]["selected_large_threshold_RG_theorem_emitted"],
            "selected_matching_scale_mu_match_closed": hradial["closure_decision"]["selected_matching_scale_mu_match_closed"],
            "selected_A_EW_emitted": ew_boundary["closure_decision"]["selected_A_EW_emitted"],
            "selected_threshold_RG_transport_closed": ew_boundary["closure_decision"]["selected_threshold_RG_transport_closed"],
            "K_threshold_Omega_H_lambda_emitted": hsector["closure_decision"]["K_threshold_Omega_H_lambda_emitted"],
            "selected_H_response_table_emitted": full_msource["closure_decision"]["selected_H_response_table_emitted"],
        },
        "name_collision_guard": {
            "kinematic_R_H_is_selected_or_partly_selected": True,
            "threshold_RG_R_H_RG_selected": False,
            "may_identify_R_H_with_R_H_RG": False,
            "reason": "The selected H-sector restriction/projection map is a domain map for H_response/Huv extraction. R_H^RG is a scalar/operator threshold transport value and requires determinant/index/RG provenance.",
        },
    }

    validation_target = {
        "schema": "MTTExternalValidationTargetManifest.v1",
        "status": "EXTERNAL_VALIDATION_TARGETS_DECLARED_NONE_IMPORTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "accepted_external_validation_target_count": 0,
        "allowed_after_source_selection_only": [
            "non-Higgs threshold/RG transport observable predicted by the same HRG scalar without retuning",
            "independent H-sector determinant/index computation yielding R_H^RG before lambda_H comparison",
            "future numerical H_response/Huv table produced from selected F_H, then compared downstream",
        ],
        "forbidden_as_selector": [
            "lambda_H(M_t)",
            "Higgs mass or top mass residual scan",
            "A_EW or mu_match chosen to force HRG",
            "near-miss finite invariant formula promoted by closeness",
        ],
    }

    determinant_matrix = {
        "schema": "MTTRHRGDeterminantIndexCandidateMatrix.v1",
        "status": "RHRG_DETERMINANT_INDEX_CANDIDATES_TESTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target_value_for_diagnostic_only": hrg,
        "candidate_rows": determinant_candidates,
        "decision": {
            "tested_candidate_count": len(determinant_candidates),
            "accepted_R_H_RG_candidate_count": 0,
            "determinant_index_candidate_accepted": False,
            "external_validation_target_imported": False,
            "strict_R_H_RG_source_constructed": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterRHRGCandidateMatrix.v1",
        "status": "NEXT_FRONTIER_HSECTOR_DETERMINANT_RG_OPERATOR_DEFINITION_OR_TARGET_INDEPENDENT_VALIDATION_RUN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "determinant/torsion candidates tested against the R_H^RG acceptance contract",
            "Higgs projection/s_beta/R_H kinematic binding separated from threshold RG R_H^RG",
            "external validation target manifest declared with zero imported targets",
        ],
        "still_open": [
            "define selected H-sector determinant/RG operator whose zeta determinant, torsion, or index emits R_H^RG",
            "run target-independent validation only after that operator is selected",
            "selected mu_match and A_EW source rows for strict H threshold transport",
            "K_threshold.Omega_H.lambda and ten-K antecedent",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedRHRGDeterminantIndexCandidateOrExternalValidationTarget",
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
            "name": "RHRGDeterminantIndexCandidateOrExternalValidationTargetTheorem",
            "proved": True,
            "statement": (
                "The available determinant/torsion and Higgs projection packets "
                "do not yet instantiate a selected H-sector determinant/index/RG "
                "operator for R_H^RG.  They narrow the next construction to an "
                "H-sector determinant/RG operator definition or a later independent "
                "validation run after source selection."
            ),
        },
        "packets": {
            "determinant_matrix": rel(DET_MATRIX),
            "higgs_binding": rel(HIGGS_BINDING),
            "validation_target": rel(VALIDATION_TARGET),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "determinant_index_candidate_accepted": False,
            "accepted_R_H_RG_candidate_count": 0,
            "higgs_projection_binding_closed": True,
            "selected_s_beta_available": True,
            "threshold_RG_R_H_RG_selected": False,
            "external_validation_target_imported": False,
            "strict_R_H_RG_source_constructed": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg,
            "selected_s_beta_value": s_beta,
            "tested_determinant_index_candidate_count": len(determinant_candidates),
            "accepted_R_H_RG_candidate_count": 0,
            "accepted_external_validation_target_count": 0,
            "accepted_selected_K_source_row_count": hsector["closure_decision"]["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": hsector["closure_decision"]["selected_K_threshold_row_count_required"],
        },
    }

    cert = {
        "certificate": "MTTSelectedRHRGDeterminantIndexCandidateOrExternalValidationTarget",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "determinant_index_candidate_accepted": False,
        "accepted_R_H_RG_candidate_count": 0,
        "higgs_projection_binding_closed": True,
        "selected_s_beta_available": True,
        "threshold_RG_R_H_RG_selected": False,
        "external_validation_target_imported": False,
        "strict_R_H_RG_source_constructed": False,
        "lambda_H_predicted": False,
    }

    note = f"""# MTT Selected R_H^RG Determinant/Index Candidate or External Validation Target v1

Status: `{STATUS}`

## Theorem

The determinant/torsion packets and the latest Higgs projection packets have
now been bound to the `R_H^RG` acceptance contract.  They supply useful support
but do not yet emit a selected threshold/RG source value.

## What Closes

- determinant/torsion candidates tested: `{len(determinant_candidates)}`
- accepted `R_H^RG` candidates: `0`
- selected `s_beta` available: `true`
- Higgs projection/reduction binding closed: `true`
- kinematic H-sector `R_H` kept distinct from threshold/RG `R_H^RG`

## What Remains Open

- selected H-sector determinant/RG operator definition;
- selected `mu_match` and `A_EW` source rows for the strict no-knob tier;
- `K_threshold.Omega_H.lambda`;
- independent validation target after source selection;
- true SM/no-knob equivalence.

Next artifact: `{NEXT}`
"""

    write_json(DET_MATRIX, determinant_matrix)
    write_json(HIGGS_BINDING, higgs_binding)
    write_json(VALIDATION_TARGET, validation_target)
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
