"""Audit Higgs external-profile packet fill or row-formula value slots."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE_SLOT = PACKET_DIR / "external_profile_packet_slot.packet.json"
ROUTE_A_SLOTS = PACKET_DIR / "route_a_row_formula_value_slots.packet.json"
FILL_STATUS = PACKET_DIR / "external_profile_or_row_values_fill_status.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_external_profile_slots.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsExternalProfilePacketFill_or_RowFormulaValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSEXTERNALPROFILEPACKETFILL_OR_ROWFORMULAVALUES_BUILT_FILL_SLOTS_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsExternalProfileData_or_RouteAFormulaRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile_slot = load(PROFILE_SLOT)
    route_a_slots = load(ROUTE_A_SLOTS)
    fill_status = load(FILL_STATUS)
    updated_true = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(profile_slot["status"] == "EXTERNAL_PROFILE_PACKET_SLOT_BUILT_NOT_FILLED", "profile slot status mismatch")
    require(profile_slot["filled_now"] is False, "profile slot overfilled")
    require(profile_slot["accepted_now"] is False, "profile slot overaccepted")
    require(len(profile_slot["row_basis"]) == 10, "profile row basis mismatch")
    require(set(profile_slot["central_widths_GeV"]) == set(profile_slot["row_basis"]), "central widths basis mismatch")
    require(all(value is None for value in profile_slot["central_widths_GeV"].values()), "profile values unexpectedly filled")
    require(profile_slot["total_width_GeV"] is None, "total width unexpectedly filled")
    require(profile_slot["guards"]["used_to_select_source"] is False, "profile selector guard failed")
    require(profile_slot["guards"]["benchmark_ratio_used_as_correction"] is False, "benchmark ratio guard failed")
    require(len(profile_slot["candidate_source_families"]) == 3, "source family inventory mismatch")

    require(route_a_slots["status"] == "ROUTE_A_ROW_FORMULA_VALUE_SLOTS_BUILT_VALUES_OPEN", "route A status mismatch")
    require(route_a_slots["summary"]["row_count"] == 10, "route A row count mismatch")
    require(route_a_slots["summary"]["filled_count"] == 0, "route A rows overfilled")
    require(route_a_slots["summary"]["accepted_count"] == 0, "route A rows overaccepted")
    require(route_a_slots["summary"]["all_rows_have_formula_slots"] is True, "route A formula slots incomplete")
    require(route_a_slots["summary"]["all_rows_require_precomparison_computation"] is True, "precomparison guard missing")
    require(route_a_slots["summary"]["all_rows_forbid_fit_factors"] is True, "fit-factor guard missing")
    require(all(row["filled"] is False and row["accepted"] is False for row in route_a_slots["rows"]), "row slot accepted too early")
    require(
        all(row["required_payload"]["computed_before_comparison"] is True for row in route_a_slots["rows"]),
        "precomparison payload guard failed",
    )
    require(
        all(row["required_payload"]["fit_factor_applied"] is False for row in route_a_slots["rows"]),
        "fit factor payload guard failed",
    )

    require(fill_status["external_profile_packet_slot_built"] is True, "profile slot not recorded")
    require(fill_status["route_a_row_formula_value_slots_built"] is True, "row slots not recorded")
    require(fill_status["external_profile_packet_filled"] is False, "profile status overfilled")
    require(fill_status["external_profile_packet_accepted"] is False, "profile status overaccepted")
    require(fill_status["route_a_values_filled_count"] == 0, "route A status overfilled")
    require(fill_status["route_a_values_accepted_count"] == 0, "route A status overaccepted")
    require(fill_status["precision_total_width_closed"] is False, "precision total overclosed")
    require(fill_status["precision_branching_ratios_closed"] is False, "precision branching overclosed")
    require(fill_status["true_SM_equivalence_closed"] is False, "true equivalence overclosed")

    require(updated_true["guardrails"]["external_profile_slot_built"] is True, "updated true profile guard missing")
    require(updated_true["guardrails"]["route_a_row_slots_built"] is True, "updated true row guard missing")
    require(updated_true["guardrails"]["external_profile_packet_filled"] is False, "updated true overfilled")
    require(updated_true["guardrails"]["route_a_values_accepted_count"] == 0, "updated true overaccepted")

    require(data["closure_decision"]["external_profile_packet_slot_built"] is True, "candidate profile slot missing")
    require(data["closure_decision"]["route_a_row_formula_value_slots_built"] is True, "candidate row slots missing")
    require(data["closure_decision"]["external_profile_packet_filled"] is False, "candidate profile overfilled")
    require(data["closure_decision"]["accepted_route_A_row_values"] == 0, "candidate route A overaccepted")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("No profile values or row formula values are filled or accepted here" in note, "note missing guard")

    for packet in [profile_slot, route_a_slots, fill_status, updated_true, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
