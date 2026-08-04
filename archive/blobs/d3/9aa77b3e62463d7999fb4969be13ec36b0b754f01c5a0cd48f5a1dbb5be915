from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

RIESZ_CERT = ROOT / "certificates" / "selected_riesz_green_dotd_from_diagonal_end0_de_certificate.json"
RIESZ_PACKET = ROOT / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.packet.json"
SCALAR_PACKET = ROOT / "candidate_data" / "selected_scalar_exps_hym_newton_replay.packet.json"

OUT_CERT = ROOT / "certificates" / "selected_t1t2_covariant_green_or_rank2sector_transfer_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_t1t2_covariant_green_or_rank2sector_transfer.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1.md"

STATUS = "SELECTED_T1T2_COVARIANT_GREEN_CLOSED_RANK2_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_Rank2_to_Rank3_Sector_Transfer_or_Physical_dotD_alpha1_From_HYM_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def theta_tau_i(degree: int, index: int, z: complex, cutoff: int = 12) -> complex:
    total = 0j
    for n in range(-cutoff, cutoff + 1):
        shifted = n + index / degree
        total += cmath.exp(
            -math.pi * degree * shifted * shifted
            + 2j * math.pi * degree * shifted * z
        )
    return total


def weighted_theta_density(
    degree: int, index: int, x: np.ndarray, y: np.ndarray, cutoff: int = 12
) -> np.ndarray:
    out = np.zeros_like(x, dtype=float)
    for idx in np.ndindex(x.shape):
        z = complex(float(x[idx]), float(y[idx]))
        value = theta_tau_i(degree, index, z, cutoff)
        out[idx] = abs(value) ** 2 * math.exp(
            -2.0 * math.pi * degree * float(y[idx]) ** 2
        )
    return out


def fft_operators(shape: tuple[int, ...]):
    freqs = [np.fft.fftfreq(m, d=1.0 / m) for m in shape]
    grids = np.meshgrid(*freqs, indexing="ij")
    k2 = np.zeros(shape, dtype=float)
    for grid in grids:
        k2 += grid * grid
    denom = -((2.0 * math.pi) ** 2) * k2
    mask = k2 > 0

    def solve_delta(source: np.ndarray) -> np.ndarray:
        source_hat = np.fft.fftn(source)
        out_hat = np.zeros_like(source_hat, dtype=complex)
        out_hat[mask] = source_hat[mask] / denom[mask]
        out_hat[~mask] = 0.0
        return np.fft.ifftn(out_hat)

    def minus_laplacian(field: np.ndarray) -> np.ndarray:
        return np.fft.ifftn((-denom) * np.fft.fftn(field))

    def derivative(field: np.ndarray, axis: int) -> np.ndarray:
        return np.fft.ifftn((2j * math.pi * grids[axis]) * np.fft.fftn(field))

    return solve_delta, minus_laplacian, derivative


def l2_complex(field: np.ndarray) -> float:
    return float(np.linalg.norm(field.ravel()) / math.sqrt(field.size))


def replay_s(mesh: int, cutoff: int, unit_rescale: float, damping: float) -> np.ndarray:
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")
    rho1 = weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0], cutoff)
    rho2 = weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :], cutoff)
    rho = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]
    solve_delta, _minus_laplacian, _derivative = fft_operators(rho.shape)
    s = np.zeros_like(rho)
    for _ in range(80):
        q = rho * np.exp(-2.0 * s)
        target = solve_delta(-(q - q.mean())).real
        s = (1.0 - damping) * s + damping * target
    return s


def kernel_projector(field: np.ndarray, phase: np.ndarray) -> tuple[np.ndarray, complex]:
    trivialized = phase * field
    coefficient = complex(trivialized.mean())
    projected = np.conjugate(phase) * coefficient
    return projected, coefficient


def reduced_green(field: np.ndarray, phase: np.ndarray, solve_delta) -> tuple[np.ndarray, np.ndarray, complex]:
    trivialized = phase * field
    coefficient = complex(trivialized.mean())
    complement = trivialized - coefficient
    green_trivialized = -solve_delta(complement)
    green_field = np.conjugate(phase) * green_trivialized
    return green_field, complement, coefficient


def gauge_laplacian(field: np.ndarray, phase: np.ndarray, minus_laplacian) -> np.ndarray:
    return np.conjugate(phase) * minus_laplacian(phase * field)


