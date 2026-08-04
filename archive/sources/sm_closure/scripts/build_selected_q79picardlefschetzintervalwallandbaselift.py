from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79picardlefschetzintervalwallandbaselift"
OUT = ROOT / "candidate_data" / SLUG
A124 = (
    ROOT
    / "candidate_data"
    / "selected_q79picardlefschetzonesidedresidualregularization.candidate.json"
)
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
WALL = DIRECTORY / "pgl3_transverse_simple_node.interval.packet.json"
BASE = DIRECTORY / "pgl3_selected_side_base_lift.interval.packet.json"
CONTOUR = DIRECTORY / "pgl3_selected_side_contour_regularization.packet.json"
WALL_SCRIPT = ROOT / "scripts" / "certify_q79_picard_lefschetz_wall_interval.py"
BASE_SCRIPT = ROOT / "scripts" / "certify_q79_selected_side_base_lift_interval.py"
CONTOUR_SCRIPT = ROOT / "scripts" / "analyze_q79_selected_side_contour_regularization.py"
THEOREM = OUT / "interval_wall_and_nonzero_PL_jump_theorem.packet.json"
DECISION = OUT / "selected_side_beta_transport.open.json"
FRONTIER = OUT / "U6_frontier_after_A125.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


STATUS = (
    "MTT_U6_Q79_PL_WALL_AND_BASE_LIFT_INTERVAL_CLOSED_"
    "SELECTED_BETA_TRANSPORT_OPEN"
)
NEXT = "MTT_Selected_q79ValidatedTaylorModelBetaTransport_or_IntegralBranch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    a124 = load(A124)
    wall = load(WALL)
    base = load(BASE)
    contour = load(CONTOUR)
    geometry = wall["geometric_bounds"]

    if not a124["checks"]["local_transported_PL_jump_formula_exact"]:
        raise AssertionError("A124 local PL theorem is unavailable")
    if not wall["unique_zero_in_box"]:
        raise AssertionError("Krawczyk wall uniqueness is unavailable")
    if min(float(value) for value in wall["krawczyk_inclusion_margins"]) <= 0:
        raise AssertionError("Krawczyk image is not strictly interior")
    if float(geometry["absolute_f_tt_lower"]) <= 1.0:
        raise AssertionError("simple-node lower bound failed")
    if float(geometry["absolute_f_u_lower"]) <= 1.0:
        raise AssertionError("base transversality denominator failed")
    if float(geometry["absolute_q_at_node_lower"]) <= 0.1:
        raise AssertionError("q divisor disjointness failed")
    if not geometry["transverse_real_carrier_crossing"]:
        raise AssertionError("transverse crossing failed")
    if float(geometry["normalized_y_chart_scale_lower"]) <= 0.5:
        raise AssertionError("projective chart regularity failed")
    if float(geometry["local_vanishing_state_V0_absolute_lower"]) <= 0:
        raise AssertionError("local vanishing state contains zero")
    if not all(wall["closed"].values()):
        raise AssertionError("one or more interval wall gates remain open")

    if not all(base["closed"].values()):
        raise AssertionError("one or more interval base-lift gates remain open")
    if float(base["maximum_component_ball_radius_upper"]) >= 1.0e-35:
        raise AssertionError("base-lift enclosure is too broad")
    if float(base["path"]["minimum_square_root_half_plane_margin"]) <= 1.0e-4:
        raise AssertionError("square-root continuation margin failed")
    if float(base["path"]["minimum_branch_sign_separation_margin"]) <= 1.0:
        raise AssertionError("branch sign separation failed")
    if float(base["path"]["opposite_outer_sheet_cancellation_upper"]) >= 1.0e-40:
        raise AssertionError("opposite infinity-sheet cancellation failed")
    if base["path"]["rigorous_integral_count"] < 1000:
        raise AssertionError("base-lift integral execution is incomplete")

    comparison = contour["comparison"]
    if comparison["maximum_absolute_component_difference"] >= 5.0e-7:
        raise AssertionError("lower-contour same-branch comparison failed")
    if comparison["projective_overlap"] <= 0.999999999999:
        raise AssertionError("lower-contour beta direction mismatch")
    if comparison["equilibrated_condition_number_reduction_factor"] <= 10.0:
        raise AssertionError("lower contour does not improve conditioning")
    if contour["strict_scope"]["endpoint_beta_interval_certified"]:
        raise AssertionError("floating contour was overpromoted")

    theorem = {
        "schema": "MTTQ79IntervalWallAndNonzeroPLJumpTheorem.v1",
        "status": "INTERVAL_WALL_AND_NONZERO_PL_JUMP_CLOSED",
        "wall": {
            "unique_zero_box": wall["initial_box"],
            "Krawczyk_image": wall["krawczyk_image"],
            "Krawczyk_inclusion_margins": wall["krawczyk_inclusion_margins"],
            "geometric_bounds": geometry,
        },
        "theorem": {
            "name": "Q79IntervalTransverseNodeAndNonzeroPLJumpTheorem",
            "proved": True,
            "statement": (
                "The frozen A124 carrier path has a unique transverse simple "
                "node in the certified Krawczyk box. The selected q divisor is "
                "disjoint and the y chart is regular there. The local vanishing "
                "state is nonzero; an invertible homogeneous Gauss-Manin "
                "fundamental matrix therefore transports it to a nonzero "
                "Picard-Lefschetz jump. Hence both one-sided beta limits cannot "
                "simultaneously vanish."
            ),
        },
        "scope": {
            "wall_and_local_nonzero_interval_certified": True,
            "endpoint_jump_coordinates_interval_certified": False,
            "selected_side_beta_interval_certified": False,
            "global_ell_zero_no_go": False,
        },
    }
    dump(THEOREM, theorem)

    decision = {
        "schema": "MTTQ79SelectedSideBetaTransportDecisionAfterA125.v1",
        "status": "CERTIFIED_INITIAL_BALL_AVAILABLE_VALIDATED_ENDPOINT_TRANSPORT_OPEN",
        "selected_side_base_lift": base,
        "floating_lower_contour": contour,
        "closed": {
            "selected_side_base_lift_interval": True,
            "same_branch_lower_contour_floating": True,
            "condition_number_reduced_more_than_tenfold": True,
        },
        "open": {
            "lower_contour_homotopy_interval_certificate": True,
            "high_order_validated_Gauss_Manin_transport": True,
            "selected_side_beta_nonzero_interval": True,
            "global_ell_zero_no_go": True,
            "exact_integral_branch_selection": True,
        },
        "rejected_method": (
            "first-order interval exponential propagation is too pessimistic "
            "near the discriminant; use a validated high-order Taylor model"
        ),
        "next_required_artifact": NEXT,
    }
    dump(DECISION, decision)

    frontier = {
        "schema": "MTTU6FrontierAfterA125.v1",
        "status": STATUS,
        "A124_exact_local_PL_formula_preserved": True,
        "unique_transverse_simple_node_interval_certified": True,
        "local_vanishing_state_and_PL_jump_nonzero": True,
        "both_one_sided_limits_cannot_vanish": True,
        "selected_side_base_lift_interval_certified": True,
        "selected_side_base_lift_maximum_radius": base[
            "maximum_component_ball_radius_upper"
        ],
        "lower_contour_condition_reduction_factor": comparison[
            "equilibrated_condition_number_reduction_factor"
        ],
        "selected_side_beta_nonzero_interval": False,
        "global_ell_zero_no_go": False,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A124,
        WALL,
        BASE,
        CONTOUR,
        WALL_SCRIPT,
        BASE_SCRIPT,
        CONTOUR_SCRIPT,
        Path(__file__),
        THEOREM,
        DECISION,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79PicardLefschetzIntervalWallAndBaseLift.v1",
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79PicardLefschetzIntervalWallAndBaseLift_v1.md"
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
            "unique_transverse_wall_interval_certified": True,
            "nonzero_PL_jump_theorem_closed": True,
            "selected_side_base_lift_interval_certified": True,
            "selected_side_endpoint_beta_interval_invented": False,
            "global_ell_zero_no_go_invented": False,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "certificate": "MTTSelectedQ79PicardLefschetzIntervalWallAndBaseLift",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "unique_transverse_wall_interval_certified": True,
        "nonzero_PL_jump_theorem_closed": True,
        "selected_side_base_lift_interval_certified": True,
        "selected_side_beta_nonzero_interval": False,
        "global_no_go_proved": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "wall and base lift interval-certified; endpoint beta transport remains open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
