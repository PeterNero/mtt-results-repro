# MTT Selected q79 Picard-Lefschetz One-Sided Residual Regularization

## Purpose

A123 removed the first apparent nodal wall by proving exact projective
line-chart covariance. It then continued the same selected `ell=0` normal-
function lift until a genuinely distinguished branch pair appeared in a
well-conditioned chart.

A124 resolves the local geometry of that later wall. It locates a transverse
simple node, derives the oriented local vanishing-period state, transports that
state through the homogeneous Gauss-Manin system, and compares the transported
endpoint jump with two independently continued one-sided beta representatives.
The Picard-Lefschetz formula is exact under the stated hypotheses. The wall
location, one-sided limits, and endpoint comparison are floating computations;
they are not promoted to interval claims here.

## Exact local theorem

Let the selected hyperelliptic fiber be

```text
U^2=f(t;s,u),
```

where `s` is a real carrier parameter and `u` is the complex base parameter.
Suppose that at `(s_*,u_*,t_*)`

```text
f(t_*;s_*,u_*)=0,
f_t(t_*;s_*,u_*)=0,
f_tt(t_*;s_*,u_*) != 0.
```

Assume additionally that the discriminant is crossed transversely, the
splitting divisor is disjoint from the node, and both continuations start from
the same A123 integral lift rather than independently recomputed Abel-Jacobi
paths.

Near the node, the holomorphic Morse coordinate gives

```text
f(t;s_*,u_*)=(f_tt(t_*)/2)(t-t_*)^2+O((t-t_*)^3).
```

For the reduced period basis `omega_k=t^k dt/U`, `k=0,...,4`, the positively
oriented vanishing cycle therefore has limiting state

```text
V_k = 2*pi*i*t_*^k/sqrt(f_tt(t_*)/2).
```

Changing the square-root branch reverses all five components together and is
exactly the orientation ambiguity of the vanishing cycle. The sign is fixed in
this packet by the sign of `Im(du_*/ds)` along the real carrier path.

Let `beta_-` and `beta_+` be the two one-sided continuations of the same
normal-function lift. Their inhomogeneous sources agree away from the wall and
therefore cancel in the difference. Consequently the period jump obeys the
homogeneous Gauss-Manin equation, and its residue contribution obeys

```text
dV/du = i A_GM V,
dJ/du = i K Res_A(V),
J(u_*) = 0.
```

It follows that the endpoint jump is

```text
beta_+ - beta_- = T_GM(u_end,u_*) V,
```

with the residue rows integrated by the displayed `J` equation. This is the
local transported Picard-Lefschetz formula used by the analyzer.

**Q79TransverseSimpleNodeTransportedPLJumpTheorem.** Under the simple-node,
transversality, divisor-disjointness, and same-integral-branch hypotheses, the
two one-sided beta continuations differ by the endpoint Gauss-Manin transport
of the oriented local state
`V_k=2*pi*i*t_*^k/sqrt(f_tt(t_*)/2)`.

The theorem is an exact identity. Applying it to a particular floating wall
does not by itself certify that wall or either endpoint vector by intervals.

## Selected wall execution

The continuation direction is the previously rejected radius-`0.001` A123
Levenberg-Marquardt direction. Solving the four real equations represented by
`f=f_t=0` gives

```text
s_* = 0.23502677005564024
u_* = 0.734552355113436
t_* = 0.32587425869698694 + 0.00051355389152308011 i.
```

The maximum `f,f_t` residual is `5.08749e-12`. The coupled real Jacobian has

```text
determinant = -9.835972108566931e16
singular values =
  540562.0591, 518938.7055, 31664.09179, 11.07359481.
```

Moreover,

```text
f_tt = 204426.40986929683 + 476977.16999373637 i
|f_tt| = 518938.7033
du_*/ds = -0.00010291264961316409
           - 0.00033573150797259501 i.
```

Thus the computed node is simple and the real carrier direction crosses the
complex discriminant transversely. The normalized `y`-chart scale is
`0.8740349066`, so this is not the A122 affine-chart collapse. The nearest
selected `q_A` root is `0.0113190` from the double root, establishing divisor
disjointness at the floating execution level.

## One-sided beta limits

Independent continuations were evaluated at offsets

```text
0.1, 0.05, 0.02, 0.01, 0.005.
```

Linear and quadratic extrapolations give

```text
selected-minus limit norm = 2.3571633144823667
crossed-plus limit norm    = 2.788072919231946
jump norm                  = 1.2208745071976763.
```

The linear/quadratic vector discrepancies are `1.341e-5` on the selected side
and `4.879e-6` on the crossed side. These values are numerical convergence
checks, not error bounds.

## Transported jump comparison

The exact local state was transported from four cutoffs
`1e-3, 3e-4, 1e-4, 3e-5` and extrapolated to the wall. The result has norm

```text
1.2208885174694104.
```

Compared with the independently extrapolated one-sided jump, it has

```text
projective overlap = 0.9999999999999621
best complex scale = 0.99998852452696807
                     + 0.00000155549046709 i
relative residual  = 2.7472377910502627e-7.
```

The limiting scale is numerically one, including orientation. This validates
that the discontinuity seen after A123 is the unit Picard-Lefschetz jump of the
same selected normal-function branch rather than a new lift or a chart artifact.

## Strict conclusion

A124 closes:

- the exact local vanishing-state formula for the five reduced periods;
- cancellation of the common inhomogeneous source in the one-sided difference;
- the exact homogeneous Gauss-Manin transport formula for the endpoint jump;
- a floating, full-rank transverse simple-node realization in the regular
  projective chart;
- a converged numerical unit-jump comparison with relative residual
  `2.75e-7`.

A124 does not prove:

- an interval enclosure of the wall coordinates or transversality;
- an interval lower bound for the selected-side beta norm;
- a global `ell=0` no-go over all admissible `PGL3` carriers;
- a smooth `ell=0` zero or a selected nonzero vector in `Z^92`.

The next target is sharply smaller than at A123: interval-enclose this wall and
the regularized selected-side beta limit. Since its floating norm is about
`2.357`, even a comparatively coarse certified enclosure can exclude this
specific basin. That would be a local nonzero theorem, not yet the global
`ell=0` no-go.
