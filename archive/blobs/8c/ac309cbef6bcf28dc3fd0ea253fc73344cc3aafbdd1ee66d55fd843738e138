---
abstract: |
  We reduce the remaining Z_64 carrier derivation to a concrete operator
  signature in the selected MTT Hessian and retarded overlap kernel.  It is
  enough to find a finite coherent residue block K_64 with a primitive shift
  S, S^64=I and S^d != I for 0<d<64, retained by Pi_coh with a positive
  excluded-sector gap.  If the Hessian/retarded kernel is block-circulant on
  this block, or equivalently lies in the polynomial algebra C[S], and its
  primitive-lag support has gcd one with 64, then the exact finite Wilson/deck
  carrier U_64 is derived.  The Fourier idempotents of S are precisely the
  Z_64 character projectors.  This does not yet compute alpha, C_fl, or
  lambda_Q; it says exactly what must be extracted from the selected MTT
  Hessian/kernel to turn the formulated carrier into a proof.
author:
- Peter Nero
date: May 2026
title: |
  Finite Wilson-Deck Carrier Extraction Criterion for Z64
---

# Purpose

The previous note formulated the safe `Z_64` carrier:

```text
K_64 ~= C[Z_64],
U_64^64 = I,
U_64^d != I for 0 < d < 64.
```

This paper gives the extraction criterion.  It answers:

```text
What exact Hessian/kernel signature proves that MTT selected this carrier?
```

# Finite Residue Block

Let `K_64` be a finite coherent residue block with basis:

```text
|r>, r in Z_64.
```

Define the primitive shift:

```text
S |r> = |r+1 mod 64>.
```

Then:

```text
S^64 = I,
S^d != I for 0 < d < 64.
```

Thus `S` is an exact-order-64 unitary.  It is the finite Wilson/deck carrier
operator.

# Character Projectors

Let:

```text
omega = exp(2 pi i / 64).
```

The character idempotents are:

```text
E_q = (1/64) sum_{r=0}^{63} omega^(-q r) S^r,
q in Z_64.
```

They satisfy:

```text
E_q E_p = delta_qp E_q,
sum_q E_q = I,
S E_q = omega^q E_q.
```

So the quotient selected by the finite block is:

```text
Char(<S>) ~= Z_64.
```

# Hessian/Kernel Signature

The selected MTT Hessian and retarded kernel derive the carrier if their
restriction to `K_64` has the block-circulant form:

```text
L_64 = sum_{m in Z_64} a_m S^m,
a_{64-m} = conjugate(a_m)
```

for the Hessian block, and similarly:

```text
K_ret,64 = sum_{m in Z_64} b_m S^m
```

for the retarded overlap kernel or its selected derivative.

Equivalently:

```text
[L_64,S]=0,
[K_ret,64,S]=0,
```

and the kernel sees the full period rather than a proper divisor.

# Primitive-Lag Test

Let:

```text
M = {m in Z_64 : b_m != 0}
```

be the set of retarded lags present in the selected derivative or overlap
kernel.  The kernel is primitive on `Z_64` when:

```text
gcd(64, M) = 1.
```

In particular, a unit-lag term:

```text
b_1 != 0
```

passes this test immediately.

If all lags are even, the kernel only sees a quotient of period at most `32`.
If all lags are multiples of `8`, it only sees a quotient of period at most
`8`.  This test is therefore the finite-carrier version of the old warning
that six independent binary memories do not automatically produce a cyclic
order-64 character.

# Coherent Inclusion

The finite carrier is a QG-compatible coherent sector when the internal
coherence operator has a retained block:

```text
H_coh,64 = H_0 tensor K_64 tensor C|tau_64>,
```

with:

```text
A_int = 0 on H_coh,64,
A_int >= lambda_* on the excluded complement,
```

or the same statement for an isolated retained cluster.  Then:

```text
P_CP,64 <= Pi_coh.
```

# Extraction Theorem

Assume:

1.  the selected MTT Hessian/kernel contains a finite residue block `K_64`
    with basis `|r>`, `r in Z_64`;

2.  the primitive shift `S|r>=|r+1>` is an admissible Wilson/deck operator on
    this block;

3.  the Hessian and selected retarded kernel are block-circulant on `K_64`,
    so they lie in `C[S]`;

4.  the selected retarded derivative has primitive-lag support:

    ```text
    gcd(64, M)=1;
    ```

5.  `H_0 tensor K_64 tensor C|tau_64>` is retained by `Pi_coh` with a positive
    excluded-sector gap.

Then MTT selects an exact finite Wilson/deck carrier:

```text
K_64 ~= C[Z_64].
```

The associated character quotient is exactly:

```text
Z_64.
```

Moreover, any selected flavor Riesz projector whose contour lies inside this
retained block satisfies:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

## Proof

The shift `S` has exact order `64` by assumption.  Its finite Fourier
idempotents `E_q` decompose `K_64` into `64` character lines.  Thus the
character quotient of the carrier is `Z_64`.

Because `L_64` and `K_ret,64` lie in `C[S]`, they preserve the same character
decomposition.  The primitive-lag condition prevents descent to a proper
subquotient.  The retained-block assumption gives:

```text
P_CP,64 <= Pi_coh.
```

The projector-compatibility lemma then applies to any flavor Riesz contour
inside this block, giving:

```text
P_fl Pi_coh = Pi_coh P_fl = P_fl.
```

This proves the criterion.

# Relation to q64 = 15

This criterion derives the carrier:

```text
Z_64.
```

It does not by itself choose the character:

```text
q_64 = 15.
```

The character selection is imported from the retarded unit-lag and
overlap-admissibility chain.  The point here is that the selected character now
has a legitimate exact-order-64 carrier to live in.

The selected-kernel branch also closes the primitive-lag test.  The retarded
unit-lag theorem gives:

```text
16 -> 15 = S^{-1}=S^63,
gcd(64,63)=1.
```

So the selected kernel sees the full `Z_64` carrier.  The raw pre-survivor
kernel route remains stronger and still requires explicit derivative
extraction.

# What Remains to Compute

The MTT proof is complete on the dyadic carrier side if the selected Hessian
and retarded kernel supply:

```text
1. the finite residue block K_64;
2. the primitive shift S;
3. block-circulant Hessian/kernel form on K_64;
4. primitive-lag support, preferably b_1 != 0;
5. coherent retained-block gap;
6. exact block commutation `[L,Pi_coh]=0`, or a commutator/warp bound.
```

If exact block commutation holds, the Schur gate is closed by:

```text
C_fl = 0,
E_Schur = 0.
```

# Gate Status

```text
finite carrier extraction criterion                      PROVED
primitive shift gives exact order 64                      PROVED
Fourier idempotents give Z_64 characters                  PROVED
block-circulant kernel preserves character sectors        PROVED
primitive-lag test prevents divisor collapse              PROVED
selected-kernel primitive lag S^{-1}                      PROVED
exact-branch Schur collapse C_fl=0                        PROVED
actual MTT Hessian/kernel block satisfying criterion      OPEN
non-exact commutator/warp bound                           OPEN IF NEEDED
```

# Bottom Line

The next computation is no longer vague.  Find the selected finite residue
block and verify:

```text
L_64, K_ret,64 in C[S],
gcd(64, selected lags)=1,
P_CP,64 <= Pi_coh.
```

That is the concrete test for the `Z_64` carrier.
