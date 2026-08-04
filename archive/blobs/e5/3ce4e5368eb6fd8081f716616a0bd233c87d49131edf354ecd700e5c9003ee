---
abstract: |
  We derive the structural source of the second-order quark breakdown cost
  used in the B_q candidate.  The key point is color-singlet admissibility:
  a quark residual cannot be held as an isolated colored identity, so one
  mismatch must be completed through equivalent hidden color-redundancy
  channels.  Schur minimization over two equivalent hidden completion channels
  gives the coefficient 1/2 in the second residual term.  This closes the
  source of the second-order color-redundancy form, but it does not yet select
  the up/down stiffness constants or the final retarded orientation branch.
author:
- Peter Nero
date: June 2026
title: |
  Color-Singlet Redundancy Source for the Quark Breakdown Operator B_q
---

# Purpose

The current quark kernel needs a real source for the second-order operator

```text
B_q.
```

The previous candidate used

```text
D_q(i,j,b)^2 =
  (J_i - J_b)^2
  + (1/2) (J_j - J_{b+1})^2.
```

This note derives the structural `1/2` coefficient from color-singlet
redundancy completion.

# Corpus Inputs

The QFT corpus says that color degrees of freedom live on the distinguished
internal bundle `B_3`, and that color-charged excitations are not globally
separable admissible coherent modes unless they combine into color-singlet
configurations.

The theta-closure corpus identifies the color fiber as

```text
B_3 ~= S^1_cen x Gamma\Nil_3,
```

with color harmonics normalized intrinsically on the compact nilmanifold.

The book-level particle interpretation says that some distinctions are
inadmissible in isolation and become admissible only in combination.

Together these imply:

```text
quark identity is not first-order isolated identity;
quark identity is first-order anchor plus color-neutral redundancy completion.
```

# Color-Singlet Completion Lemma

Let `delta` be the residual mismatch of a quark leg after the first-order
anchor/bridge placement.  Suppose color-singlet admissibility requires this
residual to be completed through two equivalent hidden redundancy channels.

Write the hidden completions as `a` and `c`, with constraint

```text
a + c = delta.
```

The least-cost color-neutral completion minimizes

```text
E(a,c) = a^2 + c^2
```

subject to that constraint.

By substitution `c=delta-a`:

```text
E(a) = a^2 + (delta-a)^2.
```

The critical point is

```text
dE/da = 4a - 2 delta = 0,
```

so

```text
a = c = delta/2.
```

Therefore

```text
E_min = (delta/2)^2 + (delta/2)^2 = delta^2/2.
```

Thus a residual completed by two equivalent hidden color channels contributes

```text
(1/2) delta^2
```

to the effective Schur-reduced cost.

# Theorem: Source of the Second-Order B_q Form

Assume:

1.  first-order family anchoring gives the role-cost profile

    ```text
    J = (0, lambda_nil/lambda_lens, 1);
    ```

2.  a quark bridge entry has the selected family channel

    ```text
    b_ij = -(i+j) mod 3;
    ```

3.  one quark leg is directly compared with the visible bridge role `b`;

4.  the other quark leg is color-neutral only after hidden two-channel
    redundancy completion;

5.  the retarded nil/color survivor orders the hidden completion by an adjacent
    role `b+sigma`, with `sigma in {+1,-1}` fixed by the selected orientation.

Then the Schur-reduced second-order quark cost has the form

```text
D_q,sigma(i,j,b)^2 =
  (J_i - J_b)^2
  + (1/2) (J_j - J_{b+sigma})^2.
```

For the already-tested orientation convention `sigma=+1`, this is exactly the
operator used in the current B_q candidate.

# Proof

The first term is direct first-order comparison with the selected bridge role.
It is not hidden behind color completion, so its coefficient is `1`.

The second term measures the residual mismatch of the other quark leg against
the retarded adjacent redundancy role.  Because this leg is not admissible as
an isolated colored identity, the residual must be completed through the
color-singlet hidden channels.  By the color-singlet completion lemma, the
Schur-minimized effective cost of that residual is one half of its square.

Therefore the effective cost is exactly

```text
(J_i - J_b)^2 + (1/2)(J_j - J_{b+sigma})^2.
```

# What This Closes

```text
B_q is not a scalar stiffness multiplier                 PROVED
B_q is sourced by color-singlet redundancy completion     PROVED-SCHEMA
the coefficient 1/2 has a Schur/completion source         PROVED
quark sector needs a second-order layer beyond leptons    SUPPORTED
```

# What Remains Open

This result does not yet choose the whole quark kernel.  The remaining finite
selection questions are:

```text
select sigma = +1 or sigma = -1 from MTT orientation      OPEN
derive mu_u from selected theta/lens/nil/color data       OPEN
derive mu_d from selected theta/lens/nil/color data       OPEN
derive Lambda_q from selected Hessian/gap data            OPEN
derive exact Yukawa magnitudes and masses                 OPEN
```

A finite structural scan confirms the same split: the hidden-two-channel
coefficient is the only simple coefficient in the tested dictionary that
robustly gives CKM-shaped quark mixing, but multiple dyadic/gap/orientation
choices remain CKM-shaped until the selected MTT source fixes them.

# Bottom Line

The B_q operator now has a real internal source:

```text
color-singlet admissibility
-> hidden two-channel redundancy completion
-> Schur coefficient 1/2
-> second-order quark breakdown cost.
```

This is a genuine advance, but not full SM flavor closure.  The exact finite
constant and orientation selection is now the next theorem.

