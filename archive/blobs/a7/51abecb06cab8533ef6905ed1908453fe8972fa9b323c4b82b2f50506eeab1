"""Audit CONST-EW-02 B41 gauge-action/RG matching frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
GAUGE_ANCHOR = BASE / "gauge_action_anchor_status.packet.json"
RG_MATCHING = BASE / "rg_matching_threshold_scheme_status.packet.json"
THETA_CLASS = BASE / "theta_v_prediction_classification.packet.json"
BOUNDARY = BASE / "weak_mixing_b41_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B41_GaugeAction_RGMatching_v1.md"

STATUS = "MTT_CONST_EW_02_B41_GAUGE_ACTION_RG_MATCHING_BUILT_ANCHOR_VALUES_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    gauge_anchor = load(GAUGE_ANCHOR)
    rg_matching = load(RG_MATCHING)
    theta_class = load(THETA_CLASS)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("gauge_anchor", gauge_anchor),
        ("rg_matching", rg_matching),
        ("theta_class", theta_class),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["gauge_action_anchor_reduced"] is True, "gauge action reduction")
    require(candidate["one_universal_primitive_extension_ready"] is True, "one primitive")
    require(candidate["RG_matching_policy_scaffold_declared"] is True, "RG scaffold")
    require(candidate["theta_V_values_classified_not_promoted"] is True, "Theta classification")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict overclosed")

    anchor_decision = gauge_anchor["decision"]
    require(anchor_decision["strict_no_knob_physical_action_anchor_closed"] is False, "strict action overclosed")
    require(anchor_decision["one_universal_primitive_extension_ready"] is True, "one primitive route")
    require(anchor_decision["twistor_action_internal_overlap_normalization_support"] is True, "twistor support")
    require(anchor_decision["physical_alpha_or_metrology_anchor_closed"] is False, "alpha overclosed")
    require(anchor_decision["K_phys_or_f_ab_closed"] is False, "K phys overclosed")
    require(
        "one universal metrological primitive" in gauge_anchor["required_to_promote"]["one_primitive_tier"],
        "one primitive promotion text",
    )

    rg_decision = rg_matching["decision"]
    require(rg_decision["RG_policy_scaffold_declared"] is True, "RG policy")
    require(rg_decision["precision_benchmark_values_imported_as_selectors"] is False, "benchmark selector")
    require(rg_decision["source_selected_mu_match_closed"] is False, "mu match overclosed")
    require(rg_decision["source_selected_threshold_vector_closed"] is False, "threshold overclosed")
    require(rg_decision["physical_weak_angle_profile_closed"] is False, "profile overclosed")
    require(len(rg_matching["external_methodology_constraints"]) >= 3, "external constraints")

    reported = theta_class["theta_V_reported_values"]
    require(reported["tree_level_matching_sin2_MZ_approx"] == 0.23120, "Theta V tree value")
    require(reported["threshold_scan_sin2_MZ_approx_range"] == [0.23157, 0.23214], "Theta V range")
    require(reported["imported_as_source_value"] is False, "Theta value source promotion")
    classification = theta_class["classification"]
    require(classification["round_trip_consistency"] is True, "Theta round trip")
    require(classification["non_circular_test_template"] is True, "Theta template")
    require(classification["strict_no_knob_physical_weak_angle_closure"] is False, "Theta strict overclosed")
    require("Do not promote" in classification["forbidden_use"], "Theta forbidden use")

    closed = boundary["closed_or_decided_now"]
    require(closed["C1_local_source_kernel_remains_retired_as_active_local_blocker"] is True, "C1 retired")
    require(closed["gauge_action_anchor_reduced_to_alpha_phys_or_universal_action_unit"] is True, "anchor reduced")
    require(closed["RG_matching_policy_scaffold_declared"] is True, "boundary RG")
    require(closed["Theta_V_values_classified_without_promotion"] is True, "boundary Theta")
    require(boundary["still_open"]["strict_no_knob_physical_action_anchor"] is True, "strict anchor open")
    require(boundary["still_open"]["source_selected_mu_match"] is True, "mu open")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "weak angle open")
    require("not re-opening C1 source-kernel ownership" in boundary["anti_cycle_delta_from_B40"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B42-SELECTED-ACTION-UNIT-OR-ONE-PRIMITIVE-BRIDGE", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B42-RG-ENGINE-EXECUTION-WITH-LOCKED-SCHEME", "next parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(cert["strict_full_no_knob_closure"] is False, "cert strict")
    require("B41" in note and "Superset Use" in note and "B42" in note, "note")

    print("CONST-EW-02 B41 gauge-action/RG matching audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
