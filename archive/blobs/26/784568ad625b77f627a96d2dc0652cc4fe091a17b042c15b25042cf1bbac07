"""Audit Step10 physical Phi_fin^C1 source-rule import artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
ROUTE_A_IMPORT = BASE / "route_a_active_ledger_source_rule_import.packet.json"
DYNAMIC_PAYLOAD = BASE / "step10_dynamic_c1_payload_emission.packet.json"
VALUE_GAP = BASE / "fulls2_no_proxy_value_row_gap.packet.json"
NEXT_PACKET = BASE / "next_after_step10_source_rule.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STEP10_PHYSICALPHIFINC1SOURCERULE_OR_INDEPENDENTGALERKINROWS_"
    "ROUTE_A_SOURCE_RULE_CLOSED_FULLS2_VALUES_OPEN"
)
NEXT = "MTT_Selected_FullS2NoProxyValueRows_or_StrictPEWDirectKExit_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure guard")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    route_a = load(ROUTE_A_IMPORT)
    dynamic = load(DYNAMIC_PAYLOAD)
    value_gap = load(VALUE_GAP)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("route_a", route_a),
        ("dynamic", dynamic),
        ("value_gap", value_gap),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "Step10PhysicalPhiFinC1SourceRuleImportTheorem", "theorem name")

    decision = data["closure_decision"]
    for key in [
        "stale_step10_source_rule_open_line_superseded",
        "route_A_selected_physical_PhiFinC1_source_rule_closed",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
    ]:
        require(decision[key] is True, f"decision true {key}")

    for key in [
        "route_B_independent_selected_Galerkin_or_row_kernel_execution_needed",
        "full_S2_value_rows_closed",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed",
        "RO_value_source_derived",
        "strict_P_EW_source_theorem_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    require(decision["accepted_RO_value_source_count"] == 0, "RO count")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW rows")
    require(decision["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")

    nums = data["key_numbers"]
    require(nums["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A")
    require(nums["A_transpose_b"] == [12.0, 12.0], "A^T b")
    require(nums["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta")
    require(nums["rank"] == 2, "rank")
    require(nums["primitive_kernel_rows"] == 72, "primitive rows")
    require(nums["hessian_b_source_rows"] == 2, "hessian rows")
    require(nums["sector_assembly_rows"] == 36, "sector rows")
    require(nums["formal_110_total_rows"] == 110, "formal rows")

    require(route_a["status"] == "ROUTE_A_PHYSICAL_PHIFIN_C1_SOURCE_RULE_IMPORTED_CLOSED", "route A status")
    require(route_a["route_A_selected_physical_PhiFinC1_source_rule_closed"] is True, "route A closed")
    require(route_a["route_B_independent_selected_Galerkin_or_row_kernel_execution_needed"] is False, "route B need")
    require(route_a["source_owner"] == "PhysicalPhiFinC1ActionSource", "source owner")
    require(route_a["source_rule_premise_free"] is True, "premise free")
    require(route_a["same_branch"] is True, "same branch")
    require(route_a["source_row_premise_used"] is False, "source premise")
    require(
        route_a["stale_open_packets_allowed_to_override_later_closure"] is False,
        "stale override guard",
    )

    require(dynamic["status"] == "STEP10_DYNAMIC_C1_PAYLOAD_EMITTED_FROM_ROUTE_A", "dynamic status")
    for key in [
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "selected_dynamic_phi_fin_c1_payload",
    ]:
        require(dynamic["promoted_objects"][key] is True, f"promoted {key}")
    for key in [
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
    ]:
        require(dynamic["contract_outputs_closed_here"][key] is True, f"closed output {key}")
    for key in [
        "full_S2_value_rows",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting",
    ]:
        require(dynamic["contract_outputs_not_closed_here"][key] is True, f"open output {key}")
    require(dynamic["row_counts"]["formal_110_total_rows"] == 110, "dynamic 110")
    require(dynamic["assembly_evidence"]["all_72_primitive_rows_exact"] is True, "dynamic 72")
    require(dynamic["assembly_evidence"]["formal_110_rows_executed"] is True, "dynamic formal")

    require(value_gap["status"] == "FULL_S2_AND_NO_PROXY_VALUE_ROWS_REMAIN_OPEN", "gap status")
    require(value_gap["dynamic_payload_blocker_retired"] is True, "dynamic blocker")
    require(value_gap["RO_family_selector_source_selected"] is True, "RO family")
    for key in [
        "RO_value_source_derived",
        "full_S2_value_rows_closed",
        "accepted_Yukawa_magnitudes_closed",
        "CKM_PMNS_measured_value_closure_closed",
        "lambda_H_row_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(value_gap[key] is False, f"gap false {key}")
    require(value_gap["accepted_RO_value_source_count"] == 0, "gap RO")
    require(value_gap["accepted_same_HRG_nonHiggs_map_count"] == 0, "gap HRG")
    require(value_gap["strict_P_EW_source_rows"] == 0, "gap strict")
    require(value_gap["direct_K_threshold_Omega_H_lambda_rows"] == 0, "gap direct")

    for key in [
        "theorem_proved",
        "stale_step10_source_rule_open_line_superseded",
        "route_A_selected_physical_PhiFinC1_source_rule_closed",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "route_B_independent_selected_Galerkin_or_row_kernel_execution_needed",
        "full_S2_value_rows_closed",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed",
        "RO_value_source_derived",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
    ]:
        require(cert[key] is False, f"cert false {key}")

    for phrase in [
        "Step10PhysicalPhiFinC1SourceRuleImportTheorem",
        "route A physical Phi_fin^C1 source rule closed = true",
        "A_selected promoted strict                      = true",
        "full S2 value rows closed = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Step10 Route A source-rule subgate is closed from the "
        "active ledger; full S2/no-proxy value rows and strict P_EW/direct-K "
        "remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
