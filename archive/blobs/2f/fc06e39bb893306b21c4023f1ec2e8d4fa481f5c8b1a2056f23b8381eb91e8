"""Audit the H phase-sign selector from the q79 lens-circle orientation."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hphasesignselector_lenscircle_or_hrgvaluemap"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def near(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    selector = read_json(f"candidate_data/{SLUG}/h_phase_sign_selector_lens_circle.packet.json")
    rows = read_json(f"candidate_data/{SLUG}/signed_hpolar_rows_after_selector.packet.json")
    frontier = read_json(f"candidate_data/{SLUG}/hrg_frontier_after_h_phase_sign.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["phase_axis_promoted"] is True, "phase axis must be promoted")
    require(candidate["decision"]["phi_sign_promoted"] is True, "phase sign must be promoted")
    require(candidate["decision"]["strict_phi_Omega_promoted"] is True, "strict phi must be promoted")
    require(candidate["decision"]["strict_r_H_promoted"] is False, "r_H must remain open")
    require(candidate["decision"]["strict_no_knob_numeric_solution_found"] is False, "strict full closure must remain open")
    require(candidate["decision"]["frontier_reduced_to_HRG_radial_value_source_only"] is True, "frontier reduction mismatch")

    require(selector["source_basis"]["ordered_basis"] == ["H_u", "H_d^dagger"], "Huv basis mismatch")
    require("q79/F,m=1" in selector["source_basis"]["same_source_branch"], "Huv branch must be q79/F,m=1")
    require(selector["phase_axis_input"]["previous_axis_promoted"] is True, "previous axis must be promoted")
    require(selector["phase_axis_input"]["previous_sign_promoted"] is False, "previous sign should have been open")
    require(selector["phase_axis_input"]["axis_options"] == ["pi/2", "-pi/2"], "axis options mismatch")

    q79 = selector["lens_circle_selector"]["time_oriented_branch"]
    conj = selector["lens_circle_selector"]["antiunitary_conjugate_branch"]
    require(q79["q"] == 79, "selected q mismatch")
    require(q79["orientation"] == "F", "selected orientation mismatch")
    require(q79["torsion_label_m"] == 1, "selected torsion label mismatch")
    require(q79["selected"] is True, "q79 branch not selected")
    require(conj["q"] == 369, "conjugate q mismatch")
    require(conj["orientation"] == "F*", "conjugate orientation mismatch")
    require(conj["torsion_label_m"] == 2, "conjugate torsion label mismatch")
    require(conj["retained"] is True, "conjugate branch must be retained")
    require(selector["lens_circle_selector"]["m1_commutator_matrix_mod3"] == [[0, 1], [2, 0]], "m1 commutator mismatch")
    require(selector["lens_circle_selector"]["m2_conjugate_commutator_matrix_mod3"] == [[0, 2], [1, 0]], "m2 commutator mismatch")
    require(selector["lens_circle_selector"]["m1_period_table_closed"] is True, "m1 period table not closed")
    require(
        selector["lens_circle_selector"]["m1_matches_qutrit_F_orientation"] is True,
        "m1 should match qutrit F orientation",
    )
    require(
        selector["lens_circle_selector"]["ordinary_bundle_coboundary_ruled_out"] is True,
        "ordinary coboundary escape should be ruled out",
    )
    require(selector["lens_circle_selector"]["finite_operator_parity_closed"] is True, "operator parity not closed")
    require(
        selector["lens_circle_selector"]["finite_operator_cp_odd_sign_flips_under_conjugation"] > 0,
        "conjugation should flip CP-odd signs",
    )

    require(
        selector["orientation_transfer_rule"]["static_cp_orientation_support"] is True,
        "static CP orientation support missing",
    )
    require(
        selector["orientation_transfer_rule"]["same_active_shift_positive_orientation_support"] is True,
        "same active shift orientation support missing",
    )
    require(
        selector["orientation_transfer_rule"]["old_lens_nil_numeric_weight_used"] is False,
        "old Lens-Nil numeric weight must not be used",
    )
    require(
        selector["orientation_transfer_rule"]["old_lens_nil_numeric_weight_rejected_by_guard"] is True,
        "Lens-Nil guard must be active",
    )

    require(selector["selected_phase"]["phi_Omega_label"] == "+pi/2", "phase label mismatch")
    require(near(selector["selected_phase"]["phi_Omega_radians"], math.pi / 2.0), "phase value mismatch")
    require(selector["selected_phase"]["Hud_re"] == 0.0, "Hud real part must vanish")
    require(selector["selected_phase"]["Hud_im_sign"] == 1, "Hud sign mismatch")
    require(selector["selected_phase"]["conjugate_branch_phase_label"] == "-pi/2", "conjugate phase mismatch")
    require(selector["selected_phase"]["conjugate_branch_retained"] is True, "conjugate phase should be retained")

    require(rows["row_acceptance"]["phase_sign_certificate_accepted"] is True, "phase sign cert not accepted")
    require(rows["row_acceptance"]["radial_value_source_certificate_accepted"] is False, "radial value should remain open")
    require(rows["row_acceptance"]["strict_value_rows_accepted"] == 0, "strict rows must remain zero")
    require(rows["rows"]["Hud_re"] == 0.0, "signed row Hud_re mismatch")
    require(rows["rows"]["Hud_im"] > 0.0, "signed row Hud_im should be positive")
    require(rows["rows"]["Hdu_im"] < 0.0, "signed row Hdu_im should be negative")

    require(frontier["next_frontier"] == "MTT_Selected_HRGValueSourceMap_or_HRadialActionScale_v1", "next frontier mismatch")
    require(cert["checks"]["phi_sign_promoted"] is True, "cert sign mismatch")
    require(cert["checks"]["strict_r_H_promoted"] is False, "cert r_H mismatch")
    require(cert["checks"]["frontier_reduced_to_HRG_radial_value_source_only"] is True, "cert frontier mismatch")

    print("selected_hphasesignselector_lenscircle_or_hrgvaluemap audit: PASS")


if __name__ == "__main__":
    main()
