"""Audit CONST-HIGGS-01 H6F symbolic D-term boundary replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6f_symbolic_dterm_boundary_replay"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
BOUNDARY_REPLAY = BASE / "symbolic_boundary_replay_functor.packet.json"
RG_CONTRACT = BASE / "higgs_rg_transport_contract.packet.json"
SOURCE_GATE = BASE / "source_input_gate_ledger.packet.json"
SUPERSET_MAP = BASE / "superset_path_map.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6F_SymbolicDTermBoundaryReplay_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6F_SYMBOLIC_DTERM_REPLAY_BUILT_VALUES_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


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
    boundary = load(BOUNDARY_REPLAY)
    rg = load(RG_CONTRACT)
    gate = load(SOURCE_GATE)
    superset = load(SUPERSET_MAP)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("boundary", boundary),
        ("rg", rg),
        ("gate", gate),
        ("superset", superset),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["symbolic_boundary_replay_functor_defined"] is True, "replay functor")
    require(candidate["Higgs_RG_transport_contract_declared"] is True, "RG contract")
    require(candidate["source_input_gate_ledger_built"] is True, "gate ledger")
    require(candidate["superset_paths_separated"] is True, "superset separated")
    require(candidate["selected_UV_beta_source_found"] is False, "UV beta overclosed")
    require(candidate["beta_primitive_declared_now"] is False, "beta declared")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    functor = boundary["boundary_functor"]
    require(functor["tree_boundary"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "tree boundary")
    require("tan_beta_H" in functor["same_formula_rewritten_with_tan_beta"], "tan rewrite")
    guards = boundary["strict_replay_guards"]
    for key in [
        "uses_measured_mH_or_v_to_choose_beta",
        "uses_measured_lambda_to_choose_threshold",
        "promotes_tan_beta_10",
        "promotes_single_Higgs_projection_to_UV_angle",
        "declares_beta_primitive",
    ]:
        require(guards[key] is False, f"guard {key}")
    outputs = boundary["output_status"]
    require(outputs["symbolic_boundary_defined"] is True, "symbolic output")
    require(outputs["numeric_boundary_value_emitted"] is False, "numeric boundary")
    require(outputs["numeric_low_scale_lambda_emitted"] is False, "numeric low")
    require(outputs["strict_no_knob_Higgs_closure"] is False, "boundary no-knob")

    transport = rg["transport_operator"]
    require("R_Higgs" == transport["name"], "transport name")
    require("lambda_H(mu_obs)" in transport["formal_action"], "transport action")
    require(transport["exact_numeric_algorithm_filled"] is False, "numeric algorithm")
    require(transport["accepted_external_benchmark_values_used_as_selectors"] is False, "benchmark selector")
    support = rg["current_imported_support"]
    require(support["rg_policy_scaffold_declared"] is True, "RG scaffold")
    require(support["one_loop_diagnostic_engine_available"] is True, "diagnostic engine")
    require(support["minimal_threshold_replay_policy_available"] is True, "minimal threshold")
    require(support["weak_mixing_conditional_profile_executable"] is True, "weak profile")
    required = rg["required_before_numerical_Higgs_comparison"]
    for key, value in required.items():
        require(value is False, f"required {key} overfilled")

    closed = gate["closed_inputs"]
    require(closed["low_energy_single_Higgs_projection"] is True, "closed single Higgs")
    require(closed["standard_Dterm_factor"] is True, "closed factor")
    require(closed["symbolic_boundary_formula"] is True, "closed symbolic")
    require(closed["primitive_beta_policy_written"] is True, "closed policy")
    open_ = gate["open_strict_inputs"]
    require(open_["selected_UV_beta_source_found"] is False, "gate UV beta")
    require(open_["beta_primitive_declared_now"] is False, "gate primitive")
    require(open_["new_Higgs_specific_parameters_now"] == 0, "gate params")
    require(open_["numeric_lambda_H_derived"] is False, "gate lambda")
    require("Higgs mass backsolve" in gate["acceptance_policy"]["rejects"], "reject backsolve")
    require("threshold residual scan against measured lambda" in gate["acceptance_policy"]["rejects"], "reject residual scan")

    require(superset["locked_target"].startswith("source-selected Higgs quartic"), "locked target")
    require(superset["paths"]["route_A_intrinsic_row"]["current_status"] == "OPEN", "route A")
    require(superset["paths"]["route_B_Dterm_boundary"]["current_status"] == "SYMBOLIC_REPLAY_READY_VALUES_OPEN", "route B")
    require(superset["paths"]["route_C_explicit_beta_primitive"]["current_status"] == "POLICY_READY_NOT_DECLARED", "route C")
    rule = superset["combination_rule"]
    require(rule["may_compare_paths"] is True, "may compare")
    require(rule["may_reuse_a_declared_universal_primitive_across_paths"] is True, "universal reuse")
    require(rule["may_sum_independent_path_residuals_to_fit_lambda"] is False, "fit residuals")
    require(rule["must_label_tier_before_numeric_comparison"] is True, "tier label")

    require("H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM" in next_work["strict_next"]["label"], "next strict")
    require("H7P-BETA-OR-SHARED-ACTION-PRIMITIVE-REPLAY" in next_work["portfolio_next"]["label"], "next portfolio")
    require(cert["status"] == STATUS, "cert status")
    require(cert["symbolic_boundary_replay_functor_defined"] is True, "cert functor")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H6F-SYMBOLIC-DTERM" in note and "R_Higgs" in note, "note")

    print("CONST-HIGGS-01 H6F symbolic D-term boundary replay audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
