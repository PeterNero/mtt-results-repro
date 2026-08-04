"""Audit gerbe-twisted source-class and response-gate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "gerbe_twisted_source_class_response_gate_import.candidate.json"
CERT = ROOT / "certificates" / "gerbe_twisted_source_class_response_gate_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "GerbeTwisted_SourceClass_ResponseGate_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_gerbe_twisted_source_class_response_gate.py"

STATUS = "GERBE_TWISTED_SOURCE_CLASS_RESPONSE_GATE_IMPORTED_VALUES_OPEN"
NEXT = "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Projective_RhoE_or_DE_Response_Source_Hunt_v1"


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

    sm = data["sm_pic0_or_gerbe_source"]
    require(sm["route_decision"]["direct_pic0_invariance"]["status"] == "RETIRED_FOR_NOW", "Pic0 not retired")
    require(sm["route_decision"]["gerbe_twisted_de_source"]["status"] == "PRIMARY_EXECUTION_ROUTE", "gerbe route not primary")
    require(sm["gate_results"]["good_cover_knob_removed"] is True, "good-cover knob not removed")
    require(sm["gate_results"]["selected_smooth_s3_source_constructed"] is False, "smooth S3 overconstructed")
    require(
        sm["imported_results"]["deck_cech_lift"]["qutrit_projective_commutator_matched"] is True,
        "finite qutrit commutator support missing",
    )
    require(
        sm["imported_results"]["finite_s3_cp_cancellation"]["finite_S3_CP_cancellation_closed"] is True,
        "finite S3 CP cancellation missing",
    )
    require(
        sm["imported_results"]["visible_gs_curvature"]["visible_green_schwarz_curvature_verified"] is True,
        "visible GS curvature missing",
    )

    interface = data["qa_gerbe_response_interface"]
    require(interface["interface_checks"]["all_pair_twists_cancel"] is True, "QA pair twists do not cancel")
    require(interface["interface_checks"]["all_products_land_in_P"] is True, "QA products miss P")
    require(interface["interface_checks"]["template_requires_finite_response"] is True, "QA response not required")
    require(interface["closure_claimed"] is False, "QA interface overclosed")

    fill = data["qa_gerbe_response_fill_attempt"]
    require(fill["fill_result"]["source_family_filled"] is True, "QA source family not filled")
    require(fill["fill_result"]["twist_cancellation_table_filled"] is True, "QA twist table not filled")
    require(fill["fill_result"]["primitive_complex_central_support_filled"] is True, "QA primitive support missing")
    for key in [
        "finite_response_filled",
        "same_branch_representative_filled",
        "section_bases_and_constants_filled",
        "same_branch_rhoE_or_local_system_filled",
        "qa_su3_packet_closed",
    ]:
        require(fill["fill_result"][key] is False, f"QA fill overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "direct_Pic0_invariance_retired_for_now",
        "good_cover_knob_removed",
        "gerbe_twisted_route_selected_as_primary",
        "finite_q79_F_m1_gerbe_support_imported",
        "qa_su3_gerbe_twist_interface_built",
        "qa_su3_partial_source_support_filled",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_smooth_S3_class_restriction",
        "smooth_S3_Freed_Witten_cancellation",
        "twisted_projector_retention_for_block_factorized_sectors",
        "same_branch_DE_dotD_Riesz_Green_response",
        "qa_su3_same_branch_representative",
        "qa_su3_section_bases_and_twisted_constants",
        "qa_su3_projective_rhoE_or_DE_response",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_direct_Pic0_invariance",
        "claims_selected_smooth_S3_source",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_qa_su3_packet_closed",
        "claims_finite_response_filled",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Direct Pic0 invariance is retired" in note, "note missing Pic0 retirement")
    require("good-cover choice reduced" in note, "note missing good-cover reduction")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
