from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
HANDLE = VALIDATED / "n3.rank3.handle_combination.interval.json"
BASE_LIFT = VALIDATED / "n3.rank3.base_lift.interval.json"
BETA = VALIDATED / "n3.rank3.anchored_beta.interval.json"
NOTES = [
    ROOT / "proof_corpus" / "MTT_q79HeightFourRank3HandleCombinationInterval_A374_v1.md",
    ROOT / "proof_corpus" / "MTT_q79HeightFourRank3BaseLiftInterval_A375_v1.md",
    ROOT / "proof_corpus" / "MTT_q79HeightFourRank3AnchoredBetaInterval_A376_v1.md",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_authority(packet: dict, label: str) -> None:
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing {label} authority {name}")
        require(sha256(path) == row["sha256"], f"stale {label} authority {name}")


def main() -> int:
    for path in [HANDLE, BASE_LIFT, BETA, *NOTES]:
        require(path.exists(), f"missing rank-3 moving-block artifact {path.name}")

    handle = load(HANDLE)
    require(handle["artifact"] == "A374", "A374 artifact label changed")
    require(
        handle["status"]
        == "N3_RANK3_ALL_EIGHT_HANDLE_COMBINATION_INTERVAL_CERTIFIED",
        "A374 status changed",
    )
    require(
        handle["selected_rank3_chain"]["primitive_handle_coordinates"]
        == [1, 1, 1, -1, 1, 0, 0, 1],
        "A374 rank-3 handle coordinates changed",
    )
    handle_rows = handle["all_eight_handle_rows"]
    require(len(handle_rows) == 8, "A374 row count changed")
    require(
        all(row["floating_value_contained"] for row in handle_rows),
        "A374 lost floating containment",
    )
    require(
        min(float(row["minimum_component_containment_margin"]) for row in handle_rows)
        > 0.0,
        "A374 containment margin is not positive",
    )
    handle_scope = handle["strict_scope"]
    require(handle_scope["rank3_handle_combination_interval_closed"], "A374 handle open")
    require(not handle_scope["rank3_anchored_beta_interval_closed"], "A374 overclaims beta")
    require(not handle_scope["interval_Jacobian_certificate"], "A374 overclaims Jacobian")
    require(not handle_scope["covariant_zero_proved"], "A374 overclaims zero")
    check_authority(handle, "A374")

    base_lift = load(BASE_LIFT)
    require(base_lift["artifact"] == "A375", "A375 artifact label changed")
    require(
        base_lift["status"] == "N3_RANK3_BASE_ABEL_JACOBI_LIFT_INTERVAL_CERTIFIED",
        "A375 status changed",
    )
    require(len(base_lift["y_chart_base_lift"]) == 5, "A375 y-lift dimension changed")
    require(
        float(base_lift["branch_selection"]["root_label_separation_margin_lower"])
        > 0.0,
        "A375 winding-root label is not separated",
    )
    base_scope = base_lift["strict_scope"]
    require(
        base_scope["rank3_base_Abel_Jacobi_lift_interval_closed"],
        "A375 base lift open",
    )
    require(not base_scope["rank3_anchored_beta_interval_closed"], "A375 overclaims beta")
    require(not base_scope["covariant_zero_proved"], "A375 overclaims zero")
    check_authority(base_lift, "A375")

    beta = load(BETA)
    require(beta["artifact"] == "A376", "A376 artifact label changed")
    require(
        beta["status"] == "N3_RANK3_ANCHORED_BETA_ALL_EIGHT_INTERVAL_CERTIFIED",
        "A376 status changed",
    )
    beta_rows = beta["all_eight_beta_rows"]
    require(len(beta_rows) == 8, "A376 row count changed")
    require(
        all(row["floating_value_contained"] for row in beta_rows),
        "A376 lost floating containment",
    )
    require(
        min(float(row["minimum_component_containment_margin"]) for row in beta_rows)
        > 0.0,
        "A376 containment margin is not positive",
    )
    require(beta["endpoint"]["zero_excluded"], "A376 endpoint beta zero exclusion lost")
    beta_scope = beta["strict_scope"]
    require(beta_scope["rank3_anchored_beta_interval_closed"], "A376 beta open")
    require(not beta_scope["interval_Jacobian_certificate"], "A376 overclaims Jacobian")
    require(not beta_scope["covariant_zero_proved"], "A376 overclaims zero")
    require(not beta_scope["full_SM_closure_proved"], "A376 overclaims SM closure")
    require(not beta_scope["observed_SM_values_used"], "moving blocks used observed SM data")
    check_authority(beta, "A376")

    print("q79 A374-A376 rank-3 moving interval blocks audit: PASS")
    print("closed: exact-n3 handle combination, base lift, and anchored beta intervals")
    print("open: full residual recomposition, interval Jacobian, and interval Newton")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
