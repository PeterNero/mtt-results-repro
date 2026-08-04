from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
STATUS = "MTT_U6_Q79_ELLIPTIC_MODULUS_REDUCED_TO_Z4_CHERN_ORBIT_BRIDGE_MARKED_K3_AND_PERIOD_ZERO_OPEN"
NEXT = "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    stabilizer = outputs["single_branch_order4_stabilizer_nogo"]
    orbit = outputs["Z4_Chern_orbit_superset"]
    modulus = outputs["order4_elliptic_modulus_selection"]
    bridge = outputs["complex_nesting_retarded_bridge_gate"]
    open_k3 = outputs["splitting_conic_K3_open_selector"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A107 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A107 next changed")
    require(all(candidate["checks"].values()), "one or more A107 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")

    exact = stabilizer["exact_stabilizer"]
    require(exact["matrices"] == "Stab(c0)={[[1,n],[0,1]]: n in Z}", "wrong Chern stabilizer")
    require(exact["finite_order_subgroup"] == "identity only", "single-branch torsion")
    require("order-two" in exact["allowing_sign"] and "no order-four" in exact["allowing_sign"], "sign quotient error")
    quarter = stabilizer["quarter_turn_test"]
    require(quarter["J"] == [[0, -1], [1, 0]], "quarter-turn matrix")
    require(quarter["J_squared"] == [[-1, 0], [0, -1]], "J square")
    require(quarter["J_fourth"] == [[1, 0], [0, 1]], "J fourth")
    require(quarter["J_c0"] == [0, 1], "J action on Chern vector")
    require(not quarter["preserves_single_branch"], "single branch falsely invariant")
    require(stabilizer["theorem"]["proved"], "single-branch no-go not proved")

    require(orbit["orbit_length"] == 4, "Chern orbit length")
    require(
        orbit["orbit"] == [["delta", 0], [0, "delta"], ["-delta", 0], [0, "-delta"]],
        "Chern orbit members",
    )
    cost = orbit["Bianchi_and_cost"]
    require(cost["each_curvature_norm_cost"] == 4, "orbit curvature cost")
    require(cost["each_source_free_allocation"] == "9+11+4=24", "orbit Bianchi allocation")
    require(cost["continuous_parameter_added"] == 0, "orbit added knob")
    covariance = orbit["gerbe_execution_covariance"]
    require(covariance["zero_invariant"], "gerbe zero not covariant")
    require(covariance["transversality_invariant"], "Jacobian transversality not covariant")
    require(covariance["one_period_execution_suffices_for_orbit"], "four executions incorrectly required")
    require(not orbit["symmetry_breaking_interpretation"]["typed_selector_currently_proved"], "branch selector invented")
    require(orbit["theorem"]["proved"], "orbit theorem not proved")

    modular = modulus["modular_action"]
    require(modular["action_on_tau"] == "tau -> -1/tau", "modular action")
    require(modular["fixed_point_equation"] == "tau=-1/tau", "fixed equation")
    require(modular["upper_half_plane_solution"] == "tau=i", "square modulus")
    require(modular["j_invariant"] == 1728, "square j invariant")
    logic = modulus["selection_logic"]
    require(not logic["local_orthogonal_complex_structure_selects_tau"], "local J overpromoted")
    require(logic["global_integral_order4_automorphism_selects_tau_i"], "global order4 implication")
    require(not logic["single_branch_supplies_that_automorphism"], "single branch supplies J")
    require(logic["Z4_orbit_superset_supplies_it_conditionally"], "conditional superset implication")
    count = modulus["source_count"]
    require(count["strict_current_unselected_complex_moduli"] == 19, "strict source count")
    require(count["conditional_Z4_parent_unselected_complex_moduli"] == 18, "conditional source count")
    require(count["new_fitted_parameters"] == 0, "modulus fit added")
    require(modulus["theorem"]["proved"], "elliptic modulus theorem not proved")

    support = bridge["corpus_support"]
    require(support["orthogonal_complex_structure_J2_minus1"], "complex nesting support lost")
    require(support["lens_quarter_turn_structurally_plausible"], "lens clue lost")
    require(not support["global_FuYau_Chern_orbit_action_derived"], "corpus overclaimed")
    imported = bridge["U9_retarded_import"]
    require(imported["q79_q369_antiunitary_orbit_closed"], "U9 orbit lost")
    require(imported["retarded_q79_representative_closed"], "U9 retarded branch lost")
    require(not imported["global_carrier_geometry_unique"], "U9 global carrier overclosed")
    require(not imported["typed_map_to_Z4_Chern_orbit"], "U9 cross-promoted")
    decision = bridge["decision"]
    require(not decision["tau_i_strictly_promoted"], "tau=i strictly promoted")
    require(decision["tau_i_conditional_superset_candidate"], "conditional tau route missing")
    require(decision["single_branch_tau_i_selector_retired"], "bad single-branch route retained")
    require(not decision["observed_data_used"], "observed selector used")
    require(bridge["missing_source_theorem"]["name"] == "LensQuarterTurnToFuYauChernOrbitSourceTheorem", "bridge target changed")

    require(not any(open_k3["acceptance"].values()), "open K3 selector accepted")
    require(open_k3["conditional_Z4_route"]["remaining_K3_complex_moduli"] == 18, "conditional K3 count")
    require("existence" in open_k3["direct_existence_route"]["role"], "direct route scope")

    require(frontier["strict_current_source_moduli_complex"] == 19, "frontier strict count")
    require(frontier["conditional_Z4_superset_source_moduli_complex"] == 18, "frontier conditional count")
    require(not frontier["strict_tau_i_selected"], "frontier tau overclosed")
    require(frontier["conditional_tau_i_selected_if_bridge"], "frontier conditional tau missing")
    require(not frontier["marked_K3_selected"], "marked K3 invented")
    require(not frontier["beta_C_zero_proved"], "gerbe zero invented")
    require(not frontier["isolated_alignment_found"], "alignment invented")
    require(not frontier["actual_FuYau_balanced_HYM_proved"], "HYM overclosed")
    require(not frontier["actual_FuYau_nonpullback_Bianchi_proved"], "Bianchi overclosed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A107 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Single-branch order-four no-go",
        "Stab(c0)={[[1,n],[0,1]] : n in Z}",
        "Minimal Z4 Chern-orbit superset",
        "When order four selects tau=i",
        "j(E)=1728",
        "Corpus and retarded guard",
        "LensQuarterTurnToFuYauChernOrbitSourceTheorem",
        "strict present branch: 19 unselected complex geometric moduli",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A107 q79 elliptic source and Z4 Chern-orbit audit: PASS")
    print(f"status={STATUS}")
    print("single branch: no order-four stabilizer; direct tau=i shortcut retired")
    print("minimal superset: four Chern orientations; one gerbe execution suffices")
    print("conditional order-four parent fixes tau=i, reducing source moduli 19 -> 18")
    print("typed lens-to-FuYau bridge, marked K3, exact gerbe zero, HYM and Bianchi remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
