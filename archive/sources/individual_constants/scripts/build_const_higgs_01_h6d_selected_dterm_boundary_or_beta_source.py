"""Build CONST-HIGGS-01 H6D selected D-term boundary or beta-source gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SINGLE_HIGGS_IMPORT = BASE / "single_higgs_projection_import.packet.json"
BETA_SOURCE_TEST = BASE / "beta_or_projection_angle_source_test.packet.json"
DTERM_CONTRACT = BASE / "dterm_boundary_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6D_SelectedDTermBoundaryOrBetaSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6D_DTERM_BOUNDARY_CONTRACT_BUILT_BETA_SOURCE_OPEN"


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

    h6c_path = DATA / "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator.candidate.json"
    h6c_boundary_path = DATA / "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator" / "susy_dterm_boundary_route_import.packet.json"
    h6c_decision_path = DATA / "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator" / "route_discriminator_decision.packet.json"
    h6b_contract_path = DATA / "const_higgs_01_h6b_local_source_identity_to_higgs_row_export" / "local_source_identity_to_higgs_row_export.packet.json"
    ew_b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching" / "rg_matching_threshold_scheme_status.packet.json"
    ew_b42_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
    q79_single_path = Q79_REPO / "certificates" / "single_higgs_channel_projection_certificate.json"
    q79_zero_mode_path = Q79_REPO / "certificates" / "selected_zero_mode_basis_dotd_interface_certificate.json"
    sm_matter_slot_path = SM_PARITY_REPO / "candidate_data" / "selected_matterslot_grading_or_sectionring_readout.candidate.json"

    h6c = load(h6c_path)
    h6c_boundary = load(h6c_boundary_path)
    h6c_decision = load(h6c_decision_path)
    h6b_contract = load(h6b_contract_path)
    ew_b41 = load(ew_b41_path)
    ew_b42 = load(ew_b42_path)
    q79_single = load(q79_single_path)
    q79_zero_mode = load(q79_zero_mode_path)
    sm_matter_slot = load(sm_matter_slot_path)

    tan_beta_example = h6c_boundary["corpus_finding"]["representative_tan_beta_in_old_text"]
    cos2beta_sq_example = h6c_boundary["diagnostic_replay_not_source"]["cos2beta_sq_float"]

    single_higgs_import = {
        "schema": "MTTConstHiggs01H6DSingleHiggsProjectionImport.v1",
        "status": "LOW_ENERGY_SINGLE_HIGGS_PROJECTION_IMPORTED_BETA_NOT_SELECTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SINGLE-HIGGS-PROJECTION-IMPORT",
        "inputs": {
            "q79_single_higgs_channel_projection_certificate": rel(q79_single_path),
            "q79_zero_mode_dotD_interface_certificate": rel(q79_zero_mode_path),
            "sm_parity_matter_slot_readout": rel(sm_matter_slot_path),
            "H6C_boundary_route": rel(h6c_boundary_path),
        },
        "imported_projection": {
            "physical_doublet": q79_single["higgs_doublet_embedding"]["physical_doublet"],
            "hypercharge": q79_single["higgs_doublet_embedding"]["hypercharge"],
            "H_u": q79_single["higgs_doublet_embedding"]["H_u"],
            "H_d": q79_single["higgs_doublet_embedding"]["H_d"],
            "single_higgs_channel_projection": q79_single["closed"]["single_higgs_channel_projection"],
            "two_independent_low_energy_higgs_alignment_references": q79_single["closed"]["two_independent_low_energy_higgs_alignment_references"],
        },
        "what_this_closes_for_H6D": {
            "which_low_energy_Higgs_doublet": True,
            "H_u_H_d_channel_conjugation": True,
            "no_second_low_energy_alignment_mode_as_flavor_knob": True,
            "SM_hypercharge_neutrality_of_Yukawa_channels": True,
        },
        "what_this_does_not_close_for_H6D": {
            "UV_two_Higgs_VEV_ratio": True,
            "selected_beta_or_tan_beta": True,
            "selected_Dterm_projection_angle": True,
            "Higgs_VEV_or_mass_prediction": q79_single["open"]["higgs_mass_and_vev_prediction"],
            "RG_threshold_matching": q79_single["open"]["rg_threshold_matching"],
            "Higgs_internal_representative_and_dotD_H": q79_zero_mode["closed_inputs"]["single_higgs_projection"]["limitation"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    beta_source_candidates = [
        {
            "id": "theta_execution_tan_beta_10",
            "candidate_value": tan_beta_example,
            "classification": "REPRESENTATIVE_EXAMPLE_NOT_SELECTED_SOURCE",
            "accepted_as_source": False,
            "reason": "The Theta execution text says representative choice; H6C already marks it not selected by MTT.",
            "would_add_Higgs_specific_parameter_if_used_now": True,
        },
        {
            "id": "q79_single_higgs_projection",
            "candidate_value": None,
            "classification": "LOW_ENERGY_CHANNEL_PROJECTION_ONLY",
            "accepted_as_source": False,
            "reason": "It selects H_u -> H and H_d -> H^dagger at low energy, but does not emit a UV two-Higgs VEV ratio or decoupling angle.",
            "would_add_Higgs_specific_parameter_if_used_now": False,
        },
        {
            "id": "SM_parity_matter_slot_dictionary",
            "candidate_value": None,
            "classification": "REPRESENTATION_CHANNEL_SUPPORT_ONLY",
            "accepted_as_source": False,
            "reason": "It records operator channels with H_u/H_d labels, but no beta/tan_beta source or two-Higgs mixing metric.",
            "would_add_Higgs_specific_parameter_if_used_now": False,
        },
        {
            "id": "single_universal_or_Higgs_primitive_beta",
            "candidate_value": None,
            "classification": "ALLOWED_ONLY_AS_EXPLICIT_NON_NO_KNOB_EXTENSION",
            "accepted_as_source": False,
            "reason": "A beta primitive may be declared only once, fixed before Higgs comparison, and reused unchanged; this would not be strict no-knob closure.",
            "would_add_Higgs_specific_parameter_if_used_now": True,
        },
    ]

    beta_source_test = {
        "schema": "MTTConstHiggs01H6DBetaOrProjectionAngleSourceTest.v1",
        "status": "NO_SELECTED_BETA_OR_TWO_HIGGS_PROJECTION_ANGLE_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-BETA-OR-PROJECTION-ANGLE-SOURCE-TEST",
        "candidate_sources": beta_source_candidates,
        "negative_result": {
            "selected_beta_or_tan_beta_source_found": False,
            "selected_two_Higgs_projection_angle_found": False,
            "representative_tan_beta_10_promoted": False,
            "single_higgs_projection_promoted_to_beta": False,
            "observed_Higgs_or_lambda_backsolve_used": False,
        },
        "diagnostic_not_source": {
            "tan_beta_example": tan_beta_example,
            "cos2beta_sq_example": cos2beta_sq_example,
            "corrected_lambda_over_8_same_gauge_diagnostic": h6c_boundary["diagnostic_replay_not_source"]["corrected_lambda_over_8_same_gauge_diagnostic"],
            "diagnostic_values_used_as_selector": False,
        },
        "superset_strategy": {
            "paths_compared": [
                "Theta representative tan_beta lane",
                "q79/NCG single-Higgs projection lane",
                "SM-parity matter-slot H_u/H_d lane",
                "explicit one-primitive beta lane",
            ],
            "locked_target": "selected beta/tan_beta or two-Higgs projection angle for D-term boundary",
            "paths_combined_as_free_parameters": False,
            "best_current_result": "single-Higgs projection is selected low-energy support; beta remains a UV matching datum and is not selected.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    dterm_contract = {
        "schema": "MTTConstHiggs01H6DDTermBoundaryAcceptanceContract.v1",
        "status": "DTERM_BOUNDARY_FORMULA_AND_LOW_ENERGY_HIGGS_PROJECTION_READY_BETA_SOURCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-DTERM-BOUNDARY-ACCEPTANCE-CONTRACT",
        "boundary_formula": {
            "potential_convention": "V(H)=-m^2 |H|^2 + lambda |H|^4",
            "formula": h6c_decision["route_B_boundary_matching"]["formula"],
            "standard_factor": h6c["standard_Dterm_boundary_formula_factor"],
            "old_factor_overhigh_by_two_under_standard_convention": h6c["old_factor_overhigh_by_two_under_standard_convention"],
        },
        "current_filled_fields": {
            "correct_formula_factor": True,
            "low_energy_single_Higgs_projection": True,
            "H_u_H_d_channel_conjugation": True,
            "selector_guardrail": h6b_contract["source_identity_exports"]["selector_guardrail"]["filled"],
            "source_boundary_no_measured_lambda": True,
        },
        "required_before_numeric_boundary_value": {
            "selected_gauge_boundary_values": {
                "filled": False,
                "source": rel(ew_b41_path),
                "current_status": "gauge/action normalization and RG/matching policy scaffolding exist, but physical anchor values remain open",
            },
            "selected_beta_or_two_Higgs_projection_angle": {
                "filled": False,
                "source": rel(BETA_SOURCE_TEST),
                "current_status": "no selected beta/tan_beta or two-Higgs projection angle found",
            },
            "matching_scale_policy": {
                "filled": False,
                "source": rel(ew_b41_path),
                "current_status": "mu_match and threshold scheme remain open/conditional",
            },
            "threshold_RG_transport": {
                "filled": False,
                "source": rel(ew_b41_path),
                "current_status": "precision transport policy exists as scaffolding, not closed Higgs boundary prediction",
            },
            "one_universal_metrology_or_action_primitive_if_needed": {
                "filled": False,
                "source": rel(ew_b42_path),
                "current_status": ew_b42["status"],
            },
        },
        "acceptance_after_H6D": {
            "Dterm_formula_ready": True,
            "low_energy_Higgs_channel_ready": True,
            "selected_Dterm_boundary_packet_closed": False,
            "DTerm_boundary_numeric_value_derived": False,
            "Higgs_quartic_numeric_value_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "forbidden_promotions": [
            "representative tan_beta=10 -> selected beta",
            "single-Higgs projection -> UV tan_beta value",
            "SM measured Higgs mass or lambda -> beta source",
            "SM-parity replay lambda -> no-knob Higgs quartic",
            "conditional one-primitive replay -> strict no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6DNextWork.v1",
        "status": "NEXT_WORKORDER_H6E_UV_TWO_HIGGS_OR_PRIMITIVE_POLICY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-SOURCE",
            "task": "Search for or construct a selected UV two-Higgs projection/decoupling packet that emits beta/tan_beta before Higgs comparison.",
        },
        "secondary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-PRIMITIVE-BETA-POLICY",
            "task": "If no theorem-derived beta exists, formalize whether beta is allowed as one explicit primitive, fixed once and not tuned to Higgs mass; keep this non-no-knob.",
        },
        "parallel_intrinsic_route": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-ACTUAL-H-SECTOR-ROW-PAYLOAD",
            "task": "Continue the intrinsic finite K_H^(4)[12,12,12,12] route as a separate possible no-beta path.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6DSelectedDTermBoundaryOrBetaSource",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE",
        "output_packets": {
            "single_higgs_projection_import": rel(SINGLE_HIGGS_IMPORT),
            "beta_or_projection_angle_source_test": rel(BETA_SOURCE_TEST),
            "dterm_boundary_acceptance_contract": rel(DTERM_CONTRACT),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6DSelectedDTermBoundaryOrBetaSourceTheorem",
            "proved": True,
            "statement": (
                "The selected q79/NCG single-Higgs projection closes the low-energy Higgs channel H_u -> H and H_d -> H^dagger, and the H6C D-term formula is fixed with the standard 1/8 factor. However, no current corpus or repo source emits a selected UV beta/tan_beta or two-Higgs projection angle. The representative tan_beta=10 value is not selected, and the single-Higgs projection may not be promoted to a UV VEV ratio. Therefore H6D builds the exact D-term boundary acceptance contract while leaving beta, gauge boundary, matching scale, threshold/RG transport, numerical lambda_H, and strict no-knob closure open."
            ),
        },
        "low_energy_single_Higgs_projection_imported": True,
        "Dterm_boundary_formula_ready": True,
        "standard_Dterm_boundary_formula_factor": "1/8",
        "selected_beta_or_tan_beta_source_found": False,
        "selected_two_Higgs_projection_angle_found": False,
        "representative_tan_beta_10_promoted": False,
        "selected_Dterm_boundary_packet_closed": False,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6E_UVTwoHiggsProjectionAngleSource_or_PrimitiveBetaPolicy_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6D_SelectedDTermBoundaryOrBetaSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "low_energy_single_Higgs_projection_imported": True,
        "Dterm_boundary_formula_ready": True,
        "standard_Dterm_boundary_formula_factor": "1/8",
        "selected_beta_or_tan_beta_source_found": False,
        "selected_two_Higgs_projection_angle_found": False,
        "representative_tan_beta_10_promoted": False,
        "selected_Dterm_boundary_packet_closed": False,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6D Selected DTerm Boundary Or Beta Source v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE`

## Result

```text
low-energy single-Higgs projection imported      True
D-term boundary formula ready                    True
standard boundary factor                         1/8
selected beta/tan_beta source                    False
selected two-Higgs projection angle              False
representative tan_beta=10 promoted              False
Higgs quartic numeric value                      False
strict no-knob Higgs closure                     False
```

## Theorem

H6D imports the selected q79/NCG single-Higgs projection:

```text
H_u -> H
H_d -> H^dagger
```

This closes the low-energy Higgs-channel identity, but it does not select a
UV two-Higgs VEV ratio.  Therefore the D-term boundary route is real but still
source-open:

```text
lambda = (g^2 + g'^2) cos^2(2 beta) / 8
```

The old `tan_beta=10` is kept as a diagnostic representative value only.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-SOURCE`

Parallel fallback:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-PRIMITIVE-BETA-POLICY`
"""

    for path, payload in [
        (SINGLE_HIGGS_IMPORT, single_higgs_import),
        (BETA_SOURCE_TEST, beta_source_test),
        (DTERM_CONTRACT, dterm_contract),
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
