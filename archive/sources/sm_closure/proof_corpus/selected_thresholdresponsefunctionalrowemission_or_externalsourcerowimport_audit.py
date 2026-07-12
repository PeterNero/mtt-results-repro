"""Audit threshold-response row emission / external source-row import bridge."""

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
BUILDER = ROOT / "scripts" / "build_selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.py"

SLUG = "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1.md"

INTERNAL = PACKET_DIR / "internal_threshold_response_functional_row_emission.packet.json"
EXTERNAL = PACKET_DIR / "post_pi_external_source_row_import.packet.json"
READINESS = PACKET_DIR / "step4_value_layer_readiness_after_external_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_response_import.packet.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEFUNCTIONALROWEMISSION_OR_EXTERNALSOURCEROWIMPORT_"
    "BUILT_EXTERNAL_REPLAY_IMPORT_CLOSED_INTERNAL_RTHETA_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    internal = load(INTERNAL)
    external = load(EXTERNAL)
    readiness = load(READINESS)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "closure_claimed",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail overclaimed: {key}", errors)
    for key in ["closure_claimed", "true_SM_equivalence_claimed", "full_no_knob_closure_claimed"]:
        expect(cert.get(key) is False, f"certificate guardrail overclaimed: {key}", errors)
    expect(cert.get("observed_data_used_as_selector") is False, "certificate observed selector used", errors)
    expect(cert.get("target_fitting_used") is False, "certificate target fitting used", errors)

    expect(
        internal.get("status") == "RTHETA_SOURCE_DOMAIN_CLOSED_NUMERIC_VALUE_ROWS_NOT_EMITTED",
        "internal status mismatch",
        errors,
    )
    expect(internal.get("source_domain_closed") is True, "internal source domain not closed", errors)
    expect(internal.get("selected_functional_symbol") == "R_theta", "internal functional symbol mismatch", errors)
    expect(
        internal.get("basis_map_to_sector_scaled_magnitude_rows_closed") is True,
        "basis map closure not preserved",
        errors,
    )
    for key in [
        "selected_threshold_response_functional_instantiated",
        "coefficient_functional_closed",
        "lambda_H_coefficient_selected",
        "accepted_as_internal_selected_Rtheta_row",
        "closure_claimed",
    ]:
        expect(internal.get(key) is False, f"internal overclosed: {key}", errors)
    expect(internal.get("selected_internal_value_emission_count") == 0, "internal emitted selected values", errors)
    expect(internal.get("accepted_coefficient_value_count") == 0, "internal accepted coefficients", errors)

    expect(
        external.get("status") == "POST_PI_ADMITTED_EXTERNAL_SOURCE_ROWS_IMPORTED_FOR_REPLAY",
        "external status mismatch",
        errors,
    )
    expect(external.get("old_manifest_local_scan_had_no_rows") is True, "old manifest state not preserved", errors)
    expect(
        external.get("post_pi_admission_supersedes_old_local_scan") is True,
        "post-Pi import reconciliation failed",
        errors,
    )
    expect(external.get("accepted_external_threshold_row_count") == 7, "threshold row count mismatch", errors)
    expect(external.get("accepted_external_mass_scheme_row_count") == 3, "mass row count mismatch", errors)
    for key in [
        "accepted_external_source_row_imported",
        "accepted_external_threshold_rows_imported",
        "accepted_external_mass_scheme_rows_imported",
        "accepted_external_profile_row_imported",
        "accepted_diagonal_profile_theorem_closed",
        "closure_claimed",
    ]:
        expect(external.get(key) is True, f"external closure missing: {key}", errors)
    expect(external.get("accepted_as_internal_selected_Rtheta_row") is False, "external promoted to internal", errors)
    expect(external.get("external_rows_used_as_branch_selector") is False, "external rows used as selector", errors)
    expect(external.get("observed_data_used_as_selector") is False, "external observed selector used", errors)
    expect(external.get("target_fitting_used") is False, "external target fitting used", errors)
    expect(external.get("closure_tier") == "admitted external replay", "external tier mismatch", errors)

    expect(
        readiness.get("status") == "STEP4_EXTERNAL_IMPORT_LANE_CLOSED_INTERNAL_VALUE_EMISSION_OPEN",
        "readiness status mismatch",
        errors,
    )
    expect(readiness.get("old_first_nonlooping_external_imported") is False, "old first pass overclosed", errors)
    expect(readiness.get("post_pi_external_source_row_imported") is True, "post-Pi import not closed", errors)
    expect(readiness.get("post_pi_external_replay_ready") is True, "post-Pi replay not ready", errors)
    expect(readiness.get("readiness_fraction") == "8/9", "readiness fraction mismatch", errors)
    expect(readiness.get("present_count") == 8, "present count mismatch", errors)
    expect(readiness.get("requirement_count") == 9, "requirement count mismatch", errors)
    expect(
        readiness.get("only_remaining_readiness_blocker") == "no_knob_value_derivation",
        "wrong remaining blocker",
        errors,
    )
    expect(readiness.get("closed_value_obligation_rows_at_internal_no_knob_tier") == 0, "internal obligations overclosed", errors)
    expect(readiness.get("closed_value_obligation_rows_at_admitted_external_tier") == 4, "external obligation count mismatch", errors)
    expect(readiness.get("obligation_count") == 5, "obligation count mismatch", errors)
    for key in ["full_no_knob_closed", "true_SM_equivalence_closed", "closure_claimed"]:
        expect(readiness.get(key) is False, f"readiness overclosed: {key}", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_INTERNAL_NOKNOB_VALUE_DERIVATION_OR_SOURCE_ANCHOR",
        "cutset status mismatch",
        errors,
    )
    closes = cutset.get("what_closes_now", {})
    for key in [
        "old_no_external_import_status_reconciled_with_post_pi_chain",
        "accepted_external_threshold_rows_imported_at_admitted_replay_tier",
        "accepted_external_mass_scheme_rows_imported_at_admitted_replay_tier",
        "accepted_diagonal_profile_theorem_imported_at_admitted_replay_tier",
        "step4_external_import_lane_closed",
        "observed_constants_excluded_as_selectors",
    ]:
        expect(closes.get(key) is True, f"cutset close flag missing: {key}", errors)
    remains = cutset.get("what_remains_open", {})
    for key in [
        "selected_internal_Rtheta_threshold_response_row",
        "selected_internal_value_emission",
        "coefficient_functional",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure_without_external_replay",
        "candidate_specific_universal_source_anchor_theorem",
        "full_no_knob_closure",
        "true_SM_equivalence_closure",
    ]:
        expect(remains.get(key) is True, f"cutset open flag missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "external_import_lane_closed_at_admitted_replay_tier",
        "accepted_external_source_row_imported",
        "accepted_diagonal_profile_theorem_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure flag missing: {key}", errors)
    expect(closure.get("accepted_external_threshold_row_count") == 7, "candidate threshold count mismatch", errors)
    expect(closure.get("accepted_external_mass_scheme_row_count") == 3, "candidate mass count mismatch", errors)
    for key in [
        "internal_selected_Rtheta_value_row_emitted",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(closure.get("selected_internal_value_emission_count") == 0, "candidate selected emissions overclosed", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate coefficient values overclosed", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    expect("external import lane, admitted replay tier : closed" in note, "note missing external closure", errors)
    expect("internal selected Rtheta value rows         : 0" in note, "note missing internal guard", errors)
    expect("Rtheta readiness                            : 8/9" in note, "note missing readiness", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Threshold response import audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Threshold response import audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
