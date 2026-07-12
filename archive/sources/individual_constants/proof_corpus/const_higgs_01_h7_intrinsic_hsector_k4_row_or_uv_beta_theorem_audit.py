"""Audit CONST-HIGGS-01 H7 intrinsic K4 row or UV beta theorem frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7_intrinsic_hsector_k4_row_or_uv_beta_theorem"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
K4_AUDIT = BASE / "intrinsic_k4_row_source_payload_audit.packet.json"
UV_BETA_AUDIT = BASE / "uv_beta_theorem_source_payload_audit.packet.json"
VALIDATOR = BASE / "strict_higgs_closure_acceptance_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7_IntrinsicHSectorK4RowOrUVBetaTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7_STRICT_SOURCE_FRONTIER_BUILT_TWO_EXITS_OPEN"


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
    k4 = load(K4_AUDIT)
    uv = load(UV_BETA_AUDIT)
    validator = load(VALIDATOR)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("k4", k4),
        ("uv", uv),
        ("validator", validator),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["strict_two_exit_frontier_built"] is True, "frontier")
    require(candidate["route_A_intrinsic_K4_exit_closed"] is False, "route A overclosed")
    require(candidate["route_B_UV_beta_exit_closed"] is False, "route B overclosed")
    require(candidate["one_primitive_declared_now"] is False, "primitive declared")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    closed = k4["closed_support"]
    require(closed["selected_Higgs_zero_mode_coordinate_closed"] is True, "H coord")
    require(closed["selected_Higgs_amplitude_coordinate"] == 12, "H index")
    require(closed["quartic_row_address"] == [12, 12, 12, 12], "row address")
    require(closed["projection_template_closed"] is True, "projection")
    require(closed["local_row_owner_contract_ready"] is True, "row owner")
    required = k4["required_strict_payload"]
    for key, item in required.items():
        require(item["filled"] is False, f"K4 required {key} overfilled")
    neg = k4["current_negative_result"]
    require(neg["actual_H_sector_fourth_variation_row_found"] is False, "K4 row found")
    require(neg["exact_multilinear_formula_found"] is False, "K4 formula")
    require(neg["row_exactness_certificate_found"] is False, "K4 exactness")
    require(neg["lambda_H_coefficient_convention_from_source_row_found"] is False, "K4 convention")
    require(neg["intrinsic_K4_exit_closed"] is False, "K4 exit")

    uv_support = uv["closed_support"]
    require(uv_support["low_energy_single_Higgs_projection_closed"] is True, "UV single Higgs")
    require(uv_support["Dterm_boundary_formula_ready"] is True, "UV formula")
    require(uv_support["symbolic_boundary_replay_functor_defined"] is True, "UV replay")
    require(uv_support["tree_boundary"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "UV tree")
    for key, item in uv["required_strict_payload"].items():
        require(item["filled"] is False, f"UV required {key} overfilled")
        require(item["must_be_selected_before_Higgs_comparison"] is True, f"UV required {key} timing")
    uv_neg = uv["current_negative_result"]
    require(uv_neg["selected_UV_beta_source_found"] is False, "UV beta")
    require(uv_neg["beta_primitive_declared_now"] is False, "UV primitive")
    require(uv_neg["UV_beta_exit_closed"] is False, "UV exit")

    eval_ = validator["current_packet_evaluation"]
    require(eval_["route_A_intrinsic_K4_passes"] is False, "validator A")
    require(eval_["route_B_UV_Dterm_beta_passes"] is False, "validator B")
    require(eval_["one_primitive_declared_now"] is False, "validator primitive")
    require(eval_["strict_no_knob_Higgs_closure"] is False, "validator no-knob")
    require(eval_["numeric_lambda_H_derived"] is False, "validator lambda")
    require("same_source_H_sector_fourth_variation_row" in validator["acceptance_rule"]["route_A_intrinsic_K4"], "validator A fields")
    require("selected_UV_two_Higgs_VEV_ratio_or_beta" in validator["acceptance_rule"]["route_B_UV_Dterm_beta"], "validator B fields")
    require("not strict no-knob" in validator["acceptance_rule"]["one_primitive_portfolio_route"], "validator primitive tier")

    require("H7A-INTRINSIC-K4-ROW-EXECUTION-PAYLOAD" in next_work["route_A_next"]["label"], "next A")
    require("H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM" in next_work["route_B_next"]["label"], "next B")
    require(cert["status"] == STATUS, "cert status")
    require(cert["strict_two_exit_frontier_built"] is True, "cert frontier")
    require(cert["route_A_intrinsic_K4_exit_closed"] is False, "cert A")
    require(cert["route_B_UV_beta_exit_closed"] is False, "cert B")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H7-INTRINSIC-H-SECTOR" in note and "K_H^(4)[12,12,12,12]" in note, "note")

    print("CONST-HIGGS-01 H7 intrinsic K4 row / UV beta frontier audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
