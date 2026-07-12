# Bianchi-Constrained Scale-Lifting Check for Iwasawa rho_UV v1

## Purpose

The selected horizontal-scale lemma showed that the rho_UV coefficient problem
has one remaining horizontal coordinate `R`.

This note checks the next issue directly:

```text
when rho_UV depends on R, can we still use R = s_*(R)?
```

The answer is: not automatically.

## Key Point

The scale-lifting lemma gives

```text
F_scale(s) = A s^(-4) + B s^2
```

and, for constant positive `A` and `B`,

```text
s_* = (2A/B)^(1/6).
```

But in the selected Iwasawa branch, the UV coefficient is not constant along
the Bianchi-constrained path:

```text
A(R) = rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2.
```

Therefore the equation

```text
R = (60 rho_UV(R))^(1/6)
```

is a fixed-point candidate, not yet the Euler-Lagrange equation of the
Bianchi-constrained one-variable functional.

## Two Possible Reduced Functionals

The corpus currently leaves one scale-law choice open.

### Branch H1: extra horizontal residual scaling

If `rho_UV(R)` is the selected coefficient and the first omitted
`alpha'/R^2` residual contributes the squared horizontal factor separately,
then the reduced functional is

```text
F_H1(R) = rho_UV(R) R^(-4) + (1/30) R^2.
```

Its direct minimizer is

```text
R_H1 = 2.982841305980989,
rho_UV(R_H1) = 3.929428772053664,
s_*(R_H1) = 2.485498155594327,
r3(R_H1) = 4.428918195741528.
```

This is not the old fixed-point value.

### Branch H2: rho_UV already includes the full UV scale response

If `rho_UV(R)` is already the complete UV penalty coefficient in the horizontal
quotient, then the reduced functional is

```text
F_H2(R) = rho_UV(R) + (1/30) R^2.
```

Its direct minimizer is

```text
R_H2 = 4.44052820580178,
rho_UV(R_H2) = 0.16453039057735,
s_*(R_H2) = 1.464646764366198,
r3(R_H2) = 4.44002897918297.
```

This is also not the old fixed-point value.

## Old Fixed-Point Candidate

The earlier self-consistency candidate was

```text
R_FP = 2.7576341244749276,
rho_UV(R_FP) = 7.329403266619077.
```

It remains a useful compatibility equation, but this check shows it is not yet
the final minimizer unless the corpus proves that the selected-radius condition
is fixed-point consistency rather than ordinary one-variable minimization with
an `R`-dependent coefficient.

## What Must Be Selected

The remaining gate is no longer "find R". It is:

```text
select the correct Bianchi-constrained horizontal scale law.
```

The corpus must decide whether the UV contribution is:

```text
H1: rho_UV(R) R^(-4),
H2: rho_UV(R),
FP: fixed-point consistency R = s_*(R),
or a third source-derived functional.
```

This must be done from the higher-alpha-prime correction and OU kernel
definitions, not from comparing the numerical outputs.

## Primitive-Constant Implication

If this scale-law selection cannot be closed, then a remaining primitive
constant may exist. In that case the primitive-constant discipline applies:
`R` or the scale-law selector must be universal, prior, audited, and
prediction-rich. It cannot be chosen target-by-target.

## Verdict

This check prevents an overclaim.

Closed:

```text
rho_UV(R) branch function,
one-dimensional horizontal coordinate,
candidate fixed-point equation,
direct H1 and H2 minimizers.
```

Open:

```text
which horizontal scale law is selected by the actual higher-alpha-prime
correction and OU damping kernel.
```

The next correct artifact is:

```text
Selected_Horizontal_Scale_Law_for_Iwasawa_Rho_UV_v1.
```
