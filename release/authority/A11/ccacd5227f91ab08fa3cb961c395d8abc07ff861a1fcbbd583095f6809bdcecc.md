---
abstract: |
  We consolidate the exact dyadic branch after the projector-compatibility,
  finite-carrier, selected-kernel primitive-lag, exact Schur-collapse, Z64
  exact-branch certificate, and Z7 Fu-Yau/Mukai charge-sector certificate.  On
  the selected exact central-circle branch, the coherent Wilson/deck block is
  K_64 ~= C[Z_64] with primitive shift S, the selected retarded kernel has
  primitive unit lag 16->15, the Schur correction vanishes, and q_64=15 is
  stable.  On the selected Fu-Yau/Mukai charge-sector branch, the
  determinant-seven Mukai block gives q_7=2.  The CRT gives q=79 mod 448.
  Stronger routes remain useful, but the two terminal q79 certificates are
  now closed for the exact/charge branch.
author:
- Peter Nero
date: May 2026
title: |
  Consolidated Exact Z64-to-q79 Closure Theorem
---

# Purpose

Many former gates have now closed separately.  This note assembles them into
one exact/charge-branch theorem.

# Inputs Already Proved

## Group-algebra carrier

Once the six carry rows are supplied, the finite carrier is canonical:

```text
K_64 = C[coker A_64] ~= C[Z_64].
```

The primitive shift is translation by the generator of `coker A_64`.

## Finite carrier criterion

If the selected Hessian/kernel contains:

```text
K_64 ~= C[Z_64],
S^64=I,
S^d != I for 0<d<64,
L_64, K_ret,64 in C[S],
```

then the finite Wilson/deck carrier is exact order `64`.

## Selected primitive lag

The selected nil-survivor retarded kernel gives:

```text
16 -> 15 = S^{-1}=S^63,
gcd(64,63)=1.
```

So the selected kernel sees the full `Z_64` carrier and does not collapse to a
proper divisor.

## Projector compatibility

If the finite carrier is retained by the coherent projector and the selected
flavor operator commutes with the coherent block:

```text
P_fl <= Pi_coh,
[L,Pi_coh]=0,
```

then:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

## Exact Schur collapse

In the same exact blockwise regime:

```text
C_fl = ||P_fl L Q|| ||Q L P_fl|| = 0,
E_Schur = 0.
```

Therefore:

```text
C_fl/(alpha lambda_Q)=0<9/2.
```

# Exact-Branch Theorem

Assume:

1.  the selected MTT Hessian/kernel realizes the finite coherent carrier:

    ```text
    K_64 ~= C[Z_64],
    S^64=I,
    S^d != I for 0<d<64;
    ```

2.  the selected Hessian/kernel is block-circulant on `K_64`:

    ```text
    L_64, K_ret,64 in C[S];
    ```

3.  the carrier block is retained by `Pi_coh`, and the exact blockwise
    commutation holds:

    ```text
    [L,Pi_coh]=0;
    ```

4.  the physical CKM CP kernel is the selected nil-survivor kernel;

5.  the odd Mukai component is:

    ```text
    q_7=2.
    ```

Then:

```text
q_64=15,
q=79 mod 448.
```

Moreover the dyadic Riesz selection is Schur-stable in the exact branch:

```text
E_Schur=0.
```

## Proof

By the finite-carrier criterion, `K_64` with primitive shift `S` supplies the
exact cyclic dyadic carrier `Z_64`.

By nil-survivor execution and the retarded unit-lag lemma, the selected quark
branch is the predecessor of the lepton quarter-turn:

```text
q_64=15.
```

The lag is primitive:

```text
15-16=-1=63 mod 64,
gcd(64,63)=1.
```

So the selected kernel sees the full carrier.

By projector compatibility and exact block commutation, the off-block Schur
maps vanish:

```text
P_fl L Q=0,
Q L P_fl=0.
```

Thus:

```text
E_Schur=0,
C_fl/(alpha lambda_Q)=0<9/2.
```

Finally solve the CRT system:

```text
q = 15 mod 64,
q = 2  mod 7.
```

The unique solution modulo `448` is:

```text
q=79.
```

This proves the theorem.

# What This Closes

```text
Z64 exact central-circle branch certificate              CLOSED
selected-kernel primitive lag                            CLOSED
dyadic q_64=15                                           CLOSED
exact-branch Schur inequality                            CLOSED
Z7 Fu-Yau/Mukai charge-sector certificate                CLOSED
CRT q_64=15, q_7=2 -> q=79                               CLOSED
```

# What Remains as Optional Strengthening or Full SM Closure

```text
1. Optional strengthening: extract the same Z64 block from a larger non-exact
   mixed MTT Hessian and prove leakage bounds before selecting the exact
   central-circle branch.

2. Optional strengthening: realize the determinant-seven Mukai pair by a
   single locally-free HYM bundle construction rather than by fixed
   Mukai/differential-K charge-sector data.

3. Full SM closure: run the no-proxy Yukawa, neutrino, threshold, and RG checks
   on the
   same coherent data.
```

# Bottom Line

The exact/charge branch is no longer a theorem schema with two terminal
certificates missing.  It is the selected branch:

```text
Z64 exact central-circle branch
+ Z7 Fu-Yau/Mukai charge-sector branch.
```

It gives:

```text
q=79 mod 448.
```
