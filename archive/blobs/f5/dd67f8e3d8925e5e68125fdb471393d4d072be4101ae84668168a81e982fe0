"""Extract the HYM SU(3) color-connection matrix data and audit closure.

The heterotic/Iwasawa corpus supplies an explicit left-invariant (0,1)
connection matrix for the rank-3 SU(3) bundle E.  This script records the
matrix data and computes only source-independent algebraic invariants.  It
does not turn those invariants into a determinant: the parameter mu, the
threshold operator/domain, and the representation still have to be selected
before a zeta determinant or analytic torsion can be evaluated.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FILL_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"
)

CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
HETEROTIC = (
    CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_terms() -> dict[str, Any]:
    text = HETEROTIC.read_text(encoding="utf-8", errors="ignore")
    required = [
        r"\bar\partial_E\;=\;\bar\partial + \mathcal{A}^{(0,1)}",
        r"\mu\,\bar\omega^3",
        r"\sqrt{\mu}\,\bar\omega^1",
        r"-\sqrt{\mu}\,\bar\omega^2",
        r"\mu>0",
        r"F_E\neq 0",
        r"\mathrm{Tr}F_E\wedge F_E=0",
        r"c_3(E)=6\,a\wedge b\wedge c",
    ]
    return {
        "path": str(HETEROTIC),
        "present": HETEROTIC.exists(),
        "terms_found": [term for term in required if term in text],
        "missing_terms": [term for term in required if term not in text],
    }


def coefficient_matrices() -> dict[str, Any]:
    """Return the coefficient matrices in symbolic mu notation."""

    return {
        "basis": ["bar_omega_1", "bar_omega_2", "bar_omega_3"],
        "A_bar_omega_1": [
            ["0", "0", "sqrt(mu)"],
            ["0", "0", "0"],
            ["0", "0", "0"],
        ],
        "A_bar_omega_2": [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["-sqrt(mu)", "0", "0"],
        ],
        "A_bar_omega_3": [
            ["0", "mu", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"],
        ],
        "parameter": "mu > 0",
    }


def algebraic_invariants() -> dict[str, Any]:
    """Compute invariants of the coefficient matrices as functions of mu.

    Each individual coefficient matrix is nilpotent, so its ordinary matrix
    eigenvalues are all zero.  The connection Laplacian is not determined by
    those eigenvalues; it depends on the covariant derivative, metric,
    representation, adjoint terms, curvature/endomorphism, and domain.
    """

    samples = []
    for mu in (0.25, 1.0, 4.0):
        frobenius_squared_sum = 2.0 * mu + mu * mu
        samples.append(
            {
                "mu": mu,
                "sum_frobenius_squared_of_A01_coefficients": frobenius_squared_sum,
                "diagnostic_only": True,
            }
        )

    return {
        "individual_coefficient_matrix_traces": {
            "A_bar_omega_1": 0,
            "A_bar_omega_2": 0,
            "A_bar_omega_3": 0,
        },
        "individual_coefficient_matrix_determinants": {
            "A_bar_omega_1": 0,
            "A_bar_omega_2": 0,
            "A_bar_omega_3": 0,
        },
        "individual_coefficient_matrix_eigenvalues": {
            "A_bar_omega_1": ["0", "0", "0"],
            "A_bar_omega_2": ["0", "0", "0"],
            "A_bar_omega_3": ["0", "0", "0"],
        },
        "sum_frobenius_squared_of_A01_coefficients": "2*mu + mu^2",
        "sample_mu_dependence": samples,
        "mu_dependence_detected": True,
    }


def main() -> int:
    fill = load(FILL_CERT)
    source = source_terms()

    blockers = [
        "select the continuous HYM matrix parameter mu from MTT/Strominger data rather than from the Qa/SU3 residual",
        "select the threshold representation: fundamental bundle E, adjoint End(E), or associated color local system",
        "construct the actual Laplace-type operator including metric, Chern/HYM connection, torsional endomorphism, BRST quotient, and det-prime zero-mode rule",
        "derive the spectrum, heat coefficients, or Ray-Singer torsion finite part for that selected operator",
        "prove compatibility between the Iwasawa HYM branch and the compact-Nil Qa Hodge/determinant branch",
    ]

    output = {
        "status": "QA_SU3_HYM_CONNECTION_MATRIX_EXTRACTED_SPECTRUM_TORSION_OPEN",
        "input_fill_status": fill["status"],
        "source_check": source,
        "selected_connection_matrix_data": {
            "connection_form": "A^(0,1)=B1*bar_omega_1 + B2*bar_omega_2 + B3*bar_omega_3",
            "coefficient_matrices": coefficient_matrices(),
            "source_parameter_status": "mu_positive_continuous_not_selected",
            "source_topology": {
                "c1": 0,
                "c2": "0 / Tr F_E wedge F_E = 0 in invariant sector",
                "c3": "6 a wedge b wedge c",
                "non_flat_warning": "source explicitly states F_E != 0 despite c2(E)=0",
            },
        },
        "computed_algebraic_invariants": algebraic_invariants(),
        "why_this_is_not_a_determinant": [
            "Chern classes and Chern-Weil traces constrain topology/anomaly data, not the full nonzero spectrum.",
            "The coefficient matrices are nilpotent, but the connection Laplacian is not the ordinary eigenvalue problem of those coefficient matrices.",
            "The free positive parameter mu changes connection-size diagnostics, so a numeric log determinant would be a knob unless mu is independently selected.",
            "No source-selected zeta derivative, heat coefficient, analytic torsion, or finite spectral table is supplied.",
        ],
        "remaining_blockers": blockers,
        "computed_numeric_response": None,
        "verdict": {
            "actual_hym_matrix_extracted": True,
            "source_selected_color_connection_candidate_found": True,
            "mu_selected": False,
            "selected_threshold_operator_constructed": False,
            "selected_spectrum_or_torsion_available": False,
            "can_close_Qa_SU3_now": False,
            "target_fitting_used": False,
            "full_SM_closure_achieved": False,
            "next_required_artifact": "Selected_Qa_SU3_HYM_Mu_and_Operator_Domain_Selection_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
