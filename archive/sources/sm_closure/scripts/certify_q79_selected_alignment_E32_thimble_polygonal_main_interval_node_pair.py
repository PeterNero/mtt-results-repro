from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)


def argument_value(name: str, default: int) -> int:
    if name not in sys.argv:
        return default
    position = sys.argv.index(name)
    return int(sys.argv[position + 1])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nodal_path(index: int) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.nodal_factor.interval.packet.json"))
    if len(rows) != 1:
        raise AssertionError(f"expected one nodal packet for d{index:03d}")
    return rows[0]


def source_path(index: int) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.thimble_period.candidate.json"))
    if len(rows) != 1:
        raise AssertionError(f"expected one source candidate for d{index:03d}")
    return rows[0]


def certified_node_pair_selector(index: int):
    node_file = nodal_path(index)
    node_packet = json.loads(node_file.read_text(encoding="utf-8"))
    if not node_packet["scope"]["node_F_equals_F_t_interval_newton_closed"]:
        raise AssertionError("nodal source is not interval-Newton certified")
    if not node_packet["scope"]["analytic_Hensel_factor_germ_closed"]:
        raise AssertionError("nodal source misses the Hensel factor")
    encoded_node = node_packet["certified_node"]["double_root_ball"]

    def select(roots: list[acb]):
        node = acb(encoded_node["real"], encoded_node["imaginary"])
        distances = sorted(
            (
                polygonal.validated.upper(abs(root - node)),
                polygonal.validated.lower(abs(root - node)),
                root_index,
            )
            for root_index, root in enumerate(roots)
        )
        if distances[1][0] >= distances[2][1]:
            raise AssertionError(
                "two roots nearest the certified double root are not interval-separated"
            )
        pair = tuple(sorted((distances[0][2], distances[1][2])))
        pair_distance = abs(roots[pair[0]] - roots[pair[1]])
        other_pair_distances = [
            abs(roots[left] - roots[right])
            for left in range(len(roots))
            for right in range(left)
            if {left, right} != set(pair)
        ]
        minimum_root_ball_separation = min(
            polygonal.validated.lower(abs(roots[left] - roots[right]))
            for left in range(len(roots))
            for right in range(left)
        )
        if minimum_root_ball_separation <= 0:
            raise AssertionError("near-node root balls overlap")
        return pair, {
            "pair_selection_method": "two cutoff roots nearest the independently certified nodal double-root ball",
            "instantaneous_closest_pair_rule_used": False,
            "certified_node_packet": str(node_file.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "certified_node_packet_sha256": sha256(node_file),
            "selected_pair_distance_lower": polygonal.validated.lower(
                pair_distance
            ),
            "selected_pair_distance_upper": polygonal.validated.upper(
                pair_distance
            ),
            "second_pair_distance_lower": min(
                polygonal.validated.lower(value)
                for value in other_pair_distances
            ),
            "second_to_selected_distance_ratio_lower": min(
                polygonal.validated.lower(value)
                for value in other_pair_distances
            )
            / polygonal.validated.upper(pair_distance),
            "minimum_root_ball_separation_lower": minimum_root_ball_separation,
            "selected_root_to_node_distance_upper": max(
                distances[0][0], distances[1][0]
            ),
            "next_root_to_node_distance_lower": distances[2][1],
            "node_affinity_separation_margin_lower": distances[2][1]
            - max(distances[0][0], distances[1][0]),
        }

    return select, node_file


if __name__ == "__main__":
    if "--output" in sys.argv:
        raise AssertionError("node-pair wrapper currently requires the default output path")
    index = argument_value("--distinguished-index", 4)
    selector, node_file = certified_node_pair_selector(index)
    wrapper_file = __file__
    polygonal.pilot.closest_pair = selector
    polygonal.__file__ = wrapper_file
    result = polygonal.main()
    source = json.loads(source_path(index).read_text(encoding="utf-8"))
    output = PERIOD_DIRECTORY / (
        f"d{index:03d}_{source['root_id']}.E32_main.interval.packet.json"
    )
    packet = json.loads(output.read_text(encoding="utf-8"))
    packet["authority"]["certified_node_pair_source"] = str(
        node_file.relative_to(ROOT)
    ).replace("\\", "/")
    packet["authority"]["certified_node_pair_source_sha256"] = sha256(node_file)
    packet["scope"]["certified_nodal_pair_selector_consumed"] = True
    polygonal.dump(output, packet)
    raise SystemExit(result)
