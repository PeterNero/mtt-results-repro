"""Audit top/Higgs threshold map rows or external precision table artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tophiggsthresholdmaprows_or_externalprecisiontable"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION_RECHECK = PACKET_DIR / "top_higgs_partial_precision_rows_recheck.packet.json"
MAP_FILL = PACKET_DIR / "top_higgs_threshold_map_row_fill_attempt.packet.json"
EXTERNAL_CONTRACT = PACKET_DIR / "external_precision_table_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_top_higgs_threshold_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TopHiggsThresholdMapRows_or_ExternalPrecisionTable_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TOPHIGGSTHRESHOLDMAPROWS_OR_EXTERNALPRECISIONTABLE_"
    "BUILT_PARTIAL_PRECISION_ROWS_MAPS_OPEN"
)
NEXT = "MTT_Selected_TopHiggsFormulaMapImport_or_RThetaThresholdDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    precision = load(PRECISION_RECHECK)
    fill = load(MAP_FILL)
    external = load(EXTERNAL_CONTRACT)
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
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(
        precision["status"] == "TOP_HIGGS_PARTIAL_PRECISION_ROWS_PRESENT_FULL_PROFILE_OPEN",
        "precision recheck status mismatch",
    )
    require(len(precision["rows"]) == 2, "expected lambda_Mt and y_t_Mt rows")
    row_ids = {row["id"] for row in precision["rows"]}
    require(row_ids == {"lambda_Mt", "y_t_Mt"}, "wrong top/Higgs precision rows")
    require(precision["partial_top_higgs_precision_rows_closed"] is True, "partial rows not closed")
    require(precision["accepted_as_external_precision_target_rows"] is True, "target rows not accepted")
    require(precision["accepted_as_threshold_map_source_rows"] is False, "precision rows overaccepted as source maps")
    require(precision["accepted_as_full_true_equivalence_profile"] is False, "full profile overaccepted")
    require(precision["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")
    require(precision["closure_claimed"] is True, "precision recheck should close locally")

    require(
        fill["status"] == "TOP_HIGGS_MAP_ROW_FILL_ATTEMPTED_NO_MAP_ROWS_ACCEPTED",
        "fill status mismatch",
    )
    require(fill["same_branch_Rtheta_convention_source_theorem_closed"] is False, "same-branch source overclosed")
    require(fill["accepted_precision_threshold_row_count_before"] == 0, "preexisting precision rows overclaimed")
    require(fill["accepted_top_higgs_threshold_map_rows"] == [], "top/Higgs maps overaccepted")
    require(fill["accepted_top_higgs_threshold_map_row_count"] == 0, "top/Higgs map count overclaimed")
    require(fill["partial_precision_rows_may_validate_maps"] is True, "partial rows should validate")
    require(fill["residuals_are_requirements_not_fitted_corrections"] is True, "residual guard missing")
    for requirement in fill["map_requirements"]:
        require(requirement["accepted_as_map_now"] is False, f"map overaccepted: {requirement['id']}")
        require(requirement["blocking_reason"], f"blocking reason missing: {requirement['id']}")
    require(fill["closure_claimed"] is False, "map fill overclosed")

    require(
        external["status"] == "EXTERNAL_PRECISION_TABLE_IMPORT_CONTRACT_BUILT_ROWS_OPEN",
        "external contract status mismatch",
    )
    require(external["current_benchmark_accepted_as_reference"] is True, "benchmark reference missing")
    require(external["current_benchmark_accepted_as_full_precision_match"] is False, "benchmark overaccepted")
    for key in ["lambda_Mt", "y_t_Mt"]:
        require(key in external["current_benchmark_values_available"], f"benchmark value missing: {key}")
    require(len(external["required_for_acceptance_as_map_source"]) == 6, "import requirements changed")
    require(external["accepted_external_precision_table_now"] is False, "external precision table overaccepted")
    require(external["closure_claimed"] is True, "external contract should close locally")

    require(
        cutset["status"] == "NEXT_ATTACK_FORMULA_MAP_IMPORT_OR_RTHETA_THRESHOLD_DERIVATION",
        "cutset status mismatch",
    )
    for key in [
        "top_higgs_partial_precision_rows_rechecked",
        "external_precision_table_import_contract",
        "top_higgs_map_fill_attempt",
        "residuals_kept_as_requirements_not_fits",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "accepted_top_higgs_threshold_map_rows",
        "accepted_external_precision_table_as_map_source",
        "same_branch_Rtheta_convention_source_theorem",
        "full_profile_covariance",
        "bottom_charm_tau_mass_scheme_maps",
        "W_Z_H_electroweak_matching_rows",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    for key in [
        "top_higgs_partial_precision_rows_closed",
        "external_precision_table_import_contract_closed",
        "top_higgs_threshold_map_fill_attempt_closed",
    ]:
        require(closure[key] is True, f"candidate closure flag missing: {key}")
    for key in [
        "accepted_top_higgs_threshold_map_rows_closed",
        "accepted_external_precision_table_as_map_source_closed",
        "same_branch_Rtheta_convention_source_theorem_closed",
        "full_profile_covariance_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["top_higgs_partial_precision_rows_closed"] is True, "certificate partial rows missing")
    require(cert["accepted_top_higgs_threshold_map_row_count"] == 0, "certificate map rows overaccepted")
    require("accepted top/Higgs threshold map rows              : 0" in note, "note missing zero-map line")
    require("lambda_Mt and y_t_Mt partial precision rows closed : true" in note, "note missing partial row line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
