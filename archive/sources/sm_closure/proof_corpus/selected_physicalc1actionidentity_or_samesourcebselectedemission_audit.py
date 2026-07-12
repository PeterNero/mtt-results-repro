"""Audit physical C1 action-identity / same-source b_selected emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalc1actionidentity_or_samesourcebselectedemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACTION_EQUIV = PACKET_DIR / "physical_action_identity_to_source_emission.packet.json"
BSELECTED = PACKET_DIR / "same_source_bselected_emission_attempt.packet.json"
CLOSURE_EQUIV = PACKET_DIR / "closure_equivalence_and_next_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalC1ActionIdentity_or_SameSourceBSelectedEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALC1ACTIONIDENTITY_OR_SAMESOURCEBSELECTEDEMISSION_BUILT_EQUIVALENCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalActionSourceEmission_or_HonestGalerkinReplacement_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    action = load(ACTION_EQUIV)
    bselected = load(BSELECTED)
    closure = load(CLOSURE_EQUIV)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(action["status"] == "ACTION_IDENTITY_REDUCED_TO_SOURCE_EMISSION_EQUIVALENCE_OPEN", "action status mismatch")
    support = action["closed_formal_support"]
    for key in [
        "selected_trace_map_support",
        "dynamic_trace_binding",
        "formal_trace_frobenius_pairing",
        "algebraic_finite_boundary_cancellation",
        "all_110_algebraic_values_filled",
        "source_map_candidate_constructed",
    ]:
        require(support[key] is True, f"closed support missing: {key}")
    current = action["current_physical_antecedents"]
    for key in [
        "physical_action_identity_promoted",
        "physical_measure_equals_trace_frobenius_pairing",
        "phase_R_Z_selected",
        "shift_R_X_selected",
        "same_source_b_selected_emitted",
        "no_extra_physical_boundary_or_source_term",
    ]:
        require(current[key] is False, f"physical antecedent overclaimed: {key}")
    require(action["route_A_promotes_if_all_antecedents_true"] is True, "route A sufficiency missing")
    require(action["route_A_promoted_now"] is False, "route A overclaimed")
    require("not a physical action proof" in action["proof_status"], "action guardrail missing")

    require(bselected["status"] == "B_SELECTED_REPLAY_AVAILABLE_SAME_SOURCE_EMISSION_OPEN", "bselected status mismatch")
    values = bselected["b_replay_values"]
    require(values["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(values["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(values["b_norm_sq"] == 24.0, "b norm mismatch")
    require(values["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(bselected["replay_available_under_axiom_patch"] is True, "b replay not available")
    require(bselected["b_selected_emitted_by_independent_hessian"] is False, "independent Hessian overclaimed")
    require(bselected["same_source_b_selected_emitted_now"] is False, "same-source b overclaimed")
    require(len(bselected["why_not_emitted"]) == 3, "b guardrails missing")
    for key, value in bselected["would_close_if_joined_with"].items():
        require(value is True, f"b sufficiency join missing: {key}")

    require(closure["status"] == "CLOSURE_EQUIVALENCE_FIXED_SOURCE_EMISSION_OR_HONEST_GALERKIN_OPEN", "closure status mismatch")
    for key, value in closure["already_not_blockers"].items():
        require(value is True, f"not-blocker flag missing: {key}")
    for key, value in closure["remaining_cutset"].items():
        require(value is True, f"remaining cutset missing: {key}")
    require(closure["route_A_same_source_physical_action_closes_now"] is False, "route A closure overclaimed")
    require(closure["route_B_honest_galerkin_replacement_closes_now"] is False, "route B closure overclaimed")
    require(closure["unpatched_SM_parity_dynamic_packet_closes_now"] is False, "dynamic closure overclaimed")

    for key in [
        "action_identity_to_source_emission_equivalence",
        "same_source_bselected_emission_attempt_built",
        "closure_equivalence_fixed",
        "finite_boundary_no_longer_blocker",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_action_identity",
        "physical_measure_equals_trace_frobenius_pairing",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
        "no_extra_physical_boundary_or_source_term",
        "honest_Galerkin_or_independent_quadrature_replacement",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require("same-source b_selected emitted        = False" in note, "note missing b guardrail")
    require("physical action identity promoted     = False" in note, "note missing action guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
