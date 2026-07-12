"""Audit Step61 chain-integrity / frontier correction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step61_chainintegrity_audit_or_frontiercorrection"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CHAIN_PACKET = PACKET_DIR / "step61_chain_integrity.packet.json"
FRONTIER_PACKET = PACKET_DIR / "step61_nonlooping_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step61_ChainIntegrityAudit_or_FrontierCorrection_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP61_CHAIN_INTEGRITY_AUDIT_FRONTIER_CONFIRMED_NO_LOOPBACK"
NEXT = "MTT_Selected_HYMProjectorZeroModeBasisValueEmission_or_PrimitiveRowFormulaExecution_v1"
SHARPER_NEXT = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    chain = load(CHAIN_PACKET)
    frontier = load(FRONTIER_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["sharper_hym_subfrontier"] == SHARPER_NEXT, "candidate sharper next mismatch")
    require(cert["sharper_hym_subfrontier"] == SHARPER_NEXT, "certificate sharper next mismatch")
    require(data["theorem"]["proved"] is True, "theorem missing")

    for item in [data, chain, frontier, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    tiers = chain["tiers"]
    admitted = tiers["admitted_replay_tier"]
    require(admitted["closed"] is True, "admitted replay should be closed")
    require(admitted["accepted_as_no_knob_MTT_prediction"] is False, "admitted replay overpromoted")
    require(admitted["accepted_internal_scalar_row_count"] == 0, "admitted replay scalar overaccepted")
    require(admitted["true_SM_equivalence_closed"] is False, "admitted replay true equivalence overclosed")
    require(admitted["full_no_knob_closed"] is False, "admitted replay no-knob overclosed")

    boundary = tiers["noknob_boundary_tier"]
    require(boundary["Rtheta_readiness_present_count"] == 8, "Rtheta readiness present mismatch")
    require(boundary["Rtheta_readiness_requirement_count"] == 9, "Rtheta readiness requirement mismatch")
    require(boundary["accepted_internal_scalar_row_count"] == 0, "boundary scalar overaccepted")

    payload = tiers["dynamic_payload_tier"]
    require(payload["dynamic_payload_row_count"] == 9, "dynamic payload count mismatch")
    require(payload["support_candidate_present_count"] == 9, "support count mismatch")
    require(payload["stationary_source_slot_closed_count"] == 3, "stationary source count mismatch")
    require(payload["accepted_dynamic_payload_row_count"] == 0, "dynamic payload rows overaccepted")
    require(payload["higher_response_Rtheta_executed"] is False, "higher response overexecuted")
    require(payload["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")

    hym = tiers["hym_model_active_support_tier"]
    require(hym["finite_model_active_projector_values_emitted"] is True, "HYM support values missing")
    require(hym["selected_projector_values_promoted"] is False, "HYM values overpromoted")
    require(hym["source_flags_still_false"] is True, "HYM source flags not detected")
    require(hym["next_hym_subfrontier"] == SHARPER_NEXT, "HYM subfrontier mismatch")

    zero = tiers["zero_mode_bridge_tier"]
    require(zero["bridge_theorem_closes"] is True, "zero-mode bridge not closed")
    require(zero["canonical_rho_candidate_promotes_now"] is False, "rho candidate overpromoted")
    require(zero["selected_zero_mode_values_open"] is True, "zero-mode values should remain open")

    diagnosis = chain["loop_diagnosis"]
    require(diagnosis["looped_back_to_first_response"] is False, "loopback to first response")
    require(diagnosis["looped_back_to_model_active_projector_values"] is False, "loopback to model-active values")

    require(frontier["active_frontier"] == NEXT, "frontier active target mismatch")
    require(frontier["sharper_hym_subfrontier"] == SHARPER_NEXT, "frontier sharper target mismatch")
    require(frontier["current_counts"]["accepted_dynamic_payload_row_count"] == 0, "frontier row overaccepted")
    require(frontier["current_counts"]["accepted_scalar_row_count_now"] == 0, "frontier scalar overaccepted")
    for stale in [
        "primitive C1 first-response source layer",
        "A_selected/b_selected/deltaTheta_C1 at the first-response layer",
        "model-active HYM projector emission without selected source flags",
    ]:
        require(stale in frontier["do_not_reopen_as_frontier"], f"missing stale guardrail: {stale}")

    decision = data["closure_decision"]
    require(decision["chain_integrity_audited"] is True, "chain audit not closed")
    require(decision["no_loopback_confirmed"] is True, "no-loopback not confirmed")
    require(decision["earlier_closer_at_admitted_replay_tier"] is True, "earlier replay closeness missing")
    require(decision["closer_at_internal_noknob_tier"] is False, "no-knob closeness overclaimed")
    require(decision["model_active_hym_values_not_promoted"] is True, "HYM nonpromotion missing")
    for key in ["higher_response_Rtheta_executed", "true_SM_equivalence_closed", "full_no_knob_closed"]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")

    for phrase in [
        "not looped back",
        "closer before at admitted replay tier        : true",
        "closer before at internal no-knob tier       : false",
        "accepted dynamic payload rows now            : 0",
        NEXT,
        SHARPER_NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
