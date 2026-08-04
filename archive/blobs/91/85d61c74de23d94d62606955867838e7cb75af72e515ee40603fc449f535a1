"""Compute the source-induced invariant adjoint commutator block for Delta_A(mu).

This is not the full Yang-Mills Laplacian.  It is the algebraic invariant-band
piece forced by the extracted HYM (0,1) connection matrices:

    H_alg(mu) = sum_i ad(B_i)^* ad(B_i)

on End(C^3).  The identity endomorphism is a zero commutator mode, while the
remaining eight complex adjoint directions are positive in this diagnostic
block.  Full mu selection still requires the metric/Chern real form, torsion,
gauge quotient, and OU weights specified by the Strominger selection theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
MU_GATE_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def connection_matrices(mu: float) -> list[np.ndarray]:
    s = math.sqrt(mu)
    return [
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
    ]


def ad_matrix(matrix: np.ndarray) -> np.ndarray:
    # Column-vectorized convention: vec(BX - XB) = (I kron B - B^T kron I) vec(X).
    identity = np.eye(matrix.shape[0], dtype=complex)
    return np.kron(identity, matrix) - np.kron(matrix.T, identity)


def algebraic_block(mu: float) -> dict[str, Any]:
    ads = [ad_matrix(matrix) for matrix in connection_matrices(mu)]
    h_alg = sum(ad.conj().T @ ad for ad in ads)
    eig = np.linalg.eigvalsh(h_alg)
    rounded = [0.0 if abs(float(value)) < 1e-12 else float(value) for value in eig]
    positive = [value for value in rounded if value > 1e-10]
    return {
        "mu": mu,
        "operator": "H_alg(mu)=sum_i ad(B_i)^* ad(B_i) on End(C^3)",
        "dimension_complex_end": 9,
        "zero_modes": len([value for value in rounded if abs(value) <= 1e-10]),
        "positive_modes": len(positive),
        "rank": int(np.linalg.matrix_rank(h_alg, tol=1e-10)),
        "eigenvalues": rounded,
        "trace": float(np.trace(h_alg).real),
        "det_prime": float(np.prod(positive)) if positive else None,
        "log_det_prime": float(np.sum(np.log(positive))) if positive else None,
        "identity_commutator_zero_mode_expected": True,
    }


def monotonicity_diagnostic(samples: list[dict[str, Any]]) -> dict[str, Any]:
    log_dets = [sample["log_det_prime"] for sample in samples]
    return {
        "sample_mu_values": [sample["mu"] for sample in samples],
        "sample_log_det_prime_values": log_dets,
        "strictly_increasing_on_samples": all(
            after > before for before, after in zip(log_dets, log_dets[1:])
        ),
        "selection_consequence": (
            "This algebraic block alone does not select an interior mu; without "
            "the missing sourced terms it would favor a boundary or arbitrary "
            "normalization, so it cannot be used as the final determinant."
        ),
    }


def main() -> int:
    gate = load(MU_GATE_CERT)
    sample_mu = [0.25, 1.0, 4.0]
    samples = [algebraic_block(mu) for mu in sample_mu]
    output = {
        "status": "QA_SU3_HYM_DELTA_A_MU_ALGEBRAIC_BLOCK_COMPUTED_FULL_SELECTION_OPEN",
        "input_mu_gate_status": gate["status"],
        "source_selected_domain": gate["selected_next_operator_gate"],
        "computed_block_scope": {
            "included": [
                "explicit HYM (0,1) coefficient matrices B_i",
                "adjoint commutator action on End(C^3)",
                "positive semidefinite algebraic invariant-band block sum ad(B_i)^* ad(B_i)",
            ],
            "excluded": [
                "real unitary u(E) slice and Hermitian metric normalization",
                "Chern (1,0) conjugate connection pieces",
                "Iwasawa metric/radius weights in the inner product",
                "torsional endomorphism and curvature terms",
                "gauge fixing and quotient of symmetry directions",
                "OU weights gamma_{n,k}^{-1}",
                "full zeta/heat regularized determinant",
            ],
        },
        "sample_blocks": samples,
        "monotonicity_diagnostic": monotonicity_diagnostic(samples),
        "remaining_required_data": [
            "derive the real u(E)-valued one-form Hessian from the Chern/HYM connection, not only the complex End(C3) commutator block",
            "insert selected Iwasawa metric/radius weights and any torsional Weitzenbock/endomorphism terms",
            "quotient gauge and symmetry directions in the same fixed gauge used by the Strominger Hessian theorem",
            "supply OU weights gamma_{n,k}^{-1} or prove they vanish/are irrelevant on this block",
            "then minimize the complete sourced Hessian/determinant in mu before comparing to Qa/SU3 data",
        ],
        "computed_numeric_response": None,
        "verdict": {
            "delta_a_mu_algebraic_block_computed": True,
            "positive_adjoint_modes_seen_in_samples": True,
            "identity_zero_mode_seen": True,
            "mu_selected": False,
            "selected_full_delta_a_spectrum_available": False,
            "can_close_Qa_SU3_now": False,
            "target_fitting_used": False,
            "full_SM_closure_achieved": False,
            "next_required_artifact": "Selected_Qa_SU3_HYM_Full_Real_Delta_A_Hessian_With_OU_Weights_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
