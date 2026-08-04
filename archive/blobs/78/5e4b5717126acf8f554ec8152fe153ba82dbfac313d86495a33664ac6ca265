"""Audit selected C1 trace-measure promotion / action-boundary proof gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1tracemeasurepromotion_or_actionboundaryproof"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE = PACKET_DIR / "selected_trace_map_and_measure_support.packet.json"
BOUNDARY = PACKET_DIR / "finite_trace_boundary_cancellation_certificate.packet.json"
ACTION = PACKET_DIR / "physical_action_boundary_promotion_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1TraceMeasurePromotion_or_ActionBoundaryProof_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1TRACEMEASUREPROMOTION_OR_ACTIONBOUNDARYPROOF_BUILT_ALGEBRAIC_BOUNDARY_CLOSED_PHYSICAL_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalC1ActionIdentity_or_SameSourceBSelectedEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    trace = load(TRACE)
    boundary = load(BOUNDARY)
    action = load(ACTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(trace["status"] == "SELECTED_TRACE_MAP_SUPPORT_IMPORTED_MEASURE_PROMOTION_OPEN", "trace status mismatch")
    support = trace["support_imported"]
    require(support["selected_basis_rows"] == 19, "basis count mismatch")
    require(support["all_basis_rows_selected"] is True, "basis support missing")
    require(support["dynamic_dotD_trace_binding"] is True, "dynamic trace binding missing")
    require(support["formal_trace_frobenius_pairing_built"] is True, "formal pairing missing")
    require(support["all_110_algebraic_values_filled"] is True, "110 values missing")
    require(trace["selected_measure_promoted_now"] is False, "measure overpromoted")
    require(len(trace["why_not_promoted"]) == 2, "trace guardrails missing")

    require(boundary["status"] == "ALGEBRAIC_FINITE_TRACE_BOUNDARY_CLOSED_PHYSICAL_BOUNDARY_OPEN", "boundary status mismatch")
    require(boundary["algebraic_boundary_closed_now"] is True, "algebraic boundary not closed")
    require("Trace cyclicity" in " ".join(boundary["proof_steps"]), "cyclic trace proof missing")
    require(boundary["physical_boundary_promoted_now"] is False, "physical boundary overpromoted")
    require("does not prove" in boundary["scope_limit"], "boundary scope guardrail missing")

    require(action["status"] == "TRACE_AND_ALGEBRAIC_BOUNDARY_SUPPORT_CLOSED_ACTION_IDENTITY_BSELECTED_OPEN", "action status mismatch")
    available = action["available_now"]
    for key in [
        "selected_trace_map_support",
        "dynamic_trace_binding",
        "formal_trace_frobenius_pairing",
        "algebraic_finite_boundary_cancellation",
        "all_110_algebraic_values_filled",
        "locked_target_matches",
    ]:
        require(available[key] is True, f"available action support missing: {key}")
    for key in [
        "physical_action_identity_equates_first_variation_to_defect_functional",
        "physical_measure_equals_trace_frobenius_pairing",
        "no_extra_physical_boundary_or_source_term",
        "same_source_b_selected_emission",
    ]:
        require(action["still_missing_for_physical_promotion"][key] is True, f"physical gap missing: {key}")
    require(action["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"]["finite_trace_algebraic_verified_now"] is True, "boundary algebraic flag missing")
    require(action["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"]["physical_verified_now"] is False, "physical boundary overclaim")
    require(action["first_variation_certificate_fields_after_this_gate"]["selected_trace_map"]["support_imported_now"] is True, "trace support flag missing")
    require(action["first_variation_certificate_fields_after_this_gate"]["selected_trace_map"]["physical_measure_promoted_now"] is False, "trace physical overclaim")
    require(action["route_A_promoted_now"] is False, "route A overclaimed")
    require(action["route_B_independent_quadrature_promoted_now"] is False, "route B overclaimed")

    for key in [
        "selected_trace_map_support_imported",
        "dynamic_trace_binding_imported",
        "algebraic_finite_trace_boundary_cancellation",
        "formal_measure_pairing_sufficiency_retained",
        "physical_promotion_reduced_to_action_identity_and_bselected",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_PhiFinC1_action_identity",
        "physical_measure_equals_trace_frobenius_pairing",
        "same_source_b_selected_emission",
        "absence_of_extra_physical_boundary_or_source_term",
        "independent_quadrature_exactness_certificate",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("finite trace algebraic boundary vanishes   = True" in note, "note missing boundary close")
    require("physical boundary/action promoted          = False" in note, "note missing physical guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
