"""Audit CONST-HIGGS-01 H7B1Q two-Higgs lift or same-source functional gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SAMESOURCE_IMPORT = BASE / "samesource_functional_value_import.packet.json"
HUV_BOUNDARY = BASE / "twohiggs_huv_boundary_after_functional_value.packet.json"
NO_CYCLE = BASE / "source_promotion_non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1Q_TwoHiggsLiftOrSameSourceFunctionalValue_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1Q_SAMESOURCE_FUNCTIONAL_VALUE_CLOSED_TWOHIGGS_HUV_OPEN"


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
    samesource = load(SAMESOURCE_IMPORT)
    huv = load(HUV_BOUNDARY)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("samesource", samesource),
        ("huv", huv),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem")
    require(candidate["H7B1P_imported"] is True, "H7B1P import")
    require(candidate["samesource_functional_exit_closed"] is True, "same-source exit")
    require(candidate["selected_N_alpha1_h_ext_value"] == 1.0, "N alpha1")
    require(candidate["du_dalpha1_equals_h_ext"] is True, "du/dalpha")
    require(candidate["selected_dotD_source_verified"] is True, "dotD")
    require(candidate["alpha1_driver_verified"] is True, "alpha1 driver")
    require(candidate["honest_dotD_validator_closed"] is True, "honest validator")
    require(candidate["selected_matter_operator_blocks_emitted"] is True, "matter operators")
    require(candidate["emitted_operator_blocks"] == ["d", "e", "nuD", "u"], "operator blocks")
    require(candidate["selected_overlap_normalization_emitted"] is True, "overlap")
    for key in [
        "primitive_C1_contractions_closed",
        "lambda_12_computable",
        "UV_twoHiggs_basis_emitted",
        "UV_twoHiggs_Huv_transfer_closed",
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
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1R_HuvSourceOperatorOrPrimitiveC1LambdaBridge_v1",
        "candidate next",
    )

    require(samesource["status"] == "SAMESOURCE_FUNCTIONAL_ALPHA1_DRIVER_CLOSED", "samesource status")
    imported = samesource["imported_chain"]
    for key, value in imported.items():
        if key == "support_candidate_value_N_alpha1_h_ext":
            require(value == 1.0, "samesource support value")
        else:
            require(value is True, f"samesource imported chain expected true: {key}")
    value = samesource["promoted_value"]
    require(value["N_alpha1_h_ext"] == 1.0, "value N")
    require(value["lambda_alpha1"] == 1.0, "value lambda alpha")
    require(value["du_dalpha1"] == "h_ext", "value du")
    require(value["selected_value_emitted_by_this_theorem"] is True, "selected value")
    require(value["tangent_residual_l2"] == 0.0, "residual")
    scope = samesource["operator_blocks_scope"]
    require(scope["emitted_operator_blocks"] == ["d", "e", "nuD", "u"], "scope blocks")
    require(scope["all_blocks_are_matter_or_neutrino"] is True, "matter scope")
    require(scope["has_uv_higgs_blocks"] is False, "Huv scope")
    require(scope["contains_H_u"] is False, "Hu scope")
    require(scope["contains_H_d_dagger"] is False, "Hd scope")
    require(scope["contains_Huv"] is False, "Huv block scope")
    residual = samesource["residual_open_from_import"]
    for key in [
        "primitive_C1_contractions_closed",
        "lambda_12_computable",
    ]:
        require(residual[key] is False, f"residual should stay false {key}")
    for key in [
        "operator_layer_Pic0_or_torsion_gerbe_rule",
        "Yukawa_magnitudes",
        "full_SM_closure",
    ]:
        require(residual[key] is True, f"residual should stay open {key}")
    decision = samesource["decision"]
    require(decision["samesource_functional_exit_closed_for_H7B1Q"] is True, "same decision")
    require(decision["closes_alpha1_driver_and_selected_dotD_side"] is True, "alpha decision")
    require(decision["closes_Higgs_UV_twoHiggs_Huv_side"] is False, "Higgs overclose")

    require(huv["status"] == "SAMESOURCE_FUNCTIONAL_CLOSED_BUT_UV_TWOHIGGS_HUV_STILL_OPEN", "huv status")
    target = huv["locked_Huv_target"]
    require(target["ordered_basis"] == ["H_u", "H_d^dagger"], "target basis")
    require(target["Huv_formula"] == "B_Huv^* M_source B_Huv", "target formula")
    available = huv["available_after_H7B1Q"]
    require(available["same_source_functional_value_closed"] is True, "available same source")
    require(available["selected_dotD_source_verified"] is True, "available dotD")
    require(available["alpha1_driver_verified"] is True, "available driver")
    require(available["selected_overlap_normalization_emitted"] is True, "available overlap")
    require(available["emitted_operator_blocks"] == ["d", "e", "nuD", "u"], "available blocks")
    require_all_false(huv["missing_for_Huv"], "missing for Huv")
    for key, value in huv["strict_payload_state"].items():
        require(value is None, f"Huv strict value emitted {key}")
    huv_decision = huv["decision"]
    require(huv_decision["H7B1Q_closes_one_previous_legal_exit"] is True, "H7B1Q exit")
    require(huv_decision["remaining_gate_is_Higgs_specific"] is True, "remaining gate")
    require(huv_decision["UV_twoHiggs_Huv_transfer_closed"] is False, "Huv transfer")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1Q", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    circ = no_cycle["circulation_test"]
    require(circ["is_reopening_H7B1O"] is False, "reopening O")
    require(circ["is_reopening_H7B1P"] is False, "reopening P")
    require(circ["is_promoting_matter_blocks_as_Huv"] is False, "matter as Huv")
    require(circ["is_promoting_alpha1_value_as_lambda_H"] is False, "alpha as lambda")
    require(len(circ["new_information_added"]) == 5, "new information")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1R_HUV_SOURCE_OPERATOR_OR_PRIMITIVE_C1_LAMBDA_BRIDGE", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    strategy = next_work["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combining")
    require(strategy["using_one_straight_way"] is False, "superset multiple")
    require("not observed Higgs mass" in strategy["locked_target"], "locked target")

    require(cert["status"] == STATUS, "cert status")
    require(cert["samesource_functional_exit_closed"] is True, "cert same source")
    require(cert["selected_N_alpha1_h_ext_value"] == 1.0, "cert N")
    require(cert["alpha1_driver_verified"] is True, "cert alpha")
    require(cert["selected_matter_operator_blocks_emitted"] is True, "cert matter")
    require(cert["UV_twoHiggs_Huv_transfer_closed"] is False, "cert Huv")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("same-source functional exit closed               True" in note, "note same-source")
    require("UV two-Higgs Huv transfer closed                 False" in note, "note Huv")
    require("H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE" in note, "note next")

    print("CONST-HIGGS-01 H7B1Q two-Higgs/functional-value audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
