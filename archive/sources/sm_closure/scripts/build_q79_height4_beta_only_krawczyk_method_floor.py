from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import build_q79_height4_krawczyk_feasibility_seed as seed


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
A393 = VALIDATED / "n3.chain.relation_l1.a393.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
OUTPUT = VALIDATED / "n3.beta_floor.a396.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourBetaOnlyKrawczykMethodFloor_A396_v1.md"
ARTIFACT = "A396"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def authorities_current(packet: dict) -> bool:
    for row in packet.get("authority", {}).values():
        path = ROOT / row["path"]
        if not path.exists() or sha256(path) != row["sha256"]:
            return False
    return True


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def indexed_rows(packet: dict, key: str) -> dict[int, dict]:
    rows = {int(row["residue_index_zero_based"]): row for row in packet[key]}
    if set(rows) != set(range(8)):
        raise AssertionError(f"{key} does not contain residues 0 through 7")
    return rows


def summary(values: np.ndarray) -> dict[str, float]:
    return {
        "maximum_component_radius_upper": float(np.max(values)),
        "product_box_l2_radius_upper": float(np.linalg.norm(values)),
    }


def main() -> int:
    prefix = load(PREFIX)
    a231 = load(A231)
    handle = load(A383)
    jacobian = load(A384)
    chart = load(A385S)
    relation = load(A393)
    wall = load(D065)
    if (
        prefix.get("artifact") != "A373"
        or int(prefix["certified_A219_priority_prefix_length"]) != 76
        or not prefix["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A396 requires the final 76-target prefix")
    if (
        handle.get("artifact") != "A383"
        or not authorities_current(handle)
        or jacobian.get("artifact") != "A384"
        or not authorities_current(jacobian)
        or chart.get("artifact") != "A385S"
        or not authorities_current(chart)
    ):
        raise AssertionError("A396 requires current A383/A384/A385S packets")
    if (
        relation.get("artifact") != "A393"
        or not relation["strict_scope"][
            "unweighted_L1_relation_compression_closed_by_optimality"
        ]
        or not authorities_current(relation)
    ):
        raise AssertionError("A396 requires the current A393 optimality theorem")
    decomposition = a231["exact_floating_decomposition"]
    if (
        int(decomposition["PL_crossing_period_distinguished_index"]) != 65
        or int(decomposition["PL_wall_weight"]) != 3
    ):
        raise AssertionError("the selected Picard-Lefschetz correction changed")

    handle_rows = indexed_rows(handle, "handle_rows")
    chain_radii = np.asarray(
        [
            float(row["certified_prefix_interval_radius_upper"])
            for row in prefix["residue_rows"]
        ],
        dtype=np.float64,
    )
    handle_radii = np.asarray(
        [float(handle_rows[index]["component_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    wall_radii = np.asarray(
        [
            3.0 * float(wall["residue_rows"][index]["full_interval_radius_upper"])
            for index in range(8)
        ],
        dtype=np.float64,
    )
    period_radii = chain_radii + handle_radii + wall_radii
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    defect = np.nextafter(
        np.asarray(
            jacobian["verified_interval_nonsingularity"][
                "componentwise_preconditioned_defect_upper_8_by_8"
            ],
            dtype=np.float64,
        ),
        math.inf,
    )
    correction_errors = seed.positive_matvec_upper(
        abs(inverse), np.nextafter(period_radii, math.inf)
    )
    zero_center = np.zeros(8, dtype=np.float64)
    method_floor_radii = seed.scaled_point_radius(
        zero_center, correction_errors, defect, 1.0
    )
    method_floor_disk = float(np.max(method_floor_radii))
    method_floor_square = method_floor_disk / math.sqrt(2.0)

    chart_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    if len(chart_radii) != 1:
        raise AssertionError("A385S y/z coordinate radii differ")
    chart_square = chart_radii.pop()
    chart_disk = math.sqrt(2.0) * chart_square
    gap = method_floor_square / chart_square
    if not method_floor_disk > chart_disk:
        raise AssertionError("the beta-only independent-box method floor fits A385S")

    contributions = {
        "raw_76_thimble_chain": summary(chain_radii),
        "A383_handle": summary(handle_radii),
        "three_times_d065_wall": summary(wall_radii),
    }
    dominant_source = max(
        contributions,
        key=lambda name: contributions[name]["product_box_l2_radius_upper"],
    )
    payload = {
        "schema": "MTTQ79HeightFourBetaOnlyKrawczykMethodFloor.v1",
        "status": "BETA_ONLY_INDEPENDENT_BOX_KRAWCZYK_METHOD_FLOOR_EXCEEDS_A385S",
        "artifact": ARTIFACT,
        "optimistic_limit_definition": {
            "beta_component_radii_set_to_zero": True,
            "residual_center_correction_set_to_zero": True,
            "current_A373_chain_A383_handle_and_d065_wall_radii_retained": True,
            "current_A384_point_Jacobian_defect_retained": True,
            "beta_period_cross_correlation_intentionally_absent": True,
        },
        "period_component_radius_uppers": period_radii.tolist(),
        "period_source_contributions": contributions,
        "dominant_period_source_by_l2_radius": dominant_source,
        "A384_preconditioned_period_uncertainty_uppers": correction_errors.tolist(),
        "method_floor_coordinate_disk_radii": method_floor_radii.tolist(),
        "summary": {
            "period_product_box_l2_radius_upper": float(np.linalg.norm(period_radii)),
            "maximum_period_component_radius_upper": float(np.max(period_radii)),
            "dominant_period_residue_index_zero_based": int(np.argmax(period_radii)),
            "optimistic_method_floor_maximum_complex_disk_radius": method_floor_disk,
            "optimistic_method_floor_equivalent_real_imaginary_square_radius": (
                method_floor_square
            ),
            "A385S_real_imaginary_square_radius": chart_square,
            "A385S_complex_disk_radius": chart_disk,
            "method_floor_to_A385S_square_gap_factor": gap,
            "beta_only_tightening_can_close_current_independent_box_point_test": False,
        },
        "authority": {
            "A373_final_76_target_prefix": authority(PREFIX),
            "A231_chain_and_PL_identity": authority(A231),
            "A383_handle_Hessian_and_ordinary_rows": authority(A383),
            "A384_point_residual_Jacobian": authority(A384),
            "A385S_selected_polydisk_chart": authority(A385S),
            "A393_relation_L1_optimality": authority(A393),
            "d065_full_interval": authority(D065),
            "A387_numerical_algorithm_source": authority(Path(seed.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "monotone_limit_of_current_independent_box_point_test_computed": True,
            "beta_only_tightening_sufficient_for_current_A385S_test": False,
            "lower_bound_on_true_residual_uncertainty_proved": False,
            "all_possible_correlation_preserving_enclosures_excluded": False,
            "absence_of_a_covariant_zero_proved": False,
            "coupled_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "construct a coupled beta-period residual transport that preserves "
            "cancellation, or tighten the selected period enclosures themselves; "
            "beta-only radius improvement cannot close the current independent-box test"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Beta-Only Krawczyk Method Floor (A396) v1\n\n"
        "A396 evaluates the optimistic monotone limit of the current independent-"
        "box point-Krawczyk calculation: all beta uncertainty and the residual "
        "center correction are set to zero, while the certified 76-cycle, handle, "
        "wall, and A384 point-Jacobian enclosures are retained.\n\n"
        f"The resulting equivalent coordinate-square radius is "
        f"`{method_floor_square:.12g}`, compared with the A385S radius "
        f"`{chart_square:.12g}`: a gap of `{gap:.12g}`. The dominant retained "
        f"period source in L2 radius is `{dominant_source}`.\n\n"
        "This is a no-go result only for beta-only tightening inside the current "
        "independent-box sufficient test. It is not a lower bound on the true "
        "residual uncertainty and does not exclude a correlation-preserving "
        "coupled transport or a covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
