---
abstract: |
  We prove the projector-compatibility bridge needed after the quantum-gravity
  alignment audit.  The exact statement is conditional but sharp: if the
  flavor closure operator L_fl is a self-adjoint internal block operator
  commuting with the coherent internal spectral data, and if the Z_64 flavor
  Riesz contour encloses only coherent-sector spectrum, then the finite flavor
  projector P_fl commutes with the QG/coherent projector Pi_coh and satisfies
  Ran(P_fl) subset Ran(Pi_coh).  Consequently the Schur complement used in the
  Z_64 proof is the same kind of coherent/noncoherent split used in the QG
  papers.  The crucial caveat is identified: raw nonzero Fourier characters on
  S^1_cen are not scalar Laplacian zero modes.  To be retained by Pi_coh they
  must be realized as twisted/equivariant holonomy sectors, or as a coherent
  spectral cluster selected by the internal projector.  Therefore the next
  concrete construction is the Z_64 CP analogue of that retained coherent
  central-circle sector.
author:
- Peter Nero
date: May 2026
title: |
  Flavor-QG Projector Compatibility Lemma for Z64 CKM Closure
---

# Purpose

The quantum-gravity alignment audit left two bridge tasks:

```text
1. prove P_fl is nested in or commutes with Pi_coh;
2. identify lambda_Q relative to the coherent/noncoherent gap.
```

This paper proves the first task under the exact blockwise spectral hypotheses
already used throughout the corpus.

It also sharpens the second task: `lambda_Q` is the gap of the selected flavor
Schur complement on the noncoherent complement of this common projector split.

# Corpus Inputs

## Joint coherent projector

The MTT Foundation says that under base-only warping:

```text
Delta_1, Delta_2, Delta_3 commute.
```

Therefore they admit a joint spectral resolution, and:

```text
Pi_coh = product_i 1_{0}(Delta_i).
```

If small fiber-dependent perturbations are present, the corpus tracks the
failure by:

```text
O(epsilon_warp).
```

## Riesz projectors commute with their operator

The fixed-point and projection corpus repeatedly uses:

```text
P = (1/2pi i) integral_Gamma (z-A)^(-1) dz.
```

When `P` is a Riesz projector of `A`, it commutes with `A` and with the
functional calculus of `A`.

## QG coherent sector

The main QG paper assumes a positive gap on the noncoherent internal complement:

```text
A_int >= lambda_* > 0
```

and uses coherent projectors realized by spectral filters of the internal
block.

It also states that mild off-diagonal/warp couplings persist with renormalized
constants under Kato-Rellich and Trotter-product control.

## Flavor holonomy as coherent line-bundle data

The central-circle paper states that flavor degrees of freedom are encoded by a
line bundle:

```text
L_F -> S^1_cen
```

with discrete holonomy.  It gives the already-written family case:

```text
Hol(L_F) = Z_3,
psi_f(theta) = exp(i q_f theta) psi_tilde_f.
```

It also says these are coherent modes, and that different holonomy sectors are
distinct admissible coherent configurations.

# Important Caveat: Raw Fourier Modes Are Not Enough

There is a real trap here.

On the raw scalar circle Laplacian:

```text
-d^2/dtheta^2 exp(iq theta) = q^2 exp(iq theta).
```

So for `q != 0`, the raw Fourier mode is not a scalar zero mode.

Therefore, the compatibility:

```text
Ran(P_fl) subset Ran(Pi_coh)
```

cannot be proved if `Pi_coh` is read as the untwisted scalar zero-mode
projector and the flavor labels are read as ordinary nonzero Fourier modes.

The coherent reading must therefore be one of:

```text
1. a retained finite spectral cluster of the internal coherent projector;
2. an equivariant sector on a finite cover/orbifold of S^1_cen;
3. a twisted bundle/connection construction whose character sector is retained
   by the spectral projector.
```

In all cases, the theorem below needs only `[L_fl, Pi_coh]=0` and that the
Riesz contour encloses no `Q`-sector spectrum.  It does not require raw scalar
Fourier modes to be zero modes.

This is exactly how the corpus already treats the family `Z_3` line bundle.
The `Z_64` CP sector needs the analogous construction.

# Setup

Let `H` be the internal Hilbert space on the admissible slab.

Let:

```text
Pi_coh
```

be the coherent projector, defined as the joint spectral projector of the
commuting vertical or twisted vertical Laplacians.

Let:

```text
L_fl
```

be the selected flavor closure operator, self-adjoint on the relevant Sobolev
domain.

Let:

```text
P_fl = (1/2pi i) integral_gamma (z-L_fl)^(-1) dz
```

be the Riesz projector onto the selected Z_64 flavor eigencluster.

# Lemma 1: Commuting Projectors

Assume:

```text
[L_fl, Pi_coh] = 0.
```

Then:

```text
[P_fl, Pi_coh] = 0.
```

## Proof

If `Pi_coh` commutes with `L_fl`, it commutes with the resolvent:

```text
Pi_coh (z-L_fl)^(-1) = (z-L_fl)^(-1) Pi_coh
```

for all `z` in the resolvent set.  Integrating around the Riesz contour
`gamma` gives:

```text
Pi_coh P_fl = P_fl Pi_coh.
```

This proves the lemma.

# Lemma 2: Subprojector Criterion

Assume:

1.  `[L_fl, Pi_coh]=0`;

2.  the Riesz contour `gamma` encloses a selected spectral cluster of
    `Pi_coh L_fl Pi_coh`;

