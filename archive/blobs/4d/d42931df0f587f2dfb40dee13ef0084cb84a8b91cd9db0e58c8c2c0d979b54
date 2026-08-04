"""Build Higgs external central-profile data or route-A formula row fill."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsexternalprofiledata_or_routeaformularows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CENTRAL_PROFILE = PACKET_DIR / "hybrid_external_central_profile_values.packet.json"
UNCERTAINTY_SIDECAR = PACKET_DIR / "diagonal_uncertainty_sidecar.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_rows_fill_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_central_values.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_central_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsExternalProfileData_or_RouteAFormulaRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSEXTERNALPROFILEDATA_OR_ROUTEAFORMULAROWS_BUILT_HYBRID_CENTRAL_VALUES_FULL_PROFILE_OPEN"

TOTAL_WIDTH_GEV = 4.08e-3
TOTAL_WIDTH_REL_UNCERTAINTY = 0.0387

ROW_BASIS = [
    "H_to_bb",
    "H_to_cc",
    "H_to_tau_tau",
    "H_to_mu_mu",
    "H_to_WW_star",
    "H_to_ZZ_star",
    "H_to_gg",
    "H_to_gamma_gamma",
    "H_to_Z_gamma",
    "H_to_ss",
]

BRANCHING_RATIOS = {
    "H_to_bb": 0.575,
    "H_to_cc": 2.90e-2,
    "H_to_tau_tau": 6.30e-2,
    "H_to_mu_mu": 2.19e-4,
    "H_to_WW_star": 0.216,
    "H_to_ZZ_star": 2.66e-2,
    "H_to_gg": 8.56e-2,
    "H_to_gamma_gamma": 2.28e-3,
    "H_to_Z_gamma": 1.55e-3,
    "H_to_ss": 2.114e-4,
}

REL_UNCERTAINTIES = {
    "H_to_bb": 0.028,
    "H_to_cc": 0.122,
    "H_to_tau_tau": 0.0605,
    "H_to_mu_mu": 0.0635,
    "H_to_WW_star": 0.0475,
    "H_to_ZZ_star": 0.0475,
    "H_to_gg": 0.1045,
    "H_to_gamma_gamma": 0.0535,
    "H_to_Z_gamma": 0.0935,
    "H_to_ss": math.sqrt(0.0073**2 + 0.0702**2 + 0.0211**2),
}

PROVENANCE = {
    "primary_12509_table": {
        "source": "LHCHXSWG CERN Yellow Report 3 interpolation page for M_H=125.09 GeV",
        "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAtMH12509_2014",
        "retrieved_or_generated_date": "2026-05-31",
        "rows": [
            "H_to_bb",
            "H_to_cc",
            "H_to_tau_tau",
            "H_to_mu_mu",
            "H_to_WW_star",
            "H_to_ZZ_star",
            "H_to_gg",
            "H_to_gamma_gamma",
            "H_to_Z_gamma",
        ],
        "note": "The page reports BR values and relative uncertainties interpolated from CERN Report 3 numbers, and reports Gamma_H=4.08 MeV.",
    },
    "strange_row_update": {
        "source": "LHCHWG-2025-008 Higgs-Boson Decays update, Table 1 strange-Yukawa row at M_H=125.09 GeV",
        "url": "https://cds.cern.ch/record/2939000/files/LHCHWG-2025-008.pdf",
        "retrieved_or_generated_date": "2026-05-31",
        "rows": ["H_to_ss"],
        "note": "Used only to fill the repo's explicit H_to_ss central row; this makes the packet hybrid rather than a single accepted correlated profile.",
    },
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def central_widths() -> dict[str, float]:
    return {channel: BRANCHING_RATIOS[channel] * TOTAL_WIDTH_GEV for channel in ROW_BASIS}


def diagonal_covariance(widths: dict[str, float]) -> list[list[float]]:
    matrix: list[list[float]] = []
    for row_channel in ROW_BASIS:
        matrix_row = []
        for col_channel in ROW_BASIS:
            if row_channel == col_channel:
                sigma = widths[row_channel] * REL_UNCERTAINTIES[row_channel]
                matrix_row.append(sigma * sigma)
            else:
                matrix_row.append(0.0)
        matrix.append(matrix_row)
    return matrix


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsexternalprofilepacketfill_or_rowformulavalues.candidate.json")
    slot = load(
        DATA
        / "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
        / "external_profile_packet_slot.packet.json"
    )
    route_a_slots = load(
        DATA
        / "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
        / "route_a_row_formula_value_slots.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
        / "updated_true_equivalence_gate_after_external_profile_slots.packet.json"
    )

    widths = central_widths()
    tracked_width_sum = sum(widths.values())
    tracked_br_sum = sum(BRANCHING_RATIOS.values())
    residual_width = TOTAL_WIDTH_GEV - tracked_width_sum
    residual_br = 1.0 - tracked_br_sum
    covariance = diagonal_covariance(widths)

    central_profile = {
        "schema": "MTTHiggsHybridExternalCentralProfileValues.v1",
        "status": "HYBRID_EXTERNAL_CENTRAL_VALUES_FILLED_FULL_PROFILE_NOT_ACCEPTED",
        "profile_id": "LHCHXSWG_CYR3_MH12509_plus_LHCHWG2025_ss_central_hybrid",
        "profile_version": "retrieved_2026-05-31",
        "row_basis": ROW_BASIS,
        "total_width_GeV": TOTAL_WIDTH_GEV,
        "total_width_source_value": "Gamma_H=4.08 MeV",
        "total_width_relative_uncertainty": TOTAL_WIDTH_REL_UNCERTAINTY,
        "central_branching_ratios": BRANCHING_RATIOS,
        "central_widths_GeV": widths,
        "tracked_branching_ratio_sum": tracked_br_sum,
        "tracked_width_sum_GeV": tracked_width_sum,
        "documented_residual_branching_ratio": residual_br,
        "documented_residual_width_GeV": residual_width,
        "branching_ratio_policy": "central widths are derived by Gamma_i = BR_i * Gamma_H; BR replay is BR_i = Gamma_i / Gamma_H",
        "scheme": {
            "higgs_mass": "M_H=125.09 GeV for primary rows; H_to_ss imported from LHCHWG-2025-008 at M_H=125.09 GeV",
            "electroweak_inputs": "LHCHXSWG/CERN Yellow Report convention",
            "qcd_inputs": "LHCHXSWG/CERN Yellow Report convention; H_to_ss update uses LHCHWG-2025 strange-Yukawa inputs",
            "perturbative_orders": "source-profile convention, not recomputed inside this artifact",
            "threshold_policy": "source-profile convention, not recomputed inside this artifact",
        },
        "provenance": PROVENANCE,
        "filled_now": True,
        "accepted_as_single_correlated_profile": False,
        "accepted_as_downstream_central_replay_seed": True,
        "full_covariance_or_nuisance_profile_supplied": False,
        "hybrid_source_warning": True,
        "guards": {
            "used_to_select_source": False,
            "fit_factor_applied_to_repo_rows": False,
            "row_basis_changed_after_comparison": False,
            "benchmark_ratio_used_as_correction": False,
            "observed_branching_ratios_used_as_formula_inputs": False,
        },
        "source_slot_requirement_satisfied": slot["row_basis"] == ROW_BASIS,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    uncertainty_sidecar = {
        "schema": "MTTHiggsDiagonalUncertaintySidecar.v1",
        "status": "DIAGONAL_UNCERTAINTY_SIDECAR_BUILT_CORRELATED_PROFILE_OPEN",
        "row_basis": ROW_BASIS,
        "relative_uncertainties": REL_UNCERTAINTIES,
        "total_width_relative_uncertainty": TOTAL_WIDTH_REL_UNCERTAINTY,
        "covariance_matrix_GeV2": covariance,
        "is_symmetric": True,
        "is_psd_by_diagonal_nonnegative": True,
        "is_full_correlated_profile": False,
        "correlation_policy": "diagonal sidecar only; full LHCHXSWG nuisance/correlation profile remains open",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_rows = []
    for row in route_a_slots["rows"]:
        route_a_rows.append(
            {
                "channel": row["channel"],
                "slot_id": row["slot_id"],
                "formula_description": row["formula_description"],
                "filled_by_route_A_formula": False,
                "filled_by_external_central_profile": True,
                "accepted_as_route_A_formula_row": False,
                "central_width_GeV_from_external_profile": widths[row["channel"]],
                "fit_factor_applied": False,
                "used_observed_branching_ratio_as_input_to_formula": False,
            }
        )

    route_a_status = {
        "schema": "MTTHiggsRouteAFormulaRowsFillStatus.v1",
        "status": "ROUTE_A_FORMULA_ROWS_UNFILLED_EXTERNAL_CENTRAL_VALUES_AVAILABLE",
        "rows": route_a_rows,
        "summary": {
            "row_count": len(route_a_rows),
            "route_A_formula_rows_filled": 0,
            "external_central_values_filled_for_rows": len(route_a_rows),
            "accepted_route_A_formula_rows": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsPrecisionPromotionAfterCentralValues.v1",
        "status": "CENTRAL_VALUES_READY_FULL_PRECISION_PROFILE_OPEN",
        "external_profile_packet_filled": True,
        "accepted_as_downstream_central_replay_seed": True,
        "accepted_as_single_correlated_profile": False,
        "route_A_formula_values_filled": 0,
        "central_total_width_value_filled": True,
        "central_branching_ratio_values_filled": True,
        "central_widths_derive_from_total_width_and_branching_ratios": True,
        "documented_residual_branching_ratio": residual_br,
        "documented_residual_width_GeV": residual_width,
        "full_correlated_profile_semantics_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "why_not_full_promotion": [
            "The ten-row central vector is hybrid-sourced because H_to_ss comes from a separate LHCHWG update.",
            "Only a diagonal uncertainty sidecar is emitted; no full covariance or nuisance profile is supplied.",
            "Route-A formula rows are not independently computed.",
            "The values are downstream SM-parity replay seeds, not selected MTT source values.",
        ],
        "next_required_action": (
            "either replace the hybrid central packet with one homogeneous accepted correlated profile, or compute "
            "the route-A formula rows and covariance contributions independently under the declared scheme"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsCentralValues.v1",
        "status": "HIGGS_CENTRAL_VALUES_FILLED_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs ten-row central external value vector",
            "Higgs central partial-width replay from total width and branching ratios",
            "Higgs diagonal uncertainty sidecar",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "homogeneous accepted correlated Higgs profile or independent route-A formula values",
        "guardrails": {
            "central_values_filled": True,
            "accepted_as_single_correlated_profile": False,
            "route_A_formula_values_filled": 0,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsExternalProfileDataOrRouteAFormulaRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsexternalprofilepacketfill_or_rowformulavalues.candidate.json"),
            "external_profile_packet_slot": rel(
                DATA
                / "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
                / "external_profile_packet_slot.packet.json"
            ),
            "route_a_row_formula_value_slots": rel(
                DATA
                / "selected_higgsexternalprofilepacketfill_or_rowformulavalues"
                / "route_a_row_formula_value_slots.packet.json"
            ),
        },
        "output_packets": {
            "hybrid_external_central_profile_values": rel(CENTRAL_PROFILE),
            "diagonal_uncertainty_sidecar": rel(UNCERTAINTY_SIDECAR),
            "route_a_formula_rows_fill_status": rel(ROUTE_A_STATUS),
            "higgs_precision_promotion_after_central_values": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsHybridCentralProfileDataFillTheorem",
            "proved": True,
            "statement": (
                "A ten-row Higgs central-value replay vector can be filled from LHCHXSWG-style downstream "
                "external sources without selecting MTT source structure. The vector is sufficient for central "
                "SM-parity replay bookkeeping, but it is not a full precision-profile proof because it is hybrid "
                "sourced, diagonal-only in uncertainty, and not an independent route-A formula computation."
            ),
        },
        "what_closes_now": {
            "higgs_external_central_values_filled": True,
            "higgs_central_partial_widths_replayed": True,
            "higgs_diagonal_uncertainty_sidecar": True,
            "route_A_formula_rows_status_recorded": True,
        },
        "what_remains_open": {
            "homogeneous_accepted_correlated_profile": True,
            "independent_route_A_formula_values": True,
            "full_covariance_or_nuisance_profile": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "central_values_filled": True,
            "accepted_as_downstream_central_replay_seed": True,
            "accepted_as_single_correlated_profile": False,
            "route_A_formula_values_filled": 0,
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
        "certificate": "MTT_Selected_HiggsExternalProfileData_or_RouteAFormulaRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "central_values_filled": True,
        "accepted_as_downstream_central_replay_seed": True,
        "accepted_as_single_correlated_profile": False,
        "route_A_formula_values_filled": 0,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsHomogeneousProfile_or_RouteAFormulaCovariance_v1",
    }

    note = f"""# MTT Selected HiggsExternalProfileData or RouteAFormulaRows v1

Status: `{STATUS}`.

This artifact fills the Higgs ten-row central-value replay vector from
LHCHXSWG-style downstream sources. It derives central partial widths by
`Gamma_i = BR_i * Gamma_H` and records the tracked residual against the total
width.

This is deliberately not promoted to a full precision-profile proof: the packet
is hybrid-sourced, the uncertainty payload is diagonal-only, and no route-A
formula rows are independently computed. The values are downstream SM-parity
replay seeds, not selected MTT source values.
"""

    for path, payload in [
        (CENTRAL_PROFILE, central_profile),
        (UNCERTAINTY_SIDECAR, uncertainty_sidecar),
        (ROUTE_A_STATUS, route_a_status),
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
