# Selected Qa/SU3 HYM Connection Erratum or Convention Resolution v1

## Purpose

The full curvature attempt found that the printed HYM connection matrix does
not satisfy the standard integrability check.  This artifact explores whether a
simple convention change fixes the problem, and derives the minimal algebraic
repair if `B1` and `B2` are kept as printed.

## Convention Scan

The scan tested:

```text
as-printed matrices,
transpose matrices,
global negative matrices,
negative transpose matrices,
dbar(bar_omega^3) sign +1 or -1,
matrix wedge sign +1 or -1.
```

At `mu=1`, every tested convention has residual norm squared:

```text
||F02_bar12||_F^2 = 3.
```

So no simple transpose/sign convention resolves the mismatch.

## Minimal Standard Repair

Keeping `B1` and `B2` as printed, standard integrability requires:

```text
B3 = -(B1 B2 - B2 B1).
```

Since

```text
B1 B2 - B2 B1 = diag(-mu, 0, mu),
```

the required coefficient is:

```text
B3_required = diag(mu, 0, -mu).
```

The printed coefficient is instead:

```text
B3_printed = mu E12.
```

Thus the minimal algebraic repair is:

```text
replace mu E12 by mu(E11 - E33).
```

This replacement is traceless and restores the standard `F^(0,2)=0` condition,
but it is not currently source-certified because the corpus explicitly prints
the off-diagonal entry.

## Way Forward

There are two rigorous paths:

```text
1. Erratum/repair path:
   Amend or annotate the source connection, then rerun the curvature/Hessian
   pipeline using B3 = mu(E11-E33).

2. Retirement path:
   If the corpus cannot be amended, retire this displayed HYM matrix as a proof
   source for Qa/SU3 closure and search for another source-certified SU3/Qa
   operator.
```

The previous results still stand: constant torsion/OU completions cannot select
`mu`, and the direct commutator curvature norm does not select `mu`.

## Verdict

```text
simple convention resolves integrability: no
minimal algebraic repair identified: yes
minimal repair source-certified: no
mu selected: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Erratum_Repaired_HYM_Pipeline_or_Source_Retirement_v1
```
