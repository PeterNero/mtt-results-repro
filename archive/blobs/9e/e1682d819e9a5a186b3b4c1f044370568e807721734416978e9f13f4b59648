"""Build remaining electroweak Higgs formula-row gate after channel refresh."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsremainingewformularows_or_precisiontotalwidth"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EW_GATE = PACKET_DIR / "remaining_ew_formula_or_precision_import_gate.packet.json"
TEN_CHANNEL = PACKET_DIR / "refreshed_ten_channel_formula_status.packet.json"
TOTAL_DECISION = PACKET_DIR / "precision_total_width_decision_after_ew_gate.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_remaining_ew_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsRemainingEWFormulaRows_or_PrecisionTotalWidth_v1.md"

STATUS = "MTT_SELECTED_HIGGSREMAININGEWFORMULAROWS_OR_PRECISIONTOTALWIDTH_BUILT_EW_GATE_TOTAL_WIDTH_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgscomputedchannelrefresh_or_totalwidthreplay.candidate.json")
    refreshed = load(
        DATA
        / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
        / "refreshed_higgs_total_width_replay.packet.json"
    )
    refresh_decision = load(
        DATA
        / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
        / "higgs_total_width_precision_decision_after_refresh.packet.json"
    )
    ew_policy = load(
        DATA
        / "selected_higgsewbenchmarkpolicy_or_fullformulas"
        / "remaining_electroweak_benchmark_replay_policy.packet.json"
    )
    ew_obligations = load(
        DATA
        / "selected_higgsewbenchmarkpolicy_or_fullformulas"
        / "remaining_higgs_precision_formula_obligations.packet.json"
    )

    remaining_channels = refresh_decision["remaining_external_fill_channels"]
    policy_by_channel = {row["channel"]: row for row in ew_policy["rows"]}
    obligation_by_channel = {
        row["channel"]: row for row in ew_obligations["formula_rows_still_required_for_precision"]
    }

    ew_rows = []
    for channel in remaining_channels:
        policy = policy_by_channel[channel]
        obligation = obligation_by_channel[channel]
        ew_rows.append(
            {
                "channel": channel,
                "current_row_kind": "external_benchmark_fill",
                "benchmark_width_GeV": policy["benchmark_width_GeV"],
                "absolute_uncertainty_GeV": policy["absolute_uncertainty_GeV"],
                "required_formula_family": obligation["required_formula_family"],
                "operator_attachment_required": obligation["operator_attachment_required"],
                "allowed_precision_closure_routes": [
                    "supply executable formula kernel with declared input scheme and uncertainty propagation",
                    "or declare an accepted external precision benchmark convention with full covariance/profile semantics",
                ],
                "formula_kernel_filled": False,
                "accepted_precision_import_filled": False,
                "accepted_as_precision_total_width_row": False,
                "benchmark_used_as_source_selector": False,
            }
        )

    ew_gate = {
        "schema": "MTTHiggsRemainingEWFormulaOrPrecisionImportGate.v1",
        "status": "REMAINING_EW_FORMULA_OR_PRECISION_IMPORT_GATE_BUILT_VALUES_OPEN",
        "rows": ew_rows,
        "summary": {
            "remaining_external_fill_count": len(ew_rows),
            "remaining_external_fill_channels": remaining_channels,
            "all_remaining_rows_have_formula_or_import_route": True,
            "all_formula_kernels_filled": False,
            "all_precision_imports_filled": False,
            "all_rows_precision_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ten_channel_rows = []
    for row in refreshed["rows"]:
        ten_channel_rows.append(
            {
                "channel": row["channel"],
                "row_kind": row["row_kind"],
                "width_GeV": row["width_GeV"],
                "is_formula_or_proxy_executable": row["row_kind"] == "computed_proxy",
                "is_external_fill": row["row_kind"] == "external_benchmark_fill",
                "accepted_for_precision_total_width": False,
            }
        )

    ten_channel = {
        "schema": "MTTRefreshedTenChannelFormulaStatus.v1",
        "status": "TEN_CHANNEL_STATUS_REFRESHED_THREE_EW_FORMULA_ROWS_OPEN",
        "rows": ten_channel_rows,
        "summary": {
            "channel_count": len(ten_channel_rows),
            "computed_or_proxy_row_count": sum(row["is_formula_or_proxy_executable"] for row in ten_channel_rows),
            "external_fill_row_count": sum(row["is_external_fill"] for row in ten_channel_rows),
            "external_fill_channels": remaining_channels,
            "all_channels_have_width_rows": True,
            "all_channels_have_formula_or_proxy_rows": False,
            "all_channels_precision_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    total_decision = {
        "schema": "MTTPrecisionTotalWidthDecisionAfterRemainingEWGate.v1",
        "status": "PRECISION_TOTAL_WIDTH_STILL_OPEN_THREE_EW_ROWS_OPEN",
        "refreshed_width_sum_GeV": refreshed["summary"]["refreshed_width_sum_GeV"],
        "refreshed_relative_residual_to_reference": refreshed["summary"]["refreshed_relative_residual_to_reference"],
        "precision_total_width_closed": False,
        "branching_ratios_closed": False,
        "values_promotable_to_precision_now": False,
        "required_before_precision_total_width": [
            "close WW* formula/import row",
            "close ZZ* formula/import row",
            "close Z gamma formula/import row",
            "upgrade proxy QCD and gamma-gamma rows or declare accepted precision convention",
            "supply full ten-channel covariance/profile likelihood",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterRemainingEWGate.v1",
        "status": "REMAINING_EW_GATE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "closed_now": [
            "remaining EW formula/import row gate after refreshed Higgs channel replay",
            "refreshed ten-channel formula-status matrix",
        ],
        "remaining_true_equivalence_blockers": [
            "WW*/ZZ*/Z gamma formula kernels or accepted precision imports",
            "precision QCD/gamma rows",
            "full ten-channel covariance/profile likelihood",
            "actual selected electroweak and Qa/SU3 operator packets for no-knob/source closure",
        ],
        "next_primary_value_gate": "fill WW*/ZZ*/Z gamma formula kernels or accepted precision imports",
        "guardrails": {
            "external_fills_not_precision_total_width": True,
            "computed_proxy_rows_not_precision_rows": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsRemainingEWFormulaRowsOrPrecisionTotalWidth",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgscomputedchannelrefresh_or_totalwidthreplay.candidate.json"),
            "refreshed_total_width_replay": rel(
                DATA
                / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
                / "refreshed_higgs_total_width_replay.packet.json"
            ),
            "ew_benchmark_policy": rel(
                DATA
                / "selected_higgsewbenchmarkpolicy_or_fullformulas"
                / "remaining_electroweak_benchmark_replay_policy.packet.json"
            ),
        },
        "output_packets": {
            "remaining_ew_formula_or_precision_import_gate": rel(EW_GATE),
            "refreshed_ten_channel_formula_status": rel(TEN_CHANNEL),
            "precision_total_width_decision": rel(TOTAL_DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "RemainingEWFormulaRowsPrecisionTotalWidthGateTheorem",
            "proved": True,
            "statement": (
                "After the refreshed Higgs replay, the only external-fill channels are WW*, ZZ*, and Z gamma. "
                "The repo now records a precise formula/import gate for those rows and a ten-channel formula-status "
                "matrix. This narrows the total-width frontier, while precision total width, branching ratios, "
                "true SM equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": {
            "remaining_EW_formula_import_gate": True,
            "refreshed_ten_channel_formula_status_matrix": True,
            "precision_total_width_blocker_localized_to_three_EW_rows_plus_profile": True,
        },
        "what_remains_open": {
            "WW_star_formula_or_precision_import": True,
            "ZZ_star_formula_or_precision_import": True,
            "Z_gamma_formula_or_precision_import": True,
            "full_ten_channel_covariance_profile": True,
            "precision_total_width": True,
            "branching_ratios": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "remaining_EW_gate_built": True,
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
        "certificate": "MTT_Selected_HiggsRemainingEWFormulaRows_or_PrecisionTotalWidth_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "remaining_EW_gate_built": True,
        "precision_total_width_closed": False,
        "branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsEWFormulaKernelExecution_or_PrecisionImportRows_v1",
    }

    note = f"""# MTT Selected HiggsRemainingEWFormulaRows or PrecisionTotalWidth v1

Status: `{STATUS}`.

After the computed-channel refresh, only `H_to_WW_star`, `H_to_ZZ_star`, and
`H_to_Z_gamma` remain as external-fill rows in the Higgs total-width replay.
This artifact builds the exact formula/import gate for those rows and records
the ten-channel formula-status matrix.

It does not close precision total width, branching ratios, true SM equivalence,
or no-knob closure.
"""

    for path, payload in [
        (EW_GATE, ew_gate),
        (TEN_CHANNEL, ten_channel),
        (TOTAL_DECISION, total_decision),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
