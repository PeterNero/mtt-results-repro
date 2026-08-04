# QM Minimal Recorder-Action Frontier Report

Date: 2026-07-23

Kernel handoff: `bc1736db-f07a-4918-ad19-571cf9f83b3d`

Controlling rows: `B.QM.01`, `B.ACTION.01`, `B.COLLAPSE.01`

## Starting Frontier

The five-output context functor was closed conditional on a selected
variational-spectral apparatus action. The remaining local apparatus questions
were:

- which q79 interaction selects an informative instrument;
- which pointer algebra carries stable `P/Q` records;
- whether the interaction emits the required quadratic capture hazards.

The existing two-state pointer isometry did not answer those source questions
because the same nonselective channel also has a random-unitary instrument.

## New Action Theorem

The q79 pair
\[
P=P_{\rm Haar},
\qquad
Q=I-P
\]
fixes the minimal interaction gauge class under the candidate principle

```text
A_rec: minimal unbiased nondemolition q79 recorder.
```

For defect/no-defect recording, the unique two-state gauge representative is

\[
H_2=\kappa_C Q\otimes\sigma_y.
\]

It exponentiates to

\[
K_r=P+\cos\theta\,Q,
\qquad
K_d=\sin\theta\,Q,
\]

and exactly recovers the prior `(7/25,24/25)` informative instrument.

## Pointer-Dimension Upgrade

Two pointer states cannot contain:

```text
one ready state
+ one stable P record
+ one stable Q record.
```

The minimum physical two-outcome capture pointer therefore has dimension three.
Its action is

\[
H_3=\kappa_C
\left(
P\otimes Y_{rP}+Q\otimes Y_{rQ}
\right).
\]

Starting from the ready state, its instrument is

\[
K_r=\cos\theta\,I,
\qquad
K_P=\sin\theta\,P,
\qquad
K_Q=\sin\theta\,Q.
\]

The outgoing diagonal qutrit algebra is atomic, commutative and stable after
the pointer decouples.

## Exact Semigroup

Choose each fresh-pointer interaction by

\[
\cos^2\theta_\Delta=e^{-\gamma_C\Delta}.
\]

Then

\[
\Phi_\Delta(\rho)
=e^{-\gamma_C\Delta}\rho
+(1-e^{-\gamma_C\Delta})(P\rho P+Q\rho Q),
\]

and

\[
\Phi_\Delta^n=\Phi_{n\Delta}
\]

exactly on every time grid. The generator is simultaneously

\[
\mathcal L_C(\rho)
=\gamma_C(P\rho P+Q\rho Q-\rho)
\]

and

\[
\mathcal L_C(\rho)
=\frac{\gamma_C}{2}(Z\rho Z-\rho).
\]

Its jump operators are

\[
L_P=\sqrt{\gamma_C}P,
\qquad
L_Q=\sqrt{\gamma_C}Q.
\]

Thus the cause-specific hazards are

\[
h_P=\gamma_C\|P\psi\|^2,
\qquad
h_Q=\gamma_C\|Q\psi\|^2.
\]

This is the exact quadratic capture-clock shape required by the previous
first-capture theorem.

## Continuous-Time Guard

A fixed bounded finite-pointer Hamiltonian gives cosine attenuation with zero
initial dissipative slope. It cannot equal \(e^{-\gamma_Ct}\) for positive
`gamma_C` on an interval.

The exact grid construction has

\[
\theta_\Delta^2
=\gamma_C\Delta+O(\Delta^2),
\]

so a controlled continuum realization requires the standard fresh-ancilla,
Fock-space or singular weak-coupling limit. This aligns with established
repeated-interaction results:

- [Attal and Pautrat](https://arxiv.org/abs/math-ph/0311002)
- [Ciccarello et al.](https://arxiv.org/abs/2106.11974)
- [Grimmer et al.](https://arxiv.org/abs/1605.04302)

## Exact Witness

The certificate uses `cos(theta)=4/5`, `sin(theta)=3/5`:

```text
one-step attenuation:   16/25
three-step attenuation: 4096/15625
eventual q79 records:   (1/3,2/3), if the trace rule is available
```

## Frontier Delta

Closed conditionally:

- minimal two-state q79 defect-recorder action;
- minimum three-state ready/`P`/`Q` capture action;
- stable outgoing record algebra;
- physically informative instrument;
- exact repeated-interaction semigroup;
- quadratic `P/Q` jump hazards.

Still open:

1. upper-MTT derivation or explicit adoption of `A_rec`;
2. the profile-selected value of `gamma_C`;
3. the controlled continuous field/Fock limit;
4. the realized-record probability law without importing Born weights;
5. extension to every allowed apparatus context.

Parameter impact:

```text
candidate structural principles:       1
new universal dimensionless parameters: 0
new fits:                               0
new observed construction inputs:       0
```

## Verification

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```

Expected totals:

```text
all exact checks: 262/262
new recorder-action checks: 29/29
unit tests: 22/22
source hashes: 16/16 current
```
