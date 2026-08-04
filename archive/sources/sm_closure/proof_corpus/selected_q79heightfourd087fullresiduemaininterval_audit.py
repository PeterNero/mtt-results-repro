from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
NODE = DIRECTORY / "d087_selected_085.n3.node.interval.packet.json"
MAIN = DIRECTORY / "d087.n3.main8.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueMainInterval_A220_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_authority(rows: dict[str, dict]) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A220 authority {name}: {path}")
        require(
            sha256(path) == row["sha256"],
            f"stale A220 authority {name}: {path}",
        )


def main() -> int:
    require(NODE.exists(), "missing A220 target-node packet")
    require(MAIN.exists(), "missing A220 all-row main packet")
    require(NOTE.exists(), "missing A220 proof note")
    node = load(NODE)
    packet = load(MAIN)
    require(
        node["schema"] == "MTTQ79HeightFourD087TargetNodeInterval.v1",
        "A220 node schema changed",
    )
    require(
        packet["schema"]
        == "MTTQ79HeightFourD087FullResidueMainInterval.v1",
        "A220 main schema changed",
    )
    require(
        packet["status"]
        == "D087_N3_NODE_AND_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED_TAIL_OPEN",
        "A220 status changed",
    )
    verify_authority(node["authority"])
    verify_authority(packet["authority"])

    certified = packet["certified_node"]
    node_diagnostics = certified["node_diagnostics"]
    factor = certified["factor_diagnostics"]
    require(
        float(certified["parameter_radius_upper"]) < 1.0e-50,
        "A220 node-parameter box is too wide",
    )
    require(
        float(certified["double_root_radius_upper"]) < 1.0e-50,
        "A220 double-root box is too wide",
    )
    require(
        float(node_diagnostics["jacobian_determinant_absolute_lower"]) > 0.0,
        "A220 node Jacobian is not separated from zero",
    )
    require(
        float(factor["quartic_at_double_root_absolute_lower"]) > 0.0,
        "A220 node is not a simple quadratic-times-quartic factor",
    )
    require(
        float(factor["hensel_jacobian_determinant_absolute_lower"]) > 0.0,
        "A220 Hensel factor Jacobian is not invertible",
    )
    require(
        all(
            row["parameter_interior_inclusion"]
            and row["root_interior_inclusion"]
            for row in node_diagnostics["iterations"]
        ),
        "A220 interval Newton inclusion changed",
    )

    execution = packet["validated_main_transport"]
    radii = [float(value) for value in execution["residue_coordinate_radius_uppers"]]
    require(len(radii) == 8, "A220 does not carry eight residue-row radii")
    require(
        all(math.isfinite(value) and value > 0.0 for value in radii),
        "A220 carries a nonfinite residue-row radius",
    )
    require(max(radii) < 1.0e-3, "A220 main enclosure regressed above 1e-3")
    require(
        abs(max(radii) - float(execution["uniform_integral_radius_upper"]))
        < 1.0e-15,
        "A220 uniform radius is not the row maximum",
    )
    require(
        int(execution["accepted_step_count"]) > 0,
        "A220 has no accepted validated steps",
    )
    final_step = execution["steps"][-1]
    require(
        abs(float(final_step["end_arclength"]) - float(execution["path_length"]))
        < 1.0e-12,
        "A220 validated path did not reach the base",
    )
    require(
        float(execution["period_center_dispersion_across_frames"]) < 1.0e-30,
        "A220 correlated frames disagree on the five-period center",
    )
    require(
        len(packet["all_eight_main_residue_rows"]["interval_centers"]) == 8,
        "A220 does not emit eight main-row centers",
    )

    orientation = packet["orientation"]
    require(int(orientation["selected_sign"]) == -1, "A220 orientation changed")
    require(
        float(orientation["selected_base_center_maximum_difference"]) < 1.0e-8,
        "A220 selected orientation no longer matches the n3 cache",
    )
    require(
        float(orientation["opposite_base_center_maximum_difference"]) > 1.0,
        "A220 opposite orientation is not separated",
    )
    scope = packet["strict_scope"]
    require(scope["target_node_interval_Newton_closed"], "A220 node scope reopened")
    require(
        scope["all_eight_main_residue_rows_interval_closed"],
        "A220 all-row main scope reopened",
    )
    require(
        not scope["node_to_cutoff_tail_interval_closed"],
        "A220 incorrectly claims the local tail",
    )
    require(
        not scope["full_d087_period_vector_interval_closed"],
        "A220 incorrectly claims the full d087 vector",
    )
    require(not scope["covariant_zero_proved"], "A220 overclaims the zero")

    print("q79 A220 d087 full-residue main interval audit: PASS")
    print(
        "closed: n3 node and eight correlated main rows; "
        f"maximum radius={max(radii):.6e}"
    )
    print("open: all-eight local tail, full d087 splice, and interval Newton zero")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
