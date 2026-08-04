"""Audit CONST-EW-02 B42 one-primitive physical bridge packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
BRIDGE = BASE / "one_primitive_physical_bridge.packet.json"
COLLAPSE = BASE / "action_unit_mu_match_collapse.packet.json"
BUDGET = BASE / "parameter_budget_and_guardrail.packet.json"
BOUNDARY = BASE / "weak_mixing_b42_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B42_OnePrimitivePhysicalBridge_v1.md"

STATUS = "MTT_CONST_EW_02_B42_ONE_PRIMITIVE_PHYSICAL_BRIDGE_BUILT_VALUE_OPEN"


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
    bridge = load(BRIDGE)
    collapse = load(COLLAPSE)
    budget = load(BUDGET)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("bridge", bridge),
        ("collapse", collapse),
        ("budget", budget),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["one_primitive_physical_bridge_contract_closed"] is True, "bridge contract")
    require(candidate["K_phys_alpha_phys_mu_match_collapsed_to_one_primitive"] is True, "slot collapse")
    require(candidate["parameter_budget_guardrail_closed"] is True, "budget guardrail")
    require(candidate["one_primitive_value_selected"] is False, "primitive value overselected")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict overclosed")

    modes = bridge["bridge_modes"]
    require(modes["strict_source_unit"]["available_now"] is False, "strict source unit overavailable")
    require(modes["strict_source_unit"]["strict_no_knob_possible"] is True, "strict route possible")
    require(modes["one_universal_primitive"]["available_now"] is True, "one primitive route")
    require(modes["one_universal_primitive"]["strict_no_knob_possible"] is False, "one primitive strict mismatch")
    require(modes["one_universal_primitive"]["value_selected_now"] is False, "one primitive value")
    require(bridge["decision"]["weak_angle_extra_physical_knob_added"] is False, "extra weak knob")
    require(bridge["decision"]["alpha1_and_weak_mixing_share_same_physical_bridge"] is True, "shared bridge")

    collapsed = collapse["collapsed_slots"]
    require("same E0/L0 primitive" in collapsed["K_phys_or_action_unit"], "K_phys collapse")
    require("Lambda_eff=E0 or 1/L0" in collapsed["mu_match"], "mu collapse")
    require(collapse["decision"]["number_of_physical_unit_primitives_needed_in_this_tier"] == 1, "primitive count")
    require(collapse["decision"]["K_phys_and_mu_match_count_as_separate_knobs"] is False, "separate knobs")
    require(collapse["decision"]["threshold_vector_closed"] is False, "threshold overclosed")
    require(collapse["decision"]["physical_weak_angle_closure"] is False, "collapse weak angle")

    budget_values = budget["budget"]
    require(budget_values["strict_no_knob_selected_parameter_count"] == 0, "strict parameter count")
    require(budget_values["one_primitive_tier_new_global_parameters"] == 1, "one primitive count")
    require(budget_values["weak_angle_specific_parameters"] == 0, "weak angle parameter count")
    require(budget_values["current_selected_numeric_value_count"] == 0, "selected numeric count")
    require(budget["decision"]["per_observable_retuning_forbidden"] is True, "retuning guardrail")
    require(budget["decision"]["one_primitive_tier_is_not_no_knob"] is True, "no-knob separation")
    require(
        "weak angle fixes the primitive and is then counted as predicted"
        in budget["forbidden_calibration_order"],
        "forbidden self calibration",
    )

    closed = boundary["closed_or_decided_now"]
    require(closed["one_primitive_physical_bridge_contract"] is True, "boundary bridge")
    require(closed["K_phys_alpha_phys_mu_match_collapse_to_one_symbolic_primitive"] is True, "boundary collapse")
    require(closed["weak_angle_specific_physical_knob_forbidden"] is True, "boundary weak knob")
    require(boundary["still_open"]["one_primitive_numeric_value"] is True, "primitive value open")
    require(boundary["still_open"]["source_selected_threshold_vector"] is True, "threshold open")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "weak angle open")
    require("not counting K_phys and mu_match as independent knobs in the one-primitive tier" in boundary["anti_cycle_delta_from_B41"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B43-SOURCE-SELECTED-THRESHOLD-VECTOR", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B43-PRIMITIVE-VALUE-SOURCE-OR-ONE-CALIBRATION", "next parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["one_primitive_value_selected"] is False, "cert primitive value")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(cert["strict_full_no_knob_closure"] is False, "cert strict")
    require("B42" in note and "one-primitive" in note and "weak-angle-specific" in note, "note")

    print("CONST-EW-02 B42 one-primitive physical bridge audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
