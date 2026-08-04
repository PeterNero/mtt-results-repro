"""Audit Step 30 projective B_N mechanical lift / visible source cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MECHANICAL = PACKET_DIR / "step30_projective_bn_mechanical_lift.packet.json"
SOURCE_GAP = PACKET_DIR / "step30_visible_operator_source_gap.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step30_next_visible_source_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step30_ProjectiveBNMechanicalLift_or_VisibleSourceCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP30_PROJECTIVEBN_MECHANICAL_LIFT_BUILT_VISIBLE_OPERATOR_SOURCE_OPEN"
NEXT = "MTT_Selected_Step31_VisibleChernWeilOperatorSource_or_SelectedProjectiveBNValues_v1"
SECTORS = {"Q", "u", "d", "L", "e", "N", "H"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    mechanical = load(MECHANICAL)
    source_gap = load(SOURCE_GAP)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(mechanical["from_step29"]["identity_rhoE_smoke_retired"] is True, "identity smoke not retired")
    require(mechanical["from_step29"]["nonidentity_projective_rhoE_candidate_imported"] is True, "projective candidate not imported")
    scaffold = mechanical["smooth_BN_scaffold"]
    require(scaffold["dimension"] == 27 and scaffold["basis_count"] == 27, "wrong BN dimension")
    require(scaffold["zero_cluster_dimension"] == 3, "wrong zero cluster")
    require(scaffold["complement_gap"] > 0, "gap missing")
    require(scaffold["ordinary_bundle_equivariance"] is False, "ordinary equivariance should be false")
    require(scaffold["projective_equivariance_up_to_central_phase"] is True, "projective equivariance missing")
    fields = mechanical["mechanical_fields_closed"]
    for key in [
        "smooth_scalar_basis_functions_phi_m",
        "metric_volume_quadrature",
        "Gram_matrix_entries",
        "stiffness_matrix_entries",
        "generalized_eigenpairs",
        "Riesz_projectors",
        "reduced_Green_operators",
        "projective_bundle_transition_or_equivariance",
        "D_E_matrix_on_27_mode_BN",
        "ordered_zero_mode_bases",
        "sector_projectors_on_27_mode_BN",
        "dotD_alpha1_matrix_in_same_basis",
    ]:
        require(fields[key] is True, f"mechanical field not closed: {key}")
    validation = mechanical["mechanical_validation"]
    require(validation["D_E_diagnostic_validator_passes"] is True, "D_E diagnostic failed")
    require(validation["D_E_honest_validator_fails_only_by_selected_source_flags"] is True, "D_E failure not isolated")
    require(validation["dotD_diagnostic_validator_passes"] is True, "dotD diagnostic failed")
    require(validation["dotD_honest_validator_fails_only_by_source_driver_flags"] is True, "dotD failure not isolated")
    require(set(validation["projector_residuals"]) == SECTORS, "sector residual set mismatch")
    for sector, item in validation["projector_residuals"].items():
        expected = 1.0 if sector == "H" else 3.0
        require(item["idempotence_residual"] == 0.0, f"idempotence residual: {sector}")
        require(item["hermitian_residual"] == 0.0, f"hermitian residual: {sector}")
        require(item["rank_trace"] == expected, f"rank mismatch: {sector}")
    for key in [
        "selected_visible_operator_source",
        "selected_source_verified_operator_flags",
        "full_iwasawa_strominger_DE_not_only_model_active",
        "operator_level_projective_rhoE_transition",
        "internal_Rtheta_scalar_rows",
    ]:
        require(mechanical["not_closed_by_mechanical_lift"][key] is True, f"mechanical overclosed: {key}")

    s3 = source_gap["s3_projective_source_status"]
    require(s3["source_level_projective_gerbe_rhoE_promoted"] is True, "S3 source not promoted")
    require(s3["operator_level_projective_rhoE_promoted"] is False, "operator rhoE overpromoted")
    require(s3["fixed_differential_cohomology_class"] is True, "cohomology class not fixed")
    require(s3["freed_witten_verified"] is True, "FW not verified")
    require(s3["green_schwarz_bianchi_verified"] is True, "GS/Bianchi not verified")
    require(s3["map_to_central_cocycle_verified"] is True, "central cocycle map missing")
    require(s3["coherent_spectral_projector_verified"] is False, "spectral projector oververified")
    for key in [
        "Chern_Weil_row_derived_from_selected_source",
        "HYM_or_Route_C_residual_for_visible_source",
        "coherent_spectral_zero_mode_projectors",
        "selected_D_E_dotD_Riesz_Green",
        "selected_visible_bundle_or_sheaf_model",
    ]:
        require(source_gap["remaining_cut_set"][key] is True, f"source cutset missing: {key}")
    require(source_gap["closure_claimed"] is False, "source gap overclaimed")

    require(contract["next_required_artifact"] == NEXT, "contract next mismatch")
    require(contract["closure_claimed"] is False, "contract overclaimed")
    for phrase in [
        "selected visible bundle/sheaf or Route-C source on q79/F,m=1",
        "Chern-Weil derivation of Tr_F_visible^2 from that selected source",
        "operator-level projective rho_E transition on the smooth projective B_N basis",
        "selected_source_verified=true for D_E in all Q,u,d,L,e,N,H slots by theorem",
        "selected_dotD_source_verified=true and alpha1_driver_verified=true in all Q,u,d,L,e,N,H slots by theorem",
    ]:
        require(phrase in contract["must_emit_next"], f"must emit missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "identity_rhoE_smoke_route_retired",
        "projective_BN_mechanical_lift_fields_closed",
        "smooth_scalar_basis_quadrature_gram_stiffness_closed",
        "model_active_D_E_projectors_Green_dotD_emitted",
        "source_level_projective_gerbe_rhoE_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_visible_operator_source_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_source_verified_operator_flags_closed",
        "coherent_spectral_projector_verified",
        "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["projective_BN_mechanical_lift_fields_closed"] is True, "certificate mechanical close missing")
    require(cert["selected_visible_operator_source_closed"] is False, "certificate overclosed visible source")
    require(cert["operator_sector_values_closed"] is False, "certificate overclosed operator values")

    for phrase in [
        "smooth projective B_N basis/quadrature/Gram         closed mechanically",
        "selected visible Chern-Weil/operator source         open",
        "operator-level projective rho_E transition          open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
