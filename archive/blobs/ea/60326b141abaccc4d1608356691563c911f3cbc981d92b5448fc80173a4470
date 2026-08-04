"""Audit precision-equivalence rows / true-SM closure after PEW promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionequivalencerows_or_truesmclosureaudit"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "post_pew_true_sm_precision_ledger.packet.json"
ROWS = PACKET_DIR / "precision_equivalence_row_status_table.packet.json"
CUTSET = PACKET_DIR / "remaining_true_sm_cutset_after_pew.packet.json"
NEXT = PACKET_DIR / "next_precision_execution_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionEquivalenceRows_or_TrueSMClosureAudit_v1.md"

STATUS = (
    "MTT_SELECTED_PRECISIONEQUIVALENCEROWS_OR_TRUESMCLOSUREAUDIT_"
    "POST_PEW_LEDGER_REBUILT_PRECISION_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    ledger = load(LEDGER)
    rows = load(ROWS)
    cutset = load(CUTSET)
    next_packet = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("ledger", ledger),
        ("rows", rows),
        ("cutset", cutset),
        ("next", next_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "PrecisionEquivalenceRowsOrTrueSMClosureAuditTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next packet")

    strict = ledger["strict_core"]
    require(strict["accepted_global_strict_P_EW_source_rows"] == 1, "strict P_EW not closed")
    require(strict["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 1, "direct K not closed")
    require(strict["strict_zero_primitive_K_threshold_row_count"] == 10, "strict K count")
    require(strict["strict_PEW_directK_blocker_closed"] is True, "PEW blocker not closed")
    stale = ledger["stale_fields_superseded"]
    require(stale["old_precision_strict_P_EW_source_theorem_closed"] is False, "old precision stale missing")
    require(stale["old_qcd_strict_P_EW_source_rows"] == 0, "old qcd stale missing")
    require(stale["old_neutrino_strict_P_EW_source_theorem_closed"] is False, "old neutrino stale missing")

    counts = ledger["parameter_counts_after_strict_PEW"]
    require(counts["non_neutrino_including_QCD_theta"] == 18, "non-neutrino count")
    require(counts["minimal_PMNS_including_QCD_theta"] == 24, "minimal PMNS count")
    require(counts["Dirac_massive_neutrino_including_QCD_theta"] == 25, "Dirac count")
    require(counts["Majorana_massive_neutrino_including_QCD_theta"] == 27, "Majorana count")

    require(rows["status"] == "ROW_STATUS_TABLE_REBUILT_AFTER_PEW", "rows status")
    require(rows["blocking_true_precision_row_count"] == 8, "blocking row count")
    require(rows["accepted_true_equivalence_precision_rows"] == 0, "accepted precision overclaim")
    table = {row["row_class"]: row for row in rows["rows"]}
    require(table["core_matrix_yukawa_higgs_pew_directk"]["closed"] is True, "core not closed")
    require(table["threshold_mass_scheme_source_rows"]["closed"] is False, "threshold overclosed")
    require(table["full_covariance_profile_likelihood"]["closed"] is False, "covariance overclosed")
    require(table["multi_loop_rg_transport_values"]["closed"] is False, "RG overclosed")
    require(table["local_qft_precision_observables"]["closed"] is False, "QFT overclosed")
    require(table["selected_qasu3_operator_packet"]["closed"] is False, "QaSU3 overclosed")
    require(table["neutrino_absolute_majorana_policy"]["closed"] is False, "neutrino overclosed")
    require(table["qcd_theta_strong_cp"]["closed"] is False, "QCD overclosed")

    require(cutset["status"] == "TRUE_SM_PRECISION_CUTSET_AFTER_PEW", "cutset status")
    require(len(cutset["remaining_blockers_ordered"]) == 7, "cutset blocker count")
    require(len(cutset["non_blockers_now"]) == 5, "non-blocker count")
    require("strict P_EW source row" in cutset["non_blockers_now"], "PEW not non-blocker")

    decision = candidate["closure_decision"]
    require(decision["post_PEW_precision_ledger_rebuilt"] is True, "decision rebuilt")
    require(decision["strict_PEW_directK_blocker_closed"] is True, "decision PEW")
    require(decision["accepted_global_strict_P_EW_source_rows"] == 1, "decision P_EW")
    require(decision["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 1, "decision K")
    require(decision["strict_zero_primitive_K_threshold_row_count"] == 10, "decision ten K")
    require(decision["precision_policy_rows_closed"] is True, "precision policy")
    require(decision["central_value_replay_baseline_closed"] is True, "central replay")
    require(decision["minimal_PMNS_oscillation_policy_closed"] is True, "PMNS policy")
    require(decision["QCD_theta_bar_policy_closed"] is True, "QCD policy")
    require(decision["local_QFT_tree_identity_observable_rows_closed"] is True, "tree QFT")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "true rows overclaim")
    require(decision["blocking_true_precision_row_count"] == 8, "decision blocking")
    for key in [
        "threshold_mass_scheme_source_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "multi_loop_RG_values_closed",
        "local_QFT_precision_observable_table_closed",
        "selected_QaSU3_operator_payload_closed",
        "neutrino_absolute_source_closed",
        "strong_CP_problem_solved",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    require(len(next_packet["recommended_next_steps"]) == 5, "next step count")

    for phrase in [
        "strict P_EW source rows              = 1",
        "strict direct K_threshold.Omega_H    = 1",
        "strict zero-primitive K ledger       = 10/10",
        "Accepted true-equivalence precision rows remain `0`",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
