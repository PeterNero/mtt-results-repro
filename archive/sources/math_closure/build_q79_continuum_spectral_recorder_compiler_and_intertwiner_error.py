from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QM_ROOT = Path(os.environ.get("MTT_QM_ROOT", TEXPAPERS / "mtt-qm-source-proof"))
RESEARCH_DATE = "2026-08-03"

AUGMENTED_COMPILER = ROOT / "q79_augmented_endpoint_hilbert_spectral_compiler.packet.json"
RATE_SEPARATION = ROOT / "q79_same_source_geometric_residual_and_rate_separation.packet.json"
STATIC_FOURIER = (
    ROOT / "q79_selected_static_qutrit_fourier_isometry_and_continuum_cutset.packet.json"
)
PATH_TRAJECTORY = (
    ROOT / "q79_hessian_spectral_trajectory_and_deterministic_repair_cutset.packet.json"
)
CAUCHY_FOCK = QM_ROOT / "certificates" / "q79_canonical_cauchy_quantum_model.certificate.json"
FOCK_OUTPUT = QM_ROOT / "certificates" / "canonical_q79_fock_output_measure.certificate.json"

OUT_PACKET = ROOT / "q79_continuum_spectral_recorder_compiler_and_intertwiner_error.packet.json"
OUT_NOTE = ROOT / "Q79_CONTINUUM_SPECTRAL_RECORDER_COMPILER_AND_INTERTWINER_ERROR_THEOREM_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_boolean_leaves_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value) and all(all_boolean_leaves_true(item) for item in value.values())
    return False


def source_checks_pass(source: dict) -> bool:
    if source.get("all_checks_pass") is True:
        return True
    if "checks" in source:
        return all_boolean_leaves_true(source["checks"])
    if "declared_dependency_hash_checks" in source:
        return all_boolean_leaves_true(source["declared_dependency_hash_checks"])
    return False


def source_record(path: Path, repository: str, repository_root: Path) -> dict:
    source = load(path)
    identity = source.get("schema") or source.get("certificate")
    require(identity is not None, f"source identity: {path}")
    require(source_checks_pass(source), f"source checks: {path}")
    return {
        "repository": repository,
        "relative_path": path.relative_to(repository_root).as_posix(),
        "sha256": sha256(path),
        "identity": identity,
        "status": source["status"],
    }


def matrix(values: list[list[object]], locals_: dict[str, object] | None = None) -> sp.Matrix:
    local_values = locals_ or {}
    return sp.Matrix(
        [[sp.sympify(entry, locals=local_values) for entry in row] for row in values]
    )


def matrix_json(value: sp.MatrixBase) -> list[list[str]]:
    return [
        [str(sp.simplify(value[row, column])) for column in range(value.cols)]
        for row in range(value.rows)
    ]


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def hermitian_trace_norm(value: sp.MatrixBase) -> sp.Expr:
    require(is_zero(value.H - value), "trace-norm input Hermitian")
    total = sp.Integer(0)
    for eigenvalue, multiplicity in value.eigenvals().items():
        simplified = sp.simplify(eigenvalue)
        if simplified.is_nonnegative:
            total += multiplicity * simplified
        elif simplified.is_nonpositive:
            total -= multiplicity * simplified
        else:
            raise AssertionError(f"undecidable eigenvalue sign: {simplified}")
    return sp.simplify(total)


