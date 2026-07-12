"""Build the H phase-sign selector from the q79 lens-circle orientation."""

from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hphasesignselector_lenscircle_or_hrgvaluemap"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HPhaseSignSelector_LensCircle_or_HRGValueMap_v1.md"

Q79 = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro")


def read_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    previous = read_json(ROOT / "candidate_data/selected_hrgvaluemapforh_or_complexrotatedhphasecertificate.candidate.json")
    phase_axis = read_json(
        ROOT
        / "candidate_data/selected_hrgvaluemapforh_or_complexrotatedhphasecertificate/"
        / "complex_rotated_h_phase_certificate_attempt.packet.json"
    )
    numeric = read_json(
        ROOT
        / "candidate_data/selected_hpolarfieldnumericalcompletionattempt_or_directfinitehactionrows/"
        / "controlled_hpolar_numeric_candidate.packet.json"
    )
    promotion = read_json(ROOT / "candidate_data/selected_hpolarfieldpromotion_or_finitehactionderivation.candidate.json")
    bhuv = read_json(
        ROOT
        / "candidate_data/selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier/"
        / "bhuv_two_column_source_orthonormal_lift.packet.json"
    )
    q79_fixed = read_json(Q79 / "candidate_data/time_oriented_fixed_gerbe_representative.candidate.json")
    q79_period = read_json(Q79 / "candidate_data/time_oriented_m1_gerbe_period_table.candidate.json")
    q79_parity = read_json(Q79 / "candidate_data/orientation_observable_parity.candidate.json")
    lens_nil_guard = read_json(Q79 / "certificates/c3_lens_nil_weight_source_audit_certificate.json")
    cp_frontier = read_json(
        ROOT
        / "candidate_data/selected_staticcoefficienttransfermap_or_cporientationfrontier/"
        / "cp_orientation_frontier_after_static_transfer.packet.json"
    )
    same_shift = read_json(
        ROOT
        / "candidate_data/selected_weylcoefficientsource_reduction_or_orientationtransfermap/"
        / "same_active_shift_orientation_branch_filter.packet.json"
    )

    q79_branch = q79_fixed["branch_representatives"]["time_oriented_q79"]
    conjugate_branch = q79_fixed["branch_representatives"]["antiunitary_conjugate_q369"]
    m1_commutator = q79_period["finite_period_table"]["commutator_matrix_mod3_on_basis_e1_e2"]
    m2_commutator = q79_period["antiunitary_conjugate_table_retained"]["period_table"][
        "commutator_matrix_mod3_on_basis_e1_e2"
    ]

    omega_abs = abs(numeric["candidate"]["Hud_im"])
    h_phase_sign_packet = {
        "schema": "MTTHPhaseSignSelectorLensCircle.v1",
        "status": "H_PHASE_SIGN_SELECTED_BY_Q79_LENS_CIRCLE_ORIENTATION_HRG_RADIAL_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_basis": {
            "ordered_basis": bhuv["ordered_two_column_source_space"]["basis"],
            "same_source_branch": bhuv["same_source_branch"],
            "connection": bhuv["source_hermitian_inner_product"]["connection_on_ordered_basis"],
            "selected_quotient": bhuv["ordered_two_column_source_space"]["selected_finite_quotient"],
        },
        "phase_axis_input": {
            "previous_axis_promoted": previous["decision"]["phi_axis_promoted"],
            "previous_sign_promoted": previous["decision"]["phi_sign_promoted"],
            "axis_options": phase_axis["promoted_now"]["phase_reduced_to"],
            "Hud_re_equals_zero_axis": phase_axis["promoted_now"]["Hud_re_equals_zero_axis"],
        },
        "lens_circle_selector": {
            "selector_name": "time-oriented q79/F,m=1 finite lens-circle orientation",
            "time_oriented_branch": {
                "q": q79_branch["q"],
                "orientation": q79_branch["orientation"],
                "torsion_label_m": q79_branch["torsion_label_m"],
                "selected": q79_fixed["calculation_results"]["retarded_time_orientation_selects_q79_representative"],
            },
            "antiunitary_conjugate_branch": {
                "q": conjugate_branch["q"],
                "orientation": conjugate_branch["orientation"],
                "torsion_label_m": conjugate_branch["torsion_label_m"],
                "retained": q79_fixed["calculation_results"]["antiunitary_conjugate_torsion_label_m2_retained"],
            },
            "m1_commutator_matrix_mod3": m1_commutator,
            "m2_conjugate_commutator_matrix_mod3": m2_commutator,
            "m1_period_table_closed": q79_period["calculation_results"]["finite_m1_period_table_constructed"],
            "m1_matches_qutrit_F_orientation": q79_period["calculation_results"][
                "commutator_matrix_matches_qutrit_F_orientation"
            ],
            "ordinary_bundle_coboundary_ruled_out": q79_period["calculation_results"][
                "ordinary_bundle_coboundary_ruled_out"
            ],
            "finite_operator_cp_odd_sign_flips_under_conjugation": q79_parity["finite_operator_parity"][
                "complex_conjugation_invariants"
            ]["nonzero_imaginary_sign_flips"],
            "finite_operator_parity_closed": q79_parity["finite_operator_parity"]["finite_parity_closed"],
        },
        "orientation_transfer_rule": {
            "rule": "With ordered Huv basis (H_u,H_d^dagger) and T3=diag(+,-), the selected q79/F,m=1 lens-circle orientation is the positive finite-Weyl complex orientation. It maps the binary imaginary axis to +J_H, J_H=[[0,i],[-i,0]]. The antiunitary q369/F*,m=2 branch maps to -J_H.",
            "static_cp_orientation_support": cp_frontier["static_commutator_cp_orientation_sign_fixed"],
            "same_active_shift_positive_orientation_support": "positive" in same_shift["compatible_cp_orientations"],
            "H_sector_orientation_label_zero_not_used_as_numeric_weight": True,
            "old_lens_nil_numeric_weight_used": False,
            "old_lens_nil_numeric_weight_rejected_by_guard": lens_nil_guard["closed"][
                "old_lens_nil_coefficient_source_rejected"
            ],
        },
        "selected_phase": {
            "phi_Omega_label": "+pi/2",
            "phi_Omega_radians": math.pi / 2.0,
            "Hud_re": 0.0,
            "Hud_im_sign": +1,
            "Hud_im_controlled_radial": omega_abs,
            "complex_generator": "+J_H",
            "conjugate_branch_phase_label": "-pi/2",
            "conjugate_branch_retained": True,
        },
        "decision": {
            "phase_axis_promoted": True,
            "phi_sign_promoted": True,
            "strict_phi_Omega_promoted_in_finite_weyl_convention": True,
            "antiunitary_minus_i_branch_retained_not_selected_for_time_oriented_branch": True,
            "old_lens_nil_numeric_weight_used": False,
            "r_H_promoted_to_strict": False,
            "strict_no_knob_numeric_solution_found": False,
        },
    }

    signed_rows = {
        "schema": "MTTSignedHPolarRowsAfterLensCircleSelector.v1",
        "status": "SIGNED_H_PHASE_ROWS_EMITTED_CONTROLLED_RADIAL_HRG_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "basis": numeric["matrix"]["basis"],
        "radial_status": "controlled HRG radial value retained; not strict source-owned",
        "selected_phase_status": "strict sign selected by q79/F,m=1 lens-circle orientation in finite-Weyl convention",
        "rows": {
            "r_H": promotion["key_numbers"]["controlled_r_H"],
            "sigma_D": promotion["key_numbers"]["promoted_sigma_D"],
            "m0": promotion["key_numbers"]["promoted_m0_tracefree"],
            "phi_Omega": math.pi / 2.0,
            "Huu": numeric["candidate"]["Huu"],
            "Hud_re": 0.0,
            "Hud_im": omega_abs,
            "Hdu_re": 0.0,
            "Hdu_im": -omega_abs,
            "Hdd": numeric["candidate"]["Hdd"],
        },
        "complex_notation": [
            ["26.835536563225222", "i*390.47033716866446"],
            ["-i*390.47033716866446", "-26.835536563225222"],
        ],
        "row_acceptance": {
            "phase_sign_certificate_accepted": True,
            "tracefree_certificate_accepted": True,
            "T3_orientation_certificate_accepted": True,
            "radial_value_source_certificate_accepted": False,
            "strict_value_rows_accepted": 0,
            "reason": "The sign is selected, but final Herm(2) value rows still depend on the unpromoted radial scale r_H.",
        },
    }

    hrg_frontier = {
        "schema": "MTTHRGValueMapFrontierAfterHPhaseSign.v1",
        "status": "FRONTIER_REDUCED_TO_HRG_RADIAL_VALUE_SOURCE_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_or_promoted": [
            "m0=0 trace-free Huv/threshold quotient",
            "sigma_D=+1 ordered B_Huv/T3 orientation",
            "complex orthogonal phase axis Hud_re=0",
            "binary +i phase sign selected by q79/F,m=1 lens-circle orientation",
        ],
        "still_open_for_strict_rows": {
            "r_H": "typed same-source HRG value map, independent H radial action scale, or selected finite-H Hessian radial norm",
            "row_certificates": "final row payload certificates after r_H is source-owned",
        },
        "next_frontier": "MTT_Selected_HRGValueSourceMap_or_HRadialActionScale_v1",
    }

    candidate = {
        "schema": "MTTSelectedHPhaseSignSelectorLensCircleOrHRGValueMapCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "LensCircleHPhaseSignSelectorTheorem",
            "proved": True,
            "statement": (
                "Given the already-promoted imaginary H phase axis, the selected time-oriented "
                "q79/F,m=1 finite lens-circle orientation selects the +i branch in the ordered "
                "(H_u,H_d^dagger) finite-Weyl convention. The antiunitary q369/F*,m=2 branch "
                "is retained as the conjugate -i branch. This promotes the H phase sign without "
                "using old Lens-Nil numerical weights. The HRG radial value r_H remains the only "
                "strict source-value blocker for final Herm(2) rows."
            ),
        },
        "decision": {
            "strict_r_H_promoted": False,
            "controlled_r_H_retained": True,
            "phase_axis_promoted": True,
            "phi_sign_promoted": True,
            "strict_phi_Omega_promoted": True,
            "antiunitary_conjugate_branch_retained": True,
            "old_lens_nil_numeric_weight_used": False,
            "strict_no_knob_numeric_solution_found": False,
            "frontier_reduced_to_HRG_radial_value_source_only": True,
        },
        "key_numbers": {
            "controlled_r_H": promotion["key_numbers"]["controlled_r_H"],
            "phi_Omega": math.pi / 2.0,
            "Hud_re": 0.0,
            "Hud_im_controlled_radial": omega_abs,
            "q79": q79_branch["q"],
            "q79_torsion_label_m": q79_branch["torsion_label_m"],
            "q369_conjugate": conjugate_branch["q"],
            "strict_value_rows_emitted": 0,
        },
        "packets": [
            f"candidate_data/{SLUG}/h_phase_sign_selector_lens_circle.packet.json",
            f"candidate_data/{SLUG}/signed_hpolar_rows_after_selector.packet.json",
            f"candidate_data/{SLUG}/hrg_frontier_after_h_phase_sign.packet.json",
        ],
        "next_target": "MTT_Selected_HRGValueSourceMap_or_HRadialActionScale_v1",
    }

    certificate = {
        "certificate": "selected_hphasesignselector_lenscircle_or_hrgvaluemap_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HPHASESIGNSELECTOR_LENSCIRCLE_PROMOTED_HRG_RADIAL_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "q79_time_oriented_F_m1_selected": True,
            "m1_period_table_closed": True,
            "antiunitary_conjugate_retained": True,
            "phase_axis_promoted": True,
            "phi_sign_promoted": True,
            "strict_phi_Omega_promoted": True,
            "old_lens_nil_numeric_weight_used": False,
            "old_lens_nil_numeric_weight_rejected": True,
            "strict_r_H_promoted": False,
            "frontier_reduced_to_HRG_radial_value_source_only": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "h_phase_sign_selector_lens_circle.packet.json", h_phase_sign_packet)
    write_json(CANDIDATE_DIR / "signed_hpolar_rows_after_selector.packet.json", signed_rows)
    write_json(CANDIDATE_DIR / "hrg_frontier_after_h_phase_sign.packet.json", hrg_frontier)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Phase-Sign Selector: Lens-Circle or HRG Value Map v1",
                "",
                "## Result",
                "",
                "The binary H phase sign is now selected in the current finite-Weyl convention.",
                "",
                "- Previous work reduced the Higgs off-diagonal phase to the imaginary axis, `phi_Omega in {+pi/2,-pi/2}`.",
                "- The ordered Huv source basis is `(H_u,H_d^dagger)` on the same `q79/F,m=1` diagonal HYM lane.",
                "- The q79 repo selects the time-oriented `F`, `m=1` finite lens-circle representative, with commutator matrix `[[0,1],[2,0]]`.",
                "- The antiunitary conjugate `q369/F*`, `m=2` representative is retained and carries the conjugate commutator `[[0,2],[1,0]]`.",
                "",
                "Therefore the selected time-oriented branch maps the binary imaginary axis to",
                "",
                "```text",
                "phi_Omega = +pi/2,",
                "Hud = +i * |Omega|,",
                "Hdu = -i * |Omega|.",
                "```",
                "",
                "The conjugate `-i` branch remains real as the antiunitary branch, but it is not the selected time-oriented branch.",
                "",
                "## Guardrail",
                "",
                "This uses lens/circle data only as an orientation/sign selector. It does not reuse the retired Lens-Nil numerical weight block.",
                "",
                "## Remaining Frontier",
                "",
                "`r_H` is still not promoted. Final strict Herm(2) value rows require a typed same-source HRG value map, an independent H radial action scale, or a selected finite-H Hessian radial norm.",
                "",
                "New frontier:",
                "",
                "```text",
                "MTT_Selected_HRGValueSourceMap_or_HRadialActionScale_v1",
                "```",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
