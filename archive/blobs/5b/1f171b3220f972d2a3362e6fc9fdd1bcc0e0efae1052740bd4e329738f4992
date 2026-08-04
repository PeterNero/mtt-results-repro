"""Audit the M_H three-row source-functional contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL = PACKET_DIR / "mh_three_row_source_functional_contract.packet.json"
EXECUTION_TABLE = PACKET_DIR / "mh_three_row_execution_table_request.packet.json"
C5C6 = PACKET_DIR / "c5c6_bridge_execution_contract.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_three_row_functional.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_three_row_functional.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MHThreeRowSourceFunctional_or_C5C6BridgeExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_MHTHREEROWSOURCEFUNCTIONAL_OR_C5C6BRIDGEEXECUTION_"
    "ROW_FUNCTIONAL_CLOSED_SOURCE_TABLE_OPEN"
)
NEXT = "MTT_Selected_HResponseHessianTable_or_C5C6BridgeProof_v1"


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
    functional = load(FUNCTIONAL)
    table = load(EXECUTION_TABLE)
    c5c6 = load(C5C6)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("functional", functional),
        ("execution table", table),
        ("C5C6", c5c6),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(cert["theorem_proved"] is True, "cert theorem proved")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "M_H_acceptance_object_bound_to_B_Huv_domain",
        "MH_three_row_source_functional_contract_closed",
        "C5C6_bridge_execution_contract_closed",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "MH_three_row_execution_table_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "C5C6_bridge_payload_emitted",
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

    require(functional["domain"]["orthonormality"] == "B_Huv^* G_Q B_Huv = I_2", "domain")
    require(functional["extraction_self_test"]["passes"] is True, "extraction self-test")
    extracted = functional["extraction_self_test"]["extracted"]
    require(extracted == {"Delta": 3.0, "Im_Omega": 5.0, "Re_Omega": -2.0}, "extracted rows")
    require(functional["row_basis"]["Delta"]["functional"] == "Delta = (1/2) Tr(H_tf sigma_z)", "Delta functional")
    require(
        functional["row_basis"]["Re_Omega"]["functional"]
        == "Re(Omega) = (1/2) Tr(H_tf sigma_x)",
        "Re functional",
    )
    require("sigma_y^MTT" in functional["row_basis"]["Im_Omega"]["functional"], "Im functional")
    for key in ["Delta", "Re_Omega", "Im_Omega", "Huu", "Hud", "Hdd", "P_L", "s_beta"]:
        require(functional["values_emitted"][key] is None, f"{key} overemitted")

    pred = functional["acceptance_predicate"]
    for key in ["same_branch", "source_owned", "exactness", "Hermitian", "non_scalar", "light_line", "no_target_fit"]:
        require(key in pred, f"acceptance predicate missing {key}")

    minimal = table["minimal_table"]
    for key in [
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "Hdu_equals_conj_Hud_certificate",
        "same_source_exactness_or_error_certificate",
        "source_ownership_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(minimal[key] is None, f"table overfilled {key}")
    current = table["current_sources_do_not_fill_table"]
    require(current["H7B1C_values_currently_emitted"] is False, "H7B1C values")
    require(current["H7B1C_search_selected_Huu_Hud_Hdd_found"] is False, "H7B1C search")
    require(current["H7B1J_dynamic_exported"] is False, "H7B1J export")
    require(current["current_underdetermination_closed"] is True, "underdetermination import")

    require(c5c6["bridge_name"] == "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem", "bridge name")
    for phrase in [
        "trace-to-H7B1U grid identity for the diagonal HYM replay",
        "Higgs projection/reduction measure equals normalized finite trace",
        "same-source E_H^UV metric binding to the selected finite basis",
    ]:
        require(phrase in c5c6["C5_required"], f"C5 missing {phrase}")
    for phrase in [
        "no-extra-boundary/source proof",
        "proof no boundary or gauge convention term selects the H row",
    ]:
        require(phrase in c5c6["C6_required"], f"C6 missing {phrase}")
    for key in [
        "trace_to_H7B1U_grid_identity",
        "projection_measure_equality",
        "no_extra_boundary_source",
        "K_threshold_Omega_H_lambda",
    ]:
        require(c5c6["values_emitted_by_bridge_now"][key] is False, f"bridge overemitted {key}")

    h_row = hk_gate["H_row"]
    require(h_row["three_row_source_functional_contract_closed"] is True, "H row functional")
    require(h_row["C5C6_bridge_execution_contract_closed"] is True, "H row C5C6")
    for key in [
        "selected_H_response_table_emitted",
        "C5C6_bridge_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")

    for phrase in [
        "Pauli/Riesz extraction functional for Delta, Re(Omega), Im(Omega)",
        "minimal H_response/Huv table request fixed",
        "C5-C6 bridge execution contract fixed",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H_response Hessian table Huu,Hud,Hdd",
        "or full same-source M_source plus H-sector restriction R_H",
        "or C5 trace-to-H7B1U/projection-measure proof",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "Pauli/Riesz extraction functional",
        "selected `H_response`/`Huv` table values `Huu,Hud,Hdd`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: M_H three-row source functional is closed; "
        "selected H_response table or C5-C6 proof remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
