"""Audit Step 33 smooth-S3 validator reconciliation and holonomy promotion cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step33_smooths3validator_reconciliation_or_holonomyoperatorpromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECONCILIATION = PACKET_DIR / "step33_strict_q79_validator_reconciliation.packet.json"
HOLONOMY = PACKET_DIR / "step33_holonomy_operator_promotion_contract.packet.json"
FILL_TARGETS = PACKET_DIR / "step33_minimal_smooth_source_fill_targets.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step33_SmoothS3ValidatorReconciliation_or_HolonomyOperatorPromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP33_SMOOTHS3_VALIDATOR_RECONCILED_HOLONOMY_PROMOTION_OPEN"
NEXT = "MTT_Selected_SmoothS3DeligneCechSourceMap_or_HolonomyOperatorSource_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    reconciliation = load(RECONCILIATION)
    holonomy = load(HOLONOMY)
    fill_targets = load(FILL_TARGETS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    step32 = reconciliation["step32_frontier"]
    require(step32["smooth_s3_twisted_source_lift_closed"] is False, "Step32 smooth source overclosed")
    require(step32["smooth_freed_witten_projector_retention_closed"] is False, "Step32 FW overclosed")
    require(step32["operator_level_projective_rhoE_transition_closed"] is False, "Step32 rhoE overclosed")

    q79 = reconciliation["q79_strict_validator"]
    require(
        q79["status"] == "VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN",
        "wrong q79 smooth attempt status",
    )
    require(q79["selected_smooth_S3_source_constructed"] is False, "q79 smooth source overclosed")
    require(q79["smooth_S3_Freed_Witten_closed"] is False, "q79 FW overclosed")
    require(q79["smooth_S3_projector_retention_closed"] is False, "q79 projector retention overclosed")
    require(q79["selected_cover_or_scaffold_verified"] is False, "selected cover overclosed")
    require(q79["source_selected_by_mtt"] is False, "source selected overclosed")
    for phrase in [
        "smooth_source.source_selected_by_mtt must be true",
        "smooth_source.selected_cover_or_scaffold_verified must be true",
        "smooth_source.good_cover_data_supplied must be true",
        "smooth_source.fixed_differential_cohomology_class must be true",
        "consistency.freed_witten_verified_for_smooth_S3_source must be true",
        "consistency.twisted_projector_retention_verified must be true",
    ]:
        require(phrase in q79["missing_validator_fields"], f"missing validator field not recorded: {phrase}")

    support = reconciliation["finite_support_kept_closed"]
    require(support["finite_S3_CP_cancellation_closed"] is True, "finite CP not retained")
    require(support["finite_twisted_CP_module_on_S3"] is True, "finite twisted module not retained")
    require(support["finite_total_twisted_DD_class_zero"] is True, "finite total DD not retained")
    require(support["finite_projector_architecture_retained"] is True, "finite projector support not retained")
    require(support["visible_green_schwarz_curvature_closed"] is True, "GS curvature support not retained")

    demoted = reconciliation["older_projective_packet_demoted_fields"]
    require(demoted["older_packet_claimed_fixed_smooth_flat_S3_class_retired"] is True, "expected old retired wording absent")
    require(demoted["older_packet_claimed_smooth_S3_twisted_Freed_Witten_retired"] is True, "expected old FW wording absent")
    require(demoted["strict_validator_keeps_these_open"] is True, "strict validator not active")

    require(holonomy["status"] == "HOLONOMY_OPERATOR_PROMOTION_CONTRACT_EMITTED_SOURCE_MAP_OPEN", "holonomy status mismatch")
    require(holonomy["operator_values_closed"] is False, "operator values overclosed")
    require(holonomy["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    for route in ["A_smooth_Deligne_Cech_source", "B_holonomy_operator_source"]:
        require(route in holonomy["two_legal_routes"], f"route missing: {route}")
    for forbidden in [
        "identity rho_E smoke",
        "ordinary rank-two DD-zero route for S3",
        "observed Yukawa/CKM/PMNS/mass values",
        "projective prototype promoted without selected cover/source certificate",
    ]:
        require(forbidden in holonomy["must_not_use"], f"forbidden shortcut missing: {forbidden}")

    required = fill_targets["required_true_fields"]
    for field in [
        "selected_stack == S3",
        "smooth_source.source_selected_by_mtt",
        "smooth_source.selected_cover_or_scaffold_verified",
        "smooth_source.deligne_cech_representative_constructed",
        "consistency.freed_witten_verified_for_smooth_S3_source",
        "consistency.block_factorized_family_higgs_projectors_retained",
    ]:
        require(field in required, f"required field missing: {field}")
    require(fill_targets["already_available_support"]["finite_S3_CP_cancellation_closed"] is True, "support field missing")
    require(fill_targets["currently_absent_source_certificate"] is True, "absent source certificate not recorded")
    require(fill_targets["selected_cycles_supplied"] is False, "selected cycles overclosed")
    require(fill_targets["rank_two_active_images_fail_ordinary_DD"] is True, "ordinary DD obstruction missing")

    decision = data["closure_decision"]
    for key in [
        "strict_q79_smooth_validator_promoted_to_active_gate",
        "older_projective_gerbe_retired_blocker_wording_demoted",
        "finite_s3_cp_and_projector_support_kept_closed",
        "holonomy_operator_promotion_contract_emitted",
        "minimal_smooth_source_fill_targets_extracted",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "smooth_s3_twisted_source_lift_closed",
        "selected_smooth_cover_or_scaffold_closed",
        "smooth_freed_witten_projector_retention_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "accepted scalar rows overclosed")
    require(data["theorem"]["proved"] is True, "frontier theorem not proved")
    require(cert["strict_q79_smooth_validator_active"] is True, "certificate validator flag missing")
    require(cert["smooth_s3_twisted_source_lift_closed"] is False, "certificate smooth source overclosed")
    require(cert["operator_sector_values_closed"] is False, "certificate operator values overclosed")

    for phrase in [
        "strict q79 smooth-source validator is now the active gate",
        "selected smooth cover/good-cover data",
        "holonomy-induced operator-level projective `rho_E`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
