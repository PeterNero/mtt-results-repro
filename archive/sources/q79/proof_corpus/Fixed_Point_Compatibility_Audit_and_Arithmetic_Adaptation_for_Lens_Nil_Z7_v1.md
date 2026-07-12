---
abstract: |
  We audit the Fixed Points series against the Lens-Nil determinant-seven CP
  descent program.  The analytic fixed-point results hold for the parts we use:
  bounded Riesz coherent projectors under spectral gaps and bounded geometry,
  joint circle-lens-nil projectors, nil noncollapse spectral gaps, and
  disturbance-damping stability.  But these papers do not by themselves prove
  that the coherent projector preserves an integral character, Bianchi, or
  gerbe lattice.  For the Z_7 proof we therefore need an arithmetic
  fixed-sector addendum: topological/differential-cohomology labels are held
  locally constant, the coherent/invariant subspace is equipped with an
  integral lattice before scalar extension, and the Lens-Nil matrix
  [[2,1],[1,4]] is protected as an exact integer block.
author:
- Peter Nero
date: May 2026
title: |
  Fixed Point Compatibility Audit and Arithmetic Adaptation for the Lens-Nil Z_7 Descent
---

# Purpose

The Lens-Nil sevenfold route now depends on the descent:

```text
componentwise Lens x Nil Bianchi data
        ->
residual Wilson/nil CP character lattice.
```

The Fixed Points series is used to justify:

```text
coherent projector,
bounded geometry,
spectral gap,
stable admissible sector.
```

This note checks what already holds and what must be adapted.

# What Holds Analytically

## FP I: Riesz projector framework

Fixed Points I assumes:

```text
bounded fiber geometry,
uniform fiber spectral gap,
constant harmonic rank,
coherent projector defined by Riesz spectral calculus.
```

It proves that the coherent projector is bounded on the relevant Sobolev
scales:

```text
Pi_coh: H^1 -> H^1 bounded,
Ran(Pi_coh) closed.
```

This is exactly the analytic projector technology needed for the descent
program.

## FP I caveat: projected vs true equilibria

FP I also includes an important warning:

```text
If N(Ran Pi_coh) is not contained in Ran Pi_coh,
then a fixed point of Pi_coh Phi_t need not be a true equilibrium of Phi_t.
```

For the Z_7 program this means:

```text
the CP lattice descent must be stated on the coherent admissible sector,
or one must assume coherence invariance for the relevant character variables.
```

This is not a failure.  It is a condition to state explicitly.

## FP II: 10D joint projector

Fixed Points II defines:

```text
Pi_coh = Pi_B1 Pi_B2 Pi_B3.
```

The fiberwise projectors commute and the joint range is:

```text
Ran Pi_coh = ker Delta_B1 cap ker Delta_B2 cap ker Delta_B3.
```

Under bounded geometry and spectral gap:

```text
Pi_coh is H^1-bounded,
Ran Pi_coh is closed.
```

This supports the circle-lens-nil coherent sector used in the flavor program.

## FP III: nil spectral gap and stability

Fixed Points III gives:

```text
noncollapsing compact nil fibers have lambda_1 >= c_* > 0.
```

It also supplies the disturbance-damping criterion:

```text
gamma_{n,k} > 0,
Sigma < infinity.
```

Thus the nil side is analytically stable provided the Lens-Nil metric remains
in the noncollapsing bounded-geometry class.

## FP V and VI: selection as admissibility

Fixed Points V treats persistence of admissibility under controlled
disturbances.  Fixed Points VI explicitly treats selection functionals as:

```text
meta-level admissibility constraints,
not new dynamics.
```

This aligns with using Bianchi/gerbe consistency as an admissibility gate rather
than as a new force.

# What Does Not Yet Follow

The Fixed Points papers are analytic.  They do not automatically imply:

```text
Pi_coh preserves an integral lattice.
```

A Riesz/orthogonal projector is defined over real or complex Hilbert spaces.
It can preserve a finite-dimensional subspace without preserving a chosen
integer lattice inside that subspace.

For the determinant-seven proof, however, we need exact arithmetic:

```text
K = [[2,1],[1,4]],
det(K)=7.
```

Small real perturbations can be analytically harmless while still destroying an
exact integer determinant statement if they alter the relation matrix.

# Required Arithmetic Addendum

The Fixed Points series should be supplemented by an arithmetic fixed-sector
addendum with these assumptions.

## Addendum A: Fixed Integral Sector

On each admissible slab, fix:

