from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
DIRECTORY = probe.PROBE_DIRECTORY
JACOBIAN = DIRECTORY / "height4_covariant_PL_recentered_jacobian.packet.json"
PLUS = (
    DIRECTORY
    / "PL_recentered_imaginary_step"
    / "id01_p_h1d0em06"
    / "probe.packet.json"
)
MINUS = (
    DIRECTORY
    / "PL_recentered_imaginary_step"
    / "id01_m_h1d0em06"
    / "probe.packet.json"
)
OUTPUT = DIRECTORY / "imaginary_holomorphic_direction_check.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourImaginaryHolomorphicCheck_A216_v1.md"
STEP = 1.0e-6


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
    plus_packet = load(PLUS)
    minus_packet = load(MINUS)
    jacobian_packet = load(JACOBIAN)
    plus_row = selected(plus_packet)
    minus_row = selected(minus_packet)
    plus_residual = probe.complex_vector(plus_row["PL_corrected_residual"])
    minus_residual = probe.complex_vector(minus_row["PL_corrected_residual"])
    center_residual = probe.complex_vector(
        plus_row["base_PL_corrected_residual"]
    )
    if np.max(
        abs(
            center_residual
            - probe.complex_vector(minus_row["base_PL_corrected_residual"])
        )
    ) > 1.0e-14:
        raise AssertionError("signed imaginary probes do not share one center")

    selected_jacobian = next(
        row
        for row in jacobian_packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 3
    )
    real_jacobian = complex_matrix(
        selected_jacobian["covariant_residual_Jacobian_8_by_k"]
    )
    measured = (plus_residual - minus_residual) / (2.0 * STEP)
    expected = 1.0j * real_jacobian[:, 0]
    discrepancy = measured - expected
    midpoint_error = (plus_residual + minus_residual) / 2.0 - center_residual
    relative_error = float(np.linalg.norm(discrepancy) / np.linalg.norm(measured))
    gate = {
        "relative_holomorphic_derivative_error_at_most_5e_4": relative_error
        <= 5.0e-4,
        "midpoint_replay_maximum_error_at_most_2e_8": float(
            np.max(abs(midpoint_error))
        )
        <= 2.0e-8,
        "both_probes_same_post_PL_chamber": all(
            packet["strict_scope"][
                "same_post_selected_039_selected_038_radial_chamber"
            ]
            for packet in (plus_packet, minus_packet)
        ),
        "both_probes_same_fixed_handle_chamber": all(
            packet["strict_scope"]["same_fixed_handle_chamber"]
            for packet in (plus_packet, minus_packet)
        ),
    }
    if not all(gate.values()):
        raise AssertionError(f"imaginary holomorphic check failed: {gate}")

    output = {
        "schema": "MTTQ79HeightFourImaginaryHolomorphicCheck.v1",
        "status": "INDEPENDENT_IMAGINARY_TANGENT_CHECK_ACCEPTED",
        "candidate_rank": 3,
        "generator_direction_one_based": 1,
        "generator_name": "E12",
        "finite_difference_step": STEP,
        "measured_imaginary_direction_derivative": probe.encoded_complex_vector(
            measured
        ),
        "holomorphic_prediction_i_times_real_derivative": probe.encoded_complex_vector(
            expected
        ),
        "derivative_discrepancy": probe.encoded_complex_vector(discrepancy),
        "derivative_discrepancy_l2_norm": float(np.linalg.norm(discrepancy)),
        "measured_derivative_l2_norm": float(np.linalg.norm(measured)),
        "relative_holomorphic_derivative_error": relative_error,
        "signed_midpoint_replay_error": probe.encoded_complex_vector(midpoint_error),
        "signed_midpoint_replay_error_l2_norm": float(np.linalg.norm(midpoint_error)),
        "signed_midpoint_replay_error_maximum_absolute_value": float(
            np.max(abs(midpoint_error))
        ),
        "acceptance_gate": gate,
        "authority": {
            "real_Jacobian": relative(JACOBIAN),
            "real_Jacobian_sha256": sha256(JACOBIAN),
            "positive_imaginary_probe": relative(PLUS),
            "positive_imaginary_probe_sha256": sha256(PLUS),
            "negative_imaginary_probe": relative(MINUS),
            "negative_imaginary_probe_sha256": sha256(MINUS),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "independent_imaginary_direction_executed": True,
            "all_eight_imaginary_directions_executed": False,
            "fixed_PL_chamber_check": True,
            "finite_difference_check_not_interval_identity": True,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, output)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Imaginary Holomorphic Check (A216) v1

The same-source A212 evaluator was executed at `exp(+ihG_1)` and
`exp(-ihG_1)` with `h={STEP:.1e}`.  Both endpoints remain in the same fixed
handle chamber and the same post-Picard-Lefschetz radial chamber.

The centered imaginary-direction derivative agrees with `i` times the
independently computed real A213 derivative to relative error
`{relative_error:.6g}`.  Its signed midpoint replay error is
`{np.max(abs(midpoint_error)):.6g}` in maximum norm.

This is an independent numerical check of the holomorphic tangent rule used
by A215.  It checks one of eight complex generators and is not an interval
proof of holomorphicity or a proof of a covariant zero.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps({
        "relative_holomorphic_derivative_error": relative_error,
        "midpoint_replay_maximum_error": float(np.max(abs(midpoint_error))),
        "accepted": all(gate.values()),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
