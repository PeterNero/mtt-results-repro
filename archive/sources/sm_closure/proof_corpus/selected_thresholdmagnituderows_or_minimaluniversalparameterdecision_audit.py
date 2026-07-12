"""Audit threshold magnitude rows or minimal universal parameter decision packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdmagnituderows_or_minimaluniversalparameterdecision"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROW_DECISION = PACKET_DIR / "threshold_magnitude_row_decision.packet.json"
ANCHOR_RECHECK = PACKET_DIR / "minimal_universal_anchor_recheck_after_source_domain.packet.json"
TERMINAL_CUTSET = PACKET_DIR / "terminal_value_closure_cutset.packet.json"
NEXT_STEP = PACKET_DIR / "next_constructive_target.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1.md"

STATUS = (
    "MTT_SELECTED_THRESHOLDMAGNITUDEROWS_OR_MINIMALUNIVERSALPARAMETERDECISION_"
    "BUILT_NUMERICAL_ROWS_STILL_OPEN_CONSTRUCTIVE_TARGET_FIXED"
)
NEXT = "MTT_Selected_SameBranchThresholdMassSchemeRows_or_SourceAnchorConstruction_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    row_decision = load(ROW_DECISION)
    anchor = load(ANCHOR_RECHECK)
    terminal = load(TERMINAL_CUTSET)
    next_step = load(NEXT_STEP)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(row_decision, errors, "row decision", closure=False)
    guard(anchor, errors, "anchor recheck", closure=False)
    guard(terminal, errors, "terminal cutset", closure=False)
    guard(next_step, errors, "next step", closure=False)

    expect(row_decision.get("source_domain_closed") is True, "source domain should be closed", errors)
    expect(row_decision.get("basis_map_to_sector_scaled_magnitude_rows_closed") is True, "basis map should be closed", errors)
    expect(row_decision.get("rank_gap_theorem_proved") is True, "rank gap theorem should be proved", errors)
    expect(row_decision.get("magnitude_bearing_projection_weights_closed") is False, "magnitude weights overclosed", errors)
    expect(row_decision.get("generation_resolved_threshold_source_rows_closed") is False, "threshold rows overclosed", errors)
    expect(row_decision.get("accepted_coefficient_row_count") == 0, "accepted coefficient rows overclosed", errors)
    expect(row_decision.get("diagnostic_coefficients_rejected_as_selectors") is True, "diagnostic rejection missing", errors)

    expect(anchor.get("selected_parameter_count_after") == 0, "universal parameter overselected", errors)
    expect(anchor.get("selected_candidates_now") == [], "selected candidates should be empty", errors)
    expect(anchor.get("source_domain_closure_changes_decision") is False, "source domain should not select anchor", errors)
    expect("no candidate-specific source-anchor theorem is present" in anchor.get("why_not_selected", []), "anchor source-theorem guard missing", errors)

    closed = terminal.get("closed_now", {})
    for key in [
        "qualitative_SM_orbit_closure",
        "Rtheta_value_functional_source_domain",
        "basis_map_to_nine_charged_magnitude_rows",
        "first_response_only_no_go",
        "higher_response_contract",
        "minimal_universal_policy_declared",
    ]:
        expect(closed.get(key) is True, f"terminal closed missing: {key}", errors)
    remains = terminal.get("still_open", {})
    for key in [
        "construct_same_branch_threshold_mass_scheme_rows",
        "construct_magnitude_bearing_projection_weights_or_coefficients",
        "construct_candidate_specific_universal_source_anchor_theorem",
        "execute_higher_response_Rtheta_scalar_rows",
        "emit_lambda_H_row",
        "emit_CKM_PMNS_Yukawa_numerical_rows",
        "true_SM_equivalence",
        "full_no_knob_or_declared_minimal_parameter_closure",
    ]:
        expect(remains.get(key) is True, f"terminal blocker missing: {key}", errors)

    routes = terminal.get("two_valid_routes", {})
    expect("route_1_no_knob" in routes, "no-knob route missing", errors)
    expect("route_2_minimal_parameter" in routes, "minimal parameter route missing", errors)

    expect(next_step.get("next_required_artifact") == NEXT, "next step artifact mismatch", errors)
    expect(next_step.get("preferred_first_attack", {}).get("name") == "SameBranchThresholdMassSchemeRows", "preferred attack mismatch", errors)
    expect(next_step.get("fallback_attack", {}).get("name") == "CandidateSpecificUniversalSourceAnchorTheorem", "fallback attack mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("terminal_value_cutset_proved") is True, "decision terminal cutset missing", errors)
    expect(decision.get("accepted_numerical_coefficient_rows") == 0, "decision coefficient rows overclosed", errors)
    expect(decision.get("minimal_universal_parameter_selected") is False, "decision universal selected", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision universal count mismatch", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision SM equivalence overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("accepted numerical coefficient rows  : 0" in note, "note missing zero coefficient guard", errors)
    expect("selected universal parameter count   : 0" in note, "note missing universal guard", errors)
    expect("full numerical SM equivalence        : false" in note, "note missing SM-equivalence guard", errors)

    if errors:
        print("Threshold magnitude rows decision audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Threshold magnitude rows decision audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
