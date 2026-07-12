"""Audit strict P_EW source theorem or SM precision closure cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_RECHECK = PACKET_DIR / "strict_pew_count_reduction_recheck.packet.json"
CUTSET_ORDER = PACKET_DIR / "precision_closure_cutset_order.packet.json"
COUNT_FRONTIER = PACKET_DIR / "sm_parameter_count_frontier.packet.json"
NEXT_TARGET = PACKET_DIR / "next_executable_target.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWSourceTheorem_or_SMPrecisionClosureCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STRICTPEWSOURCETHEOREM_OR_SMPRECISIONCLOSURECUTSET_"
    "STRICT_PEW_OPEN_CUTSET_ORDER_LOCKED"
)
NEXT = "MTT_Selected_QCDThetaPolicy_or_StrictPEWCountReduction_v1"


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
    strict = load(STRICT_RECHECK)
    cutset = load(CUTSET_ORDER)
    frontier = load(COUNT_FRONTIER)
    next_target = load(NEXT_TARGET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("cutset", cutset),
        ("frontier", frontier),
        ("next", next_target),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_target["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "StrictPEWSourceTheoremOrSMPrecisionClosureCutsetTheorem", "name")

    decision = data["closure_decision"]
    require(decision["strict_P_EW_source_theorem_closed"] is False, "strict P_EW overclaim")
    require(decision["strict_P_EW_source_rows"] == 0, "strict source rows")
    require(decision["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(decision["P_EW_count_reduction_available_now"] is False, "count reduction overclaim")
    require(decision["P_EW_count_reduction_if_closed"] == 1, "count reduction size")
    require(decision["non_neutrino_count_current_excluding_QCD_theta"] == 18, "current non-neutrino")
    require(decision["non_neutrino_count_if_strict_P_EW_closes"] == 17, "conditional non-neutrino")
    require(decision["PMNS_extension_count_current_excluding_QCD_theta"] == 24, "current PMNS")
    require(decision["PMNS_extension_count_if_strict_P_EW_closes"] == 23, "conditional PMNS")
    require(decision["QCD_theta_bar_policy_closed"] is False, "QCD theta overclaim")
    require(decision["absolute_neutrino_majorana_policy_closed"] is False, "nu policy overclaim")
    require(decision["precision_profile_closure_closed"] is False, "precision overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    require(strict["current_strict_P_EW_source_rows"] == 0, "strict packet rows")
    require(strict["strict_P_EW_source_theorem_closed"] is False, "strict packet overclaim")
    require(strict["P_EW_count_reduction_available_now"] is False, "strict packet reduction overclaim")
    require(strict["current_non_neutrino_count_excluding_QCD_theta"] == 18, "strict packet current")
    require(strict["conditional_non_neutrino_count_if_strict_P_EW_closes"] == 17, "strict packet conditional")
    require(strict["lambda_H_used_as_selector"] is False, "lambda selector")

    require(cutset["all_cutset_rows_open"] is True, "cutset open flag")
    targets = [row["target"] for row in cutset["cutset_rows"]]
    for target in [
        "strict P_EW source theorem or direct K_threshold.Omega_H.lambda",
        "QCD theta_bar / strong-CP policy",
        "absolute neutrino mass and Majorana-vs-Dirac policy",
        "precision threshold, mass-scheme, multi-loop RG, covariance/profile table",
        "actual selected Qa/SU3 operator/source payload",
    ]:
        require(target in targets, f"missing target {target}")
    require(
        cutset["duplicative_loop_guard"]["do_not_reopen_galerkin_value_search_without_new_source_owner"]
        is True,
        "loop guard",
    )

    totals = frontier["frontier_totals"]
    require(frontier["current_counts"]["non_neutrino_excluding_QCD_theta"] == 18, "frontier current 18")
    require(frontier["current_counts"]["minimal_PMNS_extension_excluding_QCD_theta"] == 24, "frontier current 24")
    require(totals["non_neutrino_if_QCD_theta_admitted"] == 19, "QCD total")
    require(totals["non_neutrino_if_strict_P_EW_closes_and_QCD_theta_admitted"] == 18, "strict+QCD total")
    require(totals["minimal_PMNS_if_QCD_theta_admitted"] == 25, "PMNS+QCD total")
    require(totals["massive_Majorana_PMNS_if_QCD_absolute_and_Majorana_admitted"] == 28, "massive total")
    require(totals["massive_Majorana_PMNS_if_strict_P_EW_closes_too"] == 27, "massive strict total")

    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["strict_P_EW_source_theorem_closed"] is False, "cert strict overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "StrictPEWSourceTheoremOrSMPrecisionClosureCutsetTheorem",
        "current strict P_EW source rows = 0",
        "non-neutrino count excluding QCD theta_bar = 18",
        "minimal PMNS oscillation extension excluding QCD theta_bar = 24",
        "non-neutrino count excluding QCD theta_bar = 17",
        "QCD `theta_bar` / strong-CP policy",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict P_EW source remains open with 0 rows; "
        "SM precision closure cutset is locked; current counts are 18/24 "
        "excluding QCD theta, conditional strict-PEW counts are 17/23."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
