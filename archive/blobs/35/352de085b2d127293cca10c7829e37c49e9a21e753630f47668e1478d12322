from __future__ import annotations

import json
import sys

from flint import acb

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_node_pair as node_pair
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_tail_reuse_zonotope as reuse


def main() -> int:
    if "--output" in sys.argv:
        raise AssertionError("tail-reuse wrapper requires the default output path")
    index = node_pair.argument_value("--distinguished-index", 4)
    source_path = node_pair.source_path(index)
    source = json.loads(source_path.read_text(encoding="utf-8"))
    stem = f"d{index:03d}_{source['root_id']}"
    tail_path = reuse.PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json"
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
            real = reuse.serialized_center_ball(center["real"], source_radius)
            imaginary = reuse.serialized_center_ball(center["imaginary"], source_radius)
            periods.append(acb(real, imaginary))
            reconstruction_radii.append(
                max(
                    polygonal.validated.upper(real.rad()),
                    polygonal.validated.upper(imaginary.rad()),
                )
            )
        return periods, {
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

    selector, node_file = node_pair.certified_node_pair_selector(index)
    polygonal.handle.direct_cut_periods = certified_cut_periods
    polygonal.pilot.closest_pair = selector
    polygonal.__file__ = __file__
    result = polygonal.main()

    output = reuse.PERIOD_DIRECTORY / f"{stem}.E32_main.interval.packet.json"
    packet = json.loads(output.read_text(encoding="utf-8"))
    packet["authority"]["certified_node_pair_source"] = reuse.relative(node_file)
    packet["authority"]["certified_node_pair_source_sha256"] = node_pair.sha256(node_file)
    packet["authority"]["certified_tail_cutoff_period_source"] = reuse.relative(tail_path)
    packet["authority"]["certified_tail_cutoff_period_source_sha256"] = node_pair.sha256(tail_path)
    packet["scope"]["certified_nodal_pair_selector_consumed"] = True
    packet["scope"]["certified_tail_cutoff_period_reuse_consumed"] = True
    packet["scope"]["compressed_augmented_frame_consumed"] = True
    packet["validated_main_transport"]["certificate_method"] = (
        "six-dimensional compressed augmented frame on a certified polygonal "
        "homotopy with certified tail cutoff-period reuse"
    )
    polygonal.dump(output, packet)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
