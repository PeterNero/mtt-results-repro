from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79picardlefschetzintervalwallandbaselift"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
OUT = ROOT / "candidate_data" / SLUG
THEOREM = OUT / "interval_wall_and_nonzero_PL_jump_theorem.packet.json"
DECISION = OUT / "selected_side_beta_transport.open.json"
FRONTIER = OUT / "U6_frontier_after_A125.packet.json"
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
WALL = DIRECTORY / "pgl3_transverse_simple_node.interval.packet.json"
BASE = DIRECTORY / "pgl3_selected_side_base_lift.interval.packet.json"
CONTOUR = DIRECTORY / "pgl3_selected_side_contour_regularization.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def strictly_inside(inner: dict, outer: dict) -> bool:
    return (
        float(outer["lower"]) < float(inner["lower"])
        and float(inner["upper"]) < float(outer["upper"])
    )


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    theorem = load(THEOREM)
    decision = load(DECISION)
    frontier = load(FRONTIER)
    wall = load(WALL)
    base = load(BASE)
    contour = load(CONTOUR)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    require(wall["unique_zero_in_box"], "wall uniqueness")
    require(
        all(
            strictly_inside(inner, outer)
            for inner, outer in zip(wall["krawczyk_image"], wall["initial_box"])
        ),
        "strict Krawczyk inclusion",
    )
    require(
        min(float(value) for value in wall["krawczyk_inclusion_margins"]) > 0,
        "Krawczyk margins",
    )
    geometry = wall["geometric_bounds"]
    require(float(geometry["absolute_f_tt_lower"]) > 5.0e5, "simple node")
    require(float(geometry["absolute_f_u_lower"]) > 3.0e4, "base denominator")
    require(float(geometry["absolute_q_at_node_lower"]) > 0.2, "q disjointness")
    require(
        float(geometry["du_star_ds"]["imaginary"]["upper"]) < 0,
        "transversality sign",
    )
    require(
        float(geometry["normalized_y_chart_scale_lower"]) > 0.8,
        "chart regularity",
    )
    require(
        float(geometry["local_vanishing_state_V0_absolute_lower"]) > 0.01,
        "vanishing state nonzero",
    )
    require(all(wall["closed"].values()), "wall closure gates")

    require(all(base["closed"].values()), "base-lift closure gates")
    require(
        float(base["maximum_component_ball_radius_upper"]) < 1.0e-40,
        "base-lift radius",
    )
    path = base["path"]
    require(path["rigorous_integral_count"] == 2995, "integral count")
    require(path["certified_segment_count"] == 599, "segment count")
    require(
        float(path["minimum_square_root_half_plane_margin"]) > 1.0e-3,
        "square-root margin",
    )
    require(
        float(path["minimum_branch_sign_separation_margin"]) > 1.0,
        "branch-sign margin",
    )
    require(
        float(path["opposite_outer_sheet_cancellation_upper"]) < 1.0e-50,
        "outer-sheet cancellation",
    )

    comparison = contour["comparison"]
    require(
        comparison["maximum_absolute_component_difference"] < 5.0e-7,
        "contour agreement",
    )
    require(comparison["projective_overlap"] > 0.999999999999, "contour overlap")
    require(
        comparison["equilibrated_condition_number_reduction_factor"] > 10,
        "condition reduction",
    )
    require(
        not contour["strict_scope"]["endpoint_beta_interval_certified"],
        "floating contour overpromoted",
    )

    require(theorem["theorem"]["proved"], "A125 theorem")
    require(
        theorem["scope"]["wall_and_local_nonzero_interval_certified"],
        "theorem interval scope",
    )
    require(
        not theorem["scope"]["selected_side_beta_interval_certified"],
        "endpoint beta invented",
    )
    require(frontier["unique_transverse_simple_node_interval_certified"], "frontier wall")
    require(frontier["local_vanishing_state_and_PL_jump_nonzero"], "frontier jump")
    require(frontier["selected_side_base_lift_interval_certified"], "frontier lift")
    require(not frontier["selected_side_beta_nonzero_interval"], "frontier beta")
    require(not frontier["global_ell_zero_no_go"], "frontier no-go")
    require(
        decision["open"]["high_order_validated_Gauss_Manin_transport"],
        "next transport gate",
    )
    require(not certificate["selected_side_beta_nonzero_interval"], "certificate beta")
    require(not certificate["global_no_go_proved"], "certificate no-go")
    require(not candidate["checks"]["observed_SM_target_fitting_used"], "target fitting")

    print("q79 A125 interval wall and base-lift audit: PASS")
    print("closed: unique transverse node, nonzero PL jump, selected-side base lift")
    print(
        "Krawczyk minimum margin="
        f"{min(float(value) for value in wall['krawczyk_inclusion_margins']):.3e}, "
        "base-lift maximum radius="
        f"{float(base['maximum_component_ball_radius_upper']):.3e}"
    )
    print("open: validated high-order endpoint beta transport")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
