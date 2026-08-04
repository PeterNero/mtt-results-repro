from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from flint import acb, arb

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_node_pair as node_pair
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_node_pair_zonotope as zonotope


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def serialized_center_ball(value: str, source_radius: float) -> arb:
    center = float(value)
    # complex_pair serializes an IEEE-754 binary64 midpoint with 17 digits.
    # Two ulps cover the Arb-to-binary64 conversion and decimal round trip.
    serialization_radius = 2.0 * math.ulp(center)
    radius = source_radius + serialization_radius
    return arb(format(center, ".17g"), format(radius, ".17g"))


def main() -> int:
    if "--output" in sys.argv:
        raise AssertionError("tail-reuse wrapper requires the default output path")
    index = node_pair.argument_value("--distinguished-index", 4)
    source = json.loads(node_pair.source_path(index).read_text(encoding="utf-8"))
    stem = f"d{index:03d}_{source['root_id']}"
    tail_path = PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json"
    if not tail_path.exists():
        raise FileNotFoundError(f"missing certified tail packet {tail_path}")
    tail = json.loads(tail_path.read_text(encoding="utf-8"))
    reference = tail["cutoff_direct_period_reference"]
    expected_pair = tuple(int(item) for item in reference["pair_zero_based"])
    source_radius = float(reference["maximum_component_radius"])
    if len(reference["period_centers"]) != 5:
        raise AssertionError("tail packet does not contain five cutoff period centers")
    if not tail["scope"]["endpoint_tail_interval_closed"]:
        raise AssertionError("tail packet is not certified")
    if int(tail["selected_thimble"]["distinguished_index"]) != index:
        raise AssertionError("tail packet distinguished index mismatch")
    if tail["selected_thimble"]["root_id"] != source["root_id"]:
        raise AssertionError("tail packet root mismatch")

    reconstruction_radii: list[float] = []

    def certified_cut_periods(
        _roots,
        _leading,
        pair,
        *,
        segments: int,
        tolerance: float,
    ):
        del _roots, _leading, segments, tolerance
        if tuple(int(item) for item in pair) != expected_pair:
            raise AssertionError("main transport selected a different nodal pair")
        periods = []
        reconstruction_radii.clear()
        for center in reference["period_centers"]:
            real = serialized_center_ball(center["real"], source_radius)
            imaginary = serialized_center_ball(center["imaginary"], source_radius)
            periods.append(acb(real, imaginary))
            reconstruction_radii.append(
                max(polygonal.validated.upper(real.rad()), polygonal.validated.upper(imaginary.rad()))
            )
        diagnostics = {
            "pair_zero_based": list(expected_pair),
            "theta_segments": int(reference["theta_segments"]),
            "integral_count": int(reference["integral_count"]),
            "minimum_half_plane_margin": float(reference["minimum_half_plane_margin"]),
            "minimum_sign_margin": float(reference["minimum_sign_margin"]),
            "period_centers": reference["period_centers"],
            "maximum_component_radius": max(reconstruction_radii),
            "certified_tail_cutoff_period_reuse": True,
            "source_maximum_component_radius": source_radius,
            "serialization_inflation_rule": "source radius plus two binary64 ulps per real coordinate",
        }
        print(
            "reused certified cutoff periods "
            f"index={index} radius={max(reconstruction_radii):.3e}",
            flush=True,
        )
        return periods, diagnostics

    selector, node_file = node_pair.certified_node_pair_selector(index)
    polygonal.handle.direct_cut_periods = certified_cut_periods
    polygonal.pilot.closest_pair = selector
    polygonal.pilot.E32LiftErrorFrame = zonotope.PhysicalGeneratorFrame
    polygonal.pilot.validated_e32_flow_step = zonotope.validated_e32_zonotope_flow_step
    polygonal.__file__ = __file__
    print(f"starting certified zonotope transport index={index}", flush=True)
    result = polygonal.main()

    output = PERIOD_DIRECTORY / f"{stem}.E32_main.interval.packet.json"
    packet = json.loads(output.read_text(encoding="utf-8"))
    packet["authority"]["certified_node_pair_source"] = relative(node_file)
    packet["authority"]["certified_node_pair_source_sha256"] = node_pair.sha256(node_file)
    packet["authority"]["certified_tail_cutoff_period_source"] = relative(tail_path)
    packet["authority"]["certified_tail_cutoff_period_source_sha256"] = node_pair.sha256(tail_path)
    packet["scope"]["certified_nodal_pair_selector_consumed"] = True
    packet["scope"]["certified_tail_cutoff_period_reuse_consumed"] = True
    packet["scope"]["uncompressed_physical_generator_zonotope_consumed"] = True
    packet["validated_main_transport"]["certificate_method"] = (
        "six-dimensional augmented uncompressed physical-generator zonotope "
        "on a certified polygonal homotopy with certified tail cutoff-period reuse"
    )
    polygonal.dump(output, packet)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
