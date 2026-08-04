from __future__ import annotations

import json
import sys
from pathlib import Path

import build_selected_q79_single_E32_thimble_full_interval as full
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
FULL_BUILDER_SOURCE = Path(full.__file__).resolve()
FULL_BUILDER_SHA256 = full.sha256(FULL_BUILDER_SOURCE)


def argument_value(name: str, default: int) -> int:
    if name not in sys.argv:
        return default
    return int(sys.argv[sys.argv.index(name) + 1])


def main() -> int:
    if "--output" in sys.argv:
        raise AssertionError("legacy-y promotion requires the default output path")
    index = argument_value("--distinguished-index", 4)
    source_path = nodal.candidate_path(index)
    source = full.load(source_path)
    if source["line_chart"] != "y":
        raise AssertionError("legacy chart promotion is restricted to the old y-only tail engine")
    stem = f"d{index:03d}_{source['root_id']}"
    tail_path = PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json"
    output_path = PERIOD_DIRECTORY / f"{stem}.E32_full.interval.packet.json"
    original_load = full.load

    def load_with_legacy_y_chart(path: Path) -> dict:
        packet = original_load(path)
        if Path(path).resolve() != tail_path.resolve():
            return packet
        selected = packet["selected_thimble"]
        if "line_chart" in selected:
            if selected["line_chart"] != "y":
                raise AssertionError("explicit tail chart is not y")
            return packet
        authority = packet["authority"]
        if authority["floating_candidate"] != full.relative(source_path):
            raise AssertionError("legacy tail does not name the selected source candidate")
        if authority["floating_candidate_sha256"] != full.sha256(source_path):
            raise AssertionError("legacy tail source-candidate hash changed")
        if int(selected["distinguished_index"]) != index:
            raise AssertionError("legacy tail distinguished index changed")
        if selected["root_id"] != source["root_id"]:
            raise AssertionError("legacy tail root id changed")
        selected["line_chart"] = "y"
        return packet

    full.load = load_with_legacy_y_chart
    full.__file__ = __file__
    if full.sha256(FULL_BUILDER_SOURCE) != FULL_BUILDER_SHA256:
        raise AssertionError("full builder changed after wrapper import")
    result = full.main()
    if full.sha256(FULL_BUILDER_SOURCE) != FULL_BUILDER_SHA256:
        raise AssertionError("full builder changed during promoted execution")

    packet = json.loads(output_path.read_text(encoding="utf-8"))
    packet["authority"].append(
        {
            "path": full.relative(FULL_BUILDER_SOURCE),
            "sha256": FULL_BUILDER_SHA256,
        }
    )
    packet["selected_thimble"]["tail_line_chart_source"] = (
        "selected y-chart source candidate plus matching legacy-tail source authority"
    )
    packet["scope"]["legacy_y_only_tail_chart_promoted_in_memory"] = True
    full.dump(output_path, packet)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
