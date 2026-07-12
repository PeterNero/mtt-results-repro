# Selected Horizontal-Scale Lemma for Iwasawa rho_UV v1

## Purpose

This note advances the remaining bridge lemma for the selected Iwasawa radius.

The previous reduction identified the exact missing statement:

```text
R is the selected horizontal scale coordinate of the Flux/Strominger
scale-lifting functional.
```

Here we prove the part supported by the current corpus and isolate the final
distinction that still prevents unconditional closure.

## Setup

On the symmetric Iwasawa branch in internal `alpha'=1` units, the source
calculation gives

```text
r1 = r2 = R,
r3^2(R) = 8(2pi)^2/(16+8/R^4).
```

The selected coefficient quotient evaluates the UV response row by

```text
v1_tilde(R) = 8 r3^2/R^4 = 64(2pi)^2/(16R^4+8).
```

The selected-character theorem then gives

```text
rho_UV(R) = v1_tilde(R)^2.
```

## Lemma 1: One-Dimensional Horizontal Coordinate

After imposing:

```text
1. the invariant Iwasawa ansatz,
2. the symmetric slice r1=r2,
3. the alpha'=1 internal normalization,
4. the componentwise Bianchi equation,
5. the finite coefficient quotient used by rho_UV,
```

the rho_UV response problem has one remaining positive coordinate, namely `R`.

Proof:

The symmetric ansatz leaves `R` and `r3`. The Bianchi equation expresses
`r3` as a function of `R`. The coefficient quotient only sees the scalar row
coefficient `v1_tilde(R)`. Therefore every rho_UV branch quantity in this
quotient factors through the single map

```text
R -> v1_tilde(R).
```

No second independent scale appears in the rho_UV coefficient problem.

## Lemma 2: Horizontal Scale-Lifting Functional

For the selected rho_UV coefficient problem, the scale-lifting functional may
be written directly in the horizontal coordinate:

```text
F_hor(R) = A(R) R^(-4) + B(R) R^2,
```

where the selected-character closure reduces the coefficient ratio to

```text
A(R)/B(R) = 30 rho_UV(R)
```

in the normalized `p=4`, `kappa=1` branch.

Equivalently, the local minimizer condition is encoded by

```text
R = (60 rho_UV(R))^(1/6).
```

This is exactly the fixed-point equation from the self-consistency candidate.

## What This Proves

This proves that the rho_UV branch does not need an arbitrary external `R`.
The branch has an internally defined horizontal fixed-point equation:

```text
R = s_*(R).
```

It also proves uniqueness of the candidate once this horizontal functional is
accepted, because `R` is increasing and `s_*(R)` is decreasing.

The unique candidate remains:

```text
R_*     = 2.7576341244749276,
r3      = 4.423799651933971,
v1      = 2.7072870676415306,
rho_UV  = 7.329403266619077,
s_*     = 2.7576341244749276.
```

## What This Does Not Yet Prove

The original scale-lifting lemma was stated for a common dilation of the
internal metric:

```text
length scale -> s length scale.
```

The Iwasawa horizontal branch is subtler:

```text
R varies,
r3 is constrained as r3(R).
```

Therefore this note does not prove that the full unprojected metric dilation
is literally the same as `R`. It proves the weaker and more relevant statement:

```text
inside the selected rho_UV coefficient quotient, R is the only scale coordinate
left for the branch.
```

To promote this to final closure, one more check is needed:

```text
the higher-alpha-prime UV penalty and OU damping floor used in the
scale-lifting lemma remain valid when restricted to the Bianchi-constrained
horizontal path R -> (R,R,r3(R)).
```

Call this the:

```text
Bianchi-Constrained Scale-Lifting Check.
```

## Primitive-Constant Fallback

If the Bianchi-Constrained Scale-Lifting Check fails, `R` must not be chosen by
target matching. The only credible fallback is to classify `R` as a primitive
internal constant if, and only if, it passes the primitive-constant discipline:

```text
universal,
prior,
audited,
not a unit convention,
not a target backsolve,
prediction-rich across sectors.
```

At present, the preferred route remains no-knob closure by proving the
Bianchi-constrained check.

## Verdict

The bridge has advanced:

```text
arbitrary R search                         CLOSED
one-dimensional rho_UV horizontal scale     CLOSED
unique fixed-point candidate                CLOSED
full common-dilation identification         NOT NEEDED for the coefficient quotient
Bianchi-constrained scale-lifting check     OPEN
```

The next artifact should test the UV and OU scaling laws directly along

```text
R -> (R,R,r3(R)).
```
