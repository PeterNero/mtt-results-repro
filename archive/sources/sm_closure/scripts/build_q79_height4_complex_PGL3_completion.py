from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe
from build_q79_height4_covariant_recentered_step import (
    handle_coordinates,
    radial_coordinates,
)


ROOT = probe.ROOT
JACOBIAN = probe.PROBE_DIRECTORY / "height4_covariant_PL_recentered_jacobian.packet.json"
BASE_TRIAL = probe.PROBE_DIRECTORY / "tr3_s1d000ep00" / "trial.packet.json"
OUTPUT = probe.PROBE_DIRECTORY / "rank3_complex_PGL3_completion.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourComplexPGL3Completion_A215_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    ctx.dps = 100
    started = time.perf_counter()
    packet = load(JACOBIAN)
    selected = next(
        row
        for row in packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 3
    )
    jacobian = np.asarray(
        [
            [probe.complex_value(value) for value in row]
            for row in selected["covariant_residual_Jacobian_8_by_k"]
        ],
        dtype=np.complex128,
    )
    residual = probe.complex_vector(selected["center_residual"])
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    complex_rank = int(np.linalg.matrix_rank(jacobian))
    if complex_rank != 8:
        raise AssertionError("post-A212 complex Jacobian is singular")
    step = np.linalg.solve(jacobian, -residual)
    prediction = residual + jacobian @ step
    realified = np.block(
        [[jacobian.real, -jacobian.imag], [jacobian.imag, jacobian.real]]
    )
    real_singular_values = np.linalg.svd(realified, compute_uv=False)
    if int(np.linalg.matrix_rank(realified)) != 16:
        raise AssertionError("complex Jacobian realification is not full rank")

    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (step[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    base_alignment = probe.complex_matrix(load(BASE_TRIAL)["alignment"])
    a208 = load(probe.A208)
    candidates = a208["height_four_candidates"][1:]
    support_indices = {
        int(row["distinguished_index"])
        for candidate in candidates
        for row in candidate["primitive_thimble_chain"]
    }
    fan = load(probe.FAN)["distinguished_positive_meridians"]
    target_root_ids = {
        row["root_id"]
        for row in fan
        if int(row["distinguished_index"]) in support_indices
    }

    samples = []
    previous_radial = None
    previous_handles = None
    crossings = []
    for sample_index, scale in enumerate(np.linspace(0.0, 1.0, 17)):
        alignment = base_alignment @ expm(float(scale) * tangent)
        centers, diagnostics = probe.continued_critical_centers(alignment)
        radial = radial_coordinates(centers, target_root_ids)
        handles = handle_coordinates(centers)
        new_crossings = []
        if previous_radial is not None:
            for key in sorted(set(previous_radial) & set(radial)):
                old = previous_radial[key]["signed_transverse_coordinate"]
                new = radial[key]["signed_transverse_coordinate"]
                if old * new < 0:
                    new_crossings.append(
                        {
                            "kind": "radial_thimble",
                            "pair": key,
                            "lower_scale": samples[-1]["scale"],
                            "upper_scale": float(scale),
                            "lower_signed_coordinate": old,
                            "upper_signed_coordinate": new,
                        }
                    )
            for name in ("A", "B"):
                for root_id, new in handles[name].items():
                    old = previous_handles[name][root_id]
                    if old * new < 0:
                        new_crossings.append(
                            {
                                "kind": "global_handle",
                                "handle": name,
                                "root_id": root_id,
                                "lower_scale": samples[-1]["scale"],
                                "upper_scale": float(scale),
                                "lower_signed_coordinate": old,
                                "upper_signed_coordinate": new,
                            }
                        )
        nearest = min(radial.values(), key=lambda row: row["clearance"])
        samples.append(
            {
                "sample_index": sample_index,
                "scale": float(scale),
                "nearest_radial_pair": nearest,
                "minimum_A_handle_clearance": min(
                    abs(value) for value in handles["A"].values()
                ),
                "minimum_B_handle_clearance": min(
                    abs(value) for value in handles["B"].values()
                ),
                "crossings_from_previous_sample": new_crossings,
                "critical_continuation": diagnostics,
            }
        )
        crossings.extend(new_crossings)
        previous_radial = radial
        previous_handles = handles
        print(
            f"[{sample_index + 1}/17] scale={scale:.4f} "
            f"nearest={nearest['target_root_id']}/{nearest['other_root_id']}:"
            f"{nearest['signed_transverse_coordinate']:+.3e} "
            f"crossings={len(new_crossings)}",
            flush=True,
        )

    crossing_lower_scales = [float(row["lower_scale"]) for row in crossings]
    safe_scale = min(crossing_lower_scales) if crossing_lower_scales else 1.0
    target_alignment = base_alignment @ expm(tangent)
    output = {
        "schema": "MTTQ79HeightFourComplexPGL3Completion.v1",
        "status": "FULL_COMPLEX_PGL3_LINEARIZED_ZERO_AND_WALL_PROFILE_EXECUTED",
        "candidate_rank": 3,
        "holomorphic_completion": {
            "real_generators": 8,
            "complex_generators": 8,
            "real_tangent_dimension": 16,
            "rule": "D_(iG_k) F = i D_(G_k) F inside a fixed holomorphic PL chamber",
            "independent_imaginary_direction_probe_executed": False,
        },
        "complex_Jacobian": probe.encoded_complex_matrix(jacobian),
        "complex_Jacobian_rank": complex_rank,
        "complex_Jacobian_singular_values": [
            float(value) for value in singular_values
        ],
        "complex_Jacobian_condition_number": float(
            singular_values[0] / singular_values[-1]
        ),
        "complex_Jacobian_determinant_absolute_value": float(
            abs(np.linalg.det(jacobian))
        ),
        "realified_Jacobian_shape": list(realified.shape),
        "realified_Jacobian_rank": int(np.linalg.matrix_rank(realified)),
        "realified_Jacobian_singular_values": [
            float(value) for value in real_singular_values
        ],
        "center_residual": probe.encoded_complex_vector(residual),
        "center_residual_l2_norm": float(np.linalg.norm(residual)),
        "complex_Newton_step": [probe.complex_pair(value) for value in step],
        "complex_Newton_step_maximum_absolute_coordinate": float(
            np.max(abs(step))
        ),
        "complex_Newton_step_l2_norm": float(np.linalg.norm(step)),
        "linearized_residual": probe.encoded_complex_vector(prediction),
        "linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
        "base_alignment": probe.encoded_complex_matrix(base_alignment),
        "target_alignment": probe.encoded_complex_matrix(target_alignment),
        "chamber_profile": {"samples": samples, "crossings": crossings},
        "maximum_sampled_wall_free_scale": safe_scale,
        "summary": {
            "complex_Jacobian_rank": complex_rank,
            "realified_Jacobian_rank": int(np.linalg.matrix_rank(realified)),
            "complex_condition_number": float(
                singular_values[0] / singular_values[-1]
            ),
            "center_residual_l2_norm": float(np.linalg.norm(residual)),
            "linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
            "complex_step_maximum_absolute_coordinate": float(np.max(abs(step))),
            "crossing_count": len(crossings),
            "first_crossing_lower_scale": (
                min(crossing_lower_scales) if crossing_lower_scales else None
            ),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "radial_helper_source": relative(
                ROOT / "scripts" / "build_q79_height4_covariant_recentered_step.py"
            ),
            "radial_helper_source_sha256": sha256(
                ROOT / "scripts" / "build_q79_height4_covariant_recentered_step.py"
            ),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "complex_PGL3_tangent_not_new_empirical_parameters": True,
            "holomorphic_completion_used": True,
            "independent_imaginary_probe_pending": True,
            "linearized_zero_only": True,
            "nonlinear_step_executed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, output)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Complex PGL(3) Completion (A215) v1

The previous Jacobians varied eight real `sl3` generators.  The selected
alignment is complex, so the holomorphic tangent of `PGL(3,C)` contains those
eight generators and their `i` multiples: sixteen real directions in total.

At the A212 rank-3 center, the complex 8-by-8 Jacobian has rank
`{complex_rank}`, condition number `{singular_values[0] / singular_values[-1]:.6g}`,
and determinant magnitude `{abs(np.linalg.det(jacobian)):.6g}`.  Its realification
has rank `{np.linalg.matrix_rank(realified)}`.

The complex Newton step has maximum coefficient `{np.max(abs(step)):.6g}` and
reduces the linearized residual from `{np.linalg.norm(residual):.12g}` to
`{np.linalg.norm(prediction):.3e}`.

This removes the artificial real-subgroup residual floor.  It is a linearized,
floating result.  An independent `iG` finite-difference probe, nonlinear
execution, chamber-aware continuation, and interval certification remain
required before claiming a covariant zero.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(output["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
