"""Audit Yukawa magnitude rows from selected dynamic packet / value-functional gap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SOURCE_IMPORT = BASE / "selected_dynamic_packet_source_import.packet.json"
FAMILY_GAP = BASE / "family_resolved_but_magnitude_functional_gap.packet.json"
MINIMAL_OBJECTS = BASE / "minimal_selected_value_functional_objects.packet.json"
NEXT_PACKET = BASE / "next_after_value_functional_gap.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaMagnitudeRowsFromSelectedDynamicPacket_or_ValueFunctionalGap_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_YUKAWAMAGNITUDEROWSFROMSELECTEDDYNAMICPACKET_OR_"
    "VALUEFUNCTIONALGAP_FAMILY_ROWS_CLOSED_MAGNITUDE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure guard")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    source = load(SOURCE_IMPORT)
    gap = load(FAMILY_GAP)
    objects = load(MINIMAL_OBJECTS)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("source", source),
        ("gap", gap),
        ("objects", objects),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "YukawaMagnitudeValueFunctionalGapTheorem", "theorem name")

    decision = data["closure_decision"]
    for key in [
        "selected_dynamic_packet_imported_for_magnitude_test",
        "family_resolving_operator_closed",
        "all_sectors_family_resolved",
        "sector_aware_projection_skeleton_closed",
        "sector_blind_first_response_magnitude_no_go_proved",
        "universal_sector_scaled_eigenprofile_nogo_proved",
    ]:
        require(decision[key] is True, f"decision true {key}")
    require(decision["accepted_first_dynamic_row_count"] == 2, "first row count")
    for key in [
        "Yukawa_magnitude_value_functional_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "generation_resolved_threshold_source_rows_closed",
        "selected_threshold_response_functional_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "lambda_H_row_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["strict_P_EW_source_rows"] == 0, "strict rows")
    require(decision["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct rows")

    require(source["status"] == "SELECTED_DYNAMIC_PACKET_IMPORTED_FOR_YUKAWA_MAGNITUDE_TEST", "source status")
    require(source["accepted_first_dynamic_row_count"] == 2, "source count")
    require(source["selected_by_MTT"] is True, "selected")
    require(source["same_source_packet_all_fields_selected"] is True, "fields")
    require(source["family_resolving_operator_closed"] is True, "family")
    require(source["all_sectors_family_resolved"] is True, "all family")

    require(gap["status"] == "FAMILY_COORDINATES_CLOSED_MAGNITUDE_FUNCTIONAL_OPEN", "gap status")
    require(gap["family_resolving_operator_closed"] is True, "gap family")
    require(gap["all_sectors_family_resolved"] is True, "gap all sectors")
    require(gap["universal_spectrum_across_sectors"] is True, "universal")
    require(gap["sector_blind_first_response_magnitude_no_go_proved"] is True, "blind nogo")
    require(gap["universal_sector_scaled_eigenprofile_nogo_proved"] is True, "profile nogo")
    require(gap["universal_scaled_profile_can_match_diagnostic_hierarchies"] is False, "profile match")
    require(gap["accepted_Yukawa_magnitudes_as_no_knob_predictions"] is False, "gap magnitudes")
    require(gap["generation_resolved_threshold_source_rows_closed"] is False, "gap thresholds")
    require(len(gap["signed_family_eigenvalues"]) == 3, "signed eigenvalues")
    require(len(gap["abs_family_eigenprofile"]) == 3, "abs eigenprofile")
    require(gap["universal_abs_eigenprofile_ratio"] == 2.0, "ratio")

    require(objects["status"] == "MINIMAL_SELECTED_VALUE_FUNCTIONAL_OBJECTS_EXTRACTED", "objects status")
    require(objects["sector_aware_projection_skeleton_closed"] is True, "objects skeleton")
    require(objects["source_owner_promoted"] is True, "objects owner")
    require(objects["required_charged_generation_row_count"] == 9, "required rows")
    require(objects["accepted_generation_threshold_source_row_count"] == 0, "accepted rows")
    require(objects["lambda_H_row_required"] is True, "lambda required")
    require(objects["same_branch_scale_scheme_loop_convention_closed"] is False, "scheme")
    require(objects["selected_threshold_response_functional_closed"] is False, "threshold")
    require(objects["vsd02_strict_fill_attempt_currently_accepts_rows"] == 0, "vsd02 rows")
    for phrase in [
        "sector-specific higher-response coefficients for u,d,e",
        "or a selected threshold response functional F_s(lambda_g) emitting magnitude rows",
        "or selected threshold/mass-scheme/profile source rows accepted by the VSD02 strict schema",
    ]:
        require(phrase in objects["minimal_new_selected_objects"], f"missing object {phrase}")

    nums = data["key_numbers"]
    require(nums["accepted_first_dynamic_row_count"] == 2, "num first rows")
    require(nums["required_charged_generation_row_count"] == 9, "num required rows")
    require(nums["accepted_generation_threshold_source_row_count"] == 0, "num accepted rows")
    require(nums["universal_abs_eigenprofile_ratio"] == 2.0, "num ratio")
    require(nums["diagnostic_hierarchy_spread"] > 1.0, "hierarchy spread")

    for key in [
        "theorem_proved",
        "family_resolving_operator_closed",
        "all_sectors_family_resolved",
        "sector_aware_projection_skeleton_closed",
        "sector_blind_first_response_magnitude_no_go_proved",
        "universal_sector_scaled_eigenprofile_nogo_proved",
    ]:
        require(cert[key] is True, f"cert true {key}")
    require(cert["accepted_first_dynamic_row_count"] == 2, "cert first count")
    for key in [
        "Yukawa_magnitude_value_functional_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "generation_resolved_threshold_source_rows_closed",
        "selected_threshold_response_functional_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "lambda_H_row_closed",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
    ]:
        require(cert[key] is False, f"cert false {key}")

    for phrase in [
        "YukawaMagnitudeValueFunctionalGapTheorem",
        "family resolving operator closed = true",
        "sector-blind magnitude no-go proved = true",
        "Yukawa magnitude value functional closed = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: selected dynamic rows resolve families, but Yukawa "
        "magnitude closure requires selected sector weights/threshold response."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
