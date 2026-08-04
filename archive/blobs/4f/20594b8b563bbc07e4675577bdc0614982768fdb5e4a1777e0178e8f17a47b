from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79projectivelinechartcovarianceandellzerocontinuation"
OUT = ROOT / "candidate_data" / SLUG
A122 = (
    ROOT
    / "candidate_data"
    / "selected_q79aligneddivisornormalfunctionsourceandpgl3branchdiagnosis.candidate.json"
)
A121_OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
DIAGNOSTIC = (
    A121_OUT
    / "pgl3_projective_line_chart_covariance_and_continuation.packet.json"
)
SEARCHES = [
    A121_OUT / f"pgl3_projective_ychart_zero_search_{index:02d}.exploratory.json"
    for index in range(1, 4)
] + [
    A121_OUT / f"pgl3_projective_ychart_broyden_{index:02d}.exploratory.json"
    for index in range(4, 6)
]
ENGINE = ROOT / "scripts" / "explore_q79_pgl3_beta_zero.py"
PROBE = ROOT / "scripts" / "q79_pgl3_beta_diagnostics.py"
SOLVER = ROOT / "scripts" / "solve_q79_pgl3_beta_zero_corrected.py"
BROYDEN = ROOT / "scripts" / "continue_q79_pgl3_beta_zero_broyden.py"
ANALYZER = ROOT / "scripts" / "analyze_q79_projective_line_chart_covariance.py"
THEOREM = OUT / "projective_line_chart_covariance_theorem.packet.json"
DECISION = OUT / "ell_zero_projective_continuation.open.json"
FRONTIER = OUT / "U6_frontier_after_A123.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


