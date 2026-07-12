"""Audit physical Phi_fin^C1 finite-quotient/no-extra-source lemma attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalphifinc1finitequotientnoextraboundarysourcelemma_or_independentrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CLAUSE_ATTACK = PACKET_DIR / "three_clause_direct_attack.packet.json"
CURRENT = PACKET_DIR / "current_two_exit_source_packet.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_two_exit_source_validator_result.packet.json"
LOCAL = PACKET_DIR / "local_principle_two_exit_source_witness.packet.json"
LOCAL_RESULT = PACKET_DIR / "local_principle_two_exit_source_validator_result.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_lemma_attack.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma_or_IndependentRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALPHIFINC1FINITEQUOTIENTNOEXTRABOUNDARYSOURCELEMMA_OR_INDEPENDENTROWS_BUILT_LOCAL_SUFFICIENCY_UNPATCHED_OPEN"
NEXT = "MTT_Selected_PhysicalRestrictionSublemma_or_RouteBIndependentRowsExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    attack = load(CLAUSE_ATTACK)
    current = load(CURRENT)
    current_result = load(CURRENT_RESULT)
    local = load(LOCAL)
    local_result = load(LOCAL_RESULT)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(attack["status"] == "DIRECT_ATTACK_REDUCED_TO_THREE_LIVE_PHYSICAL_SOURCE_FIELDS", "attack status mismatch")
    for result in attack["clause_results"].values():
        require(result["proved_now"] is False, "direct attack overproved a clause")
    require(attack["support_only_countermodel_blocks_closure"] is True, "countermodel guard missing")

    route_a = current["route_A_physical_action_restriction"]
    require(route_a["same_branch"] is True, "current Route A branch mismatch")
    for key in [
        "physical_action_restricts_to_finite_weyl_quotient",
        "zero_extra_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(route_a[key] is False, f"current Route A overclosed: {key}")
    require(current_result["returncode"] == 1, "current two-exit packet should reject")
    require(any("Route A missing" in line for line in current_result["stderr_lines"]), "current Route A missing error absent")

    local_route_a = local["route_A_physical_action_restriction"]
    for key in [
        "physical_action_restricts_to_finite_weyl_quotient",
        "zero_extra_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(local_route_a[key] is True, f"local Route A missing: {key}")
    require(local_route_a["accepted_as"] == "explicit local premise, not unpatched theorem", "local premise guard missing")
    require(local["unpatched_theorem_claimed"] is False, "local witness overclaims unpatched theorem")
    require(local_result["returncode"] == 0, "local two-exit witness should validate")

    require(cutset["status"] == "LOCAL_SUFFICIENCY_PROVED_UNPATCHED_THREE_FIELD_CERTIFICATE_OPEN", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    for field in [
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_R_Z_R_X_b_selected_emission",
    ]:
        require(field in cutset["remaining_route_A_fields"], f"cutset missing field: {field}")
        require(data["what_remains_open"][field] is True, f"candidate missing open field: {field}")

    require(data["what_closes_now"]["current_unpatched_two_exit_packet_rejected"] is True, "current rejection not recorded")
    require(data["what_closes_now"]["local_principle_route_A_two_exit_witness_validates"] is True, "local validation not recorded")
    require(data["promotion_decision"]["local_conditional_route_A_validated"] is True, "local promotion decision missing")
    for key in [
        "unpatched_physical_finite_quotient_lemma_proved",
        "route_B_independent_rows_executed",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    require("local Weyl-variation principle is sufficient" in note, "note missing local sufficiency")
    require("three-field physical source certificate is still not filled" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
