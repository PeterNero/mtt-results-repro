"""Audit differentiated PhiFinC1 primitive-overlap / Galerkin run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
TEMPLATE = (
    ROOT
    / "candidate_data"
    / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun"
    / "primitive_overlap_contractions.template.json"
)
CERT = ROOT / "certificates" / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.py"

STATUS = "MTT_SELECTED_DIFFERENTIATED_PHIFINC1_PRIMITIVEOVERLAP_OR_GALERKINRUN_BUILT_TRANSPORT_ONLY_NOGO_TEMPLATE_OPEN"
NEXT = "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1"
SECTORS = ["u", "d", "e", "nuD"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    template = load(TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    coord = data["differentiated_primitive_overlap_contract"]["coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(coord["columns"] == ["phase_packet", "shift_packet"], "coordinate columns mismatch")

    driver = data["driver_contract"]
    require(driver["selected_dotD_source_verified"] is True, "selected dotD driver not attached")
    require(driver["alpha1_driver_verified"] is True, "alpha1 driver not attached")
    require(driver["honest_dotD_alpha1_replay"] is True, "honest dotD replay not imported")
    require(driver["attached_to_differentiated_contract_as_driver"] is True, "driver not attached to contract")
    require(driver["primitive_overlap_values_emitted_by_driver"] is False, "driver overclaims primitive values")
    require("dU_dalpha" in driver["transport_derivative_formula"], "transport derivative missing")

    canonical = data["canonical_transport_only_test"]
    require(canonical["all_c1_matrices_zero_for_canonical_tensor"] is True, "canonical zero result missing")
    require(canonical["all_sector_matrices_verified_zero"] is True, "canonical matrices not all zero")
    require(canonical["can_emit_phase_shift_columns"] is False, "canonical lane overclaims phase/shift")
    require(canonical["c1_response_audit_canonical_status"] == "COMPUTED_ZERO_RESPONSE", "canonical audit status mismatch")

    noninv = data["noninvariant_candidate_import"]
    require(noninv["active_shift"] == [1, 1], "active shift mismatch")
    require(noninv["selected_by_theorem"] is False, "noninvariant candidates overselected")
    summary = noninv["candidate_summary"]
    require(summary["fixed_fiber_candidate_count"] == 3, "fixed fiber candidate count mismatch")
    require(summary["fixed_fiber_candidates"] == [0, 1, 2], "fixed fiber candidates mismatch")
    require(summary["all_fixed_fiber_rank_three"] is True, "fixed fibers not rank three")
    require(summary["all_fiber_rank_one"] is True, "all-fiber envelope rank mismatch")
    require(noninv["primitive_envelope_constructed"] is True, "primitive envelope missing")
    require(noninv["primitive_envelope_selected_as_dynamic_tensor"] is False, "primitive envelope overselected")

    contract = data["differentiated_primitive_overlap_contract"]
    require(contract["template_path"].endswith("primitive_overlap_contractions.template.json"), "template path mismatch")
    require(contract["template_status"] == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING", "template status mismatch")
    require("M_s^r[i,j]" in contract["primitive_overlap_formula"], "primitive formula missing")
    require(len(contract["acceptance_equations"]) == 5, "acceptance equation count mismatch")
    require(contract["normal_form_values_promoted_now"] is False, "normal-form values overpromoted")

    require(template["status"] == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING", "template open status mismatch")
    require(template["coordinate_system"]["codomain_real_dimension"] == 72, "template coordinate mismatch")
    require(template["alpha1_dotD_driver"]["selected_dotD_source_verified"] is True, "template dotD driver missing")
    require(template["alpha1_dotD_driver"]["alpha1_driver_verified"] is True, "template alpha1 driver missing")
    require(template["alpha1_dotD_driver"]["primitive_overlap_values_emitted_by_driver"] is False, "template driver overclaims")
    for sector in SECTORS:
        require(template["required_selected_values"]["primitive_three_by_three_contraction_terms"][sector] is None, f"template primitive slot filled: {sector}")
        require(template["required_selected_values"]["linear_response_matrices"][sector] is None, f"template response slot filled: {sector}")

    theorem = data["transport_only_no_go_theorem"]
    require(theorem["proved"] is True, "transport-only no-go not proved")
    require(theorem["finite_evidence"]["canonical_all_zero"] is True, "theorem canonical evidence missing")
    require(theorem["finite_evidence"]["all_sector_matrices_verified_zero"] is True, "theorem zero verification missing")
    require(theorem["finite_evidence"]["nonzero_unselected_candidates_found"] == 4, "theorem candidate evidence mismatch")
    require(theorem["finite_evidence"]["conditional_non_scalar_packet_passes_tests"] is True, "conditional non-scalar evidence missing")

    decision = data["promotion_decision"]
    for key in [
        "alpha1_dotD_driver_attached_to_contract",
        "transport_only_lane_rejected_as_phase_shift_source",
        "primitive_overlap_template_emitted",
    ]:
        require(decision[key] is True, f"positive decision missing: {key}")
    for key in [
        "selected_primitive_vertex_or_basis_transport_emitted",
        "selected_primitive_overlap_contractions_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "selected_sector_response_matrices_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "full_SM_no_knob_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "selected_alpha1_dotD_driver_attached_to_differentiated_contract",
        "transport_only_C1_lane_rejected",
        "canonical_zero_response_imported_and_verified",
        "noninvariant_rank3_candidate_class_imported_as_unselected",
        "primitive_overlap_template_emitted",
        "next_source_theorem_target_sharpened",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_primitive_vertex_or_basis_transport_source_theorem",
        "selected_primitive_overlap_contractions",
        "selected_Hessian_source_vector_b_selected",
        "selected_A_selected_deltaTheta_sector_response_matrices",
        "honest_Galerkin_C1_run_values",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    for key in [
        "closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "selected_primitive_overlap_contractions_claimed",
        "selected_PhiFinC1_identity_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(cert["transport_only_no_go_proved"] is True, "certificate no-go missing")
    require(cert["primitive_overlap_template_emitted"] is True, "certificate template missing")
    require("transport-only lane is" in note, "note missing transport boundary")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
