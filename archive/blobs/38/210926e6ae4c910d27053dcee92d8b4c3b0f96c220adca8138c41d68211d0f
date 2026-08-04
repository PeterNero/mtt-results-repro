"""Audit action-kernel four-clause proof or independent kernel values run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A_PARTIAL = PACKET_DIR / "route_a_four_clause_partial_proof.packet.json"
ROUTE_A_VALIDATOR = PACKET_DIR / "route_a_four_clause_validator_result.packet.json"
ROUTE_B_FIRST_RUN = PACKET_DIR / "route_b_independent_kernel_values_first_run.packet.json"
ROUTE_B_VALIDATOR = PACKET_DIR / "route_b_independent_kernel_values_validator_result.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_four_clause_partial_proof.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ActionKernelFourClauseProof_or_IndependentKernelValuesRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ACTIONKERNELFOURCLAUSEPROOF_OR_INDEPENDENTKERNELVALUESRUN_BUILT_VARIATION_SPACE_CLOSED_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalActionBindingAndSameSourceEmission_or_IndependentKernelSourceExport_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A_PARTIAL)
    route_a_validator = load(ROUTE_A_VALIDATOR)
    route_b = load(ROUTE_B_FIRST_RUN)
    route_b_validator = load(ROUTE_B_VALIDATOR)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(route_a["admissible_differentiated_variations_fixed"] is True, "variation clause not closed")
    require(route_a["physical_action_equals_c1_defect_functional"] is False, "physical action overclosed")
    require(route_a["physical_boundary_source_terms_vanish"] is False, "physical boundary overclosed")
    require(route_a["same_source_rz_rx_bselected_emitted"] is False, "same-source emission overclosed")
    require(route_a["residual_projector_replay_used_as_source"] is False, "residual replay used")
    require(route_a["locked_target_values_used_as_source"] is False, "target values used")
    require(route_a_validator["returncode"] == 1, "route A validator should still reject")
    require(any("missing action-kernel theorem fields" in line for line in route_a_validator["stderr_lines"]), "route A missing-field error absent")

    require(route_b["global_sources"]["selected_variation_space"]["selected_emitted"] is True, "variation-space source not emitted")
    require(route_b["global_sources"]["selected_variation_space"]["independent_of_residual_replay"] is True, "variation-space source not independent")
    require(route_b["global_sources"]["selected_measure_pairing"]["selected_emitted"] is False, "measure overemitted")
    require(len(route_b["primitive_row_kernel_sources"]) == 72, "primitive source count mismatch")
    require(len(route_b["hessian_b_sources"]) == 2, "hessian source count mismatch")
    require(len(route_b["sector_assembly_sources"]) == 36, "sector source count mismatch")
    require(route_b_validator["returncode"] == 1, "route B validator should still reject")

    require(cutset["status"] == "VARIATION_SPACE_CLOSED_THREE_ROUTE_A_CLAUSES_AND_KERNEL_VALUES_OPEN", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("admissible_differentiated_variations_fixed" in cutset["closed_now"], "cutset missing closed clause")

    for key in [
        "admissible_differentiated_variations_fixed",
        "variation_space_source_independent_of_residual_replay",
        "route_A_validator_rerun_with_one_clause_closed",
        "route_B_validator_rerun_with_variation_space_source_closed",
        "source_cutset_sharpened",
        "observed_constants_excluded_as_selectors",
        "target_fitting_excluded",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")

    for key in [
        "physical_action_equals_c1_defect_functional",
        "physical_boundary_source_terms_vanish",
        "same_source_rz_rx_bselected_emitted",
        "selected_independent_quadrature_rule",
        "selected_independent_measure_pairing_source",
        "primitive_kernel_source_ids_and_formulas",
        "independent_hessian_bselected_source_ids",
        "sector_assembly_source_ids",
        "unpatched_SM_parity_dynamic_packet_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    decision = data["promotion_decision"]
    require(decision["admissible_variation_space_clause_promoted"] is True, "decision missing variation clause")
    for key in [
        "route_A_action_kernel_theorem_proved",
        "route_B_independent_kernel_values_exported",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    for phrase in [
        "admissible differentiated variations fixed     CLOSED",
        "physical action = C1 defect functional         OPEN",
        "does not use residual-projector replay",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
