"""Audit accepted threshold/mass-scheme source rows or no-knob value derivation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_AUDIT = PACKET_DIR / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
DERIVATION = PACKET_DIR / "no_knob_value_derivation_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_source_row_audit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_row_audit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedThresholdMassSchemeSourceRows_or_NoKnobValueDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ACCEPTEDTHRESHOLDMASSSCHEMESOURCEROWS_OR_NOKNOBVALUEDERIVATION_"
    "BUILT_SOURCE_ROW_AUDIT_NO_KNOB_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source = load(SOURCE_AUDIT)
    derivation = load(DERIVATION)
    promotion = load(PROMOTION)
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

    require(source["candidate_count"] == 6, "candidate source row count mismatch")
    require(source["support_present_count"] >= 5, "support row count unexpectedly low")
    require(source["promotable_count"] == 0, "source rows overpromoted")
    require(source["accepted_source_rows_present"] is False, "accepted source rows overclaimed")
    require(source["accepted_threshold_matching_source_rows"] == [], "threshold source rows overclaimed")
    require(source["accepted_mass_scheme_conversion_source_rows"] == [], "mass-scheme source rows overclaimed")
    for row in source["candidate_rows"]:
        require(row["can_promote_to_accepted_threshold_mass_scheme_source"] is False, f"row overpromoted: {row['id']}")

    require(derivation["no_knob_value_derivation_closed"] is False, "no-knob derivation overclosed")
    require(derivation["closed_obligation_count"] == 0, "obligations overclosed")
    require(derivation["obligation_count"] == 5, "obligation count mismatch")
    for key, value in derivation["attempted_derivation"].items():
        require(value is False, f"derivation overclosed: {key}")

    tests = promotion["promotion_tests"]
    require(tests["candidate_source_rows_audited"] is True, "source row audit not closed")
    require(tests["support_present_for_no_knob_routes"] is True, "support not detected")
    for key in [
        "accepted_threshold_matching_source_rows",
        "accepted_mass_scheme_conversion_source_rows",
        "no_knob_value_source_derivation_closed",
        "external_correlated_likelihood_or_threshold_source_imported",
        "multi_loop_threshold_convention_source_rows",
    ]:
        require(tests[key] is False, f"promotion overclosed {key}")
    for key in [
        "accepted_threshold_matching_source_rows",
        "accepted_mass_scheme_conversion_source_rows",
        "no_knob_value_source_derivation",
        "external_correlated_likelihood_or_threshold_source_import",
        "multi_loop_threshold_convention_source_rows",
    ]:
        require(key in promotion["remaining_hard_failures"], f"hard failure missing: {key}")

    decision = promotion["promotion_decision"]
    require(decision["source_row_audit_closed"] is True, "source audit decision missing")
    require(decision["accepted_threshold_mass_scheme_source_layer_closed"] is False, "source layer overclosed")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(promotion["closure_claimed"] is False, "promotion closure overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(data["closure_decision"]["source_row_audit_closed"] is True, "candidate source audit not closed")
    require(data["closure_decision"]["accepted_threshold_mass_scheme_source_layer_closed"] is False, "candidate source layer overclosed")
    require(data["closure_decision"]["no_knob_value_derivation_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require("promotable rows        = 0" in note, "note missing zero-promotion guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
