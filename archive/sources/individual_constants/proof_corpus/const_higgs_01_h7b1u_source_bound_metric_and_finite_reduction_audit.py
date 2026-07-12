"""Audit CONST-HIGGS-01 H7B1U source-bound metric and finite-reduction gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SOURCE_BINDING = BASE / "source_bound_metric_attempt.packet.json"
FINITE_REDUCTION = BASE / "conditional_finite_reduction_execution.packet.json"
DIRECT_HERM2 = BASE / "direct_herm2_payload_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1U_CONDITIONAL_REDUCTION_EXECUTED_SOURCE_REDUCTION_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(a: float, b: float, tol: float = 1e-15) -> bool:
    return abs(a - b) <= tol


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} expected true: {key}")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    source = load(SOURCE_BINDING)
    reduction = load(FINITE_REDUCTION)
    direct = load(DIRECT_HERM2)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("source", source),
        ("reduction", reduction),
        ("direct", direct),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1T_imported"] is True, "H7B1T import")
    require(candidate["formal_UV_exact_sequence_scaffold_closed"] is True, "formal scaffold")
    require(candidate["conditional_G_minimal_lift_formula_proved"] is True, "lift formula")
    require(candidate["diagonal_HYM_grid_replayed"] is True, "grid replay")
    require(candidate["grid_replay_matches_stored_certificate"] is True, "stored replay")
    require(candidate["conditional_finite_reduction_executable"] is True, "finite reduction executable")
    for key in [
        "source_metric_bound_to_E_H_UV",
        "selected_minimal_lift_policy_emitted",
        "selected_finite_reduction_policy_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1V_ReductionSelectorOrDirectHerm2HuvSource_v1",
        "candidate next",
    )

    require(source["status"] == "SOURCE_BOUND_METRIC_ATTEMPT_FAILS_UV_HIGGS_BINDING", "source status")
    require_all_true(source["closed_support"], "source support")
    blocked = source["blocked_binding"]
    require(blocked["H_sector_currently_rank_one_not_UV_twoHiggs"] is True, "rank-one H support")
    require(blocked["H_rho_is_trivial_singlet_not_twoHiggs_action"] is True, "H trivial")
    require(blocked["same_source_identifies_two_diagonal_HYM_lines_with_Hu_Hddagger"] is False, "basis binding")
    require(blocked["selected_minimal_lift_policy_emitted"] is False, "lift policy")
    require(blocked["selected_projector_phase_covariance_emitted"] is False, "phase covariance")
    require(blocked["selected_zero_mode_H_values_emitted"] is False, "zero-mode values")
    require(source["decision"]["source_metric_bound_to_E_H_UV"] is False, "source binding decision")
    require(source["decision"]["selected_G_minimal_lift_policy_promoted"] is False, "source lift decision")

    require(reduction["status"] == "CONDITIONAL_FINITE_REDUCTION_EXECUTED_SELECTION_POLICY_OPEN", "reduction status")
    cert_replay = reduction["replay_certificate"]
    require(cert_replay["mesh"] == 24, "mesh")
    require(cert_replay["iterations_run"] == 40, "iterations")
    require(cert_replay["matches_stored_replay"] is True, "replay match")
    require(cert_replay["residual_l2"] < 1e-12, "residual")
    require(close(cert_replay["u_min"], -0.09129255457956154), "u min")
    require(close(cert_replay["u_max"], 0.04562175016803212), "u max")
    values = reduction["conditional_reduction_candidates_not_selected"]
    require(close(values["uniform_mean"], 0.004701083905943647), "uniform mean")
    require(close(values["rho_weighted_mean"], 0.01175427147946371), "rho mean")
    require(close(values["exp_density_weighted_mean"], 0.012349317823559027), "exp mean")
    require(close(values["uniform_max"], 0.032610161691198375), "uniform max")
    require(values["uniform_min"] > 0.0, "uniform min")
    promotion = reduction["promotion_requirements"]
    require(promotion["finite_reduction_exactness_certificate_emitted"] is True, "exactness")
    require(promotion["observed_Higgs_or_beta_selector_forbidden"] is True, "selector forbidden")
    require(promotion["source_metric_bound_to_E_H_UV"] is False, "promotion binding")
    require(promotion["selected_minimal_lift_policy_emitted"] is False, "promotion lift")
    require(promotion["selected_finite_reduction_policy_emitted"] is False, "promotion policy")
    decision = reduction["decision"]
    require(decision["conditional_finite_reduction_executable"] is True, "decision executable")
    require(decision["selected_finite_reduction_policy_promoted"] is False, "decision policy")
    require(decision["selected_s_beta_promoted"] is False, "decision s_beta")

    require(direct["status"] == "DIRECT_HERM2_HUV_PAYLOAD_ATTEMPT_STILL_OPEN", "direct status")
    require(direct["conditional_functor_ready"] is True, "direct functor")
    require_all_true(direct["payload_requests_ready"], "payload requests")
    for key, value in direct["actual_outputs"].items():
        require(value is None, f"direct output emitted {key}")
    direct_decision = direct["decision"]
    for key in [
        "direct_Herm2_Huv_payload_emitted",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
    ]:
        require(direct_decision[key] is False, f"direct overclosed {key}")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1U", "no cycle")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1T_formula"] is False, "reopen formula")
    require(circ["is_promoting_conditional_number_as_Higgs_value"] is False, "promote number")
    require(circ["is_using_measured_Higgs_mass_or_tan_beta"] is False, "observed selector")
    require(circ["is_reusing_rank_one_H_as_B_Huv"] is False, "reuse H")
    require(len(no_cycle["new_information_added"]) == 4, "new info count")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1V_REDUCTION_SELECTOR_OR_DIRECT_HERM2_HUV_SOURCE", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multi")
    require("not a chosen-to-match Higgs quartic" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["diagonal_HYM_grid_replayed"] is True, "cert grid")
    require(cert["grid_replay_matches_stored_certificate"] is True, "cert match")
    require(cert["conditional_finite_reduction_executable"] is True, "cert reduction")
    require(close(cert["uniform_mean_conditional_s_beta"], 0.004701083905943647), "cert uniform")
    require(close(cert["rho_weighted_mean_conditional_s_beta"], 0.01175427147946371), "cert rho")
    require(close(cert["exp_density_weighted_mean_conditional_s_beta"], 0.012349317823559027), "cert exp")
    require(cert["source_metric_bound_to_E_H_UV"] is False, "cert binding")
    require(cert["selected_finite_reduction_policy_emitted"] is False, "cert policy")
    require(cert["selected_s_beta_value_found"] is False, "cert s_beta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("conditional finite reduction executable         True" in note, "note executable")
    require("uniform mean                       0.00470108390594364735" in note, "note uniform")
    require("rho-weighted mean                  0.0117542714794637102" in note, "note rho")
    require("exp-density-weighted mean          0.0123493178235590268" in note, "note exp")
    require("H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE" in note, "note next")

    print("CONST-HIGGS-01 H7B1U source-bound metric/reduction audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
