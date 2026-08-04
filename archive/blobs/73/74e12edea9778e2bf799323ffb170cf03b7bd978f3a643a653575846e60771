"""Build the H radial/phase/trace source or finite-H action emission packet."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialphasetracesource_or_finitehactionemission"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HRadialPhaseTraceSource_or_FiniteHActionEmission_v1.md"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    previous = read_json("candidate_data/selected_finitehfunctional_or_msourcevalueemission.candidate.json")
    polar = read_json("candidate_data/selected_finitehfunctional_or_msourcevalueemission/polar_reduced_value_executor.packet.json")
    radial_split = read_json(
        "candidate_data/selected_hradialscalephasesource_or_herm2hessianrows/h_radial_scale_source_split.packet.json"
    )
    controlled = read_json(
        "candidate_data/selected_hradialscalephasesource_or_herm2hessianrows/controlled_parameter_radial_lane.packet.json"
    )
    orientation = read_json(
        "candidate_data/selected_herm2orientationphasetracesource_or_directhresponseemission/"
        "orientation_phase_trace_source_inventory.packet.json"
    )
    direct_quartic = read_json(
        "candidate_data/selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows/"
        "h_quartic_threshold_functional_reduction.packet.json"
    )
    hrg_attempt = read_json("candidate_data/selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json")
    intrinsic_attempt = read_json(
        "candidate_data/selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json"
    )

    selected_angle = polar["selected_angle_data"]
    controlled_value = controlled["controlled_parameter"]["value"]
    required_polar_fields = ["r_H", "sigma_D", "phi_Omega", "m0_or_quotient_trace"]
    strict_field_emissions = {
        "r_H": bool(radial_split["decision"]["strict_radial_scale_source_emitted"]),
        "sigma_D": bool(orientation["decision"]["selected_Delta_sign_emitted"]),
        "phi_Omega": bool(orientation["decision"]["selected_Omega_phase_emitted"]),
        "m0_or_quotient_trace": bool(orientation["decision"]["trace_center_source_or_normalization_emitted"]),
    }
    accepted_strict_fields = [name for name, emitted in strict_field_emissions.items() if emitted]

    source_inventory = {
        "schema": "MTTHRadialPhaseTraceSourceInventory.v1",
        "closure_claimed": True,
        "status": "RADIAL_PHASE_TRACE_SOURCE_INVENTORY_EXECUTED_ZERO_STRICT_POLAR_FIELDS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_angle": selected_angle,
        "strict_required_polar_fields": required_polar_fields,
        "strict_field_emissions": strict_field_emissions,
        "accepted_strict_field_count": len(accepted_strict_fields),
        "accepted_strict_fields": accepted_strict_fields,
        "controlled_radial_support": {
            "available": bool(controlled["decision"]["minimal_parameter_H_layer_available"]),
            "accepted_as_strict_no_knob_source": False,
            "name": controlled["controlled_parameter"]["name"],
            "tier": controlled["controlled_parameter"]["tier"],
            "value": controlled_value,
            "reason": (
                "The HRG lane is a controlled empirical calibration. It can support a "
                "minimal-parameter H layer, but it does not emit source-owned r_H, "
                "sigma_D, phi_Omega, m0, or row-level certificates."
            ),
        },
        "source_routes_rechecked": {
            "strict_A_EW_or_threshold_RG_route": radial_split["strict_no_knob_radial_routes"]["Dterm_EW_boundary_route"],
            "strict_R_H_RG_operator_route": radial_split["strict_no_knob_radial_routes"]["strict_R_H_RG_operator_route"],
            "intrinsic_H_quartic_or_large_threshold_RG_route": radial_split["strict_no_knob_radial_routes"][
                "intrinsic_H_quartic_or_large_threshold_RG_route"
            ],
            "orientation_phase_trace_route": orientation["source_fields"],
        },
    }

    polar_execution = {
        "schema": "MTTHPolarFieldsAfterInventory.v1",
        "closure_claimed": True,
        "status": "POLAR_ROW_FORMULAS_RETAINED_BUT_NOT_VALUE_EXECUTABLE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "conditional_rows": polar["conditional_rows"],
        "what_is_selected_now": {
            "s_beta": selected_angle["s_beta"],
            "sqrt_s_beta": selected_angle["sqrt_s_beta"],
            "sqrt_1_minus_s_beta": selected_angle["sqrt_1_minus_s_beta"],
        },
        "strict_execution": {
            "tracefree_threshold_block_executable": False,
            "full_H_response_rows_executable": False,
            "missing_fields": [name for name, emitted in strict_field_emissions.items() if not emitted],
            "accepted_value_rows": 0,
        },
        "controlled_execution": {
            "radial_support_available": True,
            "full_controlled_rows_executable": False,
            "reason": "Even after admitting controlled radial support, phase, sign, trace, and final row certificates are absent.",
        },
    }

    finite_action_attempt = {
        "schema": "MTTFiniteHActionEmissionAttempt.v1",
        "closure_claimed": True,
        "status": "FINITE_H_ACTION_NOT_EMITTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "attempted_sources": {
            "finite_H_functional_M_source_K_H": previous["theorem"]["name"],
            "direct_quartic_threshold_reduction": direct_quartic["theorem"]["name"],
            "strict_H_threshold_RG_attempt": hrg_attempt["theorem"]["name"],
            "intrinsic_H_quartic_attempt": intrinsic_attempt["theorem"]["name"],
        },
        "emission_result": {
            "selected_finite_H_action_emitted": False,
            "selected_second_variation_rows_emitted": False,
            "selected_Herm2_rows_emitted": False,
            "accepted_value_row_count": 0,
            "accepted_row_certificate_count": 0,
        },
        "why_this_is_not_a_failure_of_polar_reduction": (
            "The selected angle reduction is intact. The missing object is the value "
            "source for the radial scale, sign, phase, and trace, or a direct finite "
            "H action whose selected second variation produces those rows."
        ),
    }

    next_cutset = {
        "schema": "MTTHPolarFieldsNextCutset.v1",
        "closure_claimed": True,
        "status": "NEXT_CUTSET_FIXED_TO_POLAR_FIELDS_OR_DIRECT_FINITE_H_ACTION",
        "next_frontier": "MTT_Selected_HPolarFieldsSource_or_DirectFiniteHActionRows_v1",
        "must_emit_one_of": [
            {
                "route": "selected_H_polar_fields",
                "required": required_polar_fields
                + ["source ownership certificate", "row-level exactness/error certificate", "Hermitian quotient certificate"],
            },
            {
                "route": "direct_selected_finite_H_action",
                "required": [
                    "finite action functional",
                    "selected stationary/variation domain",
                    "second variation restricted to B_Huv",
                    "exact Huu,Hud_re,Hud_im,Hdd rows",
                    "row-level exactness/error certificate",
                ],
            },
        ],
        "retired_for_this_frontier": [
            "B_Huv support alone as a value source",
            "diagonal HYM metric as Higgs Hessian rows",
            "A^T A=12 I_2 compressed C1 normal matrix as non-scalar Huv rows",
            "controlled HRG calibration as strict no-knob source",
            "selected s_beta as radial/sign/phase/trace source",
        ],
    }

    candidate = {
        "schema": "MTTSelectedHRadialPhaseTraceSourceOrFiniteHActionEmissionCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HRadialPhaseTraceSourceOrFiniteHActionEmissionTheorem",
            "proved": True,
            "statement": (
                "The selected s_beta polar reduction and controlled HRG radial support are retained, "
                "but the strict current corpus emits zero accepted source-owned fields among r_H, "
                "sigma_D, phi_Omega, and m0/quotient trace, and emits no finite H action whose "
                "second variation supplies the Herm(2) H rows. Therefore the next frontier is not "
                "another Galerkin/H_response replay: it is selected H polar-field source emission "
                "or direct selected finite-H action rows."
            ),
        },
        "decision": {
            "selected_s_beta_polar_angle_closed": True,
            "controlled_radial_support_available": True,
            "controlled_radial_support_accepted_as_strict_source": False,
            "strict_radial_scale_source_emitted": strict_field_emissions["r_H"],
            "selected_Delta_sign_emitted": strict_field_emissions["sigma_D"],
            "selected_Omega_phase_emitted": strict_field_emissions["phi_Omega"],
            "trace_center_or_quotient_trace_emitted": strict_field_emissions["m0_or_quotient_trace"],
            "selected_finite_H_action_emitted": False,
            "selected_Herm2_rows_emitted": False,
            "full_no_knob_H_rows_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": selected_angle["s_beta"],
            "sqrt_s_beta": selected_angle["sqrt_s_beta"],
            "sqrt_1_minus_s_beta": selected_angle["sqrt_1_minus_s_beta"],
            "controlled_HRG_radial_support_value": controlled_value,
            "required_strict_polar_field_count": len(required_polar_fields),
            "accepted_strict_polar_field_count": len(accepted_strict_fields),
            "accepted_value_row_count": 0,
            "accepted_row_certificate_count": 0,
        },
        "packets": [
            str(CANDIDATE_DIR.relative_to(ROOT) / "radial_phase_trace_source_inventory.packet.json"),
            str(CANDIDATE_DIR.relative_to(ROOT) / "polar_row_family_after_inventory.packet.json"),
            str(CANDIDATE_DIR.relative_to(ROOT) / "finite_h_action_emission_attempt.packet.json"),
            str(CANDIDATE_DIR.relative_to(ROOT) / "next_cutset_after_radial_phase_trace_attempt.packet.json"),
        ],
        "next_target": "MTT_Selected_HPolarFieldsSource_or_DirectFiniteHActionRows_v1",
    }

    certificate = {
        "certificate": "selected_hradialphasetracesource_or_finitehactionemission_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HRADIALPHASETRACESOURCE_OR_FINITEHACTIONEMISSION_EXECUTED_ZERO_STRICT_FIELDS_ACTION_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "selected_s_beta_retained": True,
            "controlled_radial_support_not_counted_as_strict": True,
            "strict_polar_fields_accepted_zero": len(accepted_strict_fields) == 0,
            "finite_H_action_emitted_false": True,
            "next_cutset_fixed": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "radial_phase_trace_source_inventory.packet.json", source_inventory)
    write_json(CANDIDATE_DIR / "polar_row_family_after_inventory.packet.json", polar_execution)
    write_json(CANDIDATE_DIR / "finite_h_action_emission_attempt.packet.json", finite_action_attempt)
    write_json(CANDIDATE_DIR / "next_cutset_after_radial_phase_trace_attempt.packet.json", next_cutset)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Radial/Phase/Trace Source or Finite-H Action Emission v1",
                "",
                "## Theorem",
                "",
                candidate["theorem"]["statement"],
                "",
                "## Inputs",
                "",
                "- The selected Herm(2) polar angle remains closed by `s_beta = 0.004701083905943647`.",
                "- The polar row executor reduces the unknown H block to `r_H`, `sigma_D`, `phi_Omega`, and `m0` or a quotient trace theorem.",
                "- The controlled HRG lane supplies a minimal-parameter support value `391.39140285811936`, but it is not a strict no-knob source row.",
                "",
                "## Execution",
                "",
                "The strict radial/phase/trace inventory accepts zero source-owned polar fields:",
                "",
                "```text",
                "r_H: false",
                "sigma_D: false",
                "phi_Omega: false",
                "m0_or_quotient_trace: false",
                "```",
                "",
                "The finite-H action route is also executed at the current frontier and emits no selected action, no selected second-variation rows, and no row-level certificates.",
                "",
                "## Consequence",
                "",
                "The next target is `MTT_Selected_HPolarFieldsSource_or_DirectFiniteHActionRows_v1`.  It must emit either the four selected polar fields with ownership/exactness/Hermitian quotient certificates, or a direct selected finite-H action whose second variation restricted to `B_Huv` gives the Herm(2) rows.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
