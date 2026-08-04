from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79twistedspectralgerbelifthymandbianchiexecution"
STATUS = (
    "MTT_U6_Q79_SPECTRAL_DD_RESTRICTION_ZERO_FLAT_ANALYTIC_BRAUER_"
    "RESIDUE_HYM_BIANCHI_OPEN"
)
NEXT = "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1.md"
)


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
    surface = outputs["spectral_surface"]
    dd = outputs["integral_DD_restriction"]
    analytic = outputs["flat_analytic_gerbe_gate"]
    open_input = outputs["flat_analytic_gerbe_open_input"]
    execution = outputs["HYM_Bianchi_gate"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A104 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A104 next changed")
    require(all(candidate["checks"].values()), "one or more A104 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")

    # Independent intersection, adjunction and Hodge arithmetic.
    divisor = surface["divisor"]
    require(divisor["H_square"] == 2, "H square changed")
    require(divisor["fiber_divisor_degree"] == 3, "spectral degree changed")
    require(divisor["A_squared_B"] == 2 * 3 == 6, "A^2 B")
    require(divisor["D_cubed"] == 3 * 6 == 18, "D^3")
    adjunction = surface["adjunction_and_Noether"]
    require(adjunction["K_C_squared"] == 18, "K_C^2")
    require(adjunction["c2_J_dot_C"] == 24 * 3 == 72, "c2(J).C")
    require(adjunction["integral_c2_C"] == 18 + 72 == 90, "c2(C)")
    require(adjunction["chi_O_C"] == (18 + 90) // 12 == 9, "chi(O_C)")
    hodge = surface["Lefschetz_and_Hodge"]
    require(hodge["q"] == 1, "irregularity")
    require(hodge["p_g"] == 9, "geometric genus")
    require(hodge["h11"] == 74, "h11")
    require(hodge["betti"] == [1, 2, 92, 2, 1], "Betti numbers")
    require(hodge["H3_C"] == "Z^2" and not hodge["H3_torsion"], "H3 torsion guard")

    # Independent integral restriction test.
    pairing = dd["restriction_pairing"]
    require(dd["principal_FuYau_input"]["torus_Chern_pair"] == ["delta", "0"], "rank-one Chern pair")
    require(pairing["delta_dot_H"] == 0, "q79 orthogonality lost")
    require(pairing["pair_with_u"] == pairing["pair_with_v"] == 0, "nonzero DD pairing")
    require(pairing["H3_C_torsion_free"], "torsion escape reopened")
    require(pairing["integral_DD_restriction_zero"], "integral DD restriction not closed")
    require(not dd["consequence"]["topological_gerbe_obstruction_on_C"], "topological obstruction retained")
    require(not dd["consequence"]["torsion_escape_remaining"], "torsion loophole retained")
    require(not dd["consequence"]["holomorphic_gerbe_triviality_proved"], "analytic triviality overclaimed")

    # The analytic remainder must stay explicit and unfilled.
    exp = analytic["exponential_sequence"]
    require(exp["DD_alpha_restricted"] == 0, "DD result not consumed")
    require(exp["H2_O_complex_dimension"] == 9, "flat-residue ambient dimension")
    require(exp["residual_is_one_selected_class_not_nine_fit_parameters"], "residue miscounted as knobs")
    require(not exp["beta_C_computed"] and not exp["beta_C_zero_proved"], "beta_C invented")
    rank_one = analytic["rank_one_spectral_object_gate"]
    require(rank_one["inverse_gerbe_twisted_rank_one_sheaf_exists_iff_beta_C_zero"], "rank-one gate mistyped")
    require(not rank_one["twisted_rank_one_sheaf_constructed"], "twisted sheaf invented")
    require(not rank_one["inverse_Fourier_Mukai_transform_executed"], "inverse transform invented")
    require(not rank_one["inverse_transform_locally_free"], "local freeness invented")
    require(not analytic["adjacent_repo_guardrails"]["q79_Iwasawa_order3_flat_gerbe"]["same_FuYau_spectral_source"], "adjacent q79 gerbe promoted")
    require(analytic["adjacent_repo_guardrails"]["Qa_SU3_minimal_gerbe_gate"]["allowed_use"] == "adjacent guardrail only", "Qa gerbe promoted")

    fields = open_input["required_same_branch_fields"]
    require(len(fields["beta_C_period_vector_length_9"]) == 9, "beta period template length")
    require(all(value is None for value in fields["beta_C_period_vector_length_9"]), "beta periods fabricated")
    require(not any(open_input["acceptance"].values()), "open input accepted without data")

    visible = execution["visible_bundle_chain"]
    require(visible["smooth_spectral_surface"] and visible["integral_DD_restriction_zero"], "closed gates lost")
    for key in [
        "holomorphic_gerbe_trivialization",
        "rank_one_twisted_spectral_object",
        "locally_free_rank3_inverse_transform",
        "SU3_determinant_condition",
        "actual_total_space_c3_plusminus6",
        "balanced_slope_stability",
        "balanced_HYM_connection",
    ]:
        require(not visible[key], f"visible gate overclosed: {key}")
    bianchi = execution["Bianchi_chain"]
    require(not bianchi["integrated_Bianchi_may_be_silently_reused"], "A102 Bianchi silently reused")
    require(not bianchi["differential_Bianchi_identity_verified"], "Bianchi overclosed")
    require(execution["hidden_branch_retained"]["full_SU9_holonomy"], "A103 hidden result lost")
    require(not execution["hidden_branch_retained"]["hidden_gaugino_condensate_available"], "hidden condensate reopened")

    require(frontier["integral_DD_restriction_zero"], "frontier lost DD theorem")
    require(not frontier["analytic_gerbe_residue_decided"], "frontier invented beta decision")
    require(not frontier["actual_FuYau_balanced_HYM_proved"], "frontier overclosed HYM")
    require(not frontier["actual_FuYau_nonpullback_Bianchi_proved"], "frontier overclosed Bianchi")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")
    require(frontier["next_required_artifact"] == NEXT, "wrong A104 next")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A104 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Spectral surface topology",
        "K_C^2 = 18",
        "H^3(C,Z)=Z^2",
        "Integral gerbe restriction theorem",
        "i^* DD(alpha)=0 in H^3(C,Z)",
        "The remaining analytic residue",
        "not nine fitted",
        "Explicit closing object",
        "Bianchi guard",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A104 q79 twisted-spectral gerbe/HYM/Bianchi audit: PASS")
    print(f"status={STATUS}")
    print("spectral C: K^2=18, c2=90, pg=9, h11=74")
    print("integral DD(alpha)|C=0 exactly; no H3 torsion escape")
    print("flat holomorphic beta_C, inverse FM, HYM and Bianchi remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
