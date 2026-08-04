"""Refresh Higgs channel ledger with newer computed proxy rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEDGER = PACKET_DIR / "refreshed_higgs_channel_status_ledger.packet.json"
REPLAY = PACKET_DIR / "refreshed_higgs_total_width_replay.packet.json"
DELTA = PACKET_DIR / "higgs_channel_refresh_delta.packet.json"
DECISION = PACKET_DIR / "higgs_total_width_precision_decision_after_refresh.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsComputedChannelRefresh_or_TotalWidthReplay_v1.md"

STATUS = "MTT_SELECTED_HIGGSCOMPUTEDCHANNELREFRESH_OR_TOTALWIDTHREPLAY_BUILT_MORE_COMPUTED_ROWS_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade.candidate.json")
    old_ledger = load(
        DATA
        / "selected_completehiggschannelledger_or_totalwidthpolicy"
        / "complete_higgs_channel_status_ledger.packet.json"
    )
    old_hybrid = load(
        DATA
        / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
        / "hybrid_higgs_total_width_replay.packet.json"
    )
    qcd_execution = load(
        DATA
        / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
        / "higgs_qcd_nonfit_formula_execution.packet.json"
    )
    gamma = load(
        DATA
        / "selected_higgsgammagammacorrection_or_qcdthresholdrows"
        / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"
    )

    qcd_widths = {row["channel"]: row["computed_width_GeV"] for row in qcd_execution["rows"]}
    source_paths = {
        "H_to_ss": rel(
            DATA
            / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
            / "higgs_qcd_nonfit_formula_execution.packet.json"
        ),
        "H_to_gg": rel(
            DATA
            / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
            / "higgs_qcd_nonfit_formula_execution.packet.json"
        ),
        "H_to_gamma_gamma": rel(
            DATA
            / "selected_higgsgammagammacorrection_or_qcdthresholdrows"
            / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"
        ),
    }
    computed_replacements = {
        "H_to_ss": {
            "width_GeV": qcd_widths["H_to_ss"],
            "status": "COMPUTED_FIRSTPASS_NONFIT_QCD_FORMULA_NOT_PRECISION",
            "row_kind": "computed_proxy",
        },
        "H_to_gg": {
            "width_GeV": qcd_widths["H_to_gg"],
            "status": "COMPUTED_FIRSTPASS_NONFIT_QCD_FORMULA_NOT_PRECISION",
            "row_kind": "computed_proxy",
        },
        "H_to_gamma_gamma": {
            "width_GeV": gamma["all_charged_one_loop_width_GeV"],
            "status": "COMPUTED_ONELOOP_ALL_CHARGED_FORMULA_NOT_PRECISION",
            "row_kind": "computed_proxy",
        },
    }

    refreshed_rows = []
    old_rows = {row["channel"]: row for row in old_hybrid["rows"]}
    for row in old_hybrid["rows"]:
        channel = row["channel"]
        refreshed = dict(row)
        refreshed["source_packet"] = row.get("source_packet")
        if channel in computed_replacements:
            refreshed.update(computed_replacements[channel])
            refreshed["source_packet"] = source_paths[channel]
            refreshed["precision_accepted"] = False
            refreshed["replaced_external_benchmark_fill"] = row["row_kind"] == "external_benchmark_fill"
        else:
            refreshed["replaced_external_benchmark_fill"] = False
        refreshed_rows.append(refreshed)

    refreshed_sum = sum(float(row["width_GeV"]) for row in refreshed_rows)
    reference_total = float(old_hybrid["summary"]["reference_total_width_GeV"])
    computed_channels = [row["channel"] for row in refreshed_rows if row["row_kind"] == "computed_proxy"]
    external_channels = [row["channel"] for row in refreshed_rows if row["row_kind"] == "external_benchmark_fill"]

    ledger = {
        "schema": "MTTRefreshedHiggsChannelStatusLedger.v1",
        "status": "HIGGS_CHANNEL_LEDGER_REFRESHED_WITH_NEW_COMPUTED_ROWS",
        "channels": refreshed_rows,
        "summary": {
            "channel_count": len(refreshed_rows),
            "computed_proxy_channel_count": len(computed_channels),
            "external_benchmark_fill_channel_count": len(external_channels),
            "newly_computed_channels": ["H_to_ss", "H_to_gg", "H_to_gamma_gamma"],
            "all_major_channels_have_width_rows": True,
            "all_computed_channels_precision_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    replay = {
        "schema": "MTTRefreshedHiggsTotalWidthReplay.v1",
        "status": "REFRESHED_TOTAL_WIDTH_REPLAY_BUILT_MORE_COMPUTED_ROWS_NOT_PRECISION",
        "rows": refreshed_rows,
        "summary": {
            "refreshed_width_sum_GeV": refreshed_sum,
            "reference_total_width_GeV": reference_total,
            "refreshed_minus_reference_GeV": refreshed_sum - reference_total,
            "refreshed_relative_residual_to_reference": (refreshed_sum - reference_total) / reference_total,
            "computed_proxy_channels": computed_channels,
            "external_benchmark_fill_channels": external_channels,
            "computed_proxy_channel_count": len(computed_channels),
            "external_benchmark_fill_channel_count": len(external_channels),
        },
        "accepted_as_precision_total_width": False,
        "accepted_as_total_width_replay_scaffold": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    deltas = []
    for channel in ["H_to_ss", "H_to_gg", "H_to_gamma_gamma"]:
        old = old_rows[channel]
        new = next(row for row in refreshed_rows if row["channel"] == channel)
        deltas.append(
            {
                "channel": channel,
                "old_row_kind": old["row_kind"],
                "new_row_kind": new["row_kind"],
                "old_width_GeV": old["width_GeV"],
                "new_width_GeV": new["width_GeV"],
                "delta_GeV": new["width_GeV"] - old["width_GeV"],
                "precision_accepted": False,
                "observed_data_used_as_selector": False,
            }
        )
    delta_packet = {
        "schema": "MTTHiggsChannelRefreshDelta.v1",
        "status": "THREE_EXTERNAL_FILL_ROWS_REPLACED_BY_COMPUTED_PROXY_ROWS",
        "rows": deltas,
        "summary": {
            "replacement_count": len(deltas),
            "old_hybrid_width_sum_GeV": old_hybrid["summary"]["hybrid_width_sum_GeV"],
            "new_refreshed_width_sum_GeV": refreshed_sum,
            "width_sum_delta_GeV": refreshed_sum - old_hybrid["summary"]["hybrid_width_sum_GeV"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTHiggsTotalWidthPrecisionDecisionAfterRefresh.v1",
        "status": "MORE_COMPUTED_ROWS_FILLED_PRECISION_TOTAL_WIDTH_STILL_REJECTED",
        "computed_proxy_channel_count": len(computed_channels),
        "external_benchmark_fill_channel_count": len(external_channels),
        "precision_total_width_closed": False,
        "branching_ratios_closed": False,
        "values_promotable_to_precision_now": False,
        "remaining_external_fill_channels": external_channels,
        "remaining_precision_blockers": [
            "WW*/ZZ* off-shell formula rows still use external fills",
            "Z gamma row still uses external fill",
            "computed QCD and gamma-gamma rows are proxy/first-pass, not precision",
            "full covariance/profile likelihood is not filled",
            "actual no-knob Qa/SU3 remains open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsComputedChannelRefreshOrTotalWidthReplay",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade.candidate.json"),
            "old_channel_ledger": rel(
                DATA
                / "selected_completehiggschannelledger_or_totalwidthpolicy"
                / "complete_higgs_channel_status_ledger.packet.json"
            ),
            "old_hybrid_replay": rel(
                DATA
                / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
                / "hybrid_higgs_total_width_replay.packet.json"
            ),
            "qcd_nonfit_formula_execution": source_paths["H_to_gg"],
            "gamma_gamma_formula_execution": source_paths["H_to_gamma_gamma"],
        },
        "output_packets": {
            "refreshed_channel_ledger": rel(LEDGER),
            "refreshed_total_width_replay": rel(REPLAY),
            "channel_refresh_delta": rel(DELTA),
            "precision_decision": rel(DECISION),
        },
        "theorem": {
            "name": "HiggsComputedChannelRefreshTheorem",
            "proved": True,
            "statement": (
                "The later computed proxy rows for H_to_ss, H_to_gg, and H_to_gamma_gamma can replace "
                "their older external benchmark-fill rows in a refreshed total-width replay scaffold. This "
                "increases computed-channel coverage while keeping precision total width, branching ratios, "
                "full covariance, and no-knob Qa/SU3 open."
            ),
        },
        "what_closes_now": {
            "refreshed_Higgs_channel_ledger": True,
            "external_fill_replaced_for_ss_gg_gamma_gamma": True,
            "refreshed_total_width_replay_scaffold": True,
        },
        "what_remains_open": {
            "WW_ZZ_Zgamma_formula_rows": True,
            "precision_QCD_gamma_rows": True,
            "full_covariance_profile_likelihood": True,
            "total_width_precision_closure": True,
            "branching_ratio_precision_closure": True,
            "actual_QaSU3_operator_packet_no_knob": True,
        },
        "closure_decision": {
            "computed_channel_refresh_closed": True,
            "precision_total_width_closed": False,
            "branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsComputedChannelRefresh_or_TotalWidthReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "computed_channel_refresh_closed": True,
        "precision_total_width_closed": False,
        "branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRemainingEWFormulaRows_or_PrecisionTotalWidth_v1",
    }

    note = f"""# MTT Selected HiggsComputedChannelRefresh or TotalWidthReplay v1

Status: `{STATUS}`.

This artifact refreshes the Higgs total-width replay scaffold by replacing old
external benchmark-fill rows for `H_to_ss`, `H_to_gg`, and `H_to_gamma_gamma`
with the newer executable proxy/formula rows already built in the repo.

The refreshed replay increases computed-channel coverage. It is still not a precision total width, not a branching-ratio closure, and not true SM equivalence.
"""

    for path, payload in [
        (LEDGER, ledger),
        (REPLAY, replay),
        (DELTA, delta_packet),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
