"""Audit first value-source row fill attempt or external threshold source import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FIRST_ROW = PACKET_DIR / "first_value_source_row_fill_attempt.packet.json"
EXTERNAL_IMPORT = PACKET_DIR / "external_threshold_source_import_attempt.packet.json"
DECISION = PACKET_DIR / "first_row_acceptance_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_first_value_source_row_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstValueSourceRowFill_or_ExternalThresholdSourceImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FIRSTVALUESOURCEROWFILL_OR_EXTERNALTHRESHOLDSOURCEIMPORT_"
    "BUILT_FIRST_ROW_NUMERIC_SOURCE_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_FirstValueSourceRowPromotion_or_HonestGalerkinPrimitiveRow_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    first_row = load(FIRST_ROW)
    external_import = load(EXTERNAL_IMPORT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(first_row["target_obligation"] == "VSD-01-selected-overlap-value-kernel", "wrong target obligation")
    require(first_row["acceptance_tests"]["numeric_row_filled"] is True, "numeric row not filled")
    require(first_row["acceptance_tests"]["mass_split_positive_conditionally"] is True, "mass split test missing")
    require(first_row["acceptance_tests"]["mixing_commutators_positive_conditionally"] is True, "mixing test missing")
    require(first_row["acceptance_tests"]["cp_odd_nonzero_conditionally"] is True, "CP test missing")
    require(first_row["acceptance_tests"]["observed_flavor_data_used"] is False, "observed flavor data used")
    for key in [
        "selected_dynamic_source_to_C1_transfer_emitted",
        "selected_Hessian_blocks_emitted",
        "selected_b_selected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
    ]:
        require(first_row["acceptance_tests"][key] is False, f"source-promotion field overclosed: {key}")
    require(first_row["accepted_as_selected_dynamic_value_source_row"] is False, "first row overaccepted")
    require(first_row["closure_claimed"] is False, "first row overclaimed closure")

    require(external_import["accepted_external_rows_imported_now"] is False, "external row overimported")
    require(external_import["closure_claimed"] is False, "external import overclaimed")

    require(decision["route_A_internal_row"]["numeric_first_row_filled"] is True, "route A numeric row missing")
    require(decision["route_A_internal_row"]["conditional_quality_tests_pass"] is True, "route A quality tests missing")
    require(decision["route_A_internal_row"]["accepted_as_selected_dynamic_value_source_row"] is False, "route A overaccepted")
    require(decision["route_A_internal_row"]["can_close_VSD_01_now"] is False, "VSD-01 overclosed")
    require(decision["route_B_external_import"]["accepted_external_threshold_row_imported"] is False, "route B overimported")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["closure_claimed"] is False, "decision overclaimed")
    for key in [
        "selected_dynamic_source_to_C1_transfer_emitted",
        "selected_Hessian_blocks_emitted",
        "selected_b_selected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
        "accepted_external_threshold_rows_imported",
    ]:
        require(key in decision["remaining_hard_failures"], f"hard failure missing: {key}")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(data["closure_decision"]["first_value_source_row_numeric_payload_emitted"] is True, "candidate numeric row not emitted")
    require(data["closure_decision"]["accepted_as_selected_dynamic_value_source_row"] is False, "candidate first row overaccepted")
    require(data["closure_decision"]["VSD_01_closed"] is False, "candidate VSD-01 overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require("accepted as selected source row: false" in note, "note missing source-row guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
