"""Audit R_theta value-source VSD-01 v2 reconciliation or VSD-02 handoff."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff.py"

SLUG = "selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueSource_VSD01v2Reconciliation_or_VSD02Handoff_v1.md"

VSD01_RECHECK = PACKET_DIR / "rtheta_vsd01_v2_reconciliation.packet.json"
FIRST_ROW_RECHECK = PACKET_DIR / "first_value_row_legacy_rejection_recheck.packet.json"
VALUE_FRONTIER = PACKET_DIR / "rtheta_value_source_frontier_after_vsd01_v2.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_v2_reconciliation.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_VALUESOURCE_VSD01V2RECONCILIATION_OR_VSD02HANDOFF_"
    "RETIRED_VSD01_DYNAMIC_ABSENCE_THRESHOLD_RESPONSE_OPEN"
)
NEXT = "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    recheck = load(VSD01_RECHECK)
    first_row = load(FIRST_ROW_RECHECK)
    frontier = load(VALUE_FRONTIER)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail overclaimed: {key}", errors)

    expect(
        recheck.get("status") == "VSD01_SOURCE_DYNAMIC_SUBGATES_RECONCILED_FULL_VALUE_LAYER_OPEN",
        "VSD01 recheck status mismatch",
        errors,
    )
    for key in [
        "source_assembly_subgate_closed",
        "selected_dynamic_tensor_first_response_subgate_closed",
        "same_branch_linking_to_versioned_packet_closed",
        "firstpass_profile_layer_recorded",
        "VSD01_legacy_dynamic_absence_blocker_retired",
    ]:
        expect(recheck.get(key) is True, f"VSD01 subgate should be true: {key}", errors)
    expect(recheck.get("VSD01_full_obligation_closed") is False, "VSD01 full obligation overclosed", errors)
    expect(recheck.get("closure_claimed") is False, "VSD01 recheck overclaimed", errors)

    expect(
        first_row.get("status") == "FIRST_ROW_OLD_SOURCE_PROMOTION_REJECTION_SUPERSEDED_BY_VSD01V2",
        "first row recheck status mismatch",
        errors,
    )
    expect(first_row.get("old_numeric_payload_emitted") is True, "old first row numeric payload missing", errors)
    expect(first_row.get("old_accepted_as_selected_dynamic_value_source_row") is False, "old first row overaccepted", errors)
    expect(first_row.get("old_primitive_exactness_backimported") is True, "primitive exactness missing", errors)
    expect(first_row.get("old_first_row_source_promotion_path_retired") is True, "old first-row path not retired", errors)
    expect(first_row.get("accepted_coefficient_value_count") == 0, "first row accepted coefficients", errors)

    expect(
        frontier.get("status") == "FRONTIER_MOVED_TO_VSD02_THRESHOLD_RESPONSE_OR_EXTERNAL_IMPORT",
        "frontier status mismatch",
        errors,
    )
    expect(frontier.get("VSD01_full_obligation_closed") is False, "frontier VSD01 overclosed", errors)
    for key in [
        "accepted_threshold_matching_values",
        "accepted_mass_scheme_conversion_values",
        "external_threshold_or_likelihood_source_import",
        "multi_loop_threshold_convention_source_rows",
        "no_knob_Yukawa_Higgs_value_source_derivation",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(frontier.get(key) is False, f"frontier overclosed: {key}", errors)
    expect(frontier.get("recommended_next") == NEXT, "frontier next mismatch", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_VSD02_THRESHOLD_RESPONSE_OR_EXTERNAL_LIKELIHOOD_IMPORT",
        "cutset status mismatch",
        errors,
    )
    for key in [
        "VSD01_source_assembly_subgate",
        "VSD01_dynamic_tensor_first_response_subgate",
        "VSD01_same_branch_linking_to_versioned_packet",
        "VSD01_legacy_dynamic_absence_blocker_retired",
    ]:
        expect(cutset.get("closed_now", {}).get(key) is True, f"cutset close flag missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "VSD01_source_assembly_subgate_closed",
        "VSD01_dynamic_tensor_subgate_closed",
        "VSD01_same_branch_linking_closed",
        "VSD01_legacy_dynamic_absence_blocker_retired",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    for key in [
        "VSD01_full_obligation_closed",
        "accepted_threshold_matching_values",
        "accepted_mass_scheme_conversion_values",
        "external_threshold_or_likelihood_source_import",
        "no_knob_Yukawa_Higgs_value_source_derivation",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)
    expect(cert.get("VSD01_legacy_dynamic_absence_blocker_retired") is True, "cert VSD01 retired mismatch", errors)
    expect(cert.get("VSD01_full_obligation_closed") is False, "cert VSD01 full overclosed", errors)

    expect("VSD01 legacy dynamic absence blocker retired   : true" in note, "note missing VSD01 retired", errors)
    expect("VSD01 full value obligation closed             : false" in note, "note missing VSD01 guard", errors)

    if errors:
        print("RTheta VSD01v2 handoff audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta VSD01v2 handoff audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
