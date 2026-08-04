# q79 R-only `u1=2` Complete Nonzero-`u2` CRT Gluing Theorem

## Status

`EXACT_FULL_NONZERO_U2_CRT_GLUE_CERTIFIED`

Coverage: `COMPLETE_F101_NONZERO_U2_TORUS_IN_BOTH_SPACES`

## Theorem

For space 5 let

```text
P_5(u2) = product_(a=1)^100 (u2-a) in F_101[u2],
```

and for space 6 let

```text
P_6(u2) = product_(a=1)^100 (u2-a) in F_101[u2].
```

The certificate emits every Lagrange projector

```text
e_a = (P_s/(u2-a)) * ((P_s/(u2-a))(a))^(-1) mod P_s.
```

Their evaluation matrices are the identity, each `e_a` is idempotent modulo
`P_s`, and they sum to one. Hence

```text
F_101[u2]/(P_5) ~= product_(a=1)^100 F_101,
F_101[u2]/(P_6) ~= product_(a=1)^100 F_101.
```

Every factor is an already-certified complete R-only or full R/`y`/D unit
component. Therefore the full selected ideal quotient is the zero ring over
the complete nonzero `F_101` `u2` torus in each space. This glues `200` line
certificates, representing `20000` canonical fixed `F_101` fibers, into
two exact finite-algebra statements.

Writing `A_s` for the selected ambient algebra and `J_s` for its full
R/`y`/D ideal, the exact conclusion is

```text
A_s/(J_s + (P_s))
    ~= product_(a=1)^n_s A_s/(J_s + (u2-a))
     = product_(a=1)^n_s 0
     = 0.
```

## Projector Polynomials

Coefficients are ascending and reduced modulo `101`.

```text
P_5: [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
P_6: [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```

## What This Adds

The linewise computation is connected by an explicit algebraic decomposition,
not only by counting. All 100 nonzero `u2` components are certified in both
spaces, and both projector polynomials are exactly `u2^100-1`. The theorem
therefore closes each entire selected nonzero finite `u2` torus without a
monolithic Groebner run.

## Boundary

No new line is classified here. The theorem does not provide expanded global
Nullstellensatz coefficients and does not address the other 98 nonzero `u1`
values, mirror zero-zero charts, characteristic zero, or physical HYM/QG
promotion. The global symbolic chart count remains `138/140`. New continuous
fit parameters: `0`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_partial_CRT_gluing_audit.py
```
