"""Audit the dynamic Higgs response Hessian on B_Huv attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DOMAIN_GATE = PACKET_DIR / "dynamic_hessian_domain_and_extraction_gate.packet.json"
VALUE_SEARCH = PACKET_DIR / "direct_mh_value_search_after_domain_closure.packet.json"
DIAGONAL_REJECTION = PACKET_DIR / "diagonal_hym_t3_candidate_rejection.packet.json"
STRICT_TABLE = PACKET_DIR / "strict_mh_table_value_gate.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_dynamic_hessian_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_hessian_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicHiggsResponseHessianOnBHuv_or_DirectMHValueEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_DYNAMICHIGGSRESPONSEHESSIANONBHUV_OR_DIRECTMHVALUEEMISSION_"
    "DOMAIN_EXTRACTION_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_HiggsSecondVariationFunctionalSource_or_Herm2RowValues_v1"


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
    domain = load(DOMAIN_GATE)
    search = load(VALUE_SEARCH)
    diagonal = load(DIAGONAL_REJECTION)
    strict = load(STRICT_TABLE)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("domain gate", domain),
        ("value search", search),
        ("diagonal rejection", diagonal),
        ("strict table", strict),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "selected_H_sector_restriction_R_H_emitted",
        "selected_H_projector_P_H_emitted",
        "dynamic_Hessian_domain_on_BHuv_closed",
        "Herm2_value_extraction_law_closed",
        "direct_value_attempts_rechecked_after_domain_closure",
        "diagonal_HYM_T3_candidate_tested",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "diagonal_HYM_T3_candidate_promoted_as_M_H",
        "selected_F_H_second_variation_emitted",
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_H_response_table_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(domain["status"] == "BHUV_RH_DOMAIN_AND_HERM2_EXTRACTION_LAW_CLOSED", "domain status")
    selected_domain = domain["selected_domain"]
    require(selected_domain["source_space"]["basis_dimension"] == 27, "source dimension")
    require(selected_domain["source_space"]["branch"]["q"] == 79, "source q")
    require(selected_domain["source_space"]["branch"]["orientation"] == "F", "source orientation")
    require(selected_domain["R_H"] == "R_H(x) = B_Huv^* G_Q x", "R_H formula")
    require(selected_domain["P_H"] == "P_H = B_Huv R_H = B_Huv B_Huv^* G_Q", "P_H formula")
    for key in ["R_H_B_Huv_equals_I2", "P_H_squared_equals_P_H", "P_H_G_self_adjoint"]:
        require(selected_domain[key] is True, f"domain identity missing {key}")
    value_rule = domain["dynamic_value_rule"]
    require(value_rule["functional_name"] == "F_H", "functional name")
    require("Herm2_hessian" in value_rule, "hessian rule missing")
    require("M_H = B_Huv^* M_source B_Huv" in value_rule["equivalent_full_route"], "full route missing")
    for key, value in domain["what_is_closed_now"].items():
        require(value is True, f"domain closure missing {key}")
    for key, value in domain["what_is_not_closed"].items():
        require(value is True, f"domain open flag missing {key}")

    require(
        search["status"] == "DIRECT_MH_VALUE_SEARCH_AFTER_DOMAIN_CLOSURE_VALUES_NOT_FOUND",
        "search status",
    )
    retired = search["old_blockers_retired_by_current_repo"]
    require(retired["B_Huv_emitted_now"] is True, "B_Huv not retired")
    require(retired["R_H_emitted_now"] is True, "R_H not retired")
    require(retired["P_H_emitted_now"] is True, "P_H not retired")
    attempts = search["direct_value_attempts"]
    for key in [
        "H7B1C_selected_Huu_Hud_Hdd_found",
        "H7B1N_direct_Huv_entries_emitted",
        "H7B1Y_direct_Huu_Hud_Hdd_emitted",
        "H7B1Z_direct_Huu_Hud_Hdd_emitted",
        "H7B1W_direct_Huu_Hud_Hdd_emitted",
        "any_direct_attempt_emits_values",
    ]:
        require(attempts[key] is False, f"search overemitted {key}")
    require(search["rows_all_null"] is True, "rows should be null")
    for key, value in search["current_table_after_recheck"].items():
        require(value is None, f"search row overfilled {key}")
    support = search["positive_support_retained"]
    require(support["H7B1F_basis_invariant_functor_proved"] is True, "H7B1F support missing")
    require(support["H7B1Y_schema_emitted"] is True, "H7B1Y schema missing")
    require(support["current_R_H_closure_plugs_prior_Pi_or_RH_gap"] is True, "R_H update missing")

    require(
        diagonal["status"] == "DIAGONAL_HYM_T3_CANDIDATE_REJECTED_AS_VALUE_SOURCE",
        "diagonal status",
    )
    diag_decision = diagonal["decision"]
    require(diag_decision["promote_T3_as_M_H"] is False, "T3 promoted")
    require(diag_decision["promote_conditional_s_beta_1"] is False, "s_beta promoted")
    require(diag_decision["requires_selected_F_H_or_reduction_theorem"] is True, "F_H requirement missing")
    for key, value in diagonal["rejection_reasons"].items():
        require(value is not False, f"diagonal rejection missing {key}")

    require(strict["status"] == "STRICT_MH_TABLE_VALUES_OPEN_DOMAIN_CLOSED", "strict status")
    for key, value in strict["domain_closed"].items():
        require(value is True, f"strict domain missing {key}")
    for key, value in strict["required_values"].items():
        require(value is None, f"strict value overfilled {key}")
    require(strict["current_packet_passes"] is False, "strict table overclosed")
    require("selected F_H second-variation functional not emitted" in strict["value_closure_reasons_missing"], "F_H missing reason")
    require("promoting the source metric G_Q or connection generator T3 as M_H" in strict["forbidden_shortcuts"], "T3 guard missing")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_DYNAMIC_HESSIAN_DOMAIN_CLOSED_VALUES_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    for key in [
        "dynamic_Hessian_domain_on_BHuv_closed",
        "Herm2_value_extraction_law_closed",
        "diagonal_HYM_T3_candidate_tested",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "diagonal_HYM_T3_candidate_promoted_as_M_H",
        "selected_F_H_second_variation_emitted",
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_H_response_table_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["conditional_consequent_current"]["ten_K_antecedent_satisfied"] is False, "ten-K overclosed")
    require(
        hk_gate["conditional_consequent_current"]["strict_Omega_lambda_scalar_execution_closed"]
        is False,
        "Omega/lambda overclosed",
    )

    require(
        cutset["status"] == "NEXT_FRONTIER_HIGGS_SECOND_VARIATION_FUNCTIONAL_SOURCE_OR_HERM2_ROWS",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "dynamic Higgs Hessian domain on B_Huv fixed",
        "Herm(2) second-variation extraction law fixed",
        "diagonal HYM T3 shortcut tested and rejected as source value",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected finite H-sector action/response functional F_H",
        "selected second variation M_H on B_Huv",
        "direct Huu,Hud,Hdd rows with exactness/source certificates",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "fixed the selected dynamic Higgs Hessian domain",
        "`M_H=B_Huv^* M_source B_Huv`",
        "tested and rejected the diagonal HYM/T3 shortcut",
        "selected finite H-sector functional `F_H`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: dynamic Higgs Hessian domain/extraction is closed; "
        "Herm(2) values remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
