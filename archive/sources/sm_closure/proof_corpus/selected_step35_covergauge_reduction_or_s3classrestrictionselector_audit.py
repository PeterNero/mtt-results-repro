"""Audit Step 35 cover-gauge reduction and S3 class/restriction selector."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step35_covergauge_reduction_or_s3classrestrictionselector"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
REDUCTION = PACKET_DIR / "step35_cover_gauge_reduction.packet.json"
SELECTOR = PACKET_DIR / "step35_s3_class_restriction_selector.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step35_CoverGaugeReduction_or_S3ClassRestrictionSelector_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP35_COVER_GAUGE_REDUCED_TO_S3_CLASS_RESTRICTION_SELECTOR_OPEN"
NEXT = "MTT_Selected_S3DifferentialCohomologyClassRestriction_and_ProjectorRetention_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    reduction = load(REDUCTION)
    selector = load(SELECTOR)
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

    require(reduction["imported_q79_status"] == "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CLOSED_CLASS_RESTRICTION_OPEN", "wrong q79 status")
    closes = reduction["what_closes"]
    require(closes["good_cover_is_execution_scaffold_not_physical_knob"] is True, "good cover knob not closed")
    require(closes["particular_good_cover_need_not_be_MTT_selected"] is True, "particular cover still treated as selected")
    require(closes["selected_cover_blocker_reduced_to_selected_class_and_restriction"] is True, "cover blocker not reduced")
    require(reduction["mathematical_reduction"]["curvature_H_form"] == "0", "flat curvature mismatch")
    require(reduction["mathematical_reduction"]["torsion_order"] == 3, "torsion mismatch")
    require(reduction["good_cover_as_new_knob"] is False, "good cover knob introduced")
    require(reduction["step34_refinement"]["step34_functor_kept"] is True, "Step34 functor not preserved")

    require(selector["status"] == "S3_DIFFERENTIAL_COHOMOLOGY_CLASS_RESTRICTION_SELECTOR_OPEN", "selector status mismatch")
    require(selector["selected_class_restriction_closed"] is False, "selected class overclosed")
    require(selector["projector_retention_closed"] is False, "projector retention overclosed")
    require(selector["operator_values_closed"] is False, "operator values overclosed")
    for item in [
        "fixed smooth flat differential-cohomology class on the q79/F,m=1 S3 worldvolume",
        "restriction/pullback table of that class to S3",
        "twisted CP module matching the pulled-back class",
        "block-sector family/Higgs projector retention",
    ]:
        require(item in selector["must_select_next"], f"must-select missing: {item}")
    for item in [
        "good-cover Deligne/Cech table",
        "holonomy/classifying-map representative",
    ]:
        require(item in selector["execution_representatives_allowed_after_selection"], f"execution representative missing: {item}")

    decision = data["closure_decision"]
    for key in [
        "good_cover_removed_as_physical_knob",
        "cover_refinement_invariance_imported",
        "step34_functor_preserved",
        "frontier_reduced_to_selected_s3_class_restriction",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_s3_differential_cohomology_class_closed",
        "s3_restriction_pullback_table_closed",
        "smooth_freed_witten_projector_retention_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["good_cover_removed_as_physical_knob"] is True, "certificate cover flag missing")
    require(cert["selected_s3_differential_cohomology_class_closed"] is False, "certificate class overclosed")
    require(cert["operator_sector_values_closed"] is False, "certificate operator values overclosed")

    for phrase in [
        "good cover is an execution",
        "not a new physical knob",
        "selected smooth",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
