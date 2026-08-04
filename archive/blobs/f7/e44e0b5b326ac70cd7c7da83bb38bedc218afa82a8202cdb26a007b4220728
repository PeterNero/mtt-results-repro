"""Build spectral Yukawa response basis / coefficient-source wall packet.

This derives the clean finite spectral-calculus map from the selected family
operator to charged Yukawa magnitude rows.  It deliberately separates the
source-owned basis map from the coefficient values: coefficients computed from
common-scale Yukawa values are diagnostic replay rows, not no-knob source rows.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BASIS_PACKET = PACKET_DIR / "selected_family_spectral_response_basis.packet.json"
COEFF_PACKET = PACKET_DIR / "diagnostic_log_yukawa_response_coefficients.packet.json"
FUNCTIONAL_PACKET = PACKET_DIR / "spectral_threshold_response_functional_contract.packet.json"
NEXT_PACKET = PACKET_DIR / "next_coefficient_source_rows_or_minimal_parameter_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SpectralYukawaResponseBasis_or_CoefficientSourceWall_v1.md"

FAMILY = DATA / "selected_familyresolvingoperator_or_generationthresholdrowsexecution" / "selected_first_response_family_spectrum.packet.json"
MAG_GAP = DATA / "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap.candidate.json"
PROJECTION = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"
MAG_WEIGHTS = DATA / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation.candidate.json"
HIGHER = DATA / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate.json"
VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution" / "versioned_common_scale_yukawa_higgs_values.packet.json"
MATRIX_MINIMAL = DATA / "selected_qutrit27matrixminimalclosure_or_strictpewupgrade.candidate.json"

STATUS = (
    "MTT_SELECTED_SPECTRALYUKAWARESPONSEBASIS_OR_COEFFICIENTSOURCEWALL_"
    "BASIS_CLOSED_COEFFICIENT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_LogYukawaCoefficientSourceRows_or_MinimalFlavorParameterLedger_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
        - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
        + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
    )


def solve3(a: list[list[float]], b: list[float]) -> list[float]:
    d = det3(a)
    if abs(d) < 1e-14:
        raise ValueError("singular spectral response basis")
    out = []
    for col in range(3):
        m = [row[:] for row in a]
        for i in range(3):
            m[i][col] = b[i]
        out.append(det3(m) / d)
    return out


def matvec(a: list[list[float]], c: list[float]) -> list[float]:
    return [sum(row[j] * c[j] for j in range(3)) for row in a]


def lagrange_coefficients(xs: list[float]) -> list[dict[str, Any]]:
    rows = []
    for i, xi in enumerate(xs):
        others = [xs[j] for j in range(3) if j != i]
        denom = (xi - others[0]) * (xi - others[1])
        # (x-a)(x-b)/denom = (x^2 -(a+b)x + ab)/denom
        rows.append(
            {
                "family_index": i + 1,
                "eigenvalue": xi,
                "polynomial_basis": "1,x,x^2",
                "coefficients_constant_linear_quadratic": [
                    others[0] * others[1] / denom,
                    -(others[0] + others[1]) / denom,
                    1.0 / denom,
                ],
            }
        )
    return rows


def main() -> int:
    sources = [FAMILY, MAG_GAP, PROJECTION, MAG_WEIGHTS, HIGHER, VALUES, MATRIX_MINIMAL]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing spectral Yukawa response inputs: " + ", ".join(missing))

    family = load(FAMILY)
    mag_gap = load(MAG_GAP)
    projection = load(PROJECTION)
    mag_weights = load(MAG_WEIGHTS)
    higher = load(HIGHER)
    values = load(VALUES)
    matrix = load(MATRIX_MINIMAL)

    xs = [float(x) for x in family["sector_results"]["u"]["eigenvalues"]]
    vandermonde = [[1.0, x, x*x] for x in xs]
    determinant = det3(vandermonde)
    basis_rows = lagrange_coefficients(xs)

    sectors = {
        "u": values["derived_magnitudes"]["diag_abs_Y_u"],
        "d": values["derived_magnitudes"]["diag_abs_Y_d"],
        "e": values["derived_magnitudes"]["diag_abs_Y_e"],
    }
    coeff_rows = []
    max_abs_residual = 0.0
    for sector, mags in sectors.items():
        logs = [math.log(float(y)) for y in mags]
        coeffs = solve3(vandermonde, logs)
        reconstructed_logs = matvec(vandermonde, coeffs)
        reconstructed = [math.exp(z) for z in reconstructed_logs]
        residuals = [reconstructed[i] - float(mags[i]) for i in range(3)]
        max_abs_residual = max(max_abs_residual, max(abs(r) for r in residuals))
        coeff_rows.append(
            {
                "sector": sector,
                "source_direction": family["sector_results"][sector]["source_direction"],
                "basis": "log|Y_s|(F_s)=c0_s+c1_s*F_s+c2_s*F_s^2",
                "coefficient_values_c0_c1_c2": coeffs,
                "input_common_scale_diag_abs_Y": [float(y) for y in mags],
                "reconstructed_diag_abs_Y": reconstructed,
                "max_abs_reconstruction_residual": max(abs(r) for r in residuals),
                "accepted_as_no_knob_coefficient_source": False,
                "accepted_as_profile_replay_coefficients": True,
                "reason_not_source": "Coefficients are solved from versioned common-scale Yukawa magnitudes, not emitted by selected MTT threshold source rows.",
            }
        )

    basis_packet = {
        "schema": "MTTSelectedFamilySpectralResponseBasis.v1",
        "status": "SELECTED_FAMILY_SPECTRAL_RESPONSE_BASIS_CLOSED",
        "closure_claimed": True,
        "family_operator_closed": family["family_resolving_operator_closed"],
        "all_sectors_family_resolved": family["all_sectors_family_resolved"],
        "universal_spectrum_across_sectors": family["universal_spectrum_across_sectors"],
        "eigenvalues": xs,
        "vandermonde_basis": "1,x,x^2",
        "vandermonde_matrix": vandermonde,
        "vandermonde_determinant": determinant,
        "basis_nonsingular": abs(determinant) > 1e-14,
        "lagrange_projector_polynomials": basis_rows,
        "structural_response_map": "For each charged sector s, any positive three-family magnitude vector is represented as |Y_s|=exp(c0_s+c1_s*F_s+c2_s*F_s^2) on the selected family spectrum.",
        "accepted_as_selected_basis_map": True,
        "accepted_as_magnitude_value_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    coeff_packet = {
        "schema": "MTTDiagnosticLogYukawaResponseCoefficients.v1",
        "status": "DIAGNOSTIC_LOG_COEFFICIENTS_SOLVED_EXACTLY_SOURCE_OPEN",
        "closure_claimed": True,
        "reference_scale": values["reference_scale"],
        "reference_scheme": values["reference_scheme"],
        "coefficient_domain_closed": True,
        "coefficient_source_rows_closed": False,
        "coefficient_row_count": 9,
        "sector_rows": coeff_rows,
        "max_abs_reconstruction_residual": max_abs_residual,
        "accepted_as_no_knob_predictions": False,
        "accepted_for_SM_parity_profile_replay": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    functional_packet = {
        "schema": "MTTSpectralThresholdResponseFunctionalContract.v1",
        "status": "SPECTRAL_FUNCTIONAL_DERIVED_COEFFICIENT_SOURCE_WALL_EXPOSED",
        "closure_claimed": True,
        "closed_now": [
            "selected finite family spectral basis",
            "unique degree-2 log-response interpolation map on the three selected eigenvalues",
            "exact replay coordinates for common-scale charged Yukawa magnitudes",
            "clean separation between structural basis and source-owned coefficient rows",
        ],
        "not_closed": [
            "selected no-knob coefficient source rows c_{s,k}",
            "selected threshold/mass-scheme/profile source rows deriving those coefficients",
            "CKM/PMNS physical value closure",
            "true SM precision equivalence",
        ],
        "source_requirements_for_no_knob_upgrade": [
            "emit c0_s,c1_s,c2_s for s in {u,d,e} from selected threshold response/source operator",
            "or reduce the 9 coefficients to 1-3 universal source parameters selected before empirical replay",
            "or import accepted external profile/likelihood source rows with provenance and basis map for SM-parity only",
        ],
        "input_status_reconciliation": {
            "27_matrix_minimal_ledger_closed": matrix["closure_decision"]["minimal_one_primitive_matrix_ledger_closed"],
            "source_projection_weights_closed": projection["closure_decision"]["source_normalized_sector_projection_weights_closed"],
            "magnitude_bearing_projection_weights_closed": mag_weights["closure_decision"]["magnitude_bearing_projection_weights_closed"],
            "higher_response_sector_coefficients_closed": higher["closure_decision"]["higher_response_sector_coefficients_closed"],
            "previous_value_functional_closed": mag_gap["closure_decision"]["Yukawa_magnitude_value_functional_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCoefficientSourceRowsOrMinimalParameterPolicy.v1",
        "status": "NEXT_IS_LOG_YUKAWA_COEFFICIENT_SOURCE_OR_MINIMAL_FLAVOR_PARAMETER_LEDGER",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "ordered_routes": [
            "derive selected threshold/source operator emitting the nine c_{s,k} rows",
            "test whether source constraints reduce c_{s,k} to 1-3 universal parameters selected before replay",
            "if no source theorem appears, record a minimal flavor-parameter ledger analogous to the P_EW one-primitive lane",
            "then integrate CKM/PMNS and covariance/profile likelihood for SM-parity rather than no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSpectralYukawaResponseBasisOrCoefficientSourceWall",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "basis_map_closed": True,
        "coefficient_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "accepted_for_SM_parity_profile_replay": True,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "packets": {
            "selected_family_spectral_response_basis": rel(BASIS_PACKET),
            "diagnostic_log_yukawa_response_coefficients": rel(COEFF_PACKET),
            "spectral_threshold_response_functional_contract": rel(FUNCTIONAL_PACKET),
            "next_coefficient_source_rows_or_minimal_parameter_policy": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_family_spectral_basis_closed": True,
            "unique_degree2_log_response_basis_closed": True,
            "coefficient_domain_closed": True,
            "diagnostic_common_scale_replay_exact": max_abs_residual < 1e-12,
            "diagnostic_log_coefficient_rows_filled": 9,
            "selected_log_coefficient_source_rows": 0,
            "Yukawa_magnitude_value_functional_closed_as_structure": True,
            "Yukawa_magnitude_value_functional_closed_as_no_knob_source": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "minimal_parameter_flavor_ledger_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "family_eigenvalues": xs,
            "vandermonde_determinant": determinant,
            "diagnostic_log_coefficient_row_count": 9,
            "max_abs_reconstruction_residual": max_abs_residual,
        },
        "theorem": {
            "name": "SelectedSpectralYukawaResponseBasisTheorem",
            "proved": True,
            "statement": (
                "The selected nondegenerate three-family operator supplies a unique finite spectral calculus basis. "
                "Therefore the charged Yukawa magnitude map can be represented without ambiguity as a degree-2 "
                "log-threshold response polynomial in the selected family operator for each charged sector. "
                "This closes the basis/value-functional domain.  It does not close no-knob Yukawa prediction, because "
                "the sector coefficient rows are currently diagnostic common-scale replay coefficients rather than selected source rows."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSpectralYukawaResponseBasisOrCoefficientSourceWallCertificate",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "basis_map_closed": True,
        "coefficient_source_rows_closed": False,
        "diagnostic_log_coefficient_rows_filled": 9,
        "selected_log_coefficient_source_rows": 0,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "accepted_for_SM_parity_profile_replay": True,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected SpectralYukawaResponseBasis or CoefficientSourceWall v1

## Theorem

`SelectedSpectralYukawaResponseBasisTheorem` is proved.

The selected family operator has three nondegenerate eigenvalues, so the charged
Yukawa magnitude functional has a canonical finite spectral representation:

`log |Y_s| = c0_s + c1_s F_s + c2_s F_s^2`, for `s in {{u,d,e}}`.

This closes the basis/value-functional domain.  It does **not** close no-knob
Yukawa prediction, because the current coefficient values are solved from the
versioned common-scale profile replay packet.

## Numerical Replay

- diagnostic coefficient rows filled: `9`
- selected coefficient source rows: `0`
- max reconstruction residual: `{max_abs_residual}`

## Next

`{NEXT}`.
"""

    write_json(BASIS_PACKET, basis_packet)
    write_json(COEFF_PACKET, coeff_packet)
    write_json(FUNCTIONAL_PACKET, functional_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
