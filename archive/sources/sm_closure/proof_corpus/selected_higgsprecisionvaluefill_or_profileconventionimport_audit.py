"""Audit Higgs precision value-fill/profile convention import gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsprecisionvaluefill_or_profileconventionimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTES = PACKET_DIR / "precision_value_fill_route_matrix.packet.json"
MANIFEST = PACKET_DIR / "profile_convention_import_manifest.packet.json"
SCHEMA_PACKET = PACKET_DIR / "higgs_precision_profile_convention_input_schema.packet.json"
DECISION = PACKET_DIR / "precision_value_fill_or_profile_import_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsPrecisionValueFill_or_ProfileConventionImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSPRECISIONVALUEFILL_OR_PROFILECONVENTIONIMPORT_BUILT_IMPORT_SCHEMA_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsProfileConventionDataFile_or_PrecisionRowValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    routes = load(ROUTES)
    manifest = load(MANIFEST)
    schema_packet = load(SCHEMA_PACKET)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(routes["summary"]["row_count"] == 10, "route row count mismatch")
    require(routes["summary"]["route_A_formula_rows_filled"] == 0, "route A overfilled")
    require(routes["summary"]["route_B_profile_import_rows_filled"] == 0, "route B overfilled")
    require(routes["summary"]["route_C_no_knob_source_rows_filled"] == 0, "route C overfilled")
    require(routes["summary"]["all_rows_have_formula_and_profile_import_routes"] is True, "missing route A/B")
    require(routes["summary"]["all_rows_have_no_knob_source_upgrade_route"] is True, "missing route C")
    require(all(row["route_A_formula_value_fill"]["accepted"] is False for row in routes["rows"]), "route A overaccepted")
    require(all(row["route_B_profile_convention_import"]["accepted"] is False for row in routes["rows"]), "route B overaccepted")
    require(any(row["route_class"] == "QCD_color_threshold" for row in routes["rows"]), "QCD route class missing")
    require(any(row["route_class"] == "EW_loop_or_offshell" for row in routes["rows"]), "EW route class missing")

    require(manifest["status"] == "PROFILE_CONVENTION_IMPORT_MANIFEST_BUILT_NO_PROFILE_IMPORTED", "manifest status mismatch")
    require(len(manifest["candidate_convention_families"]) == 3, "convention family count mismatch")
    require(manifest["selected_near_term_route"]["route"] == "Route B: accepted full profile convention import", "near-term route mismatch")
    require(manifest["selected_near_term_route"]["route_selected_by_empirical_target_fit"] is False, "route selected by fit")
    require(all(family["imported_now"] is False and family["accepted_now"] is False for family in manifest["candidate_convention_families"]), "profile convention overimported")

    required = schema_packet["required_fields"]
    require(schema_packet["profile_data_filled_now"] is False, "schema overfilled")
    require(len(required["row_basis"]) == 10, "schema row basis count mismatch")
    require(set(required["central_widths_GeV"].values()) == {"number required"}, "central width schema malformed")
    require(required["guards"]["used_to_select_source"] is False, "schema source-selection guard missing")
    require(required["guards"]["fit_factor_applied_to_repo_rows"] is False, "schema fit-factor guard missing")
    require(any("PSD" in test for test in schema_packet["acceptance_tests"]), "PSD test missing")
    require(any("source selection" in test for test in schema_packet["acceptance_tests"]), "source-selection test missing")

    require(decision["precision_value_fill_route_matrix_built"] is True, "decision route matrix missing")
    require(decision["profile_convention_import_manifest_built"] is True, "decision manifest missing")
    require(decision["input_schema_built"] is True, "decision schema missing")
    require(decision["accepted_precision_row_values_filled"] is False, "decision values overfilled")
    require(decision["full_correlated_profile_imported"] is False, "decision profile overimported")
    require(decision["precision_total_width_closed"] is False, "precision total width overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["profile_import_schema_built"] is True, "candidate schema missing")
    require(data["closure_decision"]["accepted_precision_row_values_filled"] is False, "candidate values overfilled")
    require(data["closure_decision"]["full_correlated_profile_imported"] is False, "candidate profile overimported")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("No precision values are imported here" in note, "note missing import guard")

    for packet in [routes, manifest, schema_packet, decision, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
