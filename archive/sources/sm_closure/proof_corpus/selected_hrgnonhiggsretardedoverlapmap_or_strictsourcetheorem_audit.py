"""Audit HRG non-Higgs retarded-overlap map/strict-source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRGNonHiggsRetardedOverlapMap_or_StrictSourceTheorem_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

CONTRACT = BASE / "retarded_overlap_family_source_map_contract.packet.json"
MAP_EXECUTION = BASE / "nonhiggs_hrg_source_map_execution.packet.json"
STRICT_EXECUTION = BASE / "strict_hrg_source_theorem_execution.packet.json"
PAYLOAD_MANIFEST = BASE / "retarded_overlap_family_payload_manifest.packet.json"
HK_GATE = BASE / "hk_threshold_gate_after_nonhiggs_hrg_map_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_nonhiggs_hrg_map_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HRGNONHIGGSRETARDEDOVERLAPMAP_OR_STRICTSOURCETHEOREM_"
    "CONTRACT_BUILT_NO_MAP_EMITTED"
)
NEXT = "MTT_Selected_RetardedOverlapFamilySelector_or_HRGSourcePayloadFill_v1"
HRG = 391.39140285811936


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    contract = load(CONTRACT)
    map_execution = load(MAP_EXECUTION)
    strict_execution = load(STRICT_EXECUTION)
    manifest = load(PAYLOAD_MANIFEST)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")

    decision = candidate["closure_decision"]
    for key in [
        "family_source_map_contract_built",
        "nonHiggs_HRG_source_map_attempted",
        "strict_HRG_source_theorem_executed",
        "UP_RET_OVERLAP_HRG_H_only_empirical",
        "conditional_empirical_H_K_layer_10_of_10",
        "strict_source_tier_9_of_10",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "nonHiggs_HRG_source_map_emitted",
        "strict_HRG_source_theorem_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_nonHiggs_HRG_source_map_count"] == 0, "accepted map count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(nums["tested_nonHiggs_map_count"] == 4, "tested map count")
    require(nums["accepted_nonHiggs_HRG_source_map_count"] == 0, "accepted map count nums")
    require(nums["controlled_empirical_conditional_K_row_count"] == 10, "empirical K count")
    require(nums["strict_accepted_selected_K_source_row_count"] == 9, "strict K count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["family_source_map_contract_built"] is True, "cert contract")
    require(cert["nonHiggs_HRG_source_map_emitted"] is False, "cert map")
    require(cert["accepted_nonHiggs_HRG_source_map_count"] == 0, "cert accepted")
    require(cert["strict_HRG_source_emitted"] is False, "cert strict")
    require(cert["H_only_empirical_layer_retained"] is True, "cert H-only")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(contract["status"] == "RETARDED_OVERLAP_FAMILY_SOURCE_MAP_CONTRACT_BUILT", "contract status")
    cresult = contract["contract_result"]
    require(cresult["contract_built"] is True, "contract built")
    for key in [
        "selected_family_selector_emitted",
        "selected_HRG_value_source_emitted",
        "selected_nonHiggs_HRG_map_emitted",
        "crossuse_prediction_passed",
    ]:
        require(cresult[key] is False, f"contract overclosed {key}")
    accept = contract["source_map_acceptance_contract"]
    for key in [
        "family_selector_source_id_emitted_before_empirical_replay",
        "same_value_used_for_H_and_at_least_one_nonHiggs_domain",
        "sector_insertion_maps_typed",
        "nonHiggs_evaluator_emits_prediction_without_retuning",
        "H_calibration_not_counted_as_prediction",
        "observed_values_forbidden_as_selector",
        "posthoc_common_multiplier_forbidden",
    ]:
        require(accept[key] is True, f"contract clause {key}")

    require(
        map_execution["status"] == "NONHIGGS_HRG_SOURCE_MAP_EXECUTED_ZERO_ACCEPTED_MAPS",
        "map status",
    )
    require(map_execution["tested_map_count"] == 4, "map tested")
    require(map_execution["accepted_crossuse_map_count"] == 0, "map accepted")
    require(map_execution["minimum_required_accepted_map_count"] == 1, "map minimum")
    map_decision = map_execution["decision"]
    require(map_decision["nonHiggs_HRG_source_map_emitted"] is False, "map emitted")
    require(map_decision["crossuse_prediction_audit_upgraded"] is False, "crossuse upgraded")
    require(map_decision["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "universal admitted")
    require(map_decision["H_only_empirical_status_retained"] is True, "H-only retained")
    domains = {row["domain"]: row for row in map_execution["map_rows"]}
    for domain in [
        "alpha/source-strength",
        "dynamic C1 overlap/value tensor",
        "charged scalar threshold/prefactor rows",
        "generic non-Higgs threshold/RG observable",
    ]:
        require(domain in domains, f"domain missing {domain}")
        require(domains[domain]["same_HRG_primitive_map_available"] is False, f"map available {domain}")
        require(domains[domain]["prediction_emitted_without_retuning"] is False, f"prediction emitted {domain}")
        require(domains[domain]["accepted_as_crossuse_map"] is False, f"accepted {domain}")
    require(domains["charged scalar threshold/prefactor rows"]["would_count_as_nonHiggs_prediction"] is False, "charged counted")
    require(
        "T_scheme=1" in domains["charged scalar threshold/prefactor rows"]["blocking_reason"],
        "charged T_scheme guard missing",
    )

    require(strict_execution["status"] == "STRICT_HRG_SOURCE_THEOREM_EXECUTED_NOT_EMITTED", "strict status")
    sresult = strict_execution["result"]
    for key in [
        "selected_R_H_RG",
        "selected_A_EW",
        "selected_mu_match",
        "selected_K_threshold_Omega_H_lambda",
        "same_branch_determinant_index_or_RG_operator",
        "mathematical_impossibility_claimed",
    ]:
        require(sresult[key] is False, f"strict result {key}")

    require(manifest["status"] == "RETARDED_OVERLAP_FAMILY_PAYLOAD_MANIFEST_BUILT", "manifest status")
    required_ids = {row["id"] for row in manifest["payloads_required_for_next_closure"]}
    for pid in [
        "RO.family_selector",
        "RO.value_source",
        "RO.H_sector_map",
        "RO.nonHiggs_sector_map",
        "RO.nonHiggs_prediction_evaluator",
        "RO.provenance_certificate",
    ]:
        require(pid in required_ids, f"payload missing {pid}")
    for row in manifest["payloads_required_for_next_closure"]:
        require(row["current_status"] == "missing", f"payload overfilled {row['id']}")
    require(manifest["two_viable_routes"]["strict_no_knob_route"]["requires_universal_parameter"] is False, "strict route param")
    require(manifest["two_viable_routes"]["provisional_universal_route"]["requires_universal_parameter"] is True, "universal route")
    require(
        "multiply charged rows by HRG after NullThresholdDeltaTheorem selected T_scheme=1"
        in manifest["forbidden_payloads"],
        "forbidden charged multiplier",
    )

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_STRICT_9_OF_10_EMPIRICAL_10_OF_10_NO_CROSSUSE_MAP",
        "H K status",
    )
    require(hk_gate["strict_source_tier"]["accepted_selected_K_source_row_count"] == 9, "H K strict")
    empirical = hk_gate["controlled_empirical_tier"]
    require(empirical["conditional_parameterized_K_row_count"] == 10, "H K empirical")
    require(empirical["nonHiggs_HRG_source_map_attempted"] is True, "H K map attempt")
    require(empirical["nonHiggs_HRG_source_map_emitted"] is False, "H K map emitted")
    require(empirical["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "H K universal")
    require(empirical["UP_RET_OVERLAP_HRG_H_only_empirical"] is True, "H K H-only")

    require(
        cutset["status"] == "NEXT_FRONTIER_RETARDED_OVERLAP_FAMILY_SELECTOR_OR_HRG_SOURCE_PAYLOAD",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "finite UP-RET-OVERLAP family source-map contract built",
        "non-Higgs HRG map execution tested four domains",
        "zero accepted non-Higgs HRG source maps",
        "strict HRG source theorem executed and still not emitted",
        "exact retarded-overlap family payload manifest built",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "RO.family_selector",
        "RO.value_source",
        "RO.H_sector_map",
        "RO.nonHiggs_sector_map",
        "RO.nonHiggs_prediction_evaluator",
        "strict selected R_H^RG source theorem",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "non-Higgs HRG map execution: `0 / 4` accepted maps",
        "strict selected `R_H^RG` source theorem: executed, still not emitted",
        "The charged scalar rows cannot be used as the HRG cross-use target.",
        "RO.family_selector",
        "`lambda_H` remains calibration, not prediction.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: HRG non-Higgs source-map contract built; zero maps emitted; "
        "payload manifest is the next construction target."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
