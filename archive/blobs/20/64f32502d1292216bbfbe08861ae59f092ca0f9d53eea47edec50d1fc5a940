from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "hessian"
    / "precision.manifest.json"
)

INTERSECTION = [
    [0, 1, 0, 0, 0],
    [-1, 0, 1, 0, 0],
    [0, -1, 0, 1, 0],
    [0, 0, -1, 0, 1],
    [0, 0, 0, -1, 0],
]
RADICAL = [1, 0, 1, 0, 1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def authority_path(row: dict, label: str) -> Path:
    path = ROOT / row.get("path", "")
    require(path.is_file(), f"{label} authority is absent")
    require(sha256(path) == row.get("sha256"), f"{label} authority is stale")
    return path


def audit_authorities(packet: dict, label: str) -> None:
    authority = packet.get("authority", {})
    require(bool(authority), f"{label} authority is empty")
    for name, row in authority.items():
        authority_path(row, f"{label}:{name}")


def audit_coordinate_isolation(packet: dict, label: str) -> list[int]:
    solve = packet["integer_coordinate_isolation"]
    require(solve["verified_interval_solve"] is True, f"{label} solve is unverified")
    require(
        solve["all_coordinates_isolate_exactly_one_integer"] is True,
        f"{label} does not isolate every integer coordinate",
    )
    coordinates = [int(value) for value in solve["unique_integer_coordinates"]]
    intervals = solve["coordinate_intervals"]
    require(len(coordinates) == len(intervals) == 5, f"{label} coordinate rank changed")
    require(
        [int(row["coordinate"]) for row in intervals] == [1, 2, 3, 4, 5],
        f"{label} coordinate order changed",
    )
    for coordinate, row in zip(coordinates, intervals, strict=True):
        lower = Decimal(row["lower"])
        upper = Decimal(row["upper"])
        integer = int(row["integer"])
        require(integer == coordinate, f"{label} integer payload is inconsistent")
        require(lower <= integer <= upper, f"{label} integer leaves its interval")
        require(
            math.ceil(lower) == integer == math.floor(upper),
            f"{label} interval contains more than one integer",
        )
    rows = [int(value) for value in solve["selected_square_rows_zero_based"]]
    require(len(rows) == len(set(rows)) == 5, f"{label} solve rows are not a basis")
    require(all(0 <= row < 10 for row in rows), f"{label} solve row is out of range")
    return coordinates


def audit_reanchor(path: Path, index: int, seen: set[Path]) -> tuple[float, int]:
    resolved = path.resolve()
    require(resolved not in seen, f"d{index:03d} reanchor chain contains a cycle")
    seen.add(resolved)
    packet = load(path)
    label = f"d{index:03d}:{path.name}"
    require(int(packet["distinguished_index"]) == index, f"{label} index changed")
    require(
        packet["schema"]
        in {
            "MTTQ79HeightFourAffineChainBasisReanchor.v1",
            "MTTQ79HeightFourInteriorAffineChainBasisReanchor.v1",
        },
        f"{label} schema changed",
    )
    theorem = packet["affine_homology_theorem"]
    require(theorem["rank_H1_affine"] == 5, f"{label} lost affine rank five")
    require(theorem["intersection_rank"] == 4, f"{label} compact rank changed")
    require(theorem["intersection_matrix"] == INTERSECTION, f"{label} A5 form changed")
    require(
        theorem["puncture_radical_generator"] == RADICAL,
        f"{label} puncture radical changed",
    )
    require(
        theorem.get("adjacent_lifted_branch_arcs_form_integral_A5_basis", False)
        is True
        or theorem.get("five_direct_cycles_are_an_integral_affine_basis", False)
        is True,
        f"{label} affine-basis theorem is open",
    )
    audit_coordinate_isolation(packet, label)

    reanchor = packet["reanchor"]
    overlaps = reanchor["overlap_by_period_coordinate"]
    require(overlaps == [True] * 5, f"{label} direct periods do not all overlap")
    require(
        len(reanchor["selected_direct_period_balls"]) == 5,
        f"{label} direct period count changed",
    )
    direct = float(reanchor["direct_lift_maximum_component_radius_upper"])
    transported = float(reanchor["transported_lift_physical_radius_upper"])
    reduction = float(reanchor["radius_reduction_factor"])
    require(
        math.isfinite(direct) and 0.0 < direct < transported,
        f"{label} does not strictly reduce the lift radius",
    )
    require(
        math.isclose(reduction, transported / direct, rel_tol=3.0e-15),
        f"{label} radius-reduction factor does not replay",
    )
    require(
        len(reanchor["transport_direct_difference_uppers"]) == 5,
        f"{label} overlap bound count changed",
    )
    require(
        all(
            math.isfinite(float(value)) and float(value) >= 0.0
            for value in reanchor["transport_direct_difference_uppers"]
        ),
        f"{label} has an invalid overlap bound",
    )

    scope = packet["strict_scope"]
    for key in (
        "all_five_affine_period_coordinates_recomputed",
        "integer_coordinates_selected_by_verified_interval_solve",
        "puncture_at_infinity_coordinate_retained",
        "selected_cycle_integrality_consumed",
    ):
        require(scope[key] is True, f"{label} strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, f"{label} used observed values")
    require(scope["full_SM_closure_proved"] is False, f"{label} overclaims closure")
    audit_authorities(packet, label)
    replay_path = authority_path(
        packet["authority"]["selected_main_replay_interval"],
        f"{label}:selected-main",
    )
    replay = load(replay_path)
    require(
        packet["selected_root_id"] == replay["selected_target"]["root_id"],
        f"{label} root changed against its selected target",
    )

    prior = packet["authority"].get("prior_affine_chain_basis_reanchor")
    if prior is None:
        require(packet["artifact"] == "A380AB", f"{label} base artifact changed")
        require(
            packet["status"]
            == "SELECTED_AFFINE_H1_INTEGER_COORDINATES_AND_REANCHOR_CERTIFIED",
            f"{label} base status changed",
        )
        require(scope["smooth_base_affine_reanchor_closed"] is True, f"{label} base is open")
        return 0.0, 1

    require(
        packet["artifact"] in {"A380ABI", "A380ABIA"},
        f"{label} interior artifact changed",
    )
    require(
        packet["status"] == "REGULAR_FIBER_AFFINE_H1_INTEGER_COORDINATES_REANCHORED",
        f"{label} interior status changed",
    )
    require(scope["regular_fiber_affine_reanchor_closed"] is True, f"{label} is open")
    require(scope["selected_cycle_or_source_changed"] is False, f"{label} changed its source")
    if packet["artifact"] == "A380ABIA":
        require(scope["adaptive_cut_subdivision_only"] is True, f"{label} changed its source")
        adaptive = packet["adaptive_cut_subdivision"]
        multipliers = [int(value) for value in adaptive["selected_multipliers_by_adjacent_arc"]]
        require(len(multipliers) == 5, f"{label} adaptive arc count changed")
        require(set(multipliers) <= {1, 2, 4, 8, 16}, f"{label} used a noncanonical multiplier")
        require(max(multipliers) == int(adaptive["maximum_selected_multiplier"]), f"{label} multiplier summary changed")
        require(int(adaptive["maximum_allowed_multiplier"]) == 16, f"{label} adaptive ceiling changed")
        require(
            adaptive["same_interval_half_plane_and_sign_tests_used"] is True
            and adaptive["same_quadrature_tolerance_used"] is True,
            f"{label} weakened the direct-arc test",
        )
    position = float(packet["path_position"])
    require(
        math.isfinite(position) and position > 0.0,
        f"{label} has an invalid continuation position",
    )
    prior_path = authority_path(prior, f"{label}:prior")
    prior_position, depth = audit_reanchor(prior_path, index, seen)
    require(prior_position < position, f"{label} reanchor positions are not ordered")
    return position, depth + 1


def main() -> int:
    manifest = load(MANIFEST)
    require(
        manifest["schema"] == "MTTQ79HeightFourPrecisionHessianQueueManifest.v1",
        "precision manifest schema changed",
    )
    require(len(manifest["targets"]) == 76, "precision target inventory changed")
    audited = 0
    maximum_depth = 0
    for row in manifest["targets"]:
        if not row.get("full_budget_pass", False):
            continue
        main_path = ROOT / row["main_path"]
        main_packet = load(main_path)
        source = main_packet.get("authority", {}).get("affine_chain_basis_reanchor")
        if source is None:
            continue
        index = int(row["distinguished_index"])
        require(main_packet["artifact"] == "A380ABR", f"d{index:03d} affine route changed")
        audit_authorities(main_packet, f"d{index:03d}:main")
        _, depth = audit_reanchor(
            authority_path(source, f"d{index:03d}:main-source"), index, set()
        )
        audited += 1
        maximum_depth = max(maximum_depth, depth)
    require(audited > 0, "no completed affine-chain target is available")
    print(
        "PASS: replayed the selected affine H1 integer solve and chained direct "
        f"reanchors for {audited} completed target Hessians; maximum chain depth={maximum_depth}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
