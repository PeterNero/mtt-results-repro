from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79picardlefschetzonesidedresidualregularization"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
OUT = ROOT / "candidate_data" / SLUG
THEOREM = OUT / "transported_picard_lefschetz_jump_theorem.packet.json"
DECISION = OUT / "one_sided_ell_zero_residual.open.json"
FRONTIER = OUT / "U6_frontier_after_A124.packet.json"
DIAGNOSTIC = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_transverse_simple_node_and_transport_pl_jump.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    theorem = load(THEOREM)
    decision = load(DECISION)
    frontier = load(FRONTIER)
    diagnostic = load(DIAGNOSTIC)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    wall = diagnostic["wall"]
    require(wall["maximum_F_and_Ft_residual"] < 1.0e-9, "wall residual")
    require(wall["simple_node"], "simple node")
    require(wall["absolute_f_tt"] > 1.0, "nonzero second derivative")
    require(wall["transverse_real_path_crossing"], "transverse crossing")
    require(abs(wall["imaginary_du_star_ds"]) > 1.0e-5, "crossing derivative")
    require(wall["q_divisor_disjoint_from_node"], "q divisor disjointness")
    require(min(wall["q_root_distances_from_node"]) > 1.0e-3, "q distance")
    require(wall["normalized_y_chart_scale"] > 0.5, "regular line chart")
    require(
        min(wall["real_coupled_Jacobian_singular_values"]) > 1.0,
        "coupled Jacobian rank",
    )

    one_sided = diagnostic["one_sided_beta"]
    require(one_sided["selected_side_limit_norm"] > 2.0, "selected-side limit")
    require(one_sided["crossed_side_limit_norm"] > 2.0, "crossed-side limit")
    require(one_sided["extrapolated_jump_norm"] > 1.0, "one-sided jump")
    for side in ["selected_minus", "crossed_plus"]:
        require(
            one_sided["limits"][side][
                "linear_quadratic_vector_difference_norm"
            ]
            < 5.0e-5,
            f"{side} extrapolation",
        )

    transported = diagnostic["transported_Picard_Lefschetz_jump"]
    require(
        transported["projective_overlap_with_numerical_jump"] > 0.999999999,
        "transported jump overlap",
    )
    require(
        transported["relative_residual_after_best_complex_scale"] < 1.0e-5,
        "transported jump residual",
    )
    scale = transported["best_complex_scale_to_numerical_jump"]
    require(abs(float(scale["real"]) - 1.0) < 5.0e-4, "unit jump magnitude")
    require(abs(float(scale["imaginary"])) < 5.0e-4, "unit jump orientation")

    require(theorem["theorem"]["proved"], "local theorem")
    require(theorem["instantiation_scope"]["formula_exact"], "exact formula scope")
    require(
        not theorem["instantiation_scope"]["interval_nonzero_conclusion"],
        "interval theorem invented",
    )
    require(frontier["transported_PL_jump_formula_closed"], "frontier theorem")
    require(frontier["genuine_transverse_simple_node_located"], "frontier wall")
    require(not frontier["ell_zero_no_go_proved"], "frontier no-go invented")
    require(not frontier["smooth_ell_zero_found"], "frontier zero invented")
    require(
        not decision["open"]["selected_side_nonzero_interval_proved"],
        "decision interval claim",
    )
    require(not decision["open"]["global_ell_zero_no_go_proved"], "decision no-go")
    require(not certificate["selected_side_nonzero_interval_proved"], "certificate interval")
    require(not certificate["global_no_go_proved"], "certificate no-go")
    require(not candidate["checks"]["observed_SM_target_fitting_used"], "target fitting")

    print("q79 A124 transported Picard-Lefschetz jump audit: PASS")
    print("closed: exact local jump formula and floating unit-jump execution")
    print(
        "wall: residual="
        f"{wall['maximum_F_and_Ft_residual']:.3e}, "
        "minimum coupled singular value="
        f"{min(wall['real_coupled_Jacobian_singular_values']):.6f}"
    )
    print(
        "jump: overlap="
        f"{transported['projective_overlap_with_numerical_jump']:.15f}, "
        "relative residual="
        f"{transported['relative_residual_after_best_complex_scale']:.3e}"
    )
    print("open: interval-certified selected-side nonzero residual")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