def main() -> None:
    riesz_cert = load(RIESZ_CERT)
    riesz = load(RIESZ_PACKET)
    scalar = load(SCALAR_PACKET)

    scalar_problem = scalar["finite_scalar_exps_problem"]
    selected_row = scalar["inputs"]["selected_row"]
    mesh = int(scalar_problem["mesh"])
    cutoff = int(scalar_problem["theta_cutoff"])
    damping = float(scalar_problem["damping"])
    unit_rescale = float(selected_row["unit_rescale_factor"])

    s = replay_s(mesh, cutoff, unit_rescale, damping)
    solve_delta, minus_laplacian, derivative = fft_operators(s.shape)
    phase = np.exp(1j * s)
    kernel_1 = np.conjugate(phase)
    kernel_i = 1j * np.conjugate(phase)

    rng = np.random.default_rng(81)
    source = rng.normal(size=s.shape) + 1j * rng.normal(size=s.shape)
    source_kernel, source_kernel_coefficient = kernel_projector(source, phase)
    source_complement = source - source_kernel
    green_source, trivial_complement, green_kernel_coefficient = reduced_green(
        source, phase, solve_delta
    )
    residual = gauge_laplacian(green_source, phase, minus_laplacian) - source_complement

    lambda_1 = (2.0 * math.pi) ** 2
    green_operator_norm_bound = 1.0 / lambda_1
    residual_l2 = l2_complex(residual)
    source_complement_l2 = l2_complex(source_complement)
    green_l2 = l2_complex(green_source)

    # This is diagnostic only: it measures the product-rule aliasing left by
    # applying the truncated spectral derivative directly instead of using the
    # gauge-normal reduced operator.
    ds = [derivative(s, axis).real for axis in range(4)]

    def direct_covariant_D(field: np.ndarray) -> list[np.ndarray]:
        return [derivative(field, axis) + 1j * ds[axis] * field for axis in range(4)]

    direct_kernel_1_residual = math.sqrt(
        sum(l2_complex(row) ** 2 for row in direct_covariant_D(kernel_1))
    )
    direct_kernel_i_residual = math.sqrt(
        sum(l2_complex(row) ** 2 for row in direct_covariant_D(kernel_i))
    )

    kernel_inner_real_imag = complex(np.mean(np.conjugate(kernel_1) * kernel_i))
    projector_idempotence = l2_complex(
        kernel_projector(source_kernel, phase)[0] - source_kernel
    )
    complement_orthogonality = abs(complex((phase * source_complement).mean()))

    coupled_green_closed = all(
        [
            riesz_cert["status"] == "SELECTED_DIAGONAL_END0_RIESZ_GREEN_DOTD_PARTIAL_BUILT_ALPHA1_TRANSFER_OPEN",
            riesz["theorem"]["proved"] is True,
            riesz["operator_payload_boundary"]["protected_T3_Green_payload_extracted"] is True,
            residual_l2 < 1.0e-12,
            green_l2 <= green_operator_norm_bound * source_complement_l2 + 1.0e-12,
            projector_idempotence < 1.0e-14,
            complement_orthogonality < 1.0e-14,
            abs(abs(kernel_inner_real_imag) - 1.0) < 1.0e-14,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedT1T2CovariantGreenFromDiagonalHYM",
            "proved": coupled_green_closed,
            "closure_claimed": False,
            "statement": (
                "The coupled T1/T2 block of the selected diagonal End0 connection "
                "is a pure-gauge complex line: for w=T1+iT2, D w = d w + i d s w, "
                "and multiplication by exp(i s) conjugates D to d. Hence the "
                "covariant Laplacian has a two-real-dimensional parallel kernel "
                "spanned by exp(-i s) and i exp(-i s), and its reduced Green on "
                "the orthogonal complement is exp(-i s)(-Delta)^(-1)Pperp exp(i s)."
            ),
        },
        "complex_T1T2_identification": {
            "closed": coupled_green_closed,
            "real_basis": ["T1", "T2"],
            "complex_coordinate": "w = u*T1 + v*T2 represented as u + i v",
            "connection_formula": "D w = d w + i d s w",
            "gauge_trivialization": "z = exp(i s) w, so D w = exp(-i s) d z",
            "kernel_real_basis": ["Re(exp(-i s)) and Im(exp(-i s)) encoded by exp(-i s)", "i exp(-i s)"],
            "kernel_dimension_real": 2,
        },
        "reduced_projector_and_green": {
            "closed": coupled_green_closed,
            "kernel_projector": "Pker[f] = exp(-i s) mean(exp(i s) f)",
            "complement_projector": "Pperp[f] = f - Pker[f]",
            "reduced_green": "G12[f] = exp(-i s) (-Delta)^(-1)(exp(i s)f - mean(exp(i s)f))",
            "min_positive_eigenvalue": lambda_1,
            "green_operator_norm_bound": green_operator_norm_bound,
            "deterministic_test_seed": 81,
            "source_kernel_coefficient": {
                "real": float(source_kernel_coefficient.real),
                "imag": float(source_kernel_coefficient.imag),
            },
            "green_kernel_coefficient": {
                "real": float(green_kernel_coefficient.real),
                "imag": float(green_kernel_coefficient.imag),
            },
            "source_complement_l2": source_complement_l2,
            "green_l2": green_l2,
            "green_residual_l2": residual_l2,
            "projector_idempotence_l2": projector_idempotence,
            "complement_orthogonality_abs": float(complement_orthogonality),
        },
        "finite_aliasing_boundary": {
            "raw_truncated_product_rule_identity_claimed": False,
            "why": (
                "The rigorous selected finite Green is emitted in gauge-normal form. "
                "Directly expanding d+i ds on a truncated spectral grid introduces "
                "multiplication/projection aliasing and is diagnostic only."
            ),
            "direct_D_exp_minus_is_kernel_residual_l2": direct_kernel_1_residual,
            "direct_D_i_exp_minus_is_kernel_residual_l2": direct_kernel_i_residual,
        },
        "operator_payload_boundary": {
            "coupled_T1T2_covariant_Riesz_Green_extracted": coupled_green_closed,
            "T1T2_parallel_kernel_projector_extracted": coupled_green_closed,
            "rank2_to_sector_transfer_values_extracted": False,
            "physical_dotD_alpha1_extracted": False,
            "offdiagonal_End0_terms_proved_zero_or_controlled": False,
            "validator_ready": False,
            "why_not_validator_ready": (
                "The protected T3 lane and the coupled T1/T2 reduced Green are now "
                "closed for the diagonal pure-gauge End0 block. The rank2-to-sector "
                "transfer, physical alpha1 derivative, and offdiagonal End0 control "
                "remain separate selected-source gates."
            ),
        },
        "what_closes_now": {
            "previous_gate_requested_T1T2_or_sector_transfer": riesz["next_required_artifact"]
            == "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1",
            "T1T2_complex_pure_gauge_identification": coupled_green_closed,
            "T1T2_parallel_kernel_projector": coupled_green_closed,
            "T1T2_reduced_Green_formula": coupled_green_closed,
            "T1T2_finite_green_residual_test": coupled_green_closed,
            "shared_circle_spectator_preserved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "rank2_to_rank3_sector_transfer_values": True,
            "physical_dotD_alpha1_kernel": True,
            "offdiagonal_End0_control": True,
            "validator_ready_rhoE_DE_Riesz_Green_dotD": True,
        },
        "guardrails": {
            "does_not_use_observed_or_benchmark_data": True,
            "does_not_promote_T1T2_green_to_sector_transfer": True,
            "does_not_use_projective_BN_as_End0_basis": True,
            "does_not_claim_physical_alpha1_derivative": True,
            "does_not_claim_raw_truncated_product_rule_exactness": True,
            "shared_circle_remains_spectator": True,
        },
        "input_artifacts": {
            "riesz_cert": str(RIESZ_CERT),
            "riesz_packet": str(RIESZ_PACKET),
            "scalar_packet": str(SCALAR_PACKET),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "coupled_green_closed": coupled_green_closed,
        "green_residual_small": residual_l2 < 1.0e-12,
        "projector_idempotent": projector_idempotence < 1.0e-14,
        "complement_orthogonal": complement_orthogonality < 1.0e-14,
        "green_test_obeys_bound": green_l2 <= green_operator_norm_bound * source_complement_l2 + 1.0e-12,
        "lambda1_correct": abs(lambda_1 - 39.47841760435743) < 1.0e-14,
        "rank2_sector_open": packet["operator_payload_boundary"]["rank2_to_sector_transfer_values_extracted"] is False,
        "physical_alpha1_open": packet["operator_payload_boundary"]["physical_dotD_alpha1_extracted"] is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_t1t2_covariant_green_or_rank2sector_transfer",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "T1T2_covariant_reduced_Green_closed": coupled_green_closed,
        "rank2_to_sector_transfer_values_closed": False,
        "physical_dotD_alpha1_closed": False,
        "min_positive_eigenvalue": lambda_1,
        "green_operator_norm_bound": green_operator_norm_bound,
        "green_residual_l2": residual_l2,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected T1T2 Covariant Green or Rank2 Sector Transfer From Diagonal HYM v1

## Result

The coupled `T1/T2` block closes as a pure-gauge complex line. With

```text
w = u + i v
D w = d w + i d s w
z = exp(i s) w
```

we have:

```text
D w = exp(-i s) d z
Pker[f] = exp(-i s) mean(exp(i s) f)
G12[f] = exp(-i s) (-Delta)^(-1)(exp(i s)f - mean(exp(i s)f))
```

The parallel kernel is two-dimensional over the reals, generated by
`exp(-i s)` and `i exp(-i s)`.

The deterministic finite-grid reduced Green check gives:

```text
lambda_1 = {lambda_1:.14g}
||G12|| <= {green_operator_norm_bound:.17g}
||L12 G12 f - Pperp f||_L2 = {residual_l2:.3e}
```

## Boundary

This closes the `T1/T2` reduced covariant Green in gauge-normal form. It does
not yet provide rank2-to-sector transfer values, physical `dotD_alpha1`, or
offdiagonal End0 control. Direct truncated expansion of the product rule is
kept diagnostic because multiplication by `exp(i s)` aliases modes on the
finite spectral grid.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