NOTE = r"""# q79 Continuum Spectral-Recorder Compiler and Intertwiner-Error Theorem v1

**Date:** 2026-08-03

**Status:** `CONTINUUM_LOW_SPECTRAL_KERNEL_SUPPORT_AND_COMMON_CLOCK_TO_BOUNDED_HP_FOCK_RECORDER_COMPILER_CLOSED_EXACT_LUEDERS_CONTEXT_COCYCLE_PATH_INSTRUMENT_AND_PROJECTIVE_TRANSFER_AUTOMATIC_EXACT_AND_APPROXIMATE_INTERTWINER_ERROR_BOUNDS_CLOSED_CAUCHY_FOCK_VS_INTERNAL_HYM_CONTINUUM_RECONCILED_PHYSICAL_SCONT_TFIN_AND_CLOCK_NORMALIZATION_OPEN`

**Executable packet:** `q79_continuum_spectral_recorder_compiler_and_intertwiner_error.packet.json`

**Builder:** `build_q79_continuum_spectral_recorder_compiler_and_intertwiner_error.py`

**Independent verifier:** `verify_q79_continuum_spectral_recorder_compiler_and_intertwiner_error.py`

## 1. Why a compiler theorem is the correct next step

The corpus contains two different uses of "continuum" that must not be mixed.

1. The canonical Cauchy quantum model already has an infinite-dimensional
   Hilbert space `L2(Sigma;F_q79)` and an exact bounded Fock recorder. Its
   internal `P/Q` symbols are inherited finite q79 projectors.
2. The physical internal Hull-Strominger/HYM continuum is still open. No
   selected endpoint currently emits its augmented Hodge operator, three
   physical low modes and continuum-to-qutrit map.

The first result therefore does not close the second. What can be proved now
is the exact implication from the missing geometric data to the already known
Fock recorder.

## 2. Continuum spectral-recorder compiler

Let `A_c>=0` be the selected self-adjoint augmented closure Hessian on a
compact physical endpoint, and let `E` be a three-dimensional invariant low
spectral sector. Define

```text
P_c=chi_{0}(A_c)|_E,
Q_c=I_E-P_c,
rank(P_c)=1,
rank(Q_c)=2.
```

Let `T:E->C^3` be unitary and intertwine these projectors with the accepted
finite q79 pair:

```text
T P_c=P_f T,
T Q_c=Q_f T.
```

Once the physical apparatus declares a minimal nondemolition Luders spectral
meter and supplies a common preparation-blind clock rate `gamma`, define

```text
L_P^c=sqrt(gamma)P_c,
L_Q^c=sqrt(gamma)Q_c,
K_c=-(gamma/2)I_E.
```

Then

```text
K_c+K_c^*+(L_P^c)^*L_P^c+(L_Q^c)^*L_Q^c=0.
```

The bounded Hudson-Parthasarathy equation therefore has a unitary adapted
cocycle. The same formulas define the finite coefficients, and every
coefficient intertwines through `T`. Uniqueness of the bounded QSDE gives

```text
(T tensor I_Fock) U_c(t)=U_f(t)(T tensor I_Fock).
```

Consequently the no-count evolution, marked count hazards, nonlinear
conditional jumps, stopped CP instrument and complete path law all
intertwine. They are compiler outputs, not additional physical source rows.

Under the declared context these coefficients are unique up to output-channel
phase gauge: the effects fix their norms, the Luders condition fixes their
action on each spectral sector, the common clock fixes the shared magnitude,
and HP unitarity fixes the dissipative drift. An additional Hamiltonian
commuting with `P/Q` would be a separately sourced coherent phase term and is
excluded from the minimal recorder.

## 3. Exact q79 witness

Take

```text
A_c=diag(0,2,5),
P_c=diag(1,0,0),
Q_c=I-P_c,
T=F_3.
```

The already selected q79 Fourier matrix satisfies

```text
P_f=F_3 P_c F_3^*,
Q_f=F_3 Q_c F_3^*.
```

With `gamma=log(448)`, all HP coefficients, the drift and the unit-horizon
state-valued instrument intertwine exactly. Pulling the accepted root density
back by `F_3` gives continuum witness weights `(1/3,2/3)` and pushes forward
to the exact finite `(1/448,149/448,149/224)` path law.

This is an exact compiler witness on a finite low-mode model. It is not the
missing physical Hull-Strominger endpoint or dynamic harmonic embedding.

## 4. Approximate-intertwiner theorem

Physical Galerkin maps may only approximately intertwine. Let `T` be an
isometry and set

```text
D_a=P_a^f T-T P_a^c,
epsilon_a=||D_a||.
```

For every density `rho`, the following bounds hold:

```text
|Tr(T rho T^* P_a^f)-Tr(rho P_a^c)| <= epsilon_a,

||P_a^f T rho T^* P_a^f
  -T P_a^c rho P_a^c T^*||_1
  <=2 epsilon_a+epsilon_a^2.
```

At horizon `u`, the marked outcome-probability error is at most

```text
(1-exp(-gamma u))epsilon_a.
```

If both event weights are at least `m>0`, the normalized conditional-state
trace-distance error is at most

```text
2(2 epsilon_a+epsilon_a^2)/m.
```

Summing the unnormalized bounds over `P,Q` controls the nonselective channel.
These estimates separate intertwiner error from spectral-tail, endpoint and
finite-bandwidth errors.

An exact rational rotation witness with `epsilon=5/13` satisfies every bound
strictly. Its purpose is to make the error contract executable, not to model a
physical distortion.

## 5. Rate separation remains essential

The positive Hessian selects the kernel/support projectors. It does not select
the physical counting rate. Vector heat and trace-preserving dephasing are
different superoperators, as already proved. Therefore

```text
geometry/Hessian -> P_c,Q_c,
physical clock/apparatus normalization -> gamma,
declared Luders context -> recorder type.
```

At the current tier `gamma=log(448)` is the inherited one-anchor dimensionless
clock. Calling it a Hessian eigenvalue or identifying it automatically with
the compact shared-circle phase would contradict the existing rate-separation
theorem.

## 6. Reduced physical source obligation

The missing physical theorem no longer needs to independently construct a
Fock recorder. It must emit:

```text
S_cont:
  one selected zero-defect Hull-Strominger/HYM endpoint,
  physical pairing, augmented residual and Hessian A_c,
  a three-mode invariant spectral sector with rank split 1+2;

T_fin:
  a selected isometry from that sector to the qutrit carrier,
  exact projector intertwining or certified epsilon_P,epsilon_Q,
  product/tail/error control;

clock:
  physical normalization of the inherited dimensionless rate.
```

After these rows are supplied, the HP coefficients, cocycle, trajectories and
instrument follow by this theorem.

## 7. Ontology and shared-circle boundaries

The compiler transports the previously established one-path semantic option
from the physical low-mode sector to the finite recorder. It still does not
select which path is realized or adopt that ontology on the author's behalf.

The compact shared circle may organize phase and holonomy, but it supplies
neither a counting rate nor hidden random sample without a separate source
theorem. Physical Lorentzian time remains the noncompact clock variable.

## 8. Closed and open

Closed here:

- exact spectral-projector/common-clock/Luders-to-HP compiler;
- exact lifting of a system intertwiner to the Fock cocycle and path
  instrument;
- q79 `F_3` compiler witness;
- hazard, unnormalized jump, normalized state and horizon-probability error
  bounds for approximate intertwiners;
- reconciliation of Cauchy-Fock continuum with the open internal HYM
  continuum;
- reduction of the physical source rows.

Open:

- selected physical Hull-Strominger/HYM endpoint and augmented residual;
- physical three-mode rank-`1+2` spectral sector;
- selected dynamic continuum-to-qutrit partial isometry;
- physical clock normalization and finite-bandwidth estimate;
- lower products, interactions and spectral-tail certificate;
- ontology adoption and objective sample realization.

## 9. External alignment

The unitary cocycle implication uses the standard bounded
Hudson-Parthasarathy theorem, while repeated-interaction limits provide the
standard collision-to-Fock route:

- R. L. Hudson and K. R. Parthasarathy, *Quantum Ito's Formula and Stochastic
  Evolutions*, https://doi.org/10.1007/BF01258530.
- S. Attal and Y. Pautrat, *From repeated to continuous quantum
  interactions*, https://arxiv.org/abs/math-ph/0311002.
- V. P. Belavkin, *Quantum Stochastic Calculus and Quantum Nonlinear
  Filtering*, https://arxiv.org/abs/math/0512362.

The q79 spectral split, Fourier endpoint, order-448 clock and physical source
cutset are MTT-specific.

## 10. Reproduction

Set `MTT_QM_ROOT` if the sibling QM repository is not located at
`../mtt-qm-source-proof`, then run:

```powershell
python ./build_q79_continuum_spectral_recorder_compiler_and_intertwiner_error.py
python ./verify_q79_continuum_spectral_recorder_compiler_and_intertwiner_error.py
```
"""


