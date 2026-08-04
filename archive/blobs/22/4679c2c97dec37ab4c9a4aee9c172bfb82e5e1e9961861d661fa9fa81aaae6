from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_left_upper_0p05_homotopy.a390h.interval.json"
)
NAMES = {
    "reduction_determinant",
    "y_chart_scale",
    "q_leading_coefficient",
    "q_discriminant",
    "g_on_q_norm",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    packet = load(PACKET)
    require(packet["artifact"] == "A390H", "A390H artifact changed")
    require(
        packet["schema"] == "MTTQ79LeftUpperContourHomotopyIntervalCertificate.v1",
        "A390H schema changed",
    )
    require(
        packet["status"] == "LEFT_UPPER_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED",
        "A390H homotopy is not certified",
    )
    require(packet["domain"]["real_interval"] == ["0", "0.65000000000000002"], "real domain changed")
    require(packet["domain"]["imaginary_interval"] == ["0", "0.050000000000000003"], "imaginary domain changed")
    corners = [complex_value(value) for value in packet["domain"]["corners"]]
    require(
        corners == [0 + 0j, 0.05j, 0.65 + 0.05j, 0.65 + 0j, 0 + 0j],
        "A390H boundary changed",
    )

    cover = packet["boundary_cover"]
    leaves = cover["leaves"]
    require(len(leaves) == int(cover["leaf_count"]), "leaf count changed")
    require(len(leaves) > 0, "A390H has no boundary leaves")
    gate = float(cover["relative_radius_gate"])
    require(complex_value(leaves[0]["start"]) == corners[0], "boundary start changed")
    previous = corners[0]
    minimum_lowers = {name: math.inf for name in NAMES}
    for leaf in leaves:
        start = complex_value(leaf["start"])
        end = complex_value(leaf["end"])
        require(abs(start - previous) < 3.0e-15, "A390H boundary cover has a gap")
        require(end != start, "A390H has a zero-length leaf")
        require(set(leaf["absolute_lower_bounds"]) == NAMES, "obstruction rows changed")
        require(set(leaf["relative_radius_upper_bounds"]) == NAMES, "radius rows changed")
        for name in NAMES:
            lower = float(leaf["absolute_lower_bounds"][name])
            radius = float(leaf["relative_radius_upper_bounds"][name])
            require(math.isfinite(lower) and lower > 0.0, f"{name} touches zero")
            require(math.isfinite(radius) and 0.0 <= radius < gate, f"{name} lost sector separation")
            minimum_lowers[name] = min(minimum_lowers[name], lower)
        previous = end
    require(abs(previous - corners[-1]) < 3.0e-15, "boundary does not close")
    for name in NAMES:
        require(
            math.isclose(
                float(cover["minimum_absolute_lower_bounds"][name]),
                minimum_lowers[name],
                rel_tol=2.0e-15,
                abs_tol=1.0e-300,
            ),
            f"{name} minimum lower bound does not replay",
        )

    windings = packet["argument_principle"]
    require(set(windings) == NAMES, "A390H winding rows changed")
    for name in ("reduction_determinant", "y_chart_scale", "q_leading_coefficient", "g_on_q_norm"):
        require(int(windings[name]["winding_number"]) == 0, f"{name} has an interior zero")
    q_winding = int(windings["q_discriminant"]["winding_number"])
    require(q_winding <= 0, "q-discriminant winding orientation changed")
    divisor = packet["finite_flat_divisor_theorem"]
    require(divisor["applies"] is True, "finite-flat theorem lost")
    require(
        int(divisor["q_discriminant_zero_count_with_multiplicity"]) == -q_winding,
        "q collision count does not replay",
    )
    require(divisor["symmetric_divisor_and_quotient_trace_extend"] is True, "divisor extension lost")

    decision = packet["decision"]
    for key in (
        "smooth_genus_two_family_on_closed_upper_left_rectangle",
        "finite_flat_symmetric_divisor_preserved",
        "A379_to_left_upper_route_homotopy_certified",
        "normal_function_endpoint_branch_preserved",
        "selected_domain_parameters_used",
    ):
        require(decision[key] is True, f"A390H decision lost {key}")
    for label, record in packet["authority"].items():
        path = ROOT / record["path"]
        require(path.exists(), f"A390H authority path absent: {label}")
        require(sha256(path) == record["sha256"], f"A390H authority stale: {label}")
    execution = packet["execution"]
    checkpoint_path = ROOT / execution["checkpoint"]
    require(checkpoint_path.exists(), "A390H checkpoint is absent")
    require(
        sha256(checkpoint_path) == execution["checkpoint_sha256"],
        "A390H checkpoint authority changed",
    )
    checkpoint = load(checkpoint_path)
    require(
        checkpoint["schema"] == "MTTQ79LeftUpperContourHomotopyCheckpoint.v1",
        "A390H checkpoint schema changed",
    )
    require(
        checkpoint["configuration"] == execution["configuration"],
        "A390H checkpoint configuration changed",
    )
    require(
        int(checkpoint["completed_chunk_count"])
        == int(execution["completed_chunk_count"])
        == 4 * int(cover["initial_subdivisions_per_side"]),
        "A390H checkpoint is incomplete",
    )

    scope = packet["strict_scope"]
    require(scope["closed_rectangle_argument_principle_executed"] is True, "argument principle gate lost")
    require(scope["A379_route_replacement_homotopy_interval_certified"] is True, "route homotopy gate lost")
    for key in (
        "candidate_route_beta_Hessian_transport_executed",
        "candidate_route_tighter_than_A379_certified",
        "observed_SM_values_used",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A390H overclaims {key}")
    print(
        "PASS: A390H certifies the A379 left-segment replacement through the "
        "upper rectangle; beta/Hessian transport remains unexecuted"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
