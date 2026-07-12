# Iwasawa Selected D_E Construction Attempt

## Purpose

The spectral fallback has a clear first target:

```text
construct a selected operator D_E.
```

This note tries to do exactly that from the current corpus. The result is a
clean partial advance:

```text
the diagnostic Hodge pipeline works,
but the selected D_E is not constructible from the current corpus.
```

## Route R1: Corrected Non-Invariant Dolbeault Operator

This route would supply explicit connection data:

```text
D_E = barpartial + A^(0,1)
```

or its Dirac/Dolbeault-Hodge equivalent.

Current status:

```text
blocked.
```

Reason:

```text
literal printed A01: not integrable,
diagnostic one-index repair: h1=2,
e3 torsion-support sparse branch: h1=2,
sparse h1=3 examples: unselected and drop e3,
no corrected non-invariant A01 supplied.
```

The follow-up invariant repair obstruction strengthens this:

```text
preserving the printed entries admits no signed invariant completion through
four added terms, and signed invariant torsion-support candidates through five
entries never give h1=3.
```

Therefore R1 does not currently provide a selected `D_E`.

## Route R2: Typed Monad Sections

This route would supply:

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}),
g o f = 0,
transition/Cech data,
exactness or controlled sheaf substitute.
```

Current status:

```text
blocked.
```

The recovery attempt found the monad sequence and Chern labels, but not the
typed section representatives or transition data. So R2 cannot yet define a
computable `D_E`.

## Route R3: Direct Selected HYM Solve

The corpus does support the abstract theorem package:

```text
stable holomorphic data on a Gauduchon/balanced metric
-> Li-Yau HYM connection exists.
```

So formally one may write:

```text
D_E = barpartial_{A_HYM} + barpartial_{A_HYM}^*.
```

Current status:

```text
abstract existence only.
```

This is not enough for the spectral matrix. To compute, we still need:

```text
selected holomorphic structure or HYM connection coefficients,
Hermitian metric or numerical HYM solve,
operator domain and gauge fixing,
basis action of D_E on B_N,
residual and gap certificate.
```

Without those, `L_N = P_N D_E^* D_E P_N` cannot be assembled.

## What We Did Achieve

The diagnostic pipeline proves the finite extraction machinery is ready. For a
known integrable but unselected `h1=3` candidate, it constructs:

```text
L_1,
ker(L_1),
P_ker = N (N^T N)^(-1) N^T,
```

and extracts:

```text
fiber1_baromega2,
-fiber1_baromega3 + fiber2_baromega2,
fiber3_baromega1.
```

This means the obstacle is not the Hodge/Galerkin linear algebra. The obstacle
is the selected operator source.

## Minimal New Data

One of the following would close the current blocker:

```text
1. corrected selected non-invariant A^(0,1) with integrability and HYM/Strominger residuals;
2. typed monad sections plus transition/Cech data;
3. direct HYM numerical/symbolic connection with residual bounds.
```

Then the next computation is mechanical:

```text
build B_N,
build G_N,
build L_N,
compute the Riesz projector,
certify gap/error,
extract selected Psi_i.
```

## Verdict

The selected `D_E` is not yet constructed from the current corpus. But we have
reduced the task to a precise finite input:

```text
give one concrete selected connection/operator source.
```

Once that is supplied, the diagnostic Hodge pipeline can be rerun as the actual
selected spectral Galerkin computation.
