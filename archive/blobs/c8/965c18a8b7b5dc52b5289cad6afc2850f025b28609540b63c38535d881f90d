# Selected Qa/SU3 HYM Strominger Weitzenbock OU Completion v1

## Purpose

This artifact carries the Qa/SU3 HYM block as far as the current corpus allows
toward the complete Strominger Hessian.

The previous artifact computed the real unitary Chern/HYM algebraic block on
`u(3)`.  Here we add the selected Iwasawa horizontal geometry and metric
weights.  The torsional Weitzenbock endomorphism and OU mode weights remain
open because the corpus gives their structural role, not their full numeric
matrix on `u(E)`-valued one-forms.

## Source-Backed Insertions

The selected internal Iwasawa radius from the closed rho_UV horizontal branch is

```text
R_* = r1 = r2 = 4.440528182269818,
r3  = 4.440028979122532.
```

The Iwasawa coframe source gives

```text
omega^1 = (e1+i e2)/r1,
omega^2 = (e3+i e4)/r2,
omega^3 = (e5+i e6)/r3.
```

Therefore the relative one-form weights inserted into the algebraic connection
block are

```text
|bar omega_1|^2 ~ 1/r1^2 = 0.05071433540836435,
|bar omega_2|^2 ~ 1/r2^2 = 0.05071433540836435,
|bar omega_3|^2 ~ 1/r3^2 = 0.050725739919091344.
```

A common complex-frame factor would rescale all eigenvalues and does not affect
whether `mu` is selected.

The same geometry gives the sourced Bismut curvature trace coefficient

```text
A = r3/(r1 r2),
Tr_grav R_+^2 = 8 A^2 alpha_1,
8 A^2 = 0.405623467693425.
```

This matches the selected-radius certificate value for `v1_tilde`.

## Metric-Weighted Real Chern Block

For each `mu`, compute

```text
H_weighted(mu)[X,Y]
  = sum_i w_i <[B_i,X],[B_i,Y]>
  + sum_i w_i <[-B_i^*,X],[-B_i^*,Y]>,
```

where

```text
w_i = 1/r_i^2.
```

Sample eigenvalues:

```text
mu = 0.25:
0, 0.00919501, 0.02852753, 0.02852753,
0.03169789, 0.03169789, 0.05388469, 0.05388469, 0.10491509

mu = 1:
0, 0.12862921, 0.15215441, 0.15215441,
0.20288015, 0.20288015, 0.25358308, 0.25358308, 0.47998843

mu = 4:
0, 1.02890009, 1.21732652, 1.21732652,
1.62304121, 1.62304121, 2.02893836, 2.02893836, 3.840406
```

The central `u(1)` commutator zero remains.  The eight `su(3)` directions stay
positive on the sampled branch.

## Mu Selection Scan

Scanning `mu in [10^-4,10^4]` on a logarithmic grid, the metric-weighted
algebraic log-det-prime is strictly increasing.  Thus the metric-weighted
algebraic Chern block still does not select an interior `mu`.

This is a stronger obstruction than before: even after inserting the selected
Iwasawa radius and relative one-form weights, the remaining selection cannot
come from this algebraic block alone.

## What Is Closed Now

```text
selected Iwasawa radius imported for the common horizontal geometry,
r3 and R_+ trace coefficient evaluated at the selected radius,
relative one-form metric weights inserted into the real Chern block,
metric-weighted u(3) block remains positive on su(3) samples,
metric-weighted algebraic determinant scan does not select interior mu.
```

## What Remains Open

The full Strominger operator still requires:

```text
actual torsional Weitzenbock endomorphism on u(E)-valued one-forms,
lower-order differential terms beyond the invariant algebraic band,
complete fixed-gauge quotient and any noncentral symmetry directions,
mode-by-mode OU weights gamma_{n,k}^{-1},
zeta/heat determinant of the complete elliptic operator.
```

The source theorem says the OU term is nonnegative and can lift residual flat
directions.  It does not provide the numeric `gamma_{n,k}` table for this
specific HYM family.  Therefore inserting arbitrary OU weights would be a knob.

## Verdict

```text
metric-weighted real Chern block computed: yes
selected Iwasawa geometry inserted: yes
R_+ trace coefficient inserted: yes
torsional Weitzenbock endomorphism computed: no
OU weights computed: no
full Strominger Hessian computed: no
mu selected: no
target fitting used: no
```

The next true gate is:

```text
Selected_Qa_SU3_Torsional_Endomorphism_or_OU_Mode_Weights_v1
```
