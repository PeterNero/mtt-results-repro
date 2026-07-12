"""Audit CKM scalar evaluator readiness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READINESS = PACKET_DIR / "eckm_scalar_evaluator_readiness.packet.json"
FORMAL = PACKET_DIR / "formal_eckm_evaluator_instantiation.packet.json"
GAP = PACKET_DIR / "remaining_flavor_galerkin_value_gap.packet.json"
DECISION = PACKET_DIR / "eckm_scalar_evaluator_acceptance_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1.md"

STATUS = "MTT_SELECTED_CKMWEIGHT_SCALAR_EVALUATOR_READINESS_BUILT_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ZeroModeGramSectorContractionPayload_or_ECKMWeightRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    readiness = load(READINESS)
    formal = load(FORMAL)
    gap = load(GAP)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "CKMWeightScalarEvaluatorReadinessTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    for key in ["eckm_readiness_updated", "formal_evaluator_typed", "stale_source_blockers_retired"]:
        require(closure[key] is True, f"missing true closure flag: {key}")
    require(closure["closed_required_rows"] == 4, "closed readiness count")
    require(closure["required_rows"] == 8, "required readiness count")
    for key in [
        "selected_zero_mode_basis_values_emitted",
        "selected_Gram_trace_values_emitted",
        "finite_Hessian_C1_sector_contraction_values_emitted",
        "selected_functional_executed",
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")
    require(closure["accepted_weight_rows"] == 0, "accepted weight rows")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "exact correction rows")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob CKM rows")

    require(readiness["status"] == "ECKM_READINESS_UPDATED_AFTER_ACTIVE_LEDGER_IMPORT", "readiness status")
    require(readiness["closed_required_rows"] == 4, "readiness closed count")
    require(readiness["required_rows"] == 8, "readiness required count")
    rows = readiness["readiness_rows"]
    for key in [
        "q448_projection_contract",
        "selected_q79_heavylink_orbit_domain",
        "active_dotD_C1_first_response_source_layer",
        "DE_Riesz_Green_gap_layer",
    ]:
        require(rows[key]["closed"] is True, f"expected closed row {key}")
    for key in [
        "zero_mode_projector_basis_values",
        "selected_L2_Gram_trace_convention_values",
        "finite_Hessian_C1_sector_contraction_values",
        "E_CKM_weight_row_certificates",
    ]:
        require(rows[key]["closed"] is False, f"expected open row {key}")
        require(key in readiness["still_open_blockers"], f"missing blocker {key}")
    require("generic dotD_alpha1 source absence" in readiness["stale_blockers_retired"], "dotD stale blocker not retired")
    require(readiness["observed_data_used_as_selector"] is False, "readiness observed selector")
    require(readiness["target_fitting_used"] is False, "readiness target fit")

    require(formal["status"] == "FORMAL_ECKM_EVALUATOR_TYPED_NOT_EXECUTED", "formal status")
    require("E_CKM^ij = Tr_N" in formal["evaluator"], "formal evaluator")
    require(formal["selected_functional_executed"] is False, "formal executed")
    require(formal["accepted_weight_rows"] == 0, "formal accepted rows")
    require(abs(formal["rows"]["W12"]["required_postcheck_weight"] - 1.41236734693301) < 1e-12, "W12")
    require(abs(formal["rows"]["W23"]["required_postcheck_weight"] - 6.829844553504131) < 1e-12, "W23")
    require(abs(formal["rows"]["W13"]["required_postcheck_weight"] - 23.10800759390179) < 1e-12, "W13")
    require("zero_mode_projector_basis_values" in formal["inputs_not_available_as_values"], "formal zero-mode blocker")
    require(formal["observed_data_used_as_selector"] is False, "formal observed selector")
    require(formal["target_fitting_used"] is False, "formal target fit")

    require(gap["status"] == "ZERO_MODE_GRAM_SECTOR_CONTRACTION_PAYLOAD_REMAINS_OPEN", "gap status")
    require(gap["overlap_with_rtheta_scalar_frontier"] is True, "Rtheta overlap")
    require(gap["rtheta_selected_functional_executed"] is False, "Rtheta executed")
    require(gap["rtheta_accepted_scalar_row_count_now"] == 0, "Rtheta scalar count")
    require(gap["zero_mode_validator_passes_now"] is False, "zero-mode validator overpassed")
    require(gap["minimal_next_payload"]["name"] == NEXT, "gap next")
    require("selected sector zero-mode projectors P_u,P_d,P_e and ordered bases K_u,K_d,K_e" in gap["minimal_next_payload"]["must_emit"], "gap zero-mode payload")
    require(gap["observed_data_used_as_selector"] is False, "gap observed selector")
    require(gap["target_fitting_used"] is False, "gap target fit")

    require(decision["status"] == "ECKM_DOMAIN_READY_VALUE_EXECUTION_OPEN", "decision status")
    require(decision["eckm_readiness_updated"] is True, "decision readiness")
    require(decision["closed_required_rows"] == 4, "decision closed")
    require(decision["required_rows"] == 8, "decision required")
    require(decision["formal_evaluator_typed"] is True, "decision formal")
    require(decision["selected_functional_executed"] is False, "decision executed")
    require(decision["accepted_weight_rows"] == 0, "decision weights")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")

    nums = data["key_numbers"]
    require(nums["readiness_closed_required_rows"] == 4, "key readiness closed")
    require(nums["readiness_required_rows"] == 8, "key readiness required")
    require(nums["rtheta_accepted_scalar_row_count_now"] == 0, "key Rtheta")
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted weights")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["closed_required_rows"] == 4, "cert closed")
    require(cert["required_rows"] == 8, "cert required")
    require(cert["selected_functional_executed"] is False, "cert executed")
    require(cert["accepted_weight_rows"] == 0, "cert weights")
    require(cert["closure_claimed"] is False, "cert closure")
    require("closed required rows = 4/8" in note, "note readiness")
    require("accepted W rows      = 0/3" in note, "note weight rows")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
