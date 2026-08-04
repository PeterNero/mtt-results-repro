"""Audit VSD-02 threshold response rule / external likelihood import classifier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CLASSIFICATION = PACKET_DIR / "vsd02_row_route_classification.packet.json"
EXTERNAL_MANIFEST = PACKET_DIR / "external_likelihood_import_manifest.packet.json"
INTERNAL_WORKORDER = PACKET_DIR / "internal_threshold_response_derivation_workorder.packet.json"
DECISION = PACKET_DIR / "vsd02_threshold_response_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_classification.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VSD02THRESHOLDRESPONSERULE_OR_EXTERNALLIKELIHOODIMPORT_"
    "BUILT_ROUTE_CLASSIFICATION_ACCEPTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    classification = load(CLASSIFICATION)
    external = load(EXTERNAL_MANIFEST)
    internal = load(INTERNAL_WORKORDER)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(classification["target"] == "VSD-02-threshold-response-rule", "wrong target")
    require(classification["accepted_row_count"] == 0, "accepted rows overclaimed")
    require(len(classification["row_routes"]) == 6, "wrong row route count")
    buckets = classification["bucket_counts"]
    require(buckets["internal_derivation_candidate_open"] >= 2, "internal route bucket missing")
    require(buckets["partial_support_not_accepted"] >= 1, "partial support bucket missing")
    require(buckets["external_import_candidate_open"] >= 1, "external route bucket missing")
    for row in classification["row_routes"]:
        require(row["accepted_now"] is False, f"row overaccepted: {row['row_id']}")
        require(row["missing_for_acceptance"], f"missing requirements absent for {row['row_id']}")

    require(external["accepted_external_likelihood_imported_now"] is False, "external likelihood overimported")
    higgs = external["partial_external_rows"]["higgs_decay_covariance_candidate"]
    require(higgs["present"] is True, "partial Higgs covariance not detected")
    require(higgs["accepted_as_full_true_equivalence_profile"] is False, "Higgs covariance overaccepted")
    replay = external["partial_external_rows"]["published_profile_replay"]
    require(replay["present"] is True, "published profile replay not detected")
    require(replay["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overaccepted")
    full = external["full_profile_likelihood_status"]
    for key in [
        "published_or_reconstructed_profile_imported",
        "official_machine_readable_likelihood_imported",
        "profile_likelihood_scan_imported",
        "nuisance_profile_semantics_imported",
    ]:
        require(full[key] is False, f"full likelihood field overaccepted: {key}")
    require(external["closure_claimed"] is False, "external manifest overclaimed")

    require(internal["accepted_firstpass_value_packet"]["accepted_as_versioned_common_scale_candidate_values"] is True, "firstpass values missing")
    require(internal["accepted_firstpass_value_packet"]["accepted_for_true_precision_equivalence"] is False, "firstpass values overaccepted")
    require(internal["finite_residual_support"]["all_residuals_finite"] is True, "finite residual support missing")
    require(internal["finite_residual_support"]["accepted_as_threshold_matching_values"] is False, "threshold residuals overaccepted")
    require(internal["finite_residual_support"]["accepted_as_mass_scheme_conversion_values"] is False, "mass residuals overaccepted")
    require(internal["acceptance_contract"]["values_promotable_now"] is False, "acceptance contract overpromotes")
    require(len(internal["minimal_internal_derivation_outputs_required"]) >= 5, "internal workorder too small")
    require(internal["closure_claimed"] is False, "internal workorder overclaimed")

    require(decision["accepted_threshold_response_rule_closed"] is False, "threshold response overclosed")
    require(decision["accepted_external_likelihood_import_closed"] is False, "external import overclosed")
    require(decision["internal_derivation_closed"] is False, "internal derivation overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    for key in [
        "row_route_classification",
        "external_import_manifest",
        "internal_derivation_workorder",
        "partial_higgs_covariance_separated_from_full_likelihood",
        "old_VSD01_reentry_prevented",
    ]:
        require(decision["what_is_newly_closed"][key] is True, f"new close flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["VSD02_route_classification_closed"] is True, "classification not closed")
    require(final["accepted_threshold_response_rule_closed"] is False, "threshold response final overclosed")
    require(final["accepted_external_likelihood_import_closed"] is False, "external import final overclosed")
    require(final["true_SM_equivalence_closed"] is False, "true equivalence final overclosed")
    require(final["full_no_knob_closed"] is False, "no-knob final overclosed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("partial Higgs covariance separated cleanly" in note, "note missing partial/full distinction")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
