"""Audit CONST-HIGGS-01 H7B1V reduction-selector/direct-Herm2 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
REDUCTION_SELECTOR = BASE / "reduction_selector_triage.packet.json"
TRACE_BINDING = BASE / "finite_trace_to_hym_grid_binding_attempt.packet.json"
DIRECT_HERM2 = BASE / "direct_herm2_huv_source_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1V_ReductionSelectorOrDirectHerm2HuvSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1V_TRACE_SELECTOR_TRIAGED_BINDING_OPEN"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1"


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
    selector = load(REDUCTION_SELECTOR)
    trace = load(TRACE_BINDING)
    direct = load(DIRECT_HERM2)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("selector", selector),
        ("trace", trace),
        ("direct", direct),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["name"] == "H7B1VReductionSelectorTriageTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1U_imported"] is True, "H7B1U import")
    require(candidate["finite_Weyl_trace_measure_derived"] is True, "finite Weyl trace")
    require(candidate["selected_trace_payload_DE_gap_layer_closed"] is True, "trace payload")
    require(candidate["uniform_reduction_best_current_source_aligned_candidate"] is True, "uniform support")
    require(close(candidate["uniform_mean_conditional_s_beta"], 0.004701083905943647), "candidate uniform")
    require(close(candidate["rho_weighted_mean_conditional_s_beta"], 0.01175427147946371), "candidate rho")
    require(close(candidate["exp_density_weighted_mean_conditional_s_beta"], 0.012349317823559027), "candidate exp")
    for key in [
        "trace_to_HYM_grid_binding_closed",
        "source_metric_bound_to_E_H_UV",
        "selected_reduction_selector_emitted",
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
    require(candidate["selected_next_artifact"] == NEXT_ARTIFACT, "candidate next")

    require(selector["status"] == "REDUCTION_SELECTOR_TRIAGED_UNIFORM_SUPPORT_BINDING_OPEN", "selector status")
    decision = selector["selector_decision"]
    require(decision["finite_Weyl_normalized_trace_measure_derived"] is True, "selector finite trace")
    require(decision["selected_trace_payload_DE_gap_layer_closed"] is True, "selector trace payload")
    require(decision["uniform_reduction_best_current_source_aligned_candidate"] is True, "selector uniform")
    require(decision["physical_measure_promoted_as_Higgs_projection"] is False, "selector physical measure")
    require(decision["selected_reduction_selector_emitted"] is False, "selector reduction")
    require(decision["selected_s_beta_promoted"] is False, "selector s_beta")
    reductions = selector["candidate_reductions"]
    require(close(reductions["uniform_mean"]["value"], 0.004701083905943647), "selector uniform value")
    require(reductions["uniform_mean"]["finite_Weyl_trace_support"] is True, "selector uniform support")
    require(reductions["uniform_mean"]["trace_to_HYM_grid_binding_closed"] is False, "selector binding")
    require(reductions["uniform_mean"]["promoted"] is False, "selector uniform promoted")
    require(close(reductions["rho_weighted_mean"]["value"], 0.01175427147946371), "selector rho value")
    require(reductions["rho_weighted_mean"]["projection_measure_theorem_emitted"] is False, "selector rho theorem")
    require(reductions["rho_weighted_mean"]["promoted"] is False, "selector rho promoted")
    require(close(reductions["exp_density_weighted_mean"]["value"], 0.012349317823559027), "selector exp value")
    require(reductions["exp_density_weighted_mean"]["projection_measure_theorem_emitted"] is False, "selector exp theorem")
    require(reductions["exp_density_weighted_mean"]["promoted"] is False, "selector exp promoted")

    require(trace["status"] == "FINITE_TRACE_TO_HYM_GRID_BINDING_ATTEMPT_OPEN", "trace status")
    require_all_true(trace["closed_support"], "trace support")
    for key, value in trace["blocked_fields"].items():
        require(value is False, f"trace blocked field overclosed {key}")
    require(
        trace["minimal_binding_theorem_needed"]["name"]
        == "SelectedFiniteTraceHYMGridHiggsProjectionBindingTheorem",
        "trace theorem needed",
    )
    trace_decision = trace["decision"]
    require(trace_decision["trace_to_HYM_grid_binding_closed"] is False, "trace binding decision")
    require(trace_decision["uniform_mean_can_be_promoted_now"] is False, "trace promotion decision")

    require(direct["status"] == "DIRECT_HERM2_HUV_SOURCE_ATTEMPT_STILL_OPEN", "direct status")
    payload = direct["payload_status"]
    require(payload["conditional_functor_ready"] is True, "direct functor")
    require(payload["B_Huv_request_ready"] is True, "B request")
    require(payload["M_source_request_ready"] is True, "M request")
    require(payload["B_Huv_value_emitted"] is False, "B emitted")
    require(payload["M_source_value_emitted"] is False, "M emitted")
    require(payload["direct_Huu_Hud_Hdd_emitted"] is False, "Huv rows")
    for key, value in direct["actual_outputs"].items():
        require(value is None, f"direct output emitted {key}")
    direct_decision = direct["decision"]
    require(direct_decision["direct_Herm2_Huv_payload_emitted"] is False, "direct payload")
    require(direct_decision["selected_s_beta_promoted"] is False, "direct s_beta")
    require(direct_decision["numeric_lambda_H_derived"] is False, "direct lambda")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1V", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    for key, value in no_cycle["circulation_test"].items():
        require(value is False, f"circulation detected {key}")
    require(len(no_cycle["new_information_added"]) == 4, "new information count")

    require(
        next_work["status"] == "NEXT_WORKORDER_H7B1W_FINITE_TRACE_HYM_BINDING_OR_DIRECT_HUV_PAYLOAD",
        "next status",
    )
    require(next_work["primary_next"]["label"].endswith("H7B1W-FINITE-TRACE-HYM-BINDING-OR-DIRECT-HUV-PAYLOAD"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multi")
    require("not a fitted Higgs quartic" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["finite_Weyl_trace_measure_derived"] is True, "cert trace")
    require(cert["uniform_reduction_best_current_source_aligned_candidate"] is True, "cert uniform support")
    require(close(cert["uniform_mean_conditional_s_beta"], 0.004701083905943647), "cert uniform")
    require(cert["trace_to_HYM_grid_binding_closed"] is False, "cert binding")
    require(cert["selected_reduction_selector_emitted"] is False, "cert selector")
    require(cert["direct_Herm2_Huv_payload_emitted"] is False, "cert direct")
    require(cert["selected_s_beta_value_found"] is False, "cert s_beta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("finite Weyl trace measure derived             True" in note, "note trace")
    require("uniform reduction best trace-aligned candidate True" in note, "note uniform")
    require("trace-to-HYM-grid binding closed              False" in note, "note binding")
    require("selected reduction selector emitted           False" in note, "note selector")
    require("s_beta / lambda_H promoted                    False" in note, "note no promotion")
    require("SelectedFiniteTraceHYMGridHiggsProjectionBindingTheorem" in note, "note theorem")
    require("H7B1W-FINITE-TRACE-HYM-BINDING-OR-DIRECT-HUV-PAYLOAD" in note, "note next")

    print("CONST-HIGGS-01 H7B1V reduction-selector/direct-Herm2 audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
