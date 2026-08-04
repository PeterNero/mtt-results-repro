# q79 R-only triple-fiber frontier

> Superseded on 2026-07-20 by
> `Q79_Ronly_Triple_Fiber_Explicit_Minimum_Degree9_v2.md`, which emits and
> independently verifies the sixteen original-row multipliers and proves that
> degree nine is minimal.

Date: 2026-07-20

## Exact result

For the space-5, scalar-class-1 endpoint fiber

```text
(u1, a=v*u3, v) = (1,1,1),
(u0,u2,u3) = (1,1,1),
```

the ten recurrence rows

```text
1,2,3,4,5,6,14,15,16,17
```

together with the six R-terminal rows

```text
7,8,9,10,11,12
```

generate the unit ideal over `F_101`. The four D-terminal rows
`18,19,20,21` are not used.

This is exact for the displayed fiber. It is not yet a theorem for all one
million nonzero triples in this scalar chart.

## Independent constructions

The direct 14-variable R-only system has reduced Groebner basis `[1]`.

The ten triangular recurrence rows also eliminate
`h1,...,h6,y1,...,y4`, leaving six polynomials in four carriers
`u4,u5,u6,u7`. Their profiles are:

| R row | terms | total degree |
|---:|---:|---:|
| 7 | 3,030 | 14 |
| 8 | 4,814 | 16 |
| 9 | 7,242 | 18 |
| 10 | 10,533 | 20 |
| 11 | 14,812 | 22 |
| 12 | 20,301 | 24 |

Both exact msolve linear-algebra modes reduce this four-carrier system to
`[1]`. Since each carrier polynomial is the corresponding R terminal modulo
the recurrence ideal, the original selected 16-row fiber ideal is unit.

## Degree lower bound

Deterministic sparse elimination gives:

| bound | `rank(A_D)` | `rank([A_D|e_1])` | conclusion |
|---:|---:|---:|---|
| 6 | 14,831 | 14,832 | inconsistent |
| 7 | 58,490 | 58,491 | inconsistent |

Therefore no multiplier identity exists whose products have ordinary total
degree at most 7. The first unexcluded Macaulay degree is 8.

The F4 log's largest stage label of 6 is not an ordinary-total-degree
certificate bound for this inhomogeneous system. The exact rank tests resolve
that apparent conflict.

## What remains open

The mathematical unit-membership question for this fiber is closed. Expanded
six-carrier multipliers and their composed 16-row identity remain unprinted:
eager Groebner change-matrix, Singular `liftstd`, and target-only `lift`
implementations reached guarded timeouts. Those are provenance-expansion
timeouts, not failures of unit membership.

The proof frontier is now:

1. derive the `(u1,a,v)` weighted orbit action, or otherwise classify the one
   million triples in each scalar chart;
2. replay only the final unit-row elimination DAG if an explicit multiplier
   list is required;
3. repeat or transport the result across the four mirror square-class charts;
4. only then ask for physical HYM/QG promotion.

No continuous fit parameter was introduced.

## Reproducibility anchors

The compact theorem packet is
`certificates/Q79_Ronly_Triple_Fiber_Unit_and_Min_Degree_v1.json`.
Its parent input SHA-256 is
`ebde92a7b0742cf7337708fcd2e5bccc188c52837c4cff4382af9c31e3de16fe`.
The four-carrier input SHA-256 is
`649dc1b912d5f0128964fd9bec3a046622fd8ca6597ee0721f022e1e0d3c59a3`.
