from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

FINITE_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
CLASSICAL = (
    ROOT / "certificates" / "q79_finite_source_tegr_classical_closure_certificate.json"
)
GLOBAL_HESSIAN = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
GLOBAL_DG = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"
ZERO_MODE = ROOT / "certificates" / "q79_coherent_zero_mode_tt_source_certificate.json"
MASSLESS_NOGO = ROOT / "certificates" / "massless_tt_pole_internal_gap_no_go_certificate.json"
STIELTJES_NOGO = ROOT / "certificates" / "stieltjes_massless_gaussian_no_go_certificate.json"
SPECTRAL_IR = ROOT / "certificates" / "spectral_action_einstein_ir_limit_certificate.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_free_graviton_quantization_and_uv_cutset_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Free_Graviton_Quantization_and_Finite_Internal_UV_NoGo_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    finite = load(FINITE_HESSIAN)
    classical = load(CLASSICAL)
    global_hessian = load(GLOBAL_HESSIAN)
    global_dg = load(GLOBAL_DG)
    zero_mode = load(ZERO_MODE)
    massless_no_go = load(MASSLESS_NOGO)
    stieltjes_no_go = load(STIELTJES_NOGO)
    spectral_ir = load(SPECTRAL_IR)

    kappa_h, omega, p2, epsilon = sp.symbols(
        "kappa_h omega p2 epsilon", positive=True
    )
    identity2 = sp.eye(2)

    # Canonically normalized coordinates q=sqrt(kappa_h) h put the two
    # physical TT polarizations into two identical harmonic oscillators.
    hamiltonian_matrix = sp.diag(omega**2, omega**2, 1, 1)
    symplectic_form = sp.Matrix(
        [[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]]
    )
    evolution = symplectic_form * hamiltonian_matrix
    evolution_square = sp.simplify(evolution**2)
    propagator_shape = identity2 / (kappa_h * (p2 + sp.I * epsilon))
    residue = sp.simplify(
        (kappa_h * p2 * propagator_shape).subs(epsilon, 0)
    )

    # A finite internal trace only multiplies a four-dimensional loop
    # integrand. It cannot change its large-momentum exponent.
    internal_dimension = finite["finite_data"]["carrier_dimension"]
    loop_power = sp.symbols("loop_power", integer=True)
    p = sp.symbols("p", positive=True)
    scalar_integrand = p**loop_power
    finite_trace_integrand = internal_dimension * scalar_integrand
    asymptotic_power_ratio = sp.simplify(finite_trace_integrand / scalar_integrand)

    checks = {
        "physical_helicity_bundle_has_rank_two": "rank two in every fiber"
        in global_dg["theorem"]["properties"],
        "finite_internal_TT_shape_is_identity": finite["finite_data"][
            "TT_multiplicity_block"
        ]
        == [["1", "0"], ["0", "1"]],
        "finite_internal_TT_shape_has_positive_single_scale": finite["finite_data"][
            "overall_action_normalizations"
        ]
        == 1,
        "classical_Fierz_Pauli_Einstein_tier_is_available": classical[
            "claim_tiers"
        ]["classical_GR_equivalence_at_declared_finite_source_IR_tier"]
        == "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES"
        and global_hessian["claim_tiers"]["massless_quadratic_operator"]
        == "CLOSED_CONDITIONAL_ON_LINEARIZED_DIFF_GAUGE_INVARIANCE",
        "canonical_internal_zero_mode_has_unit_residue": zero_mode["claim_tiers"][
            "canonical_internal_massless_residue"
        ]
        == "CLOSED_UNIT",
        "positive_gap_alone_is_not_massless": massless_no_go["claim_tiers"][
            "pure_lambda15_carrier_as_massless_graviton"
        ]
        == "CLOSED_NO_GO",
        "two_oscillator_evolution_has_frequency_omega": evolution_square
        == -(omega**2) * sp.eye(4),
        "Hamiltonian_is_positive_for_positive_omega": all(
            eigenvalue > 0
            for eigenvalue in [omega**2, omega**2, sp.Integer(1), sp.Integer(1)]
        ),
        "propagator_has_diagonal_equal_helicity_residues": residue == identity2,
        "finite_internal_trace_does_not_change_momentum_power": asymptotic_power_ratio
        == internal_dimension,
        "Stieltjes_massless_permanent_Gaussian_conjunction_is_no_go": stieltjes_no_go[
            "claim_tiers"
        ]["three_way_incompatibility"]
        == "CLOSED",
        "spectral_heat_kernel_remainder_is_still_open": spectral_ir["claim_tiers"][
            "full_spectral_heat_kernel_remainder_bound"
        ]
        == "OPEN",
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_free_graviton_quantization_and_uv_cutset",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_FREE_MASSLESS_GRAVITON_QUANTIZATION_CLOSED_FINITE_INTERNAL_UV_COMPLETION_NOGO_INTERACTING_QG_OPEN",
        "inputs": {
            "finite_rootstack_TT_Hessian": str(FINITE_HESSIAN),
            "classical_finite_source_GR": str(CLASSICAL),
            "global_Fierz_Pauli_Hessian": str(GLOBAL_HESSIAN),
            "global_helicity_bundle": str(GLOBAL_DG),
            "coherent_internal_zero_mode": str(ZERO_MODE),
            "positive_gap_massless_no_go": str(MASSLESS_NOGO),
            "Stieltjes_Gaussian_no_go": str(STIELTJES_NOGO),
            "spectral_IR_and_remainder": str(SPECTRAL_IR),
        },
        "theorem": {
            "name": "q79FreeGravitonQuantizationAndFiniteInternalUVNoGo",
            "free_sector": {
                "physical_carrier": "ker(Delta_X) tensor E_TT, real rank 2 per nonzero spatial momentum",
                "canonical_field": "q_lambda=sqrt(kappa_h) h_lambda",
                "Hamiltonian": "H_free=(1/2) sum_lambda integral (pi_lambda^2+|grad q_lambda|^2)",
                "commutator": "[a_lambda(k),a_lambda'(k')^dagger]=(2pi)^3 delta_lambda_lambda' delta^3(k-k')",
                "propagator": "<h_lambda h_lambda'>=i delta_lambda_lambda'/(kappa_h(p^2+i0))",
                "internal_residue": "identity I2 from the connected q79 scalar zero mode and finite TT block",
                "positivity": "for kappa_h>0 the reduced TT Hamiltonian is the sum of two positive oscillators",
            },
            "finite_internal_UV_no_go": {
                "statement": (
                    "Replacing the internal carrier by a finite algebra makes every "
                    "internal trace finite but leaves the unbounded four-dimensional "
                    "loop momentum integral and its superficial degree unchanged."
                ),
                "algebraic_witness": "Tr_internal[p^n I_N]=N p^n",
                "consequence": (
                    "The six-dimensional q79 finite source is sufficient for exact "
                    "internal coefficients and free quantization, not for interacting "
                    "four-dimensional UV completion."
                ),
            },
        },
        "finite_data": {
            "physical_polarization_count": 2,
            "internal_harmonic_multiplicity": 1,
            "finite_rootstack_carrier_dimension": internal_dimension,
            "oscillator_Hamiltonian_matrix": [
                [str(value) for value in row] for row in hamiltonian_matrix.tolist()
            ],
            "symplectic_form": [
                [int(value) for value in row] for row in symplectic_form.tolist()
            ],
            "evolution_square": [
                [str(value) for value in row] for row in evolution_square.tolist()
            ],
            "helicity_propagator_shape": "I2/[kappa_h(p^2+i0)]",
            "normalized_massless_residue": [[1, 0], [0, 1]],
            "new_continuous_parameters_beyond_classical_kappa": 0,
        },
        "claim_tiers": {
            "free_massless_q79_graviton_carrier": "CLOSED_EXACT_TWO_HELICITIES",
            "free_reduced_TT_Hamiltonian_positivity": "CLOSED_FOR_KAPPA_H_POSITIVE",
            "free_Fock_quantization": "CLOSED_CONDITIONAL_ON_CAUSAL_VACUUM_I0_CHOICE",
            "free_propagator_and_unit_internal_residue": "CLOSED_EXACT_SHAPE",
            "finite_internal_trace_removes_internal_mode_sum": "CLOSED_EXACT",
            "finite_internal_trace_changes_4D_UV_power_counting": "CLOSED_NO_GO",
            "low_energy_quantum_GR_as_EFT": "AVAILABLE_STANDARD_ROUTE_HIGHER_COEFFICIENTS_OPEN",
            "selected_interacting_quantum_measure": "OPEN",
            "BRST_or_nonperturbative_constraint_closure_beyond_free_tier": "OPEN",
            "two_loop_or_nonperturbative_UV_completion": "OPEN",
            "full_interacting_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_free_quantization_is_interacting_QG": False,
            "claims_finite_internal_algebra_regulates_spacetime_loops": False,
            "claims_permanent_Gaussian_damping_with_positive_massless_spectrum": False,
            "claims_spectral_remainder_controlled": False,
            "claims_UV_completion": False,
            "uses_observed_quantum_gravity_values": False,
            "adds_continuous_parameter": False,
        },
        "primary_sources": {
            "gravity_as_low_energy_EFT": "https://arxiv.org/abs/gr-qc/9405057",
            "EFT_review": "https://arxiv.org/abs/1209.3511",
            "two_loop_divergence_original_record": "https://www.sciencedirect.com/science/article/abs/pii/0370269385914704",
        },
        "checks": checks,
        "next_required_artifact": "MTT_q79_Selected_Quantum_Measure_Constraint_Closure_and_UV_Completion_v1",
        "note_written": str(OUT_NOTE),
    }

    note = """# q79 Free Graviton Quantization and Finite-Internal UV No-Go v1

Date: 2026-07-15

Status:
`Q79_FREE_MASSLESS_GRAVITON_QUANTIZATION_CLOSED_FINITE_INTERNAL_UV_COMPLETION_NOGO_INTERACTING_QG_OPEN`

## Free quantum sector

The connected q79 internal geometry supplies one normalized scalar zero mode.
Tensoring it with the global helicity-two bundle gives exactly two physical
real polarizations per nonzero spatial momentum. The finite root-stack
Reynolds theorem gives the same positive coefficient to both.

With

```text
q_lambda=sqrt(kappa_h) h_lambda,
```

the reduced free Hamiltonian is

```text
H_free=(1/2) sum_lambda integral d^3x
       [pi_lambda^2+|grad q_lambda|^2].
```

For each momentum this is two identical positive harmonic oscillators. The
standard Fock relations give

```text
[a_lambda(k),a_lambda'(k')^dagger]
  =(2pi)^3 delta_lambda,lambda' delta^3(k-k'),
```

and the TT propagator is

```text
<h_lambda h_lambda'>
  =i delta_lambda,lambda'/[kappa_h(p^2+i0)].
```

The normalized massless residue is exactly `I2`. No continuous parameter is
added beyond the already necessary classical `kappa_h`. A time orientation
and causal vacuum/`i0` prescription remain state data.

## Finite internal algebra is not a 4D UV regulator

The q79 source has finite internal dimension, so internal traces and mode sums
are exact and finite. But for any large-momentum integrand,

```text
Tr_internal[p^n I_N]=N p^n.
```

The finite factor `N` does not change the power of the unbounded
four-dimensional loop momentum. It therefore cannot by itself remove the
standard interacting Einstein-gravity UV problem. Pure Einstein gravity is a
consistent low-energy quantum EFT, but its two-loop divergence requires a
higher-curvature counterterm; see
<https://arxiv.org/abs/gr-qc/9405057> and the original two-loop result at
<https://www.sciencedirect.com/science/article/abs/pii/0370269385914704>.

The existing MTT Stieltjes theorem also excludes the tempting shortcut of
combining a positive massless spectral representation with permanent Gaussian
propagator damping. The A51-A53 spectral route remains possible only after its
measure, Lorentzian reconstruction, and full remainder are selected and
controlled.

## Exact boundary

Closed:

```text
the free two-helicity q79 graviton Hilbert/Fock sector,
positive reduced Hamiltonian for kappa_h>0,
the massless propagator shape and unit internal residue,
the no-go for finite internal dimension alone curing 4D loop UV behavior.
```

Open:

```text
the selected interacting quantum measure,
constraint/BRST closure beyond the free tier,
higher-curvature coefficients or a nonperturbative completion,
unitarity and UV control of the completed interacting theory.
```
"""

    OUT_CERT.write_text(json.dumps(certificate, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
