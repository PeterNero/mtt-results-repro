"""Audit CONST-HIGGS-01 H6B local source-identity to Higgs-row export gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6b_local_source_identity_to_higgs_row_export"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
LOCAL_EXPORT = BASE / "local_source_identity_to_higgs_row_export.packet.json"
TEMPLATE_LEDGER = BASE / "h4_template_field_ledger_after_h6b.packet.json"
ROW_OBSTRUCTION = BASE / "quartic_row_export_obstruction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6B_LocalSourceIdentityToHiggsRowExport_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6B_LOCAL_SOURCE_IDENTITY_EXPORT_BUILT_HIGGS_ROW_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    local_export = load(LOCAL_EXPORT)
    template_ledger = load(TEMPLATE_LEDGER)
    row_obstruction = load(ROW_OBSTRUCTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("local_export", local_export),
        ("template_ledger", template_ledger),
        ("row_obstruction", row_obstruction),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["local_source_identity_fields_filled"] is True, "source identity")
    require(candidate["local_Higgs_row_export_contract_ready"] is True, "export contract")
    require(candidate["selected_Higgs_amplitude_coordinate"] == 12, "coordinate")
    require(candidate["target_quartic_row_address"] == [12, 12, 12, 12], "row address")
    require(candidate["actual_nonlinear_Higgs_source_rows_emitted"] is False, "source rows overemitted")
    require(candidate["H_sector_fourth_variation_row_emitted"] is False, "H row overemitted")
    require(candidate["projection_on_actual_source_kernel_closed"] is False, "projection overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overclosed")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["lambda_H_coefficient_convention_closed"] is False, "lambda convention")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict no-knob overclosed")
    require(candidate["strict_unpatched_action_kernel_closed"] is False, "strict unpatched")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    scope = local_export["export_scope"]
    require(scope["tier"] == "LOCAL_PREMISE_TIER_ONLY", "scope tier")
    require(scope["accepted_premise"] == "explicit local premise, not unpatched theorem", "accepted premise")
    require(scope["strict_no_knob_tier"] is False, "scope no-knob")
    require(scope["unpatched_theorem_tier"] is False, "scope unpatched")
    exports = local_export["source_identity_exports"]
    require(exports["selected_nonlinear_action_or_PhiFin_source_id"]["filled"] is True, "PhiFin source")
    require(exports["selected_variation_space_id"]["filled"] is True, "variation source")
    require(exports["finite_trace_or_pairing_source_id"]["filled"] is True, "pairing source")
    require(exports["selector_guardrail"]["filled"] is True, "selector guardrail")
    require(exports["G4_normalization_contract"]["filled"] is True, "G4 contract")
    require(exports["G4_normalization_contract"]["new_Higgs_specific_parameters"] == 0, "G4 params")
    require(exports["Higgs_projection_certificate_template"]["filled"] is True, "projection template")
    require(exports["Higgs_projection_certificate_template"]["coordinate_index"] == 12, "projection coordinate")
    require(exports["Higgs_projection_certificate_template"]["quartic_row_address"] == [12, 12, 12, 12], "projection row")
    require(exports["Higgs_projection_certificate_template"]["actual_row_projection"] is False, "actual row projection")
    non_exports = local_export["non_exports"]
    require(non_exports["second_or_fourth_variation_rows"] is False, "variation rows nonexport")
    require(non_exports["H_sector_fourth_variation_row"] is False, "H row nonexport")
    require(non_exports["exactness_or_error_certificate_for_H_row"] is False, "exactness nonexport")
    require(non_exports["lambda_H_style_coefficient_convention"] is False, "lambda convention nonexport")
    require(non_exports["Higgs_quartic_numeric_value"] is False, "numeric nonexport")
    require(local_export["superset_strategy"]["used_as_free_parameter_search"] is False, "superset parameter")
    require(local_export["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "target postcheck")

    ledger_fields = template_ledger["field_status_after_H6B"]
    for key in [
        "G4_normalization_contract",
        "selected_Higgs_zero_mode_or_amplitude_coordinate",
        "Higgs_projection_certificate",
        "selected_nonlinear_action_or_PhiFin_source_id",
        "selected_variation_space_id",
        "finite_trace_or_pairing_source_id",
        "selector_guardrail",
    ]:
        require(ledger_fields[key]["filled"] is True, f"{key} filled")
    require(ledger_fields["Higgs_projection_certificate"]["actual_source_row_projection"] is False, "ledger actual projection")
    require(ledger_fields["second_or_fourth_variation_rows"]["filled"] is False, "ledger variation rows")
    require(ledger_fields["second_or_fourth_variation_rows"]["target_row_address"] == [12, 12, 12, 12], "ledger target row")
    require(ledger_fields["exactness_or_error_certificate"]["filled"] is False, "ledger exactness")
    require(ledger_fields["lambda_H_style_coefficient_convention"]["filled"] is False, "ledger lambda")
    counts = template_ledger["counts"]
    require(counts["filled_required_field_count"] == 7, "filled count")
    require(counts["open_required_field_count"] == 2, "open count")
    require("second_or_fourth_variation_rows" in counts["open_required_fields"], "open rows listed")
    require("exactness_or_error_certificate" in counts["open_required_fields"], "open exactness listed")
    acceptance = template_ledger["acceptance_after_H6B"]
    require(acceptance["local_source_identity_fields_present"] is True, "acceptance source")
    require(acceptance["actual_H_sector_row_fields_present"] is False, "acceptance H rows")
    require(acceptance["all_required_fields_present"] is False, "acceptance all fields")
    require(acceptance["conditional_witness_counts_as_strict_closure"] is False, "conditional strict")

    attempted = row_obstruction["attempted_row"]
    require(attempted["coordinate_index"] == 12, "attempt coordinate")
    require(attempted["quartic_row_address"] == [12, 12, 12, 12], "attempt row")
    require(attempted["row_owner_source_local_tier"] is True, "row owner")
    require(attempted["actual_row_value_emitted"] is False, "row value overemitted")
    why = row_obstruction["why_the_row_does_not_follow_yet"]
    require(why["H6_SI1c_rows_are_source_identity_rows_not_H_sector_fourth_variation_rows"] is True, "SI1c distinction")
    require(why["H5B_row_address_is_a_projection_address_not_a_row_value"] is True, "address distinction")
    require(why["H3_quadratic_stiffness_K2_cannot_be_promoted_to_K4"] is True, "K2/K4 distinction")
    require(why["lambda_H_measured_backsolve_is_forbidden"] is True, "lambda guard")
    missing = row_obstruction["minimal_missing_payload"]
    require("K_H^(4)[12,12,12,12]" in missing["same_source_H_sector_fourth_variation_row"], "missing H row")
    require("H6C-LOCAL-ACTUAL-H-SECTOR-FOURTH-VARIATION-ROW" in next_work["primary_local_tier"]["label"], "next H6C")
    require("H7-UNPATCHED" in next_work["strict_upgrade"]["label"], "next H7")

    require(cert["status"] == STATUS, "cert status")
    require(cert["local_source_identity_fields_filled"] is True, "cert source")
    require(cert["local_Higgs_row_export_contract_ready"] is True, "cert contract")
    require(cert["target_quartic_row_address"] == [12, 12, 12, 12], "cert row")
    require(cert["H_sector_fourth_variation_row_emitted"] is False, "cert H row")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H6B-LOCAL-SOURCE-IDENTITY" in note and "H6C-LOCAL-ACTUAL-H-SECTOR" in note, "note")

    print("CONST-HIGGS-01 H6B local source-identity to Higgs-row export audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
