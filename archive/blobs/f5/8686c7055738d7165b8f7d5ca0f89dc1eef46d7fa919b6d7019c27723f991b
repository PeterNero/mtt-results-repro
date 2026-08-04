---
abstract: |
  We specify the coefficient-level calculation needed to finish the dyadic
  pre-quarter proof.  The bounded retarded-lag model reduces the CKM numerator
  to the inequality 0<rho_q/kappa_q<2.  This note defines kappa_q as the
  closure-strain Hessian in the selected dyadic CP tangent direction and
  rho_q as the first derivative, at the lepton quarter-turn, of the retarded
  quark overlap cost.  With these definitions, the minimizer of the local
  quadratic cost lies at u_q=16-rho_q/kappa_q, so the finite survivor is q_64=15
  exactly when the coefficient ratio lies in (0,2).  The note is an execution
  protocol, not a completed coefficient evaluation.
author:
- Peter Nero
date: May 2026
title: |
  Coefficient Extraction Protocol for the Retarded Dyadic CKM Lag
---

# Purpose

The bounded retarded-lag theorem says that the desired dyadic branch follows
from:

```text
0 < rho_q/kappa_q < 2.
```

This note defines the coefficients that must be computed from MTT data.

# Local coordinate

Let `u` be the continuous coordinate along the selected dyadic CP tangent
direction before survivor projection:

```text
u in R/64Z.
```

The lepton/lens quarter-turn is:

```text
u_l = 16.
```

Let `v_64` denote the corresponding unit dyadic tangent vector in the
closure-strain tangent space, normalized so that one unit of `u` corresponds
to one `Z_64` phase step.

# Local quark overlap cost

Let `J_q(u)` be the quark-sector retarded overlap/admissibility cost after all
non-CP directions have been minimized or projected out in the selected local
chart.

Near the lepton quarter-turn:

```text
J_q(u) =
J_q(16)
+ rho_q (u-16)
+ (1/2) kappa_q (u-16)^2
+ O((u-16)^3).
```

The coefficients are:

```text
rho_q   = dJ_q/du |_{u=16},
kappa_q = d^2J_q/du^2 |_{u=16}.
```

Equivalently, before reducing to the scalar coordinate:

```text
kappa_q = <v_64, H_q v_64>,
```

where `H_q` is the quark-sector closure-strain Hessian in the CP direction.

# Sign convention

The retarded/pre-quarter convention is:

```text
rho_q > 0.
```

Then the local minimizer solves:

```text
dJ_q/du = rho_q + kappa_q (u-16) = 0,
```

so:

```text
u_q = 16 - rho_q/kappa_q.
```

The advanced/post-quarter sign would be:

```text
rho_q < 0,
```

which gives `u_q>16` and selects the wrong adjacent branch.

# Required inequalities

The coefficient theorem needed for the CKM numerator is:

```text
kappa_q > 0,
0 < rho_q < 2 kappa_q.
```

These have distinct meanings.

```text
kappa_q > 0
```

is local stability in the quark CP direction.

```text
rho_q > 0
```

is the retarded orientation sign.

```text
rho_q < 2 kappa_q
```

is the adjacent-cell bound: the lag is smaller than two dyadic units.

# Finite consequence

If these inequalities hold, then:

```text
14 < u_q < 16.
```

The nearest primitive order-64 survivor is:

```text
q_64=15.
```

With the Mukai component:

```text
q_7=2,
```

the Chinese remainder theorem gives:

```text
q=79 mod 448.
```

# How to compute the coefficients

The next concrete calculation should proceed in this order:

1.  identify the selected local chart around the lens/lepton quarter-turn;

2.  construct the dyadic CP tangent vector `v_64` from the shared-circle carry
    coordinate;

3.  restrict the closure-strain Hessian to the quark sector and compute
    `<v_64,H_q v_64>`;

4.  compute the retarded overlap derivative at the quarter-turn:

    ```text
    d/du arg sum_gamma A_gamma exp(-S_gamma(u)) chi_gamma(u)
    ```

    or the equivalent derivative of the real admissibility cost `J_q`;

5.  fix the sign convention by the universal central-circle ordering;

6.  verify the strict inequality `0<rho_q/kappa_q<2`.

# Pass and fail criteria

The proof passes if the selected MTT data give:

```text
0 < rho_q/kappa_q < 2
```

without introducing an entry-local phase knob.

The proof fails in this form if:

```text
rho_q <= 0,
rho_q/kappa_q >= 2,
kappa_q <= 0,
```

or if `rho_q` is not computable from the selected overlap kernel.

# Gate status

```text
kappa_q identified as dyadic Hessian coefficient          DEFINED
rho_q identified as retarded overlap derivative           DEFINED
finite survivor criterion is rho_q/kappa_q in (0,2)       PASS
compute coefficients from explicit selected geometry      OPEN
```

# Bottom line

The last proof step is now coefficient-level:

```text
compute rho_q and kappa_q.
```

Everything after that is finite arithmetic.  If the ratio lands in `(0,2)`,
then `q_64=15` and the full CKM label is `q=79`.
