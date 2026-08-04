"""Audit differentiated PhiFinC1 primitive-overlap / Galerkin import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import.candidate.json"
CERT = ROOT / "certificates" / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import_certificate.json"
TEMPLATE = (
    ROOT
    / "candidate_data"
    / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import"
    / "primitive_overlap_contractions.template.json"
)
NOTE = ROOT / "proof_corpus" / "DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.py"

STATUS = "DIFFERENTIATED_PHIFINC1_PRIMITIVE_OVERLAP_IMPORTED_TRANSPORT_NOGO_TEMPLATE_OPEN"
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
    cert = load(CERT)
    template = load(TEMPLATE)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(cert["theorem"]["proved"] is True, "certificate theorem not proved")
    require(all(data["checks"].values()), "not all import checks passed")

    coord = data["coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(coord["columns"] == ["phase_packet", "shift_packet"], "coordinate columns mismatch")

    driver = data["driver_contract"]
    require(driver["selected_dotD_source_verified"] is True, "dotD source not attached")
    require(driver["alpha1_driver_verified"] is True, "alpha1 driver not attached")
    require(driver["honest_dotD_alpha1_replay"] is True, "honest replay missing")
    require(driver["attached_to_differentiated_contract_as_driver"] is True, "driver not attached")
    require(driver["primitive_overlap_values_emitted_by_driver"] is False, "driver overclaims values")

    nogo = data["transport_only_no_go_theorem"]
    canonical = data["canonical_transport_only_test"]
    require(nogo["proved"] is True, "transport-only no-go missing")
    require(canonical["all_c1_matrices_zero_for_canonical_tensor"] is True, "canonical zero missing")
    require(canonical["all_sector_matrices_verified_zero"] is True, "canonical sectors not zero")
    require(canonical["can_emit_phase_shift_columns"] is False, "canonical lane overclaims phase/shift")

    noninv = data["noninvariant_candidate_import"]
    require(noninv["active_shift"] == [1, 1], "active shift mismatch")
    require(noninv["selected_by_theorem"] is False, "unselected candidates overselected")
    require(noninv["primitive_envelope_constructed"] is True, "primitive envelope missing")
    require(noninv["primitive_envelope_selected_as_dynamic_tensor"] is False, "primitive envelope overselected")
    require(noninv["candidate_summary"]["fixed_fiber_candidates"] == [0, 1, 2], "fixed fibers mismatch")
    require(noninv["candidate_summary"]["all_fixed_fiber_rank_three"] is True, "rank-three fixed fibers missing")
    require(noninv["candidate_summary"]["all_fiber_rank_one"] is True, "all-fiber rank-one envelope missing")

    contract = data["differentiated_primitive_overlap_contract"]
    require(contract["template_status"] == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING", "contract template status mismatch")
    require(contract["normal_form_values_promoted_now"] is False, "normal-form values overpromoted")
    require("M_s^r[i,j]" in contract["primitive_overlap_formula"], "primitive formula missing")
    require(len(contract["acceptance_equations"]) == 5, "acceptance equations changed")

    require(template["status"] == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING", "template status mismatch")
    require(template["coordinate_system"] == coord, "template coordinate mismatch")
    for sector in SECTORS:
        require(
            template["required_selected_values"]["primitive_three_by_three_contraction_terms"][sector] is None,
            f"primitive slot filled: {sector}",
        )
        require(
            template["required_selected_values"]["linear_response_matrices"][sector] is None,
            f"linear response slot filled: {sector}",
        )
        require(
            template["required_selected_values"]["Hessian_counterterms"][sector] is None,
            f"Hessian slot filled: {sector}",
        )
    for key in [
        "A_selected_72_real_columns",
        "b_selected_72_real_source_vector",
        "deltaTheta_C1",
        "selected_primitive_vertex_operator_phase_Z",
        "selected_primitive_vertex_operator_shift_X",
        "transported_zero_mode_bases",
    ]:
        require(template["required_selected_values"][key] is None, f"template scalar slot filled: {key}")

    values = data["conditional_dynamic_values_retained_as_unpromoted"]
    require(values["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional Gram mismatch")
    require(values["A_transpose_b_conditional"] == [12.0, 12.0], "conditional A^T b mismatch")
    require(values["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0], "conditional deltaTheta mismatch")

    decision = data["promotion_decision"]
    for key in [
        "selected_primitive_vertex_or_basis_transport_emitted",
        "selected_primitive_overlap_contractions_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "full_SM_no_knob_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    guard = data["guardrails"]
    require(guard["transport_only_lane_rejected"] is True, "transport-only rejection missing")
    for key in [
        "selected_primitive_overlap_contractions_claimed",
        "selected_primitive_vertex_source_claimed",
        "selected_A_selected_claimed",
        "selected_b_selected_claimed",
        "selected_deltaTheta_C1_claimed",
        "honest_Galerkin_C1_contractions_claimed",
        "observed_data_used",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require(cert["transport_only_no_go_proved"] is True, "certificate no-go missing")
    require(cert["primitive_overlap_template_emitted"] is True, "certificate template missing")
    require("canonical transport-only lane is rejected" in note, "note missing no-go boundary")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
