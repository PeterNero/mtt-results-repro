from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79pgl3toprymgerbejacobianexecution"
STATUS = "MTT_U6_Q79_GERBE_ZERO_REDUCED_TO_SPLITTING_CONIC_RELATIVE_PERIOD_SYSTEM_MARKED_SOURCE_OPEN"
NEXT = "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1.md"


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
    normal = outputs["splitting_conic_K3_normal_form"]
    deligne = outputs["relative_Deligne_zero_criterion"]
    jac = outputs["residue_period_Jacobian_formula"]
    source = outputs["same_branch_source_reduction"]
    open_input = outputs["marked_geometry_open_input"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A106 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A106 next changed")
    require(all(candidate["checks"].values()), "one or more A106 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")

    roots = normal["root_calculation"]
    require(roots["R_plus_squared"] == roots["R_minus_squared"] == -2, "wrong lattice roots")
    require(roots["H_dot_R_plus"] == roots["H_dot_R_minus"] == 2, "wrong root degree")
    require(roots["R_plus_dot_R_minus"] == 6, "wrong split-conic intersection")
    require(roots["K3_Riemann_Roch_chi_for_each_root"] == 1, "wrong K3 RR value")
    model = normal["double_sextic_model"]
    require(model["normal_form"] == "F6=G3^2+Q2*H4", "normal form changed")
    require(model["marked_class"] == "delta=R_+-H=(R_+-R_-)/2", "delta marking changed")
    count = normal["parameter_count"]
    require(count["result"] == count["lattice_period_domain_dimension"] == 18, "K3 moduli count")
    require(count["count_matches"], "splitting family does not fill period domain")
    require(normal["theorem"]["proved"], "splitting-conic theorem not closed")

    exp = deligne["exponential_sequence"]
    require(exp["DD_alpha_C"] == 0, "A104 DD zero lost")
    require("image(H^2(C,Z)" in exp["zero_criterion"], "integral zero criterion missing")
    relative = deligne["relative_mapping_cone"]
    require(relative["relative_lift_exists"], "relative lift missing")
    tf = deligne["trace_free_projection"]
    require(tf["H2_O_C_dimension"] == 9, "ambient H2O dimension")
    require(tf["ambient_trace_dimension"] == 1, "trace dimension")
    require(tf["active_trace_free_dimension"] == 8, "Prym dimension")
    require(tf["H2_C_Z_rank"] == 92, "integral H2 rank")
    require("need not be a discrete lattice" in tf["projected_integral_group_warning"], "exactness warning missing")
    require(deligne["theorem"]["proved"], "relative Deligne theorem not closed")

    family = jac["spectral_family"]
    require(family["dimension_V"] == 9, "spectral section dimension")
    require(family["compact_parameter_space"] == "P(V)=P8", "P8 compactification")
    require("PGL3" in family["smooth_invertible_tensor_open_orbit"], "PGL3 orbit")
    residue = jac["trace_free_residue_basis"]
    require("Res_C_A" in residue["residue_formula"], "residue formula missing")
    periods = jac["period_system"]
    require("Z^92" in periods["fixed_integral_branch"], "integral branch dimension")
    require("Pi_rI" in periods["eight_equations"], "period congruence absent")
    cov = jac["covariant_Jacobian"]
    require(cov["shape"] == [8, 8], "Jacobian shape")
    require("nabla_s Pi_rI" in cov["formula"], "period derivative omitted")
    require("Gauss-Manin" in cov["connection"], "Gauss-Manin typing missing")
    require(jac["certified_execution"]["Jacobian_entries_as_source_inputs"] == 0, "Jacobian rows treated as source")
    require(jac["certified_execution"]["beta_coordinates_as_source_inputs"] == 0, "beta rows treated as source")

    primitive = source["primitive_geometric_source"]
    require(primitive["marked_lattice_polarized_K3_complex_moduli"] == 18, "K3 source count")
    require(primitive["elliptic_modulus_complex_moduli"] == 1, "elliptic source count")
    require(primitive["total_unselected_complex_moduli"] == 19, "total source count")
    require(primitive["alignment_complex_unknowns_solved_by_F"] == 8, "alignment equation count")
    require(primitive["independent_beta_rows"] == primitive["independent_period_Jacobian_rows"] == 0, "derived rows reopened")
    crossuse = source["tau_i_crossuse"]
    require(crossuse["available_value"] == "tau=i", "diagnostic tau missing")
    require(not crossuse["same_FuYau_K3_torus_source_theorem"], "tau=i cross-promoted")
    require("diagnostic" in crossuse["allowed_use"], "tau=i scope widened")
    guard = source["upstream_selection_guard"]
    require(not guard["rank_one_FuYau_topology_selected_by_MTT"], "A102 conditional premise promoted")
    require(source["new_fitted_observable_parameters"] == 0, "observable fit added")

    marked = open_input["marked_double_sextic"]
    require(len(marked["Q2_coefficients_6"]) == 6, "Q2 input shape")
    require(len(marked["G3_coefficients_10"]) == 10, "G3 input shape")
    require(len(marked["H4_coefficients_15"]) == 15, "H4 input shape")
    require(not any(open_input["acceptance"].values()), "open A106 input accepted")
    matrix = open_input["outputs"]["covariant_Jacobian_8x8"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "open Jacobian template")
    require(all(value is None for row in matrix for value in row), "Jacobian values fabricated")

    reduction = frontier["source_reduction"]
    require(reduction["A105_apparent_independent_Jacobian_entries"] == 64, "A105 matrix count")
    require(reduction["A105_apparent_independent_beta_entries"] == 8, "A105 beta count")
    require(reduction["A106_independent_Jacobian_or_beta_entries"] == 0, "A106 source reduction")
    require(not frontier["beta_C_zero_proved"], "gerbe zero overclosed")
    require(not frontier["isolated_alignment_found"], "alignment invented")
    require(not frontier["actual_FuYau_balanced_HYM_proved"], "HYM overclosed")
    require(not frontier["actual_FuYau_nonpullback_Bianchi_proved"], "Bianchi overclosed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A106 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Splitting-conic K3 theorem",
        "F6=G3^2+Q2 H4",
        "Exact analytic-Brauer zero",
        "Eight explicit residue rows",
        "Correct 8 by 8 system",
        "F_r(A,ell)=z_r(A)-sum_I Pi_rI(A) ell_I=0",
        "Source reduction and guardrails",
        "no theorem identifies it with the elliptic fiber",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A106 q79 PGL3-to-Prym relative-period execution audit: PASS")
    print(f"status={STATUS}")
    print("marked K3 normal form: w^2=G3^2+Q2 H4; moduli=18")
    print("global gerbe zero: 8 period congruences on an integral H2 branch")
    print("A105 beta/Jacobian source rows reduced from 8+64 to zero derived inputs")
    print("selected marked K3, same-branch tau, exact zero, HYM and Bianchi remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
