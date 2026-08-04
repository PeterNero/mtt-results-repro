# q79 R-only triple-fiber explicit minimum-degree theorem

Date: 2026-07-20

## Theorem

Let `f_1,...,f_16` be the ten recurrence rows and six R-terminal rows obtained
from the canonical space-5, scalar-class-1 parent system over `F_101` after

```text
u0=u1=u2=u3=v=1,
(u1,a=v*u3,v)=(1,1,1).
```

The selected parent rows, in certificate order, are

```text
1,2,3,4,5,6,14,15,16,17,7,8,9,10,11,12.
```

There are explicit polynomials `q_1,...,q_16` such that

```text
sum_i q_i f_i = 1
```

in `F_101[h1,...,h6,y1,...,y4,u4,...,u7]`. Their maximum product total degree
is exactly nine, and no identity for this generating set has maximum product
total degree at most eight.

## Exact verification

The explicit payload contains 175,084 nonzero multiplier terms. A verifier
that does not read the F4 trace parses the sixteen source rows, multiplies all
terms modulo 101, and obtains the one-term residual `1`. The per-row product
degree profile is

```text
9,8,9,9,9,9,9,8,9,9,9,9,9,9,9,9.
```

The same verifier starts from the 19-variable parent input, performs the five
displayed substitutions, and checks that the resulting sixteen polynomials
are exactly the rows used by the certificate. The four D-terminal rows are
not used.

## Minimality proof

Individually homogenize each `f_i` to `f_i^h` with homogenizing variable `t`,
and put

```text
J = <f_1^h,...,f_16^h>.
```

Because `J` is homogeneous, a multiplier identity with
`deg(q_i)+deg(f_i)<=D` exists exactly when `t^D` belongs to `J`. Exact normal
form computation gives

```text
NF_J(t^8) = t^8,
NF_J(t^9) = 0.
```

Thus degree at most eight is impossible and degree nine is sufficient, so
degree nine is minimal. If an identity existed at any lower degree,
multiplication by a power of `t` would put `t^8` in `J`, contradicting its
nonzero normal form.

## Generation provenance

The payload was extracted from a one-thread official msolve F4 run. The
instrumented operation DAG had 45,786 nodes and 15,217,730 recorded reducer
terms. Reversing shared ancestry from terminal basis row 3220/node 44140
produced the sixteen multipliers. This trace explains their origin; the final
identity verifier does not trust or require the trace.

The packaged msolve 0.10.1 instrumentation patches must be applied in order:
`tail_dump`, `ancestry_dump`, `provenance_degree`, then `operation_dag`.
The resulting one-thread command is frozen in
`scripts/reproduce_q79_Ronly_explicit_degree9.sh`. Its operation DAG is
137,090,813 bytes with SHA-256
`d8146f94952d0e4013db26d155cd390541264920d413b47d0031eb9db739605d`.
An independent replay on 2026-07-20 reproduced that byte hash exactly.

## Claim boundary

This closes unit membership, explicit original-row provenance, and exact
minimum certificate degree for one displayed finite-field R-only triple
fiber. It introduces no continuous fit parameter.

It does not yet classify the other scalar triples, transport the theorem
across all mirror square-class charts, or promote this finite-field
obstruction to selected physical HYM or quantum-gravity data. Those are the
next targets.

## Reproducibility

Run:

```text
python scripts/certify_q79_Ronly_explicit_minimum_degree9.py
```

To regenerate the F4 trace and multiplier payload as well, apply the four
patches, set `MSOLVE_BIN` to that msolve build, and run:

```text
bash scripts/reproduce_q79_Ronly_explicit_degree9.sh
```

The consolidated theorem packet is
`certificates/Q79_Ronly_Triple_Fiber_Explicit_Minimum_Degree9_v2.json`.
