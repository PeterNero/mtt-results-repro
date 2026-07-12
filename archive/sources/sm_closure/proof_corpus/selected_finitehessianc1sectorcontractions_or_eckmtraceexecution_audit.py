"""Audit finite Hessian/C1 sector contractions for E_CKM."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRICES = PACKET_DIR / "finite_hessian_c1_sector_contraction_matrices.packet.json"
TRACE_GATE = PACKET_DIR / "eckm_trace_weight_certificate_gate.packet.json"
DECISION = PACKET_DIR / "eckm_readiness_after_sector_contractions.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteHessianC1SectorContractions_or_ECKMTraceExecution_v1.md"

STATUS = "MTT_SELECTED_FINITEHESSIANC1_SECTOR_CONTRACTIONS_CLOSED_ECKM_WEIGHT_CERTS_OPEN"
NEXT = "MTT_Selected_ECKMWeightRowCertificates_or_CKMAngleClosureDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    matrices = load(MATRICES)
    trace_gate = load(TRACE_GATE)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "FiniteHessianC1SectorContractionECKMTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    require(closure["finite_Hessian_C1_sector_contraction_values_emitted"] is True, "contractions not emitted")
    require(closure["readiness_promoted_6_to_7"] is True, "readiness not promoted")
    require(closure["closed_required_rows"] == 7, "closed rows")
    require(closure["required_rows"] == 8, "required rows")
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

    require(matrices["status"] == "FINITE_HESSIAN_C1_SECTOR_CONTRACTION_MATRICES_CLOSED_FOR_ECKM", "matrices status")
    require(matrices["source_evidence"]["sector_response_matrices_closed_by_step10"] is True, "Step10 sector matrices")
    require(matrices["source_evidence"]["all_72_primitive_rows_exact"] is True, "72 rows")
    require(matrices["source_evidence"]["formal_110_rows_executed"] is True, "110 rows")
    require(matrices["sector_routing"] == {"d": "shift_R_X", "e": "phase_R_Z", "nuD": "shift_R_X", "u": "phase_R_Z"}, "routing")
    require(matrices["promotes_finite_Hessian_C1_sector_contraction_values"] is True, "matrix promotion")
    require(matrices["does_not_emit_ECKM_weight_rows"] is True, "matrix overclaim")
    require(abs(matrices["diagnostics"]["u"]["frobenius_norm_sq"] - 4.0) < 1e-12, "R_Z norm")
    require(abs(matrices["diagnostics"]["d"]["frobenius_norm_sq"] - 2.0) < 1e-12, "R_X norm")
    require(matrices["observed_data_used_as_selector"] is False, "matrix observed selector")
    require(matrices["target_fitting_used"] is False, "matrix target fit")

    require(trace_gate["status"] == "ECKM_TRACE_WEIGHT_ROW_CERTIFICATES_REMAIN_OPEN", "trace gate status")
    require(trace_gate["selected_functional_executed"] is False, "trace executed")
    require(trace_gate["accepted_weight_rows"] == 0, "trace weights")
    require("finite Hessian/C1 sector contraction matrices" in trace_gate["ready_inputs"], "ready contractions")
    require("three selected row certificates for Pi_CKM^12, Pi_CKM^23, Pi_CKM^13" in trace_gate["missing_inputs"], "missing certs")
    require(abs(trace_gate["required_postcheck_values"]["W12"] - 1.41236734693301) < 1e-12, "W12")
    require(trace_gate["observed_data_used_as_selector"] is False, "trace observed selector")
    require(trace_gate["target_fitting_used"] is False, "trace target fit")

    require(decision["status"] == "ECKM_READINESS_7_OF_8_WEIGHT_CERTIFICATES_OPEN", "decision status")
    require(decision["previous_closed_required_rows"] == 6, "decision previous")
    require(decision["closed_required_rows"] == 7, "decision closed")
    require(decision["required_rows"] == 8, "decision required")
    require(decision["finite_Hessian_C1_sector_contraction_values_emitted"] is True, "decision contractions")
    require(decision["E_CKM_weight_row_certificates_emitted"] is False, "decision cert rows")
    require(decision["still_open_blockers"] == ["E_CKM_weight_row_certificates"], "open blocker")
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
    require(nums["previous_readiness"] == 6, "key previous")
    require(nums["current_readiness"] == 7, "key current")
    require(nums["required_rows"] == 8, "key required")
    require(abs(nums["phase_R_Z_frobenius_norm_sq"] - 4.0) < 1e-12, "key RZ")
    require(abs(nums["shift_R_X_frobenius_norm_sq"] - 2.0) < 1e-12, "key RX")
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["readiness_promoted_6_to_7"] is True, "cert readiness")
    require(cert["closed_required_rows"] == 7, "cert closed")
    require(cert["accepted_weight_rows"] == 0, "cert accepted")
    require(cert["closure_claimed"] is False, "cert closure")
    require("current readiness  = 7/8" in note, "note readiness")
    require("accepted W rows    = 0/3" in note, "note weights")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
