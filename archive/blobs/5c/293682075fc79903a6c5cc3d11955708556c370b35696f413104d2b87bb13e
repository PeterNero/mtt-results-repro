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
TRIAL_02 = DIRECTORY / "cplx" / "n2ud" / "probe.packet.json"
OUTPUT = DIRECTORY / "rank3_complex_PGL3_refinement_03.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourComplexPGL3Refinement03_A218_v1.md"


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
    trial = load(TRIAL_02)
    if trial["numerical_profile"] != "ultra_accuracy":
        raise AssertionError("step-02 trial is not the ultra-accuracy replay")
    if trial["moving_beta"]["path"]["homotopy_strip_root_ids"]:
        raise AssertionError("step-02 beta detour changed homotopy class")
    if not trial["strict_scope"]["beta_path_same_homotopy_strip_empty"]:
        raise AssertionError("step-02 beta path gate is not accepted")

    row = selected(trial)
    residual = probe.complex_vector(row["PL_corrected_residual"])
    jacobian = complex_matrix(a215["complex_Jacobian"])
    correction = np.linalg.solve(jacobian, -residual)
    prediction = residual + jacobian @ correction
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (correction[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    base_alignment = complex_matrix(trial["alignment"])
    target_alignment = base_alignment @ expm(tangent)

    candidates = load(probe.A208)["height_four_candidates"][1:]
    support_indices = {
        int(chain_row["distinguished_index"])
        for candidate in candidates
        for chain_row in candidate["primitive_thimble_chain"]
    }
    target_root_ids = {
        fan_row["root_id"]
        for fan_row in load(probe.FAN)["distinguished_positive_meridians"]
        if int(fan_row["distinguished_index"]) in support_indices
    }
    samples = []
    crossings = []
    previous_radial = None
    previous_handles = None
    for sample_index, scale in enumerate(np.linspace(0.0, 1.0, 9)):
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
        nearest = min(radial.values(), key=lambda value: value["clearance"])
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

    gate = {
        "step_02_residual_below_1e_7": float(np.linalg.norm(residual)) < 1.0e-7,
        "step_02_ultra_accuracy": trial["numerical_profile"] == "ultra_accuracy",
        "step_02_same_homotopy_beta_detour": not trial["moving_beta"]["path"][
            "homotopy_strip_root_ids"
        ],
        "step_03_segment_wall_free": len(crossings) == 0,
        "step_03_correction_below_1e_8": float(np.max(abs(correction))) < 1.0e-8,
    }
    if not all(gate.values()):
        raise AssertionError(f"step-03 refinement gate failed: {gate}")
    output = {
        "schema": "MTTQ79HeightFourComplexPGL3Refinement03.v1",
        "status": "ULTRA_STEP02_ACCEPTED_AND_STEP03_PROFILED",
        "candidate_rank": 3,
        "step_02": {
            "actual_residual": probe.encoded_complex_vector(residual),
            "actual_residual_l2_norm": float(np.linalg.norm(residual)),
            "actual_residual_maximum_absolute_value": float(np.max(abs(residual))),
            "alignment": probe.encoded_complex_matrix(base_alignment),
            "numerical_profile": trial["numerical_profile"],
            "beta_path": trial["moving_beta"]["path"],
        },
        "step_03": {
            "complex_correction": probe.encoded_complex_vector(correction),
            "complex_correction_l2_norm": float(np.linalg.norm(correction)),
            "complex_correction_maximum_absolute_coordinate": float(
                np.max(abs(correction))
            ),
            "linearized_residual": probe.encoded_complex_vector(prediction),
            "linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
            "base_alignment": probe.encoded_complex_matrix(base_alignment),
            "target_alignment": probe.encoded_complex_matrix(target_alignment),
            "chamber_profile": {"samples": samples, "crossings": crossings},
        },
        "acceptance_gate": gate,
        "summary": {
            "step_02_actual_residual_l2_norm": float(np.linalg.norm(residual)),
            "step_03_correction_maximum_absolute_coordinate": float(
                np.max(abs(correction))
            ),
            "step_03_linearized_residual_l2_norm": float(np.linalg.norm(prediction)),
            "step_03_crossing_count": len(crossings),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "A215": relative(A215),
            "A215_sha256": sha256(A215),
            "step_02_trial": relative(TRIAL_02),
            "step_02_trial_sha256": sha256(TRIAL_02),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "step_02_same_source_nonlinear_execution": True,
            "step_03_uses_step_02_actual_residual": True,
            "step_03_uses_A213_center_Jacobian": True,
            "step_03_nonlinear_execution_pending": True,
            "interval_zero_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, output)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Complex PGL(3) Refinement 03 (A218) v1

The ultra-accuracy, same-homotopy beta-detour replay at step 02 gives a
selected residual of `{np.linalg.norm(residual):.12g}`.  This replaces the
smaller but numerically unstable production-only estimate.

The actual step-02 residual yields a third complex correction with maximum
coordinate `{np.max(abs(correction)):.6g}`.  Its sampled continuation has
`{len(crossings)}` radial or handle-wall crossings and its linearized residual
is `{np.linalg.norm(prediction):.3e}`.

Step 03 remains a profiled proposal until a full ultra-accuracy nonlinear
execution is recorded.  No interval zero is claimed.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(output["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
