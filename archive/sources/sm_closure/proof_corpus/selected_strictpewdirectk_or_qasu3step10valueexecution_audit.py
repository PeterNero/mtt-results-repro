"""Audit strict-PEW / QaSU3 Step10 value-execution reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewdirectk_or_qasu3step10valueexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STEP10 = PACKET_DIR / "qasu3_step10_reduction.packet.json"
PEW = PACKET_DIR / "strict_pew_directk_reduction.packet.json"
DECISION = PACKET_DIR / "post_step10_blocker_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1.md"

STATUS = "MTT_SELECTED_STRICTPEWDIRECTK_OR_QASU3STEP10VALUEEXECUTION_BUILT_STEP10_CLOSED_FULLS2_AND_PEW_OPEN"
NEXT = "MTT_Selected_FullS2NoProxyRows_or_StrictPEWNormalizationPayload_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    step10 = load(STEP10)
    pew = load(PEW)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(step10["status"] == "STEP10_ROUTE_A_AND_FIRST_DYNAMIC_ROWS_CLOSED_FULLS2_OPEN", "step10 status")
    require(step10["observed_data_used_as_selector"] is False, "step10 observed selector")
    require(step10["target_fitting_used"] is False, "step10 target fitting")
    require(step10["route_A_source_rule_closed"] is True, "route A not closed")
    require(step10["step10_dynamic_phi_fin_c1_payload_emitted"] is True, "payload not emitted")
    require(step10["contract_outputs_closed"]["A_selected"] is True, "A_selected")
    require(step10["contract_outputs_closed"]["b_selected"] is True, "b_selected")
    require(step10["contract_outputs_closed"]["deltaTheta_C1"] is True, "deltaTheta")
    require(step10["contract_outputs_closed"]["sector_response_matrices"] is True, "sector matrices")
    require(step10["contract_outputs_not_closed"]["full_S2_value_rows"] is True, "full S2 should remain open")
    require(
        step10["contract_outputs_not_closed"]["Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting"]
        is True,
        "no-proxy values should remain open",
    )
    require(step10["accepted_first_dynamic_value_rows"] == 2, "first dynamic rows")
    require(
        step10["accepted_first_dynamic_row_ids"]
        == [
            "VSD-01.phase.I_plus_Z.u.first_dynamic_row",
            "VSD-01.phase.I_plus_Z.e.first_dynamic_row",
        ],
        "row ids",
    )
    require(len(step10["what_remains"]) == 5, "remaining payload count")

    require(pew["status"] == "STRICT_PEW_DIRECTK_ATTEMPT_EXECUTED_ZERO_ROWS", "PEW status")
    require(pew["observed_data_used_as_selector"] is False, "PEW observed selector")
    require(pew["target_fitting_used"] is False, "PEW target fitting")
    require(pew["strict_P_EW_source_rows"] == 0, "PEW rows overaccepted")
    require(pew["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows overaccepted")
    require(pew["strict_P_EW_source_theorem_closed"] is False, "PEW theorem overclosed")
    require(pew["direct_K_threshold_Omega_H_lambda_closed"] is False, "direct K overclosed")
    require(pew["finite_H_radial_source_closed"] is True, "finite H radial")
    require(pew["minimal_one_primitive_lane_closed"] is True, "one primitive lane")

    require(decision["status"] == "STEP10_SOURCE_RULE_CLOSED_FULLS2_NOPROXY_AND_STRICT_PEW_OPEN", "decision")
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_step10_route_A_source_rules"] == 1, "route A count")
    require(counts["accepted_step10_dynamic_payloads"] == 1, "payload count")
    require(counts["accepted_first_dynamic_value_rows"] == 2, "first row count")
    require(counts["accepted_strict_P_EW_source_rows"] == 0, "PEW row count")
    require(counts["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K count")
    acceptance = decision["acceptance"]
    require(acceptance["step10_route_A_source_rule_closed"] is True, "accept route A")
    require(acceptance["step10_dynamic_payload_emitted"] is True, "accept payload")
    require(acceptance["first_dynamic_value_rows_accepted"] is True, "accept first rows")
    require(
        acceptance["qasu3_step10_blocker_reduced_to_fullS2_no_proxy_rows"] is True,
        "Step10 not reduced",
    )
    require(acceptance["strict_P_EW_directK_rows_closed"] is False, "PEW overclosed")
    require(acceptance["full_S2_value_rows_closed"] is False, "full S2 overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "StrictPEWDirectKOrQaSU3Step10ValueExecutionReductionTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_first_dynamic_value_rows"] == 2, "key first rows")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key direct K")
    require(key["fullS2_required_obligation_rows"] == 5, "key fullS2 required")
    require(key["fullS2_closed_value_source_obligation_rows_after"] == 1, "key fullS2 closed")

    require(cert["step10_route_A_source_rule_closed"] is True, "cert route A")
    require(cert["step10_dynamic_payload_emitted"] is True, "cert payload")
    require(cert["accepted_first_dynamic_value_rows"] == 2, "cert first rows")
    require(cert["qasu3_step10_blocker_reduced_to_fullS2_no_proxy_rows"] is True, "cert Step10")
    require(cert["accepted_strict_P_EW_source_rows"] == 0, "cert PEW")
    require(cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "cert direct K")
    require(cert["full_S2_value_rows_closed"] is False, "cert full S2")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")

    for phrase in [
        "Route A selected physical `Phi_fin^C1` source rule: closed",
        "first selected dynamic value rows",
        "strict `P_EW` / direct-K side remains at zero rows",
        "Full S2/no-proxy rows are also still open",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
