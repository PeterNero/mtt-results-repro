"""Audit Higgs profile-convention data-file rehearsal and precision-row value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "higgs_profile_convention_datafile_rehearsal.packet.json"
VALIDATION = PACKET_DIR / "profile_datafile_schema_validation.packet.json"
VALUES = PACKET_DIR / "precision_row_value_fill_status.packet.json"
DECISION = PACKET_DIR / "profile_datafile_or_precision_values_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsProfileConventionDataFile_or_PrecisionRowValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSPROFILECONVENTIONDATAFILE_OR_PRECISIONROWVALUES_BUILT_REHEARSAL_PROFILE_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsAcceptedProfileImport_or_RowValueReplacement_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    validation = load(VALIDATION)
    values = load(VALUES)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(profile["status"] == "REHEARSAL_PROFILE_DATAFILE_FILLED_FROM_CURRENT_SCAFFOLD_NOT_PRECISION", "profile status mismatch")
    require(len(profile["row_basis"]) == 10, "row basis count mismatch")
    require(len(profile["central_widths_GeV"]) == 10, "central widths count mismatch")
    require(len(profile["covariance_matrix_GeV2"]) == 10, "covariance row count mismatch")
    require(all(len(row) == 10 for row in profile["covariance_matrix_GeV2"]), "covariance column count mismatch")
    require(abs(sum(profile["central_widths_GeV"].values()) - profile["total_width_GeV"]) < 1e-18, "width sum mismatch")
    require(abs(sum(profile["branching_ratios"].values()) - 1.0) < 1e-12, "branching sum mismatch")
    require(profile["accepted_as_precision_profile_convention"] is False, "profile overaccepted")
    require(profile["accepted_as_precision_row_values"] is False, "row values overaccepted")

    tests = validation["tests"]
    require(tests["row_basis_matches_schema"] is True, "row basis schema validation failed")
    require(tests["central_widths_sum_to_total_width"] is True, "sum validation failed")
    require(tests["covariance_symmetric"] is True, "covariance symmetry failed")
    require(tests["covariance_psd_by_diagonal_nonnegative"] is True, "PSD validation failed")
    require(tests["branching_ratios_derived_by_fixed_map"] is True, "BR map validation failed")
    require(tests["source_selection_guard_passes"] is True, "source guard failed")
    require(tests["fit_factor_guard_passes"] is True, "fit factor guard failed")
    require(tests["precision_convention_acceptance_passes"] is False, "precision acceptance overpassed")
    require(validation["accepted_as_schema_rehearsal"] is True, "schema rehearsal not accepted")
    require(validation["accepted_as_precision_profile_convention"] is False, "validation overaccepted")
    require(len(validation["why_precision_acceptance_fails"]) == 3, "precision failure reasons mismatch")

    require(values["summary"]["row_count"] == 10, "value status row count mismatch")
    require(values["summary"]["rehearsal_values_filled"] == 10, "rehearsal values missing")
    require(values["summary"]["accepted_precision_values_filled"] == 0, "precision values overfilled")
    require(values["summary"]["all_rows_still_require_precision_acceptance"] is True, "precision blocker missing")
    require(all(row["accepted_precision_value_filled"] is False for row in values["rows"]), "row value overaccepted")

    require(decision["profile_datafile_rehearsal_built"] is True, "decision rehearsal missing")
    require(decision["schema_validation_passed_for_rehearsal"] is True, "decision validation missing")
    require(decision["precision_profile_convention_imported"] is False, "decision profile overimported")
    require(decision["accepted_precision_row_values_filled"] is False, "decision row values overfilled")
    require(decision["precision_total_width_closed"] is False, "precision total width overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["profile_datafile_rehearsal_built"] is True, "candidate rehearsal missing")
    require(data["closure_decision"]["precision_profile_convention_imported"] is False, "candidate precision profile overimported")
    require(data["closure_decision"]["accepted_precision_row_values_filled"] is False, "candidate row values overfilled")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not an accepted precision profile" in note, "note missing precision guard")

    for packet in [profile, validation, values, decision, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
