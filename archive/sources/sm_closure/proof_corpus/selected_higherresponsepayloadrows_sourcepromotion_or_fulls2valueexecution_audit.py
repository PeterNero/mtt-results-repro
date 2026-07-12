"""Audit higher-response payload source-promotion / full-S2 execution attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION = PACKET_DIR / "higher_response_payload_source_promotion_attempt.packet.json"
FULLS2 = PACKET_DIR / "full_s2_value_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_payload_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HigherResponsePayloadRows_SourcePromotion_or_FullS2ValueExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSEPAYLOADROWS_SOURCEPROMOTION_OR_FULLS2VALUEEXECUTION_"
    "BUILT_DOTD_RETIRED_OPERATOR_PAYLOAD_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_SelectedHYMOperatorPayloadPromotion_or_RhoEDEFullS2Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    promotion = load(PROMOTION)
    fulls2 = load(FULLS2)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    require(promotion["status"] == "DOTD_ALPHA1_RETIRED_REMAINING_OPERATOR_PAYLOAD_SUPPORT_ONLY", "promotion status mismatch")
    require(promotion["selected_now"] == ["sector_projectors_dotD_alpha1"], "only dotD/alpha1 should promote")
    for row in [
        "HYM_projector_zero_mode_basis_values",
        "Hermitian_metric_and_HYM_connection",
        "D_E_action",
        "rho_E_transition_data",
        "Ext_HYM_Hodge_projector_table",
        "End0_to_sector_functor",
    ]:
        require(row in promotion["support_only_rows"], f"support-only row missing: {row}")
    for key in [
        "same_branch_alpha1_derivative",
        "honest_dotd_validator_replay",
        "visible_routec_operator_source",
    ]:
        require(promotion["closed_now"][key] is True, f"closed-now flag false: {key}")
    require(promotion["not_promoted_now"]["selected_HYM_projector_zero_mode_basis_values"] is True, "HYM overpromoted")
    require(promotion["not_promoted_now"]["selected_D_E_source_promotion"] is True, "D_E overpromoted")
    require(promotion["not_promoted_now"]["selected_rho_E_transition_payload"] is True, "rhoE overpromoted")
    require(promotion["guardrail"]["diagnostic_source_lift_not_counted_as_selected"] is True, "diagnostic guard missing")
    require(promotion["guardrail"]["model_active_values_not_counted_as_selected"] is True, "model-active guard missing")

    ready = fulls2["ready_fields"]
    require(ready["higher_response_Rtheta_contract_closed"] is True, "Rtheta contract missing")
    require(ready["first_response_no_go_preserved"] is True, "first-response no-go missing")
    require(ready["alpha1_dotd_retired"] is True, "alpha1/dotD not retired")
    for key in [
        "selected_HYM_operator_payload_ready",
        "selected_rhoE_DE_operator_payload_ready",
        "selected_End0_sector_functor_ready",
        "scalar_Rtheta_rows_executable_now",
    ]:
        require(ready[key] is False, f"ready field overclosed: {key}")
    require(fulls2["execution_attempted"] is True, "execution not attempted")
    require(fulls2["execution_allowed_now"] is False, "full S2 overallowed")
    require(fulls2["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(len(fulls2["why_blocked"]) == 4, "blocked reason count mismatch")

    require(cutset["recommended_next"]["artifact"] == NEXT_ARTIFACT, "cutset next mismatch")
    for row in [
        "selected_HYM_projector_zero_mode_basis_values",
        "full_sector_HYM_metric_connection_payload",
        "selected_rho_E_D_E_Riesz_Green_payload",
        "selected_End0_to_sector_functor_values",
        "scalar_Rtheta_value_rows_after_operator_payload",
    ]:
        require(row in cutset["minimal_remaining_rows"], f"remaining row missing: {row}")

    closure = data["closure_decision"]
    require(closure["dotD_alpha1_payload_closed"] is True, "dotD/alpha1 closure missing")
    for key in [
        "selected_operator_payload_closed",
        "full_S2_value_execution_closed",
        "higher_response_Rtheta_executed",
        "Yukawa_mass_mixing_value_closure",
        "lambda_H_value_execution",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require(data["what_closes_now"]["full_S2_blocker_reduced_to_selected_operator_payload"] is True, "blocker reduction missing")
    require(data["what_remains_open"]["selected_HYM_projector_zero_mode_basis_values"] is True, "HYM not open")
    require(data["what_remains_open"]["selected_rho_E_D_E_Riesz_Green_payload"] is True, "rhoE/DE not open")
    require(data["closure_claimed"] is False, "candidate should not close")
    require(cert["closure_claimed"] is False, "certificate should not close")

    for packet in [data, promotion, fulls2, cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("same-branch alpha1 derivative" in note, "note closed row missing")
    require("Still open:" in note, "note still-open missing")
    require("diagnostic source-lift" in note, "note diagnostic guard missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
