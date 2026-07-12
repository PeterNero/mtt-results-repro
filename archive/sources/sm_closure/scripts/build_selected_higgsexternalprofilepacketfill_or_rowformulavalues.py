"""Build Higgs external-profile packet fill or row-formula value slots."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE_SLOT = PACKET_DIR / "external_profile_packet_slot.packet.json"
ROUTE_A_SLOTS = PACKET_DIR / "route_a_row_formula_value_slots.packet.json"
FILL_STATUS = PACKET_DIR / "external_profile_or_row_values_fill_status.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_external_profile_slots.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsExternalProfilePacketFill_or_RowFormulaValues_v1.md"

STATUS = "MTT_SELECTED_HIGGSEXTERNALPROFILEPACKETFILL_OR_ROWFORMULAVALUES_BUILT_FILL_SLOTS_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def null_widths(row_basis: list[str]) -> dict[str, None]:
    return {channel: None for channel in row_basis}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsacceptedprofileimport_or_rowvaluereplacement.candidate.json")
    replacement = load(
        DATA
        / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
        / "row_value_replacement_controller.packet.json"
    )
    profile_schema = load(
        DATA
        / "selected_higgsprecisionvaluefill_or_profileconventionimport"
        / "higgs_precision_profile_convention_input_schema.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
        / "updated_true_equivalence_gate_after_profile_acceptance_controller.packet.json"
    )

    row_basis = profile_schema["required_fields"]["row_basis"]
    profile_slot = {
        "schema": "MTTHiggsExternalProfilePacketSlot.v1",
        "status": "EXTERNAL_PROFILE_PACKET_SLOT_BUILT_NOT_FILLED",
        "purpose": (
            "Accept one externally versioned Higgs precision profile as a downstream SM-parity replay "
            "payload, after the selected source/interface boundary is fixed."
        ),
        "required_fields": profile_schema["required_fields"],
        "acceptance_tests": profile_schema["acceptance_tests"],
        "row_basis": row_basis,
        "candidate_source_families": [
            "LHCHXSWG/HDECAY-style SM Higgs branching-ratio convention",
            "Prophecy4f-style off-shell vector-boson convention",
            "row-by-row precision formula toolchain convention",
        ],
        "profile_id": None,
        "profile_version": None,
        "scheme": None,
        "provenance": None,
        "total_width_GeV": None,
        "central_widths_GeV": null_widths(row_basis),
        "covariance_matrix_GeV2": None,
        "nuisance_profile": None,
        "branching_ratio_policy": None,
        "filled_now": False,
        "accepted_now": False,
        "guards": {
            "used_to_select_source": False,
            "fit_factor_applied_to_repo_rows": False,
            "row_basis_changed_after_comparison": False,
            "benchmark_ratio_used_as_correction": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_rows = []
    for row in replacement["rows"]:
        route_a_rows.append(
            {
                "channel": row["channel"],
                "slot_id": f"route_A_formula_value::{row['channel']}",
                "replacement_lane": row["replacement_lane"],
                "formula_description": row["route_A_formula_description"],
                "required_payload": {
                    "central_width_GeV": None,
                    "scheme": None,
                    "uncertainty_or_covariance_contribution": None,
                    "provenance": None,
                    "computed_before_comparison": True,
                    "fit_factor_applied": False,
                    "used_observed_branching_ratio_as_input": False,
                },
                "minimum_replacement_payload": row["minimum_replacement_payload"],
                "filled": False,
                "accepted": False,
            }
        )

    route_a_slots = {
        "schema": "MTTHiggsRouteARowFormulaValueSlots.v1",
        "status": "ROUTE_A_ROW_FORMULA_VALUE_SLOTS_BUILT_VALUES_OPEN",
        "rows": route_a_rows,
        "summary": {
            "row_count": len(route_a_rows),
            "filled_count": 0,
            "accepted_count": 0,
            "all_rows_have_formula_slots": len(route_a_rows) == len(row_basis),
            "all_rows_require_precomparison_computation": True,
            "all_rows_forbid_fit_factors": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fill_status = {
        "schema": "MTTHiggsExternalProfileOrRowValuesFillStatus.v1",
        "status": "FILL_SLOTS_BUILT_ACCEPTED_VALUES_OPEN",
        "external_profile_packet_slot_built": True,
        "route_a_row_formula_value_slots_built": True,
        "external_profile_packet_filled": False,
        "external_profile_packet_accepted": False,
        "route_a_values_filled_count": 0,
        "route_a_values_accepted_count": 0,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_action": (
            "populate either the external Higgs precision profile packet with accepted provenance, "
            "scheme, widths, and covariance/profile semantics, or populate every route-A row formula "
            "slot with accepted precomparison values and covariance contributions"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterExternalProfileSlots.v1",
        "status": "EXTERNAL_PROFILE_AND_ROW_FORMULA_SLOTS_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs external precision-profile packet slot",
            "Higgs route-A ten-row formula value slots",
            "Higgs precision fill-status controller for profile-or-row values",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "accepted Higgs precision profile data or accepted route-A formula values",
        "guardrails": {
            "external_profile_slot_built": True,
            "route_a_row_slots_built": True,
            "external_profile_packet_filled": False,
            "route_a_values_accepted_count": 0,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsExternalProfilePacketFillOrRowFormulaValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsacceptedprofileimport_or_rowvaluereplacement.candidate.json"),
            "row_value_replacement_controller": rel(
                DATA
                / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
                / "row_value_replacement_controller.packet.json"
            ),
            "profile_convention_input_schema": rel(
                DATA
                / "selected_higgsprecisionvaluefill_or_profileconventionimport"
                / "higgs_precision_profile_convention_input_schema.packet.json"
            ),
            "previous_true_equivalence_gate": rel(
                DATA
                / "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
                / "updated_true_equivalence_gate_after_profile_acceptance_controller.packet.json"
            ),
        },
        "output_packets": {
            "external_profile_packet_slot": rel(PROFILE_SLOT),
            "route_a_row_formula_value_slots": rel(ROUTE_A_SLOTS),
            "external_profile_or_row_values_fill_status": rel(FILL_STATUS),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsExternalProfilePacketFillOrRowFormulaValuesSlotTheorem",
            "proved": True,
            "statement": (
                "The Higgs precision value gate has been reduced to two executable fill lanes: one accepted "
                "external correlated profile packet, or ten accepted precomparison route-A row formula values "
                "with covariance/profile semantics. The artifact builds those slots and proves that no precision "
                "total width or branching-ratio closure follows until one lane is actually filled and accepted."
            ),
        },
        "what_closes_now": {
            "external_profile_packet_slot": True,
            "route_A_row_formula_value_slots": True,
            "profile_or_row_value_fill_status_controller": True,
            "precision_value_gate_machine_readable": True,
        },
        "what_remains_open": {
            "accepted_external_precision_profile_packet_values": True,
            "accepted_route_A_formula_values": True,
            "full_correlated_profile_semantics": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "external_profile_packet_slot_built": True,
            "route_a_row_formula_value_slots_built": True,
            "external_profile_packet_filled": False,
            "external_profile_packet_accepted": False,
            "accepted_route_A_row_values": 0,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsExternalProfilePacketFill_or_RowFormulaValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_profile_packet_slot_built": True,
        "route_a_row_formula_value_slots_built": True,
        "external_profile_packet_filled": False,
        "external_profile_packet_accepted": False,
        "accepted_route_A_row_values": 0,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsExternalProfileData_or_RouteAFormulaRows_v1",
    }

    note = f"""# MTT Selected HiggsExternalProfilePacketFill or RowFormulaValues v1

Status: `{STATUS}`.

This artifact converts the remaining Higgs precision value gate into two
machine-readable fill lanes:

- an accepted external correlated Higgs precision-profile packet;
- ten accepted route-A row formula values with scheme, provenance, and
  covariance/profile payloads.

No profile values or row formula values are filled or accepted here. Therefore
the precision total width, branching-ratio replay, true SM-equivalence gate, and
no-knob gate all remain open.
"""

    for path, payload in [
        (PROFILE_SLOT, profile_slot),
        (ROUTE_A_SLOTS, route_a_slots),
        (FILL_STATUS, fill_status),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
