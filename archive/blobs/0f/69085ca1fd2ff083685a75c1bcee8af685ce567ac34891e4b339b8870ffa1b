from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb

import certify_q79_selected_alignment_single_E32_thimble_tail_interval as tail


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
    return int(sys.argv[sys.argv.index(name) + 1])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unique(pattern: str) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(pattern))
    if len(rows) != 1:
        raise AssertionError(f"expected one artifact for {pattern}")
    return rows[0]


def node_pair_selector(index: int):
    node_file = unique(f"d{index:03d}_*.nodal_factor.interval.packet.json")
    packet = json.loads(node_file.read_text(encoding="utf-8"))
    encoded_node = packet["certified_node"]["double_root_ball"]

    def select(roots: list[acb]) -> tuple[int, int]:
        node = acb(encoded_node["real"], encoded_node["imaginary"])
        distances = sorted(
            (
                tail.validated.upper(abs(root - node)),
                tail.validated.lower(abs(root - node)),
                root_index,
            )
            for root_index, root in enumerate(roots)
        )
        if distances[1][0] >= distances[2][1]:
            raise AssertionError(
                "two cutoff roots nearest the certified node are not separated"
            )
        return tuple(sorted((distances[0][2], distances[1][2])))

    return select, node_file


if __name__ == "__main__":
    if "--output" in sys.argv:
        raise AssertionError("node-pair wrapper currently requires the default output path")
    index = argument_value("--distinguished-index", 4)
    selector, node_file = node_pair_selector(index)
    wrapper_file = __file__
    tail.nodal.closest_pair = selector
    tail.__file__ = wrapper_file
    result = tail.main()
    source = json.loads(
        unique(f"d{index:03d}_*.thimble_period.candidate.json").read_text(
            encoding="utf-8"
        )
    )
    output = PERIOD_DIRECTORY / (
        f"d{index:03d}_{source['root_id']}.E32_tail.interval.packet.json"
    )
    packet = json.loads(output.read_text(encoding="utf-8"))
    packet["authority"]["certified_node_pair_source"] = str(
        node_file.relative_to(ROOT)
    ).replace("\\", "/")
    packet["authority"]["certified_node_pair_source_sha256"] = sha256(node_file)
    packet["cutoff_direct_period_reference"]["pair_selection_method"] = (
        "two cutoff roots nearest the independently certified nodal double-root ball"
    )
    packet["scope"]["certified_nodal_pair_selector_consumed"] = True
    tail.dump(output, packet)
    raise SystemExit(result)
