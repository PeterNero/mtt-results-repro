# Scale-Lifting Lemma for Selected Flux/Strominger Functional v1

## Purpose

This note proves the remaining scale-lifting lemma in the form currently
supported by the corpus.

The result is a mathematical closure of the reduced scale problem, conditional
on extracting positive source-certified coefficients from the selected
Strominger/MTT branch. It does not yet compute the physical SI normalization.

## Source-Supported Scaling Inputs

The selected heterotic/MTT corpus supplies two scale-sensitive effects.

### Small-scale obstruction

The heterotic flux papers state that the leading Hull-Strominger solutions are
controlled at `O(alpha')`, while at `O(alpha'^2)` curvature-squared and
higher-derivative terms appear. Parametric control requires large volume and
small flux in string units.

For a remaining dilation `s > 0`, curvature-type corrections scale as a
positive inverse power. The reduced small-scale penalty therefore has the form

```text
F_UV(s) = A s^{-p},  A > 0, p > 0.
```

The exponent and coefficient must be extracted from the selected correction
calculation. The lemma below only requires positivity.

### Large-scale damping floor

The fixed-point/heterotic selection corpus gives the OU mode floor

```text
Var(a) = delta/(2 gamma),
gamma = kappa lambda - L - Delta_curv.
```

For a dilation of the internal metric, nonzero Laplacian eigenvalues scale as

```text
lambda(s) = lambda_0 / s^2.
```

On the exact selected branch in which the coherent linearization has no
uncontrolled Lipschitz leak in this scale direction (`L = Delta_curv = 0` after
projection/gauge fixing), the OU floor contributes

```text
delta/(2 kappa lambda(s))
  = [delta/(2 kappa lambda_0)] s^2
  = B s^2,
```

with `B > 0` whenever the selected unresolved disturbance strength is positive.

If `L + Delta_curv > 0`, the admissible interval is even smaller because
`gamma(s)` eventually vanishes. Thus the `B s^2` case is the most permissive
large-scale limit.

## Lemma

Let

```text
F_scale(s) = A s^{-p} + B s^2,     s > 0,
```

with

```text
A > 0, B > 0, p > 0.
```

Then:

```text
F_scale(s) -> +infinity as s -> 0,
F_scale(s) -> +infinity as s -> infinity,
F_scale has exactly one critical point,
that critical point is the unique global minimizer,
F_scale''(s_*) > 0.
```

The minimizer is

```text
s_* = (p A / (2 B))^(1/(p+2)).
```

The minimum value is

```text
F_scale(s_*) =
  A (2B/(pA))^(p/(p+2))
  + B (pA/(2B))^(2/(p+2)).
```

## Proof

First,

```text
lim_{s->0+} A s^{-p} = +infinity,
lim_{s->infinity} B s^2 = +infinity,
```

so `F_scale` is proper on `(0,infinity)`.

Differentiate:

```text
F_scale'(s) = -p A s^{-p-1} + 2 B s.
```

The critical equation is

```text
2 B s = p A s^{-p-1}
```

or equivalently

```text
2 B s^{p+2} = p A.
```

Since `s -> s^{p+2}` is strictly increasing on `(0,infinity)`, this equation
has exactly one positive solution:

```text
s_* = (p A / (2 B))^(1/(p+2)).
```

Differentiate again:

```text
F_scale''(s) = p(p+1) A s^{-p-2} + 2 B.
```

This is positive for every `s > 0`. Therefore `F_scale` is strictly convex on
`(0,infinity)`, and its unique critical point is the unique global minimizer.

This proves the lemma.

## Consequence for MTT Normalization

The selected flux/Strominger branch has a rigorous scale-lifting mechanism if
the branch supplies positive values of:

```text
A = selected UV/higher-alpha-prime correction coefficient,
p = selected correction exponent,
B = selected OU disturbance/damping coefficient.
```

Once these are extracted without target constants, the internal normalization is

```text
s_* = (p A / (2 B))^(1/(p+2)).
```

This is a no-knob result only if `A`, `B`, and `p` are computed from selected
MTT/Strominger data, not chosen from observed `G_N`, `M_Pl`, `H0`, `rho_DE`, or
absolute `f_a`.

## Status

The mathematical scale-lifting lemma is proved. The remaining physical task is
coefficient extraction:

```text
selected branch
-> compute A, B, p
-> evaluate s_*
-> only then compare derived dimensionful observables.
```

So the final gate is no longer qualitative. It is an explicit coefficient
calculation.
