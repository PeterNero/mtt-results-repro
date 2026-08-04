"""Audit common-RG and empirical audit gate for SM equivalence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_common_rg_and_empirical_audit.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_common_rg_and_empirical_audit_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_common_rg_and_empirical_audit.py"

STATUS = "MTT_SM_EQUIVALENCE_COMMON_RG_AND_EMPIRICAL_AUDIT_BUILT_TRUE_EQUIVALENCE_OPEN"
NEXT = "MTT_SM_Equivalence_RGPolicy_Covariance_and_ObservableSuite_v1"


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
    require(NEXT in note, "note missing next artifact")

    superset = data["superset_strategy_use"]
    require(superset["mode"] == "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY", "superset mode mismatch")
    require(superset["measured_targets_used_to_lock_source"] is False, "measured targets used as selectors")

    native = data["native_published_parameter_replay"]
    require(native["status"] == "NATIVE_CONVENTION_REPLAY_EXECUTABLE", "native replay status mismatch")
    for key in [
        "charged_fermion_and_quark_mass_to_tree_yukawa_loop",
        "higgs_tree_lambda_seed",
        "electroweak_tree_seed",
        "CKM_complex_down_yukawa_replay",
        "PMNS_oscillation_mass_squared_replay",
        "MZ_gauge_alpha_triplet",
    ]:
        require(native["closed_rows"][key] is True, f"native replay row not closed: {key}")

    common = data["common_RG_true_equivalence_gate"]
    require(common["status"] == "TRUE_COMMON_SCALE_EQUIVALENCE_OPEN", "common RG status mismatch")
    require(common["selected_policy"]["preferred_reference_scale"] == "M_Z", "preferred reference scale mismatch")
    for key in [
        "typed_measured_slots_declared",
        "source_nonselection_guardrail",
        "native_replay_values_available",
    ]:
        require(common["closed_rows"][key] is True, f"common RG closed row missing: {key}")
    for key in [
        "single_common_scale_transport",
        "loop_order_beta_functions_and_thresholds",
        "mass_scheme_unification",
        "Yukawa_running_matrices_at_common_scale",
        "Higgs_lambda_running_at_common_scale",
        "full_CKM_PMNS_covariance_or_profile_likelihood",
        "absolute_neutrino_mass_or_declared_minimal_parity_policy",
        "observable_suite_with_tolerances",
    ]:
        require(common["open_rows"][key] is True, f"common RG open row missing: {key}")

    empirical = data["empirical_audit"]
    require(empirical["ledger_interfaces_ready"] is True, "empirical ledger interface not ready")
    require(empirical["can_claim_native_replay_closure"] is True, "native replay not claimable")
    require(empirical["can_claim_true_SM_equivalence"] is False, "true SM equivalence overclaimed")
    require(empirical["can_claim_no_knob_closure"] is False, "no-knob overclaimed")
    for key in [
        "SM_source_interface",
        "masses_and_tree_yukawas",
        "CKM_and_complex_quark_Yukawa",
        "PMNS_and_neutrino_splittings",
        "gauge_triplet",
        "QFT_observable_functor",
    ]:
        row = empirical["required_rows"][key]
        require(row["blocks_true_equivalence"] is True, f"empirical row should block true equivalence: {key}")
        require("status" in row and "reason" in row, f"empirical row incomplete: {key}")

    cutset = data["minimum_closure_cutset"]
    require([row["id"] for row in cutset] == [
        "C1_common_RG_policy",
        "C2_covariance_profile_policy",
        "C3_neutrino_absolute_policy",
        "C4_observable_suite",
        "C5_selected_SM_packet_certificate",
    ], "minimum cutset mismatch")

    level = data["closure_level"]
    require(level["native_replay_layer"] == "SUBSTANTIALLY_CLOSED", "native replay level mismatch")
    require(level["true_common_scale_SM_equivalence"] == "OPEN", "true equivalence level mismatch")
    require(level["no_knob_SM_derivation"] == "OPEN", "no-knob level mismatch")

    closes = data["what_closes_now"]
    for key in [
        "native_published_parameter_replay_audit",
        "true_SM_equivalence_standard_declared",
        "common_RG_cutset_identified",
        "empirical_audit_rows_identified",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "common_RG_transport_values",
        "loop_order_and_threshold_policy",
        "covariance_or_profile_policy",
        "absolute_neutrino_mass_or_minimal_policy",
        "observable_suite_with_tolerances",
        "selected_SM_packet_final_certificate",
        "true_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["native_replay_closure_claimed"] is True, "native replay closure should be claimed")
    require(data["closure_claimed"] is False, "generic closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("native published-parameter replay: substantially closed" in note, "note missing closure separation")
    require("C1 common RG policy" in note, "note missing cutset")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
