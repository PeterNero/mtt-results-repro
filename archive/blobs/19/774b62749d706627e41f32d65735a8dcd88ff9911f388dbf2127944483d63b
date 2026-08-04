# Stieltjes Massless Pole and Gaussian Damping No-Go v1

Date: 2026-07-15

## The theorem

Assume a Euclidean TT propagator has a positive spectral representation and a
massless residue:

```text
Delta(x) = r0/x + integral_0^infinity (x+s)^(-1) rho(ds),
rho >= 0,
r0 > 0.
```

Positivity immediately gives

```text
Delta(x) >= r0/x.
```

Suppose at the same time that the physical propagator has permanent Gaussian
suppression,

```text
Delta(x) <= C exp(-tau x)/(x+lambda),
C,tau>0,
lambda>=0.
```

Then `Delta(x)<=C exp(-tau x)/x`.  For

```text
x > log(C/r0)/tau
```

the upper bound is strictly smaller than the positive-spectral lower bound.
This is a contradiction.

## Consequence for the QG paper

The current QG paper claims all three of the following:

1. a positive Stieltjes/Kallen-Lehmann TT propagator;
2. a normalized massless pole `Delta=F(E)E^-1`, `F(0)=1`; and
3. permanent Gaussian damping on every physical graviton propagator.

The theorem proves that this conjunction is impossible.  This is not a missing
numerical coefficient and is not repaired by changing `lambda=15`.

## Correct routes

The conservative route is to retain the positive spectral representation and
massless GR pole, and treat proper-time damping as a removable regulator or
coarse-graining device rather than a permanent physical form factor.  Then the
existing all-loop Gaussian domination proof must be withdrawn or replaced.

Alternatively one may retain a permanent entire form factor, but then the
Stieltjes/OS positivity argument cannot prove unitarity; a different nonlocal
unitarity and causality theorem is required.  Negative-residue cancellations
can improve UV decay but also abandon positive spectral density.

This no-go sharply separates the viable low-energy GR construction from the
still-open UV-completion problem.
