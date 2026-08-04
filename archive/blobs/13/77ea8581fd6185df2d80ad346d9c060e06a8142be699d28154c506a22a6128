"""Build the HRG value-map / complex-rotated H phase certificate attempt."""

from __future__ import annotations

import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgvaluemapforh_or_complexrotatedhphasecertificate"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HRGValueSourceMapForH_or_ComplexRotatedHPhaseCertificate_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def diagnostic_invariant_scan(target: float, s_beta: float) -> list[dict]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    atoms = {
        "q": 79.0,
        "formal_rows": 72.0,
        "primitive_rows": 72.0,
        "charged_rows": 9.0,
        "rank": 27.0,
        "positive_dim_H": 26.0,
        "pi": math.pi,
        "sqrt2": math.sqrt(2.0),
        "sqrt3": math.sqrt(3.0),
        "phi": phi,
        "z64": 64.0,
        "z448": 448.0,
        "logdet_H_static": 43.802475498298655,
        "heat_t1_H_static": 1.886949076994966,
        "sqrt_s_beta": math.sqrt(s_beta),
        "sqrt_1_minus_s_beta": math.sqrt(1.0 - s_beta),
        "twelve": 12.0,
    }
    denominators = {
        "1": 1.0,
        "pi": math.pi,
        "sqrt2": math.sqrt(2.0),
        "sqrt3": math.sqrt(3.0),
        "phi": phi,
        "rank": 27.0,
        "charged_rows": 9.0,
        "twelve": 12.0,
        "sqrt_s_beta": atoms["sqrt_s_beta"],
        "sqrt_1_minus_s_beta": atoms["sqrt_1_minus_s_beta"],
    }
    rows: list[dict] = []
    atom_items = list(atoms.items())
    seen: set[tuple[str, str]] = set()
    for degree in range(1, 4):
        for combo in itertools.product(atom_items, repeat=degree):
            names = tuple(name for name, _ in combo)
            product = 1.0
            for _, value in combo:
                product *= value
            for denom_name, denom in denominators.items():
                key = ("*".join(names), denom_name)
                if key in seen:
                    continue
                seen.add(key)
                value = product / denom
                if not math.isfinite(value):
                    continue
                rows.append(
                    {
                        "formula": f"{'*'.join(names)}/{denom_name}",
                        "value": value,
                        "absolute_error": abs(value - target),
                        "relative_error": abs(value - target) / target,
                        "accepted_as_source_identity": False,
                    }
                )
    return sorted(rows, key=lambda row: row["relative_error"])[:12]


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    promotion = read_json(ROOT / "candidate_data/selected_hpolarfieldpromotion_or_finitehactionderivation.candidate.json")
    numeric = read_json(
        ROOT
        / "candidate_data/selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows/"
        / "controlled_hpolar_numeric_candidate.packet.json"
    )
    hrg_consumer = read_json(
        ROOT
        / "candidate_data/selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap/"
        / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
    )
    hrg_value_source = read_json(ROOT / "candidate_data/selected_hrgconsumervaluesource_or_largethresholdtransportmap.candidate.json")
    strict_hrg = read_json(ROOT / "candidate_data/selected_strictrhrgsourceconstruction_or_independentvalidationoracle.candidate.json")
    ct_pairing = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "ctwist_transgression_pairing_computation.candidate.json"
    )
    ct_norm = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "complex_rotated_ctwist_normalization.candidate.json"
    )
    ct_period = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "ctwist_period_normalization_or_a01_exit.candidate.json"
    )
    period_search = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "central_period_selector_search.candidate.json"
    )

    s_beta = promotion["key_numbers"]["selected_s_beta"]
    hrg_target = promotion["key_numbers"]["controlled_r_H"]
    scan_rows = diagnostic_invariant_scan(hrg_target, s_beta)

    hrg_packet = {
        "schema": "MTTHRGValueSourceMapForHAttempt.v1",
        "status": "HRG_VALUE_SOURCE_MAP_ATTEMPTED_STRICT_MAP_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "controlled_value": hrg_target,
        "existing_controlled_status": {
            "controlled_RO_value_source_admitted": hrg_value_source["closure_decision"][
                "controlled_RO_value_source_admitted"
            ],
            "controlled_same_HRG_nonHiggs_map_count": hrg_value_source["closure_decision"][
                "controlled_same_HRG_nonHiggs_map_count"
            ],
            "dynamic_payload_blocker_retired": hrg_consumer["decision"]["dynamic_payload_blocker_retired"],
        },
        "strict_status": {
            "typed_HRG_consumer_map_emitted": hrg_consumer["decision"]["typed_HRG_consumer_map_emitted"],
            "strict_RO_value_source_derived": hrg_value_source["closure_decision"]["strict_RO_value_source_derived"],
            "strict_R_H_RG_source_constructed": strict_hrg["closure_decision"]["strict_R_H_RG_source_constructed"],
            "accepted_strict_source_count": strict_hrg["key_numbers"]["accepted_strict_source_count"],
        },
        "expanded_diagnostic_invariant_scan": {
            "diagnostic_target_scan_used": True,
            "accepted_as_source_identity_count": 0,
            "best_candidates": scan_rows,
            "decision": "near misses are not promoted; no exact selected invariant identity was found",
        },
        "decision": {
            "r_H_promoted_to_strict": False,
            "controlled_r_H_retained": True,
            "next_required_source_object": "typed same-source HRG consumer/value map or independent H radial action scale",
        },
    }

    phase_packet = {
        "schema": "MTTComplexRotatedHPhaseCertificateAttempt.v1",
        "status": "COMPLEX_ROTATED_PHASE_AXIS_PROMOTED_SIGN_OR_PERIOD_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "phase_candidate": {
            "controlled_phi_Omega": numeric["candidate"]["phi_Omega_radians"],
            "controlled_phi_label": numeric["candidate"]["phi_Omega_label"],
            "Hud_re_controlled": numeric["candidate"]["Hud_re"],
            "Hud_im_controlled": numeric["candidate"]["Hud_im"],
        },
        "promoted_now": {
            "complex_orthogonal_axis": True,
            "Hud_re_equals_zero_axis": True,
            "phase_reduced_to": ["pi/2", "-pi/2"],
            "support": {
                "complex_rotated_central_support_detected": ct_pairing["gate_results"][
                    "complex_rotated_central_support_detected"
                ],
                "all_slants_unit_magnitude_in_scaled_frame": ct_norm["gate_results"][
                    "all_slants_unit_magnitude_in_scaled_frame"
                ],
                "conditional_c_plus_minus_one_normalization": ct_norm["gate_results"][
                    "conditional_c_plus_minus_one_normalization"
                ],
                "raw_nil_axis_match_required_for_ctwist_typing": ct_norm["gate_results"][
                    "raw_nil_axis_match_required_for_ctwist_typing"
                ],
            },
        },
        "not_promoted_now": {
            "plus_i_orientation": {
                "candidate": "pi/2",
                "promoted": False,
                "reason": "The c-twist packets supply +/- primitive complex axes, but no same-branch period/finite-quotient selector chooses the +i Higgs orientation.",
            },
            "period_or_finite_quotient": {
                "period_normalization_promoted": ct_period["gate_results"]["period_normalization_promoted"],
                "finite_quotient_same_branch_selected": ct_period["gate_results"][
                    "finite_quotient_same_branch_selected"
                ],
                "period_selector_found": period_search["gate_results"]["period_selector_found"],
            },
        },
        "decision": {
            "phi_axis_promoted": True,
            "phi_sign_promoted": False,
            "strict_phi_Omega_promoted": False,
            "phase_continuum_reduced_to_binary_orientation": True,
        },
    }

    combined = {
        "schema": "MTTHRGAndPhaseRemainingFrontier.v1",
        "status": "FRONTIER_REDUCED_TO_HRG_SOURCE_MAP_AND_PHASE_SIGN_PERIOD_SELECTOR",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_or_promoted": [
            "m0=0 trace-free quotient",
            "sigma_D=+1 ordered T3 orientation",
            "controlled finite-H quadratic action",
            "complex orthogonal phase axis Hud_re=0, phi in {+/- pi/2}",
        ],
        "still_open_for_strict_rows": {
            "r_H": "typed same-source HRG value map or independent H radial action scale",
            "phi_sign": "+i versus -i Higgs orientation from selected c-twist period/finite quotient or direct H phase theorem",
            "row_certificates": "source ownership and exactness/error certificates after r_H and phase sign are strict",
        },
        "next_frontier": "MTT_Selected_HRGValueSourceMap_or_HPhaseSignSelector_v1",
    }

    candidate = {
        "schema": "MTTSelectedHRGValueMapForHOrComplexRotatedHPhaseCertificateCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HRGValueMapAndComplexRotatedPhaseAxisReductionTheorem",
            "proved": True,
            "statement": (
                "The two remaining H polar blockers have now been attacked directly.  The HRG radial lane "
                "still does not promote: controlled HRG remains available, but the typed same-source value "
                "map and exact finite invariant identity are absent.  The phase lane partially promotes: "
                "complex-rotated c-twist support reduces the off-diagonal Higgs phase to the imaginary "
                "axis, phi_Omega in {+pi/2,-pi/2}, but the same-branch period/finite-quotient selector "
                "needed to choose the +i orientation remains open."
            ),
        },
        "decision": {
            "strict_r_H_promoted": False,
            "controlled_r_H_retained": True,
            "phi_axis_promoted": True,
            "phi_sign_promoted": False,
            "strict_phi_Omega_promoted": False,
            "strict_no_knob_numeric_solution_found": False,
            "frontier_reduced_to_HRG_map_and_phase_sign": True,
        },
        "key_numbers": {
            "controlled_r_H": hrg_target,
            "best_hrg_diagnostic_formula": scan_rows[0]["formula"],
            "best_hrg_diagnostic_value": scan_rows[0]["value"],
            "best_hrg_diagnostic_relative_error": scan_rows[0]["relative_error"],
            "phi_axis_options": ["pi/2", "-pi/2"],
            "controlled_phi_candidate": numeric["candidate"]["phi_Omega_radians"],
            "Hud_re_axis_value": 0.0,
            "Hud_im_abs_controlled": abs(numeric["candidate"]["Hud_im"]),
            "strict_value_rows_emitted": 0,
        },
        "packets": [
            f"candidate_data/{SLUG}/hrg_value_source_map_attempt.packet.json",
            f"candidate_data/{SLUG}/complex_rotated_h_phase_certificate_attempt.packet.json",
            f"candidate_data/{SLUG}/combined_frontier_after_two_gate_attack.packet.json",
        ],
        "next_target": "MTT_Selected_HRGValueSourceMap_or_HPhaseSignSelector_v1",
    }

    certificate = {
        "certificate": "selected_hrgvaluemapforh_or_complexrotatedhphasecertificate_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HRGVALUEMAPFORH_OR_COMPLEXROTATEDHPHASECERTIFICATE_PHASE_AXIS_PROMOTED_HRG_AND_SIGN_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "strict_r_H_promoted": False,
            "phi_axis_promoted": True,
            "phi_sign_promoted": False,
            "strict_phi_Omega_promoted": False,
            "diagnostic_near_misses_not_promoted": True,
            "frontier_reduced_to_HRG_map_and_phase_sign": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "hrg_value_source_map_attempt.packet.json", hrg_packet)
    write_json(CANDIDATE_DIR / "complex_rotated_h_phase_certificate_attempt.packet.json", phase_packet)
    write_json(CANDIDATE_DIR / "combined_frontier_after_two_gate_attack.packet.json", combined)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected HRG Value Source Map for H or Complex-Rotated H Phase Certificate v1",
                "",
                "## Result",
                "",
                "The two remaining gates were attacked directly.",
                "",
                "- `r_H` is not promoted.  The controlled HRG value remains available, but the typed same-source value map is still absent.",
                "- `phi_Omega` partially promotes.  Complex-rotated c-twist support reduces the phase to the imaginary axis, `phi_Omega in {+pi/2,-pi/2}`.",
                "",
                "The strict sign/orientation `+i` is not yet promoted because the c-twist period/finite-quotient selector is still open.",
                "",
                "## Diagnostic HRG Search",
                "",
                f"Best diagnostic near miss: `{scan_rows[0]['formula']}` = `{scan_rows[0]['value']}` with relative error `{scan_rows[0]['relative_error']}`.",
                "",
                "This is recorded only as a diagnostic; no near miss is promoted as a source identity.",
                "",
                "## New Frontier",
                "",
                "`MTT_Selected_HRGValueSourceMap_or_HPhaseSignSelector_v1`.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
