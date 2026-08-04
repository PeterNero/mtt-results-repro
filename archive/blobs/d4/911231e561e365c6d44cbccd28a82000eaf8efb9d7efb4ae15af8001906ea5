"""Audit full-SM minimal-parameter ledger or strict P_EW source theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SECTOR_LEDGER = PACKET_DIR / "sm_sector_minimal_parameter_ledger.packet.json"
COUNT_SUMMARY = PACKET_DIR / "minimal_parameter_count_summary.packet.json"
SLOT_BOUNDARY = PACKET_DIR / "closed_vs_open_parameter_slots.packet.json"
STRICT_PEW_CONTRACT = PACKET_DIR / "strict_pew_source_reentry_contract.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_fullsm_minimal_parameter_ledger.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FULLSMMINIMALPARAMETERLEDGER_OR_STRICTPEWSOURCETHEOREM_"
    "LEDGER_CLOSED_STRICT_PEW_AND_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_StrictPEWSourceTheorem_or_SMPrecisionClosureCutset_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    sector = load(SECTOR_LEDGER)
    counts = load(COUNT_SUMMARY)
    boundary = load(SLOT_BOUNDARY)
    strict = load(STRICT_PEW_CONTRACT)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("sector", sector),
        ("counts", counts),
        ("boundary", boundary),
        ("strict", strict),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")

    decision = data["closure_decision"]
    require(decision["minimal_parameter_ledger_closed"] is True, "ledger closed")
    require(decision["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "non-neutrino count")
    require(decision["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "PMNS count")
    require(decision["H_specific_parameter_count"] == 0, "H-specific count")
    require(decision["P_EW_counted_as_shared_physical_primitive"] is True, "P_EW counted")
    require(decision["P_EW_parameter_count"] == 1, "P_EW count")
    require(decision["lambda_H_independent_parameter_replaced"] is True, "lambda replaced")
    require(decision["gauge_triplet_counted_as_measured_replay"] == 3, "gauge count")
    require(decision["charged_yukawa_counted_as_measured_replay"] == 9, "Yukawa count")
    require(decision["CKM_counted_as_measured_replay"] == 4, "CKM count")
    require(decision["PMNS_oscillation_counted_as_minimal_policy"] == 6, "PMNS count detail")
    require(decision["QCD_theta_bar_closed"] is False, "QCD theta overclaim")
    require(decision["absolute_neutrino_mass_closed"] is False, "absolute nu overclaim")
    require(decision["strict_P_EW_source_closed"] is False, "strict P_EW overclaim")
    require(decision["true_precision_equivalence_closed"] is False, "precision overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    summary_counts = counts["counts"]
    require(summary_counts["electroweak_scale_anchor_v_or_G_F"] == 1, "scale count")
    require(summary_counts["common_scale_gauge_triplet_alpha1_alpha2_alpha3"] == 3, "summary gauge")
    require(summary_counts["charged_fermion_yukawa_magnitudes"] == 9, "summary Yukawa")
    require(summary_counts["CKM_physical_mixing_parameters"] == 4, "summary CKM")
    require(summary_counts["H_lambda_shared_physical_prefactor_P_EW"] == 1, "summary P_EW")
    require(summary_counts["PMNS_minimal_oscillation_policy"] == 6, "summary PMNS")
    require(counts["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "summary non-nu")
    require(counts["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "summary with PMNS")
    require(counts["interpretation"]["full_no_knob_closed"] is False, "summary no-knob overclaim")

    h_lane = sector["sector_rows"]["H_lambda"]
    require(h_lane["H_specific_free_parameters"] == 0, "H lane H count")
    require(h_lane["counted_parameters"] == 1, "H lane P_EW count")
    require(h_lane["lambda_H_used_as_selector"] is False, "lambda selector")
    require(h_lane["strict_P_EW_source_closed"] is False, "strict H lane overclaim")

    require(strict["current_strict_P_EW_source_rows"] == 0, "strict current rows")
    require(strict["strict_P_EW_source_closed"] is False, "strict contract overclaim")
    require(strict["strict_upgrade_would_reduce_count_by"] == 1, "strict count reduction")

    guardrails = boundary["guardrails"]
    require(all(guardrails.values()), "guardrails")
    for item in [
        "QCD theta_bar / strong-CP policy",
        "absolute neutrino mass scale",
        "full correlated covariance/profile likelihood",
        "full no-knob derivation of gauge/Yukawa/Higgs values",
    ]:
        require(item in boundary["open_slots_or_upgrade_targets"], f"missing open slot {item}")

    require(cert["full_SM_minimal_parameter_ledger_closed"] is True, "cert ledger")
    require(cert["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "cert non-nu")
    require(cert["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "cert PMNS")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "FullSMMinimalParameterLedgerOrStrictPEWSourceTheorem",
        "non-neutrino SM-like count excluding QCD theta_bar = 18",
        "minimal PMNS oscillation extension excluding QCD theta_bar = 24",
        "H-specific lambda parameters = 0",
        "P_EW shared physical primitive count = 1",
        "lambda_H used as selector = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: full-SM minimal-parameter ledger built; 18 non-neutrino "
        "slots excluding QCD theta and 24 with minimal PMNS oscillation policy; "
        "strict P_EW, true precision equivalence, and no-knob closure remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
