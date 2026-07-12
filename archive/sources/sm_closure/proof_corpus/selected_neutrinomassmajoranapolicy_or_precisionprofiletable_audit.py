"""Audit neutrino mass/Majorana policy or precision profile table."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutrinomassmajoranapolicy_or_precisionprofiletable"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NEUTRINO_POLICY = PACKET_DIR / "neutrino_mass_majorana_policy.packet.json"
COUNT_TIERS = PACKET_DIR / "sm_neutrino_count_tiers.packet.json"
SOURCE_GATE = PACKET_DIR / "neutrino_noknob_source_gate.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_neutrino_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutrinoMassMajoranaPolicy_or_PrecisionProfileTable_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_NEUTRINOMASSMAJORANAPOLICY_OR_PRECISIONPROFILETABLE_"
    "TIERED_NEUTRINO_LEDGER_CLOSED_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_PrecisionProfileTable_or_TrueSMEquivalenceAudit_v1"


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
    policy = load(NEUTRINO_POLICY)
    counts = load(COUNT_TIERS)
    gate = load(SOURCE_GATE)
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
    require(data["theorem"]["name"] == "NeutrinoMassMajoranaPolicyOrPrecisionProfileTableTheorem", "name")

    decision = data["closure_decision"]
    require(decision["neutrino_policy_gate_closed"] is True, "neutrino policy")
    require(decision["minimal_PMNS_oscillation_policy_closed"] is True, "minimal PMNS")
    require(decision["absolute_neutrino_mass_closed"] is False, "absolute mass overclaim")
    require(decision["Dirac_neutrino_yukawa_magnitudes_closed"] is False, "Dirac Yukawa overclaim")
    require(decision["Majorana_policy_selected"] is False, "Majorana selection overclaim")
    require(decision["Majorana_phases_closed"] is False, "Majorana phase overclaim")
    require(decision["neutrino_no_knob_mass_closure"] is False, "neutrino no-knob overclaim")
    require(decision["minimal_PMNS_count_including_QCD_theta"] == 25, "minimal count")
    require(decision["Dirac_massive_neutrino_count_including_QCD_theta"] == 26, "Dirac count")
    require(decision["Majorana_massive_neutrino_count_including_QCD_theta"] == 28, "Majorana count")
    require(decision["minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta"] == 24, "strict minimal")
    require(decision["Dirac_count_if_strict_P_EW_closes_including_QCD_theta"] == 25, "strict Dirac")
    require(decision["Majorana_count_if_strict_P_EW_closes_including_QCD_theta"] == 27, "strict Majorana")
    require(decision["strict_P_EW_source_theorem_closed"] is False, "strict P_EW overclaim")
    require(decision["precision_profile_closure_closed"] is False, "precision overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    require(policy["policy_closed"] is True, "policy packet")
    require(policy["minimal_oscillation_replay_closed"] is True, "policy minimal")
    require(policy["minimal_oscillation_slots"] == 6, "minimal slots")
    require(policy["absolute_neutrino_mass_filled"] is False, "absolute filled overclaim")
    require(policy["Dirac_neutrino_yukawa_magnitudes_filled"] is False, "Dirac filled overclaim")
    require(policy["Dirac_policy_selected"] is False, "Dirac policy overclaim")
    require(policy["Majorana_policy_selected"] is False, "Majorana policy overclaim")
    require(policy["absolute_mass_value_selected_by_MTT"] is False, "absolute source overclaim")
    require(policy["Majorana_phases_selected_by_MTT"] is False, "Majorana source overclaim")

    tier_counts = counts["counts_including_QCD_theta"]
    require(tier_counts["minimal_PMNS_oscillation_policy"] == 25, "tier minimal")
    require(tier_counts["Dirac_massive_neutrino_completion"] == 26, "tier Dirac")
    require(tier_counts["Majorana_massive_neutrino_completion"] == 28, "tier Majorana")
    require(tier_counts["minimal_PMNS_if_strict_P_EW_closes"] == 24, "tier strict minimal")
    require(tier_counts["Dirac_completion_if_strict_P_EW_closes"] == 25, "tier strict Dirac")
    require(tier_counts["Majorana_completion_if_strict_P_EW_closes"] == 27, "tier strict Majorana")

    require(gate["source_gate_closed"] is False, "source gate overclaim")
    require(gate["policy_gate_closed"] is True, "policy gate")
    require(gate["accepted_absolute_mass_source_values"] == 0, "absolute source rows")
    require(gate["accepted_Dirac_Yukawa_source_rows"] == 0, "Dirac source rows")
    require(gate["accepted_Majorana_mass_operator_rows"] == 0, "Majorana operator rows")
    require(gate["accepted_Majorana_phase_source_rows"] == 0, "Majorana phase rows")
    require(gate["accepted_neutrino_ontology_selectors"] == 0, "ontology selector rows")

    require(cert["neutrino_policy_gate_closed"] is True, "cert policy")
    require(cert["absolute_neutrino_mass_closed"] is False, "cert absolute overclaim")
    require(cert["Majorana_policy_selected"] is False, "cert Majorana overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "NeutrinoMassMajoranaPolicyOrPrecisionProfileTableTheorem",
        "minimal PMNS count including QCD theta_bar = 25",
        "Dirac massive-neutrino count including QCD theta_bar = 26",
        "Majorana massive-neutrino count including QCD theta_bar = 28",
        "absolute neutrino mass closed = false",
        "Majorana policy selected = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: neutrino policy tiered ledger closed; counts are 25 minimal "
        "PMNS, 26 conditional Dirac, 28 conditional Majorana including QCD theta; "
        "absolute mass, Majorana policy, source values, true equivalence, and "
        "no-knob closure remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
