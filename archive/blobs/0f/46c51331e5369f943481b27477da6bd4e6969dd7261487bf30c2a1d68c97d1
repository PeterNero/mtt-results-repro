"""Audit CONST-HIGGS-01 H7B1T UV Higgs-plane binding/minimal-lift theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
FORMAL_SEQUENCE = BASE / "formal_uv_exact_sequence_scaffold.packet.json"
MINIMAL_LIFT = BASE / "conditional_metric_minimal_lift_formula.packet.json"
BINDING_ATTEMPT = BASE / "actual_source_binding_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1T_UVHiggsPlaneBindingOrMinimalLiftTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1T_FORMAL_SEQUENCE_AND_MINIMAL_LIFT_FORMULA_CLOSED_SOURCE_BINDING_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} expected true: {key}")


def require_all_false(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is False, f"{name} expected false: {key}")


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
    formal = load(FORMAL_SEQUENCE)
    lift = load(MINIMAL_LIFT)
    binding = load(BINDING_ATTEMPT)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("formal", formal),
        ("lift", lift),
        ("binding", binding),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1S_imported"] is True, "H7B1S import")
    require(candidate["formal_UV_exact_sequence_scaffold_closed"] is True, "formal scaffold")
    require(candidate["conditional_G_minimal_lift_formula_proved"] is True, "lift formula")
    require(candidate["diagonal_HYM_metric_candidate_available"] is True, "metric candidate")
    for key in [
        "source_metric_bound_to_E_H_UV",
        "selected_minimal_lift_rule_emitted",
        "finite_Huv_scalar_reduction_emitted",
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
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1",
        "candidate next",
    )

    require(formal["status"] == "FORMAL_UV_EXACT_SEQUENCE_SCAFFOLD_CLOSED_NOT_ACTION_BINDING", "formal status")
    scaffold = formal["closed_formal_scaffold"]
    require(scaffold["ordered_UV_basis"] == ["H_u", "H_d^dagger"], "basis")
    require(scaffold["basis_labels_closed"] is True, "basis labels")
    require(scaffold["quotient_rank"] == 1, "quotient rank")
    require(scaffold["q_Hu"] == "H", "q Hu")
    require(scaffold["q_Hd_dagger"] == "H", "q Hd")
    require(scaffold["kernel_generator"] == "H_u - H_d^dagger", "kernel")
    require(scaffold["formal_UV_exact_sequence_scaffold_closed"] is True, "scaffold closed")
    require_all_false(formal["not_yet_closed"], "formal not yet")

    require(lift["status"] == "CONDITIONAL_G_MINIMAL_LIFT_FORMULA_PROVED_SOURCE_BINDING_OPEN", "lift status")
    general = lift["general_positive_diagonal_metric_formula"]
    require(general["conditional_formula_proved"] is True, "general formula")
    require(general["c_u"] == "g_d/(g_u+g_d)", "c_u formula")
    require(general["c_d"] == "g_u/(g_u+g_d)", "c_d formula")
    special = lift["diagonal_HYM_specialization_if_bound_to_E_H_UV"]
    require(special["metric_candidate"] == ["exp(u)", "exp(-u)"], "metric candidate")
    require(special["c_u"] == "1/(1+exp(2u))", "special c_u")
    require(special["c_d"] == "exp(2u)/(1+exp(2u))", "special c_d")
    require(special["conditional_local_s_beta"] == "tanh(2u)^2", "special s_beta")
    require(special["conditional_local_s_beta_max_from_current_u_bounds"] > 0.0, "s_beta bound")
    require(special["conditional_local_s_beta_max_from_current_u_bounds"] < 1.0, "s_beta bound high")
    require(special["finite_scalar_reduction_emitted"] is False, "finite reduction")
    require_all_false(lift["required_before_promotion"], "required before promotion")
    decision = lift["decision"]
    require(decision["conditional_minimal_lift_formula_proved"] is True, "decision formula")
    require(decision["selected_minimal_lift_promoted"] is False, "lift promoted")
    require(decision["selected_s_beta_promoted"] is False, "s_beta promoted")

    require(binding["status"] == "ACTUAL_UV_HIGGS_PLANE_BINDING_ATTEMPT_FAILS_SOURCE_BINDING", "binding status")
    clauses = binding["clause_status"]
    require(clauses["formal_ordered_UV_basis_and_quotient_scaffold_closed"] is True, "binding formal")
    require(clauses["selected_diagonal_HYM_metric_candidate_available"] is True, "binding metric")
    for key in [
        "selected_terminal_source_action_binding_to_E_H_UV_closed",
        "selected_diagonal_HYM_metric_proven_as_metric_on_E_H_UV",
        "same_source_minimal_lift_rule_emitted",
        "same_source_rank_one_projector_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "finite_Huv_reduction_exactness_certificate_emitted",
    ]:
        require(clauses[key] is False, f"binding overclosed {key}")
    require(clauses["no_measured_Higgs_or_beta_selector_used"] is True, "no observed selector")
    for key, value in binding["actual_outputs"].items():
        require(value is None, f"actual output emitted {key}")
    binding_decision = binding["decision"]
    require(binding_decision["UV_Higgs_plane_binding_closed"] is False, "binding closed")
    require(binding_decision["H7B1T_closes_formal_scaffold_and_conditional_formula_only"] is True, "binding partial")
    require(binding_decision["strict_no_knob_Higgs_closure"] is False, "binding closure")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1T", "no cycle")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1A_underdetermination"] is False, "reopen A")
    require(circ["is_reopening_H7B1D_conditional_diagonal_endpoint"] is False, "reopen D")
    require(circ["is_promoting_conditional_formula_as_value"] is False, "formula promoted")
    require(circ["is_using_observed_lambda_or_tan_beta"] is False, "observed use")
    require(len(no_cycle["new_information_added"]) == 4, "new info count")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1U_SOURCE_BOUND_METRIC_AND_FINITE_REDUCTION", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multi")
    require("not fitted beta or measured lambda_H" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["formal_UV_exact_sequence_scaffold_closed"] is True, "cert formal")
    require(cert["conditional_G_minimal_lift_formula_proved"] is True, "cert lift")
    require(cert["diagonal_HYM_metric_candidate_available"] is True, "cert metric")
    require(cert["source_metric_bound_to_E_H_UV"] is False, "cert binding")
    require(cert["selected_minimal_lift_rule_emitted"] is False, "cert lift emitted")
    require(cert["finite_Huv_scalar_reduction_emitted"] is False, "cert reduction")
    require(cert["selected_s_beta_value_found"] is False, "cert s_beta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("formal UV exact-sequence scaffold closed        True" in note, "note formal")
    require("conditional G-minimal lift formula proved       True" in note, "note lift")
    require("source metric bound to E_H^UV                   False" in note, "note binding")
    require("s_beta(u)=tanh(2u)^2" in note, "note formula")
    require("H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION" in note, "note next")

    print("CONST-HIGGS-01 H7B1T UV binding/minimal-lift audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
