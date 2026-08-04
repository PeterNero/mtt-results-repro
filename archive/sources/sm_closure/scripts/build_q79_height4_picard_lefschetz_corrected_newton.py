from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
DIRECTORY = probe.PROBE_DIRECTORY
JACOBIAN = DIRECTORY / "height4_covariant_floating_jacobian.packet.json"
WALL = DIRECTORY / "rank3_selected_039_selected_038_radial_wall.packet.json"
FACTORIZATION = probe.FACTORIZATION
HOMOLOGY = probe.HOMOLOGY
A208 = probe.A208
ORIENTATION = probe.ORIENTATION
OUTPUT = DIRECTORY / "height4_picard_lefschetz_corrected_newton.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourPicardLefschetzCorrectedNewton_A212_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def diagnostic_path(scale_tag: str, index: int) -> Path:
    return (
        DIRECTORY
        / f"pcdiag_r3_s{scale_tag}_d{index:03d}_n016"
        / "diagnostic.packet.json"
    )


def vector(rows: list[dict[str, str]]) -> np.ndarray:
    return probe.complex_vector(rows)


def encoded(vector_value: np.ndarray) -> list[dict[str, str]]:
    return probe.encoded_complex_vector(vector_value)


def main() -> int:
    factorization = load(FACTORIZATION)
    factors = {
        int(row["distinguished_index"]): row for row in factorization["factors"]
    }
    v64 = np.asarray(
        factors[64]["positive_vanishing_cycle_up_to_sign"], dtype=np.int64
    )
    v65 = np.asarray(
        factors[65]["positive_vanishing_cycle_up_to_sign"], dtype=np.int64
    )
    homology = load(HOMOLOGY)["homology_convention"]
    intersection_matrix = np.asarray(
        homology["intersection_matrix"], dtype=np.int64
    )
    intersection = int(v64 @ intersection_matrix @ v65)
    if intersection != 1:
        raise AssertionError("selected_039/selected_038 intersection is not +1")
    action_formula = homology["positive_generator_formula"]
    if action_formula != "T_v=I-v*v^T*J":
        raise AssertionError("Picard-Lefschetz action convention changed")

    jump_checks = []
    before64 = vector(
        load(diagnostic_path("5d000em01", 64))["execution"]["period_values"]
    )
    for scale_tag, scale in (("5d500em01", 0.55), ("7d500em01", 0.75)):
        path64 = diagnostic_path(scale_tag, 64)
        path65 = diagnostic_path(scale_tag, 65)
        raw64 = vector(load(path64)["execution"]["period_values"])
        period65 = vector(load(path65)["execution"]["period_values"])
        integer_tests = []
        for coefficient in range(-4, 5):
            residual = raw64 + coefficient * period65 - before64
            integer_tests.append(
                {
                    "coefficient": coefficient,
                    "continuation_drift_l2_norm": float(np.linalg.norm(residual)),
                    "continuation_drift_maximum_absolute_value": float(
                        np.max(abs(residual))
                    ),
                }
            )
        ordered = sorted(
            integer_tests, key=lambda row: row["continuation_drift_l2_norm"]
        )
        if ordered[0]["coefficient"] != intersection:
            raise AssertionError("computed jump does not select the PL intersection")
        jump_checks.append(
            {
                "scale": scale,
                "target_diagnostic": relative(path64),
                "target_diagnostic_sha256": sha256(path64),
                "crossing_diagnostic": relative(path65),
                "crossing_diagnostic_sha256": sha256(path65),
                "integer_coefficient_tests": integer_tests,
                "selected_coefficient": ordered[0]["coefficient"],
                "selected_drift_l2_norm": ordered[0][
                    "continuation_drift_l2_norm"
                ],
                "next_best_drift_l2_norm": ordered[1][
                    "continuation_drift_l2_norm"
                ],
                "selection_separation_factor": ordered[1][
                    "continuation_drift_l2_norm"
                ]
                / ordered[0]["continuation_drift_l2_norm"],
            }
        )

    a208 = load(A208)
    candidates = {
        row["candidate_id"]: row for row in a208["height_four_candidates"][1:]
    }
    orientation = load(ORIENTATION)
    column_sign64 = int(orientation["column_signs"][63])
    column_sign65 = int(orientation["column_signs"][64])
    if column_sign64 != column_sign65:
        raise AssertionError("selected_039/selected_038 synchronized signs differ")
    corrected_trials = []
    for run, scale in (("tr3_s7d500em01", 0.75), ("tr3_s1d000ep00", 1.0)):
        trial_path = DIRECTORY / run / "trial.packet.json"
        trial = load(trial_path)
        period65_path = DIRECTORY / run / "thimbles" / "t065.json"
        period65 = vector(load(period65_path)["period_values"])
        rows = []
        for raw_row in trial["candidate_trials"]:
            candidate = candidates[raw_row["candidate_id"]]
            coefficients = {
                int(row["distinguished_index"]): int(row["coefficient"])
                for row in candidate["primitive_thimble_chain"]
            }
            coefficient64 = coefficients.get(64, 0)
            period_correction = (
                coefficient64 * column_sign64 * intersection * period65
            )
            raw_residual = vector(raw_row["actual_residual"])
            corrected_residual = raw_residual - period_correction
            linearized = vector(raw_row["linearized_residual"])
            rows.append(
                {
                    "candidate_id": raw_row["candidate_id"],
                    "A132_objective_rank": raw_row["A132_objective_rank"],
                    "primitive_d064_coefficient": coefficient64,
                    "synchronized_d064_sign": column_sign64,
                    "period_correction": encoded(period_correction),
                    "raw_residual_l2_norm": float(np.linalg.norm(raw_residual)),
                    "PL_corrected_residual": encoded(corrected_residual),
                    "PL_corrected_residual_l2_norm": float(
                        np.linalg.norm(corrected_residual)
                    ),
                    "PL_corrected_residual_maximum_absolute_value": float(
                        np.max(abs(corrected_residual))
                    ),
                    "linearized_residual_l2_norm": float(np.linalg.norm(linearized)),
                    "PL_corrected_to_linearized_error_l2_norm": float(
                        np.linalg.norm(corrected_residual - linearized)
                    ),
                }
            )
        corrected_trials.append(
            {
                "scale": scale,
                "raw_trial": relative(trial_path),
                "raw_trial_sha256": sha256(trial_path),
                "crossing_period": relative(period65_path),
                "crossing_period_sha256": sha256(period65_path),
                "candidate_rows": rows,
            }
        )
    full_rank3 = next(
        row
        for row in corrected_trials[-1]["candidate_rows"]
        if int(row["A132_objective_rank"]) == 3
    )
    jacobian_rank3 = next(
        row
        for row in load(JACOBIAN)["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 3
    )
    packet = {
        "schema": "MTTQ79HeightFourPicardLefschetzCorrectedNewton.v1",
        "status": "RADIAL_WALL_JUMP_IDENTIFIED_AND_NEWTON_TRIAL_CORRECTED",
        "wall": {
            "target_distinguished_index": 64,
            "target_root_id": "selected_039",
            "crossing_distinguished_index": 65,
            "crossing_root_id": "selected_038",
            "wall_location": relative(WALL),
            "wall_location_sha256": sha256(WALL),
            "oriented_crossing": "positive_to_negative",
        },
        "selected_homology": {
            "intersection_matrix": intersection_matrix.tolist(),
            "target_vanishing_cycle": v64.tolist(),
            "crossing_vanishing_cycle": v65.tolist(),
            "target_crossing_intersection": intersection,
            "action_formula": action_formula,
            "factorization_action_convention": factorization["action_convention"],
            "synchronized_target_column_sign": column_sign64,
            "synchronized_crossing_column_sign": column_sign65,
        },
        "continuation_rule": {
            "formula": "P_64_continued = P_64_raw + <v_64,v_65> P_65",
            "selected_integer_coefficient": intersection,
            "jump_checks": jump_checks,
        },
        "corrected_trials": corrected_trials,
        "summary": {
            "wall_scale_midpoint": load(WALL)["summary"]["wall_scale_midpoint"],
            "wall_scale_bracket_width": load(WALL)["summary"][
                "wall_scale_bracket_width"
            ],
            "selected_jump_coefficient": intersection,
            "minimum_integer_selection_separation_factor": min(
                row["selection_separation_factor"] for row in jump_checks
            ),
            "rank3_center_residual_l2_norm": jacobian_rank3[
                "center_residual_l2_norm"
            ],
            "rank3_full_step_raw_residual_l2_norm": full_rank3[
                "raw_residual_l2_norm"
            ],
            "rank3_full_step_PL_corrected_residual_l2_norm": full_rank3[
                "PL_corrected_residual_l2_norm"
            ],
            "rank3_full_step_linearized_residual_l2_norm": full_rank3[
                "linearized_residual_l2_norm"
            ],
            "rank3_full_step_PL_to_linearized_error_l2_norm": full_rank3[
                "PL_corrected_to_linearized_error_l2_norm"
            ],
            "rank3_full_step_reduction_factor_from_center": full_rank3[
                "PL_corrected_residual_l2_norm"
            ]
            / jacobian_rank3["center_residual_l2_norm"],
        },
        "authority": {
            "factorization": relative(FACTORIZATION),
            "factorization_sha256": sha256(FACTORIZATION),
            "homology": relative(HOMOLOGY),
            "homology_sha256": sha256(HOMOLOGY),
            "A208": relative(A208),
            "A208_sha256": sha256(A208),
            "orientation": relative(ORIENTATION),
            "orientation_sha256": sha256(ORIENTATION),
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "selected_integral_PL_intersection_used": True,
            "same_source_floating_periods_used": True,
            "integer_jump_uniquely_selected_in_test_window": True,
            "floating_wall_location_only": True,
            "interval_wall_and_jump_certificate": False,
            "covariant_zero_found": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
        "next_required_artifact": (
            "recenter at the full-step PL-corrected alignment, construct the next "
            "same-source Jacobian or secant model, and include global-handle PL "
            "updates when a selected critical value crosses A or B"
        ),
    }
    dump(OUTPUT, packet)
    NOTE.write_text(
        f"""# MTT q79 Height-Four Picard-Lefschetz-Corrected Newton (A212) v1

The selected rank-3 Newton path crosses the `selected_039` radial carrier with
`selected_038` at scale `{packet['summary']['wall_scale_midpoint']:.12f}`.  The
floating wall bracket has width
`{packet['summary']['wall_scale_bracket_width']:.3e}`.

The selected vanishing cycles are `v64={v64.tolist()}` and
`v65={v65.tolist()}`.  With the selected intersection matrix and convention
`T_v=I-v*v^T*J`, their intersection is exactly `{intersection}`.  The continued
period is therefore

`P64_continued = P64_raw + P65`.

The period data select this integer coefficient independently at scales 0.55
and 0.75.  The weaker of the two best-versus-next-best separation factors is
`{packet['summary']['minimum_integer_selection_separation_factor']:.3e}`.

After applying the jump to the complete candidate chain, the full rank-3 step
has residual L2 norm
`{packet['summary']['rank3_full_step_PL_corrected_residual_l2_norm']:.12g}`
instead of the raw discontinuous value
`{packet['summary']['rank3_full_step_raw_residual_l2_norm']:.12g}`.  The
Jacobian predicted
`{packet['summary']['rank3_full_step_linearized_residual_l2_norm']:.12g}`.

This establishes the floating chamber-aware continuation rule and rescues the
full Newton step.  It is not yet an interval wall/jump certificate and it does
not prove a covariant zero.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
