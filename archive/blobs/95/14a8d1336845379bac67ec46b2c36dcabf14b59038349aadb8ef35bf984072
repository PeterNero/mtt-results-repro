"""Audit physical action restriction actual-fill attempt or Route B independent run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionrestrictionsourceactualfill_or_routebindependentrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_SCAN = PACKET_DIR / "actual_fill_source_scan.packet.json"
ACTUAL_FILL = PACKET_DIR / "physical_action_restriction_actual_fill_attempt.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "actual_fill_validator_result.packet.json"
ROUTE_B_RUN = PACKET_DIR / "route_b_independent_run_actual_status.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_actual_fill_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTIONSOURCEACTUALFILL_OR_ROUTEBINDEPENDENTRUN_BUILT_NO_ACTUAL_SOURCE_ROW_FOUND"
NEXT = "MTT_Selected_SourceRowConstructionFromCorpus_or_RouteBProvenanceFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    scan = load(SOURCE_SCAN)
    actual = load(ACTUAL_FILL)
    validator = load(VALIDATOR_RESULT)
    route_b = load(ROUTE_B_RUN)
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

    require(scan["status"] == "NO_ACTUAL_SAME_BRANCH_ACTION_ROW_FOUND", "scan status mismatch")
    require(scan["source_rows_found"] == [], "unexpected source row found")
    require(len(scan["nearby_non_sources"]) >= 4, "nearby source list too small")

    route_a = actual["route_A_physical_source_certificate"]
    require(actual["actual_source_row_found"] is False, "actual source row overfound")
    require(route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"] is False, "Route A restriction overfilled")
    require(route_a["attached_same_branch_sources"] == [], "unexpected same-branch sources")
    require(actual["promotion_allowed_now"] is False, "promotion overallowed")
    require(validator["returncode"] == 1, "strict validator should reject")
    require(any("Route A missing" in line for line in validator["stderr_lines"]), "Route A missing error absent")

    require(route_b["all_72_primitive_rows_executed"] is True, "primitive rows not ready")
    require(route_b["formal_110_rows_executed"] is True, "formal 110 rows not ready")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis independence overclaimed")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "quadrature independence overclaimed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source independence overclaimed")
    require(route_b["exactness_or_error_certificates_attached"] is False, "exactness certificates overclaimed")
    require(route_b["ready_now"] is False, "Route B overready")

    require(cutset["status"] == "ACTUAL_SOURCE_ROW_ABSENT_ROUTE_B_PROVENANCE_OPEN", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    for key in [
        "actual_fill_attempt_executed",
        "no_same_branch_physical_action_restriction_row_found",
        "strict_validator_rejects_actual_fill_attempt",
        "route_B_actual_run_not_executed",
        "source_row_construction_or_routeB_provenance_is_now_the_frontier",
    ]:
        require(data["what_closes_now"][key] is True, f"closed flag missing: {key}")

    for key in [
        "physical_action_restriction_actual_fill_succeeded",
        "route_B_independent_run_executed",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    require("no emitted same-branch physical" in note, "note missing source-row absence")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
