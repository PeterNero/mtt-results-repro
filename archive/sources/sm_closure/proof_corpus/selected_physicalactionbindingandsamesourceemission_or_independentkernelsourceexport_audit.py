"""Audit physical action binding / same-source emission or independent kernel source export."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACTION = PACKET_DIR / "route_a_action_kernel_binding_attempt.packet.json"
ACTION_RESULT = PACKET_DIR / "route_a_action_kernel_binding_validator_result.packet.json"
PHYSICAL = PACKET_DIR / "physical_source_emission_attempt.packet.json"
PHYSICAL_RESULT = PACKET_DIR / "physical_source_emission_validator_result.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_kernel_source_export_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_independent_kernel_source_export_validator_result.packet.json"
LAST_LEMMA = PACKET_DIR / "minimal_last_source_lemma_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalActionBindingAndSameSourceEmission_or_IndependentKernelSourceExport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PHYSICALACTIONBINDINGANDSAMESOURCEEMISSION_OR_INDEPENDENTKERNELSOURCEEXPORT_"
    "BUILT_LAST_SOURCE_LEMMA_EXACT"
)
NEXT = "MTT_Selected_LastSourceLemmaProof_or_IndependentC1KernelSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    action = load(ACTION)
    action_result = load(ACTION_RESULT)
    physical = load(PHYSICAL)
    physical_result = load(PHYSICAL_RESULT)
    route_b = load(ROUTE_B)
    route_b_result = load(ROUTE_B_RESULT)
    lemma = load(LAST_LEMMA)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(action["admissible_differentiated_variations_fixed"] is True, "variation clause lost")
    require(action["formal_C1_defect_functional_sourced"] is True, "formal defect source lost")
    require(action["physical_action_equals_c1_defect_functional"] is False, "physical action overclosed")
    require(action["physical_boundary_source_terms_vanish"] is False, "boundary overclosed")
    require(action["same_source_rz_rx_bselected_emitted"] is False, "same-source overclosed")
    require(action_result["returncode"] == 1, "action validator should reject")
    require(any("missing action-kernel theorem fields" in line for line in action_result["stderr_lines"]), "action missing-field error absent")

    require(physical["theorem_derived"] is False, "physical theorem overderived")
    require(physical["physical_first_variation_identity"] is False, "first variation overclosed")
    require(physical["same_source_b_selected_emission"] is False, "b selected overemitted")
    require(physical_result["returncode"] == 1, "physical validator should reject")
    require(any("missing physical-source fields" in line for line in physical_result["stderr_lines"]), "physical missing-field error absent")

    require(route_b["global_sources"]["selected_variation_space"]["selected_emitted"] is True, "variation source not retained")
    require(route_b["global_sources"]["selected_measure_pairing"]["selected_emitted"] is False, "measure overemitted")
    require(len(route_b["primitive_row_kernel_sources"]) == 72, "primitive rows mismatch")
    require(len(route_b["hessian_b_sources"]) == 2, "hessian rows mismatch")
    require(len(route_b["sector_assembly_sources"]) == 36, "sector rows mismatch")
    require(route_b_result["returncode"] == 1, "route B validator should reject")

    require(lemma["lemma_name"] == "SelectedPhiFinC1ActionSourceLemma", "lemma name mismatch")
    require(lemma["closed_inputs"]["admissible_variation_space"] is True, "lemma missing variation input")
    require(lemma["closed_inputs"]["unique_formal_C1_defect_functional"] is True, "lemma missing defect input")
    for key in [
        "physical_action_equals_c1_defect_functional",
        "physical_boundary_source_terms_vanish",
        "same_source_rz_rx_bselected_emitted",
        "independent_kernel_source_ids",
    ]:
        require(lemma["minimal_open_fields"][key] is True, f"lemma missing open field: {key}")

    for key in [
        "last_source_lemma_contract_exact",
        "formal_defect_plus_variation_shown_insufficient_for_physical_promotion",
        "action_kernel_validator_aligned",
        "physical_source_validator_aligned",
        "independent_kernel_source_validator_aligned",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")

    decision = data["promotion_decision"]
    for key in [
        "route_A_physical_action_source_promoted",
        "route_B_independent_kernel_source_exported",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require("SelectedPhiFinC1ActionSourceLemma" in note, "note missing lemma")
    require("Still not enough" in note, "note missing insufficiency")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
