"""Audit Phi_fin^C1 residual-projector application / Galerkin execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill"
APPLICATION = PACKET_DIR / "phifinc1_projector_application_audit.packet.json"
EXECUTION = PACKET_DIR / "honest_galerkin_execution_contract.packet.json"
DECISION = PACKET_DIR / "application_or_execution_decision.packet.json"
CERT = ROOT / "certificates" / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.py"

STATUS = (
    "MTT_SELECTED_PHIFINC1_RESIDUALPROJECTORAPPLICATION_OR_HONESTGALERKINEXECUTION_"
    "VALUEFILL_BUILT_APPLICATION_NOGO_OPEN"
)
NEXT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"
TOL = 1e-9


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    application = load(APPLICATION)
    execution = load(EXECUTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(
        application["status"] == "PROJECTOR_APPLICATION_NOT_DERIVED_BY_EXISTING_PHIFINC1_ARTIFACTS",
        "application status mismatch",
    )
    require(application["canonical_projector_available"] is True, "canonical projector unavailable")
    require(application["canonical_projector_mathematically_selected"] is True, "canonical projector not selected")
    checks = application["projector_operator_checks"]
    require(checks["fixed_projector_rank"] == 3, "fixed projector rank mismatch")
    require(checks["residual_projector_rank"] == 6, "residual projector rank mismatch")
    for key in [
        "fixed_projector_idempotence_norm_sq",
        "residual_projector_idempotence_norm_sq",
        "fixed_projector_self_adjoint_norm_sq",
        "residual_projector_self_adjoint_norm_sq",
        "orthogonal_complement_product_norm_sq",
        "partition_sum_identity_norm_sq",
    ]:
        require(abs(checks[key]) <= TOL, f"projector check nonzero: {key}")

    support = application["existing_PhiFinC1_support"]
    require(support["stationary_transport_source_layer_available"] is True, "stationary support missing")
    require(support["alpha1_dotD_driver_attached"] is True, "alpha1/dotD driver missing")
    require(support["selected_dotD_source_verified"] is True, "selected dotD source missing")
    require(support["selected_PhiFinC1_identity_claimed"] is False, "Phi_fin C1 identity overclaimed")

    no_go = application["blocking_no_go"]
    require(no_go["proved"] is True, "transport-only no-go not proved")
    require(no_go["all_sector_matrices_verified_zero"] is True, "transport-only matrices not zero")
    require(no_go["canonical_all_zero"] is True, "canonical transport-only zero flag missing")
    require("cannot" in no_go["consequence"], "no-go consequence not recorded")

    conditional = application["conditional_value_if_new_application_rule_is_proved"]
    require(conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional ATA mismatch")
    require(conditional["A_transpose_b"] == [12.0, 12.0], "conditional ATb mismatch")
    require(conditional["deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(conditional["SM_parity_dynamic_packet_would_close"] is True, "conditional SM parity implication missing")
    require(conditional["no_knob_flavor_constants_would_close"] is False, "conditional no-knob overclaim")

    for key in [
        "PhiFinC1_projector_application_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
    ]:
        require(application["promotion_decision"][key] is False, f"application overclaimed: {key}")
    require(application["observed_data_used"] is False, "application used observed data")
    require(application["target_fitting_used"] is False, "application used target fitting")

    require(execution["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_OPEN", "execution status mismatch")
    require(execution["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "manifest status mismatch")
    require(execution["selected_source_verified_now"] is False, "execution source oververified")
    require(execution["observed_flavor_data_forbidden"] is True, "observed flavor data not forbidden")
    require(execution["target_fitting_forbidden"] is True, "target fitting not forbidden")
    for key in [
        "selected_transported_zero_mode_bases",
        "selected_primitive_vertex_operator_phase_Z",
        "selected_primitive_vertex_operator_shift_X",
        "selected_basis_transport_corrections",
        "selected_Hessian_counterterms",
        "selected_L2_Gram_Schmidt_rule",
    ]:
        require(execution["required_inputs"][key] is None, f"execution input unexpectedly filled: {key}")
    for output in [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ]:
        require(output in execution["required_outputs"], f"execution output missing: {output}")
    for key in [
        "honest_Galerkin_C1_execution_promoted",
        "replacement_A_selected_promoted",
        "replacement_b_selected_promoted",
        "replacement_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
    ]:
        require(execution["promotion_decision"][key] is False, f"execution overclaimed: {key}")

    require(decision["status"] == "APPLICATION_NOGO_EXECUTION_VALUES_OPEN", "decision status mismatch")
    require("differentiated residual-projector source rule" in decision["straight_path"], "straight path mismatch")
    require("honest selected Galerkin C1 execution" in decision["superset_path"], "superset path mismatch")
    for key in [
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
        "observed_data_used",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaimed: {key}")

    for key in [
        "canonical_projector_not_enough_guardrail",
        "stationary_transport_only_application_rejected",
        "PhiFinC1_application_rule_reduced_to_new_differentiated_source_rule",
        "honest_Galerkin_execution_contract_reemitted",
        "straight_vs_superset_paths_separated",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_differentiated_residual_projector_source_rule",
        "selected_basis_transport_vertex_or_Hessian_source",
        "honest_selected_Galerkin_C1_execution_values",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "PhiFinC1_projector_application_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"candidate overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
    ]:
        require(data[key] is False, f"candidate flag overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Straight path" in note, "note missing straight path")
    require("Superset fallback" in note, "note missing superset fallback")
    require("zero one-response C1 matrices" in note, "note missing no-go")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
