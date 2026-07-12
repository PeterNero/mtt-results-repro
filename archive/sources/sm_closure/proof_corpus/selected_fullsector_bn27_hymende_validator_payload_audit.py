"""Audit full-sector BN27 HYM/End(E) validator payload attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_fullsector_bn27_hymende_validator_payload.py"

SLUG = "selected_fullsector_bn27_hymende_validator_payload"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1.md"
MODEL_PACKET = PACKET_DIR / "model_active_fullsector_payload_replay.packet.json"
PROMOTION_PACKET = PACKET_DIR / "selected_source_promotion_gate_for_bn27_hymende.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_final_row_validator_replay.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hym_projector_sourcepromotion_or_fullstrominger_operator_value.packet.json"

STATUS = "MTT_SELECTED_FULLSECTOR_BN27_HYMENDE_VALIDATOR_PAYLOAD_MODEL_ACTIVE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    model = load(MODEL_PACKET)
    promotion = load(PROMOTION_PACKET)
    gate = load(GATE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, model, promotion, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["model_active_payload_present"] is True, "model payload missing")
    require(decision["model_active_support_count"] >= 14, "model support count too small")
    require(decision["selected_source_blocker_count"] == 10, "selected blocker count drift")
    require(decision["selected_source_promotion_closed"] is False, "selected source overclosed")
    require(decision["BN27_final_row_accepted"] is False, "BN27 final row overaccepted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane count")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    model_closed = model["model_active_closed"]
    for key in [
        "finite_D_E_matrix_on_27_mode_BN",
        "D_E_diagnostic_validator_passes",
        "D_E_honest_fails_only_selected_source_flags",
        "sector_projectors_on_27_mode_BN",
        "dotD_matrix_in_same_basis",
        "dotD_diagnostic_validator_passes",
        "dotD_honest_fails_only_source_driver_flags",
        "finite_projector_values_emitted",
        "all_projector_checks_pass",
        "all_basis_counts_pass",
        "positive_complement_gap",
        "green_and_horizontal_flags_pass",
        "End0_equivariance_on_emitted_projectors",
        "row_model_offdiagonal_Ext_control",
        "stationary_sector_transfer_subgate",
    ]:
        require(model_closed[key] is True, f"model support not closed: {key}")

    require(model["ambient_dimension"] == 27, "ambient dimension")
    require(model["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id")
    for sector in ["Q", "u", "d", "L", "e", "N"]:
        checks = model["sector_checks"][sector]
        require(checks["projector_idempotent"] is True, f"idempotence {sector}")
        require(checks["projector_self_adjoint"] is True, f"self-adjoint {sector}")
        require(checks["rank_trace"] == 3.0, f"rank {sector}")
        require(checks["basis_vector_count"] == 3, f"basis count {sector}")
        require(checks["green_operator_verified"] is True, f"green {sector}")
        require(checks["horizontal_gauge_verified"] is True, f"horizontal {sector}")
        require(checks["selected_source_verified"] is False, f"selected source oververified {sector}")
        require(checks["selected_value_emitted"] is False, f"selected value overemitted {sector}")
    h_checks = model["sector_checks"]["H"]
    require(h_checks["rank_trace"] == 1.0, "H rank")
    require(h_checks["basis_vector_count"] == 1, "H basis count")
    require(h_checks["selected_source_verified"] is False, "H selected source oververified")

    blockers = promotion["selected_blockers"]
    for key in [
        "selected_HYM_projector_values_promoted",
        "rho_candidate_promoted_to_selected_rho_s",
        "de_action_selected_source_verified",
        "de_honest_validator_promotes",
        "dotd_selected_dotD_source_verified",
        "dotd_alpha1_driver_verified",
        "dotd_honest_validator_promotes",
        "selected_visible_operator_source_closed",
        "visible_gs_selected_operator_source_constructed",
        "full_sector_offdiagonal_control_selected",
    ]:
        require(blockers[key] is False, f"selected blocker overclosed: {key}")
    require(promotion["visible_operator_root"]["selected_visible_operator_source_closed"] is False, "visible root overclosed")
    require(promotion["visible_operator_root"]["selected_D_E_dotD_Riesz_Green_constructed"] is False, "visible DE overclosed")
    require(promotion["visible_operator_root"]["coherent_spectral_zero_mode_projectors_constructed"] is False, "visible projectors overclosed")
    require(len(promotion["minimal_promotion_requirements"]) == 6, "promotion requirement count")

    require(gate["row"] == FINAL_ROW, "gate row")
    require(gate["model_active_payload_present"] is True, "gate model payload")
    require(gate["selected_source_promotion_closed"] is False, "gate source overclosed")
    require(gate["HYM_or_EndE_final_row_accepted"] is False, "gate final row overaccepted")
    require(gate["two_premise_AH_equivalent_final_connection_table_count"] == "7/8", "gate AH count")
    require(gate["strict_no_knob_closed"] is False, "gate strict no-knob")
    require(gate["true_SM_equivalence_closed"] is False, "gate true SM")

    require("finite 27-mode D_E matrix" in next_packet["do_not_rebuild"], "D_E no-rebuild missing")
    require("finite 27-mode sector projectors" in next_packet["do_not_rebuild"], "projector no-rebuild missing")
    require("row-model offdiagonal Ext control" in next_packet["do_not_rebuild"], "offdiag no-rebuild missing")
    require(any("selected_source_verified" in item for item in next_packet["must_promote"]), "selected source requirement")
    require(any("truncation-error" in item for item in next_packet["must_promote"]), "truncation requirement")
    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")

    require(cert["model_active_payload_present"] is True, "cert model payload")
    require(cert["selected_source_promotion_closed"] is False, "cert selected source")
    require(cert["BN27_final_row_accepted"] is False, "cert final row")
    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "cert AH lane")

    require("model-active finite `27`-mode scope" in note, "note model payload")
    require("The matrices are present" in note, "note no rebuild")
    require("selected_source_verified" in note, "note source flag")
    require(NEXT in note, "note next")

    print("Full-sector BN27 HYM/EndE validator payload audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
