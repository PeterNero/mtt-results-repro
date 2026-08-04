from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.rank3.full_residual.interval.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3FullResidualInterval_A377_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    require(PACKET.exists(), "missing A377 residual packet")
    require(NOTE.exists(), "missing A377 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A377", "A377 artifact label changed")
    require(
        packet["status"] == "N3_RANK3_FULL_EIGHT_RESIDUAL_ROWS_INTERVAL_RECOMPOSED",
        "A377 status changed",
    )
    wall = packet["PL_wall_correction"]
    require(int(wall["source_distinguished_index"]) == 64, "A377 wall source changed")
    require(
        int(wall["crossing_period_distinguished_index"]) == 65,
        "A377 wall period changed",
    )
    require(int(wall["integer_weight"]) == 3, "A377 wall weight changed")
    rows = packet["residue_rows"]
    require(len(rows) == 8, "A377 row count changed")
    require(
        all(row["floating_residual_contained"] for row in rows),
        "A377 lost floating residual containment",
    )
    require(
        min(float(row["floating_containment_margin"]) for row in rows) > 0.0,
        "A377 containment margin is not positive",
    )
    require(
        all(float(row["residual_component_radius_upper"]) > 0.0 for row in rows),
        "A377 residual radius is not positive",
    )
    summary = packet["summary"]
    require(int(summary["certified_rows"]) == 8, "A377 summary row count changed")
    require(summary["all_floating_residual_diagnostics_contained"], "A377 summary containment lost")
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A377 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A377 authority {name}")
    scope = packet["strict_scope"]
    require(scope["all_76_target_intervals_closed"], "A377 reopened target chain")
    require(scope["rank3_handle_combination_interval_closed"], "A377 reopened handle")
    require(scope["rank3_anchored_beta_interval_closed"], "A377 reopened beta")
    require(scope["PL_wall_correction_interval_closed"], "A377 reopened PL correction")
    require(scope["rank3_full_residual_interval_closed"], "A377 residual is open")
    require(
        scope["zero_in_residual_box_is_not_an_existence_proof"],
        "A377 confused zero containment with existence",
    )
    require(not scope["interval_Jacobian_certificate"], "A377 overclaims Jacobian")
    require(
        not scope["interval_Newton_existence_and_uniqueness_closed"],
        "A377 overclaims interval Newton",
    )
    require(not scope["covariant_zero_proved"], "A377 overclaims covariant zero")
    require(not scope["full_SM_closure_proved"], "A377 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A377 used observed SM data")
    print("q79 A377 rank-3 full residual interval audit: PASS")
    print("closed: 76-thimble + handle + PL wall + beta all-row residual enclosure")
    print("open: interval Jacobian and interval Newton existence/uniqueness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
