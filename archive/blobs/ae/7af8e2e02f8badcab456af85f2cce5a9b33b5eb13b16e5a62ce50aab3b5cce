"""Audit CONST-HIGGS-01 H7B1S Huv bridge functor or nonlinear HYM row execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SECTION_C1_BRIDGE = BASE / "sectionring_and_c1_bridge_attempt.packet.json"
HYM_ROW_ATTEMPT = BASE / "direct_nonlinear_hym_row_execution_attempt.packet.json"
MINIMAL_THEOREM = BASE / "minimal_uv_higgs_plane_binding_theorem.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1S_HuvBridgeFunctorOrNonlinearHYMRowExecution_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1S_NEARHITS_TESTED_UV_HIGGS_PLANE_BINDING_OPEN"


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
    section = load(SECTION_C1_BRIDGE)
    hym = load(HYM_ROW_ATTEMPT)
    minimal = load(MINIMAL_THEOREM)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("section", section),
        ("hym", hym),
        ("minimal", minimal),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem")
    require(candidate["H7B1R_imported"] is True, "H7B1R import")
    require(candidate["terminal_source_operator_kernel_selects_L3_K2"] is True, "terminal source")
    require(candidate["diagonal_HYM_first_solve_support_closed"] is True, "diagonal HYM")
    require(candidate["first_C1_row_exact_value_computed"] is True, "first row")
    require(candidate["sectionring_Hu_Hd_channel_labels_present"] is True, "section labels")
    require(candidate["minimal_missing_theorem_built"] is True, "minimal theorem")
    for key in [
        "UV_Higgs_plane_binding_closed",
        "bridge_functor_emitted",
        "direct_nonlinear_HYM_rows_emitted",
        "UV_twoHiggs_basis_emitted",
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
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1T_UVHiggsPlaneBindingOrMinimalLiftTheorem_v1",
        "candidate next",
    )

    require(section["status"] == "SECTIONRING_AND_C1_NEARHITS_TESTED_NO_HUV_BRIDGE", "section status")
    require_all_true(section["nearhit_support"], "section nearhits")
    why_not = section["why_not_Huv_bridge"]
    require(why_not["first_row_codomain"] == "u:phase:r0c0", "first row codomain")
    require(why_not["flavor_HuHd_notation_is_Yukawa_Hermitian_not_Higgs_plane"] is True, "flavor notation")
    for key in [
        "sectionring_readout_closed",
        "terminal_monad_selector_closed_in_sectionring_packet",
        "first_row_independent_and_provenance_clean",
        "first_row_provenance_independent",
        "Herm2_Huv_codomain_emitted",
        "T_Huv_emitted",
    ]:
        require(why_not[key] is False, f"section overclosed {key}")
    decision = section["decision"]
    require(decision["sectionring_C1_bridge_closes_Huv"] is False, "section bridge")
    require(decision["operator_channel_labels_can_replace_UV_Higgs_metric"] is False, "labels overpromoted")
    require(decision["first_C1_row_can_replace_Huv_row"] is False, "row overpromoted")

    require(hym["status"] == "DIAGONAL_HYM_AND_TERMINAL_SOURCE_SUPPORT_CLOSED_HUV_BINDING_OPEN", "hym status")
    require_all_true(hym["closed_support"], "hym support")
    blocked = hym["blocked_binding"]
    require_all_false(blocked, "blocked binding")
    payload = hym["diagonal_HYM_payload"]
    require(payload["H_diagonal"] == ["exp(u)", "exp(-u)"], "H diagonal")
    require(payload["residual_l2"] < 1e-10, "HYM residual")
    strict = hym["strict_outputs"]
    for key, value in strict.items():
        require(value is None, f"strict Huv output emitted {key}")
    hym_decision = hym["decision"]
    require(hym_decision["direct_nonlinear_HYM_row_execution_closes_Huv"] is False, "hym row")
    require(hym_decision["diagonal_HYM_metric_promoted_to_UV_Higgs_plane_metric"] is False, "metric overpromoted")
    require(hym_decision["raw_terminal_source_operator_promoted_to_Huv_rows"] is False, "raw source overpromoted")

    require(minimal["status"] == "MINIMAL_THEOREM_REDUCED_TO_UV_HIGGS_PLANE_BINDING_AND_LIGHTLINE", "minimal status")
    theorem = minimal["theorem_to_prove_next"]
    require(theorem["name"] == "SelectedUVHiggsPlaneBindingAndLightLineSourceTheorem", "minimal theorem name")
    require(len(theorem["clauses"]) == 5, "minimal clauses")
    why_min = minimal["why_this_is_now_minimal"]
    require(why_min["alpha_overlap_blocker_retired"] is True, "alpha retired")
    require(why_min["lambda12_shortcut_retired"] is True, "lambda retired")
    require(why_min["single_Higgs_quotient_underdetermination_proved"] is True, "quotient proof")
    require(why_min["diagonal_HYM_support_available"] is True, "HYM support")
    require(why_min["terminal_source_support_available"] is True, "terminal support")
    require_all_true(minimal["would_close_if_proved"], "would close")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1S", "no cycle")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1R"] is False, "reopen R")
    require(circ["is_reopening_quotient_underdetermination"] is False, "reopen quotient")
    require(circ["is_promoting_nearhit_notation_as_Huv"] is False, "nearhit overpromoted")
    require(len(circ["new_information_added"]) == 4, "new info")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1T_UV_HIGGS_PLANE_BINDING_OR_MINIMAL_LIFT_THEOREM", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multiple")

    require(cert["status"] == STATUS, "cert status")
    require(cert["terminal_source_operator_kernel_selects_L3_K2"] is True, "cert terminal")
    require(cert["diagonal_HYM_first_solve_support_closed"] is True, "cert HYM")
    require(cert["first_C1_row_exact_value_computed"] is True, "cert row")
    require(cert["sectionring_Hu_Hd_channel_labels_present"] is True, "cert section")
    require(cert["minimal_missing_theorem_built"] is True, "cert minimal")
    require(cert["UV_Higgs_plane_binding_closed"] is False, "cert binding")
    require(cert["bridge_functor_emitted"] is False, "cert bridge")
    require(cert["direct_nonlinear_HYM_rows_emitted"] is False, "cert rows")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("terminal source operator selects L3-K2            True" in note, "note terminal")
    require("UV Higgs plane binding closed                     False" in note, "note binding")
    require("H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM" in note, "note next")

    print("CONST-HIGGS-01 H7B1S Huv bridge/nonlinear-HYM audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
