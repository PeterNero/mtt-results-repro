"""Audit selected S3 source certificate and Qa/SU3 alignment import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "s3_source_certificate_and_qa_alignment_import.candidate.json"
CERT = ROOT / "certificates" / "s3_source_certificate_and_qa_alignment_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "S3_SourceCertificate_and_QaAlignment_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_s3_source_certificate_and_qa_alignment.py"

STATUS = "S3_SOURCE_CERTIFICATE_QA_ALIGNMENT_IMPORTED_OPERATOR_RESPONSE_OPEN"
NEXT = "MTT_Selected_Visible_Green_Schwarz_Operator_Source_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Central_Cocycle_Map_Source_Augmentation_Request_v1"


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

    source = data["sm_selected_s3_source_certificate"]
    selected = source["selected_source_packet"]
    for key in [
        "source_selected_by_mtt",
        "fixed_differential_cohomology_class",
        "same_class_as_finite_m1_deck_cocycle",
        "S3_pullback_table_supplied",
        "map_to_qutrit_central_cocycle_verified",
        "smooth_Freed_Witten_cancellation_verified",
        "block_sector_projector_retention_closed",
    ]:
        require(selected[key] is True, f"S3 source field not closed: {key}")

    guard_source = source["guardrail_transfer"]
    for key in [
        "claims_selected_D_E_dotD_constructed",
        "claims_visible_operator_source_constructed",
        "claims_coherent_spectral_zero_mode_projectors",
        "claims_full_SM_closure",
        "uses_observed_flavor_data",
        "uses_benchmark_flavor_entries",
    ]:
        require(guard_source[key] is False, f"S3 source overclaimed: {key}")

    qa = data["qa_twisted_promotion_fill_attempt"]
    fill = qa["fill_result"]
    require(fill["source_family_selected"] is True, "QA source family not selected")
    require(fill["fixed_differential_class_context_found"] is True, "QA fixed class context missing")
    for key in [
        "central_cocycle_map_verified",
        "selected_Qa_SU3_representative_found",
        "mapped_Freed_Witten_verified",
        "twisted_projector_retention_verified",
        "projective_rhoE_tables_supplied",
        "selected_D_E_dotD_response_supplied",
        "monad_bridge_numeric_gf_zero_checked",
        "qa_su3_packet_closed",
    ]:
        require(fill[key] is False, f"QA fill overclaimed: {key}")
    require(qa["partial_packet"]["guardrails"]["no_q79_value_import"] is True, "q79 import guard missing")
    require(
        qa["partial_packet"]["guardrails"]["validator_pass_not_source_selection"] is True,
        "validator/source guard missing",
    )

    terms = data["corpus_alignment_terms"]
    require(all(terms["strominger"].values()), "Strominger terms missing")
    require(all(terms["flux"].values()), "flux terms missing")
    require(data["alignment_verdict"]["are_we_onto_something"] is True, "alignment verdict not positive")

    closes = data["what_closes_now"]
    for key in [
        "selected_S3_flat_Deligne_class",
        "selected_S3_pullback_restriction_table",
        "map_to_qutrit_central_cocycle",
        "smooth_S3_twisted_Freed_Witten_cancellation",
        "block_factorized_family_Higgs_projector_retention",
        "strings_flux_corpus_alignment_confirmed",
        "qa_su3_structural_alignment_confirmed",
        "bad_q79_to_qa_value_transfer_rejected",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_visible_operator_source_constructed",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_Qa_SU3_packet_closed",
        "claims_A_selected_or_b_selected",
        "uses_q79_values_as_qa_su3_values",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("real aligned branch" in note, "note missing alignment verdict")
    require("does not yet" in note and "promote" in note, "note missing QA guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
