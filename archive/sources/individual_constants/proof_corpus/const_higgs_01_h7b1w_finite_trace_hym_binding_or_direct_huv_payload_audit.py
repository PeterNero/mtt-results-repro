"""Audit CONST-HIGGS-01 H7B1W finite-trace/HYM-binding or direct-Huv gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SOURCE_HUNT = BASE / "corpus_and_repo_source_hunt.packet.json"
EXTERNAL_CRITERION = BASE / "external_hym_quadrature_criterion.packet.json"
TRACE_ATTEMPT = BASE / "finite_trace_binding_attempt.packet.json"
DIRECT_HUV = BASE / "direct_huv_payload_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1W_BRIDGE_CRITERION_BUILT_PAYLOAD_OPEN"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1X_SelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows_v1"


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
    source_hunt = load(SOURCE_HUNT)
    external = load(EXTERNAL_CRITERION)
    trace = load(TRACE_ATTEMPT)
    direct = load(DIRECT_HUV)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("source_hunt", source_hunt),
        ("external", external),
        ("trace", trace),
        ("direct", direct),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["name"] == "H7B1WFiniteTraceHYMBindingCutsetTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    for key in [
        "H7B1V_imported",
        "H7B1W_A_trace_binding_route_attacked",
        "H7B1W_B_direct_Huv_route_attacked",
        "q79_finite_connection_cutset_imported",
        "qa_su3_connection_witness_open_imported",
        "sm_transition_payload_gate_imported",
        "strominger_HYM_selection_support_imported",
        "external_HYM_quadrature_criterion_imported_method_only",
        "selected_Higgs_HYM_quadrature_bridge_criterion_emitted",
    ]:
        require(candidate[key] is True, f"candidate support missing {key}")
    for key in [
        "finite_trace_HYM_binding_closed",
        "same_source_trace_to_grid_quadrature_identity_emitted",
        "same_source_E_H_UV_metric_binding_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
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

    require(
        source_hunt["status"] == "CORPUS_REPO_SOURCE_HUNT_FINITE_TRACE_SUPPORT_STRONG_HUV_PAYLOAD_ABSENT",
        "source hunt status",
    )
    require(source_hunt["current_repo_H7B1V"]["uniform_candidate_best_trace_aligned"] is True, "H7B1V uniform")
    require(source_hunt["current_repo_H7B1V"]["trace_to_HYM_grid_binding_closed"] is False, "H7B1V binding")
    require(source_hunt["q79_repro_import"]["all_finite_value_shapes_present"] is True, "q79 finite values")
    require(
        source_hunt["q79_repro_import"]["honest_replay_cutset_status"]
        == "HONEST_REPLAY_BLOCKED_BY_SOURCE_TRACE_AND_FULL_OPERATOR_PROVENANCE",
        "q79 cutset",
    )
    require(source_hunt["q79_repro_import"]["selected_trace_equality_open"] is True, "q79 trace open")
    require(source_hunt["qa_su3_import"]["finite_connection_prefix_values_present"] is True, "qa finite")
    require(source_hunt["qa_su3_import"]["selected_connection_witness_values_absent"] is True, "qa witness absent")
    require(source_hunt["qa_su3_import"]["selected_hym_connection_constructed"] is False, "qa HYM constructed")
    require(source_hunt["qa_su3_import"]["typed_monad_cech_witness_constructed"] is False, "qa Cech")
    require(source_hunt["sm_transition_gate_import"]["theorem_proved"] is True, "sm theorem")
    require(source_hunt["sm_transition_gate_import"]["transition_payload_closed"] is False, "sm transition")
    require(source_hunt["sm_transition_gate_import"]["selected_trace_equality_open"] is True, "sm trace")
    require(source_hunt["strings_flux_corpus_import"]["strominger_selection_potential_present"] is True, "strings Xi")
    require(source_hunt["strings_flux_corpus_import"]["hym_on_gauduchon_present"] is True, "strings HYM")
    require(source_hunt["strings_flux_corpus_import"]["finite_section_ring_quadrature_emitted"] is False, "strings quad")
    require_all_false(source_hunt["decision"], "source hunt decision")

    require(external["status"] == "EXTERNAL_HYM_QUADRATURE_CRITERION_IMPORTED_METHOD_ONLY", "external status")
    require(external["not_MTT_source_selector"] is True, "external guardrail")
    require_all_true(external["criterion_imported"], "external criterion")
    require(len(external["external_method_sources"]) == 3, "external source count")
    for item in external["external_method_sources"]:
        require(item["used_as_source_selector"] is False, "external source selector")
    require(
        external["impact_on_H7B1W"]["required_bridge_name"]
        == "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem",
        "external bridge",
    )
    require(external["impact_on_H7B1W"]["uniform_trace_candidate_can_be_promoted_without_MTT_bridge"] is False, "external no promote")

    require(trace["status"] == "FINITE_TRACE_HYM_BINDING_CRITERION_BUILT_CURRENT_PAYLOAD_OPEN", "trace status")
    require_all_true(trace["closed_support"], "trace support")
    require(trace["bridge_criterion"]["criterion_emitted"] is True, "trace criterion")
    require(trace["bridge_criterion"]["name"] == "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem", "trace name")
    require(len(trace["bridge_criterion"]["clauses"]) == 9, "trace clause count")
    require_all_true(trace["missing_payload"], "trace missing payload")
    require(trace["decision"]["finite_trace_HYM_binding_closed"] is False, "trace binding")
    require(trace["decision"]["uniform_mean_can_be_promoted_now"] is False, "trace uniform")
    require(trace["decision"]["selected_s_beta_promoted"] is False, "trace s_beta")

    require(direct["status"] == "DIRECT_HERM2_HUV_PAYLOAD_SEARCHED_VALUES_ABSENT", "direct status")
    require(direct["imported_H7B1V_direct_attempt_status"] == "DIRECT_HERM2_HUV_SOURCE_ATTEMPT_STILL_OPEN", "direct import")
    for key, value in direct["actual_outputs"].items():
        require(value is None, f"direct output emitted {key}")
    require_all_false(direct["decision"], "direct decision")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1W", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    require_all_false(no_cycle["circulation_test"], "circulation")
    require(len(no_cycle["new_information_added"]) == 4, "new information count")

    require(
        next_work["status"] == "NEXT_WORKORDER_H7B1X_SELECTED_HIGGS_HYM_SECTION_RING_QUADRATURE_OR_DIRECT_HUV_ROWS",
        "next status",
    )
    require(
        next_work["primary_next"]["label"].endswith(
            "H7B1X-SELECTED-HIGGS-HYM-SECTION-RING-QUADRATURE-OR-DIRECT-HUV-ROWS"
        ),
        "next label",
    )
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multi")
    require("not a fitted Higgs mass/quartic" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_Higgs_HYM_quadrature_bridge_criterion_emitted"] is True, "cert criterion")
    require(cert["finite_trace_HYM_binding_closed"] is False, "cert binding")
    require(cert["direct_Herm2_Huv_payload_emitted"] is False, "cert direct")
    require(cert["selected_s_beta_value_found"] is False, "cert s_beta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("H7B1W-A finite trace/HYM binding attacked    True" in note, "note trace")
    require("bridge criterion emitted                    True" in note, "note criterion")
    require("finite trace/HYM binding closed             False" in note, "note binding")
    require("direct Herm2 Huv payload emitted            False" in note, "note direct")
    require("s_beta / lambda_H promoted                  False" in note, "note s_beta")
    require("H7B1X-SELECTED-HIGGS-HYM-SECTION-RING-QUADRATURE-OR-DIRECT-HUV-ROWS" in note, "note next")

    print("CONST-HIGGS-01 H7B1W finite-trace/HYM-binding or direct-Huv audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
