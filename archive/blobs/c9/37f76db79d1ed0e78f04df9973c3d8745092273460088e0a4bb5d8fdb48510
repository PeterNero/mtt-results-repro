"""Audit S3 restriction/projector and projective response-hunt import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "s3_restriction_and_projective_response_hunt_import.candidate.json"
CERT = ROOT / "certificates" / "s3_restriction_and_projective_response_hunt_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "S3_Restriction_and_Projective_Response_Hunt_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_s3_restriction_and_projective_response_hunt.py"

STATUS = "S3_RESTRICTION_PROJECTIVE_RESPONSE_HUNT_IMPORTED_SMOOTH_RESPONSE_OPEN"
NEXT = "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Interface_v1"


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
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["parallel_next_required_artifact"] == PARALLEL_NEXT, "candidate parallel next mismatch")
    require(cert["parallel_next_required_artifact"] == PARALLEL_NEXT, "certificate parallel next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    sm = data["sm_s3_restriction_projector_packet"]
    restriction = sm["restriction_packet"]
    require(restriction["S3_active_image_rank_over_F3"] == 2, "S3 rank mismatch")
    require(restriction["finite_total_twisted_DD_class_zero"] is True, "twisted DD not zero")
    require(restriction["ordinary_S3_DD_zero"] is False, "ordinary S3 DD should be rejected")
    require(restriction["W3_spinC_zero_for_visible_complex_worldvolume_class"] is True, "W3/spinC missing")
    require(restriction["twisted_stack"] == "S3", "twisted stack mismatch")

    projectors = sm["projector_retention_packet"]
    require(projectors["finite_block_factorized_sector_maps_valid"] is True, "finite projectors invalid")
    require(projectors["finite_projector_architecture_retained"] is True, "finite projectors not retained")
    require(projectors["smooth_projector_retention_verified"] is False, "smooth projectors oververified")

    gates = sm["gate_results"]
    for key in [
        "smooth_s3_source_constructed",
        "smooth_Freed_Witten_closed",
        "smooth_projector_retention_closed",
        "selected_DE_dotD_Riesz_Green_constructed",
        "selected_Qa_SU3_packet_closed",
        "no_knob_closure_claimed",
        "sm_parity_closure_claimed",
    ]:
        require(gates[key] is False, f"S3 gate overclaimed: {key}")

    qa = data["qa_projective_response_hunt"]
    hunt = qa["hunt_result"]
    require(hunt["projective_rhoe_validator_available"] is True, "projective validator missing")
    require(hunt["twisted_promotion_contract_available"] is True, "promotion contract missing")
    require(hunt["validator_patterns_found"] is True, "validator patterns missing")
    for key in [
        "selected_qa_su3_projective_rhoE_found",
        "selected_qa_su3_D_E_or_dotD_found",
        "selected_qa_su3_finite_response_found",
        "qa_su3_packet_closed",
    ]:
        require(hunt[key] is False, f"QA hunt overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "finite_visible_S3_restriction_packet_coherent",
        "ordinary_S1_S2_Cij_DD_zero_retained",
        "S3_rank_two_requires_twisted_CP",
        "W3_spinC_visible_worldvolume_imported",
        "finite_block_projector_architecture_retained",
        "projective_rhoE_validator_pattern_found",
        "qa_su3_twisted_promotion_contract_found",
        "ordinary_rhoE_shortcuts_rejected_by_guardrail",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_smooth_S3_Deligne_Cech_or_flux_source",
        "smooth_Freed_Witten_and_projector_retention",
        "selected_D_E_dotD_Riesz_Green",
        "selected_gerbe_to_central_cocycle_map",
        "selected_qa_su3_projective_rhoE",
        "selected_qa_su3_D_E_or_dotD",
        "finite_response",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_smooth_S3_source",
        "claims_smooth_Freed_Witten_projector_retention",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_selected_qa_su3_projective_rhoE",
        "claims_selected_qa_su3_DE_or_dotD",
        "claims_finite_response",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("finite q79/F,m=1 S3 restriction layer" in note, "note missing S3 import")
    require("does not close the smooth source" in note, "note missing smooth guard")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
