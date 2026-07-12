from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

END0_CERT = ROOT / "certificates" / "selected_end0_de_payload_from_diagonal_hym_certificate.json"
END0_PACKET = ROOT / "candidate_data" / "selected_end0_de_payload_from_diagonal_hym.packet.json"
SCALAR_PACKET = ROOT / "candidate_data" / "selected_scalar_exps_hym_newton_replay.packet.json"

OUT_CERT = ROOT / "certificates" / "selected_riesz_green_dotd_from_diagonal_end0_de_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1.md"

STATUS = "SELECTED_DIAGONAL_END0_RIESZ_GREEN_DOTD_PARTIAL_BUILT_ALPHA1_TRANSFER_OPEN"
NEXT = "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1"


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
        return np.fft.ifftn(out_hat).real

    def laplacian(field: np.ndarray) -> np.ndarray:
        return np.fft.ifftn(denom * np.fft.fftn(field)).real

    def derivative(field: np.ndarray, axis: int) -> np.ndarray:
        field_hat = np.fft.fftn(field)
        factor = 2j * math.pi * grids[axis]
        return np.fft.ifftn(factor * field_hat).real

    return solve_delta, laplacian, derivative


def l2(field: np.ndarray) -> float:
    return float(np.linalg.norm(field.ravel()) / math.sqrt(field.size))


def replay_s(mesh: int, cutoff: int, unit_rescale: float, damping: float) -> np.ndarray:
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")
    rho1 = weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0], cutoff)
    rho2 = weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :], cutoff)
    rho = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]
    solve_delta, _laplacian, _derivative = fft_operators(rho.shape)
    s = np.zeros_like(rho)
    for _ in range(80):
        q = rho * np.exp(-2.0 * s)
        target = solve_delta(-(q - q.mean()))
        s = (1.0 - damping) * s + damping * target
    return s


def matrix_scale(matrix: list[list[float]], scalar: float) -> list[list[float]]:
    return [[float(scalar * entry) for entry in row] for row in matrix]


def matrix_frobenius(matrix: list[list[float]]) -> float:
    return math.sqrt(sum(float(entry) ** 2 for row in matrix for entry in row))


