from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_alignment_E32_handle_combination_interval as legacy
import certify_q79_selected_alignment_E32_primitive_handle_basis_intervals as primitive
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
A209 = PERIOD_DIRECTORY / "selected_alignment_E32_primitive_handle_basis.intervals.packet.json"
A231 = PROBE / "validated_transport" / "n3.chain.frontier.json"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
OUTPUT = PROBE / "validated_transport" / "n3.rank3.handle_combination.interval.json"
HANDLE_A_CACHE = PROBE / "validated_transport" / "n3.handleA.cache.json"
HANDLE_B_CACHE = PROBE / "validated_transport" / "n3.handleB.cache.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3HandleCombinationInterval_A374_v1.md"
ARTIFACT = "A374"
EXPECTED_COORDINATES = [1, 1, 1, -1, 1, 0, 0, 1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def combine_basis(basis: list[list[acb]], coordinates: list[int]) -> list[acb]:
    if len(basis) != 4 or len(coordinates) != 4:
        raise AssertionError("rank-3 handle basis dimensions changed")
    return [
        sum((acb(coefficient) * basis[column][row] for column, coefficient in enumerate(coordinates)), acb(0))
        for row in range(5)
    ]


def oriented_n3_base_cycles(
    system: validated.SelectedQ79IntervalSystem,
    *,
    cut_segments: int,
    cut_tolerance: float,
) -> tuple[list[list[acb]], dict]:
    roots, leading = legacy.selected_base_roots(system)
    orientation = load(primitive.ORIENTATION)
    marked = np.asarray(
        [
            [legacy.complex_value(value) for value in row]
            for row in orientation["marked_base_period_matrix"]
        ],
        dtype=np.complex128,
    )
    inherited = load(A209)["rigorous_base_cut_basis"]["cut_certificates"]
    cut_specs = {
        "a2": ((0, 1), [0, 0, 1, 0]),
        "b2": ((1, 4), [0, 0, 0, 1]),
        "minus_a1_plus_a2": ((3, 4), [-1, 0, 1, 0]),
        "minus_a1_minus_b1": ((3, 5), [-1, -1, 0, 0]),
    }
    cuts: dict[str, list[acb]] = {}
    diagnostics = {}
    for name, (pair, coordinates) in cut_specs.items():
        print(f"certifying n3 base cut {name} pair={pair}", flush=True)
        raw, direct = legacy.direct_cut_periods(
            roots,
            leading,
            pair,
            segments=cut_segments,
            tolerance=cut_tolerance,
        )
        sign = int(inherited[name]["orientation_sign"])
        if sign not in {-1, 1}:
            raise AssertionError("A209 base-cut orientation sign changed")
        selected = [acb(sign) * value for value in raw]
        centers = np.asarray([legacy.midpoint(value) for value in selected])
        reference = marked @ np.asarray(coordinates, dtype=np.float64)
        inherited_error = float(np.max(abs(centers - reference)))
        opposite_error = float(np.max(abs(-centers - reference)))
        if inherited_error >= opposite_error:
            raise AssertionError("A209 orientation sign is not separated at n3")
        cuts[name] = selected
        diagnostics[name] = {
            "marked_coordinates": coordinates,
            "orientation_sign_inherited_from_A209": sign,
            "inherited_sign_reference_error": inherited_error,
            "opposite_sign_reference_error": opposite_error,
            "orientation_separation_margin": opposite_error - inherited_error,
            **direct,
        }

    a2 = cuts["a2"]
    b2 = cuts["b2"]
    a1 = [left - right for left, right in zip(a2, cuts["minus_a1_plus_a2"])]
    b1 = [-left - right for left, right in zip(a1, cuts["minus_a1_minus_b1"])]
    basis = [a1, b1, a2, b2]
    return basis, {
        "basis_order": ["a1", "b1", "a2", "b2"],
        "orientation_source": "A209 fixed base-cut signs",
        "basis_identity": {
            "a2": "cut(0,1)",
            "b2": "cut(1,4)",
            "a1": "cut(0,1)-cut(3,4)",
            "b1": "-a1-cut(3,5)",
        },
        "cut_certificates": diagnostics,
    }


def complex_vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([legacy.complex_value(value) for value in values], dtype=np.complex128)


def interval_row(center: complex, radius: float, floating: complex) -> dict:
    ball = acb(
        arb(format(center.real, ".17g"), format(radius, ".17g")),
        arb(format(center.imag, ".17g"), format(radius, ".17g")),
    )
    real_difference = abs(floating.real - center.real)
    imaginary_difference = abs(floating.imag - center.imag)
    contained = real_difference <= radius and imaginary_difference <= radius
    if not contained:
        raise AssertionError("n3 floating handle diagnostic left the certified box")
    return {
        "interval": legacy.complex_interval(ball),
        "interval_center": legacy.complex_pair(center),
        "uniform_component_radius_upper": radius,
        "floating_value_diagnostic_only": legacy.complex_pair(floating),
        "floating_real_center_difference": real_difference,
        "floating_imaginary_center_difference": imaginary_difference,
        "floating_value_contained": bool(contained),
        "minimum_component_containment_margin": radius
        - max(real_difference, imaginary_difference),
    }


def cached_handle_transport(
    cache_path: Path,
    system: validated.SelectedQ79IntervalSystem,
    initial: list[acb],
    *,
    endpoint: complex,
    label: str,
    dps: int,
    order: int,
    initial_step: float,
    minimum_step: float,
) -> tuple[list[acb], arb, dict]:
    configuration = {
        "label": label,
        "endpoint": legacy.complex_pair(endpoint),
        "dps": dps,
        "order": order,
        "initial_step": format(initial_step, ".17g"),
        "minimum_step": format(minimum_step, ".17g"),
        "initial_values": [validated.encoded_acb(value) for value in initial],
        "n3_fibration_sha256": sha256(n3_engine.FIBRATION),
        "primitive_handle_engine_sha256": sha256(Path(primitive.__file__).resolve()),
        "validated_taylor_engine_sha256": sha256(Path(validated.__file__).resolve()),
    }
    if cache_path.exists():
        packet = load(cache_path)
        if packet.get("schema") != "MTTQ79Rank3HandleTransportCache.v1":
            raise ValueError(f"stale rank-3 handle cache schema: {cache_path.name}")
        if packet.get("configuration") != configuration:
            raise ValueError(f"stale rank-3 handle cache configuration: {cache_path.name}")
        print(f"resumed completed {label} from {relative(cache_path)}", flush=True)
        return (
            [validated.decoded_acb(value) for value in packet["center"]],
            arb(packet["common_radius_ball"]),
            packet["diagnostics"],
        )
    center, radius_ball, diagnostics = primitive.validated_handle_transport(
        system,
        initial,
        endpoint=endpoint,
        label=label,
        order=order,
        initial_step=initial_step,
        minimum_step=minimum_step,
    )
    dump(
        cache_path,
        {
            "schema": "MTTQ79Rank3HandleTransportCache.v1",
            "status": "COMPLETED_VALIDATED_HANDLE_TRANSPORT_CACHED",
            "configuration": configuration,
            "center": [validated.encoded_acb(value) for value in center],
            "common_radius_ball": str(radius_ball),
            "diagnostics": diagnostics,
        },
    )
    print(f"wrote {relative(cache_path)}", flush=True)
    return center, radius_ball, diagnostics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-8)
    parser.add_argument("--cut-segments", type=int, default=12)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-28)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    a208 = load(A208)
    candidates = [
        row
        for row in a208["height_four_candidates"]
        if int(row["A132_objective_rank"]) == 3
    ]
    if len(candidates) != 1:
        raise AssertionError("A208 no longer selects exactly one rank-3 row")
    candidate = candidates[0]
    coordinates = [int(value) for value in candidate["primitive_handle_coordinates"]]
    if coordinates != EXPECTED_COORDINATES:
        raise AssertionError("selected rank-3 primitive-handle coordinates changed")

    system = n3_engine.exact_target_system(arguments.dps)
    basis, basis_diagnostics = oriented_n3_base_cycles(
        system,
        cut_segments=arguments.cut_segments,
        cut_tolerance=arguments.cut_tolerance,
    )
    a_initial = combine_basis(basis, coordinates[:4])
    b_initial = combine_basis(basis, coordinates[4:])

    a_center, a_radius_ball, a_diagnostics = cached_handle_transport(
        HANDLE_A_CACHE,
        system,
        a_initial,
        endpoint=-1j,
        label="n3 rank-3 A-handle combination",
        dps=arguments.dps,
        order=arguments.order,
        initial_step=arguments.initial_step,
        minimum_step=arguments.minimum_step,
    )
    b_center, b_radius_ball, b_diagnostics = cached_handle_transport(
        HANDLE_B_CACHE,
        system,
        b_initial,
        endpoint=1 + 0j,
        label="n3 rank-3 B-handle combination",
        dps=arguments.dps,
        order=arguments.order,
        initial_step=arguments.initial_step,
        minimum_step=arguments.minimum_step,
    )

    n3 = load(N3)
    floating_matrix = np.asarray(
        [
            [legacy.complex_value(value) for value in row]
            for row in n3["moving_handles"]["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    if floating_matrix.shape != (8, 8):
        raise AssertionError("n3 floating primitive-handle matrix changed")
    floating = floating_matrix @ np.asarray(coordinates, dtype=np.int64)

    a_common_radius = validated.upper(a_radius_ball)
    b_common_radius = validated.upper(b_radius_ball)
    rows = []
    for residue_index in range(8):
        a_value = a_center[5 + residue_index]
        b_value = b_center[5 + residue_index]
        value = a_value + b_value
        center = legacy.midpoint(value)
        arithmetic_radius = validated.radius_upper(value)
        serialization_radius = 8.0 * np.finfo(np.float64).eps * max(1.0, abs(center))
        radius = float(
            a_common_radius + b_common_radius + arithmetic_radius + serialization_radius
        )
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                **interval_row(center, radius, floating[residue_index]),
            }
        )

    maximum_radius = max(row["uniform_component_radius_upper"] for row in rows)
    minimum_margin = min(row["minimum_component_containment_margin"] for row in rows)
    payload = {
        "schema": "MTTQ79HeightFourRank3HandleCombinationInterval.v1",
        "status": "N3_RANK3_ALL_EIGHT_HANDLE_COMBINATION_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_rank3_chain": {
            "candidate_id": candidate["candidate_id"],
            "A132_objective_rank": 3,
            "primitive_column_order": primitive.HANDLE_ORDER,
            "primitive_handle_coordinates": coordinates,
            "A_path_coordinates": coordinates[:4],
            "B_path_coordinates": coordinates[4:],
            "identity": (
                "H_n3 = transport_A(a1+b1+a2-b2) "
                "+ transport_B(a1+b2)"
            ),
        },
        "rigorous_base_cut_basis": basis_diagnostics,
        "validated_A_path": a_diagnostics,
        "validated_B_path": b_diagnostics,
        "all_eight_handle_rows": rows,
        "summary": {
            "certified_rows": len(rows),
            "maximum_component_radius_upper": maximum_radius,
            "product_box_l2_radius_upper": math.sqrt(
                sum(row["uniform_component_radius_upper"] ** 2 for row in rows)
            ),
            "minimum_floating_containment_margin": minimum_margin,
            "all_floating_diagnostics_contained": all(
                row["floating_value_contained"] for row in rows
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A208_selected_rank3_chain": A208,
                "A209_fixed_base_cut_orientations": A209,
                "A231_chain_decomposition": A231,
                "n3_ultra_probe": N3,
                "n3_exact_fibration": n3_engine.FIBRATION,
                "A131_orientation": primitive.ORIENTATION,
                "n3_interval_system": Path(n3_engine.__file__).resolve(),
                "primitive_handle_interval_engine": Path(primitive.__file__).resolve(),
                "validated_taylor_engine": Path(validated.__file__).resolve(),
                "validated_A_path_cache": HANDLE_A_CACHE,
                "validated_B_path_cache": HANDLE_B_CACHE,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "exact_n3_interval_system_used": True,
            "rank3_handle_coordinates_selected_before_interval_execution": True,
            "rigorous_base_cut_basis_closed": True,
            "homogeneous_A_and_B_Gauss_Manin_transports_closed": True,
            "rank3_handle_combination_interval_closed": True,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "certify the selected anchored beta branch in the same exact n3 "
            "interval system, then combine it with the 76-target chain"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Handle Combination Interval (A374) v1\n\n"
        "A374 certifies the selected rank-3 primitive-handle contribution in all "
        "eight residue rows on the exact n3 interval system. The fixed coordinates "
        "`[1,1,1,-1,1,0,0,1]` are evaluated as two homogeneous Gauss-Manin "
        "transports: `A:(a1+b1+a2-b2)` and `B:(a1+b2)`.\n\n"
        f"The maximum component radius is `{maximum_radius:.12g}` and every "
        "independent n3 floating diagnostic lies inside its rigorous interval; "
        f"the minimum component margin is `{minimum_margin:.12g}`. Floating "
        "values are diagnostics only, not error bounds.\n\n"
        "This closes the selected moving handle block. The anchored beta branch, "
        "interval Jacobian, and covariant zero remain separate proof obligations.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
