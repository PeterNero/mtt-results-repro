"""Audit CONST-HIGGS-01 H7B1X Higgs section-ring/quadrature or direct-Huv gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
ORDERED_LABELS = BASE / "ordered_higgs_channel_label_import.packet.json"
VALIDATOR = BASE / "bridge_validator_replay.packet.json"
REQUEST = BASE / "section_basis_quadrature_payload_request.packet.json"
DIRECT_ROWS = BASE / "direct_herm2_huv_rows_search.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1X_SelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1X_ORDERED_HIGGS_CHANNEL_LABELS_FILLED_OPERATOR_QUADRATURE_OPEN"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1Y_SelectedEHUvSectionBasisQuadratureOrHerm2RowValues_v1"


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
    ordered = load(ORDERED_LABELS)
    validator = load(VALIDATOR)
    request = load(REQUEST)
    direct = load(DIRECT_ROWS)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("ordered", ordered),
        ("validator", validator),
        ("request", request),
        ("direct", direct),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["name"] == "H7B1XOrderedHiggsChannelScaffoldTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    for key in [
        "H7B1W_imported",
        "H7B1T_imported",
        "q79_single_higgs_projection_imported",
        "q79_E6_SU5_dictionary_imported",
        "qa_terminal_ordered_source_layer_imported",
        "sm_Hdagger_conjugate_basis_policy_imported",
        "ordered_Hu_Hd_channel_scaffold_closed",
        "E_H_UV_exact_sequence_scaffold_closed",
        "bridge_validator_first_clause_filled",
    ]:
        require(candidate[key] is True, f"candidate support missing {key}")
    for key in [
        "selected_E_H_UV_section_basis_emitted",
        "selected_HYM_metric_or_connection_emitted",
        "quadrature_weights_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "Higgs_projection_measure_equality_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
        "same_branch_selected_operator_emission",
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

    require(ordered["status"] == "ORDERED_HIGGS_CHANNEL_LABEL_SCAFFOLD_FILLED_OPERATOR_LAYER_OPEN", "ordered status")
    require_all_true(ordered["closed_support"], "ordered support")
    channel = ordered["ordered_channel_map"]
    require(channel["E_H_UV_basis_labels"] == ["H_u", "H_d^dagger"], "E_H_UV labels")
    require(channel["low_energy_projection"]["H_u"] == "H", "Hu projection")
    require(channel["low_energy_projection"]["H_d"] == "H^dagger", "Hd projection")
    require(channel["quotient"]["q_Hu"] == "H", "q Hu")
    require(channel["quotient"]["q_Hd_dagger"] == "H", "q Hd")
    guard = ordered["scope_guardrail"]
    require(guard["ordered_source_label_layer_only"] is True, "ordered scope")
    require(guard["principle_unconditional_in_mtt_axioms"] is False, "principle overclaim")
    require(guard["same_branch_selected_operator_emission"] is False, "operator emission")
    require(guard["operator_layer_Pic0_closed"] is False, "Pic0")
    require(guard["selected_overlap_normalization_emitted"] is False, "overlap")
    decision = ordered["decision"]
    require(decision["ordered_Hu_Hd_channel_scaffold_closed"] is True, "ordered decision")
    require(decision["E_H_UV_exact_sequence_scaffold_closed"] is True, "sequence decision")
    require(decision["selected_E_H_UV_section_basis_emitted"] is False, "basis emitted")
    require(decision["selected_HYM_metric_or_connection_emitted"] is False, "metric emitted")
    require(decision["quadrature_weights_emitted"] is False, "weights emitted")
    require(decision["trace_to_H7B1U_grid_identity_emitted"] is False, "trace grid")
    require(decision["selected_s_beta_promoted"] is False, "s beta")

    require(
        validator["status"] == "HIGGS_HYM_QUADRATURE_BRIDGE_VALIDATOR_FIRST_CLAUSE_FILLED_REST_OPEN",
        "validator status",
    )
    clauses = validator["clauses"]
    require(clauses["C1_branch_and_ordered_channel_labels"]["closed"] is True, "validator C1")
    for key in [
        "C2_typed_E_H_UV_section_basis_or_finite_quotient",
        "C3_selected_HYM_metric_or_connection_fixed_point",
        "C4_quadrature_weights_and_trace_normalization",
        "C5_trace_to_H7B1U_grid_and_projection_measure_identity",
        "C6_no_extra_boundary_or_source_term",
        "B_direct_Herm2_Huv_rows",
    ]:
        require(clauses[key]["closed"] is False, f"validator overclosed {key}")
    validator_decision = validator["decision"]
    require(validator_decision["first_clause_filled"] is True, "first clause")
    require(validator_decision["bridge_validator_complete"] is False, "validator complete")
    require(validator_decision["uniform_mean_can_be_promoted_now"] is False, "uniform promote")
    require(validator_decision["direct_Herm2_Huv_payload_emitted"] is False, "direct validator")
    require(validator_decision["selected_s_beta_promoted"] is False, "validator s beta")

    require(request["status"] == "E_H_UV_SECTION_BASIS_QUADRATURE_PAYLOAD_REQUEST_SHARPENED", "request status")
    require_all_true(request["filled_now"], "request filled")
    for key, value in request["must_emit_next"].items():
        require(value is None, f"request emitted {key}")
    require(len(request["forbidden_promotions"]) == 4, "forbidden count")
    require(request["decision"]["payload_request_complete"] is True, "request complete")
    require(request["decision"]["selected_E_H_UV_section_basis_emitted"] is False, "request basis")
    require(request["decision"]["quadrature_weights_emitted"] is False, "request weights")
    require(request["decision"]["trace_to_H7B1U_grid_identity_emitted"] is False, "request trace")

    require(direct["status"] == "DIRECT_HERM2_HUV_ROWS_SEARCHED_VALUES_ABSENT_AFTER_LABEL_FILL", "direct status")
    for key, value in direct["actual_outputs"].items():
        require(value is None, f"direct output emitted {key}")
    require_all_false(direct["decision"], "direct decision")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1X", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    require_all_false(no_cycle["circulation_test"], "circulation")
    require(len(no_cycle["new_information_added"]) == 4, "new information count")

    require(
        next_work["status"] == "NEXT_WORKORDER_H7B1Y_SELECTED_EHUV_SECTION_BASIS_QUADRATURE_OR_HERM2_ROW_VALUES",
        "next status",
    )
    require(
        next_work["primary_next"]["label"].endswith(
            "H7B1Y-SELECTED-EHUV-SECTION-BASIS-QUADRATURE-OR-HERM2-ROW-VALUES"
        ),
        "next label",
    )
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multi")
    require("not fitted lambda_H or tan beta" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["ordered_Hu_Hd_channel_scaffold_closed"] is True, "cert ordered")
    require(cert["E_H_UV_exact_sequence_scaffold_closed"] is True, "cert sequence")
    require(cert["bridge_validator_first_clause_filled"] is True, "cert first clause")
    require(cert["selected_E_H_UV_section_basis_emitted"] is False, "cert basis")
    require(cert["selected_HYM_metric_or_connection_emitted"] is False, "cert metric")
    require(cert["quadrature_weights_emitted"] is False, "cert weights")
    require(cert["trace_to_H7B1U_grid_identity_emitted"] is False, "cert trace")
    require(cert["direct_Herm2_Huv_payload_emitted"] is False, "cert direct")
    require(cert["selected_s_beta_value_found"] is False, "cert s beta")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("ordered Hu/Hd channel scaffold closed        True" in note, "note ordered")
    require("selected E_H^UV finite section basis emitted False" in note, "note basis")
    require("quadrature weights emitted                   False" in note, "note weights")
    require("direct Herm2 Huv payload emitted             False" in note, "note direct")
    require("s_beta / lambda_H promoted                   False" in note, "note s beta")
    require("H7B1Y-SELECTED-EHUV-SECTION-BASIS-QUADRATURE-OR-HERM2-ROW-VALUES" in note, "note next")

    print("CONST-HIGGS-01 H7B1X Higgs section-ring/quadrature or direct-Huv audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
