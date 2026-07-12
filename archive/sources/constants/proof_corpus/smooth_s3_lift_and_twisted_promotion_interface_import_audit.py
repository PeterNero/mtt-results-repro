"""Audit smooth S3 lift and Qa/SU3 twisted-promotion interface import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "smooth_s3_lift_and_twisted_promotion_interface_import.candidate.json"
CERT = ROOT / "certificates" / "smooth_s3_lift_and_twisted_promotion_interface_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SmoothS3Lift_and_TwistedPromotionInterface_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_smooth_s3_lift_and_twisted_promotion_interface.py"

STATUS = "SMOOTH_S3_LIFT_TWISTED_PROMOTION_INTERFACE_IMPORTED_SOURCE_CERTIFICATE_OPEN"
NEXT = "MTT_Selected_S3_Differential_Cohomology_Source_Certificate_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Fill_Attempt_v1"


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

    lift = data["sm_smooth_s3_lift"]
    gates = lift["gate_results"]
    for key in [
        "finite_prerequisites_assembled",
        "good_cover_not_physical_knob",
        "smooth_s3_lift_artifact_built",
        "template_validator_confirms_open",
    ]:
        require(gates[key] is True, f"smooth lift closed flag missing: {key}")
    for key in [
        "fixed_differential_cohomology_class_supplied",
        "smooth_source_selected",
        "smooth_S3_Freed_Witten_closed",
        "smooth_projector_retention_closed",
        "selected_DE_dotD_Riesz_Green_constructed",
        "selected_Qa_SU3_packet_closed",
        "sm_parity_closure_claimed",
        "no_knob_closure_claimed",
    ]:
        require(gates[key] is False, f"smooth lift overclaimed: {key}")

    contract = data["smooth_lift_packet_contract"]
    for field in [
        "source_selected_by_mtt",
        "fixed_differential_cohomology_class",
        "restricts_to_selected_S3_worldvolume",
        "map_to_qutrit_central_cocycle_verified",
        "smooth_twisted_CP_or_worldvolume_flux_constructed",
        "freed_witten_verified_for_smooth_S3_source",
        "twisted_projector_retention_verified",
    ]:
        require(field in contract["must_supply_now"], f"smooth contract missing {field}")

    qa = data["qa_twisted_promotion_interface"]
    require(qa["closure_claimed"] is False, "QA interface overclosed")
    require(qa["target_fitting_used"] is False, "QA target fitting")
    for key in [
        "source_family_available",
        "projective_validator_pattern_available",
        "twisted_promotion_contract_available",
        "strict_selected_fields_open",
    ]:
        require(qa["interface_checks"][key] is True, f"QA interface missing {key}")

    template = data["qa_template"]
    require(template["source_evidence"]["selected_by_mtt"] is None, "QA selected flag filled")
    require(
        template["source_evidence"]["map_to_central_cocycle_verified"] is None,
        "QA central map filled",
    )
    require(template["projective_rhoE"]["projective_mesh_tables"] is None, "QA rhoE filled")
    require(template["operator_response"]["D_E"] is None, "QA D_E filled")
    require(template["operator_response"]["dotD"] is None, "QA dotD filled")
    require(template["monad_bridge"]["same_source_bridge_to_operator"] is None, "QA bridge filled")

    closes = data["what_closes_now"]
    for key in [
        "finite_prerequisites_for_s3_lift_assembled",
        "good_cover_not_physical_knob_imported",
        "smooth_lift_template_validator_run",
        "smooth_s3_lift_gate_reduced_to_source_certificate",
        "downstream_de_operator_bridge_identified",
        "qa_su3_promotion_schema_built",
        "q79_contract_translated_without_value_import",
        "strict_selected_source_fields_named",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_smooth_S3_source",
        "claims_fixed_differential_cohomology_class",
        "claims_smooth_Freed_Witten_projector_retention",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_selected_qa_su3_source",
        "claims_selected_qa_su3_projective_rhoE_or_DE",
        "claims_A_selected_or_b_selected",
        "uses_q79_values_as_qa_su3_values",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("smooth lift" in note, "note missing smooth lift")
    require(
        "without importing q79" in note and "values as Qa/SU3 values" in note,
        "note missing q79 guard",
    )
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
