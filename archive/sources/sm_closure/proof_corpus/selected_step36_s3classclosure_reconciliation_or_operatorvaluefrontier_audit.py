"""Audit Step 36 S3 class-closure reconciliation and operator-value frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECON = PACKET_DIR / "step36_s3_class_closure_reconciliation.packet.json"
FRONTIER = PACKET_DIR / "step36_operator_value_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step36_S3ClassClosureReconciliation_or_OperatorValueFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP36_S3_CLASS_CLOSURE_RECONCILED_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_OperatorLevelProjectiveRhoE_DE_RieszGreenDotD_from_S3Source_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(RECON)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    before = recon["step35_frontier_flags_before_reconciliation"]
    require(before["selected_s3_differential_cohomology_class_closed"] is False, "expected Step35 old open flag absent")
    require(before["s3_restriction_pullback_table_closed"] is False, "expected Step35 pullback old open flag absent")
    require(before["smooth_freed_witten_projector_retention_closed"] is False, "expected Step35 FW old open flag absent")

    strong = recon["stronger_selected_s3_source_certificate"]
    require(strong["selected_s3_flat_Deligne_class_imported"] is True, "selected S3 class not imported")
    require(strong["selected_s3_pullback_table_imported"] is True, "S3 pullback not imported")
    require(strong["map_to_qutrit_central_cocycle_verified"] is True, "central cocycle not verified")
    require(strong["smooth_Freed_Witten_cancellation_closed"] is True, "FW not closed")
    require(strong["block_projector_retention_closed"] is True, "block projector retention not closed")
    require(strong["selected_packet_validator_passes"] is True, "selected packet validator does not pass")
    closes = strong["certificate_closes"]
    require(closes["selected_S3_flat_Deligne_class"] is True, "cert class close missing")
    require(closes["selected_S3_pullback_restriction_table"] is True, "cert pullback close missing")
    require(closes["block_factorized_family_Higgs_projector_retention"] is True, "cert block projector close missing")

    demotion = recon["older_open_artifacts_demoted_for_exact_fields_only"]
    require(demotion["smooth_lift_fixed_class_supplied_old_flag"] is False, "old smooth lift should be older open flag")
    require(demotion["smooth_lift_source_selected_old_flag"] is False, "old smooth source should be older open flag")
    require("does not close operator" in demotion["demotion_rule"], "demotion rule must preserve operator frontier")

    closed = frontier["closed_before_operator_frontier"]
    for key in [
        "projective_BN_mechanical_lift_fields_closed",
        "selected_S3_flat_Deligne_class",
        "selected_S3_pullback_restriction_table",
        "map_to_qutrit_central_cocycle",
        "smooth_S3_twisted_Freed_Witten_cancellation",
        "block_factorized_family_Higgs_projector_retention",
        "visible_green_schwarz_curvature_support",
    ]:
        require(closed[key] is True, f"frontier closed support missing: {key}")
    open_ops = frontier["still_open_operator_values"]
    require(open_ops["selected_visible_operator_source_constructed"] is False, "visible operator overclosed")
    require(open_ops["selected_D_E_dotD_Riesz_Green_constructed"] is False, "DE/dotD overclosed")
    require(open_ops["coherent_spectral_zero_mode_projectors_constructed"] is False, "spectral projectors overclosed")
    require(open_ops["coherent_spectral_projector_retention"] is True, "spectral frontier missing")
    require(open_ops["selected_RouteC_Strominger_Galerkin_residual_solve"] is True, "Route-C frontier missing")
    require(frontier["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    for item in [
        "operator-level projective rho_E transition induced by the selected S3 source",
        "selected covariant D_E on the projective B_N lift",
        "source-verified Riesz/Green operator with gap/error certificate",
        "source-verified dotD and coherent spectral zero-mode projectors",
    ]:
        require(item in frontier["next_must_emit"], f"next item missing: {item}")

    decision = data["closure_decision"]
    for key in [
        "selected_s3_differential_cohomology_class_closed",
        "s3_restriction_pullback_table_closed",
        "smooth_freed_witten_cancellation_closed",
        "block_family_higgs_projector_retention_closed",
        "good_cover_removed_as_physical_knob",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "coherent_spectral_zero_mode_projectors_closed",
        "selected_visible_operator_source_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "accepted scalar rows overclosed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["selected_s3_differential_cohomology_class_closed"] is True, "certificate class close missing")
    require(cert["operator_sector_values_closed"] is False, "certificate operator values overclosed")
    require(cert["coherent_spectral_zero_mode_projectors_closed"] is False, "certificate spectral projectors overclosed")

    for phrase in [
        "Step36 reconciles Step35",
        "S3 differential-cohomology class/restriction frontier is now closed",
        "operator-level projective `rho_E`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
