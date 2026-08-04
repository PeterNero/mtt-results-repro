from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import explore_q79_height4_covariant_floating_probe as probe


SLUG = "selected_q79heightfourcomplexpgl3floatingboundary"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def close(left: float, right: float, tolerance: float = 1.0e-13) -> bool:
    return abs(float(left) - float(right)) <= tolerance


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    note_path = ROOT / candidate["note"]
    packet = load(packet_path)
    if candidate["artifact"] != "A219":
        raise AssertionError("A219 artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A219 overclaims closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A219 packet hash mismatch")
    if sha256(note_path) != candidate["note_sha256"]:
        raise AssertionError("A219 note hash mismatch")
    if sha256(Path(__file__)) != candidate["audit_sha256"]:
        raise AssertionError("A219 audit hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A219 candidate hash mismatch")

    authority = packet["authority"]
    for name, row in authority.items():
        path = ROOT / row["path"]
        if sha256(path) != row["sha256"]:
            raise AssertionError(f"A219 authority hash mismatch: {name}")
    a215 = load(ROOT / authority["A215"]["path"])
    a216 = load(ROOT / authority["A216"]["path"])
    n1 = load(ROOT / authority["n1"]["path"])
    n2 = load(ROOT / authority["n2_ultra_detour"]["path"])
    ultra = load(ROOT / authority["n3_ultra_detour"]["path"])
    extreme = load(ROOT / authority["n3_extreme_detour"]["path"])

    jacobian = complex_matrix(a215["complex_Jacobian"])
    if np.linalg.matrix_rank(jacobian) != 8:
        raise AssertionError("A219 complex Jacobian lost rank")
    realified = np.block(
        [[jacobian.real, -jacobian.imag], [jacobian.imag, jacobian.real]]
    )
    if np.linalg.matrix_rank(realified) != 16:
        raise AssertionError("A219 realified Jacobian lost rank")
    center = probe.complex_vector(a215["center_residual"])
    first_step = probe.complex_vector(a215["complex_Newton_step"])
    if np.linalg.norm(center + jacobian @ first_step) > 1.0e-14:
        raise AssertionError("A219 first complex Newton solve does not replay")
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (first_step[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    replay_alignment = complex_matrix(a215["base_alignment"]) @ expm(tangent)
    if np.max(abs(replay_alignment - complex_matrix(n1["alignment"]))) > 1.0e-14:
        raise AssertionError("A219 first nonlinear alignment does not replay")
    if a215["summary"]["crossing_count"] != 0:
        raise AssertionError("A219 first complex segment crosses a wall")

    if not all(a216["acceptance_gate"].values()):
        raise AssertionError("A219 imaginary-direction check is not accepted")
    plus_path = ROOT / a216["authority"]["positive_imaginary_probe"]
    minus_path = ROOT / a216["authority"]["negative_imaginary_probe"]
    plus = selected(load(plus_path))
    minus = selected(load(minus_path))
    measured = (
        probe.complex_vector(plus["PL_corrected_residual"])
        - probe.complex_vector(minus["PL_corrected_residual"])
    ) / (2.0 * float(a216["finite_difference_step"]))
    predicted = probe.complex_vector(
        a216["holomorphic_prediction_i_times_real_derivative"]
    )
    relative_error = float(np.linalg.norm(measured - predicted) / np.linalg.norm(measured))
    if not close(
        relative_error,
        a216["relative_holomorphic_derivative_error"],
        1.0e-12,
    ):
        raise AssertionError("A219 imaginary derivative replay mismatch")
    if relative_error > 5.0e-4:
        raise AssertionError("A219 imaginary derivative check degraded")

    residuals = {
        "A212_center": center,
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
    for stored, (name, residual) in zip(
        packet["Newton_history"], residuals.items()
    ):
        if stored["stage"] != name or not close(
            stored["residual_l2_norm"], np.linalg.norm(residual), 1.0e-15
        ):
            raise AssertionError("A219 Newton history mismatch")
    first_four = list(residuals.values())[:4]
    if not all(
        np.linalg.norm(first_four[index + 1]) < np.linalg.norm(first_four[index])
        for index in range(3)
    ):
        raise AssertionError("A219 Newton residuals are not monotone")

    ultra_residual = residuals["complex_Newton_03_ultra"]
    extreme_residual = residuals["complex_Newton_03_extreme"]
    difference = extreme_residual - ultra_residual
    midpoint = (ultra_residual + extreme_residual) / 2.0
    empirical_radius = np.linalg.norm(difference) / 2.0
    comparison = packet["n3_profile_comparison"]
    if not close(
        comparison["residual_difference_l2_norm"], np.linalg.norm(difference), 1.0e-15
    ):
        raise AssertionError("A219 profile-difference norm mismatch")
    if not close(comparison["empirical_l2_radius"], empirical_radius, 1.0e-15):
        raise AssertionError("A219 empirical radius mismatch")
    if np.linalg.norm(midpoint) > empirical_radius:
        raise AssertionError("A219 empirical profile ball no longer contains zero")
    if not comparison["not_an_interval_ball"]:
        raise AssertionError("A219 promotes an empirical ball to interval authority")

    ultra_period = probe.complex_vector(
        selected(ultra)["PL_corrected_moving_period"]
    )
    extreme_period = probe.complex_vector(
        selected(extreme)["PL_corrected_moving_period"]
    )
    ultra_beta = ultra_residual + ultra_period
    extreme_beta = extreme_residual + extreme_period
    decomposition = packet["difference_decomposition"]
    if not close(
        decomposition["selected_period_difference_l2_norm"],
        np.linalg.norm(extreme_period - ultra_period),
        1.0e-15,
    ):
        raise AssertionError("A219 period decomposition mismatch")
    if not close(
        decomposition["anchored_beta_difference_l2_norm"],
        np.linalg.norm(extreme_beta - ultra_beta),
        1.0e-15,
    ):
        raise AssertionError("A219 beta decomposition mismatch")

    candidate_queue = load(probe.A208)["height_four_candidates"][1:]
    source_candidate = next(
        row for row in candidate_queue if int(row["A132_objective_rank"]) == 3
    )
    signs = np.asarray(load(probe.ORIENTATION)["column_signs"], dtype=np.int64)
    contribution_rows = []
    for chain_row in source_candidate["primitive_thimble_chain"]:
        index = int(chain_row["distinguished_index"])
        coefficient = int(chain_row["coefficient"]) * int(signs[index - 1])
        ultra_thimble = load(
            (ROOT / authority["n3_ultra_detour"]["path"]).parent
            / "thimbles"
            / f"t{index:03d}.json"
        )
        extreme_thimble = load(
            (ROOT / authority["n3_extreme_detour"]["path"]).parent
            / "thimbles"
            / f"t{index:03d}.json"
        )
        value = coefficient * (
            probe.complex_vector(extreme_thimble["period_values"])
            - probe.complex_vector(ultra_thimble["period_values"])
        )
        contribution_rows.append((np.linalg.norm(value), index))
    contribution_rows.sort(reverse=True)
    if contribution_rows[0][1] != 87:
        raise AssertionError("A219 dominant unstable thimble changed")
    stored_dominant = decomposition["dominant_thimble"]
    if stored_dominant["distinguished_index"] != 87 or not close(
        stored_dominant["contribution_difference_l2_norm"],
        contribution_rows[0][0],
        1.0e-15,
    ):
        raise AssertionError("A219 dominant-thimble replay mismatch")

    scope = packet["strict_scope"]
    if (
        scope["covariant_zero_proved"]
        or scope["selected_alignment_exists_proved"]
        or scope["full_SM_closure_proved"]
    ):
        raise AssertionError("A219 strict scope overclaims closure")
    if not scope["empirical_ball_is_not_interval_certificate"]:
        raise AssertionError("A219 interval disclaimer disappeared")

    print("q79 A219 complex PGL3 floating-boundary audit: PASS")
    print(
        "nonlinear residual: "
        f"{np.linalg.norm(center):.6e} -> {np.linalg.norm(ultra_residual):.6e}"
    )
    print(
        "floating boundary: interprofile difference "
        f"{np.linalg.norm(difference):.6e}; dominant d087 "
        f"{contribution_rows[0][0]:.6e}"
    )
    print("open: validated d087 period transport and an interval Newton zero")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
