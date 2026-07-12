"""Audit Step 32 same-source symmetry breaking to smooth S3 twisted source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step32_samesourcesymmetrybreaking_to_smooths3twistedsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PIC0 = PACKET_DIR / "step32_pic0_or_gerbe_route_decision.packet.json"
S3 = PACKET_DIR / "step32_finite_s3_restriction_projector_retention.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step32_smooth_s3_twisted_source_lift_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step32_SameSourceSymmetryBreaking_to_SmoothS3TwistedSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP32_SAMESOURCE_SYMMETRYBREAKING_REDUCED_TO_SMOOTH_S3_TWISTED_SOURCE"
NEXT = "MTT_Selected_SmoothS3TwistedSourceLift_or_HolonomyOperatorPromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    pic0 = load(PIC0)
    s3 = load(S3)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(pic0["from_step31"]["same_source_symmetrybreaking_contract_emitted"] is True, "Step31 contract missing")
    require(pic0["from_step31"]["same_source_symmetrybreaking_source_closed"] is False, "Step31 source overclosed")
    terminal = pic0["terminal_pic0_gate"]
    require(terminal["terminal_lane_conditional_uniqueness_imported"] is True, "terminal uniqueness missing")
    require(terminal["selected_terminal_lane_pic0_source_proved"] is False, "terminal source overproved")
    require(terminal["naive_pic0_quotient_rejected"] is True, "Pic0 quotient not rejected")
    require(terminal["neutral_pic0_selection_absent"] is True, "neutral Pic0 overselected")
    require(terminal["finite_gerbe_torsion_route_live"] is True, "gerbe route not live")
    reduction = pic0["pic0_to_gerbe_reduction"]
    require(reduction["direct_pic0_invariance_proved"] is False, "direct Pic0 overproved")
    require(reduction["direct_pic0_invariance_retired_for_now"] is True, "direct Pic0 not retired")
    require(reduction["finite_q79_f_m1_gerbe_imported"] is True, "finite gerbe not imported")
    require(reduction["gerbe_twisted_de_source_status"] == "PRIMARY_EXECUTION_ROUTE", "gerbe route not primary")
    require(reduction["selected_DE_dotD_Riesz_Green_constructed"] is False, "operator values overconstructed")
    require(reduction["selected_smooth_s3_source_constructed"] is False, "smooth source overconstructed")

    restriction = s3["restriction_packet"]
    require(restriction["branch"]["q"] == 79, "wrong q")
    require(restriction["branch"]["orientation"] == "F", "wrong orientation")
    require(restriction["branch"]["torsion_label_m"] == 1, "wrong torsion label")
    require(restriction["S3_active_image_rank_over_F3"] == 2, "wrong S3 rank")
    require(restriction["ordinary_S3_DD_zero"] is False, "ordinary S3 DD zero overclaimed")
    require(restriction["finite_twisted_CP_DD_class_matches_B_restriction"] is True, "twisted CP mismatch")
    finite = s3["finite_gate_results"]
    for key in [
        "S3_rank_two_active_image_imported",
        "finite_twisted_S3_CP_cancellation_imported",
        "finite_block_projector_architecture_retained",
        "ordinary_S3_DD_zero_rejected",
        "W3_spinC_imported_closed",
    ]:
        require(finite[key] is True, f"finite gate missing: {key}")
    smooth = s3["smooth_open_flags"]
    for key in [
        "smooth_s3_source_constructed",
        "smooth_Freed_Witten_closed",
        "smooth_projector_retention_closed",
        "selected_DE_dotD_Riesz_Green_constructed",
    ]:
        require(smooth[key] is False, f"smooth gate overclosed: {key}")
    proj = s3["projective_gerbe_status"]
    require(proj["source_level_projective_gerbe_rhoE_promoted"] is True, "source gerbe not promoted")
    require(proj["operator_level_projective_rhoE_promoted"] is False, "operator rhoE overpromoted")
    require(proj["coherent_spectral_projector_verified"] is False, "spectral projector oververified")
    require(s3["projective_BN_mechanical_lift_closed"] is True, "Step30 mechanical lift not imported")

    require(contract["next_required_artifact"] == NEXT, "contract next mismatch")
    require(contract["closure_claimed"] is False, "contract overclaimed")
    for phrase in [
        "fixed smooth Deligne/Cech differential-cohomology representative restricting to the finite q79/F,m=1 S3 cocycle",
        "selected S3 cycles or smooth substitute proving Freed-Witten cancellation, not only finite CP cancellation",
        "smooth block-factorized Q,u,d,L,e,N,H projector retention on the twisted S3 source",
        "same-branch operator-level projective rho_E transition on the smooth projective B_N lift",
        "selected D_E, Riesz/Green, and dotD source flags derived from that smooth source",
    ]:
        require(phrase in contract["must_emit_next"], f"must emit missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source",
        "direct_pic0_invariance_route_retired",
        "gerbe_twisted_s3_route_primary",
        "finite_s3_restriction_projector_retention_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "smooth_s3_twisted_source_lift_closed",
        "smooth_freed_witten_projector_retention_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source"] is True, "certificate reduction missing")
    require(cert["smooth_s3_twisted_source_lift_closed"] is False, "certificate overclosed smooth source")
    require(cert["operator_sector_values_closed"] is False, "certificate overclosed values")

    for phrase in [
        "direct Pic0 invariance / neutral Pic0 shortcut      retired",
        "finite S3 rank-two active image                     closed",
        "smooth S3 twisted source lift                       open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
