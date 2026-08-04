---
abstract: |
  We give the rigorous coefficient theorem needed to turn the retarded
  dyadic-lag mechanism into a proof of the CKM label q=79.  In a selected
  local chart at the lepton quarter-turn, write s=u-16 and split the remaining
  tangent variables into the dyadic CP coordinate s and nuisance coordinates
  eta.  After minimizing eta, the effective one-dimensional coefficients are
  not the raw Hessian and force entries.  They are the Schur-reduced quantities
  rho_q = r_u - b^T D^{-1} r_eta and
  kappa_q = a - b^T D^{-1} b, where a, b, D are the selected closure-strain
  Hessian blocks and r_u, r_eta are the first derivatives of the retarded
  overlap cost.  Equivalently, in the exact total-cost formulation,
  kappa_q is the Schur complement of the eta eta block of the total Hessian.
  Therefore the final proof obligation is a concrete spectral and overlap
  derivative inequality: kappa_q>0 and 0<rho_q<2 kappa_q.  If it holds, the
  retarded cell is 14<u_q<16, the primitive dyadic survivor is q_64=15, and
  together with q_7=2 the CRT gives q=79 mod 448.
author:
- Peter Nero
date: May 2026
title: |
  Schur-Retarded Coefficient Theorem for the CKM q=79 Lag
---

# Purpose

The previous notes reduced the CKM numerator problem to:

```text
0 < rho_q/kappa_q < 2.
```

This note makes the phrase "compute rho_q/kappa_q from the selected MTT
Hessian and retarded overlap kernel" fully explicit.

The result is a theorem-level recipe:

```text
selected closure Hessian blocks + selected retarded overlap derivative
    -> rho_q
    -> kappa_q
    -> epsilon_MTT = rho_q/kappa_q
    -> q_64
    -> q mod 448.
```

# Selected Local Chart

Let `Theta_*` be the selected flavor point at the lepton/lens quarter-turn.
Use a local chart with coordinates:

```text
s   = u - 16,
eta = all non-dyadic-CP tangent coordinates.
```

Here `u` is normalized so that one unit of `u` is one `Z_64` dyadic phase
step.  Thus:

```text
u = 16
```

is the lepton quarter-turn, and the desired retarded quark point has:

```text
-2 < s_q < 0.
```

The selected quark cost is decomposed as:

```text
J_q(s,eta) = C_q(s,eta) + R_q(s,eta),
```

where:

- `C_q` is the closure-strain cost;
- `R_q` is the real retarded-overlap/admissibility cost extracted from the
  selected MTT overlap kernel.

# Exact Schur Reduction

First state the exact local theorem.

Assume `J_q` is `C^3` near `(0,0)`, and assume the nuisance block

```text
J_eta eta(0,0)
```

is positive definite.  Also assume the chart has already been centered on the
selected nuisance minimum:

```text
J_eta(0,0) = 0.
```

Then the implicit function theorem gives a unique smooth nuisance minimizer:

```text
eta = eta(s),
eta(0)=0,
J_eta(s,eta(s))=0.
```

Define the effective one-dimensional cost:

```text
J_eff(s) = J_q(s,eta(s)).
```

Then:

```text
rho_q = J_eff'(0)
      = J_s(0,0),
```

and:

```text
kappa_q = J_eff''(0)
        = J_ss(0,0)
          - J_s eta(0,0) [J_eta eta(0,0)]^{-1} J_eta s(0,0).
```

This is the exact coefficient extraction formula.  The effective stiffness is
the Schur complement of the nuisance block, not necessarily the raw `ss`
entry.

## Proof

Differentiate the nuisance equation:

```text
J_eta(s,eta(s)) = 0.
```

At `s=0`:

```text
J_eta s + J_eta eta eta'(0) = 0,
```

so:

```text
eta'(0) = -[J_eta eta]^{-1} J_eta s.
```

Now:

```text
J_eff'(s) = J_s + J_eta eta'(s).
```

At `s=0`, `J_eta=0`, hence:

```text
J_eff'(0) = J_s(0,0).
```

