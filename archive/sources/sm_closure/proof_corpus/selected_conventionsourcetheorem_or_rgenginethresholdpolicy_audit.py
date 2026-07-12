"""Audit convention source theorem or RG engine threshold policy artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_ATTEMPT = PACKET_DIR / "same_branch_convention_source_theorem_attempt.packet.json"
POLICY_RECONCILIATION = PACKET_DIR / "rg_benchmark_policy_reconciliation.packet.json"
THRESHOLD_POLICY = PACKET_DIR / "threshold_pole_running_policy_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_convention_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CONVENTIONSOURCETHEOREM_OR_RGENGINETHRESHOLDPOLICY_"
    "BUILT_BENCHMARK_POLICY_CLOSED_SOURCE_MAPS_OPEN"
)
NEXT = "MTT_Selected_ThresholdPoleRunningMaps_or_RThetaConventionSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source = load(SOURCE_ATTEMPT)
    policy = load(POLICY_RECONCILIATION)
    threshold = load(THRESHOLD_POLICY)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(
        source["status"] == "SAME_BRANCH_CONVENTION_SOURCE_THEOREM_ATTEMPTED_STILL_OPEN",
        "source attempt status mismatch",
    )
    require(source["target_scale"] == "M_Z", "source target scale mismatch")
    require(source["target_scheme"] == "MSbar", "source target scheme mismatch")
    require(source["target_identified"] is True, "source target not identified")
    for key in [
        "firstpass_profile_layer",
        "diagnostic_internal_rg_convergence",
        "finite_residual_table",
        "external_literature_benchmark",
    ]:
        require(source["source_evidence_present"][key] is True, f"source evidence missing: {key}")
    require(
        "external literature benchmark rows are downstream validation references, not MTT source selectors"
        in source["why_not_same_branch_source"],
        "external benchmark nonselector reason missing",
    )
    require(source["same_branch_convention_source_theorem_closed"] is False, "source theorem overclosed")
    require(source["closure_claimed"] is False, "source attempt overclosed")

    require(
        policy["status"] == "RG_BENCHMARK_POLICY_RECONCILED_FOR_VALIDATION_NOT_SOURCE_SELECTION",
        "policy status mismatch",
    )
    require(policy["reference_scale"] == "M_Z", "policy reference scale mismatch")
    require(policy["scheme"] == "MSbar", "policy scheme mismatch")
    require(policy["external_benchmark_values_filled"] is True, "external benchmark values missing")
    require(
        policy["external_benchmark_accepted_as_reference"] is True,
        "external benchmark not accepted as reference",
    )
    require(
        policy["external_benchmark_accepted_as_full_precision_match"] is False,
        "external benchmark overaccepted as precision match",
    )
    require(
        policy["internal_rg_convergence_closed_for_diagnostic_engine"] is True,
        "internal RG convergence missing",
    )
    require(
        policy["internal_rg_accepted_for_SM_parity_values"] is False,
        "internal RG overaccepted",
    )
    require(policy["all_literature_local_deltas_finite"] is True, "finite deltas missing")
    require(policy["benchmark_policy_closed_for_validation"] is True, "benchmark policy not closed")
    require(policy["benchmark_policy_closes_source_selection"] is False, "benchmark selected source")
    require(policy["closure_claimed"] is True, "policy should close locally")

    require(
        threshold["status"] == "THRESHOLD_POLE_RUNNING_POLICY_CONTRACT_BUILT_MAP_VALUES_OPEN",
        "threshold policy status mismatch",
    )
    require(threshold["threshold_matching_required"]["top"], "top threshold policy missing")
    require(
        threshold["mass_scheme_conversion_required"]["direct_top_mass"] is True,
        "direct top conversion missing",
    )
    require(threshold["finite_residual_rows_present"] is True, "finite residual rows missing")
    require(threshold["residual_row_count"] >= 10, "too few residual rows")
    require(
        threshold["accepted_as_threshold_matching_values"] is False,
        "threshold residuals overaccepted",
    )
    require(
        threshold["accepted_as_mass_scheme_conversion_values"] is False,
        "mass-scheme residuals overaccepted",
    )
    require(len(threshold["map_outputs_required_next"]) == 6, "map output contract changed")
    require(threshold["can_emit_values_now"] is False, "threshold map values overemitted")
    require(threshold["closure_claimed"] is True, "threshold policy should close locally")

    require(
        cutset["status"] == "NEXT_ATTACK_THRESHOLD_POLE_RUNNING_MAPS_OR_SELECTED_CONVENTION_SOURCE",
        "cutset status mismatch",
    )
    for key in [
        "same_branch_convention_source_attempt",
        "rg_benchmark_policy_reconciled_for_validation",
        "threshold_pole_running_policy_contract",
        "external_benchmark_rows_confirmed_downstream_only",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "same_branch_convention_source_theorem",
        "versioned_threshold_pole_running_map_values",
        "accepted_threshold_matching_source_rows",
        "accepted_mass_scheme_conversion_source_rows",
        "profile_covariance_or_diagonal_limitation",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["rg_benchmark_policy_closed_for_validation"] is True, "candidate policy not closed")
    require(closure["threshold_pole_running_policy_contract_closed"] is True, "candidate threshold contract not closed")
    for key in [
        "same_branch_convention_source_theorem_closed",
        "versioned_threshold_pole_running_map_values_closed",
        "accepted_threshold_matching_source_rows_closed",
        "accepted_mass_scheme_conversion_source_rows_closed",
        "profile_covariance_or_diagonal_limitation_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require("RG benchmark policy closed for validation    : true" in note, "note missing policy line")
    require("external benchmark accepted as source selector: false" in note, "note missing nonselector line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
