"""Audit the M_H value-emission search and C5-C6 frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_mhvalueemissionsearch_or_c5c6bridgefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVENTORY = PACKET_DIR / "mh_value_source_inventory.packet.json"
UNDERDET = PACKET_DIR / "herm2_underdetermination_no_promotion.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_mh_value_search.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_mh_value_search.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MHValueEmissionSearch_or_C5C6BridgeFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_MHVALUEEMISSIONSEARCH_OR_C5C6BRIDGEFRONTIER_"
    "NO_SELECTED_ROWS_FOUND_FUNCTIONAL_REQUIRED"
)
NEXT = "MTT_Selected_MHThreeRowSourceFunctional_or_C5C6BridgeExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    inventory = load(INVENTORY)
    underdet = load(UNDERDET)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("inventory", inventory),
        ("underdetermination", underdet),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem proved")
    require(cert["theorem_proved"] is True, "cert theorem proved")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "M_H_acceptance_object_bound_to_B_Huv_domain",
        "current_Higgs_value_source_inventory_checked",
        "Herm2_three_row_underdetermination_closed",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "M_H_three_real_value_rows_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K selected count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    domain = inventory["current_closed_domain"]
    require(domain["B_Huv_two_column_lift"] is True, "B_Huv domain")
    require(domain["M_H_acceptance_object_bound_to_B_Huv_domain"] is True, "M_H object")
    require(domain["required_rows"] == ["Delta", "Re(Omega)", "Im(Omega)"], "required rows")
    require(inventory["accepted_source_row_count"] == 0, "inventory accepted rows")
    require(inventory["direct_value_slots_all_null"] is True, "value slots null")
    for key in ["Delta", "Re_Omega", "Im_Omega", "Huu", "Hud", "Hdd", "P_L", "s_beta"]:
        require(inventory["source_rows_found"][key] is None, f"{key} should not be found")
    for key in [
        "H7B1Y_B_Huv_false_is_retired_by_current_B_Huv",
        "H7B1Z_B_Huv_false_is_retired_by_current_B_Huv",
    ]:
        require(inventory["retired_old_gaps"][key] is True, f"old gap not retired {key}")
    for key in [
        "H7B1Y_Herm2_values_null",
        "H7B1Z_Herm2_values_null",
        "H7B1C_is_request_not_value_packet",
        "H7B1F_is_reduction_formula_not_value_packet",
    ]:
        require(inventory["still_true_after_retiring_old_gaps"][key] is True, f"inventory {key}")

    require(underdet["theorem"]["proved"] is True, "underdetermination theorem")
    require(
        underdet["admissible_family"]["nondegenerate_iff"]
        == "Delta^2 + Re(Omega)^2 + Im(Omega)^2 > 0",
        "nondegenerate condition",
    )
    require(
        underdet["admissible_family"]["s_beta_if_values_exist"]
        == "Delta^2/(Delta^2+Re(Omega)^2+Im(Omega)^2)",
        "s_beta condition",
    )
    for phrase in [
        "B_Huv source-orthonormality",
        "diagonal HYM metric Gram data",
        "matter/neutrino alpha1/dotD operator blocks",
        "diagnostic replay s_beta or observed Higgs data",
    ]:
        require(phrase in underdet["not_enough_to_select_values"], f"missing no-promotion guard {phrase}")
    require("only blocks promotion" in underdet["this_is_not_a_global_MTT_nogo"], "nogo scope")

    h_row = hk_gate["H_row"]
    require(h_row["M_H_value_source_inventory_checked"] is True, "H row inventory")
    require(h_row["Herm2_three_row_underdetermination_closed"] is True, "H row underdet")
    for key in [
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H gate K selected")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H gate K required")

    for phrase in [
        "current Higgs value-source inventory checked",
        "Herm(2) three-row underdetermination theorem recorded",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset missing {phrase}")
    for phrase in [
        "selected Hessian/value functional emitting Delta, Re(Omega), Im(Omega)",
        "or full same-source M_source plus H-sector restriction R_H",
        "or selected C5 trace-to-H7B1U/projection-measure equality",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "actual value slots remain null",
        "local underdetermination theorem",
        "selected Hessian/value functional",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: M_H value inventory found zero selected rows; "
        "three-row functional or C5-C6 bridge is required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
