"""Audit selected dynamic C1 transfer tensor / Galerkin C1 values manifest."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
STRICT = PACKET_DIR / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
DUAL = PACKET_DIR / "dual_path_value_fill_contract.packet.json"
CERT = ROOT / "certificates" / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_AcceptanceManifest_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.py"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_OR_GALERKINC1VALUES_ACCEPTANCE_MANIFEST_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT)
    dual = load(DUAL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    coord = strict["coordinate_system"]
    require(coord["sectors"] == ["u", "e", "d", "nuD"], "sector order mismatch")
    require(coord["total_real_coordinates"] == 72, "coordinate dimension mismatch")
    require(strict["static_source_prerequisites"]["static_enriched_weylpair_source_provenance_closed"] is True, "static prerequisite missing")
    require(strict["static_source_prerequisites"]["phase_route"] == ["u", "e"], "phase route mismatch")
    require(strict["static_source_prerequisites"]["shift_route"] == ["d", "nuD"], "shift route mismatch")
    acceptance = strict["dynamic_value_acceptance"]
    for key in [
        "A_selected_72_real_columns_required",
        "b_selected_72_real_source_vector_required",
        "deltaTheta_C1_must_be_solved_from_selected_values",
        "must_report_A_transpose_A",
        "must_report_A_transpose_b",
        "must_report_sector_response_matrices",
        "must_report_nonzero_family_rank_or_countertheorem",
        "must_not_use_observed_flavor_constants",
        "must_not_select_by_target_residual",
    ]:
        require(acceptance[key] is True, f"acceptance flag missing: {key}")
    require(acceptance["required_rank_or_replacement_theorem"] == 2, "rank requirement mismatch")
    reference = strict["conditional_reference_not_a_promotion"]
    require(reference["operator_is_A_selected"] is False, "conditional operator overpromoted")
    require(reference["source_vector_is_b_selected"] is False, "conditional b overpromoted")
    current = strict["current_value_status"]
    for key in [
        "dynamic_transfer_tensor_emitted",
        "A_selected_emitted",
        "b_selected_emitted",
        "deltaTheta_C1_promoted",
        "honest_Galerkin_values_emitted",
        "SM_parity_dynamic_packet_closed",
    ]:
        require(current[key] is False, f"value status overclaimed: {key}")

    require(dual["status"] == "DUAL_PATH_CONTRACT_READY_VALUES_OPEN", "dual status mismatch")
    require(dual["lane_A_same_source_dynamic_transfer"]["currently_closed"] is False, "lane A overclosed")
    require(dual["lane_B_honest_galerkin_c1_run"]["currently_closed"] is False, "lane B overclosed")
    require(dual["template_alignment"]["template_requires_A_columns"] is True, "template A alignment missing")
    require(dual["template_alignment"]["template_requires_b_vector"] is True, "template b alignment missing")
    require("same typed 72-real C1 objects" in dual["superset_strategy"]["locked_target"], "locked target missing")

    for key in [
        "dynamic_C1_acceptance_manifest",
        "lane_A_lane_B_target_equivalence",
        "72_real_coordinate_target_locked",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_dynamic_source_to_C1_transfer_tensor",
        "selected_primitive_C1_overlap_contractions",
        "theorem_derived_A_selected",
        "theorem_derived_b_selected",
        "selected_deltaTheta_C1",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "SM_parity_dynamic_packet_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")
    for key in ["observed_data_used", "target_fitting_used", "closure_claimed"]:
        require(data[key] is False, f"candidate overclaimed: {key}")
    require("Lane A and Lane B are different routes" in note, "note missing superset explanation")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
