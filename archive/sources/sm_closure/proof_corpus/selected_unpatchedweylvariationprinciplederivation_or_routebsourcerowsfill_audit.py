"""Audit unpatched Weyl-variation principle derivation or Route-B source rows fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MEASURE = PACKET_DIR / "finite_trace_measure_reduction.packet.json"
ACTION = PACKET_DIR / "unpatched_weylvariation_action_kernel_attempt.packet.json"
ACTION_RESULT = PACKET_DIR / "unpatched_weylvariation_action_kernel_validator_result.packet.json"
PHYSICAL = PACKET_DIR / "physical_source_attempt_with_measure_closed.packet.json"
PHYSICAL_RESULT = PACKET_DIR / "physical_source_with_measure_closed_validator_result.packet.json"
ROUTE_B = PACKET_DIR / "route_b_source_rows_fill_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_source_rows_fill_validator_result.packet.json"
REMAINDER = PACKET_DIR / "physical_finite_quotient_remainder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnpatchedWeylVariationPrincipleDerivation_or_RouteBSourceRowsFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_UNPATCHEDWEYLVARIATIONPRINCIPLEDERIVATION_OR_ROUTEB_SOURCEROWSFILL_BUILT_MEASURE_CLOSED_ACTION_REMAINDER_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma_or_IndependentRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    measure = load(MEASURE)
    action = load(ACTION)
    action_result = load(ACTION_RESULT)
    physical = load(PHYSICAL)
    physical_result = load(PHYSICAL_RESULT)
    route_b = load(ROUTE_B)
    route_b_result = load(ROUTE_B_RESULT)
    remainder = load(REMAINDER)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(measure["measure_normalization_derived"] is True, "measure not derived")
    require(measure["finite_trace_boundary_cancellation"] is True, "finite boundary not imported")
    require(measure["measure_part_no_longer_axiomatic"] is True, "measure still axiomatic")
    require(measure["remainder_name"] == "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma", "remainder mismatch")

    require(action["measure_sublemma_derived"] is True, "action missing measure sublemma")
    require(action["admissible_differentiated_variations_fixed"] is True, "variation clause lost")
    require(action["physical_action_equals_c1_defect_functional"] is False, "physical action overclosed")
    require(action["physical_boundary_source_terms_vanish"] is False, "boundary overclosed")
    require(action["same_source_rz_rx_bselected_emitted"] is False, "same-source overclosed")
    require(action_result["returncode"] == 1, "action validator should reject")

    require(physical["physical_measure_equals_trace_frobenius_pairing"] is True, "physical measure not promoted")
    require(physical["physical_first_variation_identity"] is False, "first variation overclosed")
    require(physical["phase_R_Z_source_selection"] is False, "R_Z overclosed")
    require(physical["shift_R_X_source_selection"] is False, "R_X overclosed")
    require(physical["same_source_b_selected_emission"] is False, "b_selected overclosed")
    require(physical["no_extra_physical_boundary_or_source_term"] is False, "boundary/source overclosed")
    require(physical_result["returncode"] == 1, "physical validator should reject")

    require(route_b["global_sources"]["selected_variation_space"]["selected_emitted"] is True, "variation source not retained")
    require(route_b["global_sources"]["selected_measure_pairing"]["selected_emitted"] is False, "measure source overemitted")
    require(len(route_b["primitive_row_kernel_sources"]) == 72, "primitive rows mismatch")
    require(len(route_b["hessian_b_sources"]) == 2, "hessian rows mismatch")
    require(len(route_b["sector_assembly_sources"]) == 36, "sector rows mismatch")
    require(route_b_result["returncode"] == 1, "Route B should still reject")

    require(remainder["lemma_name"] == "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma", "lemma mismatch")
    for value in remainder["current_truth_values"].values():
        require(value is False, "remainder current truth should remain false")
    require("finite trace/Frobenius measure normalization" in remainder["already_removed_from_blocker"], "measure not removed from blocker")

    for key in [
        "finite_trace_measure_sublemma_derived_imported",
        "physical_measure_field_promoted_in_partial_attempt",
        "unpatched_principle_remainder_sharpened",
        "action_kernel_validator_rejects_remaining_physical_fields",
        "physical_source_validator_rejects_remaining_source_fields",
        "route_B_source_rows_still_open_honestly",
    ]:
        require(data["what_closes_now"][key] is True, f"closed flag missing: {key}")

    decision = data["promotion_decision"]
    require(decision["measure_sublemma_promoted_unpatched"] is True, "measure decision missing")
    for key in [
        "unpatched_SelectedWeylVariationActionPrinciple_derived",
        "unpatched_last_source_lemma_proved",
        "route_B_independent_C1_kernel_source_rows_exported",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require("measure part is no longer a patch" in note, "note missing measure result")
    require("PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma" in note, "note missing next lemma")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
