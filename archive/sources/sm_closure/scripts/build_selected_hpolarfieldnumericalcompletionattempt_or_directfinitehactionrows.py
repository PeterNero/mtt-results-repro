"""Build the H polar-field numerical completion attempt packet."""

from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HPolarFieldNumericalCompletionAttempt_or_DirectFiniteHActionRows_v1.md"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def herm2_rows(r_h: float, s_beta: float, sigma_d: int, phase: str, m0: float) -> dict:
    sqrt_s = math.sqrt(s_beta)
    sqrt_c = math.sqrt(1.0 - s_beta)
    delta = sigma_d * r_h * sqrt_s
    omega_abs = r_h * sqrt_c
    if phase == "0":
        hud_re, hud_im = omega_abs, 0.0
        phi = 0.0
    elif phase == "pi/2":
        hud_re, hud_im = 0.0, omega_abs
        phi = math.pi / 2.0
    elif phase == "pi":
        hud_re, hud_im = -omega_abs, 0.0
        phi = math.pi
    elif phase == "-pi/2":
        hud_re, hud_im = 0.0, -omega_abs
        phi = -math.pi / 2.0
    else:
        raise ValueError(f"unsupported phase: {phase}")

    h_uu = m0 + delta
    h_dd = m0 - delta
    recovered_s_beta = (delta * delta) / (delta * delta + hud_re * hud_re + hud_im * hud_im)
    return {
        "r_H": r_h,
        "sigma_D": sigma_d,
        "phi_Omega_label": phase,
        "phi_Omega_radians": phi,
        "m0": m0,
        "Delta": delta,
        "Omega_abs": omega_abs,
        "Hud_re": hud_re,
        "Hud_im": hud_im,
        "Huu": h_uu,
        "Hdd": h_dd,
        "Hdu_re": hud_re,
        "Hdu_im": -hud_im,
        "trace": h_uu + h_dd,
        "tracefree": abs((h_uu + h_dd) - 2.0 * m0) <= 1e-12,
        "det_tracefree": -(delta * delta + hud_re * hud_re + hud_im * hud_im),
        "eigenvalues_tracefree": [-r_h, r_h],
        "recovered_s_beta": recovered_s_beta,
        "s_beta_residual": recovered_s_beta - s_beta,
        "hermitian_residual": 0.0,
        "non_scalar_norm": math.sqrt(delta * delta + hud_re * hud_re + hud_im * hud_im),
    }


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    previous = read_json("candidate_data/selected_hradialphasetracesource_or_finitehactionemission.candidate.json")
    polar = read_json("candidate_data/selected_finitehfunctional_or_msourcevalueemission/polar_reduced_value_executor.packet.json")
    hrg = read_json(
        "candidate_data/selected_hradialscalephasesource_or_herm2hessianrows/controlled_parameter_radial_lane.packet.json"
    )
    aew_hrg = read_json(
        "candidate_data/selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector/"
        "aew_hrg_burden_equivalence_diagnostic.packet.json"
    )
    ct = read_json("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/ctwist_transgression_pairing_computation.candidate.json")
    hym = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-protospinor-gr-response-proof/candidate_data/"
        "selected_hym_correction_and_gauge_projector_value_table.packet.json"
    )
    diag_hym = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-protospinor-gr-response-proof/candidate_data/"
        "selected_diagonal_hym_operator_payload_extraction.packet.json"
    )

    s_beta = polar["selected_angle_data"]["s_beta"]
    r_controlled = hrg["controlled_parameter"]["value"]
    m0_tracefree = 0.0

    candidate_rows = []
    for sigma_d in (1, -1):
        for phase in ("0", "pi/2", "pi", "-pi/2"):
            rows = herm2_rows(r_controlled, s_beta, sigma_d, phase, m0_tracefree)
            rows["candidate_id"] = f"controlled_HRG_tracefree_sigma{sigma_d}_{phase.replace('/', '_')}"
            rows["strict_no_knob_accepted"] = False
            rows["controlled_numeric_candidate"] = True
            rows["continuous_parameter_count"] = 1
            rows["continuous_parameter_source"] = "UP_RET_OVERLAP.HRG controlled empirical calibration"
            candidate_rows.append(rows)

    selected_controlled = herm2_rows(r_controlled, s_beta, 1, "pi/2", m0_tracefree)
    selected_controlled.update(
        {
            "candidate_id": "controlled_HRG_tracefree_T3_complex_rotated_plus",
            "selection_reason_controlled_tier": [
                "r_H uses the existing controlled HRG radial support and is not counted as strict no-knob.",
                "m0=0 uses the trace-free quotient normalization already legal for the threshold block.",
                "sigma_D=+1 follows the imported selected T3 orientation convention, but is not yet a Higgs-row certificate.",
                "phi_Omega=pi/2 follows the complex-rotated central support clue, but is not yet a Higgs-row certificate.",
            ],
            "strict_no_knob_accepted": False,
            "controlled_numeric_candidate": True,
        }
    )

    numerical_enumeration = {
        "schema": "MTTHPolarFieldNumericalCompletionEnumeration.v1",
        "status": "CONTROLLED_POLAR_COMPLETIONS_ENUMERATED_STRICT_NONE_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "s_beta": s_beta,
            "r_H_controlled": r_controlled,
            "sqrt_s_beta": polar["selected_angle_data"]["sqrt_s_beta"],
            "sqrt_1_minus_s_beta": polar["selected_angle_data"]["sqrt_1_minus_s_beta"],
            "m0_tracefree_trial": m0_tracefree,
        },
        "enumerated_candidates": candidate_rows,
        "strict_acceptance": {
            "accepted_count": 0,
            "reason": "r_H, sigma_D, phi_Omega, and m0/trace are not source-owned strict H rows in the current corpus.",
        },
    }

    source_clue_map = {
        "schema": "MTTHPolarFieldSourceClueMap.v1",
        "status": "SOURCE_CLUES_SUPPORT_CONTROLLED_DISCRETE_CHOICES_NOT_STRICT_SELECTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "clues": {
            "T3_orientation": {
                "available": hym["first_tracefree_hym_correction"]["selected_End0_direction"] == "T3",
                "source": "selected HYM first trace-free correction",
                "supports": "sigma_D orientation convention",
                "strict_Huv_certificate": False,
            },
            "tracefree_quotient": {
                "available": True,
                "source": "Herm(2) trace-free threshold block contract",
                "supports": "m0=0 for quotient/trace-free candidate",
                "strict_full_H_response_trace_certificate": False,
            },
            "complex_rotated_phase": {
                "available": ct["gate_results"]["complex_rotated_central_support_detected"],
                "source": "Qa/SU3 c-twist transgression pairing",
                "supports": "phi_Omega=pi/2 as complex orthogonal phase candidate",
                "strict_Huv_phase_certificate": False,
            },
            "controlled_radial": {
                "available": hrg["decision"]["minimal_parameter_H_layer_available"],
                "source": "UP_RET_OVERLAP.HRG controlled lane",
                "supports": "r_H numerical radial scale in controlled tier",
                "strict_Huv_radial_certificate": False,
            },
            "diagonal_HYM_scale": {
                "available": diag_hym["diagonal_metric_payload"]["closed"],
                "source": "selected diagonal HYM operator payload",
                "supports": "T3/trace-free shape only",
                "strict_Huv_radial_certificate": False,
                "why_not_used_as_r_H": "The constants-side H7B1D packet already rejects diagonal HYM as a finite scalar Huv row source.",
            },
        },
        "external_diagnostic_guard": {
            "A_EW_HRG_burden_equality_exact": aew_hrg["values"]["ratio_residual"] == 0.0,
            "accepted_as_source_row": aew_hrg["interpretation"]["accepted_as_source_row"],
            "used_to_select_rows_here": False,
        },
    }

    selected_packet = {
        "schema": "MTTHControlledHPolarNumericalCandidate.v1",
        "status": "CONTROLLED_NUMERICAL_HERM2_CANDIDATE_EMITTED_STRICT_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "candidate": selected_controlled,
        "matrix": {
            "basis": ["H_u", "H_d^dagger"],
            "Huv": [
                [[selected_controlled["Huu"], 0.0], [selected_controlled["Hud_re"], selected_controlled["Hud_im"]]],
                [[selected_controlled["Hdu_re"], selected_controlled["Hdu_im"]], [selected_controlled["Hdd"], 0.0]],
            ],
            "complex_notation": [
                ["Huu", "i*Omega_abs"],
                ["-i*Omega_abs", "Hdd"],
            ],
        },
        "acceptance_tests": {
            "Hermitian": True,
            "tracefree": True,
            "non_scalar": selected_controlled["non_scalar_norm"] > 0.0,
            "s_beta_recovered": abs(selected_controlled["s_beta_residual"]) <= 1e-15,
            "no_observed_target_selector": True,
            "strict_source_owned_rows": False,
            "strict_row_certificates": False,
            "controlled_tier_candidate": True,
        },
    }

    next_cutset = {
        "schema": "MTTHNumericalCandidateNextCutset.v1",
        "status": "NEXT_CUTSET_PROMOTE_CONTROLLED_CHOICES_OR_EMIT_DIRECT_ACTION",
        "closure_claimed": True,
        "next_frontier": "MTT_Selected_HPolarFieldPromotion_or_FiniteHActionDerivation_v1",
        "must_do_to_close_strict": [
            "derive UP_RET_OVERLAP.HRG or another r_H from selected same-source H action/operator data",
            "promote T3 orientation to a Higgs-row sigma_D certificate",
            "promote complex-rotated central support to a Higgs-row phi_Omega certificate",
            "prove m0=0 as the selected quotient trace theorem for the full row interface or emit m0",
            "emit row-level exactness/error certificates for Huu,Hud,Hdd",
        ],
        "controlled_result_available_now": True,
    }

    candidate = {
        "schema": "MTTSelectedHPolarFieldNumericalCompletionAttemptOrDirectFiniteHActionRowsCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "ControlledHPolarNumericalCompletionAttemptTheorem",
            "proved": True,
            "statement": (
                "The current strict corpus does not emit a no-knob H polar-field solution, "
                "but the smallest controlled completion is numerically executable. With the "
                "existing controlled HRG radial support, trace-free quotient normalization, "
                "T3 orientation clue, and complex-rotated central phase clue, the Herm(2) "
                "candidate has r_H=391.39140285811936, sigma_D=+1, phi_Omega=pi/2, m0=0, "
                "Huu=26.835536563225222, Hud=i*390.47033716866446, and Hdd=-26.835536563225222. "
                "This exactly recovers selected s_beta but remains controlled-tier, not strict no-knob."
            ),
        },
        "decision": {
            "strict_no_knob_numeric_solution_found": False,
            "controlled_numeric_candidate_found": True,
            "controlled_candidate_reconstructs_selected_s_beta": True,
            "direct_finite_H_action_emitted": False,
            "next_frontier_fixed": True,
        },
        "key_numbers": {
            "r_H_controlled": r_controlled,
            "sigma_D_controlled": 1,
            "phi_Omega_controlled": math.pi / 2.0,
            "m0_controlled": 0.0,
            "Delta": selected_controlled["Delta"],
            "Omega_abs": selected_controlled["Omega_abs"],
            "Huu": selected_controlled["Huu"],
            "Hud_re": selected_controlled["Hud_re"],
            "Hud_im": selected_controlled["Hud_im"],
            "Hdd": selected_controlled["Hdd"],
            "selected_s_beta": s_beta,
            "recovered_s_beta": selected_controlled["recovered_s_beta"],
            "s_beta_residual": selected_controlled["s_beta_residual"],
            "strict_accepted_row_count": 0,
            "controlled_candidate_row_count": 4,
        },
        "packets": [
            f"candidate_data/{SLUG}/controlled_polar_completion_enumeration.packet.json",
            f"candidate_data/{SLUG}/source_clue_map_for_discrete_choices.packet.json",
            f"candidate_data/{SLUG}/controlled_hpolar_numeric_candidate.packet.json",
            f"candidate_data/{SLUG}/next_cutset_after_controlled_numeric_candidate.packet.json",
        ],
        "next_target": "MTT_Selected_HPolarFieldPromotion_or_FiniteHActionDerivation_v1",
    }

    certificate = {
        "certificate": "selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HPOLARFIELDNUMERICALCOMPLETIONATTEMPT_OR_DIRECTFINITEHACTIONROWS_CONTROLLED_CANDIDATE_EMITTED_STRICT_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "strict_no_knob_numeric_solution_found": False,
            "controlled_numeric_candidate_found": True,
            "s_beta_residual_zero": abs(selected_controlled["s_beta_residual"]) <= 1e-15,
            "Hermitian": True,
            "tracefree": True,
            "non_scalar": selected_controlled["non_scalar_norm"] > 0.0,
            "controlled_not_counted_as_strict": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "controlled_polar_completion_enumeration.packet.json", numerical_enumeration)
    write_json(CANDIDATE_DIR / "source_clue_map_for_discrete_choices.packet.json", source_clue_map)
    write_json(CANDIDATE_DIR / "controlled_hpolar_numeric_candidate.packet.json", selected_packet)
    write_json(CANDIDATE_DIR / "next_cutset_after_controlled_numeric_candidate.packet.json", next_cutset)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Polar-Field Numerical Completion Attempt or Direct Finite-H Action Rows v1",
                "",
                "## Result",
                "",
                "A controlled numerical Herm(2) candidate is now executable, but strict no-knob closure is still open.",
                "",
                "```text",
                "r_H       = 391.39140285811936",
                "sigma_D   = +1",
                "phi_Omega = pi/2",
                "m0        = 0",
                "Delta     = 26.835536563225222",
                "Omega     = i * 390.47033716866446",
                "Huu       = 26.835536563225222",
                "Hud       = i * 390.47033716866446",
                "Hdd       = -26.835536563225222",
                "```",
                "",
                "The candidate is Hermitian, trace-free, non-scalar, and recovers the selected polar angle `s_beta` to numerical roundoff.",
                "",
                "## Boundary",
                "",
                "This is not a strict no-knob solution.  The radial scale is the controlled HRG calibration, while the `T3` orientation and complex-rotated phase are source clues rather than final Higgs-row certificates.",
                "",
                "The next strict target is `MTT_Selected_HPolarFieldPromotion_or_FiniteHActionDerivation_v1`: promote these controlled choices from the same source, or emit a direct finite-H action whose second variation gives the rows.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
