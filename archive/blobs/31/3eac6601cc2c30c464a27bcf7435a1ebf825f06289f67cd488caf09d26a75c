---
abstract: |
  We audit the Lens x Nil Bianchi formulas used as the source of the
  determinant-seven CP block.  With the structure equations and flux ansatz
  stated in the corpus, the forms beta_1 and beta_3 are not closed, so a
  nonzero formula dH=W_1 beta_1+W_3 beta_3 would violate d^2H=0.  Moreover the
  stated abelian flux F=f eta12+h sigma45 squares to the cross term
  2fh eta12 sigma45, not to f^2 beta_1+h^2 beta_3.  Therefore the current
  Lens-Nil appendix cannot by itself prove the Z_7 block.  The proof can still
  be rescued, but only after replacing the Lens-Nil component system by a
  closed/differential-character-correct system whose exact Smith normal form is
  recomputed.
author:
- Peter Nero
date: May 2026
title: |
  Lens-Nil Bianchi Consistency Obstruction and Correction Path
---

# Executive conclusion

The attempted proof cannot be finished from the Lens-Nil appendix as currently
written.

The obstruction is algebraic:

```text
d^2H must be zero.
```

But the stated Lens-Nil component formula uses non-closed component forms:

```text
d beta_1 != 0,
d beta_3 != 0.
```

Therefore:

```text
dH = W_1 beta_1 + W_3 beta_3
```

with nonzero constant `W_1,W_3` cannot be correct as a literal exterior
calculus identity.

# Check 1: beta forms are not closed

Using the stated structure equations:

```text
d eta^i = epsilon_ijk eta^j wedge eta^k,
d sigma^6 = sigma^4 wedge sigma^5,
```

and:

```text
beta_1 = eta^1 eta^2 eta^3 sigma^6,
beta_3 = eta^3 sigma^4 sigma^5 sigma^6,
```

the audit gives:

```text
d beta_1 = - e^12345,
d beta_3 =   e^12456.
```

These supports are distinct, so no nonzero linear combination:

```text
W_1 beta_1 + W_3 beta_3
```

is closed unless:

```text
W_1 = W_3 = 0.
```

Thus the claimed nonzero `dH` expansion cannot be literal.

# Check 2: the stated flux square has wrong support

The appendix states:

```text
F = 2 pi T (f eta^1 eta^2 + h sigma^4 sigma^5).
```

For this abelian two-form:

```text
F wedge F = 2 f h eta^1 eta^2 sigma^4 sigma^5.
```

That is:

```text
F^2 = 2fh beta_2,
beta_2 = eta^1 eta^2 sigma^4 sigma^5.
```

It is not:

```text
f^2 beta_1 + h^2 beta_3.
```

Indeed:

```text
(eta^1 eta^2)^2 = 0,
(sigma^4 sigma^5)^2 = 0.
```

So the flux component equations used for the determinant-seven block are not
consistent with the displayed flux ansatz.

# Consequence for the Z_7 route

The determinant-seven block:

```text
[[2,1],
 [1,4]]
```

remains a beautiful formal candidate, but it is not proved by the current
Lens-Nil appendix.

The specific route:

```text
Lens-Nil dH/R_+^2/F^2 coefficients
        ->
K_LN = [[2,1],[1,4]]
        ->
Z_7
```

is blocked until the underlying Lens-Nil component system is corrected.

# Correction path

There are three viable ways forward.

## Path A: repair the Lens-Nil geometry

Find the intended closed invariant/differential-character basis and recompute:

```text
dH,
Tr F^2,
Tr R_+^2.
```

Then reduce the exact integer matrix by Smith normal form.

This is the cleanest route if the original appendix had a basis or flux typo.

## Path B: change the flux ansatz

The flux ansatz must contain two-form components whose wedge products actually
land in the desired closed component directions.

For example, terms involving:

```text
eta^1 eta^2,
eta^3 sigma^6,
sigma^4 sigma^5
```

can generate different four-form supports through cross terms.  But the result
must be closed and compatible with quantization.

After changing the flux, recompute the exact Smith normal form.  Do not assume
the determinant remains seven.

## Path C: abandon Lens-Nil as the Z_7 source

Keep the formal arithmetic theorem:

```text
K with SNF [7] gives Z_7.
```

But search for the required primitive determinant-seven matrix in another
fixed arithmetic sector:

```text
central circle/lens/nil character lattice,
orbifold projection,
Freed-Witten congruence,
torsion subgroup,
or another flux/holonomy component system.
```

# Updated proof status

The following are still valid:

```text
Hom(coker [[2,1],[1,4]], U(1)) ~= Z_7.
Z_64 x Z_7 ~= Z_448.
Z_1344 / Z_3-family ~= Z_448.
```

But the Lens-Nil appendix does not currently prove the premise:

```text
K_LN = [[2,1],[1,4]].
```

# Next action

The next research task is now clear:

```text
recompute the Lens-Nil Bianchi/flux/curvature system from exterior calculus.
```

If the recomputation produces a protected matrix with SNF `[7]`, the proof can
continue.  If it does not, the `Z_7` factor must be sourced elsewhere.

