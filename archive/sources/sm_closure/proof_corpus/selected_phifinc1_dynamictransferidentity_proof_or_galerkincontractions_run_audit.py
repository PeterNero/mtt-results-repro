"""Audit PhiFinC1 dynamic-transfer proof / Galerkin contractions run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
CERT = ROOT / "certificates" / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.py"

STATUS = "MTT_SELECTED_PHIFINC1_DYNAMICTRANSFERIDENTITY_PROOF_OR_GALERKINCONTRACTIONS_RUN_BUILT_STATIONARY_TRACE_CLOSED_C1_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    coord = data["coordinate_system"]
    require(coord["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(coord["columns"] == ["phase_packet", "shift_packet"], "coordinate columns mismatch")

    stationary = data["stationary_trace_import"]
    for key in [
        "selected_source_verified",
        "selected_projector_source_verified",
        "selected_riesz_green_source_verified",
        "selected_rho_s_validator_ready",
        "transport_closed_finite_validator_replay",
        "symbolic_transport_conjugation_validator_extended",
        "functional_gauge_transported_trace_proved",
        "finite_raw_truncation_aliasing_bypassed_by_symbolic_transport",
    ]:
        require(stationary[key] is True, f"stationary import not closed: {key}")
    require(
        stationary["selected_dotD_source_verified_inside_stationary_transport_replay"] is False,
        "stationary replay overclaims dotD",
    )
    require(
        stationary["alpha1_driver_verified_inside_stationary_transport_replay"] is False,
        "stationary replay overclaims alpha1",
    )

    alpha1_import = stationary["crossrepo_alpha1_dotD_support"]
    require(alpha1_import["import_available"] is True, "cross-repo alpha1 import not recorded")
    require(alpha1_import["selected_dotD_source_verified_imported"] is True, "imported dotD support missing")
    require(alpha1_import["alpha1_driver_verified_imported"] is True, "imported alpha1 support missing")
    require(alpha1_import["primitive_C1_contractions_claimed_by_import"] is False, "primitive C1 overclaimed by import")
    require(alpha1_import["A_selected_claimed_by_import"] is False, "A_selected overclaimed by import")
    require(alpha1_import["b_selected_claimed_by_import"] is False, "b_selected overclaimed by import")

    boundary = data["phifin_payload_boundary"]
    require(boundary["all_support_shapes_present"] is True, "PhiFin support shapes missing")
    require(boundary["all_selected_values_emitted"] is False, "PhiFin values overemitted")
    require(boundary["finite_Hessian_C1_source_selected"] is False, "Hessian selected overclaimed")
    require(boundary["primitive_C1_contractions_selected"] is False, "primitive C1 selected overclaimed")
    require(boundary["dotD_alpha1_selected_inside_phifin_payload"] is False, "PhiFin dotD selected overclaimed")

    identity = data["PhiFinC1_identity_attempt"]
    require(identity["stationary_trace_sufficient_for_C1_transfer_identity"] is False, "stationary trace marked sufficient")
    require(identity["selected_identity_proved_now"] is False, "PhiFinC1 identity overproved")
    require(identity["normal_form_values_not_promoted_now"] is True, "normal-form guard missing")
    require(len(identity["missing_dynamic_objects"]) == 5, "missing dynamic object count mismatch")
    require(identity["if_future_identity_proved_then_values"]["deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")

    galerkin = data["Galerkin_run_attempt"]
    require(galerkin["stationary_support_reused"]["stationary_support_closed_by_transport_conjugation"] is True, "stationary support not reused")
    require(galerkin["open_dynamic_stages"]["C1_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "C1 manifest status mismatch")
    require(galerkin["open_dynamic_stages"]["C1_manifest_selected_source_verified"] is False, "C1 manifest oververified")
    require(galerkin["can_promote_honest_galerkin_C1_now"] is False, "Galerkin C1 overpromoted")

    theorem = data["partial_promotion_theorem"]
    require(theorem["proved"] is True, "theorem not proved")
    require(theorem["corollary_now"]["stationary_source_layer_closed"] is True, "stationary corollary missing")
    require(theorem["corollary_now"]["C1_dynamic_layer_closed"] is False, "C1 corollary overclosed")
    require(theorem["corollary_now"]["selected_A_b_delta_promoted"] is False, "A/b/delta overpromoted")

    closes = data["what_closes_now"]
    for key in [
        "stationary_PhiFin_trace_imported_as_selected_source",
        "selected_projector_riesz_green_rho_s_layer_closed",
        "stationary_trace_insufficiency_for_C1_transfer_proved",
        "PhiFinC1_or_Galerkin_live_target_sharpened",
        "normal_form_values_preserved_as_conditional_only",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_differentiated_PhiFinC1_transfer_identity",
        "primitive_C1_overlap_contractions",
        "selected_Hessian_source_vector_b_selected",
        "selected_A_selected_deltaTheta_sector_response_matrices",
        "honest_Galerkin_C1_run_or_equivalent_symbolic_contractions",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")
    require(remains["selected_dotD_alpha1_attached_to_PhiFinC1"] is False, "imported dotD not reflected")
    require(remains["selected_alpha1_driver_attached_to_PhiFinC1"] is False, "imported alpha1 not reflected")

    decision = data["promotion_decision"]
    require(decision["stationary_source_layer_promoted"] is True, "stationary layer not promoted")
    for key in [
        "selected_PhiFinC1_identity_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "selected_sector_response_matrices_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "full_SM_no_knob_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    for key in [
        "closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "selected_PhiFinC1_identity_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("stationary trace theorem" in note, "note missing stationary boundary")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