Differentiating again and using `J_eta(0,0)=0` gives:

```text
J_eff''(0)
= J_ss + J_s eta eta'(0)
= J_ss - J_s eta [J_eta eta]^{-1} J_eta s.
```

This proves the formula.

# Closure-Plus-Retarded Linear Form

For the MTT retarded-lag calculation, the useful expansion separates the
positive closure Hessian from the first retarded forcing.

Write the closure-strain expansion as:

```text
C_q(s,eta)
= C_0
 + 1/2 a s^2
 + s b^T eta
 + 1/2 eta^T D eta
 + O(||(s,eta)||^3),
```

where:

```text
a = C_ss(0,0),
b = C_eta s(0,0),
D = C_eta eta(0,0).
```

Write the retarded-overlap cost to first order as:

```text
R_q(s,eta)
= R_0
 + r_u s
 + r_eta^T eta
 + O(||(s,eta)||^2).
```

Then, to the same local order, minimizing `eta` gives:

```text
eta(s) = -D^{-1}(b s + r_eta) + higher-order terms.
```

Substitution gives:

```text
J_eff(s)
= const
 + [r_u - b^T D^{-1} r_eta] s
 + 1/2 [a - b^T D^{-1} b] s^2
 + higher-order terms.
```

Therefore the coefficient ratio is:

```text
rho_q   = r_u - b^T D^{-1} r_eta,
kappa_q = a   - b^T D^{-1} b,
epsilon_MTT = rho_q/kappa_q.
```

This is the main formula.

It also corrects a possible mistake: the retarded force is not always just
`r_u`.  If the closure Hessian couples the dyadic direction to nuisance
directions, and if the retarded kernel pushes those nuisance directions, then
the actual dyadic force is:

```text
r_u - b^T D^{-1} r_eta.
```

Only when `b=0` or `r_eta=0` does the raw derivative `r_u` equal `rho_q`.

# Retarded Kernel Derivative

The selected MTT overlap kernel has the schematic form already used in the
corpus:

```text
Y_q(Theta)
= sum_{gamma in Gamma_q(Theta)}
    A_gamma(Theta) exp(-S_gamma(Theta)) chi_gamma(Theta).
```

In the selected local chart, write:

```text
Y_q(s,eta)
= sum_gamma B_gamma(s,eta) exp(i phi_gamma(s,eta)),
B_gamma = A_gamma exp(-S_gamma).
```

For any coordinate `x_i` equal to either `s` or one component of `eta`,

```text
partial_i Y_q
= sum_gamma B_gamma exp(i phi_gamma)
   [partial_i log A_gamma - partial_i S_gamma
    + i partial_i phi_gamma].
```

If the real retarded cost is a smooth function of the complex overlap,

```text
R_q = Phi(Y_q, conjugate(Y_q), s, eta),
```

then:

```text
r_i = partial_i R_q(0,0)
```

is obtained by the chain rule from `partial_i Y_q`.

If the retarded datum is the overlap phase:

```text
delta_q = Arg Y_q,
```

and `Y_q(0,0) != 0`, then:

```text
partial_i delta_q
= Im[(partial_i Y_q)/Y_q] at (0,0).
```

This gives the force vector used above.  For example, if the local retarded
cost contains a term:

```text
lambda Phi_ret(delta_q),
```

then:

```text
r_i
= lambda Phi_ret'(delta_q(0,0)) Im[(partial_i Y_q)/Y_q].
```

The sign of `rho_q` is therefore a computable orientation statement about the
selected retarded channel data, not an independent convention once the kernel
is fixed.

# Spectral Sufficient Conditions

The exact pass condition is:

```text
D positive definite,
kappa_q = a - b^T D^{-1} b > 0,
0 < rho_q = r_u - b^T D^{-1} r_eta < 2 kappa_q.
```

A useful norm certificate is the following.

Let:

```text
lambda = smallest eigenvalue of D,
B      = ||b||,
R      = ||r_eta||.
```

Then:

```text
b^T D^{-1} b     <= B^2/lambda,
|b^T D^{-1} r_eta| <= B R/lambda.
```

