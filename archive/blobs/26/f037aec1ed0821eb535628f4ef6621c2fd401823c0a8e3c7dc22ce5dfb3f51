"""Audit post-source Weyl coefficient-lift candidate packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
SEARCH = PACKET_DIR / "minimal_weyl_coefficient_lift_search.packet.json"
GAP = PACKET_DIR / "coefficient_lift_source_selection_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_weyl_coefficient_lift.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSourceWeylCoefficientLift_or_SecondOrderFlavorCandidate_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate.py"

STATUS = "MTT_SELECTED_POSTSOURCE_WEYLCOEFFICIENT_LIFT_BUILT_ALGEBRAIC_CANDIDATES_SOURCE_SELECTION_OPEN"
NEXT = "MTT_Selected_WeylCoefficientSourceSelection_or_HigherResponseEmission_v1"
TOL = 1e-9


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def approx(value: float, expected: float, tol: float = TOL) -> bool:
    return abs(value - expected) <= tol


def cp_imag(value: float | list[float]) -> float:
    if isinstance(value, list):
        return float(value[1])
    return 0.0


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    search = load(SEARCH)
    gap = load(GAP)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("search", search),
        ("gap", gap),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(search["status"] == "MINIMAL_ZX_COEFFICIENT_LIFT_SPLITS_AND_EMITS_CP_CANDIDATES", "search status mismatch")
    require(search["candidate_count"] == 4, "candidate count mismatch")
    require(search["all_branches_split_three_families"] is True, "not all branches split")
    require(search["all_branches_emit_nonzero_CP_odd_invariant"] is True, "not all branches emit CP")
    require(search["cp_orientation_branches"] == ["negative", "positive"], "orientation pair mismatch")
    require(search["first_layer_problem"]["formal_layer_twofold_degeneracy"] is True, "first layer gap not imported")
    require(search["first_layer_problem"]["formal_layer_CP_odd_invariant_nonzero"] is False, "first layer CP overclaimed")

    expected_cp = 972.0 * math.sqrt(3.0)
    orientations = []
    for branch in search["branches"]:
        require(branch["hermitian_spectrum_each_sector"] == [1.0, 4.0, 7.0], "spectrum mismatch")
        require(branch["three_distinct_family_masses"] is True, "branch does not split")
        require(approx(branch["commutator_norm_sq"], 324.0), "commutator norm mismatch")
        require(branch["CP_odd_invariant_nonzero"] is True, "CP not nonzero")
        require(branch["cp_odd_exact_magnitude"] == "972*sqrt(3)", "exact CP magnitude label mismatch")
        require(approx(abs(cp_imag(branch["cp_odd_trace_commutator_cubed"])), expected_cp), "CP magnitude mismatch")
        require(branch["promoted_as_selected_value"] is False, "branch overpromoted")
        orientations.append(branch["cp_odd_orientation"])
    require(sorted(set(orientations)) == ["negative", "positive"], "branch orientations not conjugate")

    require(gap["status"] == "ALGEBRAIC_WALL_BROKEN_SOURCE_SELECTION_OPEN", "gap status mismatch")
    require(gap["diagnostic_relation_to_prior_search"]["prior_diagnostic_splitter_found"] is True, "prior diagnostic not imported")
    require(gap["diagnostic_relation_to_prior_search"]["prior_selected_correction_promoted"] is False, "prior overpromoted")
    require(gap["selected_source_emits_coefficient_lift"] is False, "source selection overclaimed")
    require(gap["selected_higher_response_matrices_emitted"] is False, "higher response overclaimed")
    require("the [1,1] light-family degeneracy is not forced by the finite Weyl algebra" in gap["what_this_proves"], "degeneracy conclusion missing")
    require("that MTT selects lambda=1+omega or lambda=1+omega2" in gap["what_this_does_not_prove"], "source gap missing")

    closed = candidate["what_closes_now"]
    require(closed["minimal_second_order_weyl_lift_search_executed"] is True, "search not closed")
    require(closed["three_family_splitting_candidate_found"] is True, "three-family candidate missing")
    require(closed["nonzero_CP_candidate_found"] is True, "CP candidate missing")
    require(closed["CP_conjugate_orientation_pair_identified"] is True, "orientation pair missing")
    require(closed["algebraic_degeneracy_wall_rejected"] is True, "degeneracy wall not rejected")

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_lambda_source_theorem",
        "selected_higher_response_matrix_emission",
        "CP_orientation_selection_or_coexistence_theorem",
        "physical_CKM_PMNS_Yukawa_value_closure",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["algebraic_candidate_found"] is True, "candidate not found")
    require(decision["selected_source_emits_candidate"] is False, "selected source overclaimed")
    require(decision["physical_values_promoted"] is False, "physical values overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("Hermitian spectra              : [7,4,1]" in note, "note missing split spectra")
    require("|CP-odd commutator cube|       : 972*sqrt(3)" in note, "note missing CP magnitude")
    require("selected physical promotion    : false" in note, "note missing source guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