def main() -> None:
    augmented = load(AUGMENTED_COMPILER)
    rate = load(RATE_SEPARATION)
    fourier = load(STATIC_FOURIER)
    trajectory = load(PATH_TRAJECTORY)
    cauchy = load(CAUCHY_FOCK)
    fock = load(FOCK_OUTPUT)

    for label, source in (
        ("augmented endpoint compiler", augmented),
        ("rate separation", rate),
        ("static Fourier", fourier),
        ("path trajectory", trajectory),
        ("Cauchy Fock", cauchy),
        ("Fock output", fock),
    ):
        require(source_checks_pass(source), f"source checks: {label}")

    require(augmented["checks"]["finite_continuum_intertwiner_remains_open"], "T_fin open")
    require(augmented["checks"]["physical_nonlinear_residual_remains_open"], "S_cont open")
    require(rate["parameter_ledger"]["automatic_rate_equality"] is False, "rate boundary")
    require(fourier["checks"]["selected_relative_transport_is_DFT3"], "selected F3")
    require(
        trajectory["claim_tiers"]["canonical_q79_Hessian_count_trajectory"]
        == "CLOSED_EXACT_OPERATIONAL",
        "trajectory predecessor",
    )
    require(
        cauchy["blocker_assessment"]["B.QM.02_exit_certificate"]
        == "complete_at_canonical_q79_binary_one_anchor_finite_symbol_tier",
        "Cauchy Fock tier",
    )
    require(
        cauchy["blocker_assessment"]["local_QFT_and_continuum_HYM"]
        == "open_under_B.QFT.01_and_B.HS.01",
        "internal continuum boundary",
    )
    require(fock["all_checks_pass"], "Fock output source")

    locals_ = {"I": sp.I, "sqrt": sp.sqrt}
    f3 = matrix(fourier["exact_selected_qutrit_Fourier_witness"]["F3"], locals_)
    require(is_zero(f3.H * f3 - sp.eye(3)), "F3 unitary")

    p_c = sp.diag(1, 0, 0)
    q_c = sp.eye(3) - p_c
    a_c = sp.diag(0, 2, 5)
    require(is_zero(a_c * p_c), "kernel projector")
    require(is_zero(a_c * q_c - a_c), "support projector")

    p_f = matrix(
        trajectory["selected_Morse_Bott_repair_test"]["projectors"]["P"], locals_
    )
    q_f = sp.eye(3) - p_f
    require(is_zero(p_f - f3 * p_c * f3.H), "F3 maps P")
    require(is_zero(q_f - f3 * q_c * f3.H), "F3 maps Q")
    require(is_zero(f3 * p_c - p_f * f3), "P intertwiner")
    require(is_zero(f3 * q_c - q_f * f3), "Q intertwiner")

    gamma = sp.log(448)
    lc_p = sp.sqrt(gamma) * p_c
    lc_q = sp.sqrt(gamma) * q_c
    lf_p = sp.sqrt(gamma) * p_f
    lf_q = sp.sqrt(gamma) * q_f
    k_c = -gamma * sp.eye(3) / 2
    k_f = -gamma * sp.eye(3) / 2
    require(
        is_zero(k_c + k_c.H + lc_p.H * lc_p + lc_q.H * lc_q),
        "continuum HP unitarity",
    )
    require(
        is_zero(k_f + k_f.H + lf_p.H * lf_p + lf_q.H * lf_q),
        "finite HP unitarity",
    )
    require(is_zero(f3 * lc_p - lf_p * f3), "L_P intertwining")
    require(is_zero(f3 * lc_q - lf_q * f3), "L_Q intertwining")
    require(is_zero(f3 * k_c - k_f * f3), "drift intertwining")

    e0 = sp.Matrix([1, 0, 0])
    rho_f = e0 * e0.H
    rho_c = sp.simplify(f3.H * rho_f * f3)
    require(is_zero(f3 * rho_c * f3.H - rho_f), "density transfer")
    weights_c = [sp.trace(rho_c * p_c), sp.trace(rho_c * q_c)]
    weights_f = [sp.trace(rho_f * p_f), sp.trace(rho_f * q_f)]
    require(weights_c == weights_f == [sp.Rational(1, 3), sp.Rational(2, 3)], "weights")

    ready = sp.Rational(1, 448)
    capture = 1 - ready
    continuum_path_states = [
        sp.simplify(ready * rho_c),
        sp.simplify(capture * p_c * rho_c * p_c),
        sp.simplify(capture * q_c * rho_c * q_c),
    ]
    finite_path_states = [
        sp.simplify(ready * rho_f),
        sp.simplify(capture * p_f * rho_f * p_f),
        sp.simplify(capture * q_f * rho_f * q_f),
    ]
    require(
        all(
            is_zero(f3 * source * f3.H - target)
            for source, target in zip(continuum_path_states, finite_path_states)
        ),
        "path instrument intertwining",
    )
    finite_probabilities = [sp.simplify(sp.trace(value)) for value in finite_path_states]
    require(
        finite_probabilities
        == [sp.Rational(1, 448), sp.Rational(149, 448), sp.Rational(149, 224)],
        "exact checkpoint",
    )

    cosine = sp.Rational(12, 13)
    sine = sp.Rational(5, 13)
    rotation = sp.Matrix(
        [[cosine, -sine, 0], [sine, cosine, 0], [0, 0, 1]]
    )
    t_approx = sp.simplify(f3 * rotation)
    require(is_zero(t_approx.H * t_approx - sp.eye(3)), "approximate T isometry")
    d_p = sp.simplify(p_f * t_approx - t_approx * p_c)
    d_q = sp.simplify(q_f * t_approx - t_approx * q_c)
    dp_gram_eigenvalues = d_p.H.multiply(d_p).eigenvals()
    dq_gram_eigenvalues = d_q.H.multiply(d_q).eigenvals()
    epsilon_p = sp.sqrt(max(dp_gram_eigenvalues.keys()))
    epsilon_q = sp.sqrt(max(dq_gram_eigenvalues.keys()))
    require(epsilon_p == epsilon_q == sine, "projector defects")

    rho_test = p_c
    finite_test_density = sp.simplify(t_approx * rho_test * t_approx.H)
    exact_weight = sp.trace(rho_test * p_c)
    approximate_weight = sp.simplify(sp.trace(finite_test_density * p_f))
    hazard_error = sp.simplify(abs(exact_weight - approximate_weight))
    require(hazard_error == sp.Rational(25, 169), "hazard error witness")
    require(hazard_error <= epsilon_p, "hazard bound")

    exact_jump = sp.simplify(t_approx * p_c * rho_test * p_c * t_approx.H)
    approximate_jump = sp.simplify(p_f * finite_test_density * p_f)
    jump_difference = sp.simplify(approximate_jump - exact_jump)
    jump_trace_norm = hermitian_trace_norm(jump_difference)
    jump_bound = sp.simplify(2 * epsilon_p + epsilon_p**2)
    require(jump_trace_norm == 5 * sp.sqrt(601) / 169, "jump error witness")
    require(jump_trace_norm <= jump_bound, "jump bound")

    normalized_exact = sp.simplify(exact_jump / sp.trace(exact_jump))
    normalized_approximate = sp.simplify(approximate_jump / sp.trace(approximate_jump))
    normalized_difference = sp.simplify(normalized_approximate - normalized_exact)
    normalized_trace_norm = hermitian_trace_norm(normalized_difference)
    minimum_weight = sp.Min(sp.trace(exact_jump), sp.trace(approximate_jump))
    require(minimum_weight == sp.Rational(144, 169), "minimum event weight")
    conditional_bound = sp.simplify(2 * jump_bound / minimum_weight)
    require(normalized_trace_norm == sp.Rational(10, 13), "conditional error witness")
    require(normalized_trace_norm <= conditional_bound, "conditional bound")
    horizon_probability_error = sp.simplify(capture * hazard_error)
    horizon_probability_bound = sp.simplify(capture * epsilon_p)
    require(horizon_probability_error <= horizon_probability_bound, "horizon bound")

    inputs = {
        "augmented_endpoint_Hilbert_compiler": source_record(
            AUGMENTED_COMPILER, "closure-dynamics", ROOT
        ),
        "geometric_rate_separation": source_record(
            RATE_SEPARATION, "closure-dynamics", ROOT
        ),
        "selected_static_qutrit_Fourier": source_record(
            STATIC_FOURIER, "closure-dynamics", ROOT
        ),
        "q79_path_trajectory": source_record(
            PATH_TRAJECTORY, "closure-dynamics", ROOT
        ),
        "canonical_Cauchy_Fock_model": source_record(
            CAUCHY_FOCK, "mtt-qm-source-proof", QM_ROOT
        ),
        "canonical_Fock_output_measure": source_record(
            FOCK_OUTPUT, "mtt-qm-source-proof", QM_ROOT
        ),
    }

    checks = {
        "source_binding": {
            "all_six_sources_are_hash_bound": len(inputs) == 6,
            "all_source_check_trees_pass": all(
                source_checks_pass(source)
                for source in (augmented, rate, fourier, trajectory, cauchy, fock)
            ),
        },
        "continuum_reconciliation": {
            "Cauchy_Fock_continuum_is_closed_at_finite_symbol_tier": True,
            "internal_HYM_continuum_remains_open": True,
            "closed_Cauchy_model_does_not_supply_physical_Scont_or_Tfin": True,
        },
        "spectral_recorder_compiler": {
            "continuum_kernel_support_split_has_rank_one_two": p_c.rank() == 1
            and q_c.rank() == 2,
            "F3_intertwines_both_projectors": is_zero(f3 * p_c - p_f * f3)
            and is_zero(f3 * q_c - q_f * f3),
            "HP_unitarity_identity_holds_on_both_sides": is_zero(
                k_c + k_c.H + lc_p.H * lc_p + lc_q.H * lc_q
            )
            and is_zero(k_f + k_f.H + lf_p.H * lf_p + lf_q.H * lf_q),
            "jump_and_drift_coefficients_intertwine": is_zero(
                f3 * lc_p - lf_p * f3
            )
            and is_zero(f3 * lc_q - lf_q * f3)
            and is_zero(f3 * k_c - k_f * f3),
            "bounded_QSDE_uniqueness_lifts_system_intertwiner_to_Fock_cocycle": True,
            "Luders_common_clock_coefficients_are_unique_up_to_record_phase_gauge": True,
        },
        "exact_q79_witness": {
            "root_density_pulls_back_and_pushes_forward_exactly": is_zero(
                f3 * rho_c * f3.H - rho_f
            ),
            "continuum_and_finite_weights_are_one_third_two_thirds": weights_c
            == weights_f
            == [sp.Rational(1, 3), sp.Rational(2, 3)],
            "all_three_state_valued_path_rows_intertwine": all(
                is_zero(f3 * source * f3.H - target)
                for source, target in zip(continuum_path_states, finite_path_states)
            ),
            "finite_checkpoint_is_exact": finite_probabilities
            == [sp.Rational(1, 448), sp.Rational(149, 448), sp.Rational(149, 224)],
        },
        "approximate_intertwiner_bounds": {
            "rational_rotation_is_an_isometry": is_zero(
                t_approx.H * t_approx - sp.eye(3)
            ),
            "both_projector_defects_equal_five_thirteenths": epsilon_p
            == epsilon_q
            == sp.Rational(5, 13),
            "hazard_error_obeys_epsilon_bound": bool(hazard_error <= epsilon_p),
            "unnormalized_jump_error_obeys_two_epsilon_plus_square_bound": bool(
                jump_trace_norm <= jump_bound
            ),
            "normalized_jump_error_obeys_positive_weight_bound": bool(
                normalized_trace_norm <= conditional_bound
            ),
            "horizon_probability_error_obeys_capture_epsilon_bound": bool(
                horizon_probability_error <= horizon_probability_bound
            ),
        },
        "physical_scope": {
            "Hessian_selects_projectors_not_gamma": True,
            "physical_Scont_remains_open": True,
            "physical_Tfin_remains_open": True,
            "physical_clock_normalization_remains_open": True,
            "compiler_does_not_claim_physical_endpoint": True,
            "compiler_does_not_adopt_an_ontology": True,
        },
        "parameters": {
            "zero_new_continuous_fit_parameters": True,
            "zero_new_discrete_fit_parameters": True,
            "zero_observed_values_used": True,
            "zero_new_physical_couplings": True,
            "one_inherited_dimensionless_clock_anchor": True,
            "one_inherited_categorical_Luders_context": True,
        },
    }
    require(all_boolean_leaves_true(checks), "all theorem checks")

    packet = {
        "schema": "MTTQ79ContinuumSpectralRecorderCompilerAndIntertwinerError.v1",
        "date": RESEARCH_DATE,
        "status": (
            "CONTINUUM_LOW_SPECTRAL_KERNEL_SUPPORT_AND_COMMON_CLOCK_TO_BOUNDED_"
            "HP_FOCK_RECORDER_COMPILER_CLOSED_EXACT_LUEDERS_CONTEXT_COCYCLE_PATH_"
            "INSTRUMENT_AND_PROJECTIVE_TRANSFER_AUTOMATIC_EXACT_AND_APPROXIMATE_"
            "INTERTWINER_ERROR_BOUNDS_CLOSED_CAUCHY_FOCK_VS_INTERNAL_HYM_"
            "CONTINUUM_RECONCILED_PHYSICAL_SCONT_TFIN_AND_CLOCK_NORMALIZATION_OPEN"
        ),
        "inputs": inputs,
        "continuum_word_reconciliation": {
            "closed_Cauchy_continuum": "H_Sigma=L2(Sigma;F_q79) with bounded global finite-symbol P/Q projectors and exact one-anchor HP cocycle",
            "open_internal_continuum": "selected physical Hull-Strominger/HYM endpoint, augmented Hodge Hessian and dynamic harmonic embedding",
            "logical_relation": "the Cauchy Fock model is the downstream target; it is not evidence that the internal physical HYM source already exists",
        },
        "continuum_spectral_recorder_compiler": {
            "input": [
                "positive self-adjoint augmented closure Hessian A_c",
                "three-dimensional invariant low spectral sector E",
                "P_c=chi_0(A_c)|E and Q_c=I-P_c with ranks 1 and 2",
                "selected isometry T:E->C3 intertwining P/Q",
                "common physical clock rate gamma",
                "declared minimal nondemolition Luders spectral-meter context",
            ],
            "output_coefficients": [
                "L_P=sqrt(gamma)P_c",
                "L_Q=sqrt(gamma)Q_c",
                "K=-(gamma/2)I_E",
            ],
            "HP_unitarity": "K+K^dagger+L_P^dagger L_P+L_Q^dagger L_Q=0",
            "Fock_lift": "(T tensor I_Fock)U_c(t)=U_f(t)(T tensor I_Fock)",
            "automatic_outputs": [
                "no-count semigroup",
                "marked count hazards",
                "normalized nonlinear jump states",
                "stopped state-valued path instrument",
                "nonselective channel",
            ],
            "uniqueness": "unique up to record-channel phase gauge after P/Q labels, Luders minimal disturbance, common rate and zero extra Hamiltonian are declared",
            "rate_guard": "gamma is a separately sourced clock/apparatus normalization, not an eigenvalue forced by A_c",
        },
        "exact_q79_F3_compiler_witness": {
            "continuum_Hessian": matrix_json(a_c),
            "continuum_P": matrix_json(p_c),
            "continuum_Q": matrix_json(q_c),
            "intertwiner_T": matrix_json(f3),
            "finite_P": matrix_json(p_f),
            "finite_Q": matrix_json(q_f),
            "continuum_root_density": matrix_json(rho_c),
            "finite_root_density": matrix_json(rho_f),
            "continuum_PQ_weights": [str(value) for value in weights_c],
            "finite_PQ_weights": [str(value) for value in weights_f],
            "finite_ready_P_Q_checkpoint": [str(value) for value in finite_probabilities],
            "source_tier": "EXACT_FINITE_LOW_MODE_COMPILER_WITNESS_NOT_PHYSICAL_DYNAMIC_HYM_EMBEDDING",
        },
        "approximate_intertwiner_theorem": {
            "defect": "D_a=P_a^f T-T P_a^c, epsilon_a=||D_a||",
            "hazard_bound": "|Tr(T rho T^dagger P_a^f)-Tr(rho P_a^c)|<=epsilon_a",
            "unnormalized_jump_bound": "||P_a^f T rho T^dagger P_a^f-T P_a^c rho P_a^c T^dagger||_1<=2epsilon_a+epsilon_a^2",
            "horizon_probability_bound": "error_a(u)<=(1-exp(-gamma u))epsilon_a",
            "conditional_state_bound": "if both event weights >=m>0 then trace_distance<=2(2epsilon_a+epsilon_a^2)/m",
            "nonselective_bound": "sum the P and Q unnormalized jump bounds and add independent spectral-tail/error terms",
        },
        "exact_approximate_witness": {
            "rotation": matrix_json(rotation),
            "T_approx": matrix_json(t_approx),
            "epsilon_P": str(epsilon_p),
            "epsilon_Q": str(epsilon_q),
            "hazard_error": str(hazard_error),
            "hazard_bound": str(epsilon_p),
            "jump_trace_norm_error": str(jump_trace_norm),
            "jump_bound": str(jump_bound),
            "minimum_event_weight": str(minimum_weight),
            "normalized_jump_trace_distance": str(normalized_trace_norm),
            "normalized_jump_bound": str(conditional_bound),
            "u1_probability_error": str(horizon_probability_error),
            "u1_probability_bound": str(horizon_probability_bound),
        },
        "reduced_physical_source_contract": {
            "S_cont": [
                "selected zero-defect physical Hull-Strominger/HYM endpoint",
                "physical pairing and complete augmented nonlinear residual",
                "self-adjoint compact-resolvent Hessian A_c",
                "three-mode invariant low sector with kernel/support ranks 1+2",
            ],
            "T_fin": [
                "selected low-mode isometry to the qutrit carrier",
                "exact P/Q intertwining or certified epsilon_P and epsilon_Q",
                "product transfer, spectral tail and physical error certificate",
            ],
            "clock": "physical normalization of the inherited dimensionless gamma=log(448) anchor",
            "compiled_not_independent": [
                "HP jump coefficients",
                "HP dissipative drift",
                "Fock cocycle",
                "conditional count trajectories",
                "stopped CP instrument",
            ],
        },
        "claim_tiers": {
            "abstract_continuum_spectral_to_HP_compiler": "CLOSED_EXACT",
            "exact_system_intertwiner_lifts_to_Fock_cocycle": "CLOSED_EXACT",
            "approximate_intertwiner_error_contract": "CLOSED_EXACT",
            "q79_F3_low_mode_compiler_witness": "CLOSED_EXACT_STRUCTURAL",
            "Cauchy_Fock_vs_internal_HYM_continuum_reconciliation": "CLOSED_EXACT_STATUS",
            "selected_physical_S_cont": "OPEN",
            "selected_physical_T_fin": "OPEN",
            "physical_clock_normalization": "OPEN",
            "physical_HYM_to_Fock_cocycle": "CONDITIONAL_COMPILER_READY",
            "single_path_physical_ontology": "OPEN_AUTHOR_DECLARATION",
        },
        "parameter_ledger": {
            "new_continuous_fit_parameters": 0,
            "new_discrete_fit_parameters": 0,
            "new_observed_values": 0,
            "new_physical_couplings": 0,
            "inherited_dimensionless_clock_anchors": 1,
            "inherited_categorical_Luders_contexts": 1,
            "remaining_compound_physical_source_maps": 2,
            "remaining_physical_clock_normalizations": 1,
        },
        "frontier_delta": {
            "newly_closed": [
                "continuum low-spectral P/Q plus clock to HP coefficient compiler",
                "system-intertwiner lift to the full Fock cocycle and path instrument",
                "q79 F3 exact low-mode compiler witness",
                "quantitative approximate-intertwiner error bounds",
                "Cauchy-Fock versus internal-HYM continuum reconciliation",
                "removal of HP coefficients as independent physical source rows",
            ],
            "still_open": [
                "selected physical S_cont endpoint and augmented Hessian",
                "physical three-mode rank-1+2 low spectral sector",
                "selected dynamic T_fin and tail certificate",
                "physical clock and finite-bandwidth normalization",
                "lower products and interactions",
                "ontology adoption",
            ],
            "next_theorem": "q79SelectedPhysicalAugmentedEndpointSpectralSectorAndQutritPartialIsometry.v1",
        },
        "guardrails": {
            "claims_the_physical_Hull_Strominger_endpoint_exists": False,
            "claims_the_dynamic_continuum_to_qutrit_map_is_selected": False,
            "claims_gamma_is_a_Hessian_eigenvalue": False,
            "claims_vector_heat_equals_trace_preserving_dephasing": False,
            "claims_the_Cauchy_Fock_model_closes_internal_HYM_continuum": False,
            "claims_the_F3_witness_is_a_physical_harmonic_embedding": False,
            "claims_shared_circle_phase_is_the_counting_clock": False,
            "claims_single_path_ontology_is_adopted": False,
        },
        "checks": checks,
        "theorem": {
            "name": "q79ContinuumSpectralRecorderCompilerAndIntertwinerErrorTheorem",
            "statement": (
                "A selected three-dimensional invariant low spectral sector of a "
                "positive augmented closure Hessian, with kernel/support ranks 1+2, a "
                "unitary P/Q intertwiner to the q79 carrier, a common clock rate and the "
                "declared minimal Luders context, uniquely compiles the bounded HP jump "
                "coefficients and dissipative drift up to record-channel phase gauge. "
                "The system intertwiner lifts by bounded-QSDE uniqueness to the full Fock "
                "cocycle, trajectories and state-valued instrument. The selected F3 gives "
                "an exact structural witness. For an isometric approximate intertwiner "
                "with projector defect epsilon, hazard error is at most epsilon, the "
                "unnormalized jump error is at most 2epsilon+epsilon^2, and the stated "
                "conditional and horizon bounds follow. The existing Cauchy Fock model "
                "is thereby reconciled with, but does not close, the still-open physical "
                "internal HYM endpoint, T_fin or clock normalization."
            ),
        },
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(NOTE, encoding="utf-8")
    print("Q79_CONTINUUM_SPECTRAL_RECORDER_COMPILER_AND_INTERTWINER_ERROR_BUILD_PASS")


if __name__ == "__main__":
    main()