```text
an integral topological/differential-cohomology sector Lambda_Z.
```

Continuous fixed-point flow may vary metrics, connections, and representatives
inside this sector, but it may not change the integral sector without crossing
an admissibility boundary.

In the Lens-Nil case:

```text
flux integers,
Bianchi component labels,
gerbe class,
and residual character labels
```

are locally constant discrete data.

This fixed-sector language is directly supported by the Strominger/heterotic
selection paper, where the B-field is treated as a Deligne 2-gerbe connection,
variations are taken inside a fixed differential-cohomology class, and the
selection theorem is stated in a fixed topological sector.

## Addendum B: Arithmetic Coherent Subsector

Define an integral coherent lattice:

```text
Lambda_coh,Z subset Lambda_Z
```

such that:

```text
Lambda_coh,Z tensor R
```

is the coherent/invariant subspace used analytically by `Pi_coh`.

The analytic projector is then the scalar extension of a lattice-level
selection, rather than an arbitrary real projection expected to preserve
integrality.

## Addendum C: Differential-Cohomology Component Lattice

Because the individual Lens-Nil forms `beta_1,beta_3` are not closed, the
lattice should not be stated as:

```text
H^4 generated by beta_1,beta_3.
```

It should be stated as:

```text
the integral Bianchi/gerbe component lattice selected by the invariant
coherent sector.
```

This is the lattice whose unitary dual may carry the residual Wilson/nil CP
characters.

## Addendum D: Exact Integer Block Protection

The integer block:

```text
K_LN = [[2,1],[1,4]]
```

must be protected as an exact relation matrix in the fixed integral sector.

Analytic corrections may perturb real metric coefficients, but they must not
alter the integral relation matrix unless the model crosses into a different
discrete sector.  Otherwise the determinant-seven result is not protected.

This point is especially important because the Lens x Nil curvature appendix
writes:

```text
A = 4 lambda^2 + O(lambda^2 nu^2),
B = 4 nu^2     + O(lambda^2 nu^2).
```

So a final proof must show that the correction terms do not change the
fixed-sector integer character matrix, or that the exact matrix is
GL(2,Z)-equivalent to `[[2,1],[1,4]]`.

## Addendum E: Character Dual Identification

The remaining main theorem must identify:

```text
(w,n) in Hom(Lambda_coh,Z / K_LN Lambda_coh,Z, U(1)).
```

Then:

```text
Hom(coker K_LN, U(1)) ~= Z_7.
```

# Status Ledger

The executable status check is:

```text
fixed_point_descent_alignment_check.py
```

It reports:

```text
FP I projector/gap framework                         HOLDS
FP I projected-equilibrium caveat                    HOLDS WITH CAVEAT
FP II joint circle-lens-nil projector                HOLDS
FP III nil noncollapse spectral gap                  HOLDS
FP III/V disturbance-damping persistence             HOLDS
FP VI selection as admissibility                     HOLDS
Pi_coh preserves an integral character/gerbe lattice NEEDS ADDENDUM
fixed topological sector is locally constant         NEEDS ADDENDUM
[[2,1],[1,4]] exactness under corrections            NEEDS ADDENDUM
CP labels w,n are dual to that lattice               OPEN PROOF TARGET
```

# Proposed Insert for Future FP Revision

A concise paragraph to add to the Fixed Points framework is:

```text
Arithmetic fixed-sector convention.  When coherent sectors carry topological,
flux, gerbe, or character data, the analytic coherent projector is understood
after fixing an integral sector Lambda_Z.  The coherent arithmetic sublattice
Lambda_coh,Z is selected before extension of scalars to R or C, and the Riesz
projector acts on Lambda_coh,Z tensor R.  Continuous fixed-point evolution may
vary representatives inside a fixed sector but does not change the integral
sector unless an admissibility boundary is crossed.
```

For the Lens-Nil Z_7 descent, add:

```text
In the Lens x Nil invariant sector, the Bianchi/gerbe component lattice is
part of the fixed arithmetic data.  The determinant-seven block K_LN must be
an exact integer relation matrix on this lattice; analytic perturbations may
renormalize metric coefficients but may not change K_LN within the same
discrete sector.
```

# Bottom line

The Fixed Points papers hold for the analytic use we make of them.

They need one clear adaptation for this flavor program:

```text
add an arithmetic/differential-cohomology fixed-sector layer.
```

With that addendum, the fixed-point framework aligns cleanly with the Lens-Nil
determinant-seven descent program.
