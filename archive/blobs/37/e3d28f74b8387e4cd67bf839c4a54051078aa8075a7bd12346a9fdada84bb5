"""Audit same-branch threshold/mass-scheme rows and source-anchor construction frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXTERNAL_REPLAY = PACKET_DIR / "admitted_external_replay_integration_after_orbit_source_domain.packet.json"
INTERNAL_GAP = PACKET_DIR / "same_branch_internal_source_row_gap.packet.json"
ANCHOR_GAP = PACKET_DIR / "source_anchor_construction_gap.packet.json"
FINAL_FRONTIER = PACKET_DIR / "final_value_frontier_after_integration.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameBranchThresholdMassSchemeRows_or_SourceAnchorConstruction_v1.md"

STATUS = (
    "MTT_SELECTED_SAMEBRANCHTHRESHOLDMASSSCHEMEROWS_OR_SOURCEANCHORCONSTRUCTION_"
    "BUILT_READINESS_8_OF_9_FINAL_NOKNOB_VALUE_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1"


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
    external = load(EXTERNAL_REPLAY)
    internal = load(INTERNAL_GAP)
    anchor = load(ANCHOR_GAP)
    frontier = load(FINAL_FRONTIER)
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
    guard(external, errors, "external replay", closure=False)
    guard(internal, errors, "internal gap", closure=False)
    guard(anchor, errors, "anchor gap", closure=False)
    guard(frontier, errors, "final frontier", closure=False)

    expect(external.get("Rtheta_value_functional_source_domain_closed") is True, "source domain not integrated", errors)
    expect(external.get("same_branch_scale_scheme_loop_convention_closed") is True, "convention not integrated", errors)
    expect(external.get("admitted_external_threshold_matching_rows") is True, "external threshold rows not integrated", errors)
    expect(external.get("admitted_external_mass_scheme_rows") is True, "external mass rows not integrated", errors)
    expect(external.get("accepted_diagonal_profile_theorem_closed") is True, "diagonal profile not integrated", errors)
    expect(external.get("readiness_fraction") == "8/9", "readiness fraction mismatch", errors)
    expect(external.get("only_remaining_readiness_blocker") == "no_knob_value_derivation", "readiness blocker mismatch", errors)
    expect(external.get("can_claim_admitted_external_replay_boundary") is True, "external replay boundary should be claimable", errors)
    expect(external.get("can_claim_true_SM_equivalence") is False, "true SM equivalence overclaimed", errors)
    expect(external.get("can_claim_full_no_knob") is False, "full no-knob overclaimed", errors)

    expect(internal.get("external_rows_admitted") is True, "external rows not admitted", errors)
    expect(internal.get("selected_internal_Rtheta_threshold_mass_derivation_closed") is False, "internal derivation overclosed", errors)
    expect(internal.get("selected_threshold_response_functional_instantiated") is False, "functional overinstantiated", errors)
    expect(internal.get("selected_internal_value_emission_count") == 0, "internal values overemitted", errors)
    expect(internal.get("accepted_coefficient_value_count") == 0, "coefficient values overaccepted", errors)
    expect(internal.get("lambda_H_coefficient_selected") is False, "lambda_H overselected", errors)

    expect(anchor.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)
    expect(anchor.get("minimal_universal_parameter_selection_closed") is False, "universal selection overclosed", errors)
    expect(anchor.get("candidate_specific_source_theorem_required") is True, "source theorem requirement missing", errors)
    expect(anchor.get("universal_policy_matrix_available") is True, "universal policy matrix missing", errors)

    closed = frontier.get("closed_now", {})
    for key in [
        "qualitative_SM_orbit_closure",
        "Rtheta_value_functional_source_domain",
        "same_branch_scale_scheme_loop_convention",
        "admitted_external_threshold_matching_rows",
        "admitted_external_mass_scheme_conversion_rows",
        "accepted_diagonal_profile_theorem",
        "Rtheta_readiness_8_of_9",
        "admitted_external_replay_boundary",
    ]:
        expect(closed.get(key) is True, f"frontier closed missing: {key}", errors)
    remains = frontier.get("still_open", {})
    for key in [
        "no_knob_value_derivation",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiation",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "candidate_specific_universal_source_theorem",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        expect(remains.get(key) is True, f"frontier blocker missing: {key}", errors)
    expect(frontier.get("remaining_readiness_blocker") == "no_knob_value_derivation", "frontier readiness blocker mismatch", errors)
    expect(frontier.get("next_required_artifact") == NEXT, "frontier next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("Rtheta_readiness_8_of_9") is True, "decision readiness missing", errors)
    expect(decision.get("admitted_external_replay_boundary_integrated") is True, "decision external replay missing", errors)
    expect(decision.get("selected_internal_value_emission_count") == 0, "decision internal values overemitted", errors)
    expect(decision.get("accepted_coefficient_value_count") == 0, "decision coefficients overaccepted", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision universal overselected", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("Rtheta readiness                 : 8/9" in note, "note missing readiness", errors)
    expect("only readiness blocker           : no_knob_value_derivation" in note, "note missing blocker", errors)
    expect("selected internal value emissions: 0" in note, "note missing internal zero", errors)

    if errors:
        print("Same-branch threshold/source-anchor integration audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Same-branch threshold/source-anchor integration audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