3.  `gamma` encloses no spectrum of `Q L_fl Q`, where:

    ```text
    Q = I - Pi_coh.
    ```

Then:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl,
Ran(P_fl) subset Ran(Pi_coh).
```

## Proof

The commutation assumption block-diagonalizes `L_fl`:

```text
L_fl = Pi_coh L_fl Pi_coh  direct_sum  Q L_fl Q.
```

By the spectral mapping/Riesz calculus, the Riesz projector splits as:

```text
P_fl = P_gamma(Pi_coh L_fl Pi_coh) Pi_coh
       + P_gamma(Q L_fl Q) Q.
```

The second term is zero because `gamma` encloses no `Q L_fl Q` spectrum.
Therefore:

```text
P_fl = P_gamma(Pi_coh L_fl Pi_coh) Pi_coh.
```

Thus `P_fl Pi_coh = Pi_coh P_fl = P_fl`, and the range inclusion follows.

# Theorem: Flavor-QG Projector Compatibility

Assume:

1.  the admissible internal geometry is in the exact blockwise regime:

    ```text
    epsilon_warp = 0;
    ```

2.  the `Z_64` CP sector is realized as a twisted/equivariant central-circle
    sector whose selected states are retained by the coherent spectral
    projector;

3.  `L_fl` is an internal self-adjoint flavor closure operator preserving this
    coherent twisted/equivariant sector:

    ```text
    [L_fl, Pi_coh] = 0;
    ```

4.  the `Z_64` Riesz contour encloses only the selected coherent flavor
    spectral cluster and no `Q`-sector spectrum.

Then:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl,
Ran(P_fl) subset Ran(Pi_coh).
```

Consequently, the finite `Z_64` flavor projector is a coherent-sector
subprojector, not an external add-on to the QG/coherent projection.

# Consequence for the Schur Gate

Under the compatibility theorem, the Schur split used in the Z_64 proof is
the same kind of coherent/noncoherent split as in the QG corpus:

```text
H = Ran(Pi_coh) direct_sum Ran(Q),
Q = I - Pi_coh.
```

The selected flavor correction is:

```text
E_Schur = P_fl L Q (Q L Q)^(-1) Q L P_fl.
```

Therefore:

```text
||E_Schur|| <= C_fl/lambda_Q,
C_fl = ||P_fl L Q|| ||Q L P_fl||.
```

The remaining Z_64 gate is still:

```text
C_fl/(alpha lambda_Q) < 9/2.
```

This paper does not compute `C_fl`, `alpha`, or `lambda_Q`; it proves that
they are the right coherent-sector quantities once the twisted holonomy
realization is supplied.

# Warp/Off-Diagonal Version

If the exact commutation fails only by a controlled amount:

```text
||[L_fl, Pi_coh]|| <= epsilon_warp,
```

then exact subprojection is replaced by an almost-invariance statement:

```text
||Q P_fl|| = O(epsilon_warp / gap_gamma),
```

where `gap_gamma` is the contour separation from the unwanted spectrum.

This is the same bookkeeping already used in the pure central-circle reduction:

```text
C_fl/(alpha lambda_Q) + epsilon_warp/alpha < 9/2.
```

A full almost-projector theorem can be proved by the standard resolvent identity
and Davis-Kahan/Kato spectral-subspace bounds, but the exact blockwise theorem
above is the clean result needed for the current proof spine.

# What Is Now Proved

We have proved:

```text
commuting twisted spectral data
+ coherent-only flavor Riesz contour
=> P_fl is a subprojector of Pi_coh.
```

This closes the formal projector-compatibility bridge.

# What Remains Open

The proof still needs an execution-level derivation of the CP carrier from the
selected MTT Hessian and retarded kernel.  The safe target is now the finite
Wilson/deck carrier:

```text
K_64 ~= C[Z_64],
U_64^64 = I,
U_64^d != I for 0 < d < 64,
```

attached to the shared central circle and retained by `Pi_coh`, such that:

```text
1. its unitary character quotient contains the selected Z_64 CP sector;
2. its selected states are retained by the coherent spectral projector;
3. L_fl preserves this twisted/equivariant coherent sector;
4. the selected Riesz contour has no Q-sector spectrum.
```

This is the precise version of "replace Z_448 with the finite quotient MTT
actually selects": the finite quotient must be the unitary character quotient
of a coherent finite Wilson/deck internal sector.

# Gate Status

```text
Foundation joint spectral Pi_coh found                       YES
Riesz projectors commute with own operator                   YES
QG spectral-filter coherent projector aligns structurally     YES
central-circle flavor line-bundle holonomy found             YES
raw Fourier/scalar-zero-mode mismatch identified             YES
exact compatibility theorem under twisted block assumptions  PROVED
P_fl subprojector of Pi_coh under spectral-contour condition  PROVED
Z_64 finite Wilson/deck carrier target formulated            YES
MTT Hessian selects exact Z_64 carrier                       OPEN
L_fl preservation of twisted/equivariant coherent sector     OPEN
lambda_Q relation to lambda_*                                OPEN
```

# Bottom Line

The projector bridge is now mathematically clean:

```text
if Z_64 flavor lives as a coherent twisted/equivariant spectral sector,
then P_fl is inside Pi_coh.
```

The next real construction is therefore not another abstract projector lemma.
It is deriving the selected finite `Z_64` Wilson/deck carrier from the actual
MTT Hessian and retarded overlap kernel.
