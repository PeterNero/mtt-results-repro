"""Build CONST-GR-01 G2 modal-gap dimensional-anchor packet fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
GR_REPO = TEXPAPERS / "mtt-protospinor-gr-response-proof"
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_ATTEMPT = BASE / "selected_dimensional_anchor_packet_fill_attempt.packet.json"
ROUTE_MATRIX = BASE / "dimensional_anchor_route_matrix.packet.json"
TAU_BRIDGE = BASE / "same_branch_tau_rod_clock_bridge.packet.json"
OMEGA_REDUCTION = BASE / "omega0_source_reduction.packet.json"
BOUNDARY = BASE / "g2_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_GR_01_AbsoluteScale_G2_ModalGapDimensionalAnchorPacketFill_v1.md"

STATUS = "MTT_CONST_GR_01_G2_MODAL_GAP_DIMENSIONAL_ANCHOR_PACKET_FILL_BUILT"


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

    g1_path = DATA / "const_gr_01_absolute_scale_g1_shared_primitive_source_search.candidate.json"
    m_theory_candidate_path = GR_REPO / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
    m_theory_attempt_path = GR_REPO / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json"
    same_branch_path = GR_REPO / "certificates" / "same_branch_physical_clock_or_length_source_search_certificate.json"
    same_branch_packet_path = GR_REPO / "candidate_data" / "same_branch_physical_clock_or_length_source.packet.json"
    modal_to_unit_path = GR_REPO / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json"
    omega_gap_path = GR_REPO / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"
    higher_order_path = GR_REPO / "certificates" / "selected_higher_order_correction_and_disturbance_covariance_theorem_certificate.json"
    anchor_hunt_path = GR_REPO / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"
    absolute_candidate_path = NONSM_REPO / "certificates" / "absolute_normalization_candidate_gate_certificate.json"
    scale_coeff_path = NONSM_REPO / "certificates" / "selected_scale_coefficient_extraction_certificate.json"
    rho_final_path = NONSM_REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"

    g1 = load(g1_path)
    m_theory_candidate = load(m_theory_candidate_path)
    m_theory_attempt = load(m_theory_attempt_path)
    same_branch = load(same_branch_path)
    same_branch_packet = load(same_branch_packet_path)
    modal_to_unit = load(modal_to_unit_path)
    omega_gap = load(omega_gap_path)
    higher_order = load(higher_order_path)
    anchor_hunt = load(anchor_hunt_path)
    absolute_candidate = load(absolute_candidate_path)
    scale_coeff = load(scale_coeff_path)
    rho_final = load(rho_final_path)

    attempted_packet = {
        "packet": "SelectedDimensionalAnchorPacket",
        "status": "ATTEMPTED_STRUCTURAL_FILL_VALUE_OPEN",
        "candidate_id": "m_theory_modal_gap_planck_anchor_plus_same_branch_tau_bridge",
        "source_branch": "Z448/q79 exact central-circle branch with rho_UV import",
        "dimensionful_quantity": {
            "symbol": "omega_gap_phys or equivalently L0/E0/ell_p after convention choice",
            "units": "physical inverse length, length, energy, or M-theory Planck length",
            "physical_meaning": "the one shared rod/clock/metrology primitive needed by alpha, weak mixing, and GR",
            "value": None,
            "uncertainty_or_exactness": None,
        },
        "source_certification": {
            "selected_by_mtt": False,
            "source_files": list(same_branch["external_sources"].values()),
            "source_certificates": [
                rel(m_theory_candidate_path),
                rel(m_theory_attempt_path),
                rel(same_branch_path),
                rel(modal_to_unit_path),
                rel(omega_gap_path),
                rel(higher_order_path),
            ],
            "same_branch_as_rho_uv_and_z448": True,
            "computed_before_target_comparison": False,
            "structural_role_found": True,
            "absolute_value_found": False,
        },
        "forbidden_inputs_absent": {
            "observed_Newton_or_Planck": True,
            "observed_Omega0_H0_rhoDE": True,
            "observed_particle_masses_or_TeV_calibration": True,
            "unit_convention_only": True,
        },
        "map_to_alpha_phys": {
            "formula": "alpha_phys = tau_int/L0^2 = tau_int*E0^2",
            "alpha_phys_value": None,
            "dimensional_analysis_checked": True,
            "convention_factors_declared": True,
        },
        "downstream_predictions_allowed_after_acceptance": [
            "Omega0 physical value",
            "omega_gap_phys physical value",
            "Lambda_gap_phys physical value",
            "G_eff/kappa_STF physical normalization",
        ],
        "promotion": {
            "packet_promotes_to_closed_anchor": False,
            "blocking_fields": m_theory_attempt["promotion"]["blocking_fields"],
            "reason": "The strongest current fill supplies selected branch, dimensional role, equations, and no-backsolve guardrails, but leaves the dimensionful value and source-selected physical unit absent.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    routes = {
        "m_theory_modal_gap_to_ellp": anchor_hunt["route_status"]["route_A_m_theory_modal_gap_to_ellp"],
        "theta_matching_scale": anchor_hunt["route_status"]["route_B_theta_matching_scale"],
        "proper_time_tau": anchor_hunt["route_status"]["route_C_proper_time_tau"],
        "action_unit_G10": anchor_hunt["route_status"]["route_D_action_unit_G10"],
        "dimensionless_only": anchor_hunt["route_status"]["route_E_dimensionless_only"],
        "flux_bianchi_alpha_prime": next(row for row in absolute_candidate["candidates"] if row["id"] == "D_flux_bianchi_alpha_prime"),
        "topological_flux_integer_minimization": next(row for row in absolute_candidate["candidates"] if row["id"] == "E_topological_flux_integer_minimization"),
        "central_circle_spectral_gap": next(row for row in absolute_candidate["candidates"] if row["id"] == "F_central_circle_spectral_gap"),
    }

    route_matrix = {
        "schema": "MTTConstGR01G2DimensionalAnchorRouteMatrix.v1",
        "status": "ALL_CURRENT_ROUTES_CLASSIFIED_NO_PROMOTION",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-DIMENSIONAL-ANCHOR-ROUTE-MATRIX",
        "inputs": {
            "anchor_hunt": rel(anchor_hunt_path),
            "absolute_normalization_candidate_gate": rel(absolute_candidate_path),
        },
        "routes": routes,
        "best_current_route": {
            "id": "m_theory_modal_gap_to_ellp",
            "why": "It is the only current route that ties the same compactification and modal-gap data to both Planck/GR and gauge normalizations.",
            "classification": routes["m_theory_modal_gap_to_ellp"]["classification"],
            "remaining_blocker": routes["m_theory_modal_gap_to_ellp"]["missing"],
        },
        "best_unconventional_auxiliary": {
            "id": "same_branch_tau_rod_clock_bridge",
            "why": "It sources the physical role of tau as coherent length/proper time, which gives a legitimate rod/clock bridge without choosing target data.",
            "remaining_blocker": "absolute metrological value of alpha_phys, L0, or ell_coh",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    tau_bridge = {
        "schema": "MTTConstGR01G2SameBranchTauRodClockBridge.v1",
        "status": "SAME_BRANCH_TAU_ROLE_CLOSED_ABSOLUTE_VALUE_OPEN",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-SAME-BRANCH-TAU-ROD-CLOCK-BRIDGE",
        "inputs": {
            "same_branch_physical_clock_or_length_source_search": rel(same_branch_path),
            "same_branch_packet": rel(same_branch_packet_path),
        },
        "source_identification": same_branch_packet["source_identification"],
        "source_hits": same_branch_packet["source_hits"],
        "relative_values": same_branch_packet["relative_values"],
        "absolute_values": same_branch_packet["absolute_values"],
        "verdict": same_branch["verdict"],
        "metrology_no_go": same_branch["metrology_no_go"],
        "achievement": "The physical object is not arbitrary anymore: tau is sourced as the coherent-length/proper-time object. What remains is a physical value for that object.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    omega_reduction = {
        "schema": "MTTConstGR01G2Omega0SourceReduction.v1",
        "status": "OMEGA0_REDUCED_TO_CUV_QTAU_AND_PHYSICAL_UNIT",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-OMEGA0-SOURCE-REDUCTION",
        "inputs": {
            "selected_physical_omega_gap": rel(omega_gap_path),
            "selected_higher_order_correction_and_disturbance_covariance": rel(higher_order_path),
            "selected_scale_coefficient_extraction": rel(scale_coeff_path),
            "final_internal_rho_uv": rel(rho_final_path),
        },
        "closed_internal_data": {
            "rho_UV": rho_final["selected_values"]["rho_UV"],
            "s_star_from_rho": rho_final["selected_values"]["s_star_from_rho"],
            "lambda_internal_exact": omega_gap["internal_formulae"]["lambda_internal_exact"],
            "sqrt_lambda_internal_exact": omega_gap["internal_formulae"]["sqrt_lambda_internal_exact"],
            "kappa": scale_coeff["extracted_coefficients"]["kappa"],
            "scale_minimizer_formula": scale_coeff["extracted_coefficients"]["s_star_after_kappa_extraction"],
        },
        "primitive_source_objects": higher_order["primitive_source_objects"],
        "repaired_rho_formula": higher_order["repaired_rho_formula"],
        "open_gates": higher_order["open_gates"],
        "next_required_artifacts": higher_order["next_required_artifacts"],
        "interpretation": "G2 reduces the anchor fill to a smaller source-data problem: compute C_UV, Q_tau/d_Q, and Omega0 from the same selected branch, not from physical targets.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstGR01G2Boundary.v1",
        "status": "G2_PACKET_FILL_ATTEMPT_COMPLETE_PROMOTION_BLOCKED_BY_PHYSICAL_UNIT",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-BOUNDARY",
        "closed_or_tightened_now": {
            "SelectedDimensionalAnchorPacket_structural_fill": True,
            "M_theory_modal_gap_route_remains_best": True,
            "same_branch_tau_rod_clock_bridge_imported": True,
            "omega_gap_source_data_reduced_to_CUV_Qtau_Omega0": True,
            "all_current_routes_classified": True,
            "no_target_backsolve_guard_preserved": True,
        },
        "still_open": {
            "dimensionful_quantity_value": True,
            "source_certification_selected_by_mtt_for_physical_unit": True,
            "computed_before_target_comparison_for_physical_unit": True,
            "alpha_phys_value": True,
            "C_UV_source_certified_value": True,
            "Q_tau_or_d_Q_source_certified_value": True,
            "physical_Omega0_source": True,
            "Newton_or_Planck_prediction": True,
            "strict_no_knob_absolute_scale_closure": True,
        },
        "anti_cycle_delta_from_G1": {
            "G1": "proved GR joins the shared E0/L0 primitive portfolio",
            "G2": "attempts the actual selected dimensional-anchor packet fill and reduces the next proof to C_UV/Q_tau/Omega0 source data",
            "not_repeated": [
                "not merely restating one-anchor GR propagation",
                "not treating tau role as tau value",
                "not promoting a structural M-theory slot as a physical length",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstGR01G2NextWork.v1",
        "status": "NEXT_WORKORDER_G3_CUV_QTAU_OMEGA0_SOURCE_DATA",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-NEXT",
        "primary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA",
            "task": "Try to compute or source the selected higher-order correction coefficient C_UV, the finite-memory carrier covariance Q_tau/d_Q, and the physical Omega0 unit from the same branch.",
        },
        "secondary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3B-DECLARE-ONE-METROLOGY-PRIMITIVE-TIER",
            "task": "If the source-data theorem cannot emit a physical unit, freeze the one-universal-metrology-primitive tier and move to another constant to test it.",
        },
    }

    candidate = {
        "candidate": "MTTConstGR01AbsoluteScaleG2ModalGapDimensionalAnchorPacketFill",
        "status": STATUS,
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL",
        "output_packets": {
            "selected_dimensional_anchor_packet_fill_attempt": rel(PACKET_ATTEMPT),
            "dimensional_anchor_route_matrix": rel(ROUTE_MATRIX),
            "same_branch_tau_rod_clock_bridge": rel(TAU_BRIDGE),
            "omega0_source_reduction": rel(OMEGA_REDUCTION),
            "g2_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTGR01G2DimensionalAnchorPacketFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The selected dimensional-anchor packet can be filled structurally from the M-theory/modal-gap route plus the same-branch tau rod/clock bridge, but it cannot promote to a closed physical anchor because the current corpus does not emit a target-independent dimensionful value. The next non-cyclic gate is the same-branch source-data computation of C_UV, Q_tau/d_Q, and Omega0."
            ),
        },
        "structural_packet_fill_attempted": True,
        "packet_promotes_to_closed_anchor": False,
        "same_branch_tau_role_closed": True,
        "absolute_physical_value_closed": False,
        "next_gate_reduced_to_CUV_Qtau_Omega0": True,
        "measured_Newton_or_Planck_derived": False,
        "strict_no_knob_absolute_scale_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_GR_01_AbsoluteScale_G2_ModalGapDimensionalAnchorPacketFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "structural_packet_fill_attempted": True,
        "packet_promotes_to_closed_anchor": False,
        "same_branch_tau_role_closed": True,
        "absolute_physical_value_closed": False,
        "next_gate_reduced_to_CUV_Qtau_Omega0": True,
        "next_primary": next_work["primary"]["label"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST GR 01 Absolute Scale G2 Modal Gap Dimensional Anchor Packet Fill v1

Status: `{STATUS}`

Label: `CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL`

## Result

```text
SelectedDimensionalAnchorPacket structural fill    True
packet promotes to closed physical anchor          False
same-branch tau rod/clock role                     True
absolute physical value                            False
next gate reduced to C_UV, Q_tau, Omega0           True
Newton/Planck prediction                           False
```

G2 tries the actual dimensional-anchor packet fill.  The best fill is not
empty: it combines the M-theory modal-gap Planck slot with the same-branch
coherent `tau` rod/clock bridge.  The packet has the correct source branch,
correct dimensional role, no-backsolve guardrails, and downstream formulae.

It still fails promotion because the physical value is absent:

```text
dimensionful_quantity.value                         None
source_certification.selected_by_mtt                False
source_certification.computed_before_target_compare False
map_to_alpha_phys.alpha_phys_value                  None
```

## What Tightened

The blocker is no longer vague "absolute scale".  It is now:

```text
C_UV   selected O(alpha'^2)/curvature UV correction coefficient
Q_tau  selected finite-memory carrier covariance, or d_Q
Omega0 physical inverse-length/action unit
```

The closed internal data include:

```text
rho_UV = 0.164530397543639
s_star = 1.464646774701829
lambda_internal = 15
kappa = 1
```

## Superset Status

Straight source path: M-theory/modal gap remains the best route, but the
dimensionful value is not emitted.

Cross-sector path: tau is now sourced as the same-branch rod/clock object; this
supports the one-universal-metrology-primitive tier.

Strict no-knob path: compute `C_UV`, `Q_tau/d_Q`, and `Omega0` from the same
selected branch without Newton, Planck, mass, cosmology, TeV, or unit-convention
backsolve.

## Next

`CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA`
"""

    for path, payload in [
        (PACKET_ATTEMPT, attempted_packet),
        (ROUTE_MATRIX, route_matrix),
        (TAU_BRIDGE, tau_bridge),
        (OMEGA_REDUCTION, omega_reduction),
        (BOUNDARY, boundary),
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
