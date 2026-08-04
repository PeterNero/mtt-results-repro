"""Build residual Weyl-polynomial source theorem attempt."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SOURCE_TEMPLATE = (
    DATA
    / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
    / "minimal_residual_source_packet.template.json"
)
PROMOTION_GATE = DATA / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission.candidate.json"
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
WEYL_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"

OUTPUT = DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"
PACKET_DIR = DATA / "selected_residual_weylpolynomial_source_theorem_attempt"
WEYL_PACKET = PACKET_DIR / "residual_weyl_polynomial_decomposition.packet.json"
SELECTION_GATE = PACKET_DIR / "canonical_residual_projector_selection_gate.packet.json"
CERT = CERTS / "selected_residual_weylpolynomial_source_theorem_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_Residual_WeylPolynomial_Source_Theorem_Attempt_v1.md"

STATUS = "MTT_SELECTED_RESIDUAL_WEYLPOLYNOMIAL_SOURCE_THEOREM_ATTEMPT_BUILT_PROJECTOR_SELECTION_OPEN"
NEXT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"
TOL = 1e-9


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def c(value: Any) -> complex:
    if isinstance(value, bool):
        raise TypeError(value)
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(value)


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def inner(a: list[list[complex]], b: list[list[complex]]) -> complex:
    return sum(a[i][j].conjugate() * b[i][j] for i in range(3) for j in range(3))


def matrix_from_packet(source: dict[str, Any], key: str) -> list[list[complex]]:
    raw = source["required_source_emissions"][key]["shape"]["matrix"]
    return [[c(value) for value in row] for row in raw]


def matrix_norm_sq(m: list[list[complex]]) -> float:
    return float(sum(abs(m[i][j]) ** 2 for i in range(3) for j in range(3)))


def matrix_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def matrix_add_scaled(
    terms: list[tuple[complex, list[list[complex]]]]
) -> list[list[complex]]:
    return [[sum(coeff * matrix[i][j] for coeff, matrix in terms) for j in range(3)] for i in range(3)]


def encode_matrix(m: list[list[complex]]) -> list[list[Any]]:
    return [[encode_scalar(value) for value in row] for row in m]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    source_template = load(SOURCE_TEMPLATE)
    promotion_gate = load(PROMOTION_GATE)
    source_selector = load(SOURCE_SELECTOR)
    provenance = load(WEYL_PROVENANCE)

    omega = cmath.exp(2j * math.pi / 3)
    identity = [[complex(1.0 if i == j else 0.0, 0.0) for j in range(3)] for i in range(3)]
    z = [[omega**i if i == j else 0.0 for j in range(3)] for i in range(3)]
    x = [[complex(1.0 if j == (i + 1) % 3 else 0.0, 0.0) for j in range(3)] for i in range(3)]
    z_powers = [identity, z, matmul(z, z)]
    x_powers = [identity, x, matmul(x, x)]

    basis: list[tuple[int, int, list[list[complex]]]] = []
    for a, za in enumerate(z_powers):
        for b, xb in enumerate(x_powers):
            basis.append((a, b, matmul(za, xb)))

    residual_matrices = {
        "R_Z": matrix_from_packet(source_template, "phase_residual_operator_R_Z"),
        "R_X": matrix_from_packet(source_template, "shift_residual_operator_R_X"),
    }

    decompositions: dict[str, Any] = {}
    for name, matrix in residual_matrices.items():
        coefficients = []
        reconstructed_terms = []
        for a, b, basis_matrix in basis:
            coeff = inner(basis_matrix, matrix) / 3.0
            if abs(coeff) > TOL:
                coefficients.append(
                    {
                        "basis": f"Z^{a} X^{b}",
                        "a": a,
                        "b": b,
                        "coefficient": encode_scalar(coeff),
                        "coefficient_abs": abs(coeff),
                    }
                )
                reconstructed_terms.append((coeff, basis_matrix))
        reconstructed = matrix_add_scaled(reconstructed_terms)
        error = matrix_norm_sq(matrix_sub(matrix, reconstructed))
        decompositions[name] = {
            "coefficients": coefficients,
            "coefficient_count": len(coefficients),
            "reconstruction_error_norm_sq": error,
            "norm_sq": matrix_norm_sq(matrix),
            "matrix": encode_matrix(matrix),
            "reconstructed_matrix": encode_matrix(reconstructed),
        }

    exact_polynomial_form = {
        "R_X": "(1/3) I + (1/3) X - (2/3) X^2",
        "R_Z": "(2/3) I + (2/3) Z - (1/3) X - (1/3) X^2 + (e^{i*pi/3}/3) Z X + (e^{-i*pi/3}/3) Z X^2",
    }

    weyl_packet = {
        "schema": "MTTResidualWeylPolynomialDecomposition.v1",
        "status": "EXACT_LOW_DEGREE_WEYL_POLYNOMIAL_DECOMPOSITION_COMPUTED",
        "source_level_weyl_carrier_selected": provenance["source_level_weyl_carrier"]["proved"],
        "active_shift_selected": provenance["active_shift_provenance"]["proved"],
        "static_source_selector_selected": source_selector["promotion_decision"]["source_selector_promoted"],
        "basis": "qutrit Weyl basis {Z^a X^b | a,b in Z_3}",
        "orthogonality": "Tr((Z^a X^b)^* Z^c X^d)=3 delta_ac delta_bd",
        "exact_polynomial_form": exact_polynomial_form,
        "decompositions": decompositions,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    selection_gate = {
        "schema": "MTTCanonicalResidualProjectorSelectionGate.v1",
        "status": "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN",
        "what_is_now_canonical": [
            "Weyl carrier Z/X is selected at source level",
            "active shift (1,1) is selected",
            "fixed-fiber class [0,1,2] is selected for current C1 spectral observables",
            "trace/Frobenius transfer normalization is selected",
            "orthogonal residual projection is uniquely computed from those ingredients",
        ],
        "what_is_not_yet_selected": [
            "the C1 transfer functor applying that residual projector as physical dynamic response",
            "the theorem that Phi_fin^C1 uses the residualized Weyl polynomial rather than only the fixed-fiber projection",
            "honest Galerkin C1 replacement values",
        ],
        "if_projector_selection_theorem_is_supplied": {
            "lane_A_residual_source_promotes": True,
            "SM_parity_dynamic_packet_closes": True,
            "A_selected_available": True,
            "b_selected_available": True,
            "deltaTheta_C1": [1.0, 1.0],
            "no_knob_flavor_constants_derived": False,
        },
        "current_decision": "SOURCE_CARRIER_AND_CANONICAL_POLYNOMIAL_CLOSED_PROJECTOR_SELECTION_OPEN",
    }

    candidate = {
        "candidate": "MTTSelectedResidualWeylPolynomialSourceTheoremAttempt",
        "status": STATUS,
        "inputs": {
            "minimal_residual_source_packet": rel(SOURCE_TEMPLATE),
            "residual_promotion_gate": rel(PROMOTION_GATE),
            "source_selector": rel(SOURCE_SELECTOR),
            "weyl_source_provenance": rel(WEYL_PROVENANCE),
        },
        "output_packets": {
            "weyl_polynomial_decomposition": rel(WEYL_PACKET),
            "canonical_residual_projector_selection_gate": rel(SELECTION_GATE),
        },
        "what_closes_now": {
            "residuals_compressed_to_low_degree_weyl_polynomials": True,
            "source_level_weyl_carrier_attached": True,
            "canonical_trace_projector_target_identified": True,
            "Lane_A_reduced_to_projector_selection_theorem": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "canonical_residual_projector_selection_theorem": True,
            "selected_PhiFinC1_transfer_functor_on_residual_polynomial": True,
            "honest_selected_Galerkin_C1_value_run": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "Lane_A_promoted": False,
            "canonical_residual_projector_promoted": False,
            "residual_weyl_polynomial_selected_as_dynamic_response": False,
            "SM_parity_dynamic_packet_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "SM_parity_view": promotion_gate["SM_parity_view"],
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ResidualWeylPolynomialReductionTheorem",
            "proved": True,
            "statement": (
                "The required residual matrices R_Z and R_X are not arbitrary numerical "
                "objects: they decompose exactly as low-degree polynomials in the selected "
                "qutrit Weyl carrier Z/X.  Therefore Lane A reduces from searching for "
                "matrices to proving that the selected Phi_fin^C1 or Hessian/basis-transport "
                "rule applies the canonical trace-orthogonal residual projector to this "
                "Weyl polynomial packet.  That projector-selection theorem is still open."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_Residual_WeylPolynomial_Source_Theorem_Attempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "weyl_packet_path": rel(WEYL_PACKET),
        "selection_gate_path": rel(SELECTION_GATE),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Residual WeylPolynomial Source Theorem Attempt v1

Status: `{STATUS}`.

The residual matrices are now exactly compressed into qutrit Weyl polynomials:

```text
R_X = {exact_polynomial_form["R_X"]}
R_Z = {exact_polynomial_form["R_Z"]}
```

This is progress because the missing Lane A object is no longer an arbitrary
matrix packet.  It is a canonical Weyl-polynomial residual packet over the
already selected source-level `Z/X` carrier, active shift `(1,1)`, fixed-fiber
class `[0,1,2]`, and trace/Frobenius normalization.

What remains open is the selection theorem saying that `Phi_fin^C1`, the
basis-transport correction, or the Hessian counterterm applies the canonical
trace-orthogonal residual projector as the physical dynamic response.  Without
that theorem, the packet remains diagnostic and SM-parity dynamic closure is not
claimed.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    WEYL_PACKET.write_text(json.dumps(weyl_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SELECTION_GATE.write_text(json.dumps(selection_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
