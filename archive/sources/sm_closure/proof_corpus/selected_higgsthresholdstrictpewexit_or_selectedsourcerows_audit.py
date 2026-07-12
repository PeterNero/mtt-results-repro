"""Audit Higgs-threshold / strict-PEW exit reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsthresholdstrictpewexit_or_selectedsourcerows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
HIGGS_STATUS = PACKET_DIR / "higgs_threshold_status_after_finite_hscalar.packet.json"
PEW_STATUS = PACKET_DIR / "strict_pew_directk_status_after_prefactor_packets.packet.json"
DECISION = PACKET_DIR / "higgs_pew_remaining_source_rows_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1.md"

STATUS = (
    "MTT_SELECTED_HIGGSTHRESHOLDSTRICTPEWEXIT_OR_SELECTEDSOURCEROWS_"
    "BUILT_HSCALAR_ZERO_H_KNOB_CLOSED_STRICT_PREFACTOR_OPEN"
)
NEXT = "MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    higgs = load(HIGGS_STATUS)
    pew = load(PEW_STATUS)
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

    require(
        higgs["status"] == "FINITE_HSCALAR_AND_ZERO_H_RADIAL_SOURCE_CLOSED_LAMBDA_PREFACTOR_OPEN",
        "higgs status",
    )
    require(higgs["observed_data_used_as_selector"] is False, "higgs observed selector")
    require(higgs["target_fitting_used"] is False, "higgs target fitting")
    require(higgs["accepted_H_scalar_source_rows"] == 1, "H scalar rows")
    require(higgs["finite_projected_A_N_exactness_available"] is True, "finite exactness")
    require(higgs["H_scalar_functional_on_A_N_closed"] is True, "H scalar closed")
    require(higgs["strict_tau_H_promoted"] is True, "tau_H")
    require(higgs["strict_r_H_promoted"] is True, "r_H")
    require(higgs["selected_H_radial_source_row_emitted"] is True, "H radial")
    require(higgs["selected_R_H_RG_source_emitted"] is True, "R_H_RG")
    require(higgs["H_parameter_count_after_replacement"] == 0, "H parameter count")
    require(higgs["old_H_one_parameter_lane_retired_for_radial_source"] is True, "old lane")
    require(higgs["selected_K_threshold_row_count_now"] == 9, "K row count")
    require(higgs["selected_K_threshold_row_count_required"] == 10, "K required")
    require(higgs["lambda_H_postcheck_passed"] is True, "lambda postcheck")
    require(abs(higgs["lambda_H_postcheck_residual"]) < 1e-12, "lambda residual")
    require(higgs["lambda_H_value_row_emitted_as_strict_no_knob"] is False, "lambda overclosed")
    require(higgs["selected_K_threshold_Omega_H_lambda_emitted"] is False, "K omega overclosed")
    require(higgs["higgs_threshold_rows_closed"] is False, "higgs threshold overclosed")

    require(
        pew["status"] == "STRICT_PEW_DIRECTK_PREFRACTOR_CONTRACTS_LOCKED_ZERO_FINAL_ROWS",
        "PEW status",
    )
    require(pew["observed_data_used_as_selector"] is False, "PEW observed selector")
    require(pew["target_fitting_used"] is False, "PEW target fitting")
    require(pew["accepted_selected_prefactor_source_count"] == 0, "prefactor rows")
    require(pew["accepted_A_EW_source_operator_rows"] == 0, "A_EW rows")
    require(pew["accepted_physical_prefactor_rows"] == 0, "physical prefactor")
    require(pew["accepted_threshold_convention_rows"] == 0, "threshold convention")
    require(pew["aew_required_field_count"] == 7, "AEW required")
    require(pew["aew_required_fields_filled_by_current_packets"] == 2, "AEW filled")
    require(pew["pew_payload_contract_locked"] is True, "payload contract")
    require(pew["pew_source_required_field_count"] == 8, "PEW required")
    require(pew["pew_source_filled_field_count"] == 0, "PEW filled")
    require(pew["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(pew["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(pew["premised_physical_normalization_source_axiom_constructed"] is True, "premised axiom")
    require(pew["premised_direct_K_certificate_constructed"] is True, "premised K")
    require(pew["premised_P_EW_source_rows"] == 1, "premised PEW")
    require(pew["premised_direct_K_threshold_Omega_H_lambda_rows"] == 1, "premised direct K")
    require(pew["premised_selected_K_row_count"] == 10, "premised ten K")
    require(pew["shared_physical_primitive_count_under_axiom"] == 1, "shared primitive")
    require(pew["physical_normalization_axiom_derived"] is False, "axiom overderived")
    require(pew["strict_derivation_route_count"] == 0, "strict derivation")
    require(pew["strict_strominger_threshold_value_rows"] == 0, "Strominger rows")
    require(pew["strict_metrology_unit_source_rows"] == 0, "metrology rows")
    require(pew["strict_PEW_directK_values_closed"] is False, "PEW overclosed")

    require(
        decision["status"] == "HSCALAR_ZERO_H_KNOB_CLOSED_FINAL_PREFRACTOR_SOURCE_ROWS_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_H_scalar_source_rows"] == 1, "decision H scalar")
    require(counts["accepted_H_radial_source_rows"] == 1, "decision H radial")
    require(counts["accepted_selected_R_H_RG_source_rows"] == 1, "decision R_H_RG")
    require(counts["strict_selected_K_threshold_rows_now"] == 9, "decision K now")
    require(counts["strict_selected_K_threshold_rows_required"] == 10, "decision K required")
    require(counts["accepted_strict_lambda_H_value_rows"] == 0, "decision lambda")
    require(counts["accepted_strict_P_EW_source_rows"] == 0, "decision PEW")
    require(counts["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "decision direct K")
    require(counts["premised_P_EW_source_rows"] == 1, "decision premised PEW")
    require(counts["premised_direct_K_threshold_Omega_H_lambda_rows"] == 1, "decision premised K")
    acceptance = decision["acceptance"]
    require(acceptance["finite_H_scalar_source_closed"] is True, "accept H scalar")
    require(acceptance["H_radial_zero_parameter_replacement_closed"] is True, "accept H radial")
    require(acceptance["selected_R_H_RG_source_emitted"] is True, "accept R_H_RG")
    require(acceptance["lambda_H_postcheck_passed"] is True, "accept lambda postcheck")
    require(acceptance["strict_lambda_H_value_row_closed"] is False, "lambda overclosed")
    require(acceptance["strict_K_threshold_Omega_H_lambda_closed"] is False, "K overclosed")
    require(acceptance["premised_one_shared_primitive_ten_K_lane_closed"] is True, "premised lane")
    require(acceptance["physical_normalization_axiom_derived"] is False, "axiom overclosed")
    require(acceptance["strict_PEW_directK_values_closed"] is False, "PEW overclosed")
    require(acceptance["higgs_threshold_rows_closed"] is False, "Higgs overclosed")
    require(acceptance["fullS2_no_proxy_rows_closed"] is False, "fullS2 overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(
        data["theorem"]["name"] == "HiggsThresholdStrictPEWExitOrSelectedSourceRowsReductionTheorem",
        "theorem name",
    )
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_H_scalar_source_rows"] == 1, "key H scalar")
    require(key["H_parameter_count_after_replacement"] == 0, "key H parameter")
    require(key["selected_K_threshold_row_count_now"] == 9, "key K now")
    require(key["selected_K_threshold_row_count_required"] == 10, "key K required")
    require(abs(key["lambda_H_postcheck_residual"]) < 1e-12, "key lambda")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key direct K")
    require(key["premised_selected_K_row_count"] == 10, "key premised")
    require(key["shared_physical_primitive_count_under_axiom"] == 1, "key primitive")

    require(cert["finite_H_scalar_source_closed"] is True, "cert H scalar")
    require(cert["H_radial_zero_parameter_replacement_closed"] is True, "cert H radial")
    require(cert["selected_R_H_RG_source_emitted"] is True, "cert R_H_RG")
    require(cert["strict_lambda_H_value_row_closed"] is False, "cert lambda")
    require(cert["strict_K_threshold_Omega_H_lambda_closed"] is False, "cert K")
    require(cert["premised_one_shared_primitive_ten_K_lane_closed"] is True, "cert premised")
    require(cert["physical_normalization_axiom_derived"] is False, "cert axiom")
    require(cert["accepted_strict_P_EW_source_rows"] == 0, "cert PEW")
    require(cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "cert direct K")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "finite H scalar source rows: `1`",
        "strict selected K-threshold rows before final prefactor: `9/10`",
        "strict `lambda_H` value row: `0`",
        "physical-normalization axiom derivation: open",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
