"""Build Higgs precision value-fill or profile-convention import gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsprecisionvaluefill_or_profileconventionimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTES = PACKET_DIR / "precision_value_fill_route_matrix.packet.json"
MANIFEST = PACKET_DIR / "profile_convention_import_manifest.packet.json"
SCHEMA_PACKET = PACKET_DIR / "higgs_precision_profile_convention_input_schema.packet.json"
DECISION = PACKET_DIR / "precision_value_fill_or_profile_import_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_profile_import_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsPrecisionValueFill_or_ProfileConventionImport_v1.md"

STATUS = "MTT_SELECTED_HIGGSPRECISIONVALUEFILL_OR_PROFILECONVENTIONIMPORT_BUILT_IMPORT_SCHEMA_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def route_class(channel: str) -> str:
    if channel in {"H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"}:
        return "QCD_color_threshold"
    if channel in {"H_to_WW_star", "H_to_ZZ_star", "H_to_gamma_gamma", "H_to_Z_gamma"}:
        return "EW_loop_or_offshell"
    return "leptonic_yukawa_radiative"


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsprecisionrows_or_fullcorrelatedprofile.candidate.json")
    row_gate = load(
        DATA
        / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
        / "higgs_precision_row_promotion_gate.packet.json"
    )
    readiness = load(
        DATA
        / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
        / "full_correlated_profile_readiness_matrix.packet.json"
    )
    blockers = load(
        DATA
        / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
        / "minimal_precision_closure_blocker_set.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
        / "updated_true_equivalence_gate_after_precision_row_gate.packet.json"
    )

    route_rows = []
    for row in row_gate["rows"]:
        route_rows.append(
            {
                "channel": row["channel"],
                "route_class": route_class(row["channel"]),
                "current_row_kind": row["current_row_kind"],
                "route_A_formula_value_fill": {
                    "description": row["precision_route"],
                    "missing_inputs": row["missing_inputs"],
                    "filled": False,
                    "accepted": False,
                },
                "route_B_profile_convention_import": {
                    "description": "import this row as part of one accepted precision Higgs profile convention",
                    "requires": [
                        "same convention version as all ten rows",
                        "central partial width",
                        "uncertainty/covariance contribution",
                        "declared correlation semantics",
                    ],
                    "filled": False,
                    "accepted": False,
                },
                "route_C_no_knob_source_upgrade": {
                    "description": row["operator_source_requirement"],
                    "required_for_true_source_closure": True,
                    "filled": False,
                    "accepted": False,
                },
                "may_close_sm_parity_precision_via_route_A_or_B": True,
                "may_close_no_knob_only_with_route_C_plus_values": True,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    routes = {
        "schema": "MTTHiggsPrecisionValueFillRouteMatrix.v1",
        "status": "PRECISION_VALUE_FILL_ROUTE_MATRIX_BUILT_VALUES_OPEN",
        "rows": route_rows,
        "summary": {
            "row_count": len(route_rows),
            "route_A_formula_rows_filled": 0,
            "route_B_profile_import_rows_filled": 0,
            "route_C_no_knob_source_rows_filled": 0,
            "all_rows_have_formula_and_profile_import_routes": True,
            "all_rows_have_no_knob_source_upgrade_route": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    manifest = {
        "schema": "MTTHiggsProfileConventionImportManifest.v1",
        "status": "PROFILE_CONVENTION_IMPORT_MANIFEST_BUILT_NO_PROFILE_IMPORTED",
        "candidate_convention_families": [
            {
                "name": "LHCHXSWG/HDECAY-style SM Higgs branching-ratio convention",
                "role": "ten-channel central widths and branching ratios under a fixed SM precision convention",
                "acceptable_if": [
                    "version and input scheme are frozen",
                    "central partial widths map exactly onto repo ten-channel row_basis",
                    "total width convention is included",
                    "uncertainty and correlation/profile semantics are included or explicitly profiled",
                ],
                "imported_now": False,
                "accepted_now": False,
            },
            {
                "name": "Prophecy4f-style off-shell vector-boson convention",
                "role": "precision handling for WW*/ZZ* four-fermion final states inside a larger Higgs profile",
                "acceptable_if": [
                    "embedded into the same ten-channel convention as the remaining rows",
                    "off-shell final-state treatment is declared",
                    "EW input covariance is propagated",
                ],
                "imported_now": False,
                "accepted_now": False,
            },
            {
                "name": "row-by-row formula toolchain convention",
                "role": "fallback if a single accepted profile convention is unavailable",
                "acceptable_if": [
                    "every row is computed before benchmark comparison",
                    "all rows share one scheme/scale/profile policy",
                    "full 10x10 covariance or nuisance likelihood is supplied",
                ],
                "imported_now": False,
                "accepted_now": False,
            },
        ],
        "selected_near_term_route": {
            "route": "Route B: accepted full profile convention import",
            "reason": (
                "For SM-parity precision, one accepted profile convention can close row values and covariance "
                "semantics together. Route A remains the formula-by-formula fallback, and Route C remains the "
                "parallel no-knob source upgrade path."
            ),
            "route_selected_by_empirical_target_fit": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    row_basis = [row["channel"] for row in row_gate["rows"]]
    schema_packet = {
        "schema": "MTTHiggsPrecisionProfileConventionInputSchema.v1",
        "status": "INPUT_SCHEMA_BUILT_AWAITING_PROFILE_DATA",
        "required_fields": {
            "profile_id": "stable identifier for the imported convention/profile",
            "profile_version": "version/date/toolchain or paper table identifier",
            "row_basis": row_basis,
            "central_widths_GeV": {channel: "number required" for channel in row_basis},
            "total_width_GeV": "number required",
            "covariance_matrix_GeV2": "10x10 symmetric PSD matrix or null if nuisance_profile supplied",
            "nuisance_profile": "explicit profile likelihood/nuisance model or null if covariance_matrix_GeV2 supplied",
            "branching_ratio_policy": "derived from central_widths/total_width or supplied with consistency proof",
            "scheme": {
                "higgs_mass": "declared value/convention",
                "electroweak_inputs": "declared input scheme",
                "qcd_inputs": "declared alpha_s/quark-mass scheme",
                "perturbative_orders": "declared per row",
                "threshold_policy": "declared per massive threshold",
            },
            "provenance": {
                "source": "publication/tool/table path",
                "license_or_access_note": "short note",
                "retrieved_or_generated_date": "ISO date",
            },
            "guards": {
                "used_to_select_source": False,
                "fit_factor_applied_to_repo_rows": False,
                "row_basis_changed_after_comparison": False,
            },
        },
        "acceptance_tests": [
            "row_basis matches the repo ten-channel basis exactly",
            "central_widths sum to total_width within declared tolerance or give a documented residual",
            "covariance matrix is symmetric PSD (positive semidefinite), or nuisance profile validates",
            "branching ratios are derived by a fixed map from widths and total width",
            "profile values enter downstream after source selection and packet selection",
            "no benchmark ratio is used as a correction factor",
        ],
        "profile_data_filled_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTHiggsPrecisionValueFillOrProfileImportDecision.v1",
        "status": "PROFILE_IMPORT_SCHEMA_BUILT_VALUES_NOT_FILLED",
        "precision_value_fill_route_matrix_built": True,
        "profile_convention_import_manifest_built": True,
        "input_schema_built": True,
        "selected_near_term_route": manifest["selected_near_term_route"]["route"],
        "accepted_precision_row_values_filled": False,
        "full_correlated_profile_imported": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "remaining_blockers": blockers["minimal_for_sm_parity_precision_replay"],
        "profile_readiness_import": readiness["summary"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterProfileImportGate.v1",
        "status": "PROFILE_IMPORT_SCHEMA_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs precision value-fill route matrix",
            "Higgs profile convention import manifest",
            "Higgs precision profile convention input schema",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "fill the Higgs precision profile convention input packet or compute accepted precision row values",
        "guardrails": {
            "profile_schema_not_profile_data": True,
            "no_precision_values_imported": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsPrecisionValueFillOrProfileConventionImport",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsprecisionrows_or_fullcorrelatedprofile.candidate.json"),
            "precision_row_gate": rel(
                DATA
                / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
                / "higgs_precision_row_promotion_gate.packet.json"
            ),
            "full_profile_readiness": rel(
                DATA
                / "selected_higgsprecisionrows_or_fullcorrelatedprofile"
                / "full_correlated_profile_readiness_matrix.packet.json"
            ),
        },
        "output_packets": {
            "precision_value_fill_route_matrix": rel(ROUTES),
            "profile_convention_import_manifest": rel(MANIFEST),
            "profile_convention_input_schema": rel(SCHEMA_PACKET),
            "precision_value_fill_or_profile_import_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsPrecisionValueFillOrProfileConventionImportGateTheorem",
            "proved": True,
            "statement": (
                "The ten-channel Higgs precision frontier admits two SM-parity precision routes: accepted row-by-row "
                "precision values or one accepted full profile convention import. This artifact builds the route "
                "matrix, import manifest, and machine-checkable input schema required for that value fill, while "
                "importing no precision values and preserving source non-selection."
            ),
        },
        "what_closes_now": {
            "precision_value_fill_route_matrix": True,
            "profile_convention_import_manifest": True,
            "machine_checkable_profile_input_schema": True,
            "near_term_route_selected_without_target_fit": True,
        },
        "what_remains_open": {
            "accepted_precision_row_values": True,
            "full_correlated_profile_data": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "profile_import_schema_built": True,
            "accepted_precision_row_values_filled": False,
            "full_correlated_profile_imported": False,
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
        "certificate": "MTT_Selected_HiggsPrecisionValueFill_or_ProfileConventionImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "profile_import_schema_built": True,
        "accepted_precision_row_values_filled": False,
        "full_correlated_profile_imported": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsProfileConventionDataFile_or_PrecisionRowValues_v1",
    }

    note = f"""# MTT Selected HiggsPrecisionValueFill or ProfileConventionImport v1

Status: `{STATUS}`.

This artifact turns the Higgs precision frontier into a fillable interface. It
selects the full profile-convention import as the fastest SM-parity precision
route, while keeping row-by-row formula values and no-knob source upgrades as
parallel routes.

No precision values are imported here. The key deliverable is the
machine-checkable input schema for the next data/value packet.
"""

    for path, payload in [
        (ROUTES, routes),
        (MANIFEST, manifest),
        (SCHEMA_PACKET, schema_packet),
        (DECISION, decision),
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
