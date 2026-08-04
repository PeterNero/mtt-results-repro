"""Audit CONST-HIGGS-01 H7B1O diagonal HYM payload to Huv transfer gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1o_diagonal_hym_payload_to_huv_transfer_gate"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DIAGONAL_IMPORT = BASE / "diagonal_hym_payload_import.packet.json"
END0_BOUNDARY = BASE / "rank2_end0_payload_boundary.packet.json"
HUV_GATE = BASE / "higgs_huv_transfer_gate.packet.json"
CYCLE_RETIREMENT = BASE / "cycle_retirement.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1O_DiagonalHYMPayloadToHuvTransferGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1O_DIAGONAL_HYM_PAYLOAD_CLOSED_HUV_TRANSFER_OPEN"


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
    diagonal = load(DIAGONAL_IMPORT)
    end0 = load(END0_BOUNDARY)
    huv = load(HUV_GATE)
    retirement = load(CYCLE_RETIREMENT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("diagonal", diagonal),
        ("end0", end0),
        ("huv", huv),
        ("retirement", retirement),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require(candidate["H7B1N_gate_imported"] is True, "H7B1N import")
    require(candidate["selected_diagonal_HYM_first_solve_closed"] is True, "diagonal solve")
    require(candidate["rank2_End0_payload_closed"] is True, "rank2 End0")
    require(candidate["full_diagonal_End0_green_closed"] is True, "full End0 Green")
    require(candidate["row_model_offdiagonal_Ext_control_closed"] is True, "offdiag control")
    require(candidate["rank2_to_Huv_or_sector_transfer_closed"] is False, "transfer overclosed")
    require(candidate["physical_dotD_or_sector_payload_closed"] is False, "physical payload overclosed")
    for key in [
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1P_End0ToHuvOrSectorRouting_v1",
        "candidate next",
    )

    require(diagonal["status"] == "SELECTED_DIAGONAL_HYM_PAYLOAD_IMPORTED_AND_CLOSED", "diagonal status")
    first = diagonal["first_tracefree_step"]
    require(first["closed"] is True, "first correction closed")
    require(first["selected_End0_direction"] == "T3", "first direction")
    require(first["poisson_residual_l2"] < 1e-12, "first residual")
    require(first["phi_min"] < 0 < first["phi_max"], "first phi range")
    exp_s = diagonal["diagonal_expS_step"]
    require(exp_s["closed"] is True, "expS closed")
    require(exp_s["iterations_run"] == 40, "expS iterations")
    require(exp_s["final_residual_l2"] < 1e-12, "expS residual")
    require(exp_s["u_min"] < 0 < exp_s["u_max"], "expS u range")
    op = diagonal["operator_payload_step"]
    require(op["diagonal_metric_closed"] is True, "metric")
    require(op["diagonal_connection_closed"] is True, "connection")
    require(op["curvature_residual_closed"] is True, "curvature")
    require(op["validator_ready"] is False, "operator validator")
    decision = diagonal["branch_decision"]
    require(decision["diagonal_HYM_payload_closed"] is True, "diagonal branch")
    require(decision["counts_as_M_source_or_Huv"] is False, "diagonal promoted")

    require(end0["status"] == "RANK2_END0_PAYLOAD_CLOSED_TRANSFER_VALUES_OPEN", "end0 status")
    closed = end0["closed_source_payloads"]
    for key in [
        "A_HYM_rank2_connection_payload",
        "diagonal_End0_DE_formula",
        "protected_T3_Riesz_Green",
        "T1_T2_covariant_Green",
        "full_diagonal_End0_Riesz_Green",
        "row_model_offdiagonal_Ext_control",
        "dotD_Frechet_schema",
    ]:
        require(closed[key] is True, f"closed source payload {key}")
    transfer = end0["transfer_boundary"]
    require(transfer["rank2_to_sector_transfer_closed"] is False, "rank2 transfer")
    require(transfer["sector_routing_values_emitted"] is False, "routing values")
    require(transfer["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD")
    require(transfer["validator_ready_sector_payload"] is False, "sector validator")
    require(transfer["source_or_value_emission_required"] is True, "source emission required")
    strict = end0["strict_decision"]
    require(strict["rank2_End0_payload_closed"] is True, "strict rank2")
    require(strict["rank2_to_Huv_or_sector_transfer_closed"] is False, "strict transfer")
    require(strict["promote_to_Higgs_M_source"] is False, "strict M")
    require(strict["promote_to_Huv"] is False, "strict Huv")

    require(huv["status"] == "HUV_TRANSFER_VALUES_NOT_EMITTED", "huv status")
    require(huv["passes"] is False, "huv pass")
    target = huv["locked_Huv_target"]
    require(target["ordered_basis"] == ["H_u", "H_d^dagger"], "Huv basis")
    require(target["reduction_formula"] == "B_Huv^* M_source B_Huv", "Huv formula")
    state = huv["strict_payload_state"]
    for key in ["B_Huv_value_emitted", "M_source_value_emitted", "direct_Huv_entries_emitted"]:
        require(state[key] is False, f"Huv emitted {key}")
    for key in ["Huu", "Hud", "Hdd", "Delta", "Omega", "s_beta", "lambda_H"]:
        require(state[key] is None, f"Huv value emitted {key}")
    require_all_true(huv["why_diagonal_payload_does_not_close_Huv"], "why not Huv")
    require_all_true(huv["guardrail"], "guardrail")

    require(retirement["status"] == "DIAGONAL_HYM_BRANCH_RETIRED_AS_BLOCKER_TRANSFER_GATE_ACTIVE", "retirement status")
    require_all_true(retirement["retired_blockers"], "retired blockers")
    require_all_true(retirement["active_blockers"], "active blockers")
    require(len(retirement["non_cycles"]) == 4, "non-cycle list")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1P_END0_TO_HUV_OR_SECTOR_ROUTING", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING"), "next label")
    require(len(next_work["legal_exits"]) == 3, "legal exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "not single path")
    require(strategy["locked_target"] == "Huv two-Higgs mass-strain payload, not measured Higgs data", "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_diagonal_HYM_first_solve_closed"] is True, "cert diagonal")
    require(cert["rank2_End0_payload_closed"] is True, "cert End0")
    require(cert["full_diagonal_End0_green_closed"] is True, "cert Green")
    require(cert["row_model_offdiagonal_Ext_control_closed"] is True, "cert offdiag")
    require(cert["rank2_to_Huv_or_sector_transfer_closed"] is False, "cert transfer")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("rank2-to-Huv/sector transfer closed            False" in note, "note transfer")
    require("H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING" in note, "note next")

    print("CONST-HIGGS-01 H7B1O diagonal HYM payload to Huv transfer gate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
