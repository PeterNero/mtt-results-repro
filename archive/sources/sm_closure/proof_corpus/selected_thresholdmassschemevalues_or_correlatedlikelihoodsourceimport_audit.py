"""Audit threshold/mass-scheme values or correlated likelihood source-import gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESIDUALS = PACKET_DIR / "threshold_mass_scheme_residual_values.packet.json"
IMPORT = PACKET_DIR / "correlated_likelihood_source_import_status.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_after_residuals_and_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_mass_scheme_source_import.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDMASSSCHEMEVALUES_OR_CORRELATEDLIKELIHOODSOURCEIMPORT_"
    "BUILT_RESIDUAL_VALUES_SOURCE_IMPORT_OPEN"
)
NEXT = "MTT_Selected_AcceptedThresholdMassSchemeSourceRows_or_NoKnobValueDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    residuals = load(RESIDUALS)
    import_status = load(IMPORT)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    summary = residuals["summary"]
    require(summary["row_count"] == 15, "unexpected residual row count")
    require(summary["all_residuals_finite"] is True, "non-finite residual")
    require(summary["max_abs_transport_relative_delta"] > 0.0, "transport residuals missing")
    require(summary["max_abs_boundary_relative_delta"] > 0.0, "boundary residuals missing")
    require(len(residuals["transport_residual_rows"]) == 9, "transport row count mismatch")
    require(len(residuals["boundary_residual_rows"]) == 6, "boundary row count mismatch")
    require(residuals["what_this_closes"]["finite_residual_table_for_threshold_mass_scheme_audit"] is True, "residual audit not closed")
    require(residuals["accepted_as_threshold_matching_values"] is False, "threshold values overaccepted")
    require(residuals["accepted_as_mass_scheme_conversion_values"] is False, "mass-scheme values overaccepted")
    for row in residuals["transport_residual_rows"] + residuals["boundary_residual_rows"]:
        require(row["finite"] is True, f"row not finite: {row['id']}")

    require(import_status["source_import_absence_confirmed"] is True, "source absence not confirmed")
    require(import_status["published_or_reconstructed_profile_imported"] is False, "profile import overclaimed")
    require(import_status["accepted_as_full_correlated_likelihood_source"] is False, "likelihood overaccepted")

    tests = promotion["promotion_tests"]
    require(tests["threshold_mass_scheme_residual_values_emitted"] is True, "residual values not emitted")
    require(tests["all_residuals_finite"] is True, "finite residual test missing")
    for key in [
        "accepted_threshold_matching_values_emitted",
        "accepted_mass_scheme_conversion_values_emitted",
        "correlated_likelihood_source_imported",
        "multi_loop_threshold_convention_values_emitted",
        "no_knob_MTT_source_derivation_of_values",
    ]:
        require(tests[key] is False, f"promotion overclosed {key}")
        require(key in promotion["remaining_hard_failures"], f"hard failure missing: {key}")

    decision = promotion["promotion_decision"]
    require(decision["residual_value_audit_closed"] is True, "residual audit decision missing")
    require(decision["accepted_threshold_mass_scheme_layer_closed"] is False, "threshold layer overclosed")
    require(decision["correlated_likelihood_source_imported"] is False, "source import overclosed")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(promotion["closure_claimed"] is False, "promotion overclaimed closure")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed closure")
    require(data["closure_decision"]["residual_value_audit_closed"] is True, "candidate residual audit not closed")
    require(data["closure_decision"]["accepted_threshold_mass_scheme_layer_closed"] is False, "candidate threshold overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require("residual-value audit only" in note, "note missing residual guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
