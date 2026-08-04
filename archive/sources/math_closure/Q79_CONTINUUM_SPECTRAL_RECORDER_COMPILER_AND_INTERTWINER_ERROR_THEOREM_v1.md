# q79 Continuum Spectral-Recorder Compiler and Intertwiner-Error Theorem v1

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