STATUS = (
    "MTT_U6_Q79_PROJECTIVE_LINE_CHART_COVARIANCE_CLOSED_"
    "ELL_ZERO_CONTINUED_TO_GENUINE_PL_BOUNDARY"
)
NEXT = "MTT_Selected_q79PicardLefschetzOneSidedResidualRegularization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    a122 = load(A122)
    diagnostic = load(DIAGNOSTIC)
    exact = diagnostic["exact_chart_checks"]
    covariance = diagnostic["same_branch_beta_chart_covariance"]
    continuation = diagnostic["ell_zero_continuation"]
    reclassification = diagnostic["A122_endpoint_reclassification"]

    if not a122["checks"]["aligned_source_chain_rule_exact"]:
        raise AssertionError("A122 aligned source theorem is unavailable")
    if not all(exact["homogeneous_degree_transition_residuals_zero"].values()):
        raise AssertionError("homogeneous projective chart covariance failed")
    if exact["residue_form_transition_residual"] != "0":
        raise AssertionError("residue form is not chart covariant")
    if exact["five_period_transition_determinant"] != "-1":
        raise AssertionError("five-period transition determinant changed")
    if covariance["maximum_absolute_difference"] >= 5.0e-5:
        raise AssertionError("same-branch beta chart comparison failed")
    if covariance["projective_overlap"] <= 0.999999:
        raise AssertionError("same-branch beta directions disagree")
    if covariance["base_lift_transition_maximum_absolute_residual"] >= 1.0e-12:
        raise AssertionError("base-lift chart transition is inaccurate")
    for endpoint in reclassification.values():
        if not isinstance(endpoint, dict) or "minimum_affine_branch_separation" not in endpoint:
            continue
        if endpoint["minimum_affine_branch_separation"]["z"] >= 1.0e-2:
            raise AssertionError("A122 endpoint did not reproduce the small z gap")
        if endpoint["minimum_affine_branch_separation"]["y"] <= 5.0e-2:
            raise AssertionError("A122 endpoint is not separated in the regular chart")
    norms = [float(value) for value in continuation["beta_norms"]]
    if len(norms) != 6 or not all(
        norms[index + 1] < norms[index] for index in range(len(norms) - 1)
    ):
        raise AssertionError("same-branch projective continuation is not monotone")
    if continuation["fresh_Jacobian_steps"] != 3:
        raise AssertionError("fresh projective Jacobian step count")
    if continuation["guarded_Broyden_steps"] != 2:
        raise AssertionError("guarded Broyden step count")
    if continuation["latest_projective_branch_separation"] <= 5.0e-3:
        raise AssertionError("latest accepted carrier crossed the PL guard")
    if diagnostic["decision"]["smooth_ell_zero_found"]:
        raise AssertionError("ell=0 zero was overpromoted")
    if diagnostic["decision"]["ell_zero_no_go_proved"]:
        raise AssertionError("ell=0 no-go was overpromoted")

    theorem = {
        "schema": "MTTQ79ProjectiveLineChartCovarianceTheorem.v1",
        "status": "EXACT_PROJECTIVE_LINE_CHART_COVARIANCE_CLOSED",
        "overlap_hypothesis": "ell_1*ell_2 != 0",
        "charts": {
            "z_elimination": (
                "X_z=(ell_2,ell_2*t_z,-(ell_0+ell_1*t_z))"
            ),
            "y_elimination": (
                "X_y=(ell_1,-(ell_0+ell_2*t_y),ell_1*t_y)"
            ),
            "transition": exact["transition"],
            "fiber_scaling": exact["fiber_scaling"],
        },
        "homogeneous_covariance": {
            "formula": (
                "P_z(t_z(t_y))=(ell_2/ell_1)^d*P_y(t_y) "
                "for every homogeneous degree-d polynomial P"
            ),
            "checked_degrees": exact[
                "homogeneous_degree_transition_residuals_zero"
            ],
            "covers": ["Q2", "G3", "H4", "F6"],
        },
        "normal_function_covariance": {
            "residue_form_transition_residual": exact[
                "residue_form_transition_residual"
            ],
            "reduced_period_basis_transition_determinant": exact[
                "five_period_transition_determinant"
            ],
            "same_integral_branch_condition": (
                "The five-component base lift must be transformed by the "
                "triangular period map; recomputing unrelated straight paths "
                "may add an integral period."
            ),
        },
        "theorem": {
            "name": "Q79ProjectiveLineChartCovarianceTheorem",
            "proved": True,
            "statement": (
                "On the overlap ell_1*ell_2 != 0, the z- and y-elimination "
                "descriptions define the same aligned splitting curve, Mumford "
                "divisor, residue one-forms, and five-component reduced lift. "
                "The period transition has determinant -1, so a vanishing "
                "affine z-root gap caused only by ell_2/ell_1 is not a "
                "Picard-Lefschetz degeneration."
            ),
        },
        "strict_scope": {
            "exact": True,
            "PGL3_zero_implied": False,
            "ell_zero_no_go_implied": False,
        },
    }
    dump(THEOREM, theorem)

    decision = {
        "schema": "MTTQ79EllZeroProjectiveContinuationDecision.v1",
        "status": "ELL_ZERO_CONTINUED_TO_GENUINE_PL_BOUNDARY_ZERO_OPEN",
        "A122_false_nodal_wall": {
            "retired": True,
            "reason": (
                "The small z-chart gap expands to a uniformly separated "
                "y-chart configuration under the exact projective transition."
            ),
            "exact_A122_aligned_source_preserved": True,
        },
        "same_branch_chart_audit": covariance,
        "beta_norm_chain": norms,
        "latest_beta_norm": norms[-1],
        "latest_projective_branch_separation": continuation[
            "latest_projective_branch_separation"
        ],
        "genuine_PL_boundary_localized": diagnostic["decision"][
            "genuine_Picard_Lefschetz_boundary_localized"
        ],
        "open": {
            "smooth_ell_zero_found": False,
            "ell_zero_no_go_proved": False,
            "one_sided_PL_limit_interval_certified": False,
            "nonzero_integral_branch_selected": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(DECISION, decision)

    frontier = {
        "schema": "MTTU6FrontierAfterA123.v1",
        "status": STATUS,
        "A121_normalized_Deligne_beta_representative_preserved": True,
        "A122_aligned_divisor_source_theorem_preserved": True,
        "projective_line_chart_covariance_closed": True,
        "A122_apparent_nodal_wall_retired": True,
        "ell_zero_search_advanced_beyond_old_chart_wall": True,
        "latest_ell_zero_beta_norm": norms[-1],
        "smooth_ell_zero_found": False,
        "ell_zero_no_go_proved": False,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A122,
        DIAGNOSTIC,
        *SEARCHES,
        ENGINE,
        PROBE,
        SOLVER,
        BROYDEN,
        ANALYZER,
        Path(__file__),
        THEOREM,
        DECISION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79ProjectiveLineChartCovarianceAndEllZeroContinuation.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79ProjectiveLineChartCovarianceAndEllZeroContinuation_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "theorem": str(THEOREM.relative_to(ROOT)).replace("\\", "/"),
            "decision": str(DECISION.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "projective_chart_covariance_exact": True,
            "residue_form_covariance_exact": True,
            "period_transition_determinant_minus_one": True,
            "same_ell_zero_branch_preserved_numerically": True,
            "A122_false_wall_retired": True,
            "PGL3_zero_invented": False,
            "ell_zero_no_go_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": "MTTSelectedQ79ProjectiveLineChartCovarianceAndEllZeroContinuation",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "projective_chart_covariance_theorem_closed": True,
        "A122_false_wall_retired": True,
        "ell_zero_beta_norm_advanced_to": norms[-1],
        "smooth_PGL3_zero_found": False,
        "global_no_go_proved": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(f"beta norm: {norms[0]:.6f} -> {norms[-1]:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