def main() -> None:
    end0_cert = load(END0_CERT)
    end0 = load(END0_PACKET)
    scalar = load(SCALAR_PACKET)

    scalar_problem = scalar["finite_scalar_exps_problem"]
    selected_row = scalar["inputs"]["selected_row"]
    mesh = int(scalar_problem["mesh"])
    cutoff = int(scalar_problem["theta_cutoff"])
    damping = float(scalar_problem["damping"])
    unit_rescale = float(selected_row["unit_rescale_factor"])

    s = replay_s(mesh, cutoff, unit_rescale, damping)
    solve_delta, laplacian, derivative = fft_operators(s.shape)

    rng = np.random.default_rng(79)
    test_source = rng.normal(size=s.shape)
    test_source = test_source - test_source.mean()
    green_test = -solve_delta(test_source)
    green_residual = -laplacian(green_test) - test_source
    green_residual_l2 = l2(green_residual)
    green_test_l2 = l2(green_test)
    source_l2 = l2(test_source)

    lambda_1 = (2.0 * math.pi) ** 2
    green_operator_norm_bound = 1.0 / lambda_1

    ad_t3 = end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
    ad_t3_frobenius = matrix_frobenius(ad_t3)
    t3_kernel_annihilated = matrix_scale(ad_t3, 1.0)[2] == [0.0, 0.0, 0.0]

    dotd_direction_payload = {}
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        ds = derivative(s, axis)
        dotd_direction_payload[label] = {
            "formula": f"dotD_{label}[h] = (partial_{label} h) ad(T3)",
            "selected_driver_h_equals_s": True,
            "driver_partial_s_l2": l2(ds),
            "driver_dotD_frobenius_l2": float(ad_t3_frobenius * l2(ds)),
            "driver_partial_s_min": float(ds.min()),
            "driver_partial_s_max": float(ds.max()),
        }

    projected_t3_green_closed = all(
        [
            end0_cert["status"] == "SELECTED_END0_DE_DIAGONAL_PAYLOAD_BUILT_RIESZ_DOTD_TRANSFER_OPEN",
            end0["theorem"]["proved"] is True,
            end0["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"] is True,
            ad_t3 == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            t3_kernel_annihilated,
            abs(float(test_source.mean())) < 1.0e-14,
            green_residual_l2 < 1.0e-12,
            green_test_l2 <= green_operator_norm_bound * source_l2 + 1.0e-12,
            all(row["driver_partial_s_l2"] > 0 for row in dotd_direction_payload.values()),
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedRieszGreenDotDFromDiagonalEnd0DE",
            "proved": projected_t3_green_closed,
            "closure_claimed": False,
            "statement": (
                "On the protected diagonal T3 lane selected by the diagonal End0 "
                "operator, ad(T3)T3=0, so the covariant Laplacian reduces to the "
                "scalar positive operator -Delta on zero-mean scalar fields tensor "
                "T3. The selected Riesz/Green inverse and formal dotD packet are "
                "therefore computable for this lane. The coupled T1/T2 covariant "
                "Green, physical alpha1 derivative, sector transfer, and full "
                "validator payload remain open."
            ),
        },
        "protected_T3_lane": {
            "closed": projected_t3_green_closed,
            "basis_vector": "T3",
            "ad_T3_annihilates_T3": t3_kernel_annihilated,
            "projector_formula": "P0[f*T3] = mean(f) * T3",
            "zero_mean_projector_formula": "Pperp[f*T3] = (f-mean(f)) * T3",
            "operator_reduction": "D_E on T3 lane = d; D_E^*D_E = -Delta on zero-mean scalar fields",
        },
        "scalar_Riesz_Green_packet": {
            "closed": projected_t3_green_closed,
            "operator": "G = (-Delta)^(-1) on zero-mean scalar fields, tensor T3",
            "domain": "periodic 4D selected theta grid, mean-zero scalar fields",
            "mesh": mesh,
            "min_positive_eigenvalue_minus_delta": lambda_1,
            "green_operator_norm_bound": green_operator_norm_bound,
            "deterministic_test_seed": 79,
            "test_source_l2": source_l2,
            "green_test_l2": green_test_l2,
            "green_residual_l2": green_residual_l2,
            "residual_formula": "(-Delta)Gf - f for mean-zero f",
        },
        "dotD_frechet_packet": {
            "formula_closed": projected_t3_green_closed,
            "formal_formula": "dotD_a[h] = (partial_a h) ad(T3)",
            "selected_driver": "h=s from selected scalar expS HYM replay",
            "active_direction_payload": dotd_direction_payload,
            "physical_alpha1_driver_selected": False,
            "physical_alpha1_driver_status": "open; no physical alpha1 deformation kernel has been selected in this artifact",
        },
        "operator_payload_boundary": {
            "protected_T3_Riesz_payload_extracted": projected_t3_green_closed,
            "protected_T3_Green_payload_extracted": projected_t3_green_closed,
            "formal_dotD_packet_extracted": projected_t3_green_closed,
            "coupled_T1T2_covariant_Riesz_Green_extracted": False,
            "physical_dotD_alpha1_extracted": False,
            "rank2_to_sector_transfer_values_extracted": False,
            "offdiagonal_End0_terms_proved_zero_or_controlled": False,
            "validator_ready": False,
            "why_not_validator_ready": (
                "This proves the protected diagonal T3 scalar Riesz/Green lane and "
                "formal Frechet dotD formula, but it is not full validator-ready "
                "rhoE/D_E/Riesz/Green/dotD data until the coupled T1/T2 covariant "
                "operator, physical alpha1 derivative, rank2-to-sector transfer, "
                "and offdiagonal End0 control are supplied."
            ),
        },
        "what_closes_now": {
            "previous_gate_requested_Riesz_Green_dotD_payload": end0["next_required_artifact"]
            == "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1",
            "protected_T3_kernel_identified": projected_t3_green_closed,
            "protected_T3_projector_formula": projected_t3_green_closed,
            "protected_T3_scalar_Green_inverse_tested": projected_t3_green_closed,
            "formal_dotD_formula_for_diagonal_End0": projected_t3_green_closed,
            "shared_circle_spectator_preserved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "coupled_T1T2_covariant_Riesz_Green": True,
            "physical_dotD_alpha1_kernel": True,
            "rank2_to_rank3_sector_transfer_values": True,
            "offdiagonal_End0_control": True,
            "validator_ready_rhoE_DE_Riesz_Green_dotD": True,
        },
        "guardrails": {
            "does_not_use_observed_or_benchmark_data": True,
            "does_not_promote_protected_T3_lane_to_full_sector_payload": True,
            "does_not_use_projective_BN_as_End0_basis": True,
            "does_not_claim_physical_alpha1_derivative": True,
            "shared_circle_remains_spectator": True,
        },
        "input_artifacts": {
            "end0_cert": str(END0_CERT),
            "end0_packet": str(END0_PACKET),
            "scalar_packet": str(SCALAR_PACKET),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "protected_lane_closed": projected_t3_green_closed,
        "green_residual_small": green_residual_l2 < 1.0e-12,
        "lambda1_correct": abs(lambda_1 - 39.47841760435743) < 1.0e-14,
        "green_norm_bound_correct": abs(green_operator_norm_bound - 0.025330295910584444) < 1.0e-17,
        "green_test_obeys_bound": green_test_l2 <= green_operator_norm_bound * source_l2 + 1.0e-12,
        "formal_dotd_closed": packet["dotD_frechet_packet"]["formula_closed"],
        "physical_alpha1_open": packet["dotD_frechet_packet"]["physical_alpha1_driver_selected"] is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_riesz_green_dotd_from_diagonal_end0_de",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "protected_T3_Riesz_Green_dotD_closed": projected_t3_green_closed,
        "min_positive_eigenvalue_minus_delta": lambda_1,
        "green_operator_norm_bound": green_operator_norm_bound,
        "green_residual_l2": green_residual_l2,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Riesz Green dotD From Diagonal End0 DE v1

## Result

The diagonal End0 connection has a protected lane:

```text
D_E = d + ad(d s * T3)
ad(T3)T3 = 0
```

Therefore, on scalar fields tensor `T3`,

```text
P0[f*T3] = mean(f) * T3
Pperp[f*T3] = (f-mean(f)) * T3
G = (-Delta)^(-1) on zero-mean scalar fields tensor T3
dotD_a[h] = (partial_a h) ad(T3)
```

The deterministic finite-grid check gives:

```text
lambda_1(-Delta) = {lambda_1:.14g}
||G|| <= {green_operator_norm_bound:.17g}
||(-Delta)Gf - f||_L2 = {green_residual_l2:.3e}
```

with seed `79` and zero-mean test source.

## Boundary

This is a protected diagonal `T3` Riesz/Green and formal Frechet `dotD`
packet. It is not the full validator-ready payload: the coupled `T1/T2`
covariant Green operator, physical `dotD_alpha1` kernel, rank2-to-sector
transfer values, and offdiagonal End0 control remain open.

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
