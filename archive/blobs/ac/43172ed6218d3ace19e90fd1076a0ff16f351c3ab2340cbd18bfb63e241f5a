"""Audit selected HYM operator payload promotion / rhoE-D_E full-S2 execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAYLOAD = PACKET_DIR / "selected_hym_operator_payload_promotion_gate.packet.json"
FULLS2 = PACKET_DIR / "rhoede_full_s2_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hym_operator_payload_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SelectedHYMOperatorPayloadPromotion_or_RhoEDEFullS2Execution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SELECTEDHYMOPERATORPAYLOADPROMOTION_OR_RHOEDEFULLS2EXECUTION_"
    "BUILT_DIAGONAL_END0_CLOSED_PHIFIN_TRACE_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    payload = load(PAYLOAD)
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

    closed = payload["closed_diagonal_payload"]
    for key in [
        "full_expS_diagonal_replay",
        "rank2_metric_connection_payload",
        "End0_D_E_connection_matrices",
        "protected_T3_Riesz_Green",
        "T1_T2_covariant_Green",
        "row_model_offdiagonal_Ext_control",
    ]:
        require(closed[key] is True, f"diagonal payload field false: {key}")

    boundary = payload["promotion_boundary"]
    require(boundary["rank2_End0_payload_closed"] is True, "rank2 payload not closed")
    require(boundary["selected_diagonal_HYM_first_solve_closed"] is True, "first solve not closed")
    for key in [
        "rank2_to_sector_transfer_closed",
        "physical_dotD_alpha1_closed",
        "selected_End0_to_sector_routing_values_extracted",
        "finite_projector_values_promoted_to_selected",
        "PhiFin_selected_trace_emitted",
    ]:
        require(boundary[key] is False, f"promotion boundary overclosed: {key}")

    shortcuts = payload["rejected_shortcuts"]
    for key in [
        "continuous_Ext_scale_as_physical_alpha1",
        "alpha1_tangent_without_source_or_routing_lemma",
        "q79_constants_support_as_sector_routing_values",
        "model_active_projectors_as_selected_Ps_Ks",
    ]:
        require(shortcuts[key] is True, f"shortcut not rejected: {key}")

    ready = fulls2["ready"]
    require(ready["diagonal_End0_payload_ready"] is True, "diagonal End0 not ready")
    require(ready["row_model_offdiagonal_control_ready"] is True, "offdiagonal control not ready")
    for key in [
        "PhiFin_selected_minimizer_trace_ready",
        "selected_projector_promotion_ready",
        "physical_dotD_alpha1_ready",
        "End0_to_sector_routing_ready",
        "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
        "full_S2_scalar_execution_ready",
    ]:
        require(ready[key] is False, f"full S2 overready: {key}")
    require(len(fulls2["blocked_by"]) == 4, "blocked-by count mismatch")

    require(cutset["recommended_next"]["artifact"] == NEXT_ARTIFACT, "cutset next mismatch")
    for row in [
        "Phi_fin_selected_minimizer_trace",
        "selected_P_s_K_s_projector_promotion",
        "selected_rho_s_matrix_values",
        "selected_End0_to_sector_routing_values",
        "physical_dotD_alpha1_same_branch_driver",
        "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
    ]:
        require(row in cutset["minimal_remaining_rows"], f"remaining row missing: {row}")

    closure = data["closure_decision"]
    require(closure["diagonal_End0_operator_payload_closed"] is True, "diagonal payload should close")
    for key in [
        "selected_HYM_sector_payload_closed",
        "rank2_to_sector_transfer_closed",
        "physical_dotD_alpha1_closed",
        "rhoE_DE_fullS2_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require(data["what_closes_now"]["next_phifin_trace_cutset_selected"] is True, "next cutset not selected")
    require(data["what_remains_open"]["Phi_fin_selected_minimizer_trace"] is True, "Phi_fin trace not open")
    require(data["what_remains_open"]["full_S2_value_execution"] is True, "full S2 not open")
    require(data["closure_claimed"] is False, "candidate should not close")
    require(cert["closure_claimed"] is False, "certificate should not close")

    for packet in [data, payload, fulls2, cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("full diagonal End0 HYM payload" in note, "note diagonal closure missing")
    require("Still open:" in note, "note open section missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
