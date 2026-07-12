---
abstract: |
  We give the local response form that would prove the dyadic pre-quarter
  orientation.  Near the lepton/lens quarter-turn in the selected Z_64
  refinement, let u_q be the continuous dyadic coordinate of the quark CP
  overlap before survivor projection.  A retarded shared-circle response with
  positive forcing rho_q and positive quark stiffness kappa_q gives
  u_q=16-rho_q/kappa_q.  If 0<rho_q/kappa_q<2, the sharp primitive survivor
  is q_64=15.  Combined with the Mukai q_7=2 component, this yields q=79 by
  CRT.  This paper does not yet compute rho_q and kappa_q from a concrete
  internal metric; it turns the final numerator problem into an explicit
  local inequality for the closure-strain Hessian and retarded overlap force.
author:
- Peter Nero
date: May 2026
title: |
  Bounded Retarded-Lag Model for the Dyadic CKM Pre-Quarter Branch
---

# Purpose

The previous orientation note reduced the remaining numerator problem to:

```text
14 < u_q < 16,
```

where `u_q` is the continuous dyadic coordinate of the quark CP overlap before
sharp survivor projection.

This paper gives the local response model that would prove that inequality.

# Local response ansatz

Work near the lepton/lens quarter-turn:

```text
u_l = 16 in Z_64.
```

Let `u_q` be the quark CP dyadic overlap coordinate.  In a one-dimensional
normal form along the selected dyadic phase direction, write the local
closure-strain response equation as:

```text
kappa_q (u_q - 16) + rho_q = 0.
```

Here:

```text
kappa_q > 0
```

is the effective quark stiffness in the dyadic CP direction, inherited from
the sector-induced closure metric and Hessian, and

```text
rho_q > 0
```

is the retarded shared-circle overlap forcing in the chosen orientation.

Solving gives:

```text
u_q = 16 - rho_q/kappa_q.
```

# Pre-quarter condition

The finite survivor is `q_64=15` exactly when:

```text
14 < u_q < 16.
```

Substituting the response equation:

```text
14 < 16 - rho_q/kappa_q < 16
```

which is equivalent to:

```text
0 < rho_q/kappa_q < 2.
```

Thus the physical proof reduces to two inequalities:

```text
rho_q > 0,
rho_q < 2 kappa_q.
```

The first inequality is the retarded orientation sign.  The second is the
stiffness bound keeping the quark branch inside the adjacent primitive cell.

# Why the assumptions match MTT

The corpus supports this form but does not yet prove the coefficients.

The closure-strain paper defines sector-induced closure metrics and Hessian
blocks around alignment.  Quarks are partially anchored composite sectors with
maximal effective stiffness, while CP-odd effects are stiffness-modulated.

The central-circle paper supplies the universal orientation: successive
coherent projections impose a monotonic ordering of central-circle alignment.

The finite projection and nil-selection papers supply the survivor-filter
interpretation: a continuous pre-projection coordinate is sharpened to a
discrete admissible survivor label.

Therefore `u_q=16-rho_q/kappa_q` is the right local normal form to test.

# Finite theorem

#### Theorem

Assume:

1.  the selected dyadic CP factor is `Z_64`;

2.  the lepton/lens branch is the quarter-turn `u_l=16`;

3.  the quark CP overlap coordinate satisfies the retarded stiffness response

    ```text
    u_q = 16 - rho_q/kappa_q
    ```

    with `kappa_q>0`;

4.  the retarded forcing and stiffness obey

    ```text
    0 < rho_q/kappa_q < 2;
    ```

5.  sharp survivor projection chooses the nearest primitive order-64 label.

Then:

```text
q_64=15.
```

Combining with the Mukai discriminant component `q_7=2` gives:

```text
q = CRT(15,2) = 79 mod 448.
```

# Proof

By the response equation and the ratio bound:

```text
14 < 16-rho_q/kappa_q < 16.
```

The primitive labels nearest the quarter-turn are:

```text
15 < 16 < 17.
```

Every `u_q` in `(14,16)` has unique nearest primitive label `15`.
Therefore the dyadic survivor is `q_64=15`.  The CRT conclusion follows from
the already-checked product decomposition.

# Check script

The script

```text
bounded_retarded_lag_q64_check.py
```

scans values of

```text
epsilon = rho_q/kappa_q
```

and confirms:

```text
0 < epsilon < 2      -> q_64=15,
-2 < epsilon < 0     -> q_64=17,
epsilon = 0 or 2     -> boundary ambiguity,
epsilon outside cell -> other primitive labels.
```

So the sign and bound are both necessary.  The algebra alone does not decide
between the pre-quarter and post-quarter branches.

# What remains

The proof now asks for a concrete internal calculation:

```text
rho_q = <dyadic retarded force from the selected overlap kernel>,
kappa_q = <quark closure-strain Hessian in the CP direction>.
```

The final non-empirical derivation succeeds if:

```text
0 < rho_q < 2 kappa_q.
```

It fails, or must be revised, if the computed ratio is negative, zero, greater
than two, or not well-defined without an arbitrary phase choice.

# Gate status

```text
local response equation isolates sign and bound             PASS
positive stiffness kappa_q is corpus-supported              SUPPORTED
retarded forcing sign rho_q>0 is plausible                  SUPPORTED
finite survivor q_64=15 follows from 0<rho_q/kappa_q<2      PASS
compute rho_q and kappa_q from selected MTT geometry        OPEN
```

# Bottom line

The last numerator step is now an explicit local inequality:

```text
0 < rho_q/kappa_q < 2.
```

If the closure-strain Hessian and retarded overlap force satisfy this
inequality, the chain closes:

```text
rho_q/kappa_q in (0,2)
-> q_64=15
-> CRT(15,2)=79.
```
