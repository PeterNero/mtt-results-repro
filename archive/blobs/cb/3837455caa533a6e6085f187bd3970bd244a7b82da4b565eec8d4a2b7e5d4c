# Selected Qa/SU3 HYM Color Connection Spectrum or Torsion Computation

## Purpose

This note advances the Qa/SU3 color-connection branch from existence data to
actual matrix data.

The heterotic Iwasawa source supplies an explicit left-invariant
Hermitian-Yang-Mills candidate connection on the rank-3 SU(3) bundle E.  The
question is whether this is enough to compute the missing Qa/SU3 determinant,
heat coefficient, or analytic torsion without using the target residual.

## Extracted Matrix Data

The source gives:

```text
A^(0,1) = B1 bar_omega_1 + B2 bar_omega_2 + B3 bar_omega_3,  mu > 0
```

with coefficient matrices:

```text
B1 =
[ 0  0  sqrt(mu) ]
[ 0  0  0        ]
[ 0  0  0        ]

B2 =
[ 0         0  0 ]
[ 0         0  0 ]
[ -sqrt(mu) 0  0 ]

B3 =
[ 0  mu  0 ]
[ 0  0   0 ]
[ 0  0   0 ]
```

The same source states:

```text
c1(E) = 0,
c2(E) = 0 / Tr F_E wedge F_E = 0 in the invariant sector,
c3(E) = 6 a wedge b wedge c,
F_E != 0.
```

The last line matters: `c2(E)=0` does not make the connection flat.

## Computed Algebraic Invariants

Each coefficient matrix is nilpotent:

```text
trace(Bi) = 0,
det(Bi) = 0,
ordinary eigenvalues(Bi) = 0,0,0.
```

But this is not the spectrum of the connection Laplacian.  The relevant
threshold determinant depends on the full Laplace-type operator, including:

```text
metric,
Chern/HYM connection,
torsional endomorphism,
representation,
BRST quotient,
det-prime zero-mode rule,
boundary/domain data.
```

A simple source-independent diagnostic already detects a live continuous
parameter:

```text
sum ||Bi||_F^2 = 2 mu + mu^2.
```

Thus a numeric determinant would vary continuously unless `mu` is selected by
MTT/Strominger data before comparison with the Qa/SU3 residual.

## What This Closes

This closes the vague part of the previous blocker:

```text
actual HYM connection matrix data exists.
```

The branch is no longer merely existential.  We have the matrix form of the
candidate connection.

## What Remains Open

The determinant is still not computable because the following data are missing:

```text
1. selected value or rule for mu > 0,
2. selected representation: E, End(E), adjoint, or associated local system,
3. selected Laplace-type threshold operator,
4. selected spectrum, heat coefficients, or analytic torsion finite part,
5. compatibility proof between Iwasawa HYM and compact-Nil Qa determinant data.
```

## Verdict

```text
actual HYM matrix extracted: yes
numeric Qa/SU3 determinant: no
target fitting used: no
full SM closure: no
```

Next artifact:

```text
Selected_Qa_SU3_HYM_Mu_and_Operator_Domain_Selection_v1
```
