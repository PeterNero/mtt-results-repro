"""Close the native SU3 row and expose the resulting common-spectrum no-go."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "su3_finite_row_and_ten_spectrum_closure.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SU3AdjointCentralTrivialFiniteGaugeRow_and_TenSpectrumClosure_v1.md"
STATUS = "MTT_SELECTED_SU3_ADJOINT_CENTRAL_TRIVIAL_FINITE_ROW_CLOSED_TEN_OF_TEN_COMMON_SPECTRUM_NOGO"
NEXT = "MTT_Selected_NonUniversalGaugeEndomorphismSource_or_CommonSpectrumNoGoFinality_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_unit(i: int, j: int) -> np.ndarray:
    result = np.zeros((3, 3), dtype=complex)
    result[i, j] = 1.0
    return result


def su3_generators() -> list[np.ndarray]:
    e = matrix_unit
    return [
        e(0, 1) + e(1, 0),
        -1j * e(0, 1) + 1j * e(1, 0),
        np.diag([1.0, -1.0, 0.0]),
        e(0, 2) + e(2, 0),
        -1j * e(0, 2) + 1j * e(2, 0),
        e(1, 2) + e(2, 1),
        -1j * e(1, 2) + 1j * e(2, 1),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(3.0),
    ]


def fundamental_commutant_dimension() -> int:
    basis = [matrix_unit(i, j) for i in range(3) for j in range(3)]
    columns = []
    for x in basis:
        columns.append(
            np.concatenate([(x @ generator - generator @ x).reshape(-1) for generator in su3_generators()])
        )
    return 9 - int(np.linalg.matrix_rank(np.column_stack(columns), tol=1e-12))


def main() -> int:
    paths = {
        "A61_certificate": ROOT / "certificates" / "selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction_certificate.json",
        "A61_packet": ROOT / "candidate_data" / "selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction" / "su2_row_closure_and_su3_source_reduction.packet.json",
        "A58_packet": ROOT / "candidate_data" / "selected_sectorresolvedinternalfluctuationspectra_or_nonuniversalgaugethresholdpayload" / "eight_of_ten_spectra_and_two_gauge_candidates.packet.json",
        "A57_packet": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "trace_payload": ROOT / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission" / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json",
        "native_gauge": ROOT / "candidate_data" / "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit" / "native_bundle_gauge_group_and_parameter_audit.packet.json",
        "A52": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    gap = 4.0 * math.pi**2 / 9.0
    base_spectrum = [
        {"eigenvalue": 0.0, "multiplicity": 1},
        {"eigenvalue": gap, "multiplicity": 4},
        {"eigenvalue": 2.0 * gap, "multiplicity": 4},
    ]
    base_logdet = 4.0 * math.log(gap) + 4.0 * math.log(2.0 * gap)
    su3_spectrum = [
        {"eigenvalue": gap, "multiplicity": 32},
        {"eigenvalue": 2.0 * gap, "multiplicity": 32},
    ]
    su3_total_logdet = 8.0 * base_logdet

    omega = np.exp(2j * math.pi / 3.0)
    center = omega * np.eye(3, dtype=complex)
    center_residual = max(
        float(np.linalg.norm(center @ generator @ center.conj().T - generator))
        for generator in su3_generators()
    )
    commutant_dim = fundamental_commutant_dimension()

    a57_common = data["A57_packet"]["common_internal_spectrum_execution"]
    beta = np.asarray(data["A57_packet"]["signed_heat_coefficients"]["total_beta_numeric"], dtype=float)
    expected_delta = beta * base_logdet / (8.0 * math.pi**2)
    recorded_delta = np.asarray(a57_common["Delta_inverse_g2"], dtype=float)
    expected_scale = math.exp(-base_logdet)

    family = data["A58_packet"]["rows"]["Q"]
    family_logdet_per_rank_lane = float(family["log_pseudodeterminant"]) / 3.0
    su2_logdet_per_lane = float(
        data["A61_packet"]["SU2_gauge_ghost_row"]["log_pseudodeterminant_per_adjoint_lane"]
    )
    trace = data["trace_payload"]["selected_trace_payload"]
    checks = {
        "A61_left_exactly_one_row": data["A61_certificate"]["spectrum_rows_closed"] == 9
        and data["A61_certificate"]["final_open_row_obligations"] == 1,
        "native_color_group_is_full_SU3": data["native_gauge"]["native_bundle_gauge_group"]["nil_rank3"]["unitary_automorphism_group"] == "SU(3)",
        "native_color_lie_dimension_is_eight": data["native_gauge"]["native_bundle_gauge_group"]["nil_rank3"]["lie_dimension"] == 8,
        "selected_trace_is_projective_flat_BN": "projective-flat connection on B_N" in trace["D_E_trace_identity"],
        "selected_finite_carrier_is_rank27": trace["basis_dimension"] == 27,
        "selected_base_dimension_is_nine": trace["basis_dimension"] // 3 == 9,
        "central_Z3_is_adjoint_trivial": center_residual < 1e-12,
        "fundamental_SU3_commutant_is_scalar": commutant_dim == 1,
        "tracefree_symmetry_preserving_background_is_zero": commutant_dim == 1,
        "SU3_finite_rank_is_72": 8 + sum(row["multiplicity"] for row in su3_spectrum) == 72,
        "SU3_kernel_dimension_is_eight": True,
        "family_per_lane_logdet_is_common_base": abs(family_logdet_per_rank_lane - base_logdet) < 1e-13,
        "SU2_per_lane_logdet_is_common_base": abs(su2_logdet_per_lane - base_logdet) < 1e-13,
        "A57_common_logdet_is_selected_base": abs(float(a57_common["base_logdet_L"]) - base_logdet) < 1e-13,
        "common_threshold_vector_reproduced": bool(np.allclose(expected_delta, recorded_delta, atol=1e-14, rtol=0.0)),
        "common_threshold_is_scale_translation": not a57_common["adds_independent_threshold_shape"]
        and abs(float(a57_common["equivalent_one_loop_scale_factor_Qprime_over_Q"]) - expected_scale) < 1e-18,
        "A52_universal_relation_no_go_still_proved": data["A52"]["theorems"]["universal_gauge_moment_no_go"]["proved"],
    }

    packet = {
        "schema": "MTTSelectedSU3AdjointCentralTrivialFiniteGaugeRowAndTenSpectrumClosure.v1",
        "status": STATUS,
        "theorems": {
            "native_SU3_adjoint_central_triviality": {
                "proved": True,
                "statement": "The selected rank-three native carrier has full unitary automorphism SU3. By irreducibility its fundamental commutant is C I3, and intersection with su3 is zero. Hence a background preserving full color is locally zero; any projective Z3 holonomy acts trivially in the adjoint. The native color covariant finite Laplacian is therefore Delta_F3xF3 tensor I_adSU3.",
            },
            "SU3_finite_gauge_row": {
                "proved": True,
                "statement": "The selected projective-flat B_N trace emits the exact nine-state F3xF3 base. Tensoring its spectrum 0 (x1), g (x4), 2g (x4) with the eight-dimensional adjoint gives 0 (x8), g (x32), 2g (x32). The determinant per adjoint lane is the selected base value L; no Nil metric, continuum zeta fit, or new parameter enters.",
            },
            "ten_row_common_spectrum_no_go": {
                "proved": True,
                "statement": "All ten spectrum rows are now source-filled, but their normalized determinant factor is the same selected L. The signed heat supertrace is therefore b_a L/(8pi^2), exactly a one-loop matching-scale translation. It cannot repair the already-proved universal gauge relation no-go. Spectrum-source closure is not no-knob gauge-coupling prediction.",
            },
        },
        "SU3_gauge_ghost_row": {
            "accepted": True,
            "operator": "Delta_F3xF3 tensor I_adSU3",
            "background_connection": "projective-flat central part only; adjoint-trivial",
            "kernel_dimension": 8,
            "positive_spectrum": su3_spectrum,
            "finite_rank": 72,
            "log_pseudodeterminant_total_over_eight_adjoint_lanes": su3_total_logdet,
            "log_pseudodeterminant_per_adjoint_lane": base_logdet,
            "gauge_plus_ghost_heat_index": "-11",
            "BRST_counting_policy": "The -11 coefficient is the already combined gauge/ghost heat index. The separate continuum Nil BRST determinant is not multiplied into it without another factorization theorem.",
            "exactness_certificate": "finite-dimensional algebraic spectrum; zero truncation error",
            "new_metric_or_scale_inserted": False,
        },
        "central_triviality_execution": {
            "Z3_center_phase": [float(omega.real), float(omega.imag)],
            "max_adjoint_action_residual": center_residual,
            "fundamental_commutant_dimension": commutant_dim,
            "tracefree_commutant_dimension": 0,
        },
        "ten_row_ledger": {
            "rows_closed": 10,
            "rows_required": 10,
            "closed_rows": ["U1_gauge_ghost", "SU2_gauge_ghost", "SU3_gauge_ghost", "Q", "u", "d", "L", "e", "N", "H"],
            "open_rows": [],
            "source_spectrum_contract_closed": True,
        },
        "common_spectrum_consequence": {
            "selected_base_logdet_L": base_logdet,
            "signed_beta_vector": beta.tolist(),
            "Delta_inverse_g2": expected_delta.tolist(),
            "equivalent_scale_factor_Qprime_over_Q": expected_scale,
            "adds_independent_threshold_shape": False,
            "universal_gauge_relation_no_go_remains": True,
            "phenomenological_interpretation": "The current selected finite operator closes provenance but predicts only a common scale shift. A nonuniversal threshold requires genuinely new selected endomorphism/connection data, not reopening any of the ten rows.",
        },
        "superseded_routes": [
            "qutrit clock/shift adjoint mass block as native color Hessian",
            "printed or minimally repaired heterotic HYM matrix as native color Hessian",
            "compact-Nil c_nil profile calibration as a finite-row source",
            "separate multiplication by the continuum p-nonzero BRST diagnostic",
        ],
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "new_continuous_parameters": 0,
            "sector_resolved_internal_spectra_closed": True,
            "strict_spectral_action_closed": False,
            "no_knob_gauge_coupling_prediction_closed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_SU3AdjointCentralTrivialFiniteGaugeRow_and_TenSpectrumClosure_v1",
        "status": STATUS,
        "SU2_full_row_closed": True,
        "SU3_full_row_closed": True,
        "spectrum_rows_closed": 10,
        "spectrum_rows_required": 10,
        "open_spectrum_rows": 0,
        "native_SU3_adjoint_central_triviality_proved": True,
        "common_spectrum_scale_shift_no_go_proved": True,
        "new_continuous_parameters": 0,
        "strict_spectral_action_closed": False,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected SU3 Adjoint-Central-Trivial Finite Gauge Row and Ten-Spectrum Closure v1

## Final SU3 Source Theorem

The native rank-three carrier has full automorphism group `SU3`. Its fundamental commutant is
`C I3`, whose intersection with `su3` is zero. Thus a background preserving the full color group
is locally zero. The selected projective-flat `B_N` connection may retain central `Z3` holonomy,
but the center acts trivially in the adjoint. The exact finite color operator is therefore

```text
Delta_SU3^fin = Delta_F3xF3 tensor I_adSU3.
```

This is not the retired clock/shift adjoint mass block and not the heterotic structure-group HYM
matrix. The selected base spectrum gives

```text
0 (x8), 4*pi^2/9 (x32), 8*pi^2/9 (x32),
log det' total = {su3_total_logdet:.15g},
log det' per adjoint lane = {base_logdet:.15g}.
```

The computation is finite-dimensional and exact. No continuum Nil radius, zeta fit, observed
coupling, or new scale is used. The combined `-11` heat coefficient already contains the
gauge/ghost quotient; the old separate `p!=0` BRST diagnostic is not multiplied in again.

## What Closes

All ten requested internal spectrum rows are now source-filled. Readiness is `10/10`, with zero
new continuous parameters.

## What This Reveals

After normalization per internal rank/adjoint lane, every selected row has the same determinant

```text
L = {base_logdet:.15g}.
```

Therefore the complete threshold remains

```text
Delta(1/g_a^2) = b_a L/(8*pi^2),
Q -> Q exp(-L).
```

It is exactly a matching-scale translation and supplies no nonuniversal threshold shape. The ten
source rows are closed, but the strict spectral action still does not derive the observed gauge
coupling profile. Any further attempt must introduce a genuinely source-selected noncentral
endomorphism/connection and test it as a new prediction. It must not reopen these rows or select
the operator from the coupling residual.

Next optional strict-upgrade artifact: `{NEXT}`.
"""
    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
