from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb, ctx

import certify_q79_selected_side_base_lift_interval as base_interval
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A375 = VALIDATED / "n3.rank3.base_lift.interval.json"
A374 = VALIDATED / "n3.rank3.handle_combination.interval.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
B_CHECKPOINT = VALIDATED / "n3.handleB.hessian.checkpoint.json"
A401 = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"
OUTPUT = VALIDATED / "n3.beta_minus_B.source.a402s.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourBetaMinusBHandleSource_A402S_v1.md"
ARTIFACT = "A402S"
EXPECTED_HANDLE_COORDINATES = [1, 1, 1, -1, 1, 0, 0, 1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def main() -> int:
    ctx.dps = 100
    base = load(A375)
    handle = load(A374)
    handle_hessian = load(A383)
    b_checkpoint = load(B_CHECKPOINT)
    homotopy = load(A401)

    coordinates = [
        int(value)
        for value in handle["selected_rank3_chain"]["primitive_handle_coordinates"]
    ]
    if coordinates != EXPECTED_HANDLE_COORDINATES:
        raise AssertionError("the selected rank-3 handle coordinates changed")
    if not homotopy["strict_scope"]["A130_B_handle_may_use_A376_lower_contour"]:
        raise AssertionError("A401 does not authorize the lower B contour")
    if (
        handle_hessian["authority"]["B_path_checkpoint"]["sha256"]
        != sha256(B_CHECKPOINT)
    ):
        raise AssertionError("A383 no longer authorizes the B-path checkpoint")
    if str(b_checkpoint["position"]) != "1":
        raise AssertionError("the A383 B-path checkpoint is incomplete")

    beta_lift = [
        validated.interval_from_bounds(value) for value in base["y_chart_base_lift"]
    ]
    b_initial = [
        validated.decoded_acb(value)
        for value in b_checkpoint["configuration"]["initial_periods"]
    ]
    if len(beta_lift) != 5 or len(b_initial) != 5:
        raise AssertionError("the lift and B-handle initial states must have dimension five")
    shifted = [left - right for left, right in zip(beta_lift, b_initial)]
    maximum_radius = max(validated.radius_upper(value) for value in shifted)

    rows = []
    for index, (left, right, value) in enumerate(zip(beta_lift, b_initial, shifted)):
        reconstructed = value + right
        if not reconstructed.overlaps(left):
            raise AssertionError("the shifted source fails its interval reconstruction")
        rows.append(
            {
                "coordinate_zero_based": index,
                "beta_base_lift": base_interval.complex_interval(left),
                "B_handle_base_period": base_interval.complex_interval(right),
                "beta_minus_B_initial_lift": base_interval.complex_interval(value),
                "interval_reconstruction_overlaps_A375": True,
            }
        )
    encoded_shifted = [base_interval.complex_interval(value) for value in shifted]
    serialized_shifted = [
        validated.interval_from_bounds(value) for value in encoded_shifted
    ]
    maximum_serialized_radius = max(
        validated.radius_upper(value) for value in serialized_shifted
    )

    waypoints = homotopy["contour_homotopy"]["selected_lower_waypoints"]
    payload = {
        "schema": "MTTQ79HeightFourBetaMinusBHandleSource.v1",
        "status": "N3_BETA_MINUS_B_HANDLE_INITIAL_LIFT_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "theorem": {
            "name": "Selected lower-contour beta-minus-B linearity theorem",
            "initial_identity": "nu_rel(0) = nu_beta(0) - nu_B(0)",
            "transport_identity": (
                "I_rel(t) = I_beta(t) - I_B(t) for the common A401 contour, "
                "because nu_beta'=A nu_beta+s and nu_B'=A nu_B imply "
                "nu_rel'=A nu_rel+s, while the eight residue rows are linear "
                "in nu_rel"
            ),
            "B_handle_coordinates_in_base_basis": coordinates[4:],
            "common_contour_waypoints": waypoints,
            "common_contour_authorized_by_A401": True,
        },
        "source_rows": rows,
        "y_chart_base_lift": encoded_shifted,
        "summary": {
            "source_dimension": len(shifted),
            "maximum_in_memory_component_ball_radius_upper": maximum_radius,
            "maximum_component_ball_radius_upper": maximum_serialized_radius,
            "all_interval_reconstructions_overlap": True,
            "A401_minimum_critical_value_clearance_lower": homotopy[
                "contour_homotopy"
            ]["minimum_critical_value_clearance_lower"],
        },
        "authority": {
            "A375_rank3_beta_base_lift": authority(A375),
            "A374_selected_handle": authority(A374),
            "A383_handle_Hessian_interval": authority(A383),
            "A383_validated_B_path_checkpoint": authority(B_CHECKPOINT),
            "A401_lower_B_contour_homotopy": authority(A401),
            "validated_transport_engine": authority(Path(validated.__file__).resolve()),
            "full_precision_interval_serializer": authority(
                Path(base_interval.__file__).resolve()
            ),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "selected_B_handle_coordinates_consumed": True,
            "A375_rank3_beta_base_lift_consumed": True,
            "A401_common_contour_homotopy_consumed": True,
            "beta_minus_B_initial_source_interval_closed": True,
            "joint_beta_minus_B_handle_transport_executed": False,
            "full_relative_chain_transport_executed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute the exact n3 13-state affine transport from this source on "
            "the A401 common lower contour"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Beta Minus B-Handle Source (A402S) v1\n\n"
        "A402S forms the rigorous five-coordinate initial lift "
        "`nu_beta(0)-nu_B(0)` from A375 and A383's validated realization of the "
        "preselected B-handle coordinates `[1,0,0,1]`. A401 proves that the "
        "B-handle may use the same lower "
        "contour as beta. Linearity of the residue rows then identifies the "
        "resulting eight transported outputs with `beta-H_B`.\n\n"
        f"The maximum serialized initial component-ball radius is "
        f"`{maximum_serialized_radius:.12g}`. "
        "This certifies the correlated source, not its endpoint transport and "
        "not the full covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
