"""Audit refreshed Higgs channel ledger and total-width replay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "refreshed_higgs_channel_status_ledger.packet.json"
REPLAY = PACKET_DIR / "refreshed_higgs_total_width_replay.packet.json"
DELTA = PACKET_DIR / "higgs_channel_refresh_delta.packet.json"
DECISION = PACKET_DIR / "higgs_total_width_precision_decision_after_refresh.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsComputedChannelRefresh_or_TotalWidthReplay_v1.md"

STATUS = "MTT_SELECTED_HIGGSCOMPUTEDCHANNELREFRESH_OR_TOTALWIDTHREPLAY_BUILT_MORE_COMPUTED_ROWS_PRECISION_OPEN"
NEXT = "MTT_Selected_HiggsRemainingEWFormulaRows_or_PrecisionTotalWidth_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    ledger = load(LEDGER)
    replay = load(REPLAY)
    delta = load(DELTA)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(ledger["summary"]["channel_count"] == 10, "ledger channel count mismatch")
    require(ledger["summary"]["computed_proxy_channel_count"] == 7, "computed channel count mismatch")
    require(ledger["summary"]["external_benchmark_fill_channel_count"] == 3, "external fill count mismatch")
    require(ledger["summary"]["all_computed_channels_precision_accepted"] is False, "precision overclaimed")
    require(set(ledger["summary"]["newly_computed_channels"]) == {"H_to_ss", "H_to_gg", "H_to_gamma_gamma"}, "new computed channels mismatch")
    require(replay["accepted_as_total_width_replay_scaffold"] is True, "replay scaffold not accepted")
    require(replay["accepted_as_precision_total_width"] is False, "precision total width overclaimed")
    require(replay["summary"]["computed_proxy_channel_count"] == 7, "replay computed count mismatch")
    require(replay["summary"]["external_benchmark_fill_channel_count"] == 3, "replay external count mismatch")
    require(delta["summary"]["replacement_count"] == 3, "replacement count mismatch")
    require(delta["summary"]["new_refreshed_width_sum_GeV"] != delta["summary"]["old_hybrid_width_sum_GeV"], "refresh did not change replay")
    require(decision["precision_total_width_closed"] is False, "precision total overclosed")
    require(decision["branching_ratios_closed"] is False, "BR overclosed")
    require(decision["values_promotable_to_precision_now"] is False, "values overpromoted")
    require(set(decision["remaining_external_fill_channels"]) == {"H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"}, "remaining fills mismatch")
    require(data["closure_decision"]["computed_channel_refresh_closed"] is True, "refresh closure missing")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "candidate precision overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not a precision total width" in note, "note missing precision guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
