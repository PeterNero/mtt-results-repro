"""Audit last source lemma proof attempt or independent C1 kernel source rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT_ACTION_RESULT = PACKET_DIR / "current_unpatched_action_kernel_validator_result.packet.json"
CURRENT_PHYSICAL_RESULT = PACKET_DIR / "current_unpatched_physical_source_validator_result.packet.json"
LOCAL_ACTION = PACKET_DIR / "local_principle_action_kernel_witness.packet.json"
LOCAL_ACTION_RESULT = PACKET_DIR / "local_principle_action_kernel_validator_result.packet.json"
LOCAL_PHYSICAL = PACKET_DIR / "local_principle_physical_source_witness.packet.json"
LOCAL_PHYSICAL_RESULT = PACKET_DIR / "local_principle_physical_source_validator_result.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_c1_kernel_source_rows_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_independent_c1_kernel_source_rows_validator_result.packet.json"
DECISION = PACKET_DIR / "last_source_lemma_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LastSourceLemmaProof_or_IndependentC1KernelSourceRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LASTSOURCELEMMAPROOF_OR_INDEPENDENTC1KERNELSOURCEROWS_BUILT_LOCAL_WITNESS_UNPATCHED_OPEN"
NEXT = "MTT_Selected_UnpatchedWeylVariationPrincipleDerivation_or_RouteBSourceRowsFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    decision = load(DECISION)
    current_action_result = load(CURRENT_ACTION_RESULT)
    current_physical_result = load(CURRENT_PHYSICAL_RESULT)
    local_action = load(LOCAL_ACTION)
    local_action_result = load(LOCAL_ACTION_RESULT)
    local_physical = load(LOCAL_PHYSICAL)
    local_physical_result = load(LOCAL_PHYSICAL_RESULT)
    route_b = load(ROUTE_B)
    route_b_result = load(ROUTE_B_RESULT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(current_action_result["returncode"] == 1, "current action should reject")
    require(current_physical_result["returncode"] == 1, "current physical should reject")
    require(local_action_result["returncode"] == 0, "local action should validate")
    require(local_physical_result["returncode"] == 0, "local physical should validate")
    require(route_b_result["returncode"] == 1, "Route B should still reject")

    for field in [
        "physical_action_equals_c1_defect_functional",
        "admissible_differentiated_variations_fixed",
        "physical_boundary_source_terms_vanish",
        "same_source_rz_rx_bselected_emitted",
    ]:
        require(local_action[field] is True, f"local action witness missing {field}")
    require(local_action["accepted_as"] == "explicit local premise, not unpatched theorem", "local action premise guard missing")
    require(local_action["closure_claimed"] is False, "local action overclaims closure")

    for field in [
        "physical_first_variation_identity",
        "physical_measure_equals_trace_frobenius_pairing",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
        "no_extra_physical_boundary_or_source_term",
    ]:
        require(local_physical[field] is True, f"local physical witness missing {field}")
    require(local_physical["accepted_as"] == "explicit local premise, not unpatched theorem", "local physical premise guard missing")
    require(local_physical["closure_claimed"] is False, "local physical overclaims closure")

    require(route_b["global_sources"]["selected_variation_space"]["selected_emitted"] is True, "variation source not retained")
    require(route_b["global_sources"]["selected_measure_pairing"]["selected_emitted"] is False, "measure source overemitted")
    require(len(route_b["primitive_row_kernel_sources"]) == 72, "primitive rows mismatch")
    require(len(route_b["hessian_b_sources"]) == 2, "hessian rows mismatch")
    require(len(route_b["sector_assembly_sources"]) == 36, "sector rows mismatch")

    require(decision["local_principle_witness_validates"] is True, "local witness decision missing")
    require(decision["current_unpatched_attempt_rejected"] is True, "unpatched rejection missing")
    require(decision["route_B_independent_rows_rejected"] is True, "Route B rejection missing")
    require(decision["local_principle_is_not_unpatched_proof"] is True, "local/unpatched guard missing")
    require(decision["unpatched_last_source_lemma_proved_now"] is False, "unpatched lemma overproved")
    require(decision["independent_C1_kernel_source_rows_exported_now"] is False, "Route B overexported")

    require(data["theorem"]["proved"] is True, "local sufficiency theorem not proved")
    for key in [
        "local_principle_suffices_for_last_source_lemma",
        "unpatched_attempt_rejected_honestly",
        "route_B_source_rows_still_open_honestly",
        "last_source_lemma_reduced_to_unpatched_weylvariation_or_routeB_rows",
    ]:
        require(data["what_closes_now"][key] is True, f"closed flag missing: {key}")
    for key in [
        "unpatched_last_source_lemma_proved",
        "route_B_independent_C1_kernel_source_rows_exported",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    require("does not claim SM closure" in note, "note missing closure guard")
    require("derive `SelectedWeylVariationActionPrinciple` unpatched" in note, "note missing next route")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
