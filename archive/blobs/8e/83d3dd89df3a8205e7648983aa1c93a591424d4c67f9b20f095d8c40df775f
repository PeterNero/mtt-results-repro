"""Audit selected C1 measure/pairing or physical-action identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1measurepairing_or_physicalactionidentity"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAIRING = PACKET_DIR / "candidate_trace_frobenius_measure_pairing.packet.json"
ACTION = PACKET_DIR / "physical_action_identity_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_sufficiency_and_remaining_axioms.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1MeasurePairing_or_PhysicalActionIdentity_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1MEASUREPAIRING_OR_PHYSICALACTIONIDENTITY_BUILT_FORMAL_PAIRING_PROMOTION_OPEN"
NEXT = "MTT_Selected_C1TraceMeasurePromotion_or_ActionBoundaryProof_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    pairing = load(PAIRING)
    action = load(ACTION)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(pairing["status"] == "FORMAL_TRACE_FROBENIUS_PAIRING_BUILT_NOT_PHYSICAL_MEASURE_PROMOTED", "pairing status mismatch")
    support = pairing["formal_support"]
    require(support["selected_basis_rows"] == 19, "basis count mismatch")
    require(support["all_basis_rows_selected"] is True, "basis support missing")
    require(support["unique_formal_C1_defect_functional_sourced"] is True, "defect source missing")
    require(support["euler_projection_scale_independence"] is True, "scale independence missing")
    require(support["finite_euler_projection"] is True, "Euler projection missing")
    require(support["least_norm_Q_residual_selection"] is True, "least-norm Q missing")
    require(support["all_110_algebraic_value_slots_filled"] is True, "value slots missing")
    require(pairing["would_accept_route_B_if_promoted"]["locked_target_matches"] is True, "locked target mismatch")
    require(pairing["would_accept_route_B_if_promoted"]["exactness_certificate_is_algebraic_not_independent_quadrature"] is True, "algebraic guardrail missing")
    for key in [
        "selected_physical_C1_measure_from_PhiFin_trace_missing",
        "independent_quadrature_engine_measure_missing",
        "boundary_clause_missing",
        "same_source_b_selected_emission_missing",
    ]:
        require(pairing["not_promoted_because"][key] is True, f"pairing gap missing: {key}")
    require(pairing["selected_measure_pairing_promoted_now"] is False, "pairing overclaimed")

    require(action["status"] == "PHYSICAL_ACTION_IDENTITY_REDUCED_TO_BOUNDARY_AND_TRACE_MEASURE_OPEN", "action status mismatch")
    require(action["theorem_name"] == "SelectedPhiFinC1PhysicalActionIdentity", "action theorem mismatch")
    for key in [
        "formal_defect_functional_unique",
        "finite_euler_projection_derived",
        "least_norm_Q_residual_selection",
        "algebraic_values_filled",
    ]:
        require(action["closed_formal_clauses"][key] is True, f"closed action clause missing: {key}")
    for key in [
        "selected_trace_map_verified",
        "first_variation_identity_verified",
        "boundary_cancellation_verified",
        "physical_action_equals_formal_pairing",
        "same_source_b_selected_emission",
    ]:
        require(action["remaining_physical_clauses"][key] is True, f"action gap missing: {key}")
    require(action["route_A_promoted_now"] is False, "action overclaimed")

    require(promotion["status"] == "SUFFICIENCY_PROVED_PROMOTION_AXIOMS_OPEN", "promotion status mismatch")
    require(promotion["current_truth_values"]["formal_pairing_built"] is True, "formal pairing missing")
    require(promotion["current_truth_values"]["algebraic_values_filled"] is True, "values missing")
    for key in [
        "selected_C1_measure_pairing_promoted",
        "physical_action_identity_promoted",
        "boundary_terms_verified",
        "same_source_b_selected_emitted",
        "closure_claimed",
    ]:
        require(promotion["current_truth_values"][key] is False, f"truth value overclaimed: {key}")
    require(promotion["sufficient_if"]["locked_target_matches"] is True, "sufficiency locked target missing")
    require("using observed masses, CKM/PMNS, or CP as selectors" in promotion["forbidden_shortcuts"], "forbidden selector guardrail missing")

    for key in [
        "formal_trace_frobenius_pairing_built",
        "pairing_sufficiency_for_locked_replay_proved",
        "physical_action_identity_reduced_to_specific_clauses",
        "boundary_and_same_source_bselected_identified_as_remaining",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_C1_measure_pairing_promotion",
        "selected_physical_action_identity",
        "selected_trace_map_verification",
        "boundary_cancellation_verification",
        "same_source_b_selected_emission",
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
    require("formal trace/Frobenius C1 pairing       = True" in note, "note missing pairing line")
    require("selected physical measure promoted       = False" in note, "note missing promotion guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
