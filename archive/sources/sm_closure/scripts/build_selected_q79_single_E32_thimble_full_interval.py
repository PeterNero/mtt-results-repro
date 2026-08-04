from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import acb, arb

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
DEFAULT_INDEX = 4


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def disk(center: dict[str, str], radius: float) -> acb:
    return acb(
        arb(center["real"], format(radius, ".17g")),
        arb(center["imaginary"], format(radius, ".17g")),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, default=DEFAULT_INDEX)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    source_path = nodal.candidate_path(arguments.distinguished_index)
    source = load(source_path)
    stem = f"d{arguments.distinguished_index:03d}_{source['root_id']}"
    main_path = PERIOD_DIRECTORY / f"{stem}.E32_main.interval.packet.json"
    tail_path = PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json"
    if not main_path.exists() or not tail_path.exists():
        raise FileNotFoundError("both the selected main and tail interval packets are required")
    main_packet = load(main_path)
    tail_packet = load(tail_path)
    a134 = load(A134)
    if main_packet["selected_thimble"]["root_id"] != source["root_id"]:
        raise AssertionError("main interval root id mismatch")
    if tail_packet["selected_thimble"]["root_id"] != source["root_id"]:
        raise AssertionError("tail interval root id mismatch")
    if main_packet["selected_thimble"]["line_chart"] != source["line_chart"]:
        raise AssertionError("main interval and floating source charts differ")
    if tail_packet["selected_thimble"].get("line_chart", "y") != source["line_chart"]:
        raise AssertionError("tail interval and floating source charts differ")
    main_epsilon = float(main_packet["selected_thimble"]["endpoint_cutoff_epsilon"])
    tail_epsilon = float(tail_packet["selected_thimble"]["endpoint_cutoff_epsilon"])
    if main_epsilon != tail_epsilon:
        raise AssertionError("main and tail cutoff values differ")

    main_row = main_packet["E32_main_segment"]
    main_ball = disk(
        main_row["interval_center"], float(main_row["interval_radius_upper"])
    )
    tail_ball = validated.interval_from_bounds(
        tail_packet["E32_endpoint_tail"]["interval"]
    )
    orientation_sign = int(main_packet["orientation"]["selected_sign"])
    if orientation_sign not in (-1, 1):
        raise AssertionError("main orientation sign is not binary")
    oriented_tail = acb(orientation_sign) * tail_ball
    full = main_ball + oriented_tail
    floating = handle.complex_value(
        source["execution"]["period_values"][FORM_NAMES.index("E32")]
    )
    floating_ball = acb(
        format(floating.real, ".17g"), format(floating.imag, ".17g")
    )
    floating_contained = full.contains(floating_ball)
    center_difference = abs(handle.midpoint(full) - floating)
    radius = validated.radius_upper(full)
    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )

    output = arguments.output
    if output is None:
        output = PERIOD_DIRECTORY / f"{stem}.E32_full.interval.packet.json"
    elif not output.is_absolute():
        output = ROOT / output
    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleE32ThimbleFullInterval.v1",
        "status": (
            "SELECTED_SINGLE_E32_THIMBLE_FULL_INTERVAL_CERTIFIED_WITHIN_A134_FALLBACK"
            if radius < fallback
            else "SELECTED_SINGLE_E32_THIMBLE_FULL_INTERVAL_CERTIFIED_FALLBACK_RADIUS_NOT_MET"
        ),
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (source_path, main_path, tail_path, A134, Path(__file__))
        ],
        "selected_thimble": {
            "distinguished_index": arguments.distinguished_index,
            "root_id": source["root_id"],
            "line_chart": source["line_chart"],
            "endpoint_cutoff_epsilon": main_epsilon,
            "orientation_sign_from_validated_base_marking": orientation_sign,
        },
        "splice_identity": (
            "full_E32 = validated_main_E32 + orientation_sign * "
            "validated_node_to_cutoff_tail_E32"
        ),
        "components": {
            "main_interval": main_row,
            "raw_tail_interval": tail_packet["E32_endpoint_tail"],
            "oriented_tail_interval": handle.complex_interval(oriented_tail),
        },
        "full_E32_thimble": {
            "interval": handle.complex_interval(full),
            "interval_center": handle.complex_pair(handle.midpoint(full)),
            "interval_radius_upper": radius,
            "A131_floating_candidate_diagnostic_only": handle.complex_pair(floating),
            "floating_candidate_center_difference": center_difference,
            "floating_candidate_contained": bool(floating_contained),
        },
        "A134_radius_ledger": {
            "sufficient_uniform_per_unit_thimble_radius": fallback,
            "single_thimble_radius": radius,
            "fallback_margin": fallback - radius,
            "fallback_met": bool(radius < fallback),
        },
        "scope": {
            "observed_SM_values_used": False,
            "floating_candidate_used_as_bound": False,
            "main_interval_closed": True,
            "nodal_tail_interval_closed": True,
            "orientation_splice_closed": True,
            "single_full_E32_thimble_interval_closed": True,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "next_required_artifact": (
            "execute the same source-selected certificate for the remaining weighted support, "
            "then sum the 71 oriented balls with their exact integer coefficients"
        ),
    }
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "distinguished_index": arguments.distinguished_index,
                "root_id": source["root_id"],
                "full_center": handle.complex_pair(handle.midpoint(full)),
                "full_radius": radius,
                "fallback": fallback,
                "fallback_met": radius < fallback,
                "floating_contained": floating_contained,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