So the stronger, directly checkable conditions:

```text
a > B^2/lambda,
r_u > B R/lambda,
r_u + B R/lambda < 2(a - B^2/lambda)
```

imply:

```text
kappa_q > 0,
0 < rho_q < 2 kappa_q.
```

These are sufficient, not necessary.  The exact Schur formulas should be used
when the selected matrices are known.

# Remainder Control

If the reduced cost has a cubic remainder:

```text
J_eff(s)
= J_eff(0) + rho_q s + 1/2 kappa_q s^2 + E_3(s),
```

then the exact quadratic conclusion survives under a simple derivative bound.

Let:

```text
epsilon = rho_q/kappa_q,
margin  = min(epsilon, 2-epsilon).
```

If:

```text
|E_3'(s)| < margin * kappa_q
```

for all `s in [-2,0]`, then:

```text
J_eff'(-2) < 0,
J_eff'(0)  > 0.
```

Thus the local critical point lies in:

```text
-2 < s_q < 0.
```

With strict convexity on the interval, it is the unique local minimizer there.

For the empirical CKM target computed earlier:

```text
epsilon_target = 0.999560473758,
margin_target  = 0.999560473758.
```

So the target is almost maximally centered in the retarded cell.

# Finite CKM Consequence

If the selected MTT data prove:

```text
0 < epsilon_MTT = rho_q/kappa_q < 2,
```

then:

```text
-2 < s_q < 0,
14 < u_q < 16.
```

The nearest primitive order-64 dyadic survivor is:

```text
q_64 = 15.
```

The selected Mukai component is:

```text
q_7 = 2.
```

Solving:

```text
q = 15 mod 64,
q = 2  mod 7
```

gives:

```text
q = 79 mod 448.
```

Then the phase-sum partner to the lepton quarter-turn `l=336` is:

```text
r = -(q+l) = 33 mod 448.
```

# Computational Check

The script:

```text
retarded_lag_schur_coefficient_formula.py
```

verifies the Schur formula by direct minimization of the quadratic model.
Its demonstration data are not MTT geometry.  They merely check the algebra.

The script reports:

```text
Schur rho matches direct minimization      PASS
Schur kappa matches direct minimization    PASS
positive nuisance Hessian                  PASS
actual selected MTT matrices supplied      OPEN
```

# What Must Be Supplied Next

To complete the proof, the selected MTT construction must provide:

```text
a,
b,
D,
r_u,
r_eta,
```

where:

```text
a,b,D      come from the selected quark closure-strain Hessian,
r_u,r_eta  come from the selected retarded overlap kernel derivative.
```

Then compute:

```text
rho_q   = r_u - b^T D^{-1} r_eta,
kappa_q = a   - b^T D^{-1} b.
```

The proof passes if:

```text
D > 0,
kappa_q > 0,
0 < rho_q < 2 kappa_q.
```

It fails, or the model must be revised, if:

```text
D is not positive on the projected nuisance sector,
kappa_q <= 0,
rho_q <= 0,
rho_q >= 2 kappa_q,
or r_u,r_eta require an entry-local phase knob.
```

# Gate Status

```text
exact Schur reduction theorem                         PROVED
linear closure-plus-retarded coefficient formula      PROVED
kernel derivative formula                             PROVED
finite implication to q_64=15                         PROVED
CRT implication to q=79 from q_64=15,q_7=2            PROVED
selected numeric H_q blocks supplied                  OPEN
selected retarded kernel derivative supplied          OPEN
non-empirical inequality 0<rho_q<2kappa_q             OPEN
```

# Bottom Line

The rigorous coefficient formula is:

```text
epsilon_MTT
= rho_q/kappa_q
= [r_u - b^T D^{-1} r_eta] / [a - b^T D^{-1} b].
```

This is the precise bridge from MTT geometry to the CKM numerator.

Once the selected Hessian blocks and retarded overlap derivative are supplied,
there is no further interpretive freedom: the ratio either lands in `(0,2)` and
proves `q=79`, or it does not.
