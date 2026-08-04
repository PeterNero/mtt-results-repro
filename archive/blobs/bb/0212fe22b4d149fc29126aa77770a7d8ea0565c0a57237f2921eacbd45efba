"""Audit zero-mode/Gram readiness promotion for E_CKM."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STATIONARY = PACKET_DIR / "stationary_transported_basis_import_for_eckm.packet.json"
GRAM = PACKET_DIR / "gram_trace_convention_for_eckm.packet.json"
CONTRACTIONS = PACKET_DIR / "sector_contraction_value_gap.packet.json"
DECISION = PACKET_DIR / "eckm_readiness_after_zeromode_gram_import.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ZeroModeGramSectorContractionPayload_or_ECKMWeightRows_v1.md"

STATUS = "MTT_SELECTED_ZEROMODE_GRAM_ECKM_READINESS_PROMOTED_SECTOR_CONTRACTIONS_OPEN"
NEXT = "MTT_Selected_FiniteHessianC1SectorContractions_or_ECKMTraceExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    stationary = load(STATIONARY)
    gram = load(GRAM)
    contractions = load(CONTRACTIONS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "ZeroModeGramECKMReadinessPromotionTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    require(closure["zero_mode_projector_basis_values_promoted"] is True, "zero-mode not promoted")
    require(closure["selected_L2_Gram_trace_convention_values_promoted"] is True, "Gram not promoted")
    require(closure["readiness_promoted_4_to_6"] is True, "readiness not promoted")
    require(closure["closed_required_rows"] == 6, "closed count")
    require(closure["required_rows"] == 8, "required count")
    require(closure["finite_Hessian_C1_sector_contraction_values_emitted"] is False, "contractions overemitted")
    require(closure["E_CKM_weight_row_certificates_emitted"] is False, "cert rows overemitted")
    require(closure["selected_functional_executed"] is False, "functional overexecuted")
    require(closure["accepted_weight_rows"] == 0, "accepted weights")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    require(stationary["status"] == "STATIONARY_TRANSPORTED_ZERO_MODE_PROJECTOR_BASIS_IMPORTED_FOR_ECKM", "stationary status")
    require(stationary["transported_projectors_selected_at_stationary_tier"] is True, "projectors")
    require(stationary["all_stationary_slots_verified"] is True, "stationary slots")
    require(stationary["validator_ready_stationary_rho_s"] is True, "rho_s")
    require(stationary["active_ledger_supplies_dotD_alpha1"] is True, "active dotD")
    require(stationary["promotes_eckm_zero_mode_projector_basis_readiness"] is True, "stationary promotion")
    require(stationary["does_not_emit_sector_contraction_values"] is True, "stationary overclaim")
    for sector in ["u", "d", "e"]:
        require(len(stationary["sector_basis_labels_for_ECKM"][sector]) == 3, f"{sector} basis labels")
    require(stationary["observed_data_used_as_selector"] is False, "stationary observed selector")
    require(stationary["target_fitting_used"] is False, "stationary target fit")

    require(gram["status"] == "GRAM_TRACE_CONVENTION_PROMOTED_FOR_STATIONARY_ECKM_DOMAIN", "gram status")
    require(gram["conditional_gram_theorem_proved"] is True, "conditional gram")
    require(gram["gram_conditionally_forced_after_rho_s"] is True, "forced gram")
    require(gram["stationary_rho_s_available_from_B1"] is True, "gram rho_s")
    require(gram["selected_projector_basis_available_from_B1"] is True, "gram basis")
    require(gram["active_dotD_closure_imported"] is True, "gram dotD")
    require(gram["matter_T3_norms_equal"] is True, "T3 norms")
    require(abs(gram["raw_T3_frobenius_norm_per_matter_sector"] - 2 ** 0.5) < 1e-12, "T3 norm value")
    require(gram["promotes_eckm_Gram_trace_readiness"] is True, "gram promotion")
    require(gram["physical_transfer_normalization_selected_in_old_packet"] is False, "old packet should remain old-open")
    require(gram["observed_data_used_as_selector"] is False, "gram observed selector")
    require(gram["target_fitting_used"] is False, "gram target fit")

    require(contractions["status"] == "FINITE_HESSIAN_C1_SECTOR_CONTRACTION_VALUES_REMAIN_OPEN", "contractions status")
    require(contractions["selected_source_verified"] is False, "contractions source oververified")
    require(contractions["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "manifest status")
    require("finite three-by-three contraction terms in transported bases" in contractions["still_missing_for_ECKM"], "missing contraction gap")
    require(contractions["observed_flavor_data_forbidden"] is True, "observed flavor forbidden")
    require(contractions["target_fitting_forbidden"] is True, "target fitting forbidden")

    require(decision["status"] == "ECKM_READINESS_6_OF_8_SECTOR_CONTRACTIONS_OPEN", "decision status")
    require(decision["previous_closed_required_rows"] == 4, "decision previous")
    require(decision["closed_required_rows"] == 6, "decision closed")
    require(decision["required_rows"] == 8, "decision required")
    require(decision["zero_mode_projector_basis_values_promoted"] is True, "decision zero-mode")
    require(decision["selected_L2_Gram_trace_convention_values_promoted"] is True, "decision Gram")
    require(decision["finite_Hessian_C1_sector_contraction_values_emitted"] is False, "decision contractions")
    require(decision["E_CKM_weight_row_certificates_emitted"] is False, "decision cert rows")
    require(
        set(decision["still_open_blockers"])
        == {"finite_Hessian_C1_sector_contraction_values", "E_CKM_weight_row_certificates"},
        "open blockers",
    )
    require(decision["next_required_artifact"] == NEXT, "decision next")
    for key in [
        "selected_functional_executed",
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")

    nums = data["key_numbers"]
    require(nums["previous_readiness"] == 4, "key previous readiness")
    require(nums["current_readiness"] == 6, "key current readiness")
    require(nums["required_rows"] == 8, "key required")
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted weights")
    require(abs(nums["required_q448_weights"]["W12"] - 1.41236734693301) < 1e-12, "W12")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["readiness_promoted_4_to_6"] is True, "cert readiness")
    require(cert["closed_required_rows"] == 6, "cert closed")
    require(cert["accepted_weight_rows"] == 0, "cert weights")
    require(cert["closure_claimed"] is False, "cert closure")
    require("current readiness  = 6/8" in note, "note readiness")
    require("accepted W rows    = 0/3" in note, "note weights")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
