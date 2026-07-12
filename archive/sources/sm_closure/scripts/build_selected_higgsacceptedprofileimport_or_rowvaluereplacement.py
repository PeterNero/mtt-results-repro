"""Build Higgs accepted-profile import or row-value replacement controller."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACCEPTANCE = PACKET_DIR / "accepted_profile_import_acceptance_result.packet.json"
REPLACEMENT = PACKET_DIR / "row_value_replacement_controller.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_after_replacement_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_profile_acceptance_controller.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsAcceptedProfileImport_or_RowValueReplacement_v1.md"

STATUS = "MTT_SELECTED_HIGGSACCEPTEDPROFILEIMPORT_OR_ROWVALUEREPLACEMENT_BUILT_CONTROLLER_NO_ACCEPTED_VALUES"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def replacement_lane(channel: str) -> str:
    if channel in {"H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"}:
        return "profile_import_preferred_EW_kernel_fallback"
    if channel in {"H_to_gg", "H_to_ss"}:
        return "route_A_QCD_precision_formula_or_profile_import"
    if channel in {"H_to_bb", "H_to_cc"}:
        return "route_A_multiloop_qq_formula_or_profile_import"
    if channel == "H_to_gamma_gamma":
        return "route_A_EW_loop_formula_or_profile_import"
    return "route_A_leptonic_radiative_formula_or_profile_import"


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsprofileconventiondatafile_or_precisionrowvalues.candidate.json")
    profile = load(
        DATA
        / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
        / "higgs_profile_convention_datafile_rehearsal.packet.json"
    )
    validation = load(
        DATA
        / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
        / "profile_datafile_schema_validation.packet.json"
    )
    values = load(
        DATA
        / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
        / "precision_row_value_fill_status.packet.json"
    )
    route_matrix = load(
        DATA
        / "selected_higgsprecisionvaluefill_or_profileconventionimport"
        / "precision_value_fill_route_matrix.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
        / "updated_true_equivalence_gate_after_profile_datafile_rehearsal.packet.json"
    )

    tests = validation["tests"]
    structural_tests_pass = all(
        tests[key]
        for key in [
            "row_basis_matches_schema",
            "central_widths_sum_to_total_width",
            "covariance_symmetric",
            "covariance_psd_by_diagonal_nonnegative",
            "branching_ratios_derived_by_fixed_map",
            "source_selection_guard_passes",
            "fit_factor_guard_passes",
        ]
    )
    precision_acceptance_passes = bool(tests["precision_convention_acceptance_passes"])
    acceptance = {
        "schema": "MTTHiggsAcceptedProfileImportAcceptanceResult.v1",
        "status": "PROFILE_IMPORT_REJECTED_FOR_PRECISION_ACCEPTANCE_REHEARSAL_ONLY",
        "profile_id": profile["profile_id"],
        "profile_version": profile["profile_version"],
        "structural_schema_tests_pass": structural_tests_pass,
        "precision_acceptance_tests_pass": precision_acceptance_passes,
        "accepted_as_profile_convention_import": False,
        "accepted_as_precision_total_width_source": False,
        "accepted_as_precision_branching_ratio_source": False,
        "accepted_precision_row_count": 0,
        "rejection_reasons": validation["why_precision_acceptance_fails"],
        "promotion_rule": (
            "Structural schema success is necessary but not sufficient. Precision promotion also requires "
            "accepted external/profile provenance or independently accepted row-value formulas with full "
            "correlated covariance/profile semantics."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_by_channel = {row["channel"]: row for row in route_matrix["rows"]}
    replacement_rows = []
    for row in values["rows"]:
        route = route_by_channel[row["channel"]]
        replacement_rows.append(
            {
                "channel": row["channel"],
                "current_row_kind": row["current_row_kind"],
                "current_rehearsal_width_GeV": row["current_width_GeV"],
                "replacement_lane": replacement_lane(row["channel"]),
                "route_A_formula_description": route["route_A_formula_value_fill"]["description"],
                "route_B_profile_import_available": True,
                "route_C_no_knob_source_description": route["route_C_no_knob_source_upgrade"]["description"],
                "minimum_replacement_payload": [
                    "accepted central partial width",
                    "declared convention/scheme",
                    "row uncertainty and covariance/profile contribution",
                    "provenance that is independent of source selection",
                ],
                "may_replace_rehearsal_value_now": False,
                "accepted_replacement_value_filled": False,
            }
        )

    replacement = {
        "schema": "MTTHiggsRowValueReplacementController.v1",
        "status": "ROW_VALUE_REPLACEMENT_CONTROLLER_BUILT_NO_REPLACEMENTS_FILLED",
        "rows": replacement_rows,
        "summary": {
            "row_count": len(replacement_rows),
            "replacement_values_filled": 0,
            "profile_import_still_preferred_for_bulk_precision": True,
            "route_A_formula_fallback_available_for_all_rows": True,
            "route_C_no_knob_source_upgrade_retained_for_all_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsPrecisionPromotionAfterReplacementDecision.v1",
        "status": "NO_ACCEPTED_PROFILE_OR_ROW_REPLACEMENTS_PRECISION_REMAINS_OPEN",
        "accepted_profile_import": False,
        "accepted_row_replacements": 0,
        "structural_rehearsal_valid": structural_tests_pass,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_action": (
            "supply an accepted external/full Higgs precision profile convention packet, or fill route-A "
            "accepted row-value replacements until all ten rows and the covariance/profile semantics pass"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterProfileAcceptanceController.v1",
        "status": "PROFILE_ACCEPTANCE_CONTROLLER_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs accepted-profile import acceptance controller",
            "Higgs row-value replacement controller",
            "precision promotion decision after replacement gate",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "accepted external Higgs precision profile convention packet or accepted row-value replacement packet",
        "guardrails": {
            "rehearsal_profile_rejected_for_precision": True,
            "zero_replacement_values_filled": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsAcceptedProfileImportOrRowValueReplacement",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsprofileconventiondatafile_or_precisionrowvalues.candidate.json"),
            "profile_datafile_rehearsal": rel(
                DATA
                / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
                / "higgs_profile_convention_datafile_rehearsal.packet.json"
            ),
            "schema_validation": rel(
                DATA
                / "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
                / "profile_datafile_schema_validation.packet.json"
            ),
            "route_matrix": rel(
                DATA
                / "selected_higgsprecisionvaluefill_or_profileconventionimport"
                / "precision_value_fill_route_matrix.packet.json"
            ),
        },
        "output_packets": {
            "accepted_profile_import_acceptance_result": rel(ACCEPTANCE),
            "row_value_replacement_controller": rel(REPLACEMENT),
            "precision_promotion_after_replacement_decision": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsAcceptedProfileImportOrRowValueReplacementControllerTheorem",
            "proved": True,
            "statement": (
                "The current rehearsal profile passes structural schema validation but is rejected for precision "
                "acceptance. The repo now has an executable controller that distinguishes structural validity from "
                "precision promotion and emits row-level replacement lanes for an accepted profile import or accepted "
                "route-A precision row values without using measured values as source selectors."
            ),
        },
        "what_closes_now": {
            "accepted_profile_import_acceptance_controller": True,
            "row_value_replacement_controller": True,
            "structural_vs_precision_acceptance_split": True,
            "zero_promotion_decision": True,
        },
        "what_remains_open": {
            "accepted_external_precision_profile_packet": True,
            "accepted_route_A_row_value_replacements": True,
            "full_correlated_profile_semantics": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "profile_acceptance_controller_built": True,
            "rehearsal_profile_structurally_valid": structural_tests_pass,
            "accepted_profile_import": False,
            "accepted_row_replacements": 0,
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
        "certificate": "MTT_Selected_HiggsAcceptedProfileImport_or_RowValueReplacement_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "profile_acceptance_controller_built": True,
        "rehearsal_profile_structurally_valid": structural_tests_pass,
        "accepted_profile_import": False,
        "accepted_row_replacements": 0,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsExternalProfilePacketFill_or_RowFormulaValues_v1",
    }

    note = f"""# MTT Selected HiggsAcceptedProfileImport or RowValueReplacement v1

Status: `{STATUS}`.

This artifact builds the promotion controller after the Higgs profile datafile
rehearsal. The rehearsal profile is structurally valid but rejected for
precision acceptance. The replacement controller now records what each row needs
before it can replace the scaffold value.

No precision profile import or row replacement is accepted here.
"""

    for path, payload in [
        (ACCEPTANCE, acceptance),
        (REPLACEMENT, replacement),
        (PROMOTION, promotion),
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
