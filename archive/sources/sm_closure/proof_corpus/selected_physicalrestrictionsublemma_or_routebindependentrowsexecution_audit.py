"""Audit physical restriction sublemma / Route B independent rows execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESTRICTION_PROBE = PACKET_DIR / "physical_restriction_sublemma_probe.packet.json"
STRICT_REPLAY = PACKET_DIR / "strict_source_certificate_replay.packet.json"
ROUTE_B_GAP = PACKET_DIR / "route_b_independent_rows_execution_gap.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_physical_restriction_probe.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalRestrictionSublemma_or_RouteBIndependentRowsExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALRESTRICTIONSUBLEMMA_OR_ROUTEBINDEPENDENTROWSEXECUTION_BUILT_A1A_SOURCE_ROW_OPEN"
NEXT = "MTT_Selected_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    restriction = load(RESTRICTION_PROBE)
    replay = load(STRICT_REPLAY)
    route_b = load(ROUTE_B_GAP)
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

    require(restriction["status"] == "SUPPORT_COMPLETE_SOURCE_ROW_NOT_EMITTED", "restriction status mismatch")
    require(restriction["all_closed_support_true"] is True, "closed support not complete")
    require(restriction["accepted_same_branch_sources_found"] == [], "unexpected same-branch source found")
    require(restriction["same_branch_physical_action_restriction_emitted"] is False, "restriction overemitted")
    require(restriction["field_filled_now"] is False, "restriction field overfilled")
    require(restriction["support_only_not_sufficient"] is True, "support-only guard missing")

    require(replay["validator_result"]["returncode"] == 1, "strict validator should reject")
    require(replay["psm_replay_exit_code"] == 1, "PSM replay should reject")
    require(
        replay["expected_missing_route_a_field"] == "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "expected missing Route A field mismatch",
    )
    require(replay["route_A_current_truth"]["same_branch"] is False, "Route A same branch overclaimed")
    require(
        replay["route_A_current_truth"]["physical_action_restricts_to_selected_finite_Weyl_quotient"] is False,
        "Route A restriction overclaimed",
    )
    require(replay["route_A_current_truth"]["attached_same_branch_sources_count"] == 0, "unexpected Route A sources")

    require(route_b["all_72_primitive_rows_executed"] is True, "primitive rows not ready")
    require(route_b["formal_110_rows_executed"] is True, "formal 110 rows not ready")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis independence overclaimed")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "quadrature independence overclaimed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source independence overclaimed")
    require(route_b["exactness_or_error_certificates_attached"] is False, "certificates overclaimed")
    require(route_b["ready_now"] is False, "Route B overready")

    require(cutset["status"] == "A1A_PHYSICAL_SOURCE_ROW_OR_ROUTEB_PROVENANCE_REMAINS", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    for key in [
        "physical_restriction_support_probe_imported",
        "closed_support_all_true_but_source_row_absent",
        "strict_validator_replay_rejects_current_packet",
        "route_B_formal_rows_ready_but_provenance_open",
    ]:
        require(data["what_closes_now"][key] is True, f"closed flag missing: {key}")

    for key in [
        "physical_action_restriction_sublemma_proved",
        "route_B_independent_rows_executed",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    require("no same-branch physical `Phi_fin^C1` action row" in note, "note missing source-row guard")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
