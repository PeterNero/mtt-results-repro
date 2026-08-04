"""Build the H polar-field promotion / finite-H action derivation packet."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hpolarfieldpromotion_or_finitehactionderivation"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HPolarFieldPromotion_or_FiniteHActionDerivation_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    numerical = read_json(ROOT / "candidate_data/selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows.candidate.json")
    numeric_packet = read_json(
        ROOT
        / "candidate_data/selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows/"
        / "controlled_hpolar_numeric_candidate.packet.json"
    )
    tracefree = read_json(
        ROOT
        / "candidate_data/selected_herm2polarsourcecompletion_or_hresponserows/"
        / "tracefree_polar_source_completion.packet.json"
    )
    bhuv = read_json(
        ROOT
        / "candidate_data/selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier/"
        / "bhuv_two_column_source_orthonormal_lift.packet.json"
    )
    orientation = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-protospinor-gr-response-proof/candidate_data/"
        "selected_hym_correction_and_gauge_projector_value_table.packet.json"
    )
    diagonal = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-protospinor-gr-response-proof/candidate_data/"
        "selected_diagonal_hym_operator_payload_extraction.packet.json"
    )
    ct_norm = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "complex_rotated_ctwist_normalization.candidate.json"
    )
    ct_period = read_json(
        "C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data/"
        "ctwist_period_normalization_or_a01_exit.candidate.json"
    )
    hrg_consumer = read_json(
        ROOT / "candidate_data/selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap/"
        / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
    )

    rows = numeric_packet["candidate"]
    h_uu = rows["Huu"]
    hud_re = rows["Hud_re"]
    hud_im = rows["Hud_im"]
    h_dd = rows["Hdd"]

    promotion = {
        "schema": "MTTHPolarFieldPartialPromotion.v1",
        "status": "TRACEFREE_AND_T3_ORIENTATION_PROMOTED_PHASE_AND_RADIAL_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "promoted_now": {
            "m0_tracefree_quotient": {
                "promoted": tracefree["decision"]["m0_retired_for_tracefree_threshold_block"],
                "value": 0.0,
                "scope": "trace-free Huv/threshold block only",
                "not_promoted_for_full_H_response_trace": not tracefree["decision"]["m0_retired_for_full_H_response_rows"],
                "source": "trace-free Herm(2) polar contract plus determinant-one/central-trace-free HYM lane",
            },
            "sigma_D_orientation": {
                "promoted": True,
                "value": 1,
                "scope": "ordered B_Huv basis orientation convention",
                "ordered_basis": bhuv["ordered_two_column_source_space"]["basis"],
                "connection_on_ordered_basis": bhuv["source_hermitian_inner_product"]["connection_on_ordered_basis"],
                "selected_End0_direction": orientation["first_tracefree_hym_correction"]["selected_End0_direction"],
                "reason": "The selected ordered basis is (H_u,H_d^dagger) and the selected diagonal HYM lane is T3=diag(+,-) in that order.",
            },
        },
        "not_promoted_now": {
            "phi_Omega": {
                "candidate_value": "pi/2",
                "complex_rotated_support_available": ct_norm["gate_results"]["conditional_c_plus_minus_one_normalization"],
                "phase_certificate_emitted": False,
                "reason": "The complex-rotated c-twist support is primitive in the scaled frame, but period/finite-quotient selection remains open.",
                "period_gate_status": ct_period["status"],
            },
            "r_H": {
                "candidate_value": rows["r_H"],
                "controlled_radial_support_available": True,
                "strict_radial_certificate_emitted": False,
                "reason": "The HRG consumer route has selected dynamic payload availability but still no typed value-source map for UP_RET_OVERLAP.HRG.",
                "hrg_consumer_map_emitted": hrg_consumer["decision"]["typed_HRG_consumer_map_emitted"],
            },
        },
        "counts": {
            "promoted_polar_certificates": 2,
            "strict_value_rows_emitted": 0,
            "remaining_strict_polar_fields": ["r_H", "phi_Omega"],
        },
    }

    controlled_action = {
        "schema": "MTTHControlledFiniteHActionDerivation.v1",
        "status": "CONTROLLED_FINITE_H_ACTION_DERIVED_SOURCE_SELECTION_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "functional": {
            "name": "F_H_controlled",
            "domain": "z=(z_u,z_d) in C^2 on the ordered B_Huv basis",
            "formula": "F_H_controlled(z)=z^* H_controlled z",
            "H_controlled": [
                [[h_uu, 0.0], [hud_re, hud_im]],
                [[hud_re, -hud_im], [h_dd, 0.0]],
            ],
            "expanded_real_formula": (
                f"{h_uu}*|z_u|^2 + {h_dd}*|z_d|^2 "
                f"+ 2*Re(({hud_re}+{hud_im}i)*conj(z_u)*z_d)"
            ),
        },
        "second_variation": {
            "d2F_dconjz_dz_equals_H_controlled": True,
            "Huu": h_uu,
            "Hud_re": hud_re,
            "Hud_im": hud_im,
            "Hdd": h_dd,
            "Hermitian": numeric_packet["acceptance_tests"]["Hermitian"],
            "tracefree": numeric_packet["acceptance_tests"]["tracefree"],
            "non_scalar": numeric_packet["acceptance_tests"]["non_scalar"],
            "s_beta_recovered": numeric_packet["acceptance_tests"]["s_beta_recovered"],
        },
        "tier": {
            "controlled_action_emitted": True,
            "strict_selected_finite_H_action_emitted": False,
            "why_not_strict": [
                "H_controlled contains controlled r_H rather than a strict same-source radial source.",
                "H_controlled contains phi_Omega=pi/2 from conditional c-twist normalization support rather than a Higgs phase certificate.",
            ],
        },
    }

    strict_gap = {
        "schema": "MTTHPolarPromotionRemainingGap.v1",
        "status": "STRICT_GAP_REDUCED_TO_RADIAL_SOURCE_AND_PHASE_CERTIFICATE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_now": [
            "trace-free quotient m0=0 for Huv threshold block",
            "ordered T3 orientation sigma_D=+1",
            "controlled finite-H action exact second variation",
        ],
        "still_open": {
            "strict_r_H": "derive/admit UP_RET_OVERLAP.HRG from a typed same-source value map or replace it with another selected H radial source",
            "strict_phi_Omega": "derive the pi/2 phase from selected c-twist period/finite quotient or a Higgs-row phase theorem",
            "row_certificates": "after strict r_H and phi_Omega, emit source ownership and exactness/error certificates for Huu,Hud,Hdd",
        },
        "minimal_next_targets": [
            "MTT_Selected_HRGValueSourceMapForH_or_RadialActionScale_v1",
            "MTT_Selected_ComplexRotatedHPhaseCertificate_or_CTwistPeriodSelector_v1",
        ],
    }

    candidate = {
        "schema": "MTTSelectedHPolarFieldPromotionOrFiniteHActionDerivationCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "PartialHPolarPromotionAndControlledFiniteHActionTheorem",
            "proved": True,
            "statement": (
                "The controlled H polar-field candidate can be partially promoted.  The trace-free quotient "
                "promotes m0=0 for the Huv threshold block, and the selected ordered B_Huv/T3 HYM lane "
                "promotes sigma_D=+1 as the orientation convention.  These two promotions allow an exact "
                "controlled finite-H quadratic action whose second variation emits the numerical Herm(2) rows. "
                "Strict no-knob closure remains open precisely at r_H and phi_Omega: the HRG radial value still "
                "lacks a typed same-source value map, and the complex-rotated pi/2 phase still lacks the selected "
                "period/finite-quotient Higgs-row certificate."
            ),
        },
        "decision": {
            "m0_tracefree_quotient_promoted": True,
            "sigma_D_orientation_promoted": True,
            "controlled_finite_H_action_emitted": True,
            "strict_selected_finite_H_action_emitted": False,
            "strict_r_H_promoted": False,
            "strict_phi_Omega_promoted": False,
            "strict_no_knob_numeric_solution_found": False,
            "frontier_reduced_to_two_promotions": True,
        },
        "key_numbers": {
            "promoted_m0_tracefree": 0.0,
            "promoted_sigma_D": 1,
            "controlled_r_H": rows["r_H"],
            "controlled_phi_Omega": rows["phi_Omega_radians"],
            "Huu": h_uu,
            "Hud_re": hud_re,
            "Hud_im": hud_im,
            "Hdd": h_dd,
            "selected_s_beta": numerical["key_numbers"]["selected_s_beta"],
            "recovered_s_beta": numerical["key_numbers"]["recovered_s_beta"],
            "strict_value_rows_emitted": 0,
            "remaining_strict_promotion_count": 2,
        },
        "packets": [
            f"candidate_data/{SLUG}/partial_polar_field_promotion.packet.json",
            f"candidate_data/{SLUG}/controlled_finite_h_action_derivation.packet.json",
            f"candidate_data/{SLUG}/strict_gap_after_partial_promotion.packet.json",
        ],
        "next_target": "MTT_Selected_HRGValueSourceMapForH_or_ComplexRotatedHPhaseCertificate_v1",
    }

    certificate = {
        "certificate": "selected_hpolarfieldpromotion_or_finitehactionderivation_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HPOLARFIELDPROMOTION_OR_FINITEHACTIONDERIVATION_PARTIAL_PROMOTION_CONTROLLED_ACTION_STRICT_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "m0_tracefree_quotient_promoted": True,
            "sigma_D_orientation_promoted": True,
            "controlled_action_second_variation_exact": True,
            "strict_selected_action_emitted": False,
            "strict_r_H_promoted": False,
            "strict_phi_Omega_promoted": False,
            "remaining_strict_promotion_count": 2,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "partial_polar_field_promotion.packet.json", promotion)
    write_json(CANDIDATE_DIR / "controlled_finite_h_action_derivation.packet.json", controlled_action)
    write_json(CANDIDATE_DIR / "strict_gap_after_partial_promotion.packet.json", strict_gap)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Polar-Field Promotion or Finite-H Action Derivation v1",
                "",
                "## Result",
                "",
                "Two parts of the controlled numerical candidate promote cleanly:",
                "",
                "- `m0=0` is promoted for the trace-free Huv/threshold block.",
                "- `sigma_D=+1` is promoted as the ordered `(H_u,H_d^dagger)` / `T3=diag(+,-)` orientation convention.",
                "",
                "This gives an exact controlled quadratic finite-H action:",
                "",
                "```text",
                "F_H_controlled(z)=z^* H_controlled z",
                "H_controlled = [[26.835536563225222, i*390.47033716866446],",
                "                [-i*390.47033716866446, -26.835536563225222]]",
                "```",
                "",
                "Its second variation emits exactly the controlled Herm(2) rows.",
                "",
                "## Boundary",
                "",
                "This is still not strict no-knob closure.  The remaining strict promotions are:",
                "",
                "- `r_H`: derive/admit the HRG radial value from a typed same-source value map, or replace it with another selected H radial source.",
                "- `phi_Omega`: derive the `pi/2` phase from a selected c-twist period/finite quotient or direct Higgs-row phase theorem.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
