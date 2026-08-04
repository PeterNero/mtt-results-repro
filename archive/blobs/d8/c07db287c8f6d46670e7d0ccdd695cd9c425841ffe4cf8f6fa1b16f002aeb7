---
abstract: |
  We formulate the safest concrete target for the remaining Z_64 CP-sector
  construction.  The Z_64 labels should not be ordinary nonzero scalar Fourier
  zero modes on S^1_cen.  They should be realized as a finite Wilson/deck
  character carrier retained by the coherent internal projector.  Equivalently,
  MTT must select a finite internal unitary U_64 with exact order 64, acting on
  a finite coherent carrier K_64 ~= C[Z_64], while the scalar central-circle
  zero mode remains separate.  This supplies the correct finite quotient for
  the Z_64 dyadic tower and makes the projector-compatibility lemma apply:
  the flavor projector lies inside Pi_coh once the carrier is selected and
  gapped.  The note does not claim final derivation from the MTT Hessian; it
  identifies the construction that the Hessian and retarded kernel must now
  realize.
author:
- Peter Nero
date: May 2026
title: |
  Twisted-Equivariant Central-Circle Z64 CP Sector Candidate
---

# Purpose

The projector-compatibility lemma proves:

```text
[L_fl, Pi_coh]=0
+ coherent-only Riesz contour
=> P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

The remaining danger was interpretive.  If the `Z_64` labels are read as raw
nonzero scalar Fourier modes on the central circle, they are not scalar
zero modes and cannot automatically lie inside `Pi_coh`.

This note gives the correct construction target.

# Safe Carrier

Let:

```text
H_0 = scalar/base coherent central-circle sector,
K_64 = C[Z_64].
```

The `Z_64` CP carrier is the finite internal Hilbert space `K_64`, attached to
the shared central circle as Wilson/deck/equivariant data.  It is not the
nonzero scalar Fourier spectrum of `S^1_cen`.

Choose a unitary:

```text
U_64 : K_64 -> K_64
```

with:

```text
U_64^64 = I,
U_64^d != I for 0 < d < 64.
```

In the character basis:

```text
U_64 |q> = exp(2 pi i q/64) |q>,
q in Z_64.
```

The character projectors are:

```text
E_q = (1/64) sum_{r=0}^{63} exp(-2 pi i q r/64) U_64^r.
```

Thus:

```text
K_64 = direct_sum_{q in Z_64} E_q K_64.
```

This is the finite quotient MTT actually needs on the dyadic CP side.

# Coherent Projector Realization

The coherent projector must retain the finite carrier as an internal spectral
cluster:

```text
H_coh,64 = H_0 tensor K_64 tensor C|tau_64>,
```

where:

```text
tau_64 = selected five-step D_2 tower with terminal spinorial parity.
```

Equivalently, the internal coherence operator has a block:

```text
A_int = 0 on H_coh,64,
A_int >= lambda_* on the excluded complement.
```

or the same statement with a small coherent cluster in place of the exact zero
eigenvalue.

Then:

```text
P_CP,64 <= Pi_coh.
```

Here `P_CP,64` projects onto the finite `Z_64` carrier block.  The scalar
circle zero mode supplies shared coherence; the finite CP character register
supplies the discrete phase quotient.

# Why This Avoids the Fourier Trap

On the ordinary scalar circle:

```text
-d^2/dtheta^2 exp(i q theta) = q^2 exp(i q theta).
```

So nonzero scalar Fourier modes are not zero modes.

The present construction does not use them as zero modes.  It uses:

```text
base scalar coherence on S^1_cen,
finite Wilson/deck character data in K_64,
Riesz selection of the dyadic tower.
```

The finite phases are eigenvalues of `U_64`, not scalar Laplacian eigenmodes.

# Relation to the Existing Z64 Tower Proof

The already-proved dyadic tower result says that exact order `64` with
spinorial terminal parity is selected by:

```text
(2,2,2,2,2)
```

under the central-circle cover-cost normal form.

That proof should now be read as acting on the finite CP carrier:

```text
K_64 ~= C[Z_64],
```

with cumulative carry rows:

```text
2x_i = x_{i+1}, i=0,...,4,
2x_5 = 0.
```

The associated Smith normal form is:

```text
[64].
```

So the carrier and the tower match:

```text
finite Wilson/deck carrier K_64
+ selected D_2 carry tower
=> exact dyadic CP quotient Z_64.
```

# Preferred Interpretation

The most conservative interpretation is:

```text
Z_64 is a finite internal Wilson/deck character carrier
over the shared central circle.
```

This is stronger than saying "there are Fourier modes with denominator 64".
It says that the coherent internal reduction contains a finite unitary of exact
order `64`, and the physical CP labels are its character projectors.

# Equivalent Models

The same target can be presented in several equivalent languages.

## Finite Wilson Carrier

The coherent sector contains a finite unitary Wilson operator `U_64` with exact
order `64`.  This is the cleanest operator-theoretic model.

## Deck/Equivariant Carrier

The coherent sector contains a finite deck action of `Z_64` over the shared
circle.  The projectors `E_q` are the character idempotents of this deck
action.

## Twisted Bundle Carrier

A twisted bundle formulation is acceptable only if its spectral projector is
explicitly defined to retain the selected character sector.  It must not be
replaced by the false claim that ordinary nonzero scalar Fourier modes are
untwisted scalar zero modes.

# Compatibility Theorem for the Candidate

Assume:

1.  MTT selects the finite coherent carrier:

    ```text
    H_coh,64 = H_0 tensor K_64 tensor C|tau_64>;
    ```

2.  the excluded internal complement has positive gap `lambda_*`;

3.  the selected flavor closure operator preserves this block:

    ```text
    [L_fl, Pi_coh] = 0;
    ```

4.  the flavor Riesz contour encloses only spectrum inside this block.

Then:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

## Proof

Since the carrier block is retained by `Pi_coh`, the selected flavor cluster
lies in:

```text
Ran(Pi_coh).
```

The commutator condition block-diagonalizes `L_fl` relative to:

```text
Pi_coh + (I-Pi_coh).
```

The Riesz projector splits over these two blocks.  The contour encloses no
excluded-block spectrum, so the excluded contribution is zero.  Therefore the
Riesz projector has range inside `Ran(Pi_coh)`, which gives:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

# What This Achieves

This construction closes the interpretive gap:

```text
Z_64 is not an illicit scalar Fourier zero-mode sector.
Z_64 is a finite coherent Wilson/deck character sector.
```

It also tells us exactly what the MTT Hessian and retarded overlap kernel must
produce:

```text
1. an exact-order-64 finite carrier U_64;
2. the five-step D_2 carry tower with terminal spinorial parity;
3. block preservation by L_fl;
4. a positive excluded-sector gap lambda_Q;
5. a Schur constant satisfying C_fl/(alpha lambda_Q) < 9/2.
```

# Gate Status

```text
raw scalar Fourier interpretation                         REJECTED
finite Wilson/deck carrier target                         FORMULATED
exact-order U_64 character projectors                     FORMULATED
compatibility with Pi_coh if carrier is selected           PROVED
D_2 tower supplies Z_64 carry rows                         IMPORTED
finite carrier extraction criterion                        PROVED
selected-kernel primitive lag                              PROVED
exact coherent-block Schur inequality                      PROVED
MTT Hessian selects this exact carrier                     OPEN
lambda_Q relation to lambda_* for QG complement            PROVED-CONDITIONAL
non-exact Schur/warp leakage bound                         OPEN IF NEEDED
```

# Bottom Line

The correct way forward is now sharply fixed:

```text
derive the finite coherent Wilson/deck carrier U_64
from the selected MTT Hessian and retarded kernel.
```

If that derivation succeeds, the dyadic CP branch is not merely compatible
with QG coherence; it is a finite subprojector inside it.
