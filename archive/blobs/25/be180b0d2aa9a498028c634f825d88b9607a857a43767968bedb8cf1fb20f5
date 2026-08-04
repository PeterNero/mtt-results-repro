"""Audit Step69 HYM/threshold prefactor rows / Omega scalar execution frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULA_PACKET = PACKET_DIR / "step69_prefactor_solution_formula_rows.packet.json"
DIAGNOSTIC_PACKET = PACKET_DIR / "step69_diagnostic_prefactor_postcheck.packet.json"
OPERATOR_PACKET = PACKET_DIR / "step69_operator_prefactor_source_audit.packet.json"
GATE_PACKET = PACKET_DIR / "step69_strict_omega_acceptance_gate.packet.json"
CUTSET_PACKET = PACKET_DIR / "step69_next_prefactor_source_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step69_HYMThresholdPrefactorRows_or_OmegaScalarExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP69_PREFACTOR_FORMULA_CONTRACT_BUILT_SOURCE_ROWS_OPEN"
NEXT = "MTT_Selected_PrefactorSourceRowsFromHYMOperatorPayload_or_StrictOmegaAcceptance_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    formula = load(FORMULA_PACKET)
    diagnostic = load(DIAGNOSTIC_PACKET)
    operator = load(OPERATOR_PACKET)
    gate = load(GATE_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, formula, diagnostic, operator, gate, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    rows = formula["formula_rows"]
    require(formula["formula_row_count"] == 10, "formula row count mismatch")
    require(formula["accepted_formula_skeleton_row_count"] == 10, "formula skeleton count mismatch")
    require(formula["unique_prefactor_slot_count"] == 10, "prefactor slot count mismatch")
    require(formula["accepted_prefactor_source_row_count"] == 0, "prefactor rows overaccepted")
    require(formula["accepted_full_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(formula["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(formula["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")

    expected_omega = {
        "Omega_u.gen1",
        "Omega_u.gen2",
        "Omega_u.gen3",
        "Omega_d.gen1",
        "Omega_d.gen2",
        "Omega_d.gen3",
        "Omega_e.gen1",
        "Omega_e.gen2",
        "Omega_e.gen3",
        "Omega_H.lambda",
    }
    require({row["omega_id"] for row in rows} == expected_omega, "Omega row set mismatch")
    require({row["prefactor_slot_id"] for row in rows} == {
        "C_HYMthr.u.gen1",
        "C_HYMthr.u.gen2",
        "C_HYMthr.u.gen3",
        "C_HYMthr.d.gen1",
        "C_HYMthr.d.gen2",
        "C_HYMthr.d.gen3",
        "C_HYMthr.e.gen1",
        "C_HYMthr.e.gen2",
        "C_HYMthr.e.gen3",
        "C_HYMthr.H.lambda",
    }, "prefactor slot set mismatch")

    expected_exponents = {
        "Omega_u.gen1": "2",
        "Omega_u.gen2": "1",
        "Omega_u.gen3": "0",
        "Omega_d.gen1": "2",
        "Omega_d.gen2": "1",
        "Omega_d.gen3": "2/3",
        "Omega_e.gen1": "2",
        "Omega_e.gen2": "1",
        "Omega_e.gen3": "2/3",
        "Omega_H.lambda": "1/3",
    }
    for row in rows:
        require(row["theta_exponent"] == expected_exponents[row["omega_id"]], f"bad exponent {row['omega_id']}")
        require(row["accepted_formula_skeleton"] is True, f"formula skeleton not accepted {row['omega_id']}")
        require(row["prefactor_source_closed"] is False, f"prefactor overclosed {row['omega_id']}")
        require(row["accepted_as_full_omega_source_row"] is False, f"Omega overaccepted {row['omega_id']}")
        require(row["accepted_as_internal_scalar_value"] is False, f"scalar overaccepted {row['omega_id']}")
        require("epsilon_Theta" in row["formula"], f"formula missing epsilon {row['omega_id']}")
        require(row["value_payload"] is None, f"value payload overfilled {row['omega_id']}")

    diagnostic_rows = diagnostic["diagnostic_rows"]
    require(diagnostic["diagnostic_row_count"] == 10, "diagnostic count mismatch")
    require(diagnostic["all_diagnostic_prefactors_finite"] is True, "diagnostic prefactors not finite")
    require(
        diagnostic["all_diagnostic_prefactors_inside_order_one_window_0p1_to_10"] is True,
        "diagnostic prefactors outside order-one window",
    )
    require(diagnostic["accepted_prefactor_source_row_count"] == 0, "diagnostic prefactors overaccepted")
    require(diagnostic["diagnostic_only_not_a_selector"] is True, "diagnostic selector guard missing")
    require(diagnostic["min_abs_diagnostic_prefactor"] > 0.1, "diagnostic min too small")
    require(diagnostic["max_abs_diagnostic_prefactor"] < 10.0, "diagnostic max too large")
    require(math.isfinite(diagnostic["log10_prefactor_span"]), "diagnostic span not finite")
    for row in diagnostic_rows:
        require(row["accepted_as_prefactor_source_row"] is False, f"diagnostic promoted {row['omega_id']}")
        require(row["accepted_as_full_omega_source_row"] is False, f"diagnostic Omega promoted {row['omega_id']}")
        require(row["inside_order_one_window_0p1_to_10"] is True, f"diagnostic not order-one {row['omega_id']}")

    closed_support = operator["closed_support"]
    require(closed_support["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is True, "transition support missing")
    require(closed_support["diagonal_End0_operator_payload_closed"] is True, "diagonal End0 support missing")
    require(closed_support["dotD_alpha1_payload_closed"] is True, "dotD support missing")
    require(closed_support["dynamic_payload_row_inventory_built"] is True, "dynamic inventory missing")
    require(operator["accepted_prefactor_source_row_count"] == 0, "operator prefactor rows overaccepted")
    for key, value in operator["still_open_source_gates"].items():
        require(value is False, f"source gate unexpectedly closed: {key}")

    strict = gate["strict_acceptance_result"]
    require(gate["closed_by_step69"]["ten_prefactor_formula_rows"] is True, "formula rows not closed")
    require(gate["closed_by_step69"]["diagnostic_order_one_postcheck"] is True, "diagnostic postcheck not closed")
    require(strict["accepted_formula_skeleton_row_count"] == 10, "strict formula count mismatch")
    require(strict["accepted_prefactor_source_row_count"] == 0, "strict prefactor rows overaccepted")
    require(strict["accepted_full_omega_source_row_count"] == 0, "strict Omega rows overaccepted")
    require(strict["accepted_internal_scalar_value_row_count"] == 0, "strict scalar rows overaccepted")
    require(strict["value_rows_execute"] is False, "strict values executed early")
    for key in [
        "selected_prefactor_source_rows",
        "selected_higher_response_operator_payload",
        "same_branch_threshold_matching_source_rows",
        "same_branch_mass_scheme_conversion_source_rows",
        "lambda_H_value_row",
    ]:
        require(gate["not_closed_by_step69"][key] is True, f"gate overclosed: {key}")

    for phrase in [
        "selected same-branch finite HYM/threshold prefactor source row for each Omega slot",
        "selected scale/scheme/loop convention attached to those prefactor rows",
        "selected lambda_H prefactor/value row",
        "strict Omega acceptance theorem promoting formula rows to scalar source rows",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing: {phrase}")
    for phrase in [
        "promote diagnostic postcheck prefactors as source rows",
        "use replay values to choose HYM/threshold prefactors",
        "treat formula skeleton rows as accepted scalar rows",
        "import external top/Higgs formula maps as no-knob internal rows",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "prefactor_formula_contract_closed",
        "ten_omega_formula_rows_constructed",
        "unique_prefactor_slots_identified",
        "diagnostic_order_one_prefactor_postcheck_closed",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "hym_threshold_prefactor_rows_closed",
        "selected_higher_response_operator_payload_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "lambda_H_value_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    require(decision["accepted_prefactor_source_row_count"] == 0, "decision prefactor rows overaccepted")
    require(decision["accepted_full_omega_source_row_count"] == 0, "decision Omega rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "decision scalar rows overaccepted")

    for phrase in [
        "formula rows      = 10",
        "prefactor slots   = 10",
        "accepted prefactor source rows = 0",
        "accepted Omega source rows     = 0",
        "accepted scalar values         = 0",
        "Omega_u.gen1",
        "Omega_H.lambda",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
