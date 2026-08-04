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
DIRECTORY = probe.PROBE_DIRECTORY
A215 = DIRECTORY / "rank3_complex_PGL3_completion.packet.json"
A216 = DIRECTORY / "imaginary_holomorphic_direction_check.packet.json"
TRIAL_01 = DIRECTORY / "cplx" / "n1" / "probe.packet.json"
OUTPUT = DIRECTORY / "rank3_complex_PGL3_refinement_02.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourComplexPGL3NonlinearRefinement_A217_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_matrix(values: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[probe.complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def selected(packet: dict) -> dict:
    return next(
        row
        for row in packet["candidate_residuals"]
        if int(row["A132_objective_rank"]) == 3
    )


def main() -> int:
    ctx.dps = 100
    started = time.perf_counter()
    a215 = load(A215)
    a216 = load(A216)
    trial = load(TRIAL_01)
    if not all(a216["acceptance_gate"].values()):
        raise AssertionError("A216 imaginary-direction check is not accepted")
    if a215["summary"]["crossing_count"] != 0:
        raise AssertionError("A215 first Newton segment is not wall-free")

    target_01 = complex_matrix(a215["target_alignment"])
    actual_alignment = complex_matrix(trial["alignment"])
    alignment_replay_error = float(np.max(abs(target_01 - actual_alignment)))
    if alignment_replay_error > 1.0e-14:
        raise AssertionError("executed A215 alignment does not replay its target")

    trial_row = selected(trial)
    residual = probe.complex_vector(trial_row["PL_corrected_residual"])
    center_residual = probe.complex_vector(
        trial_row["base_PL_corrected_residual"]
    )
    jacobian = complex_matrix(a215["complex_Jacobian"])
    correction = np.linalg.solve(jacobian, -residual)
    prediction = residual + jacobian @ correction
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (correction[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    target_02 = actual_alignment @ expm(tangent)

    a208 = load(probe.A208)
    candidates = a208["height_four_candidates"][1:]
    support_indices = {
        int(row["distinguished_index"])
        for candidate in candidates
        for row in candidate["primitive_thimble_chain"]
    }
    target_root_ids = {
        row["root_id"]
        for row in load(probe.FAN)["distinguished_positive_meridians"]
        if int(row["distinguished_index"]) in support_indices
    }

    samples = []
    crossings = []
    previous_radial = None
    previous_handles = None
    for sample_index, scale in enumerate(np.linspace(0.0, 1.0, 9)):
        alignment = actual_alignment @ expm(float(scale) * tangent)
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
            f"[{sample_index + 1}/9] scale={scale:.3f} "
            f"nearest={nearest['target_root_id']}/{nearest['other_root_id']}:"
            f"{nearest['signed_transverse_coordinate']:+.3e} "
            f"crossings={len(new_crossings)}",
            flush=True,
        )

    reduction_factor = float(np.linalg.norm(residual) / np.linalg.norm(center_residual))
    gate = {
        "first_nonlinear_residual_below_1e_5": float(np.linalg.norm(residual))
        < 1.0e-5,
        "first_nonlinear_reduction_factor_below_2e_3": reduction_factor < 2.0e-3,
        "first_segment_wall_free": a215["summary"]["crossing_count"] == 0,
        "refinement_segment_wall_free": len(crossings) == 0,
        "independent_imaginary_check_accepted": all(
            a216["acceptance_gate"].values()
        ),
    }
    if not all(gate.values()):
        raise AssertionError(f"complex refinement gate failed: {gate}")

    output = {
        "schema": "MTTQ79HeightFourComplexPGL3Refinement.v1",
        "status": "NONLINEAR_COMPLEX_NEWTON_STEP01_ACCEPTED_AND_STEP02_PROFILED",
        "candidate_rank": 3,
        "step_01": {
            "center_residual_l2_norm": float(np.linalg.norm(center_residual)),
            "actual_residual": probe.encoded_complex_vector(residual),
            "actual_residual_l2_norm": float(np.linalg.norm(residual)),
            "actual_residual_maximum_absolute_value": float(np.max(abs(residual))),
            "reduction_factor": reduction_factor,
            "alignment_replay_maximum_error": alignment_replay_error,
            "same_fixed_handle_chamber": trial["strict_scope"][
                "same_fixed_handle_chamber"
            ],
            "same_post_PL_radial_chamber": trial["strict_scope"][
                "same_post_selected_039_selected_038_radial_chamber"
            ],
        },
        "step_02": {
            "recentered_residual": probe.encoded_complex_vector(residual),
            "complex_correction": probe.encoded_complex_vector(correction),
            "complex_correction_l2_norm": float(np.linalg.norm(correction)),
            "complex_correction_maximum_absolute_coordinate": float(
                np.max(abs(correction))
            ),
            "linearized_residual": probe.encoded_complex_vector(prediction),
            "linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
            "base_alignment": probe.encoded_complex_matrix(actual_alignment),
            "target_alignment": probe.encoded_complex_matrix(target_02),
            "chamber_profile": {"samples": samples, "crossings": crossings},
        },
        "acceptance_gate": gate,
        "summary": {
            "step_01_actual_residual_l2_norm": float(np.linalg.norm(residual)),
            "step_01_reduction_factor": reduction_factor,
            "step_02_correction_maximum_absolute_coordinate": float(
                np.max(abs(correction))
            ),
            "step_02_linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
            "step_02_crossing_count": len(crossings),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "A215": relative(A215),
            "A215_sha256": sha256(A215),
            "A216": relative(A216),
            "A216_sha256": sha256(A216),
            "step_01_trial": relative(TRIAL_01),
            "step_01_trial_sha256": sha256(TRIAL_01),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "step_01_same_source_nonlinear_execution": True,
            "step_02_uses_step_01_actual_residual": True,
            "step_02_uses_A213_center_Jacobian": True,
            "step_02_recentered_Jacobian_executed": False,
            "step_02_nonlinear_execution_pending": True,
            "interval_zero_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, output)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Complex PGL(3) Nonlinear Refinement (A217) v1

The wall-free A215 complex Newton alignment was executed through the full
same-source period and beta evaluator.  The selected rank-3 residual fell from
`{np.linalg.norm(center_residual):.12g}` to `{np.linalg.norm(residual):.12g}`,
a reduction factor of `{reduction_factor:.6g}`.

This is a nonlinear result, not a linear prediction.  A second correction,
formed from the actual endpoint residual and the nonsingular A213/A215 complex
Jacobian, has maximum coefficient `{np.max(abs(correction)):.6g}`.  Its sampled
continuation segment has `{len(crossings)}` radial or handle-wall crossings.

The first nonlinear step is accepted.  The second correction remains a
profiled proposal until its full same-source nonlinear execution is recorded.
An interval zero certificate is still open.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(output["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
