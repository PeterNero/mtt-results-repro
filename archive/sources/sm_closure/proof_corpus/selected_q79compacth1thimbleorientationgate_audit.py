from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
MAIN = PERIOD_DIRECTORY / "d030_selected_034.E32_main.interval.packet.json"
FULL = PERIOD_DIRECTORY / "d030_selected_034.E32_full.interval.packet.json"
A158 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A158.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79CompactH1ThimbleOrientationGate_v1.md"
BUILDER = ROOT / "scripts" / "certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_compact_h1.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 2.0e-18) -> bool:
    return math.isclose(left, right, rel_tol=1.0e-13, abs_tol=tolerance)


def main() -> int:
    orientation = load(ORIENTATION)
    main_packet = load(MAIN)
    full = load(FULL)
    successor = load(A158)

    scope = orientation["strict_scope"]
    assert scope["compact_H1_holomorphic_rows_used_for_orientation"] == 2
    assert scope["higher_meromorphic_rows_used_for_orientation"] == 0
    assert scope["higher_meromorphic_rows_retain_puncture_lift_dependence"]
    assert orientation["checks"]["next_best_to_selected_maximum_residual_ratio"] == (
        "134359078.62281385"
    )

    authority = main_packet["authority"]
    assert authority["builder_source"] == str(BUILDER.relative_to(ROOT)).replace(
        "\\", "/"
    )
    assert authority["builder_source_sha256"] == sha256(BUILDER)
    assert authority["orientation_synchronization"] == str(
        ORIENTATION.relative_to(ROOT)
    ).replace("\\", "/")
    assert authority["orientation_synchronization_sha256"] == sha256(ORIENTATION)
    selected = main_packet["orientation"]
    assert selected["selection_basis"] == "compact H1 holomorphic periods only"
    assert selected["compact_H1_holomorphic_component_count"] == 2
    assert selected["selected_sign"] == -1
    assert not selected["higher_meromorphic_rows_used_for_orientation"]
    assert close(
        selected["selected_base_center_maximum_difference"],
        1.922947248965649e-10,
    )
    assert selected["opposite_base_center_maximum_difference"] > 0.258
    assert selected["higher_meromorphic_puncture_lift_difference_diagnostic"] > 11.5
    assert main_packet["scope"]["compact_H1_orientation_synchronization_consumed"]
    assert main_packet["scope"][
        "higher_meromorphic_puncture_lift_rows_excluded_from_orientation"
    ]

    system = validated.SelectedQ79IntervalSystem(dps=60, line_chart="y")
    _connection, _source, residue = system.connection_source_residue(acb(0))
    assert all(
        residue[row][column] == acb(0)
        for row in range(len(residue))
        for column in range(2, 5)
    )

    assert close(
        main_packet["validated_main_transport"]["uniform_integral_radius_upper"],
        6.576746775026099e-8,
    )
    assert full["full_E32_thimble"]["floating_candidate_contained"]
    assert full["A134_radius_ledger"]["fallback_met"]
    assert successor["new_accepted_full_interval"]["distinguished_index"] == 30
    assert successor["weighted_budget_ledger"]["selected_support_closed"] == 23
    assert "higher meromorphic rows" in NOTE.read_text(encoding="utf-8")

    print("q79 compact-H1 thimble orientation gate audit: PASS")
    print("closed: d030 sign from two synchronized holomorphic periods")
    print("closed: E32 residue excludes all three meromorphic lift columns")
    print("frontier: A158 support 23/71 and L1 44/123")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
