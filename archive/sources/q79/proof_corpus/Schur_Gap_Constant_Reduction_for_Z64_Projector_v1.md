---
abstract: |
  We continue the reduced Z_64 Hessian proof after the pure central-circle
  block reduction.  The live condition is now
  C lambda_Q^{-1} < 9 alpha/2, with an optional epsilon_warp leakage term.
  Searching the MTT corpus shows that the Schur constant C is not yet given as
  a number, but the baseline scale papers identify its structural source:
  coherent/noncoherent mixing amplitudes ||L_PQ|| and ||L_QP|| enter through
  ||L_PQ||||L_QP||/lambda_*.  Thus the remaining proof can be rewritten as a
  dimensionless mixing-gap inequality.  If the selected flavor Q-sector has
  gap lambda_Q and mixing product C_fl, then the Z_64 projector passes when
  C_fl/lambda_Q + epsilon_warp < 9 alpha/2.  Using the conservative baseline
  floor lambda_Q >= lambda_* >= 1/4 gives the sufficient numerical criterion
  C_fl < 9 alpha/8 in the exact base-only case.  This does not finish the proof:
  it identifies precisely the missing flavor-sector estimate.
author:
- Peter Nero
date: May 2026
title: |
  Schur Gap Constant Reduction for the Z64 Projector
---

# Purpose

The previous reduction proved that the Hessian-level correction is no longer:

```text
E_mix + E_Schur + E_cubic.
```

On the fixed pure central-circle dyadic sector it is:

```text
E_Schur,
```

so the live pass condition is:

```text
C lambda_Q^{-1} < 9 alpha/2.
```

This paper asks what the corpus already says about `C` and `lambda_Q`.

# Corpus Inputs

## Schur-Feshbach bound

The theta-closure paper gives the block decomposition:

```text
L =
[ P_0 L P_0   P_0 L Q
  Q L P_0     Q L Q ],
```

and the effective generator:

```text
L_eff = P_0 L P_0 - P_0 L Q (Q L Q)^(-1) Q L P_0.
```

It records:

```text
||P_0 L Q (Q L Q)^(-1) Q L P_0|| <= C lambda_Q^{-1}.
```

Thus `C` is the sector constant controlling coherent/noncoherent mixing.

## Baseline scale paper

The baseline scale paper makes the same point in more explicit operator terms.
It states that coupling between coherent and noncoherent sectors is quantified
by:

```text
||L_PQ||, ||L_QP||,
```

and that these scales enter through:

```text
||L_PQ|| ||L_QP|| / lambda_*.
```

For the flavor projector sector, define:

```text
C_fl := ||P_fl L Q|| ||Q L P_fl||,
```

or any certified upper bound for that product.  Then:

```text
||E_Schur|| <= C_fl / lambda_Q.
```

## Conservative gap floor

The theta-closure baseline-geometry section records the internal gap lower
bounds:

```text
lambda_Sigma1 ~ 1/R_1^2,
lambda_lens >= 2/(f_2 R_lens)^2,
lambda_nil >= h_0^2/4.
```

It then uses the worked baseline:

```text
h_0 = 1,
lambda_nil = 1/4,
lambda_* >= 0.25.
```

Therefore, if the selected flavor noncoherent complement is controlled by the
same conservative vertical floor:

```text
lambda_Q >= lambda_* >= 1/4.
```

This is only a floor.  The theta-closure high-coherence regime may have a much
larger `lambda_Q`.

# Lemma: Schur Constant as Mixing Product

Assume:

1.  `Q L Q` is invertible on the selected noncoherent complement;

2.  the selected complement has gap:

    ```text
    ||(Q L Q)^(-1)|| <= lambda_Q^{-1};
    ```

3.  the coherent/noncoherent mixing maps are bounded:

    ```text
    ||P_fl L Q|| <= M_PQ,
    ||Q L P_fl|| <= M_QP.
    ```

Then:

```text
||E_Schur|| <= M_PQ M_QP lambda_Q^{-1}.
```

Thus one may take:

```text
C_fl = M_PQ M_QP.
```

## Proof

By submultiplicativity of the operator norm:

```text
||P_fl L Q (Q L Q)^(-1) Q L P_fl||
<= ||P_fl L Q|| ||(Q L Q)^(-1)|| ||Q L P_fl||.
```

Using the gap bound for `(Q L Q)^(-1)` gives:

```text
||E_Schur|| <= M_PQ M_QP lambda_Q^{-1}.
```

# Theorem: Reduced Numerical Gate

