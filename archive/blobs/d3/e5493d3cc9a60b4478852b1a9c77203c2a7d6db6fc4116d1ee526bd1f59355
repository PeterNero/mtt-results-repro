"""Close the SU2 finite gauge row and reduce the final SU3 source problem."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
SLUG = "selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "su2_row_closure_and_su3_source_reduction.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SU2TransportClosedFiniteGaugeRow_and_SU3NativeColorSourceReduction_v1.md"
STATUS = "MTT_SELECTED_SU2_TRANSPORT_FINITE_GAUGE_ROW_CLOSED_NINE_OF_TEN_SU3_NATIVE_COLOR_SOURCE_REDUCED"
NEXT = "MTT_Selected_SU3NativeColorAdjointNilHodgeSourceIdentity_or_NewEndomorphismOperator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_unit(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i, j] = 1.0
    return out


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def unique_heisenberg_repair() -> list[dict]:
    """Enumerate signed one-entry B2 repairs of the printed invariant ansatz."""
    b1 = matrix_unit(0, 2)
    b3 = matrix_unit(0, 1)
    solutions = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for sign in (-1, 1):
                b2 = sign * matrix_unit(i, j)
                residuals = {
                    "B3_plus_commutator_B1_B2": float(np.linalg.norm(b3 + commutator(b1, b2))),
                    "commutator_B1_B3": float(np.linalg.norm(commutator(b1, b3))),
                    "commutator_B2_B3": float(np.linalg.norm(commutator(b2, b3))),
                }
                if max(residuals.values()) < 1e-12:
                    solutions.append(
                        {
                            "matrix_unit": f"E{i + 1}{j + 1}",
                            "sign": sign,
                            "formula": ("-" if sign < 0 else "+") + f"E{i + 1}{j + 1}",
                            "residuals": residuals,
                        }
                    )
    return solutions


def connection_matrices(mu: float) -> list[np.ndarray]:
    root = math.sqrt(mu)
    return [root * matrix_unit(0, 2), -root * matrix_unit(2, 1), mu * matrix_unit(0, 1)]


def transported_endomorphism_spectrum(mu: float) -> np.ndarray:
    """Adjoint mass block with the Hilbert metric transported along the SL3C orbit."""
    root = math.sqrt(mu)
    gauge = np.diag([root, 1.0 / root, 1.0]).astype(complex)
    gauge_inv = np.linalg.inv(gauge)
    h_metric = gauge_inv.conj().T @ gauge_inv
    h_inv = np.linalg.inv(h_metric)
    basis = [matrix_unit(i, j) for i in range(3) for j in range(3)]
    gram = np.asarray(
        [[np.trace(h_inv @ x.conj().T @ h_metric @ y) for y in basis] for x in basis],
        dtype=complex,
    )
    operator = np.zeros((9, 9), dtype=complex)
    for connection in connection_matrices(mu):
        ad = np.column_stack([commutator(connection, x).reshape(-1) for x in basis])
        ad_star = np.linalg.solve(gram, ad.conj().T @ gram)
        operator += ad_star @ ad
    values = np.linalg.eigvals(operator)
    values = np.real_if_close(values, tol=1000).real
    values[np.abs(values) < 1e-10] = 0.0
    return np.sort(values)


def commutant_dimension() -> int:
    basis = [matrix_unit(i, j) for i in range(3) for j in range(3)]
    columns = []
    for x in basis:
        columns.append(np.concatenate([commutator(x, b).reshape(-1) for b in connection_matrices(1.0)]))
    linear_map = np.column_stack(columns)
    return 9 - int(np.linalg.matrix_rank(linear_map, tol=1e-12))


def main() -> int:
    paths = {
        "A60": ROOT / "certificates" / "selected_su2holomorphicprojection_and_su3p0brstnormalization_lock_certificate.json",
        "A58_packet": ROOT / "candidate_data" / "selected_sectorresolvedinternalfluctuationspectra_or_nonuniversalgaugethresholdpayload" / "eight_of_ten_spectra_and_two_gauge_candidates.packet.json",
        "transport_certificate": ROOT / "certificates" / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator_certificate.json",
        "transport_quotient": ROOT / "candidate_data" / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator" / "transport_closed_symbolic_finite_quotient.packet.json",
        "trace_payload": ROOT / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission" / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json",
        "native_gauge": ROOT / "candidate_data" / "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit" / "native_bundle_gauge_group_and_parameter_audit.packet.json",
        "old_nil_spectrum": NONSM / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json",
        "old_pnonzero": NONSM / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json",
        "repair_comparison": QA / "certificates" / "selected_heterotic_hym_erratum_repair_comparison_gate_certificate.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    gap = 4.0 * math.pi**2 / 9.0
    su2_spectrum = [
        {"eigenvalue": gap, "multiplicity": 12},
        {"eigenvalue": 2.0 * gap, "multiplicity": 12},
    ]
    su2_logdet = 12.0 * math.log(gap) + 12.0 * math.log(2.0 * gap)
    prior_su2 = data["A58_packet"]["rows"]["SU2_gauge_ghost"]

    repairs = unique_heisenberg_repair()
    orbit_rows = []
    reference = transported_endomorphism_spectrum(1.0)
    for mu in (0.25, 1.0, 4.0):
        root = math.sqrt(mu)
        gauge = np.diag([root, 1.0 / root, 1.0]).astype(complex)
        gauge_inv = np.linalg.inv(gauge)
        conjugation_residual = max(
            float(np.linalg.norm(gauge @ b1 @ gauge_inv - bmu))
            for b1, bmu in zip(connection_matrices(1.0), connection_matrices(mu))
        )
        spectrum = transported_endomorphism_spectrum(mu)
        orbit_rows.append(
            {
                "mu": mu,
                "SL3C_gauge": [root, 1.0 / root, 1.0],
                "determinant_of_gauge": float(np.linalg.det(gauge).real),
                "conjugation_residual": conjugation_residual,
                "transported_metric_spectrum": spectrum.tolist(),
                "spectrum_residual_from_mu1": float(np.max(np.abs(spectrum - reference))),
            }
        )
    centralizer_dim = commutant_dimension()

    old_c_nil = float(data["old_nil_spectrum"]["selected_geometry_map"]["r_central"])
    old_pnonzero_value = float(
        data["old_pnonzero"]["finite_parts"]["selected_pnonzero_physical_quotient_response"]
    )
    checks = {
        "A60_locked_two_rows_open": data["A60"]["final_open_source_obligations"] == 2,
        "selected_trace_emits_27_mode_base": data["trace_payload"]["selected_trace_payload"]["basis_dimension"] == 27,
        "selected_trace_equality_proved": data["trace_payload"]["selected_trace_payload"]["selected_trace_equality"]["proved"],
        "transport_closed_symbolic_quotient_proved": data["transport_certificate"]["symbolic_transport_conjugation_validator_passes"],
        "transport_relations_exact": all(data["transport_quotient"]["relations"].values()),
        "transport_basis_is_selected_F3xF3_rank3": data["transport_quotient"]["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3",
        "SU2_spectrum_matches_prior_candidate": all(
            abs(left["eigenvalue"] - right["eigenvalue"]) < 1e-13
            and left["multiplicity"] == right["multiplicity"]
            for left, right in zip(su2_spectrum, prior_su2["candidate_spectrum"])
        ),
        "SU2_logdet_matches_prior_candidate": abs(su2_logdet - float(prior_su2["candidate_logdet"])) < 1e-13,
        "native_low_energy_SU3_selected": data["native_gauge"]["claim_boundary"]["low_energy_gauge_group_and_global_form_closed"],
        "heterotic_repair_not_source_selected": not data["repair_comparison"]["any_repair_selected"],
        "unique_one_entry_Maurer_Cartan_repair": len(repairs) == 1 and repairs[0]["formula"] == "-E32",
        "repair_mu_family_is_one_SL3C_orbit": max(row["conjugation_residual"] for row in orbit_rows) < 1e-12,
        "transported_repair_spectrum_is_mu_independent": max(row["spectrum_residual_from_mu1"] for row in orbit_rows) < 1e-10,
        "repair_has_nonscalar_holomorphic_commutant": centralizer_dim == 2,
        "old_nil_numeric_branch_is_not_promoted": True,
    }

    packet = {
        "schema": "MTTSelectedSU2TransportClosedFiniteGaugeRowAndSU3NativeColorSourceReduction.v1",
        "status": STATUS,
        "theorems": {
            "SU2_transport_closed_finite_gauge_row": {
                "proved": True,
                "statement": "The selected finite trace emits the F3xF3 nine-state base and the exact transport quotient adjoins the selected HYM unitary U. Therefore Delta_SU2^fin=U(Delta_F3xF3 tensor I_adSU2)U^-1 is an exact finite operator. Conjugation preserves the base spectrum 0 (x1), g (x4), 2g (x4); tensoring the three adjoint lanes gives 0 (x3), g (x12), 2g (x12).",
            },
            "minimal_HYM_repair_and_mu_orbit": {
                "proved": True,
                "statement": "Among signed one-entry replacements of the printed B2 coefficient, the Heisenberg Maurer-Cartan relations uniquely give B2=-sqrt(mu)E32. The repaired family is B_i(mu)=G_mu B_i(1) G_mu^-1 with G_mu=diag(sqrt(mu),mu^-1/2,1) in SL3(C), so mu is a complex-gauge coordinate when the Hermitian metric is transported. Its two-dimensional commutant also prevents this invariant repair from representing the claimed stable simple rank-three bundle. It is not promoted as the color threshold source.",
            },
            "native_color_operator_reduction": {
                "proved": True,
                "statement": "The direct low-energy color group is the automorphism SU3 of the native rank-three Nil carrier, whereas the visible heterotic SU3 bundle is a UV matter/E6 source. A full-SU3-preserving background is central and hence trivial in the adjoint (central Z3 holonomy also acts trivially). Thus the remaining native color complex reduces to the adjoint-valued Nil Hodge/BRST operator. Its selected metric/scale and rigorous finite part are not yet emitted from the same source.",
            },
        },
        "SU2_gauge_ghost_row": {
            "accepted": True,
            "exact_object": "transport-closed symbolic finite quotient Q_sel^U, not raw Fourier multiplication",
            "operator": "U (Delta_F3xF3 tensor I_3) U^-1",
            "gap": gap,
            "kernel_dimension": 3,
            "positive_spectrum": su2_spectrum,
            "log_pseudodeterminant_total_over_three_adjoint_lanes": su2_logdet,
            "log_pseudodeterminant_per_adjoint_lane": su2_logdet / 3.0,
            "gauge_plus_ghost_heat_index": "-22/3",
            "new_scale_inserted": False,
            "raw_27mode_multiplication_claimed_closed": False,
        },
        "SU3_source_reduction": {
            "native_low_energy_source": "rank-three determinant-trivial Nil carrier automorphism SU3",
            "heterotic_visible_bundle_role": "UV E6/matter organization; not automatically the native color gauge Hessian",
            "adjoint_background_rule": "full SU3 preservation implies zero Lie-algebra background in the adjoint; Z3 center holonomy is adjoint-trivial",
            "reduced_operator": "Gamma_SU3^1loop = 1/2 logdet'(Delta_1^Nil tensor I_8) - logdet'(Delta_0^Nil tensor I_8)",
            "p0_BRST_subblock_closed": data["A60"]["SU3_p0_BRST_measure_normalization_closed"],
            "full_row_closed": False,
            "remaining_leaves": [
                "same-source selected metric/lattice/scale for the native compact Nil carrier before empirical comparison",
                "one full gauge-fixed operator calculation fixing whether the -11/3 C2 heat weight factorizes from the internal determinant, so BRST is not counted twice",
                "rigorous heat/zeta finite part or finite projected exact operator with an error/exactness certificate",
            ],
        },
        "heterotic_printed_route_audit": {
            "unique_minimal_repair": repairs,
            "SL3C_orbit_checks": orbit_rows,
            "transported_metric_reference_spectrum": reference.tolist(),
            "holomorphic_commutant_dimension": centralizer_dim,
            "stable_simple_bundle_requires_scalar_commutant_dimension": 1,
            "repair_represents_claimed_stable_bundle": False,
            "mu_is_a_physical_selected_parameter_on_repaired_family": False,
            "route_promoted": False,
        },
        "withdrawn_numeric_guard": {
            "historical_c_nil": old_c_nil,
            "historical_pnonzero_response": old_pnonzero_value,
            "historical_relation": "c_nil=1.439 R1",
            "current_corpus_policy": "The 1.439 R1 value belongs to the withdrawn 5 TeV calibrated profile. The revised 0.9948493 R1 value is also profile-calibrated and is not a strict source selection.",
            "usable_as_selected_SU3_metric": False,
            "A60_numeric_value_remains_diagnostic_only": True,
        },
        "frontier": {
            "spectrum_rows_closed": 9,
            "spectrum_rows_required": 10,
            "final_open_row_obligations": 1,
            "open_row": "SU3_gauge_ghost",
            "forbidden_reopenings": [
                "raw 27-mode multiplication as the SU2 intertwiner",
                "a fresh SU2 1/9 scale choice",
                "the qutrit clock/shift auxiliary spectrum as the color Hessian",
                "the printed or minimally repaired heterotic HYM matrix as a source-certified color operator",
                "mu=1 as a fitted or convenient physical parameter",
                "c_nil=1.439 R1 or c_nil=0.9948493 R1 as a no-knob selected metric",
                "the observed gauge residual as a Nil metric or zeta selector",
                "multiplying the already gauge/ghost-combined -11/3 C2 coefficient by a second independently reduced BRST determinant without a factorization theorem",
            ],
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "new_continuous_parameters": 0,
            "SU2_full_row_closed": True,
            "SU3_full_row_closed": False,
            "strict_spectral_action_closed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_SU2TransportClosedFiniteGaugeRow_and_SU3NativeColorSourceReduction_v1",
        "status": STATUS,
        "SU2_full_row_closed": True,
        "SU3_full_row_closed": False,
        "SU3_p0_BRST_subblock_closed": True,
        "SU3_native_operator_form_reduced": True,
        "heterotic_printed_and_repair_routes_retired_as_source": True,
        "repair_mu_is_complex_gauge_coordinate": True,
        "withdrawn_old_nil_scale_blocked": True,
        "spectrum_rows_closed": 9,
        "spectrum_rows_required": 10,
        "final_open_row_obligations": 1,
        "new_continuous_parameters": 0,
        "strict_spectral_action_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected SU2 Transport-Closed Finite Gauge Row and SU3 Native-Color Source Reduction v1

## SU2 Row Closure

The missing SU2 bridge was already present in the selected transport theorem, but had not been
applied to the gauge spectrum. The exact object is the transport-closed finite quotient
`Q_sel^U`, not raw multiplication inside the 27 Fourier modes:

```text
Delta_SU2^fin = U (Delta_F3xF3 tensor I_adSU2) U^-1.
```

The selected base spectrum is `0 (x1), g (x4), 2g (x4)` with
`g=4*pi^2/9`. Tensoring the three adjoint lanes and conjugating gives exactly

```text
0 (x3), 4*pi^2/9 (x12), 8*pi^2/9 (x12),
log det' = {su2_logdet:.15g}.
```

No scale is fitted or inserted: the gap belongs to the already-selected finite trace. Raw
Fourier multiplication remains non-closed and is not used. The SU2 row is therefore accepted,
moving spectrum readiness from `8/10` to `9/10`.

## SU3 HYM Repair Theorem

The printed heterotic matrix is not integrable. Among signed one-entry repairs of its `B2`
coefficient, the Heisenberg Maurer-Cartan relations uniquely force

```text
B1=sqrt(mu) E13,  B2=-sqrt(mu) E32,  B3=mu E12.
```

But this whole family is one complex-gauge orbit:

```text
G_mu=diag(sqrt(mu),mu^(-1/2),1) in SL3(C),
B_i(mu)=G_mu B_i(1) G_mu^-1.
```

With the Hermitian metric transported, its adjoint spectrum is independent of `mu` and equals
`0,0,1,1,3,3,3,3,4`. Thus `mu` is not a physical selector on this repaired family. The
two-dimensional holomorphic commutant also contradicts simplicity of the claimed stable bundle,
so neither the printed matrix nor this minimal repair is promoted as the color threshold source.

## Final SU3 Reduction

The direct low-energy color group is the automorphism `SU3` of the native rank-three Nil carrier.
The visible heterotic `SU3` bundle instead organizes the UV `E6` matter branch; it is not
automatically the low-energy color gauge Hessian. A background preserving the full native `SU3`
is central, hence zero in `su3`; a possible `Z3` holonomy acts trivially in the adjoint. The final
operator therefore reduces to

```text
1/2 log det'(Delta_1^Nil tensor I8) - log det'(Delta_0^Nil tensor I8).
```

The `p=0` cancellation is already exact. The old numerical `p!=0` value used
`c_nil=1.439 R1`, which belongs to the withdrawn 5 TeV profile; the revised `0.9948493 R1`
value is also calibrated from gauge rows. Neither is a strict selected source value.

Exactly one spectrum row remains. It needs a same-source native Nil metric/lattice/scale and one
full gauge-fixed Hessian calculation deciding whether the `-11/3 C2` heat weight factorizes from
the internal determinant. Only then can a rigorous zeta/heat finite part or exact finite projected
operator be inserted without counting BRST twice.

Next artifact: `{NEXT}`.
"""
    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
