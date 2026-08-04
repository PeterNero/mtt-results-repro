"""Audit primitive-vertex / basis-transport source selection theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_primitivevertex_source_or_basistransport_selectiontheorem"
    / "primitive_vertex_source_selector.packet.json"
)
CERT = ROOT / "certificates" / "selected_primitivevertex_source_or_basistransport_selectiontheorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitivevertex_source_or_basistransport_selectiontheorem.py"

STATUS = "MTT_SELECTED_PRIMITIVEVERTEX_SOURCE_OR_BASISTRANSPORT_SELECTIONTHEOREM_BUILT_SOURCE_SELECTOR_CLOSED_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(packet["status"] == "SELECTED_SOURCE_SELECTOR_EMITTED_VALUES_OPEN", "selector packet status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    coord = data["coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(coord["columns"] == ["phase_packet", "shift_packet"], "coordinate columns mismatch")

    components = packet["selector_components"]
    require(packet["same_source"] is True, "selector packet not same-source")
    require(components["source_level_qutrit_weyl_carrier"]["selected"] is True, "Weyl carrier not selected")
    require(components["source_level_qutrit_weyl_carrier"]["phase_generator"] == "Z", "phase generator mismatch")
    require(components["source_level_qutrit_weyl_carrier"]["shift_generator"] == "X", "shift generator mismatch")
    require(components["active_deck_shift"]["selected"] is True, "active shift not selected")
    require(components["active_deck_shift"]["value"] == [1, 1], "active shift mismatch")
    require(components["fixed_fiber_quotient"]["selected_for_current_observables"] is True, "fiber quotient not selected")
    require(components["fixed_fiber_quotient"]["absolute_fiber_origin_selected"] is False, "absolute fiber origin overselected")
    require(components["fixed_fiber_quotient"]["fixed_fiber_class"] == [0, 1, 2], "fiber class mismatch")
    require(components["static_sector_route"]["selected"] is True, "static sector route not selected")
    require(components["static_sector_route"]["phase_Z_to"] == ["u", "e"], "phase route mismatch")
    require(components["static_sector_route"]["shift_X_to"] == ["d", "nuD"], "shift route mismatch")
    require(components["static_overlap_transfer_normalization"]["selected"] is True, "overlap normalization not selected")
    require("rho_s(T_i)/sqrt(2)" in components["static_overlap_transfer_normalization"]["unit_trace_transfer"], "unit transfer mismatch")
    require(components["alpha1_dotD_driver"]["selected_dotD_source_verified"] is True, "dotD source not selected")
    require(components["alpha1_dotD_driver"]["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(components["alpha1_dotD_driver"]["honest_dotD_alpha1_replay"] is True, "honest dotD replay missing")

    for key in [
        "primitive_three_by_three_contraction_terms",
        "differentiated_vertex_integrals",
        "Hessian_counterterms",
        "A_selected_72_real_columns",
        "b_selected_source_vector",
        "deltaTheta_C1",
        "sector_response_matrices",
    ]:
        require(packet["values_not_emitted"][key] is True, f"value-emission guard missing: {key}")

    theorem = data["source_selector_theorem"]
    require(theorem["proved"] is True, "source selector theorem not proved")
    require(len(theorem["proof_steps"]) == 7, "proof-step count mismatch")
    for phrase in [
        "primitive overlap contraction values",
        "A_selected or selected 72-real phase/shift columns",
        "deltaTheta_C1",
    ]:
        require(phrase in theorem["what_this_does_not_prove"], f"missing theorem guard: {phrase}")

    boundary = data["transfer_boundary"]
    require(boundary["conditional_source_to_C1_transfer_exact"] is True, "conditional transfer not exact")
    require(boundary["old_selected_transfer_map_emitted"] is False, "old selected transfer unexpectedly emitted")
    require(boundary["updated_by_this_artifact"]["source_selector_for_transfer_promoted"] is True, "selector not promoted")
    require(boundary["updated_by_this_artifact"]["dynamic_overlap_tensor_values_promoted"] is False, "dynamic values overpromoted")
    require(boundary["updated_by_this_artifact"]["normal_form_values_promoted"] is False, "normal-form values overpromoted")

    template = data["template_instantiation"]
    require(template["selector_attached"] is True, "selector not attached to template")
    require(template["selected_values_filled"] is False, "template values overfilled")
    require(len(template["next_fill_fields"]) == 6, "next fill fields mismatch")

    decision = data["promotion_decision"]
    require(decision["source_selector_promoted"] is True, "source selector not promoted")
    require(decision["selected_primitive_vertex_or_basis_transport_source_promoted"] is True, "primitive source selector not promoted")
    for key in [
        "selected_primitive_overlap_contractions_promoted",
        "selected_dynamic_overlap_tensor_promoted",
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
        "primitive_vertex_source_selector_emitted",
        "source_level_ZX_carrier_imported",
        "active_shift_and_fiber_quotient_imported",
        "static_sector_route_imported",
        "static_trace_transfer_normalization_imported",
        "alpha1_dotD_driver_imported",
        "value_emission_target_reduced_to_primitive_overlap_contractions",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_primitive_overlap_contraction_values",
        "selected_vertex_integrals_or_honest_Galerkin_C1_values",
        "selected_Hessian_source_vector_b_selected",
        "selected_A_selected_deltaTheta_sector_response_matrices",
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

    require(cert["source_selector_promoted"] is True, "certificate selector flag missing")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require("This does not emit primitive overlap values" in note, "note missing value guard")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