Assume the pure central-circle Hessian reduction:

```text
L_fl,MTT | H_64 = alpha L_tower + E_Schur.
```

Assume also:

```text
||E_Schur|| <= C_fl lambda_Q^{-1}.
```

Then the Z_64 Riesz projector is selected if:

```text
C_fl lambda_Q^{-1} < 9 alpha/2.
```

Equivalently:

```text
C_fl / (alpha lambda_Q) < 9/2.
```

With warp leakage:

```text
C_fl / (alpha lambda_Q) + epsilon_warp/alpha < 9/2.
```

# Conservative Baseline Corollary

If the selected flavor complement obeys the conservative corpus floor:

```text
lambda_Q >= 1/4,
```

and if `epsilon_warp=0`, then it is sufficient to prove:

```text
C_fl < 9 alpha/8.
```

In normalized tower units `alpha=1`, this is:

```text
C_fl < 1.125.
```

This is not claimed to be necessary.  It is the baseline-floor sufficient
condition.  If a sharper flavor gap is proven, replace `1/4` by that sharper
`lambda_Q`.

# Candidate Closure Routes

There are now three clean routes to finish the Z_64 Hessian gate.

## Route A: conservative global gap floor

Use:

```text
lambda_Q >= lambda_* >= 1/4.
```

Then prove:

```text
C_fl < 9 alpha/8.
```

This is rigorous but may be stronger than needed.

## Route B: pure central-circle Q-gap

If the relevant noncoherent complement is the central-circle complement, the
circle spectral law gives:

```text
lambda_Q >= R_c^{-2}.
```

In normalized central-circle units `R_c=1`, this gives:

```text
C_fl < 9 alpha/2.
```

This route is less restrictive, but it requires proving that the eliminated
Q-modes for the flavor projector are really central-circle Q-modes and not the
full internal complement.

## Route C: high-coherence regime

Theta closure assumes a high-coherence regime where `lambda_Q` is
parametrically large and the Schur-Feshbach remainder is `O(lambda_Q^{-1})`.

If the flavor sector lies in this same regime and `C_fl/alpha` remains bounded
independently of `lambda_Q`, then the reduced bound eventually holds.

This route is powerful but needs a sector-identification theorem connecting
the CKM dyadic flavor projector to the same high-coherence slab.

# What Remains Open

The corpus now identifies the final missing estimate for the general
non-exact branch:

```text
C_fl = ||P_fl L Q|| ||Q L P_fl||,
lambda_Q = spectral gap of Q L Q on the selected flavor complement,
alpha = central-circle closure stiffness.
```

To finish the proof one must show:

```text
C_fl / (alpha lambda_Q) < 9/2
```

and, if the exact base-only ansatz is relaxed:

```text
C_fl / (alpha lambda_Q) + epsilon_warp/alpha < 9/2.
```

# Exact-Branch Update

The later projector-compatibility and exact Schur-collapse papers sharpen this
for the exact coherent finite-carrier branch.  If:

```text
P_fl <= Pi_coh,
[L,Pi_coh]=0,
Q=I-Pi_coh,
```

then:

```text
P_fl L Q = 0,
Q L P_fl = 0,
C_fl = 0,
E_Schur = 0.
```

Therefore:

```text
C_fl / (alpha lambda_Q) = 0 < 9/2.
```

So the exact branch is closed.  The open estimate remains only for relaxed
warp/noncommuting branches, where one must bound:

```text
||[L,Pi_coh]||
```

or the explicit warp leakage.

# Gate Status

```text
Schur-Feshbach operator form found                         YES
C identified as coherent/noncoherent mixing product        YES
baseline internal gap floor lambda_* >= 1/4 found          YES
reduced dimensionless gate derived                         PROVED
conservative sufficient condition C_fl < 9 alpha/8         PROVED
exact coherent-block C_fl=0 branch                         PROVED
lambda_Q>=lambda_* for QG complement branch                PROVED-CONDITIONAL
non-exact flavor mixing product C_fl computed              OPEN
non-exact selected flavor gap lambda_Q computed            OPEN
physical central-circle stiffness alpha computed           OPEN
choice between Route A/B/C resolved                        OPEN
```

# Bottom Line

The exact coherent-block branch is now closed.  The non-exact branch has the
specific remaining estimate:

```text
prove C_fl / (alpha lambda_Q) < 9/2.
```

Under the conservative baseline gap floor this becomes:

```text
prove C_fl < 9 alpha/8.
```

That is the next proof target.
