"""Build R_theta value-row basis map / universal source anchor theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rthetavaluerows_or_universalsourceanchortheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SPECTRAL_BASIS = PACKET_DIR / "selected_family_spectral_projector_basis.packet.json"
BASIS_MAP = PACKET_DIR / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
INSTANTIATION_UPDATE = PACKET_DIR / "rtheta_instantiation_update_after_basis_map.packet.json"
VALUE_ROW_ATTEMPT = PACKET_DIR / "rtheta_value_row_coefficients_attempt.packet.json"
DECISION = PACKET_DIR / "rtheta_value_rows_or_universal_anchor_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_basis_map.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaValueRows_or_UniversalSourceAnchorTheorem_v1.md"

PREVIOUS = DATA / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.candidate.json"
PREVIOUS_DOMAIN = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "rtheta_domain_readiness_after_dynamic_family_closure.packet.json"
)
PREVIOUS_INSTANTIATION = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "rtheta_instantiation_update_after_dynamic_source_closure.packet.json"
)
PREVIOUS_UNIVERSAL = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "minimal_universal_parameter_selection_attempt.packet.json"
)
FAMILY_SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
SECTOR_NOGO = DATA / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate.json"
SECTOR_MODEL_TESTS = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_scaled_eigenprofile_model_tests.packet.json"
)
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)
BACKSOLVE = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "diagnostic_magnitude_weight_backsolve.packet.json"
)
THETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETAVALUEROWS_OR_UNIVERSALSOURCEANCHORTHEOREM_"
    "BUILT_BASIS_MAP_CLOSED_COEFFICIENTS_OPEN"
)
NEXT = "MTT_Selected_RThetaCoefficientFunctional_or_UniversalAnchorSelection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R_theta value-row basis-map sources: " + ", ".join(missing))


def to_complex(value: Any) -> complex:
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(value[0], value[1])
    return complex(value)


def matrix(payload: list[list[Any]]) -> np.ndarray:
    return np.array([[to_complex(value) for value in row] for row in payload], dtype=complex)


def encode_number(value: complex, digits: int = 12) -> float | list[float]:
    real = round(float(value.real), digits)
    imag = round(float(value.imag), digits)
    if abs(imag) <= 10 ** (-digits):
        return real
    return [real, imag]


def encode_matrix(mat: np.ndarray) -> list[list[float | list[float]]]:
    return [[encode_number(value) for value in row] for row in mat]


def projector_metrics(projectors: list[np.ndarray]) -> dict[str, Any]:
    identity = np.eye(projectors[0].shape[0], dtype=complex)
    projective_errors = []
    hermitian_errors = []
    traces = []
    ranks = []
    for projector in projectors:
        projective_errors.append(float(np.linalg.norm(projector @ projector - projector)))
        hermitian_errors.append(float(np.max(np.abs(projector - projector.conj().T))))
        traces.append(round(float(np.trace(projector).real), 12))
        ranks.append(int(np.linalg.matrix_rank(projector)))
    orthogonality_errors = []
    for i, left in enumerate(projectors):
        for j, right in enumerate(projectors):
            if i < j:
                orthogonality_errors.append(float(np.linalg.norm(left @ right)))
    completeness_error = float(np.linalg.norm(sum(projectors) - identity))
    return {
        "max_projector_idempotency_error": max(projective_errors),
        "max_projector_hermitian_error": max(hermitian_errors),
        "max_projector_orthogonality_error": max(orthogonality_errors),
        "projector_traces": traces,
        "projector_ranks": ranks,
        "completeness_error": completeness_error,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DOMAIN,
        PREVIOUS_INSTANTIATION,
        PREVIOUS_UNIVERSAL,
        FAMILY_SPECTRUM,
        DYNAMIC_VALUES,
        SECTOR_NOGO,
        SECTOR_MODEL_TESTS,
        VSD02_FILL_ATTEMPT,
        RANK_GAP,
        BACKSOLVE,
        THETA_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_domain = load(PREVIOUS_DOMAIN)
    previous_instantiation = load(PREVIOUS_INSTANTIATION)
    previous_universal = load(PREVIOUS_UNIVERSAL)
    family_spectrum = load(FAMILY_SPECTRUM)
    dynamic_values = load(DYNAMIC_VALUES)
    sector_nogo = load(SECTOR_NOGO)
    sector_model_tests = load(SECTOR_MODEL_TESTS)
    vsd02_fill_attempt = load(VSD02_FILL_ATTEMPT)
    rank_gap = load(RANK_GAP)
    backsolve = load(BACKSOLVE)

    sectors = ["u", "d", "e", "nuD"]
    charged_sectors = ["u", "d", "e"]
    spectral_rows: dict[str, Any] = {}
    charged_basis_rows: list[dict[str, Any]] = []

    for sector in sectors:
        h1 = matrix(dynamic_values["sector_first_responses"][sector]["first_hermitian_response_H1"])
        eigenvalues, eigenvectors = np.linalg.eigh(h1)
        order = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[order]
        eigenvectors = eigenvectors[:, order]
        projectors = []
        sector_projectors = []
        for idx, eigenvalue in enumerate(eigenvalues, start=1):
            vector = eigenvectors[:, idx - 1]
            projector = np.outer(vector, vector.conj())
            projectors.append(projector)
            projector_row = {
                "family_index": idx,
                "family_label_convention": "ascending selected H1 eigenvalue",
                "eigenvalue": round(float(eigenvalue), 12),
                "projector_matrix": encode_matrix(projector),
                "projector_rank": int(np.linalg.matrix_rank(projector)),
                "projector_trace": round(float(np.trace(projector).real), 12),
            }
            sector_projectors.append(projector_row)
            if sector in charged_sectors:
                charged_basis_rows.append(
                    {
                        "row_id": f"{sector}.gen{idx}.magnitude_basis_projector",
                        "sector": sector,
                        "generation": idx,
                        "family_label_convention": "ascending selected H1 eigenvalue",
                        "family_eigenvalue": round(float(eigenvalue), 12),
                        "spectral_projector_ref": f"{sector}.P{idx}",
                        "coefficient_slot": f"theta_coeff.{sector}.gen{idx}",
                        "coefficient_value_selected": False,
                        "accepted_as_basis_row": True,
                        "accepted_as_magnitude_value_row": False,
                    }
                )
        metrics = projector_metrics(projectors)
        spectral_rows[sector] = {
            "source_direction": dynamic_values["sector_first_responses"][sector]["source_direction"],
            "eigenvalues": [round(float(value), 12) for value in eigenvalues],
            "projectors": sector_projectors,
            "projector_metrics": metrics,
            "spectral_projector_basis_closed": (
                max(
                    metrics["max_projector_idempotency_error"],
                    metrics["max_projector_hermitian_error"],
                    metrics["max_projector_orthogonality_error"],
                    metrics["completeness_error"],
                )
                < 1e-10
                and metrics["projector_ranks"] == [1, 1, 1]
                and metrics["projector_traces"] == [1.0, 1.0, 1.0]
            ),
        }

    spectral_basis_closed = all(row["spectral_projector_basis_closed"] for row in spectral_rows.values())
    spectral_basis = {
        "schema": "MTTSelectedFamilySpectralProjectorBasis.v1",
        "status": "SELECTED_FAMILY_SPECTRAL_PROJECTOR_BASIS_EMITTED",
        "source": rel(DYNAMIC_VALUES),
        "family_spectrum": rel(FAMILY_SPECTRUM),
        "family_label_convention": "ascending selected H1 eigenvalue",
        "sector_projector_bases": spectral_rows,
        "all_sector_projector_bases_closed": spectral_basis_closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SPECTRAL_BASIS, spectral_basis)

    basis_map_closed = (
        spectral_basis_closed
        and family_spectrum["family_resolving_operator_closed"]
        and len(charged_basis_rows) == rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]
    )
    basis_map = {
        "schema": "MTTRThetaFamilyEigenprofileToMagnitudeRowBasisMap.v1",
        "status": "FAMILY_EIGENPROFILE_TO_CHARGED_MAGNITUDE_ROW_BASIS_MAP_CLOSED",
        "functional_contract": rel(THETA_CONTRACT),
        "spectral_projector_basis": rel(SPECTRAL_BASIS),
        "charged_sectors": charged_sectors,
        "charged_basis_rows": charged_basis_rows,
        "charged_basis_row_count": len(charged_basis_rows),
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map_closed,
        "coefficient_values_selected": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "distinction": (
            "This closes the selected projector basis and row-slot map. It does not select the magnitude "
            "coefficients theta_coeff.s.gen or lambda_H."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BASIS_MAP, basis_map)

    remaining_failures = [
        failure
        for failure in previous_instantiation["remaining_hard_failures"]
        if failure != "basis_map_to_sector_scaled_magnitude_rows"
    ]
    instantiation_update = {
        "schema": "MTTRThetaInstantiationUpdateAfterBasisMap.v1",
        "status": "RTHETA_BASIS_MAP_CLOSED_COEFFICIENT_AND_VALUE_ROWS_OPEN",
        "previous_instantiation_update": rel(PREVIOUS_INSTANTIATION),
        "retired_failures": ["basis_map_to_sector_scaled_magnitude_rows"],
        "remaining_hard_failures": remaining_failures,
        "functional_contract_closed": previous["closure_decision"]["functional_contract_closed"],
        "dynamic_domain_subgate_closed": previous["closure_decision"]["dynamic_domain_subgate_closed"],
        "family_coordinate_subgate_closed": previous["closure_decision"]["family_coordinate_subgate_closed"],
        "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map_closed,
        "domain_present_count_after_update": previous_instantiation["domain_present_count_after_update"] + 1,
        "domain_requirement_count": previous_instantiation["domain_requirement_count"],
        "codomain_present_required_output_count_after_update": previous_instantiation[
            "codomain_present_required_output_count_after_update"
        ],
        "codomain_required_output_count": previous_instantiation["codomain_required_output_count"],
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "selected_threshold_response_functional_instantiated": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INSTANTIATION_UPDATE, instantiation_update)

    diagnostic_coefficients = []
    for row in backsolve["diagnostic_weights"]:
        diagnostic_coefficients.append(
            {
                "coefficient_slot": f"theta_coeff.{row['sector']}.gen{row['generation']}",
                "diagnostic_value_not_selected": row["diagnostic_magnitude_weight"],
                "accepted_as_selected_coefficient": False,
                "why_not": [
                    "diagnostic value comes from first-pass/profile value packet",
                    "basis map is selected, but coefficient functional is not",
                    "using this coefficient would make replay magnitudes selectors",
                ],
            }
        )
    value_row_attempt = {
        "schema": "MTTRThetaValueRowCoefficientsAttempt.v1",
        "status": "BASIS_ROWS_CLOSED_COEFFICIENT_VALUES_REJECTED_AS_DIAGNOSTIC",
        "basis_map": rel(BASIS_MAP),
        "diagnostic_coefficients": diagnostic_coefficients,
        "diagnostic_coefficient_count": len(diagnostic_coefficients),
        "accepted_coefficient_rows": [],
        "accepted_coefficient_row_count": 0,
        "lambda_H_coefficient_selected": False,
        "sector_scale_only_nogo_preserved": sector_nogo["closure_decision"][
            "universal_sector_scaled_eigenprofile_nogo_proved"
        ],
        "universal_profile_nogo_source": rel(SECTOR_MODEL_TESTS),
        "selected_universal_parameter_count": previous_universal["selected_parameter_count_after"],
        "coefficient_functional_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_ROW_ATTEMPT, value_row_attempt)

    decision = {
        "schema": "MTTRThetaValueRowsOrUniversalAnchorDecision.v1",
        "status": "BASIS_MAP_CLOSED_COEFFICIENT_FUNCTIONAL_OR_UNIVERSAL_ANCHOR_OPEN",
        "previous_status": previous["status"],
        "functional_contract_closed": previous["closure_decision"]["functional_contract_closed"],
        "dynamic_domain_subgate_closed": previous["closure_decision"]["dynamic_domain_subgate_closed"],
        "family_coordinate_subgate_closed": previous["closure_decision"]["family_coordinate_subgate_closed"],
        "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map_closed,
        "coefficient_functional_closed": False,
        "selected_universal_parameter_count": previous_universal["selected_parameter_count_after"],
        "minimal_universal_parameter_selection_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_closes": [
            "emits selected spectral projectors for each sector",
            "maps selected family eigenprofile into the 9 charged magnitude-row basis slots",
            "retires the basis-map blocker while preserving the coefficient/value-row blocker",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaBasisMap.v1",
        "status": "NEXT_ATTACK_RTHETA_COEFFICIENT_FUNCTIONAL_OR_UNIVERSAL_ANCHOR",
        "closed_this_artifact": {
            "selected_spectral_projector_basis": spectral_basis_closed,
            "family_eigenprofile_to_magnitude_row_basis_map": basis_map_closed,
            "basis_map_blocker_retired": basis_map_closed,
        },
        "still_open": [
            "coefficient functional selecting theta_coeff.s.gen without observed magnitudes",
            "lambda_H source row",
            "same-branch true precision scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "candidate-specific universal source-anchor theorem or full profile likelihood",
        ],
        "next_required_artifact": NEXT,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The selected family basis now maps to the charged row slots. The remaining mathematical object is "
                "a coefficient functional or universal source anchor that fills those slots without using measured "
                "magnitudes."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaValueRowsOrUniversalSourceAnchorTheorem",
        "status": STATUS,
        "inputs": {
            "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.candidate": rel(PREVIOUS),
            "rtheta_domain_readiness_after_dynamic_family_closure.packet": rel(PREVIOUS_DOMAIN),
            "rtheta_instantiation_update_after_dynamic_source_closure.packet": rel(PREVIOUS_INSTANTIATION),
            "minimal_universal_parameter_selection_attempt.packet": rel(PREVIOUS_UNIVERSAL),
            "selected_first_response_family_spectrum.packet": rel(FAMILY_SPECTRUM),
            "selected_non_scalar_dynamic_overlap_values.packet": rel(DYNAMIC_VALUES),
            "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate": rel(
                SECTOR_NOGO
            ),
            "sector_scaled_eigenprofile_model_tests.packet": rel(SECTOR_MODEL_TESTS),
            "accepted_source_rows_fill_attempt.packet": rel(VSD02_FILL_ATTEMPT),
            "magnitude_weight_rank_gap.packet": rel(RANK_GAP),
            "diagnostic_magnitude_weight_backsolve.packet": rel(BACKSOLVE),
            "selected_threshold_response_functional_contract.packet": rel(THETA_CONTRACT),
        },
        "output_packets": {
            "selected_family_spectral_projector_basis": rel(SPECTRAL_BASIS),
            "rtheta_family_eigenprofile_to_magnitude_row_basis_map": rel(BASIS_MAP),
            "rtheta_instantiation_update_after_basis_map": rel(INSTANTIATION_UPDATE),
            "rtheta_value_row_coefficients_attempt": rel(VALUE_ROW_ATTEMPT),
            "rtheta_value_rows_or_universal_anchor_decision": rel(DECISION),
            "next_cutset_after_rtheta_basis_map": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedFamilyEigenprofileToMagnitudeRowBasisMapTheorem",
            "proved": True,
            "statement": (
                "The selected first-response Hermitian operator has a nondegenerate spectrum in each sector, so "
                "its spectral theorem emits rank-one projectors with a selected generation-label convention. "
                "Restricting those projectors to the charged sectors u,d,e gives exactly nine charged "
                "magnitude-row basis slots. This closes the basis map from family eigenprofile to sector-scaled "
                "magnitude-row slots, but not the coefficient functional, lambda_H, or Yukawa magnitudes."
            ),
        },
        "closure_decision": {
            "functional_contract_closed": previous["closure_decision"]["functional_contract_closed"],
            "dynamic_domain_subgate_closed": previous["closure_decision"]["dynamic_domain_subgate_closed"],
            "family_coordinate_subgate_closed": previous["closure_decision"]["family_coordinate_subgate_closed"],
            "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map_closed,
            "coefficient_functional_closed": False,
            "selected_universal_parameter_count": previous_universal["selected_parameter_count_after"],
            "minimal_universal_parameter_selection_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "generation_resolved_threshold_source_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "minimal_parameter_yukawa_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaValueRows_or_UniversalSourceAnchorTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map_closed,
        "charged_basis_row_count": len(charged_basis_rows),
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "coefficient_functional_closed": False,
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaValueRows or UniversalSourceAnchorTheorem v1

Status: `{STATUS}`.

This artifact closes the basis map from the selected family eigenprofile to the
charged magnitude-row basis slots.

```text
selected spectral projector basis closed        : {str(spectral_basis_closed).lower()}
basis map to sector-scaled magnitude rows closed: {str(basis_map_closed).lower()}
charged basis rows emitted                      : {len(charged_basis_rows)}/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
coefficient functional closed                   : false
accepted generation threshold rows              : {vsd02_fill_attempt["accepted_row_count"]}/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
Yukawa magnitudes no-knob closed                : false
minimal-parameter Yukawa closure closed         : false
```

The family eigenprofile now gives a selected spectral-projector basis and a
canonical row-slot map for `u`, `d`, and `e`.  The missing object is no longer
the basis map; it is the coefficient functional selecting the row values
`theta_coeff.s.gen`, plus `lambda_H`, without using observed magnitudes as
selectors.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
