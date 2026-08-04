# Selected Iwasawa Radius Bridge Reduction v1

## Purpose

The selected-character rho_UV theorem closes

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2
```

and the self-consistency candidate shows that the equation

```text
R = s_*(R)
```

has one positive solution. This note asks whether the current corpus already
proves the required bridge:

```text
Iwasawa horizontal radius R = scale-lifting dilation s.
```

## What the Corpus Proves

The Iwasawa flux/Strominger calculation gives, in internal `alpha'=1` units,

```text
r1 = r2 = R,
r3^2(R) = 8(2pi)^2/(16+8/R^4).
```

Thus the symmetric Iwasawa branch is one-dimensional after the invariant
coefficient choices are fixed. The rho_UV theorem evaluates the UV row on this
one-dimensional branch.

The scale-lifting lemma proves that a reduced functional

```text
F_scale(s) = A s^(-p) + B s^2
```

has a unique positive minimizer. In the selected rho_UV branch, after the
selected-character closure,

```text
s_*(R) = (60 rho_UV(R))^(1/6).
```

Therefore, if the remaining scale coordinate of the selected Flux/Strominger
functional is the same coordinate as the symmetric Iwasawa radius, the selected
radius must satisfy

```text
R = s_*(R).
```

## What the Corpus Does Not Yet Prove

The current scale-lifting text describes `s` as a common dilation / string-unit
scale. The Iwasawa branch parameter `R` is the horizontal radius `r1=r2`, while
`r3` is not freely dilated with it; it is constrained by the Bianchi equation.

So the bridge cannot be silently assumed. The missing lemma is exactly:

```text
Selected Horizontal-Scale Lemma:
  after the invariant Iwasawa gauge and alpha'=1 action normalization are
  imposed, the only scale direction seen by the selected rho_UV
  Flux/Strominger scale functional is the horizontal radius R.
```

Equivalently, prove that the apparent difference between:

```text
common metric dilation s
```

and:

```text
Iwasawa horizontal branch coordinate R with r3=r3(R)
```

is already removed by the selected Bianchi constraint and coefficient quotient.

## Conditional Selected-Radius Theorem

Assume the Selected Horizontal-Scale Lemma. Then the selected radius is the
unique positive fixed point of

```text
R = (60)^(1/6) [64(2pi)^2/(16R^4+8)]^(1/3).
```

The solution is

```text
R_*     = 2.7576341244749276,
r3      = 4.423799651933971,
v1      = 2.7072870676415306,
rho_UV  = 7.329403266619077,
s_*     = 2.7576341244749276.
```

The fixed point is unique because the left side is strictly increasing in `R`
and the right side is strictly decreasing in `R`.

## Shared-Circle Compatibility

The exact central-circle branch supplies

```text
R1(N) = sqrt(log N / 15).
```

At the candidate Iwasawa radius:

| N | R1(N) | R1(N)/R_* |
|---:|---:|---:|
| 64 | 0.5265537695468319 | 0.1909440287504026 |
| 79 | 0.5397189300902845 | 0.195718106800354 |
| 448 | 0.6379547127299338 | 0.231341317931872 |

There is no immediate contradiction with the shared-circle setup:

```text
R1(N) <= 2
```

still holds for the tested branches, and R_* is not the central-circle radius.
It is the Iwasawa horizontal radius. Therefore `R_* > 2` does not violate the
central-circle admissibility bound.

This does not prove LensNil closure. LensNil can use a ratio `R1/R`, but the
current corpus does not select the flux integers `(f,h)` that would certify one
of the ratios above.

## Correct Way Forward

The path to final closure is now:

```text
1. Prove the Selected Horizontal-Scale Lemma.
2. Promote the conditional selected-radius theorem to final.
3. Separately audit LensNil/shared-circle compatibility by deriving the flux
   integers or showing the ratio gate is not needed for rho_UV.
```

The most important discipline point is that step 1 must be internal. It cannot
be proved by observing that the resulting `rho_UV` is numerically attractive.

## Verdict

The missing puzzle piece is no longer an arbitrary radius search. It is one
precise bridge lemma:

```text
R is the selected horizontal scale coordinate of the Flux/Strominger
scale-lifting functional.
```

If that lemma is proved, the rho_UV branch closes to a single internal
dimensionless value. If it fails, then `R=s_*(R)` is only a useful candidate,
and the program must instead compute the reduced scale functional directly in
the Iwasawa branch coordinate.
