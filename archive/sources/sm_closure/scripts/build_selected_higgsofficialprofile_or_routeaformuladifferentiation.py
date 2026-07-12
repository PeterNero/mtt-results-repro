"""Build Higgs official-profile assessment or route-A replay differentiation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsofficialprofile_or_routeaformuladifferentiation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OFFICIAL_ASSESSMENT = PACKET_DIR / "official_profile_import_assessment.packet.json"
REPLAY_JACOBIAN = PACKET_DIR / "total_width_and_branching_ratio_replay_jacobian.packet.json"
PROPAGATED = PACKET_DIR / "propagated_width_and_branching_covariance.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_differentiation_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_replay_differentiation.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_replay_differentiation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsOfficialProfile_or_RouteAFormulaDifferentiation_v1.md"

STATUS = "MTT_SELECTED_HIGGSOFFICIALPROFILE_OR_ROUTEAFORMULADIFFERENTIATION_BUILT_REPLAY_JACOBIAN_FORMULA_DIFF_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a_ik * b[k][j] for k, a_ik in enumerate(a_row)) for j in range(len(b[0]))]
        for a_row in a
    ]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgshomogeneousprofile_or_routeaformulacovariance.candidate.json")
    model = load(
        DATA
        / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
        / "source_derived_correlated_covariance_model.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
        / "updated_true_equivalence_gate_after_higgs_covariance_model.packet.json"
    )

    row_basis = model["row_basis"]
    widths = [float(model["central_widths_GeV"][channel]) for channel in row_basis]
    covariance = model["covariance_matrix_GeV2"]
    total_width = sum(widths)
    branching = [width / total_width for width in widths]

    total_jacobian = [1.0 for _ in row_basis]
    br_jacobian = []
    for i, width_i in enumerate(widths):
        br_jacobian.append(
            [
                ((1.0 if i == j else 0.0) * total_width - width_i) / (total_width * total_width)
                for j in range(len(row_basis))
            ]
        )

    # Combine one total-width row and ten BR rows into an observable Jacobian.
    observable_jacobian = [total_jacobian] + br_jacobian
    observable_covariance = matmul(matmul(observable_jacobian, covariance), transpose(observable_jacobian))
    total_variance = observable_covariance[0][0]
    br_covariance = [row[1:] for row in observable_covariance[1:]]

    official_assessment = {
        "schema": "MTTHiggsOfficialProfileImportAssessment.v1",
        "status": "OFFICIAL_PROFILE_IMPORT_ASSESSED_NOT_FOUND",
        "official_full_profile_imported": False,
        "official_likelihood_or_nuisance_profile_imported": False,
        "homogeneous_ten_row_profile_imported": False,
        "reason": (
            "The repo has central LHCHXSWG-style values and a source-derived covariance model, but no official "
            "machine-readable ten-row covariance/nuisance likelihood packet covering the repo row basis."
        ),
        "accepted_official_profile": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    replay_jacobian = {
        "schema": "MTTHiggsTotalWidthAndBranchingRatioReplayJacobian.v1",
        "status": "TOTAL_WIDTH_AND_BRANCHING_RATIO_REPLAY_JACOBIAN_BUILT",
        "input_width_basis": row_basis,
        "output_observable_basis": ["Gamma_total_tracked"] + [f"BR::{channel}" for channel in row_basis],
        "central_widths_GeV": dict(zip(row_basis, widths)),
        "tracked_total_width_GeV": total_width,
        "tracked_branching_ratios": dict(zip(row_basis, branching)),
        "jacobian_rows": {
            "Gamma_total_tracked": total_jacobian,
            **{f"BR::{channel}": br_jacobian[i] for i, channel in enumerate(row_basis)},
        },
        "map": {
            "total_width": "Gamma_total_tracked = sum_i Gamma_i",
            "branching_ratios": "BR_i = Gamma_i / Gamma_total_tracked",
        },
        "accepted_as_replay_map_differentiation": True,
        "accepted_as_route_A_physics_formula_differentiation": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    propagated = {
        "schema": "MTTHiggsPropagatedWidthAndBranchingCovariance.v1",
        "status": "WIDTH_AND_BRANCHING_COVARIANCE_PROPAGATED_FROM_SOURCE_MODEL",
        "input_partial_width_covariance": rel(
            DATA
            / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
            / "source_derived_correlated_covariance_model.packet.json"
        ),
        "observable_basis": ["Gamma_total_tracked"] + [f"BR::{channel}" for channel in row_basis],
        "tracked_total_width_GeV": total_width,
        "tracked_total_width_variance_GeV2": total_variance,
        "tracked_total_width_sigma_GeV": total_variance**0.5,
        "tracked_branching_ratios": dict(zip(row_basis, branching)),
        "branching_ratio_covariance": br_covariance,
        "full_observable_covariance": observable_covariance,
        "is_symmetric": True,
        "psd_inherited_by_jacobian_congruence": True,
        "accepted_as_propagated_covariance_for_current_source_model": True,
        "accepted_as_official_precision_covariance": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_status = {
        "schema": "MTTHiggsRouteAFormulaDifferentiationStatus.v1",
        "status": "REPLAY_MAP_DIFFERENTIATED_ROUTE_A_PHYSICS_FORMULAS_STILL_OPEN",
        "replay_map_differentiated": True,
        "partial_width_formula_rows_differentiated": 0,
        "route_A_physics_formula_differentiation_closed": False,
        "formula_rows_requiring_differentiation": row_basis,
        "why_route_A_still_open": [
            "The current differentiation acts on the replay map from partial widths to total width and branching ratios.",
            "It does not differentiate the underlying partial-width physics formulas with respect to masses, alpha_s, electroweak inputs, or thresholds.",
            "WW*/ZZ*/Zgamma off-shell rows and rare-loop rows still need declared route-A formula engines.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsPrecisionPromotionAfterReplayDifferentiation.v1",
        "status": "REPLAY_DIFFERENTIATION_READY_PRECISION_PROFILE_AND_FORMULA_DIFF_OPEN",
        "official_profile_imported": False,
        "replay_map_differentiated": True,
        "propagated_covariance_built": True,
        "route_A_physics_formula_differentiation_closed": False,
        "accepted_as_current_source_model_observable_covariance": True,
        "accepted_as_official_precision_profile": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "remaining_gap": (
            "Import an official full Higgs profile/likelihood, or differentiate the actual route-A partial-width "
            "formula engines against declared inputs to replace the source-derived covariance model."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsReplayDifferentiation.v1",
        "status": "HIGGS_REPLAY_DIFFERENTIATION_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs official-profile import assessment",
            "Higgs total-width and branching-ratio replay Jacobian",
            "Higgs propagated observable covariance from current source model",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "official Higgs profile import or route-A partial-width formula differentiation",
        "guardrails": {
            "replay_map_differentiated": True,
            "official_profile_imported": False,
            "route_A_physics_formula_differentiation_closed": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsOfficialProfileOrRouteAFormulaDifferentiation",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgshomogeneousprofile_or_routeaformulacovariance.candidate.json"),
            "source_derived_covariance_model": rel(
                DATA
                / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
                / "source_derived_correlated_covariance_model.packet.json"
            ),
        },
        "output_packets": {
            "official_profile_import_assessment": rel(OFFICIAL_ASSESSMENT),
            "total_width_and_branching_ratio_replay_jacobian": rel(REPLAY_JACOBIAN),
            "propagated_width_and_branching_covariance": rel(PROPAGATED),
            "route_a_formula_differentiation_status": rel(ROUTE_A_STATUS),
            "higgs_precision_promotion_after_replay_differentiation": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsReplayMapDifferentiationTheorem",
            "proved": True,
            "statement": (
                "Given the current source-derived partial-width covariance model, the total-width and branching-ratio "
                "replay map has an explicit Jacobian, and covariance propagates by congruence. This closes replay-map "
                "differentiation for the current model, while official profile import and route-A physics formula "
                "differentiation remain open."
            ),
        },
        "what_closes_now": {
            "official_profile_route_assessed": True,
            "total_width_replay_jacobian": True,
            "branching_ratio_replay_jacobian": True,
            "observable_covariance_propagated_from_current_model": True,
        },
        "what_remains_open": {
            "official_full_Higgs_profile_or_likelihood": True,
            "route_A_partial_width_formula_differentiation": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "replay_map_differentiation_closed": True,
            "official_profile_imported": False,
            "route_A_physics_formula_differentiation_closed": False,
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
        "certificate": "MTT_Selected_HiggsOfficialProfile_or_RouteAFormulaDifferentiation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "replay_map_differentiation_closed": True,
        "official_profile_imported": False,
        "route_A_physics_formula_differentiation_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodImport_v1",
    }

    note = f"""# MTT Selected HiggsOfficialProfile or RouteAFormulaDifferentiation v1

Status: `{STATUS}`.

This artifact does not find or import an official full Higgs likelihood/profile.
Instead it constructs the differentiable replay layer for the current
source-derived covariance model:

- `Gamma_total = sum_i Gamma_i`;
- `BR_i = Gamma_i / Gamma_total`;
- covariance propagates by `J Cov(Gamma) J^T`.

This closes replay-map differentiation only. It does not differentiate the
underlying route-A physics partial-width formulas and does not promote Higgs
precision total-width or branching-ratio closure.
"""

    for path, payload in [
        (OFFICIAL_ASSESSMENT, official_assessment),
        (REPLAY_JACOBIAN, replay_jacobian),
        (PROPAGATED, propagated),
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
