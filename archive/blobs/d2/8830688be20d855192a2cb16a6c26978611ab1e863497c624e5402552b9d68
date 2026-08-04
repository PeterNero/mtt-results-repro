from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79picardlefschetzonesidedresidualregularization"
OUT = ROOT / "candidate_data" / SLUG
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation.candidate.json"
)
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_transverse_simple_node_and_transport_pl_jump.packet.json"
)
ANALYZER = ROOT / "scripts" / "analyze_q79_picard_lefschetz_wall.py"
ENGINE = ROOT / "scripts" / "explore_q79_pgl3_beta_zero.py"
NORMAL_FUNCTION = ROOT / "scripts" / "compute_q79genus2normalfunction.py"
THEOREM = OUT / "transported_picard_lefschetz_jump_theorem.packet.json"
DECISION = OUT / "one_sided_ell_zero_residual.open.json"
FRONTIER = OUT / "U6_frontier_after_A124.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


STATUS = (
    "MTT_U6_Q79_TRANSPORTED_PICARD_LEFSCHETZ_JUMP_FORMULA_CLOSED_"
    "INTERVAL_RESIDUAL_OPEN"
)
NEXT = "MTT_Selected_q79PicardLefschetzIntervalResidualCertificate_or_NonzeroIntegralBranch_v1"


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
    a123 = load(A123)
    packet = load(PACKET)
    wall = packet["wall"]
    one_sided = packet["one_sided_beta"]
    transported = packet["transported_Picard_Lefschetz_jump"]
    decision_in = packet["decision"]

    if not a123["checks"]["projective_chart_covariance_exact"]:
        raise AssertionError("A123 projective chart theorem is unavailable")
    if wall["maximum_F_and_Ft_residual"] >= 1.0e-9:
        raise AssertionError("simple-node wall solve is inaccurate")
    if not wall["simple_node"] or wall["absolute_f_tt"] <= 1.0:
        raise AssertionError("wall is not a simple node")
    if not wall["transverse_real_path_crossing"]:
        raise AssertionError("discriminant crossing is not transverse")
    if not wall["q_divisor_disjoint_from_node"]:
        raise AssertionError("splitting divisor meets the node")
    if wall["normalized_y_chart_scale"] <= 0.5:
        raise AssertionError("wall line chart is ill-conditioned")
    if min(wall["real_coupled_Jacobian_singular_values"]) <= 1.0:
        raise AssertionError("coupled wall Jacobian lost numerical rank")
    if one_sided["selected_side_limit_norm"] <= 2.0:
        raise AssertionError("selected-side floating limit collapsed")
    if one_sided["crossed_side_limit_norm"] <= 2.0:
        raise AssertionError("crossed-side floating limit collapsed")
    for side in ["selected_minus", "crossed_plus"]:
        if (
            one_sided["limits"][side][
                "linear_quadratic_vector_difference_norm"
            ]
            >= 5.0e-5
        ):
            raise AssertionError("one-sided extrapolation is not converged")
    if transported["projective_overlap_with_numerical_jump"] <= 0.999999999:
        raise AssertionError("transported PL jump direction mismatch")
    if transported["relative_residual_after_best_complex_scale"] >= 1.0e-5:
        raise AssertionError("transported PL jump residual too large")
    scale = transported["best_complex_scale_to_numerical_jump"]
    if abs(float(scale["real"]) - 1.0) >= 5.0e-4:
        raise AssertionError("transported PL jump coefficient is not unit")
    if abs(float(scale["imaginary"])) >= 5.0e-4:
        raise AssertionError("transported PL jump phase is not unit-oriented")
    if decision_in["selected_side_nonzero_interval_proved"]:
        raise AssertionError("interval residual was overpromoted")
    if decision_in["global_ell_zero_no_go_proved"]:
        raise AssertionError("global ell=0 no-go was overpromoted")

    theorem = {
        "schema": "MTTQ79TransportedPicardLefschetzJumpTheorem.v1",
        "status": "EXACT_LOCAL_TRANSPORTED_PL_JUMP_FORMULA_CLOSED",
        "hypotheses": {
            "simple_node": "f=f_t=0 and f_tt != 0",
            "transverse_crossing": "Im(du_star/ds) != 0",
            "source_regular_at_node": "q_A(t_star) != 0",
            "same_integral_branch": (
                "the A123 base lift is transformed, not recomputed on an "
                "unrelated Abel-Jacobi path"
            ),
        },
        "local_vanishing_state": {
            "formula": transported["local_vanishing_state_formula"],
            "orientation": (
                "positive node loop fixed by the sign of Im(du_star/ds)"
            ),
        },
        "endpoint_jump": {
            "formula": transported["endpoint_transport_formula"],
            "interpretation": (
                "The source cancels between the two continuations. Their "
                "difference solves the homogeneous Gauss-Manin equation; "
                "integrating its residue rows to the endpoint gives the beta jump."
            ),
        },
        "theorem": {
            "name": "Q79TransverseSimpleNodeTransportedPLJumpTheorem",
            "proved": True,
            "statement": packet["theorem"]["exact_statement"],
        },
        "instantiation_scope": {
            "formula_exact": True,
            "wall_coordinates_floating": True,
            "endpoint_transport_floating": True,
            "interval_nonzero_conclusion": False,
        },
    }
    dump(THEOREM, theorem)

    decision = {
        "schema": "MTTQ79OneSidedEllZeroResidualDecision.v1",
        "status": "UNIT_PL_JUMP_EXECUTED_INTERVAL_NONZERO_DECISION_OPEN",
        "wall": wall,
        "one_sided_limits": one_sided["limits"],
        "selected_side_limit_norm": one_sided["selected_side_limit_norm"],
        "crossed_side_limit_norm": one_sided["crossed_side_limit_norm"],
        "extrapolated_jump_norm": one_sided["extrapolated_jump_norm"],
        "transported_PL_comparison": {
            "limit_norm": transported["limit_norm"],
            "projective_overlap": transported[
                "projective_overlap_with_numerical_jump"
            ],
            "best_complex_scale": scale,
            "relative_residual": transported[
                "relative_residual_after_best_complex_scale"
            ],
        },
        "closed": {
            "transverse_simple_node_located_floating": True,
            "unit_PL_jump_executed_floating": True,
            "exact_local_jump_formula": True,
        },
        "open": {
            "selected_side_nonzero_interval_proved": False,
            "global_ell_zero_no_go_proved": False,
            "smooth_ell_zero_found": False,
            "selected_nonzero_integral_branch": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(DECISION, decision)

    frontier = {
        "schema": "MTTU6FrontierAfterA124.v1",
        "status": STATUS,
        "A121_normalized_Deligne_beta_representative_preserved": True,
        "A122_aligned_divisor_source_theorem_preserved": True,
        "A123_projective_chart_covariance_preserved": True,
        "transported_PL_jump_formula_closed": True,
        "genuine_transverse_simple_node_located": True,
        "selected_side_floating_limit_norm": one_sided[
            "selected_side_limit_norm"
        ],
        "unit_PL_jump_relative_residual": transported[
            "relative_residual_after_best_complex_scale"
        ],
        "smooth_ell_zero_found": False,
        "ell_zero_no_go_proved": False,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A123,
        PACKET,
        ANALYZER,
        ENGINE,
        NORMAL_FUNCTION,
        Path(__file__),
        THEOREM,
        DECISION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79PicardLefschetzOneSidedResidualRegularization.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79PicardLefschetzOneSidedResidualRegularization_v1.md"
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
            "local_transported_PL_jump_formula_exact": True,
            "simple_node_and_transversality_observed": True,
            "unit_PL_jump_numerically_verified": True,
            "interval_nonzero_invented": False,
            "global_ell_zero_no_go_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": "MTTSelectedQ79PicardLefschetzOneSidedResidualRegularization",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "transported_PL_jump_theorem_closed": True,
        "unit_PL_jump_numerically_verified": True,
        "selected_side_floating_limit_norm": one_sided[
            "selected_side_limit_norm"
        ],
        "selected_side_nonzero_interval_proved": False,
        "global_no_go_proved": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "PL jump: overlap="
        f"{transported['projective_overlap_with_numerical_jump']:.15f}, "
        "relative residual="
        f"{transported['relative_residual_after_best_complex_scale']:.3e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
