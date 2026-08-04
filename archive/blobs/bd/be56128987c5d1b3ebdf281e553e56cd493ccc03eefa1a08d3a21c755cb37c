"""Audit CONST-HIGGS-01 H7B1P End0-to-Huv or sector-routing gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1p_end0_to_huv_or_sector_routing"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SECTOR_IMPORT = BASE / "sector_routing_import.packet.json"
HUV_BOUNDARY = BASE / "huv_boundary_after_sector_routing.packet.json"
DOTD_FRONTIER = BASE / "dotd_driver_and_samesource_frontier.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1P_End0ToHuvOrSectorRouting_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1P_SECTOR_ROUTING_IMPORTED_HUV_TWOHIGGS_LIFT_OPEN"


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
    sector = load(SECTOR_IMPORT)
    huv = load(HUV_BOUNDARY)
    dotd = load(DOTD_FRONTIER)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("sector", sector),
        ("huv", huv),
        ("dotd", dotd),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem")
    require(candidate["H7B1O_imported"] is True, "H7B1O import")
    require(candidate["sector_chain_support_closed"] is True, "sector chain")
    require(candidate["functional_projector_payload_closed"] is True, "functional payload")
    require(candidate["symbolic_transport_replay_closed"] is True, "transport")
    require(candidate["dotD_transport_derivative_closed"] is True, "dotD")
    require(candidate["collapsed_H_only"] is True, "collapsed H")
    for key in [
        "UV_twoHiggs_Huv_transfer_closed",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "alpha1_source_strength_value_emitted",
        "same_source_selected_emission_closed",
        "selected_matter_slot_routing_closed",
        "selected_1M_Dirac_rule_closed",
        "selected_transfer_normalization_closed",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1Q_TwoHiggsLiftOrSameSourceFunctionalValue_v1",
        "candidate next",
    )

    require(sector["status"] == "QA_SU3_SECTOR_ROUTING_SUPPORT_IMPORTED_SELECTED_PAYLOAD_OPEN", "sector status")
    closed = sector["closed_support"]
    require_all_true(closed, "sector closed support")
    open_flags = sector["selected_payload_open"]
    require_all_false(open_flags, "sector selected payload")
    require(sector["sector_chain_support_closed"] is True, "sector support flag")
    require(sector["selected_payload_still_open"] is True, "sector open flag")

    require(huv["status"] == "SECTOR_ROUTING_REACHES_COLLAPSED_H_NOT_UV_TWOHIGGS_HUV", "huv status")
    target = huv["locked_Huv_target"]
    require(target["ordered_basis"] == ["H_u", "H_d^dagger"], "Huv basis")
    require(target["Huv_formula"] == "B_Huv^* M_source B_Huv", "Huv formula")
    available = huv["sector_output_available"]
    require(available["contains_collapsed_H"] is True, "collapsed H available")
    require(available["contains_H_u"] is False, "Hu not available")
    require(available["contains_H_d_dagger"] is False, "Hd not available")
    require(available["H_sector_rank"] == 1, "H rank")
    require(available["H_sector_zero_response"] is True, "H zero")
    decision = huv["decision"]
    require(decision["collapsed_H_only"] is True, "Huv collapsed")
    require(decision["End0_to_sector_support_can_be_used_for_SM_sector_packet"] is True, "sector usable")
    for key in [
        "End0_to_sector_support_can_close_UV_Huv",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "Omega_emitted",
        "s_beta_emitted",
        "lambda_H_emitted",
    ]:
        require(decision[key] is False, f"Huv overclosed {key}")
    for key, value in huv["strict_payload_state"].items():
        require(value is None, f"Huv strict value emitted {key}")

    require(dotd["status"] == "DOTD_TRANSPORT_CLOSED_ALPHA1_SOURCE_STRENGTH_VALUE_OPEN", "dotd status")
    dotd_frontier = dotd["dotD_frontier"]
    require(dotd_frontier["transport_derivative_formula_closed"] is True, "dotd derivative")
    require(dotd_frontier["selected_dotD_source_formula_closed"] is True, "dotd formula")
    require(dotd_frontier["selected_dotD_source_verified_by_transport_derivative"] is True, "dotd source algebra")
    require(dotd_frontier["dotD_matrices_pass_if_driver_theorem_supplied"] is True, "dotd matrices")
    require(dotd_frontier["source_only_fails_only_by_alpha1_driver"] is True, "dotd fail reason")
    require(dotd_frontier["alpha1_driver_verified_now"] is False, "alpha1 driver overclosed")
    source = dotd["source_strength_frontier"]
    require(source["source_strength_equivalence_theorem_proved"] is True, "source theorem")
    require(source["necessary_and_sufficient_for_dotD_closure"] is True, "source iff")
    require(source["current_source_value_no_go_proved"] is True, "source no-go")
    require(source["du_dalpha1_equals_h_ext_emitted"] is False, "du/dalpha")
    require(source["normalization_value_emitted_now"] is False, "normalization")
    same = dotd["same_source_frontier"]
    require(same["support_present"] == same["required"] == 7, "support count")
    require(same["selected_emitted"] == 0, "selected emitted")
    require(same["same_source"] == 0, "same source")
    require(same["theorem_derived"] == 0, "theorem derived")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1P", "no-cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1O"] is False, "circling H7B1O")
    require(circ["is_promoting_support_as_selected_values"] is False, "promoting support")
    require(len(circ["new_information_added"]) == 7, "new info")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1Q_TWOHIGGS_LIFT_OR_SAMESOURCE_FUNCTIONAL_VALUE", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multiple")

    require(cert["status"] == STATUS, "cert status")
    require(cert["sector_chain_support_closed"] is True, "cert sector")
    require(cert["collapsed_H_only"] is True, "cert collapsed")
    require(cert["UV_twoHiggs_Huv_transfer_closed"] is False, "cert Huv")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("UV two-Higgs Huv transfer closed                 False" in note, "note Huv")
    require("H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE" in note, "note next")

    print("CONST-HIGGS-01 H7B1P End0-to-Huv/sector-routing audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
