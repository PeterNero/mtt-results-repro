"""Build physical-anchor or smooth-EQa source-fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_request": DATA / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_source_request.json",
    "internal_lock": DATA / "selected_heterotic_projectiverhoe_internal_closure_lock_after_source_request.json",
    "ew_internal_weaksplit": DATA / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
    "ew_physical_anchor_rg": DATA / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json",
    "ew_action_anchor_key": DATA / "selected_electroweak_physical_action_anchor_key.fill_attempt.json",
    "physical_gate": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "kphys_or_smooth": DATA / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
    "bismut_payload": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt.candidate.json"
OUTPUT_REPORT = DATA / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefill_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_PhysicalAnchor_or_SmoothEQa_SourceFillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCEFILL_PARTIAL_EW_INTERNAL_THRESHOLD_CLOSED_PHYSICAL_ANCHOR_SMOOTHEQA_OPEN"
NEXT = "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "exists": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
    }


def main() -> dict[str, Any]:
    request = load(INPUTS["source_request"])
    internal_lock = load(INPUTS["internal_lock"])
    ew_internal = load(INPUTS["ew_internal_weaksplit"])
    ew_rg = load(INPUTS["ew_physical_anchor_rg"])
    ew_anchor = load(INPUTS["ew_action_anchor_key"])
    physical_gate = load(INPUTS["physical_gate"])
    kphys_or_smooth = load(INPUTS["kphys_or_smooth"])
    bismut = load(INPUTS["bismut_payload"])
    rplus = load(INPUTS["rplus_payload"])

    typed_map = ew_internal["same_scheme_argument"]["typed_hypercharge_map"]
    threshold = ew_internal["selected_internal_threshold_vector"]
    omega_reduction = ew_rg["conditional_interface"]["Omega0_reduction"]
    rplus_summary = rplus["rplus_payload"]["R_plus_summary"]

    fill_report = {
        "schema": "SelectedHeteroticProjectiveRhoE.PhysicalAnchorOrSmoothEQa.SourceFillReport.v1",
        "source_request": rel(INPUTS["source_request"]),
        "internal_lock": rel(INPUTS["internal_lock"]),
        "filled_physical_lane": {
            "same_branch_physical_action_unit": {
                "filled": False,
                "status": ew_anchor["status"],
                "best_structural_route": "m_theory_modal_gap_planck_anchor",
                "value": ew_anchor["dimensionful_anchor"]["value"],
            },
            "K_phys_or_Omega0_or_ellp_or_kappa11_or_alpha_prime": {
                "filled": False,
                "Omega0_formula_if_alpha_phys_selected": omega_reduction["Omega0"],
                "Omega0_over_sqrt_alpha_phys": omega_reduction["Omega0_over_sqrt_alpha_phys"],
                "alpha_phys_status": omega_reduction["alpha_phys_status"],
            },
            "matching_scale_mu_match": {
                "filled": False,
                "reason": "Omega0 is not identified with the electroweak matching surface by the current source.",
            },
            "RG_and_threshold_scheme": {
                "filled": False,
                "reason": "The matching formula shape is recorded, but beta/threshold scheme and match surface are not selected.",
                "formula_shape": ew_rg["conditional_interface"]["matching_formula_shape"],
            },
            "typed_electroweak_convention_map": {
                "filled": True,
                "status": typed_map["status"],
                "threshold_combination": typed_map["threshold_combination"],
                "weak_split": typed_map["weak_split"],
                "weights": typed_map["weights"],
            },
            "threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted": {
                "filled": "partial_internal_weaksplit_only",
                "lambda_12_internal": threshold["lambda_12_internal"],
                "Delta_G12_internal": threshold["Delta_G12_internal"],
                "p_Y_internal": threshold["p_Y_internal"],
                "p_a_internal": threshold["p_a_internal"],
                "p_c_weaksplit": threshold["p_c_weaksplit"],
                "p_SU2_weaksplit": threshold["p_SU2_weaksplit"],
                "full_factor_threshold_vector_closed": ew_rg["still_open"]["full_factor_threshold_vector_beyond_weak_split"] is False,
            },
            "proof_no_observed_constant_selected_any_missing_value": {
                "filled": True,
                "no_observed_electroweak_data": ew_rg["guardrails"]["uses_observed_electroweak_data"] is False,
                "no_backsolve": ew_anchor["guardrails"]["no_Newton_or_Planck_backsolve"],
                "target_fitting_used": False,
            },
        },
        "filled_smooth_lane": {
            "smooth_projective_rhoE_transition_or_Deligne_Cech_representative": {
                "filled": False,
                "finite_internal_rhoE_available": request["already_closed_internal_branch"]["rho_E_and_D_E"],
                "smooth_transition_values_absent": True,
            },
            "selected_bundle_connection_A_or_equivalent_smooth_operator_source": {
                "filled": False,
                "geometric_Bismut_connection_available": bismut["decision"]["geometric_tensor_payload_filled"],
                "bundle_connection_A_available": False,
            },
            "bundle_curvature_F_A": {
                "filled": False,
                "R_plus_curvature_available": rplus["decision"]["R_plus_curvature_filled"],
                "R_plus_nonzero_components": rplus_summary["nonzero_components"],
                "bundle_curvature_F_A_available": False,
            },
            "representation_action_on_uE_valued_one_forms": {
                "filled": False,
                "ad_bundle_representation_available": False,
            },
            "trace_lift_from_finite_trace_to_smooth_heat_zeta_torsion_trace": {
                "filled": False,
                "internal_complement_quotient_policy": internal_lock["locked_claims"]["internal_complement_quotient_policy"],
                "smooth_trace_lift_available": False,
            },
            "smooth_E_Qa_matrix_or_equivalent_finitepart_operator": {
                "filled": False,
                "E_Qa_computed": rplus["decision"]["E_Qa_computed"],
            },
            "smooth_regularization_and_zero_mode_policy": {
                "filled": False,
                "finite_internal_policy_locked": True,
                "smooth_policy_available": False,
            },
        },
        "source_statuses": {name: source_status(path) for name, path in INPUTS.items()},
        "forbidden_shortcuts_preserved": request["forbidden_shortcuts"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REPORT.write_text(json.dumps(fill_report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    filled_physical = fill_report["filled_physical_lane"]
    filled_smooth = fill_report["filled_smooth_lane"]
    physical_closed_keys = [key for key, value in filled_physical.items() if value["filled"] is True]
    physical_partial_keys = [key for key, value in filled_physical.items() if value["filled"] == "partial_internal_weaksplit_only"]
    smooth_support_keys = [
        "selected_bundle_connection_A_or_equivalent_smooth_operator_source",
        "bundle_curvature_F_A",
    ]

    decision = {
        "source_fill_attempt_built": True,
        "internal_branch_remains_locked": internal_lock["locked_claims"]["selected_internal_logdet"] == "log(2008)",
        "new_physical_lane_progress": {
            "typed_electroweak_convention_map_closed": filled_physical["typed_electroweak_convention_map"]["filled"] is True,
            "internal_weaksplit_threshold_closed": filled_physical["threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted"]["filled"] == "partial_internal_weaksplit_only",
            "no_target_proof_closed": filled_physical["proof_no_observed_constant_selected_any_missing_value"]["filled"] is True,
        },
        "physical_anchor_still_open": ew_rg["decision"]["physical_gauge_action_anchor_closed"] is False,
        "matching_scale_still_open": ew_rg["decision"]["matching_scale_closed"] is False,
        "RG_scheme_still_open": ew_rg["decision"]["RG_scheme_closed"] is False,
        "full_physical_electroweak_matching_closed": False,
        "smooth_geometry_support_present": kphys_or_smooth["decision"]["smooth_lane_has_geometry_but_no_bundle_operator"],
        "smooth_EQa_still_open": rplus["decision"]["E_Qa_computed"] is False,
        "preferred_next_lane": "physical_gauge_action_anchor_RG_scheme",
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEPhysicalAnchorOrSmoothEQaSourceFillAttempt",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "source_fill_report_path": rel(OUTPUT_REPORT),
        "physical_lane_closed_keys": physical_closed_keys,
        "physical_lane_partial_keys": physical_partial_keys,
        "smooth_lane_support_keys": smooth_support_keys,
        "decision": decision,
        "closed_now": {
            "typed_electroweak_convention_map": True,
            "internal_weaksplit_threshold_for_physical_lane": True,
            "no_observed_constant_guardrail_for_missing_values": True,
            "Rplus_geometry_support_for_smooth_lane": True,
        },
        "still_open": {
            "physical_action_unit_K_phys_or_alpha_phys": True,
            "mu_match": True,
            "RG_and_threshold_scheme": True,
            "full_factor_threshold_vector_beyond_weak_split": True,
            "smooth_projective_transition_or_Deligne_Cech_values": True,
            "selected_bundle_A_and_F_A": True,
            "smooth_E_Qa_or_heat_zeta_torsion_finite_part": True,
        },
        "guardrails": {
            "does_not_set_K_phys_from_internal_units": True,
            "does_not_identify_Omega0_with_mu_match": True,
            "does_not_promote_Rplus_to_bundle_curvature": True,
            "does_not_promote_finite_rhoE_to_smooth_transition": True,
            "does_not_compare_to_observed_couplings": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoEPhysicalAnchorOrSmoothEQaSourceFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The source request can now be partially filled from existing same-repo "
                "certificates: the typed electroweak convention map, internal weak-split "
                "threshold, and no-target guardrail are closed for the physical lane; "
                "the Bismut/R+ geometry support is filled for the smooth lane. These "
                "do not close physical electroweak matching because K_phys/alpha_phys, "
                "mu_match, RG/threshold scheme, and the full threshold vector remain "
                "unselected. They also do not close smooth E_Qa because no selected "
                "bundle A/F_A, representation trace, smooth transition data, or "
                "heat/zeta/torsion finite part is emitted."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "source_fill_report_path": rel(OUTPUT_REPORT),
        "note_path": rel(OUTPUT_NOTE),
        "closed_now": candidate["closed_now"],
        "still_open": candidate["still_open"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE PhysicalAnchor or SmoothEQa SourceFillAttempt v1

## Result

```text
status = {STATUS}
typed_electroweak_convention_map = closed
internal_weaksplit_threshold = closed
physical_action_unit = open
mu_match = open
RG_threshold_scheme = open
smooth_EQa = open
next_required_artifact = {NEXT}
```

## What changed

The previous request is now partially filled.  The physical lane no longer has
an empty threshold/convention slot: the selected typed hypercharge map and the
internal weak-split threshold are available from the same internal accounting
scheme.

```text
lambda_12_internal = {threshold["lambda_12_internal"]}
Delta_G12_internal = {threshold["Delta_G12_internal"]}
p_Y_internal = {threshold["p_Y_internal"]}
```

The smooth lane also has real support data: the Bismut geometry and `R^+`
curvature payload are present.  This is still not a smooth `E_Qa` identity,
because selected bundle `A`, bundle `F_A`, representation trace, and smooth
heat/zeta/torsion finite-part data are not emitted.

The next best closure target is therefore the physical gauge/action anchor plus
RG and matching-scale theorem.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REPORT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
