"""Build a complete Higgs channel ledger and total-width policy gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_completehiggschannelledger_or_totalwidthpolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEDGER = PACKET_DIR / "complete_higgs_channel_status_ledger.packet.json"
PARTIAL = PACKET_DIR / "currently_computed_higgs_partial_width_sum.packet.json"
POLICY = PACKET_DIR / "total_width_branching_policy_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_channel_ledger.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CompleteHiggsChannelLedger_or_TotalWidthPolicy_v1.md"

STATUS = "MTT_SELECTED_COMPLETEHIGGSCHANNELLEDGER_OR_TOTALWIDTHPOLICY_BUILT_LEDGER_TOTAL_WIDTH_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy.candidate.json")
    previous_gate = load(
        DATA
        / "selected_multiloophiggsqqformula_or_fullwidthpolicy"
        / "updated_true_equivalence_gate_after_multiloop_qq_formula.packet.json"
    )
    qq = load(
        DATA
        / "selected_multiloophiggsqqformula_or_fullwidthpolicy"
        / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
    )
    tree_decays = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )

    qq_widths = {
        row["fermion"]: row["stage_widths_GeV"]["N3LO"]
        for row in qq["rows"]
    }
    lepton_tree = {
        row["fermion"]: row["width_GeV"]
        for row in tree_decays["higgs_fermion_decay_rows"]
        if row["fermion"] in {"tau", "mu"}
    }

    channel_rows = [
        {
            "channel": "H_to_bb",
            "status": "COMPUTED_N3LO_MASSLESS_QCD_PROXY_NOT_PRECISION",
            "width_GeV": qq_widths["b"],
            "source_packet": rel(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy" / "n3lo_qcd_higgs_qq_proxy_values.packet.json"),
            "accepted_for_total_width_precision": False,
        },
        {
            "channel": "H_to_cc",
            "status": "COMPUTED_N3LO_MASSLESS_QCD_PROXY_NOT_PRECISION",
            "width_GeV": qq_widths["c"],
            "source_packet": rel(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy" / "n3lo_qcd_higgs_qq_proxy_values.packet.json"),
            "accepted_for_total_width_precision": False,
        },
        {
            "channel": "H_to_tau_tau",
            "status": "COMPUTED_TREE_LEPTONIC_PROXY_NOT_PRECISION",
            "width_GeV": lepton_tree["tau"],
            "source_packet": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "accepted_for_total_width_precision": False,
        },
        {
            "channel": "H_to_mu_mu",
            "status": "COMPUTED_TREE_LEPTONIC_PROXY_NOT_PRECISION",
            "width_GeV": lepton_tree["mu"],
            "source_packet": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "accepted_for_total_width_precision": False,
        },
    ]
    placeholder_channels = [
        ("H_to_WW_star", "off-shell vector-boson formula and EW corrections required"),
        ("H_to_ZZ_star", "off-shell vector-boson formula and EW corrections required"),
        ("H_to_gg", "loop-induced gluonic width and higher-order QCD required"),
        ("H_to_gamma_gamma", "loop-induced photonic width and EW/QCD corrections required"),
        ("H_to_Z_gamma", "loop-induced mixed electroweak width required"),
        ("H_to_ss", "running strange mass and QCD correction policy required"),
    ]
    for channel, requirement in placeholder_channels:
        channel_rows.append(
            {
                "channel": channel,
                "status": "BENCHMARK_OR_FORMULA_REQUIRED_NOT_COMPUTED",
                "width_GeV": None,
                "missing_requirement": requirement,
                "accepted_for_total_width_precision": False,
            }
        )

    computed_sum = sum(row["width_GeV"] for row in channel_rows if row["width_GeV"] is not None)
    reference_total = 0.00407
    ledger = {
        "schema": "MTTCompleteHiggsChannelStatusLedger.v1",
        "status": "COMPLETE_HIGGS_CHANNEL_LEDGER_BUILT_VALUES_PARTIAL",
        "channels": channel_rows,
        "summary": {
            "channel_count": len(channel_rows),
            "computed_proxy_channel_count": sum(row["width_GeV"] is not None for row in channel_rows),
            "placeholder_channel_count": sum(row["width_GeV"] is None for row in channel_rows),
            "all_major_channels_classified": True,
            "all_computed_channels_precision_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    partial_sum = {
        "schema": "MTTCurrentlyComputedHiggsPartialWidthSum.v1",
        "status": "PARTIAL_PROXY_WIDTH_SUM_BUILT_NOT_TOTAL_WIDTH",
        "computed_proxy_width_sum_GeV": computed_sum,
        "reference_total_width_GeV": reference_total,
        "fraction_of_reference_total_width": computed_sum / reference_total,
        "computed_channels": [row["channel"] for row in channel_rows if row["width_GeV"] is not None],
        "missing_channels": [row["channel"] for row in channel_rows if row["width_GeV"] is None],
        "accepted_as_total_width": False,
        "why_not_total_width": (
            "The sum omits vector-boson, gluon, photon, Z-gamma, strange, and precision correction policies. "
            "It is a bookkeeping partial sum only."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    policy = {
        "schema": "MTTTotalWidthBranchingPolicyGate.v1",
        "status": "TOTAL_WIDTH_BRANCHING_POLICY_GATE_BUILT_VALUES_OPEN",
        "policy_requirements": [
            "every major Higgs decay channel must have a formula row or accepted external benchmark row",
            "all partial widths must share the same mass, scheme, scale, and correction convention",
            "uncertainties/covariances must propagate to total width and branching ratios",
            "benchmark rows may be downstream replay inputs but cannot select source data",
            "source-sensitive rows must attach to the actual selected Qa/SU3 packet",
        ],
        "current_acceptance": {
            "channel_ledger_complete": True,
            "partial_width_values_complete": False,
            "total_width_value_complete": False,
            "branching_ratio_values_complete": False,
            "precision_promotion_accepted": False,
        },
        "next_value_targets": [
            "H_to_WW_star width row",
            "H_to_ZZ_star width row",
            "H_to_gg width row",
            "H_to_gamma_gamma width row",
            "H_to_Z_gamma width row",
            "H_to_ss width row",
            "uncertainty/covariance sidecar",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["complete Higgs channel status ledger"]
    if "complete Higgs partial-width channel formula set" in remaining:
        remaining.remove("complete Higgs partial-width channel formula set")
    for blocker in [
        "computed values for missing Higgs channels",
        "full Higgs total-width and branching-ratio policy",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterChannelLedger.v1",
        "status": "COMPLETE_CHANNEL_LEDGER_BUILT_TOTAL_WIDTH_VALUES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "compute or import missing Higgs channels under the total-width policy",
        "guardrails": {
            "channel_ledger_not_total_width": True,
            "partial_proxy_sum_not_precision_width": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCompleteHiggsChannelLedgerOrTotalWidthPolicy",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy.candidate.json"),
            "n3lo_qq_proxy_values": rel(
                DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy" / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
            ),
            "tree_decay_rows": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
        },
        "output_packets": {
            "complete_higgs_channel_status_ledger": rel(LEDGER),
            "currently_computed_higgs_partial_width_sum": rel(PARTIAL),
            "total_width_branching_policy_gate": rel(POLICY),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "CompleteHiggsChannelLedgerTheorem",
            "proved": True,
            "statement": (
                "The repo now classifies the major Higgs partial-width channels, identifies computed proxy rows and "
                "missing formula/benchmark rows, and constructs a total-width/branching-policy gate. This closes the "
                "channel-status ledger, not the total Higgs width or precision SM-equivalence."
            ),
        },
        "what_closes_now": {
            "complete_Higgs_channel_status_ledger": True,
            "computed_partial_proxy_sum": True,
            "total_width_branching_policy_gate": True,
        },
        "what_remains_open": {
            "missing_Higgs_channel_values": True,
            "total_width_and_branching_ratios": True,
            "covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "channel_ledger_closed": True,
            "total_Higgs_width_closed": False,
            "branching_ratios_closed": False,
            "full_precision_QFT_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_CompleteHiggsChannelLedger_or_TotalWidthPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "channel_ledger_closed": True,
        "total_Higgs_width_closed": False,
        "branching_ratios_closed": False,
        "full_precision_QFT_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsMissingChannelValues_or_TotalWidthReplay_v1",
    }

    note = """# MTT Selected CompleteHiggsChannelLedger or TotalWidthPolicy v1

Status: `MTT_SELECTED_COMPLETEHIGGSCHANNELLEDGER_OR_TOTALWIDTHPOLICY_BUILT_LEDGER_TOTAL_WIDTH_OPEN`.

This artifact classifies the major Higgs partial-width channels. Current
computed rows are proxy-level `H->bb`, `H->cc`, `H->tau tau`, and `H->mu mu`.
The vector-boson, gluon, photon, Z-gamma, and strange channels are explicitly
marked as missing formula/benchmark rows.

The computed partial sum is bookkeeping only. It is not a total Higgs width and
not a precision SM-equivalence claim.
"""

    for path, payload in [
        (LEDGER, ledger),
        (PARTIAL, partial_sum),
        (POLICY, policy),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
