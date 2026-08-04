"""Audit unpatched Phi_fin C1 source-rule / HRG consumer-map reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTables_to_HRGConsumerMap_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

SOURCE_RECONCILIATION = BASE / "source_rule_backimport_reconciliation.packet.json"
PAYLOAD_PROMOTION = BASE / "selected_dynamic_phifinc1_payload_promotion.packet.json"
HRG_HANDOFF = BASE / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
CUTSET = BASE / "next_cutset_after_unpatched_phifinc1_to_hrg.packet.json"

STATUS = (
    "MTT_SELECTED_UNPATCHEDPHIFINC1SOURCERULE_OR_HONESTGALERKINTABLES_TO_"
    "HRGCONSUMERMAP_CLOSED_DYNAMIC_PAYLOAD_PROMOTED_HRG_VALUE_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGConsumerValueSource_or_LargeThresholdTransportMap_v1"
HRG = 391.39140285811936


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    source = load(SOURCE_RECONCILIATION)
    payload = load(PAYLOAD_PROMOTION)
    hrg = load(HRG_HANDOFF)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "previous_source_rule_open_frontier_superseded",
        "unpatched_source_rule_proved_by_backimport",
        "route_A_physical_source_certificate_used",
        "formal_110_row_assembly_selected",
        "strict_unpatched_dynamic_C1_closed",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
        "dynamic_payload_available_for_HRG_consumer",
        "HRG_consumer_map_gate_built",
        "RO_family_selector_source_selected",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "route_B_honest_galerkin_needed_for_dynamic_payload",
        "typed_HRG_consumer_map_emitted",
        "RO_value_source_derived",
        "same_HRG_nonHiggs_prediction_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_RO_value_source_count"] == 0, "accepted RO source count")
    require(decision["accepted_same_HRG_nonHiggs_map_count"] == 0, "accepted same-HRG maps")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["required_A_EW_over_external_A_EW"] - HRG) < 1e-12, "A_EW ratio")
    require(nums["required_A_EW_over_external_A_EW_minus_HRG_abs"] == 0.0, "HRG residual")
    require(nums["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A")
    require(nums["A_transpose_b"] == [12.0, 12.0], "A^T b")
    require(nums["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta")
    require(nums["rank"] == 2, "rank")
    require(nums["primitive_kernel_rows"] == 72, "primitive rows")
    require(nums["sector_assembly_rows"] == 36, "sector rows")
    require(nums["hessian_b_source_rows"] == 2, "hessian rows")
    require(nums["formal_110_total_rows"] == 110, "formal total rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "theorem_proved",
        "unpatched_source_rule_proved_by_backimport",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "typed_HRG_consumer_map_emitted",
        "RO_value_source_derived",
        "same_HRG_nonHiggs_prediction_emitted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(
        source["status"] == "PREVIOUS_SOURCE_RULE_OPEN_GATE_SUPERSEDED_BY_ACTIVE_UNPATCHED_SOURCE_STACK",
        "source status",
    )
    require(source["theorem"]["proved"] is True, "source theorem")
    require(source["previous_open_flags"]["strict_unpatched_dynamic_C1_closed"] is False, "previous flag")
    require(source["previous_open_flags"]["source_rule_proved_unpatched"] is False, "previous source flag")
    require(source["active_ledger_closure_sources"]["unpatched_source_promotion_stack_closed"] is True, "stack")
    require(
        source["active_ledger_closure_sources"]["SelectedFiniteC1SourceIdentityTheorem_promoted"]
        is True,
        "identity theorem",
    )
    require(source["active_ledger_closure_sources"]["physical_PhiFinC1_action_source"] is True, "physical source")
    require(
        source["active_ledger_closure_sources"]["cross_repo_guard_stale_open_packets_disallowed"]
        is True,
        "stale-open guard",
    )
    require(source["decision"]["source_rule_or_galerkin_wall_closed_for_dynamic_payload"] is True, "wall")
    require(source["decision"]["honest_galerkin_tables_required_for_this_promotion"] is False, "route B need")
    require_no_selector(source, "source")

    require(payload["status"] == "SELECTED_DYNAMIC_PHIFINC1_PAYLOAD_PROMOTED_IN_ACTIVE_LEDGER", "payload status")
    require(payload["source_owner"] == "PhysicalPhiFinC1ActionSource", "payload owner")
    require(payload["source_rule_premise_free"] is True, "premise free")
    require(payload["source_row_premise_used"] is False, "source row premise")
    require(payload["emitted_before_residual_replay"] is True, "emitted before replay")
    promoted = payload["promoted_objects"]
    for key in [
        "PhysicalPhiFinC1ActionSource",
        "SelectedFiniteC1SourceIdentityTheorem",
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "selected_dynamic_phi_fin_c1_payload",
    ]:
        require(promoted[key] is True, f"payload promoted {key}")
    require(payload["exact_values"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "payload A")
    require(payload["exact_values"]["A_transpose_b"] == [12.0, 12.0], "payload b")
    require(payload["exact_values"]["deltaTheta_C1"] == [1.0, 1.0], "payload delta")
    require(payload["row_counts"]["formal_110_total_rows"] == 110, "payload 110")
    require(payload["assembly_evidence"]["all_72_primitive_rows_exact"] is True, "payload 72")
    require(payload["assembly_evidence"]["formal_110_rows_executed"] is True, "payload formal")
    require(payload["assembly_evidence"]["formal_110_matches_prior_replay"] is True, "payload match")
    for key in [
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
        "strict_unpatched_dynamic_C1_closed",
    ]:
        require(payload["decision"][key] is True, f"payload decision {key}")
    require(payload["decision"]["honest_selected_galerkin_export_needed_now"] is False, "payload route B")
    require_no_selector(payload, "payload")

    require(hrg["status"] == "DYNAMIC_PAYLOAD_AVAILABLE_HRG_CONSUMER_VALUE_SOURCE_OPEN", "HRG status")
    require(hrg["theorem"]["proved"] is True, "HRG theorem")
    require(hrg["consumer_acceptance_conditions"]["selected_dynamic_payload_available"] is True, "HRG payload")
    require(hrg["consumer_acceptance_conditions"]["RO_family_selector_source_selected"] is True, "RO family")
    for key in [
        "RO_value_source_derived",
        "typed_HRG_consumer_map_emitted",
        "same_HRG_nonHiggs_map_accepted",
        "UP_RET_OVERLAP_HRG_admitted_as_universal",
        "selected_AEW_large_threshold_transport_available",
        "external_lambda_Mt_used_as_selector",
    ]:
        require(hrg["consumer_acceptance_conditions"][key] is False, f"HRG condition false {key}")
    require(hrg["decision"]["dynamic_payload_blocker_retired"] is True, "HRG dynamic retired")
    require(hrg["decision"]["accepted_RO_value_source_count"] == 0, "HRG RO count")
    require(hrg["decision"]["accepted_same_HRG_nonHiggs_map_count"] == 0, "HRG same count")
    for key in [
        "typed_HRG_consumer_map_emitted",
        "RO_value_source_derived",
        "same_HRG_nonHiggs_prediction_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(hrg["decision"][key] is False, f"HRG decision false {key}")
    require_no_selector(hrg, "HRG")

    require(
        cutset["status"] == "NEXT_FRONTIER_HRG_CONSUMER_VALUE_SOURCE_OR_LARGE_THRESHOLD_TRANSPORT",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "unpatched Phi_fin^C1 source rule promoted by premise-free Route A backimport",
        "selected dynamic Phi_fin/C1 payload is available to the HRG route",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "typed HRG consumer/value-source map from selected dynamic payload to UP_RET_OVERLAP.HRG",
        "same-HRG non-Higgs prediction without retuning",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "Correction",
        "A_selected promoted                     True",
        "formal total rows    110",
        "RO.value_source derived            False",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: unpatched Phi_fin/C1 source promotion is backimported and "
        "dynamic payload is selected; HRG consumer/value-source map remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
