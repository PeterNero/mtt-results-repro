from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
PACKET = PROBE / "validated_transport" / "n3.chain.frontier.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourN3ChainDecompositionFrontier_A231_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def main() -> int:
    require(PACKET.exists(), "missing A231 packet")
    require(NOTE.exists(), "missing A231 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A231", "A231 artifact label changed")
    require(
        packet["status"]
        == "N3_FULL_FLOATING_CHAIN_IDENTITY_REPLAYED_INTERVAL_FRONTIER_EXACT",
        "A231 status changed",
    )
    authority = packet["authority"]
    for name, row in authority.items():
        if name == "n3_thimble_caches":
            continue
        path = ROOT / row["path"]
        require(path.exists(), f"missing A231 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A231 authority {name}")
    caches = authority["n3_thimble_caches"]
    require(len(caches) == 76, "A231 cache count changed")
    require(
        len({int(row["distinguished_index"]) for row in caches}) == 76,
        "A231 cache inventory is not unique",
    )
    for row in caches:
        path = ROOT / row["path"]
        require(path.exists(), "missing A231 thimble cache")
        require(sha256(path) == row["sha256"], "stale A231 thimble cache")

    decomposition = packet["exact_floating_decomposition"]
    rows = decomposition["thimble_rows"]
    require(len(rows) == 76, "A231 thimble support changed")
    thimble_sum = np.sum(
        np.asarray([vector(row["raw_chain_contribution"]) for row in rows]), axis=0
    )
    require(
        np.max(abs(thimble_sum - vector(decomposition["raw_thimble_sum"]))) < 1.0e-12,
        "A231 raw thimble sum changed",
    )
    raw = thimble_sum + vector(decomposition["primitive_handle_contribution"])
    require(
        np.max(abs(raw - vector(decomposition["raw_moving_period_recomposition"])))
        < 1.0e-12,
        "A231 raw moving-period identity changed",
    )
    corrected = raw + vector(decomposition["PL_period_correction"])
    require(
        np.max(
            abs(
                corrected
                - vector(decomposition["PL_corrected_moving_period_recomposition"])
            )
        )
        < 1.0e-12,
        "A231 PL-corrected identity changed",
    )
    require(int(decomposition["PL_wall_source_distinguished_index"]) == 64, "wall source changed")
    require(int(decomposition["PL_crossing_period_distinguished_index"]) == 65, "wall period changed")
    require(int(decomposition["PL_wall_weight"]) == 3, "wall weight changed")
    require(
        max(
            float(decomposition["stored_raw_replay_maximum_error"]),
            float(decomposition["stored_wall_replay_maximum_error"]),
            float(decomposition["stored_corrected_replay_maximum_error"]),
        )
        < 1.0e-12,
        "A231 stored replay tolerance failed",
    )

    summary = packet["summary"]
    require(int(summary["raw_thimble_support"]) == 76, "A231 raw support changed")
    require(int(summary["raw_thimble_coefficient_l1_norm"]) == 165, "A231 raw L1 changed")
    require(int(summary["PL_corrected_support"]) == 76, "A231 corrected support changed")
    require(
        int(summary["PL_corrected_coefficient_l1_norm"]) == 168,
        "A231 corrected L1 changed",
    )
    require(int(summary["certified_all_eight_thimble_target_count"]) == 5, "A231 certified count changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 71, "A231 frontier count changed")
    require(not summary["A209_replaces_rank3_thimble_frontier"], "A231 incorrectly promotes A209")
    frontier = packet["remaining_interval_frontier"]
    targets = frontier["targets_in_A219_profile_priority_order"]
    require(len(targets) == 71, "A231 frontier inventory changed")
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == sorted(int(row["A219_profile_priority_rank"]) for row in targets),
        "A231 frontier priority order changed",
    )
    scope = packet["strict_scope"]
    require(scope["full_n3_floating_chain_decomposition_identity_closed"], "A231 identity reopened")
    require(scope["PL_wall_correction_assignment_closed"], "A231 PL assignment reopened")
    require(not scope["remaining_71_all_eight_thimble_intervals_closed"], "A231 overclaims 71 intervals")
    require(not scope["rank3_handle_combination_interval_closed"], "A231 overclaims handles")
    require(not scope["rank3_anchored_beta_interval_closed"], "A231 overclaims beta")
    require(not scope["interval_Jacobian_certificate"], "A231 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A231 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A231 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A231 consumed observed SM values")
    note = NOTE.read_text(encoding="utf-8")
    require("A209 certifies E32 primitive handles" in note, "A231 note lost A209 correction")
    print("q79 A231 n3 chain-decomposition frontier audit: PASS")
    print("closed: exact 76-thimble + handle + PL floating identity and 71-target frontier")
    print("open: 71 all-eight intervals, selected handle/beta intervals, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
