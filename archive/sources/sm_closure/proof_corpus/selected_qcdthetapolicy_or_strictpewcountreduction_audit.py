"""Audit QCD theta policy or strict P_EW count reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qcdthetapolicy_or_strictpewcountreduction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QCD_POLICY = PACKET_DIR / "qcd_theta_policy.packet.json"
COUNT_UPDATE = PACKET_DIR / "sm_count_with_qcd_theta_update.packet.json"
NO_KNOB_GATE = PACKET_DIR / "strong_cp_noknob_gate.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_qcd_theta_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QCDThetaPolicy_or_StrictPEWCountReduction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_QCDTHETAPOLICY_OR_STRICTPEWCOUNTREDUCTION_"
    "QCD_THETA_SLOT_ADMITTED_STRICT_PEW_OPEN"
)
NEXT = "MTT_Selected_NeutrinoMassMajoranaPolicy_or_PrecisionProfileTable_v1"


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
    policy = load(QCD_POLICY)
    counts = load(COUNT_UPDATE)
    gate = load(NO_KNOB_GATE)
    next_target = load(NEXT_TARGET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("policy", policy),
        ("counts", counts),
        ("gate", gate),
        ("next", next_target),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_target["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "QCDThetaPolicyOrStrictPEWCountReductionTheorem", "name")

    decision = data["closure_decision"]
    require(decision["QCD_theta_bar_policy_closed"] is True, "QCD policy")
    require(decision["QCD_theta_bar_admitted_parameter_slot"] is True, "QCD admitted")
    require(decision["QCD_theta_bar_slot_count"] == 1, "QCD count")
    require(decision["theta_bar_value_selected_by_MTT"] is False, "theta value overclaim")
    require(decision["theta_bar_zero_predicted"] is False, "theta zero overclaim")
    require(decision["strong_CP_problem_solved"] is False, "strong CP overclaim")
    require(decision["strict_P_EW_source_theorem_closed"] is False, "strict PEW overclaim")
    require(decision["strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(decision["P_EW_count_reduction_available_now"] is False, "strict reduction overclaim")
    require(decision["non_neutrino_count_including_QCD_theta"] == 19, "non-neutrino QCD count")
    require(decision["minimal_PMNS_count_including_QCD_theta"] == 25, "PMNS QCD count")
    require(decision["non_neutrino_count_if_strict_P_EW_closes_including_QCD_theta"] == 18, "strict non-nu")
    require(decision["minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta"] == 24, "strict PMNS")
    require(decision["absolute_neutrino_majorana_policy_closed"] is False, "nu policy overclaim")
    require(decision["precision_profile_closure_closed"] is False, "precision overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    require(policy["policy_closed"] is True, "policy packet")
    require(policy["slot_count"] == 1, "policy count")
    require(policy["theta_bar_value_selected_by_MTT"] is False, "policy value overclaim")
    require(policy["theta_bar_zero_predicted"] is False, "policy zero overclaim")
    require(policy["strong_CP_problem_solved"] is False, "policy strong CP overclaim")

    require(counts["counts_excluding_QCD_theta"]["non_neutrino"] == 18, "excluding non-nu")
    require(counts["counts_excluding_QCD_theta"]["minimal_PMNS"] == 24, "excluding PMNS")
    require(counts["counts_including_QCD_theta"]["non_neutrino"] == 19, "including non-nu")
    require(counts["counts_including_QCD_theta"]["minimal_PMNS"] == 25, "including PMNS")
    require(counts["counts_including_QCD_theta"]["if_strict_P_EW_closes_non_neutrino"] == 18, "strict non-nu")
    require(counts["counts_including_QCD_theta"]["if_strict_P_EW_closes_minimal_PMNS"] == 24, "strict PMNS")

    require(gate["source_gate_closed"] is False, "source gate overclaim")
    require(gate["policy_gate_closed"] is True, "policy gate")
    require(gate["accepted_theta_bar_source_values"] == 0, "source values")
    require(gate["accepted_theta_bar_cancellation_theorems"] == 0, "cancellation")

    require(cert["QCD_theta_bar_policy_closed"] is True, "cert policy")
    require(cert["theta_bar_value_selected_by_MTT"] is False, "cert value overclaim")
    require(cert["theta_bar_zero_predicted"] is False, "cert zero overclaim")
    require(cert["strong_CP_problem_solved"] is False, "cert strong CP overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "QCDThetaPolicyOrStrictPEWCountReductionTheorem",
        "QCD theta_bar policy closed = true",
        "theta_bar zero predicted = false",
        "strong CP problem solved = false",
        "non-neutrino count including QCD theta_bar = 19",
        "minimal PMNS count including QCD theta_bar = 25",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: QCD theta_bar policy slot admitted; counts are 19/25 "
        "including QCD theta; theta value, theta=0, strong CP, strict P_EW, "
        "true equivalence, and no-knob closure remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
