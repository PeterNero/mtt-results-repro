# Selected Qa/SU3 Full Left-Invariant Curvature Matrix Attempt v1

## Purpose

This attempts the next requested gate:

```text
Selected_Qa_SU3_Full_Left_Invariant_Curvature_Matrix_v1
```

The attempt finds a source-level consistency obstruction.  With the printed
connection matrix and the printed Iwasawa structure equation, the standard
integrability check does not vanish.

## Source Equations Used

The source gives

```text
dbar(bar_omega_1)=0,
dbar(bar_omega_2)=0,
dbar(bar_omega_3)=bar_omega_1 wedge bar_omega_2.
```

It also prints

```text
A^(0,1)=B1 bar_omega_1 + B2 bar_omega_2 + B3 bar_omega_3
```

with

```text
B1 =
[0 0 sqrt(mu)]
[0 0 0]
[0 0 0]

B2 =
[0 0 0]
[0 0 0]
[-sqrt(mu) 0 0]

B3 =
[0 mu 0]
[0 0 0]
[0 0 0].
```

The same paragraph states:

```text
dbar_E^2=0.
```

## Integrability Check

For a standard matrix-valued `(0,1)` connection,

```text
F^(0,2) = dbar A^(0,1) + A^(0,1) wedge A^(0,1).
```

The coefficient of `bar_omega_1 wedge bar_omega_2` is

```text
F02_bar12 = B3 + (B1 B2 - B2 B1).
```

Substituting the printed matrices gives

```text
F02_bar12 =
[-mu  mu  0]
[  0   0  0]
[  0   0  mu].
```

Therefore

```text
||F02_bar12||_F^2 = 3 mu^2.
```

This vanishes only at `mu=0`, outside the source branch `mu>0`.

Changing only the sign of `dbar(bar_omega^3)` does not repair the problem: the
Frobenius norm is still nonzero for `mu>0`.

## Interpretation

This does not prove that the intended bundle is non-holomorphic.  It proves a
narrower and more useful statement:

```text
the displayed matrix, read with the displayed Iwasawa structure equation and
standard matrix-valued wedge convention, does not reproduce the displayed
claim dbar_E^2=0.
```

So the full curvature matrix cannot be source-certified from the printed data
until one of the following is resolved:

```text
transpose/dual-bundle convention for matrix action,
missing diagonal or off-diagonal connection entries,
different sign convention for matrix-valued wedge products,
different sign in dbar(bar_omega^3),
monad basis contribution not represented by the displayed matrix.
```

## What Is Closed

```text
direct full-curvature computation from the printed data is blocked,
the obstruction is explicit and reproducible: residual norm 3 mu^2,
no target fitting or mu choice can repair integrability for mu>0.
```

## Verdict

```text
full left-invariant curvature matrix computed: no
printed data pass standard integrability: no
source erratum or convention needed: yes
mu selected: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_HYM_Connection_Erratum_or_Convention_Resolution_v1
```
