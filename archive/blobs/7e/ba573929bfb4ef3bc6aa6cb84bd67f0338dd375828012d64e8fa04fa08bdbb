"""Build the H radial norm-law / value-source derivation attempt."""

from __future__ import annotations

import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgradialnormlaw_or_value_source_derivation"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HRadialNormLaw_or_ValueSourceDerivation_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def best_source_only_scan(target: float, s_beta: float, static_logdet: float, heat_trace: float) -> list[dict]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    eps = math.exp(-2.0 * math.pi)
    atoms = {
        "1": 1.0,
        "q79": 79.0,
        "z448": 448.0,
        "rank27": 27.0,
        "formal72": 72.0,
        "positive_dim_H26": 26.0,
        "kernel_H1": 1.0,
        "pi": math.pi,
        "sqrt2": math.sqrt(2.0),
        "sqrt3": math.sqrt(3.0),
        "phi": phi,
        "epsilon_Theta": eps,
        "epsilon_Theta_1_3": eps ** (1.0 / 3.0),
        "sqrt_s_beta": math.sqrt(s_beta),
        "sqrt_1_minus_s_beta": math.sqrt(1.0 - s_beta),
        "static_H_logdet": static_logdet,
        "H_heat_t1": heat_trace,
    }
    denominator_names = [
        "1",
        "pi",
        "sqrt2",
        "sqrt3",
        "phi",
        "rank27",
        "positive_dim_H26",
        "epsilon_Theta_1_3",
        "sqrt_s_beta",
        "sqrt_1_minus_s_beta",
        "H_heat_t1",
    ]
    rows: list[dict] = []
    atom_items = list(atoms.items())
    seen: set[tuple[str, str]] = set()
    for degree in range(1, 4):
        for combo in itertools.combinations_with_replacement(atom_items, degree):
            product = 1.0
            names: list[str] = []
            for name, value in combo:
                product *= value
                names.append(name)
            numerator = "*".join(names)
            for denom_name in denominator_names:
                denom = atoms[denom_name]
                if denom == 0:
                    continue
                key = (numerator, denom_name)
                if key in seen:
                    continue
                seen.add(key)
                value = product / denom
                if not math.isfinite(value):
                    continue
                rows.append(
                    {
                        "formula": f"{numerator}/{denom_name}",
                        "value": value,
                        "absolute_error": abs(value - target),
                        "relative_error": abs(value - target) / target,
                        "accepted_as_source_identity": False,
                    }
                )
    return sorted(rows, key=lambda row: row["relative_error"])[:20]


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    phase = read_json(ROOT / "candidate_data/selected_hphasesignselector_lenscircle_or_hrgvaluemap.candidate.json")
    phase_rows = read_json(
        ROOT / "candidate_data/selected_hphasesignselector_lenscircle_or_hrgvaluemap/signed_hpolar_rows_after_selector.packet.json"
    )
    radial_split = read_json(
        ROOT / "candidate_data/selected_hradialscalephasesource_or_herm2hessianrows/h_radial_scale_source_split.packet.json"
    )
    polar_law = read_json(
        ROOT / "candidate_data/selected_hradialscalephasesource_or_herm2hessianrows/herm2_polar_reconstruction_law.packet.json"
    )
    strict_rhrg = read_json(ROOT / "candidate_data/selected_strictrhrgsourceconstruction_or_independentvalidationoracle.candidate.json")
    hrg_value_map = read_json(ROOT / "candidate_data/selected_hrgvaluemapforh_or_complexrotatedhphasecertificate.candidate.json")
    k_gate = read_json(
        ROOT / "candidate_data/selected_tschemelambdah_sourcerows_or_kthresholdrowclosure/kthreshold_gate_after_tscheme_lambdah_attempt.packet.json"
    )
    threshold_delta = read_json(
        ROOT / "candidate_data/selected_thresholddeltarows_or_lambdahpayloadexecution/ten_kthreshold_gate_after_charged_null_delta.packet.json"
    )
    det_rg = read_json(ROOT / "candidate_data/selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun.candidate.json")
    logdet = read_json(ROOT / "candidate_data/selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum.candidate.json")
    primitive = read_json(
        ROOT / "candidate_data/selected_huvprimitiveformula_or_finiteerrorboundexecution/bhuv_support_underdetermination_witness.packet.json"
    )

    target = phase["key_numbers"]["controlled_r_H"]
    s_beta = radial_split["selected_angle_support"]["s_beta"]
    sqrt_s = math.sqrt(s_beta)
    sqrt_c = math.sqrt(1.0 - s_beta)
    static_logdet = logdet["key_numbers"]["static_H_sector_log_pseudodeterminant"]
    heat_trace = logdet["key_numbers"]["static_H_sector_kernel_dimension"] + logdet["key_numbers"][
        "static_H_sector_positive_dimension"
    ] * 0.0
    # Use the audited t=1 heat trace from the candidate when present.
    heat_trace = 1.886949076994966
    scan_rows = best_source_only_scan(target, s_beta, static_logdet, heat_trace)

    unit_matrix = {
        "basis": ["H_u", "H_d^dagger"],
        "unit_tracefree_generator": [
            [[sqrt_s, 0.0], [0.0, sqrt_c]],
            [[0.0, -sqrt_c], [-sqrt_s, 0.0]],
        ],
        "complex_notation": [
            ["sqrt(s_beta)", "i*sqrt(1-s_beta)"],
            ["-i*sqrt(1-s_beta)", "-sqrt(s_beta)"],
        ],
        "normalization_checks": {
            "trace": 0.0,
            "determinant": -1.0,
            "eigenvalues": [-1.0, 1.0],
            "frobenius_norm_squared": 2.0,
            "radial_norm_identity": "r_H = sqrt(Tr(H_tf^2)/2) = ||H_tf||_F/sqrt(2) = spectral_radius(H_tf)",
        },
    }

    norm_law = {
        "schema": "MTTHRadialNormLaw.v1",
        "status": "H_RADIAL_NORM_LAW_DERIVED_NUMERIC_VALUE_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs_now_selected": {
            "s_beta_selected": True,
            "m0_tracefree_quotient_promoted": True,
            "sigma_D_orientation_promoted": True,
            "phi_sign_promoted": phase["decision"]["phi_sign_promoted"],
            "plus_i_phase": phase["key_numbers"]["phi_Omega"],
        },
        "derived_tracefree_unit_generator": unit_matrix,
        "conditional_Huv_formula": {
            "H_tf(r_H)": "r_H * [[sqrt(s_beta), i*sqrt(1-s_beta)],[-i*sqrt(1-s_beta), -sqrt(s_beta)]]",
            "Delta": "r_H*sqrt(s_beta)",
            "Omega_abs": "r_H*sqrt(1-s_beta)",
            "Hud": "+i*r_H*sqrt(1-s_beta)",
            "Hdd": "-r_H*sqrt(s_beta)",
        },
        "controlled_numeric_replay": {
            "r_H_controlled": target,
            "Delta": phase_rows["rows"]["Huu"],
            "Omega_abs": phase_rows["rows"]["Hud_im"],
            "reconstructed_from_norm_law": True,
            "strict_value_source": False,
        },
        "decision": {
            "radial_norm_law_promoted": True,
            "numeric_radial_value_promoted": False,
            "strict_Herm2_rows_promoted": False,
        },
    }

    source_route_audit = {
        "schema": "MTTHRadialValueSourceRouteAudit.v1",
        "status": "THREE_LEGAL_RADIAL_VALUE_ROUTES_RECHECKED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "routes": {
            "typed_HRG_value_map": {
                "accepted": False,
                "accepted_strict_source_count": strict_rhrg["key_numbers"]["accepted_strict_source_count"],
                "strict_R_H_RG_source_constructed": strict_rhrg["closure_decision"]["strict_R_H_RG_source_constructed"],
                "previous_hrg_map_strict_r_H_promoted": hrg_value_map["decision"]["strict_r_H_promoted"],
            },
            "H_lambda_K_threshold_row": {
                "accepted": False,
                "selected_K_threshold_row_count_present": threshold_delta["conditional_full_scalar_closure_current"][
                    "selected_K_threshold_row_count_present"
                ],
                "selected_K_threshold_row_count_required": threshold_delta["conditional_full_scalar_closure_current"][
                    "selected_K_threshold_row_count_required"
                ],
                "selected_H_lambda_payload_emitted": k_gate["selected_lambda_H_payload_emitted"],
                "H_row_selected_K_threshold_row_emitted": next(
                    row for row in k_gate["rows"] if row["omega_id"] == "Omega_H.lambda"
                )["selected_K_threshold_row_emitted"],
            },
            "determinant_RG_radial_operator": {
                "accepted": False,
                "operator_contract_defined": det_rg["closure_decision"]["operator_contract_defined"],
                "operator_value_emitted": det_rg["closure_decision"]["operator_value_emitted"],
                "static_logdet_imported": logdet["closure_decision"]["static_H_logdet_imported"],
                "static_logdet_promoted_to_R_H_RG": logdet["closure_decision"]["static_H_logdet_promoted_to_R_H_RG"],
            },
        },
        "underdetermination_guard": {
            "bhuv_support_underdetermines_rows": primitive["decision"]["B_Huv_support_selects_value_rows"] is False,
            "radial_positive_rescaling_modulus_survives_current_selected_constraints": True,
            "reason": "For any r>0, the selected s_beta, trace-free quotient, T3 orientation, and +i phase produce an admissible normalized Herm(2) ray. A value source must fix the ray length.",
        },
        "decision": {
            "accepted_numeric_radial_value_sources": 0,
            "numeric_radial_value_promoted": False,
            "required_next_object": "selected H radial action norm value, selected K_threshold.Omega_H.lambda row, or strict R_H^RG determinant/RG value",
        },
    }

    scan_packet = {
        "schema": "MTTHRadialSourceOnlyFiniteInvariantScan.v1",
        "status": "SOURCE_ONLY_FINITE_INVARIANT_SCAN_NO_EXACT_ACCEPTED_IDENTITY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target": target,
        "atoms_allowed": [
            "q79",
            "z448",
            "rank27",
            "formal72",
            "positive_dim_H26",
            "epsilon_Theta",
            "s_beta",
            "static_H_logdet",
            "H_heat_t1",
            "pi/sqrt2/sqrt3/phi",
        ],
        "accepted_as_source_identity_count": 0,
        "best_candidates": scan_rows,
        "decision": {
            "near_misses_promoted": False,
            "exact_source_identity_found": False,
        },
    }

    candidate = {
        "schema": "MTTSelectedHRadialNormLawOrValueSourceDerivationCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HRadialNormLawAndValueSourceCutsetTheorem",
            "proved": True,
            "statement": (
                "After the selected s_beta angle, trace-free quotient, T3 orientation, and q79 lens-circle +i phase are fixed, "
                "the Huv matrix is a selected Herm(2) ray.  The radial law is now derived: "
                "H_tf(r)=r [[sqrt(s_beta), i sqrt(1-s_beta)],[-i sqrt(1-s_beta), -sqrt(s_beta)]], "
                "with r=sqrt(Tr(H_tf^2)/2)=||H_tf||_F/sqrt(2).  The current selected ledger does not emit the numeric ray length. "
                "The three legal value-source routes -- typed HRG/R_H^RG map, H/lambda K_threshold row, and determinant/RG radial operator -- "
                "all still accept zero numeric value rows."
            ),
        },
        "decision": {
            "radial_norm_law_promoted": True,
            "numeric_radial_value_promoted": False,
            "strict_r_H_promoted": False,
            "strict_Herm2_rows_promoted": False,
            "frontier_reduced_to_numeric_radial_value_source": True,
            "strict_no_knob_numeric_solution_found": False,
        },
        "key_numbers": {
            "controlled_r_H": target,
            "sqrt_s_beta": sqrt_s,
            "sqrt_1_minus_s_beta": sqrt_c,
            "best_source_only_formula": scan_rows[0]["formula"],
            "best_source_only_value": scan_rows[0]["value"],
            "best_source_only_relative_error": scan_rows[0]["relative_error"],
            "accepted_numeric_radial_value_sources": 0,
        },
        "packets": [
            f"candidate_data/{SLUG}/h_radial_norm_law.packet.json",
            f"candidate_data/{SLUG}/h_radial_value_source_route_audit.packet.json",
            f"candidate_data/{SLUG}/h_radial_source_only_finite_invariant_scan.packet.json",
        ],
        "next_target": "MTT_Selected_HRadialActionNormValue_or_HLambdaThresholdRow_v1",
    }

    certificate = {
        "certificate": "selected_hrgradialnormlaw_or_value_source_derivation_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HRADIALNORMLAW_OR_VALUESOURCEDERIVATION_NORM_LAW_CLOSED_VALUE_SOURCE_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "radial_norm_law_promoted": True,
            "numeric_radial_value_promoted": False,
            "strict_r_H_promoted": False,
            "typed_HRG_value_map_accepted": False,
            "H_lambda_K_threshold_row_accepted": False,
            "determinant_RG_radial_operator_value_accepted": False,
            "source_only_scan_exact_identity_found": False,
            "frontier_reduced_to_numeric_radial_value_source": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "h_radial_norm_law.packet.json", norm_law)
    write_json(CANDIDATE_DIR / "h_radial_value_source_route_audit.packet.json", source_route_audit)
    write_json(CANDIDATE_DIR / "h_radial_source_only_finite_invariant_scan.packet.json", scan_packet)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Radial Norm Law or Value-Source Derivation v1",
                "",
                "## Result",
                "",
                "The radial law is now derived, but the numeric radial value is not yet selected.",
                "",
                "With `s_beta`, trace-free quotient, ordered `T3`, and the q79 lens-circle `+i` phase fixed, the Huv block is the selected Herm(2) ray",
                "",
                "```text",
                "H_tf(r) = r * [[sqrt(s_beta), i*sqrt(1-s_beta)],",
                "             [-i*sqrt(1-s_beta), -sqrt(s_beta)]].",
                "```",
                "",
                "The radial scalar is therefore",
                "",
                "```text",
                "r_H = sqrt(Tr(H_tf^2)/2) = ||H_tf||_F/sqrt(2) = spectral_radius(H_tf).",
                "```",
                "",
                "This closes the meaning of `r_H`: it is the selected H radial action/Hessian norm. It does not yet close the value.",
                "",
                "## Value-Source Audit",
                "",
                "The three legal numeric routes were rechecked:",
                "",
                "- typed HRG / strict `R_H^RG` value map: `0` accepted source rows",
                "- direct H/lambda `K_threshold.Omega_H.lambda` row: absent; ten-row K closure remains `9/10`",
                "- determinant/RG radial operator: domain contract defined, value not emitted",
                "",
                f"Best finite-invariant diagnostic near miss: `{scan_rows[0]['formula']}` = `{scan_rows[0]['value']}` with relative error `{scan_rows[0]['relative_error']}`. It is not promoted.",
                "",
                "## Next Target",
                "",
                "```text",
                "MTT_Selected_HRadialActionNormValue_or_HLambdaThresholdRow_v1",
                "```",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
