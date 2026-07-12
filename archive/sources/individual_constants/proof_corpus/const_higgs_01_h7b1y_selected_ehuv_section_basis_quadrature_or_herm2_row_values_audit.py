"""Audit CONST-HIGGS-01 H7B1Y selected E_H^UV payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
HUNT = BASE / "payload_search_manifest.packet.json"
SECTION_SCHEMA = BASE / "ehuv_section_basis_quadrature_schema.packet.json"
DIRECT_SCHEMA = BASE / "direct_herm2_huv_row_schema.packet.json"
OVERALL = BASE / "overall_achievement_and_remaining_parts.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1Y_SelectedEHUvSectionBasisQuadratureOrHerm2Rows_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1Y_PAYLOAD_HUNT_COMPLETE_SCHEMAS_EMITTED_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1Z_FillEHUvFiniteBasisOrHerm2Values_v1"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_false(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is False, f"{name} expected false: {key}")


def require_all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} expected true: {key}")


def require_nested_none(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        if isinstance(value, dict):
            require_nested_none(value, f"{name}.{key}")
        else:
            require(value is None, f"{name}.{key} emitted value")


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
    hunt = load(HUNT)
    section_schema = load(SECTION_SCHEMA)
    direct_schema = load(DIRECT_SCHEMA)
    overall = load(OVERALL)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("hunt", hunt),
        ("section_schema", section_schema),
        ("direct_schema", direct_schema),
        ("overall", overall),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["name"] == "H7B1YPayloadHuntAndSchemaTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    for key in [
        "payload_hunt_executed",
        "exact_payload_atoms_classified",
        "section_basis_quadrature_schema_emitted",
        "direct_Herm2_schema_emitted",
        "overall_report_emitted",
        "ordered_Hu_Hd_channel_scaffold_closed",
        "E_H_UV_exact_sequence_scaffold_closed",
        "bridge_validator_first_clause_filled",
    ]:
        require(candidate[key] is True, f"candidate missing {key}")
    for key in [
        "selected_E_H_UV_section_basis_emitted",
        "selected_HYM_metric_or_connection_emitted",
        "quadrature_weights_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "Higgs_projection_measure_equality_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(candidate["selected_next_artifact"] == NEXT_ARTIFACT, "next artifact")

    require(hunt["status"] == "H7B1Y_PAYLOAD_HUNT_EXECUTED_VALUES_NOT_FOUND", "hunt status")
    require_all_true(hunt["closed_support_retained"], "hunt support")
    require(len(hunt["payload_atoms"]) == 5, "atom count")
    for atom_name, atom in hunt["payload_atoms"].items():
        require(atom["found"] is False, f"atom found unexpectedly {atom_name}")
        require(atom["required"], f"atom missing required text {atom_name}")
        require(atom["blocker"], f"atom missing blocker text {atom_name}")
    require_all_false(hunt["search_verdict"], "hunt verdict")
    require(len(hunt["why_this_is_not_a_repeat"]) == 4, "nonrepeat count")

    require(
        section_schema["status"] == "SELECTED_EHUV_SECTION_BASIS_QUADRATURE_SCHEMA_EMITTED_VALUES_OPEN",
        "section status",
    )
    require(section_schema["known_scaffold"]["ordered_basis_labels"] == ["H_u", "H_d^dagger"], "section labels")
    require(section_schema["acceptance_booleans"]["ordered_Hu_Hd_labels_closed"] is True, "section scaffold")
    for key, value in section_schema["acceptance_booleans"].items():
        if key != "ordered_Hu_Hd_labels_closed":
            require(value is False, f"section overclosed {key}")
    require_nested_none(section_schema["required_fields"], "section required")

    require(direct_schema["status"] == "DIRECT_HERM2_HUV_ROW_SCHEMA_EMITTED_VALUES_OPEN", "direct status")
    require(direct_schema["basis"] == ["H_u", "H_d^dagger"], "direct labels")
    require("B_Huv^* M_source B_Huv" in direct_schema["accepted_formula"], "direct formula")
    require_nested_none(direct_schema["required_fields"], "direct required")
    require_all_false(direct_schema["acceptance_booleans"], "direct acceptance")

    require(overall["status"] == "OVERALL_FRONTIER_REPORT_EMITTED_AFTER_H7B1Y", "overall status")
    require(len(overall["achieved"]) == 8, "achieved count")
    labels = {entry["label"] for entry in overall["remaining_parts"]}
    require({"H7B1Z-A", "H7B1Z-B", "H7B1Z-C", "H7B1Z-D", "H7B2", "NO-KNOB-GUARD"} <= labels, "remaining labels")
    require(overall["how_close"]["proof_not_closed_yet"] is True, "overall closure")
    require(overall["how_close"]["no_new_Higgs_specific_parameters"] is True, "overall params")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1Y", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    require_all_false(no_cycle["circulation_test"], "circulation")
    require(len(no_cycle["new_information_added"]) == 4, "new info count")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1Z_FILL_EHUV_BASIS_OR_HERM2_VALUES", "next status")
    require(next_work["primary_next"]["artifact"] == NEXT_ARTIFACT, "next artifact packet")
    require(next_work["primary_next"]["label"].endswith("H7B1Z-FILL-EHUV-FINITE-BASIS-OR-HERM2-VALUES"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    require(next_work["superset_strategy"]["combining_paths"] is True, "superset combining")
    require(next_work["superset_strategy"]["using_one_straight_way"] is False, "superset paths")

    require(cert["status"] == STATUS, "cert status")
    require(cert["payload_hunt_executed"] is True, "cert hunt")
    require(cert["exact_payload_atoms_classified"] is True, "cert atoms")
    require(cert["section_basis_quadrature_schema_emitted"] is True, "cert section schema")
    require(cert["direct_Herm2_schema_emitted"] is True, "cert direct schema")
    require(cert["overall_report_emitted"] is True, "cert report")
    for key in [
        "selected_E_H_UV_section_basis_emitted",
        "selected_HYM_metric_or_connection_emitted",
        "quadrature_weights_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(cert[key] is False, f"cert overclosed {key}")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("payload hunt executed                    True" in note, "note hunt")
    require("selected E_H^UV basis found              False" in note, "note basis")
    require("direct Herm2 Huv rows found              False" in note, "note direct")
    require("H7B1Z-FILL-EHUV-FINITE-BASIS-OR-HERM2-VALUES" in note, "note next")

    print("CONST-HIGGS-01 H7B1Y selected E_H^UV payload audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
