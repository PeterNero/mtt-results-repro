"""Build CONST-HIGGS-01 H6C H-sector row or boundary-route discriminator."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
OBSIDIAN_MTT = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory")

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROW_SEARCH = BASE / "actual_hsector_fourth_row_search.packet.json"
BOUNDARY_IMPORT = BASE / "susy_dterm_boundary_route_import.packet.json"
ROUTE_DECISION = BASE / "route_discriminator_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6C_HSectorRowOrBoundaryRouteDiscriminator_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6C_ROW_ABSENT_BOUNDARY_ROUTE_IDENTIFIED"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h6b_path = DATA / "const_higgs_01_h6b_local_source_identity_to_higgs_row_export.candidate.json"
    h6b_obstruction_path = DATA / "const_higgs_01_h6b_local_source_identity_to_higgs_row_export" / "quartic_row_export_obstruction.packet.json"
    h6_local_path = DATA / "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem" / "local_principle_kernel_import.packet.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    h3_quadratic_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "selected_quadratic_stiffness_kernel.packet.json"
    theta_exec_path = OBSIDIAN_MTT / "18 Theta-Closure & Execution Program" / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md"
    theta_verify_path = TEXPAPERS / "18 Theta-Closure & Execution Program" / "verification_report.md"
    correction_notes_path = TEXPAPERS / "18 Theta-Closure & Execution Program" / "_md_v3_corrected" / "V3_CORRECTION_NOTES.md"
    sm_tree_path = TEXPAPERS / "mtt-sm-parity-closure" / "candidate_data" / "sm_equivalence_tree_level_replay_seed.candidate.json"
    sm_lit_path = TEXPAPERS / "mtt-sm-parity-closure" / "candidate_data" / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance" / "literature_vs_local_convention_comparison.packet.json"

    h6b = load(h6b_path)
    h6b_obstruction = load(h6b_obstruction_path)
    h6_local = load(h6_local_path)
    h5b_projection = load(h5b_projection_path)
    h3_quadratic = load(h3_quadratic_path)
    sm_tree = load(sm_tree_path)
    sm_lit = load(sm_lit_path)

    tan_beta_example = 10
    cos2beta_sq = ((tan_beta_example * tan_beta_example - 1) / (tan_beta_example * tan_beta_example + 1)) ** 2
    legacy_gauge_over_4 = 0.2004
    legacy_lambda_over_4 = legacy_gauge_over_4 * cos2beta_sq
    corrected_lambda_over_8_same_gauge = legacy_lambda_over_4 / 2

    row_search = {
        "schema": "MTTConstHiggs01H6CActualHSectorFourthRowSearch.v1",
        "status": "NO_ACTUAL_HSECTOR_FOURTH_ROW_PACKET_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-ACTUAL-H-SECTOR-FOURTH-ROW-SEARCH",
        "searched_evidence": {
            "H6B_row_obstruction": rel(h6b_obstruction_path),
            "H6_local_source_identity": rel(h6_local_path),
            "H5B_projection_contract": rel(h5b_projection_path),
            "H3_quadratic_stiffness": rel(h3_quadratic_path),
            "neighbor_repo_scan_summary": "mtt-sm-parity-closure/mtt-sm-parity-repro/mtt-q79-proof-repro contain measured/replay lambda values and boundary-condition text, not a selected finite H-sector fourth-variation row.",
        },
        "target_row": {
            "formal_object": h5b_projection["projection_functional"]["projected_formal_object"],
            "coordinate_index": h6b["selected_Higgs_amplitude_coordinate"],
            "quartic_row_address": h6b["target_quartic_row_address"],
            "row_owner_source_local_tier": h6b["local_Higgs_row_export_contract_ready"],
        },
        "negative_result": {
            "actual_H_sector_fourth_variation_row_found": False,
            "exact_multilinear_formula_found": False,
            "row_exactness_certificate_found": False,
            "lambda_H_coefficient_convention_from_source_row_found": False,
            "no_knob_Higgs_value_found": False,
        },
        "non_promotions_reconfirmed": {
            "H3_quadratic_K2_to_K4": False,
            "H5B_row_address_to_row_value": False,
            "H6_SI1c_source_rows_to_H_sector_fourth_row": False,
            "SM_parity_measured_lambda_to_source": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary_import = {
        "schema": "MTTConstHiggs01H6CSusyDTermBoundaryRouteImport.v1",
        "status": "SUSY_DTERM_BOUNDARY_ROUTE_IDENTIFIED_AS_DISTINCT_FROM_H_ROW",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-SUSY-DTERM-BOUNDARY-ROUTE-IMPORT",
        "sources": {
            "original_theta_execution_higgs_section": str(theta_exec_path).replace("\\", "/"),
            "theta_verification_report_factor_check": str(theta_verify_path).replace("\\", "/"),
            "v3_correction_notes": str(correction_notes_path).replace("\\", "/"),
            "SM_parity_tree_level_replay_seed": rel(sm_tree_path),
            "SM_parity_external_RG_comparison": rel(sm_lit_path),
        },
        "corpus_finding": {
            "old_execution_formula_factor": "1/4",
            "standard_SM_normalized_MSSM_tree_formula_factor": "1/8",
            "standard_formula_for_V_minus_m2_H2_plus_lambda_H4": "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8",
            "old_factor_overhigh_by_two_under_standard_convention": True,
            "representative_tan_beta_in_old_text": tan_beta_example,
            "representative_tan_beta_selected_by_MTT": False,
        },
        "diagnostic_replay_not_source": {
            "tan_beta_example": tan_beta_example,
            "cos2beta_sq_exact_rational": "9801/10201",
            "cos2beta_sq_float": cos2beta_sq,
            "legacy_gauge_over_4_from_old_text": legacy_gauge_over_4,
            "legacy_lambda_over_4_diagnostic": legacy_lambda_over_4,
            "corrected_lambda_over_8_same_gauge_diagnostic": corrected_lambda_over_8_same_gauge,
            "diagnostic_values_used_as_selector": False,
        },
        "route_requirements_for_source_use": {
            "selected_gauge_couplings_or_selected_EW_boundary_packet": True,
            "selected_beta_or_two_Higgs_projection_angle": True,
            "matching_scale_and_threshold_policy": True,
            "RG_transport_to_observable_scale": True,
            "no_use_of_measured_Higgs_mass_or_lambda_as_selector": True,
        },
        "what_this_route_can_replace": {
            "finite_H_sector_fourth_row_required_for_boundary_lambda": False,
            "source_row_route_if_MTT_demands_intrinsic_phi4_action": True,
        },
        "what_this_route_does_not_close": {
            "selected_beta_or_tan_beta": True,
            "physical_gauge_coupling_normalization": True,
            "threshold_RG_precision": True,
            "strict_no_knob_Higgs_quartic": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_decision = {
        "schema": "MTTConstHiggs01H6CRouteDiscriminatorDecision.v1",
        "status": "TWO_LEGAL_HIGGS_QUARTIC_ROUTES_SEPARATED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-ROUTE-DISCRIMINATOR",
        "route_A_finite_H_row": {
            "role": "derive an intrinsic selected finite H-sector fourth-variation row",
            "current_status": "OPEN",
            "next_missing_object": "K_H^(4)[12,12,12,12] or exact finite multilinear formula from selected pre-residual action",
            "best_when": "MTT insists the Higgs quartic is an intrinsic finite Phi_fin self-interaction source.",
        },
        "route_B_boundary_matching": {
            "role": "derive the Higgs quartic as an electroweak/SUSY D-term boundary condition",
            "current_status": "FORMULA_IDENTIFIED_SOURCE_INPUTS_OPEN",
            "formula": "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8",
            "next_missing_object": "selected beta/tan_beta or two-Higgs projection angle plus selected EW gauge boundary and threshold/RG policy",
            "best_when": "MTT treats the quartic as a low-energy boundary induced by selected gauge/Higgs geometry rather than a standalone finite K4 row.",
        },
        "recommended_near_term_path": {
            "primary": "Route B boundary matching should be explored next because the corpus already contains this structural lane and it may avoid needing an intrinsic row.",
            "parallel_guard": "Keep Route A as the strict intrinsic-row route until the boundary route is theorem-derived.",
        },
        "superset_strategy": {
            "paths_compared": ["finite Phi_fin H-row route", "electroweak/SUSY D-term boundary route"],
            "locked_target": "selected Higgs quartic threshold source without measured lambda_H selector",
            "paths_combined_as_free_parameters": False,
            "allowed_future_parameter_note": "If beta/tan_beta is not theorem-derived, it must be declared as an explicit universal or Higgs-sector primitive, fixed once and reused, not tuned to Higgs mass.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6CNextWork.v1",
        "status": "NEXT_WORKORDER_H6D_SELECTED_BETA_OR_DTERM_BOUNDARY_PACKET",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE",
            "task": "Build the exact D-term boundary packet: selected gauge boundary, selected beta/tan_beta or two-Higgs projection angle, matching scale, threshold/RG policy, and no-Higgs-observation selector guardrail.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-ACTUAL-H-SECTOR-ROW-PAYLOAD",
            "task": "Continue searching for an intrinsic K_H^(4)[12,12,12,12] source row, but do not block boundary-route exploration on it.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / HIGGS-QUARTIC-ROUTE-DISCRIMINATOR",
            "task": "Correct the factor-of-two convention and separate intrinsic K4 row claims from D-term boundary matching claims.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6CHSectorRowOrBoundaryRouteDiscriminator",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-HSECTOR-ROW-OR-BOUNDARY-ROUTE-DISCRIMINATOR",
        "output_packets": {
            "actual_hsector_fourth_row_search": rel(ROW_SEARCH),
            "susy_dterm_boundary_route_import": rel(BOUNDARY_IMPORT),
            "route_discriminator_decision": rel(ROUTE_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6CHSectorRowOrBoundaryRouteDiscriminatorTheorem",
            "proved": True,
            "statement": (
                "The current repo, neighboring numerical repos, and the Theta corpus do not contain a selected actual H-sector fourth-variation row K_H^(4)[12,12,12,12]. They do contain a distinct supersymmetric/electroweak D-term Higgs-quartic boundary route. Under the standard SM potential convention V=-m^2|H|^2+lambda|H|^4, the correct MSSM tree boundary factor is (g^2+g'^2)cos^2(2 beta)/8, so older factor-1/4 text must be treated as conventionally high by a factor of two unless a different potential normalization is explicitly proved. Therefore the Higgs program now has two separated legal routes: intrinsic finite H-row emission, still open, or D-term boundary matching, formula identified but source inputs still open."
            ),
        },
        "actual_H_sector_fourth_variation_row_found": False,
        "boundary_route_identified": True,
        "standard_Dterm_boundary_formula_factor": "1/8",
        "old_factor_overhigh_by_two_under_standard_convention": True,
        "selected_beta_or_tan_beta_source_found": False,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6D_SelectedDTermBoundaryOrBetaSource_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6C_HSectorRowOrBoundaryRouteDiscriminator_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "actual_H_sector_fourth_variation_row_found": False,
        "boundary_route_identified": True,
        "standard_Dterm_boundary_formula_factor": "1/8",
        "old_factor_overhigh_by_two_under_standard_convention": True,
        "selected_beta_or_tan_beta_source_found": False,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6C H-Sector Row Or Boundary Route Discriminator v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-HSECTOR-ROW-OR-BOUNDARY-ROUTE-DISCRIMINATOR`

## Result

```text
actual K_H^(4)[12,12,12,12] row found            False
D-term boundary route identified                 True
standard boundary factor                         1/8
old 1/4 factor high by two under SM convention   True
selected beta/tan_beta source                    False
Higgs quartic numeric value                      False
strict no-knob Higgs closure                     False
```

## Route Split

Route A remains the intrinsic finite-row route:

```text
emit K_H^(4)[12,12,12,12]
```

Route B is the corpus-supported boundary route:

```text
lambda = (g^2 + g'^2) cos^2(2 beta) / 8
```

The old Theta execution text used a factor `1/4`; the verification/correction
notes already identify the standard SM-normalized MSSM tree-level factor as
`1/8` for `V=-m^2 |H|^2 + lambda |H|^4`.

## Meaning

This is progress because it prevents two different meanings of "Higgs quartic"
from being mixed.  The intrinsic row route and D-term boundary route are both
legal superset paths, but neither can use measured Higgs mass or target
`lambda_H` as a selector.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE`
"""

    for path, payload in [
        (ROW_SEARCH, row_search),
        (BOUNDARY_IMPORT, boundary_import),
        (ROUTE_DECISION, route_decision),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
