from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
STATUS = (
    "MTT_U6_HIDDEN_FULL_SU9_HOLONOMY_CLOSED_VISIBLE_C3_TOPOLOGICAL_AND_"
    "SPECTRAL_CANDIDATES_CLOSED_TWISTED_HOLOMORPHIC_HYM_BIANCHI_LIFT_OPEN"
)
NEXT = "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1.md"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def stable_k3_discriminant_lower_bound(rank: int) -> Fraction:
    return Fraction(rank * rank - 1, rank)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    iwasawa = outputs["Iwasawa_source_validity"]
    topology = outputs["shared_circle_clutching"]
    spectral = outputs["q79_spectral_cover"]
    holonomy = outputs["hidden_full_holonomy"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A103 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A103 next changed")
    require(all(candidate["checks"].values()), "one or more A103 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")
    require(candidate["results"]["hidden_full_SU9_holonomy_proved"], "hidden holonomy not closed")
    require(not candidate["results"]["actual_FuYau_balanced_HYM_proved"], "visible HYM overclaimed")
    require(not candidate["results"]["actual_FuYau_nonpullback_Bianchi_proved"], "visible Bianchi overclaimed")

    # Independent differential-form and global-frame checks.
    require(not iwasawa["printed_invariant_forms"]["c_closed"], "Iwasawa c promoted to closed")
    require(iwasawa["line_bundle_gate"]["invalid_line_bundle_c1_count"] == 4, "wrong nonclosed line count")
    require(not iwasawa["Dolbeault_gate"]["integrable"], "printed A01 promoted")
    require(iwasawa["global_frame_gate"]["Chern_classes_of_trivial_smooth_rank3_bundle"] == [0, 0, 0], "trivial bundle Chern classes changed")
    require(not iwasawa["global_frame_gate"]["compatible"], "trivial frame accepted with c3=6")
    require(not iwasawa["verdict"]["may_source_c3_equal_6_proof"], "invalid Iwasawa source reused")

    # Independent Gysin/Kunneth arithmetic for X=P_delta x S1.
    p_betti = topology["rank_one_FuYau_topology"]["P_delta_betti"]
    x_betti = topology["rank_one_FuYau_topology"]["X_betti"]
    require(p_betti == [1, 0, 21, 21, 0, 1], "P_delta Betti numbers")
    require(x_betti == [1, 1, 21, 42, 21, 1, 1], "Fu-Yau Betti numbers")
    require(sum((-1) ** degree * value for degree, value in enumerate(x_betti)) == 0, "Fu-Yau Euler characteristic")
    require(topology["rank_one_FuYau_topology"]["H4_P_delta_rank"] == 0, "slice c2 does not vanish topologically")
    require(topology["rank_one_FuYau_topology"]["H5_P_delta_rank"] == 1, "clutching winding group missing")
    require(topology["clutching_construction"]["integral_c3"] == [6, -6], "clutching c3")
    require(topology["clutching_construction"]["unselected_discrete_winding"] == [3, -3], "clutching winding")
    require(topology["clutching_construction"]["nonpullback"], "clutching bundle called pullback")
    require(not topology["same_branch_guard"]["integrable_holomorphic_structure_constructed"], "topological witness overpromoted")
    require(not topology["same_branch_guard"]["differential_Bianchi_representative_checked"], "Bianchi silently reused")

    # Independent genus-two/FMW arithmetic.
    require(spectral["q79_genus_two_map"]["H_square"] == 2, "q79 polarization changed")
    require(spectral["q79_genus_two_map"]["genus"] == 2, "genus calculation")
    require(spectral["q79_genus_two_map"]["h0_H"] == 3, "linear-system dimension")
    require(spectral["determinant_zero_cover"]["degree_over_K3"] == 3, "spectral degree")
    require(spectral["determinant_zero_cover"]["fiberwise_determinant"] == 0, "spectral determinant")
    require(not spectral["determinant_zero_cover"]["projective_identification_selected"], "PGL3 alignment invented")
    require(spectral["determinant_zero_cover"]["PGL3_alignment_complex_dimension"] == 8, "PGL3 alignment dimension")
    lam = Fraction(spectral["sectioned_reference_FMW_check"]["lambda"])
    require(lam == Fraction(3, 2), "spectral lambda")
    require(2 * lam * 2 == 6, "spectral c3 arithmetic")
    vertical_c2 = Fraction(1, 2) * (lam**2 - Fraction(1, 4)) * 3 * 2
    require(vertical_c2 == 6, "spectral c2 arithmetic")
    require(spectral["sectioned_reference_FMW_check"]["spectral_line_c1_coefficients"] == {"sigma": 6, "eta": -1, "c1_base": 5}, "spectral line integrality")
    require(spectral["sectioned_reference_FMW_check"]["same_c3_as_shared_circle_clutching"], "two c3 paths disagree")
    require(not spectral["q79_arithmetic_clue"]["source_map_in_corpus"], "q7/lambda coincidence promoted")
    require(not spectral["principal_FuYau_lift_gate"]["global_cover_to_bundle_surjectivity_proved"], "gerbe lift invented")
    require(not spectral["principal_FuYau_lift_gate"]["sectioned_reference_c2_matches_A102_visible_nine"], "c2 mismatch hidden")

    # Independent rank-nine holonomy exclusions.
    require(holonomy["input_bundle"]["rank"] == 9, "hidden rank")
    require(holonomy["input_bundle"]["c2"] == 11, "hidden c2")
    require(holonomy["holonomy_reduction"]["connected"], "hidden holonomy disconnected")
    require(holonomy["holonomy_reduction"]["irreducible"], "hidden holonomy reducible")
    proper = holonomy["proper_case_exclusions"]
    require(proper["SO9"]["required_c2_parity"] == "even" and proper["SO9"]["actual_c2"] % 2 == 1, "SO9 parity exclusion")
    sym8_index = math.comb(10, 3)
    require(sym8_index == 120, "Sym8 Dynkin index")
    rank2_bound = stable_k3_discriminant_lower_bound(2)
    require(sym8_index * rank2_bound == 180, "Sym8 Mukai bound")
    rank3_bound = stable_k3_discriminant_lower_bound(3)
    require(rank3_bound == Fraction(8, 3), "rank-three Mukai bound")
    require(3 * rank3_bound + 3 * rank3_bound == 16, "3x3 tensor bound")
    require(proper["A1_Sym8"]["excluded"], "Sym8 not excluded")
    require(proper["three_by_three_tensor"]["Brauer_obstruction_allowed_in_test"], "Brauer case assumed away")
    require(proper["three_by_three_tensor"]["excluded"], "Brauer-twisted tensor not excluded")
    require(holonomy["conclusion"]["HYM_holonomy"] == "SU9", "full SU9 conclusion")
    require(holonomy["conclusion"]["embedded_E8_commutant"] == "Z3", "hidden commutant")
    require(holonomy["conclusion"]["continuous_hidden_gauge_rank"] == 0, "hidden continuous gauge factor")
    require(not holonomy["conclusion"]["hidden_gaugino_condensate_available"], "hidden condensate retained")
    require(not holonomy["conclusion"]["hidden_bundle_modulus_selected"], "hidden modulus invented")

    require(frontier["hidden_branch_update"]["full_SU9_holonomy"], "frontier lost holonomy result")
    require(not frontier["hidden_branch_update"]["f_hidden_condensate_row_required"], "frontier asks for absent condensate")
    require(frontier["hidden_branch_update"]["threshold_row_required"], "threshold gap hidden")
    require(frontier["visible_branch_update"]["topological_c3_plusminus6_existence"], "topological c3 result lost")
    require(not frontier["visible_branch_update"]["actual_holomorphic_HYM_bundle"], "visible source overclosed")
    require(len(frontier["not_closed_here"]) == 6, "remaining frontier changed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")
    require(frontier["unfixed_spectral_alignment_complex_dimension"] == 8, "spectral alignment hidden")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A103 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Iwasawa correction",
        "Shared-circle clutching theorem",
        "integral c3(E_g)=2k",
        "q79 genus-two spectral cover",
        "unfixed `PGL(3)` alignment",
        "c3=2 lambda H^2=6",
        "Full hidden SU9 holonomy",
        "Hol(W9)=SU(9)",
        "Delta(A tensor B)=3 Delta(A)+3 Delta(B)",
        "inverse-gerbe twisted rank-one spectral object",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A103 q79 non-pullback chirality/full-SU9-holonomy audit: PASS")
    print(f"status={STATUS}")
    print("hidden Hol(W9)=SU9; E8 commutant=Z3; hidden condensate absent")
    print("visible topological c3=+/-6 and determinant-zero spectral cover closed")
    print("actual Fu-Yau gerbe lift/HYM/Bianchi remains open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
