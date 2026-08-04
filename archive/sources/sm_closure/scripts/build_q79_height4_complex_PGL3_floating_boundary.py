from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
DIRECTORY = probe.PROBE_DIRECTORY
A215 = DIRECTORY / "rank3_complex_PGL3_completion.packet.json"
A216 = DIRECTORY / "imaginary_holomorphic_direction_check.packet.json"
A217 = DIRECTORY / "rank3_complex_PGL3_refinement_02.packet.json"
A218 = DIRECTORY / "rank3_complex_PGL3_refinement_03.packet.json"
N1 = DIRECTORY / "cplx" / "n1" / "probe.packet.json"
N2 = DIRECTORY / "cplx" / "n2ud" / "probe.packet.json"
N3_ULTRA = DIRECTORY / "cplx" / "n3ud" / "probe.packet.json"
N3_EXTREME = DIRECTORY / "cplx" / "n3xd" / "probe.packet.json"
OUTPUT = DIRECTORY / "rank3_complex_PGL3_floating_boundary.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourComplexPGL3FloatingBoundary_A219_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def selected(packet: dict) -> dict:
    return next(
        row
        for row in packet["candidate_residuals"]
        if int(row["A132_objective_rank"]) == 3
    )


def complex_matrix(values: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[probe.complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def main() -> int:
    started = time.perf_counter()
    a215 = load(A215)
    a216 = load(A216)
    n1 = load(N1)
    n2 = load(N2)
    ultra = load(N3_ULTRA)
    extreme = load(N3_EXTREME)
    rows = {
        "A212_center": probe.complex_vector(a215["center_residual"]),
        "complex_Newton_01": probe.complex_vector(
            selected(n1)["PL_corrected_residual"]
        ),
        "complex_Newton_02": probe.complex_vector(
            selected(n2)["PL_corrected_residual"]
        ),
        "complex_Newton_03_ultra": probe.complex_vector(
            selected(ultra)["PL_corrected_residual"]
        ),
        "complex_Newton_03_extreme": probe.complex_vector(
            selected(extreme)["PL_corrected_residual"]
        ),
    }
    history = [
        {
            "stage": name,
            "residual_l2_norm": float(np.linalg.norm(value)),
            "residual_maximum_absolute_value": float(np.max(abs(value))),
        }
        for name, value in rows.items()
    ]

    ultra_row = selected(ultra)
    extreme_row = selected(extreme)
    ultra_residual = rows["complex_Newton_03_ultra"]
    extreme_residual = rows["complex_Newton_03_extreme"]
    residual_difference = extreme_residual - ultra_residual
    residual_midpoint = (ultra_residual + extreme_residual) / 2.0
    empirical_l2_radius = float(np.linalg.norm(residual_difference) / 2.0)
    empirical_max_radius = float(np.max(abs(residual_difference)) / 2.0)
    ultra_period = probe.complex_vector(
        ultra_row["PL_corrected_moving_period"]
    )
    extreme_period = probe.complex_vector(
        extreme_row["PL_corrected_moving_period"]
    )
    ultra_beta = ultra_residual + ultra_period
    extreme_beta = extreme_residual + extreme_period
    ultra_handles = complex_matrix(
        ultra["moving_handles"]["primitive_handle_period_matrix"]
    )
    extreme_handles = complex_matrix(
        extreme["moving_handles"]["primitive_handle_period_matrix"]
    )

    queue = load(probe.A208)["height_four_candidates"][1:]
    candidate = next(
        row for row in queue if int(row["A132_objective_rank"]) == 3
    )
    column_signs = np.asarray(
        load(probe.ORIENTATION)["column_signs"], dtype=np.int64
    )
    thimble_rows = []
    thimble_sum = np.zeros(8, dtype=np.complex128)
    for chain_row in candidate["primitive_thimble_chain"]:
        index = int(chain_row["distinguished_index"])
        signed_coefficient = int(chain_row["coefficient"]) * int(
            column_signs[index - 1]
        )
        ultra_thimble = load(N3_ULTRA.parent / "thimbles" / f"t{index:03d}.json")
        extreme_thimble = load(
            N3_EXTREME.parent / "thimbles" / f"t{index:03d}.json"
        )
        difference = signed_coefficient * (
            probe.complex_vector(extreme_thimble["period_values"])
            - probe.complex_vector(ultra_thimble["period_values"])
        )
        thimble_sum += difference
        thimble_rows.append(
            {
                "distinguished_index": index,
                "root_id": ultra_thimble["root_id"],
                "signed_coefficient": signed_coefficient,
                "contribution_difference": probe.encoded_complex_vector(difference),
                "contribution_difference_l2_norm": float(np.linalg.norm(difference)),
                "contribution_difference_maximum_absolute_value": float(
                    np.max(abs(difference))
                ),
                "ultra_numerics": ultra_thimble["numerics"],
                "extreme_numerics": extreme_thimble["numerics"],
            }
        )
    thimble_rows.sort(
        key=lambda row: row["contribution_difference_l2_norm"], reverse=True
    )
    individual_norm_sum = sum(
        row["contribution_difference_l2_norm"] for row in thimble_rows
    )
    dominant = thimble_rows[0]

    gate = {
        "A215_complex_Jacobian_full_rank": a215["complex_Jacobian_rank"] == 8,
        "A216_imaginary_check_accepted": all(a216["acceptance_gate"].values()),
        "three_nonlinear_steps_monotonically_reduce_ultra_residual": all(
            history[index + 1]["residual_l2_norm"]
            < history[index]["residual_l2_norm"]
            for index in range(3)
        ),
        "ultra_and_extreme_same_beta_homotopy": all(
            not packet["moving_beta"]["path"]["homotopy_strip_root_ids"]
            for packet in (ultra, extreme)
        ),
        "zero_inside_empirical_l2_profile_ball": float(
            np.linalg.norm(residual_midpoint)
        )
        <= empirical_l2_radius,
        "floating_profile_difference_dominates_each_n3_residual": all(
            np.linalg.norm(value) <= np.linalg.norm(residual_difference)
            for value in (ultra_residual, extreme_residual)
        ),
        "dominant_thimble_is_d087": dominant["distinguished_index"] == 87,
    }
    if not all(gate.values()):
        raise AssertionError(f"floating-boundary gate failed: {gate}")

    output = {
        "schema": "MTTQ79HeightFourComplexPGL3FloatingBoundary.v1",
        "status": "FLOATING_ZERO_UNRESOLVED_VALIDATED_PERIOD_TRANSPORT_REQUIRED",
        "candidate_rank": 3,
        "Newton_history": history,
        "n3_profile_comparison": {
            "ultra_residual": probe.encoded_complex_vector(ultra_residual),
            "extreme_residual": probe.encoded_complex_vector(extreme_residual),
            "residual_difference": probe.encoded_complex_vector(
                residual_difference
            ),
            "residual_difference_l2_norm": float(
                np.linalg.norm(residual_difference)
            ),
            "residual_difference_maximum_absolute_value": float(
                np.max(abs(residual_difference))
            ),
            "empirical_midpoint": probe.encoded_complex_vector(residual_midpoint),
            "empirical_midpoint_l2_norm": float(np.linalg.norm(residual_midpoint)),
            "empirical_l2_radius": empirical_l2_radius,
            "empirical_maximum_coordinate_radius": empirical_max_radius,
            "zero_inside_empirical_l2_ball": float(
                np.linalg.norm(residual_midpoint)
            )
            <= empirical_l2_radius,
            "not_an_interval_ball": True,
        },
        "difference_decomposition": {
            "selected_period_difference_l2_norm": float(
                np.linalg.norm(extreme_period - ultra_period)
            ),
            "anchored_beta_difference_l2_norm": float(
                np.linalg.norm(extreme_beta - ultra_beta)
            ),
            "handle_matrix_difference_frobenius_norm": float(
                np.linalg.norm(extreme_handles - ultra_handles)
            ),
            "primitive_thimble_chain_difference": probe.encoded_complex_vector(
                thimble_sum
            ),
            "primitive_thimble_chain_difference_l2_norm": float(
                np.linalg.norm(thimble_sum)
            ),
            "sum_of_individual_thimble_contribution_norms": individual_norm_sum,
            "chain_cancellation_ratio": float(
                np.linalg.norm(thimble_sum) / individual_norm_sum
            ),
            "dominant_thimble": dominant,
            "top_five_fraction_of_individual_norm_sum": float(
                sum(
                    row["contribution_difference_l2_norm"]
                    for row in thimble_rows[:5]
                )
                / individual_norm_sum
            ),
            "ranked_thimble_contributions": thimble_rows,
        },
        "acceptance_gate": gate,
        "next_required_artifact": (
            "validated or arbitrary-precision Picard-Fuchs transport for d087, "
            "followed by d034, d041, d030, and d062 and a recomposed rank-3 chain"
        ),
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A215": A215,
                "A216": A216,
                "A217": A217,
                "A218": A218,
                "n1": N1,
                "n2_ultra_detour": N2,
                "n3_ultra_detour": N3_ULTRA,
                "n3_extreme_detour": N3_EXTREME,
                "source": Path(__file__),
            }.items()
        },
        "strict_scope": {
            "same_source_complex_Newton_history_executed": True,
            "floating_profile_boundary_identified": True,
            "empirical_ball_is_not_interval_certificate": True,
            "covariant_zero_proved": False,
            "selected_alignment_exists_proved": False,
            "full_SM_closure_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, output)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Complex PGL(3) Floating Boundary (A219) v1

Three wall-free nonlinear complex Newton executions reduce the selected
same-source residual from `{history[0]['residual_l2_norm']:.12g}` through
`{history[1]['residual_l2_norm']:.12g}` and
`{history[2]['residual_l2_norm']:.12g}` to
`{history[3]['residual_l2_norm']:.12g}` in the ultra profile.

At the identical n3 alignment the extreme profile gives
`{history[4]['residual_l2_norm']:.12g}`.  The two residual vectors differ by
`{np.linalg.norm(residual_difference):.12g}`, and the empirical ball centered
at their midpoint has radius `{empirical_l2_radius:.12g}` while its center norm
is `{np.linalg.norm(residual_midpoint):.12g}`.  Thus zero lies inside this
empirical floating envelope.  This is not an interval certificate.

The profile difference is period-dominated:

- selected period difference: `{np.linalg.norm(extreme_period - ultra_period):.12g}`;
- anchored beta difference: `{np.linalg.norm(extreme_beta - ultra_beta):.12g}`;
- handle-matrix difference: `{np.linalg.norm(extreme_handles - ultra_handles):.12g}`.

Thimble `d{dominant['distinguished_index']:03d}` is the dominant unstable
contribution, with norm `{dominant['contribution_difference_l2_norm']:.12g}`.
The next proof object is validated or arbitrary-precision Picard-Fuchs
transport for that thimble and then the remaining top contributors.  No
covariant zero, selected alignment existence theorem, or full SM closure is
claimed here.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps({
        "ultra_residual_l2_norm": float(np.linalg.norm(ultra_residual)),
        "extreme_residual_l2_norm": float(np.linalg.norm(extreme_residual)),
        "interprofile_difference_l2_norm": float(np.linalg.norm(residual_difference)),
        "empirical_midpoint_l2_norm": float(np.linalg.norm(residual_midpoint)),
        "empirical_l2_radius": empirical_l2_radius,
        "dominant_thimble": dominant["distinguished_index"],
        "dominant_thimble_difference_l2_norm": dominant[
            "contribution_difference_l2_norm"
        ],
        "elapsed_seconds": time.perf_counter() - started,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
