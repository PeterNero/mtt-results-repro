# Selected Qa/SU3 A01 Repair Guardrail Local Recompute v1

We recompute the sparse A01 repair options in the scale-free normal form

```text
A = sqrt(mu) B1 e1 + sqrt(mu) B2 e2 + mu B3 e3,
dbar e3 = e1 wedge e2.
```

The full invariant Maurer-Cartan equations are

```text
B3 + [B1,B2] = 0,
[B1,B3] = 0,
[B2,B3] = 0.
```

## Local Results

| candidate | B1 | B2 | B3 | reduced F12 | full MC |
|---|---|---|---|---|---|
| printed A01 | E13 | -E31 | E12 | fail | fail |
| repair A | E13 | -E31 | E11-E33 | pass | fail |
| repair B | E13 | -E32 | E12 | pass | pass |

The important result is narrow: moving the printed `B2=-E31` entry to
`B2=-E32` gives a sparse full-Maurer-Cartan integrable candidate.

## Guardrail

This does not close Qa/SU3. Repair B is not source-certified by the current
corpus. It is an erratum candidate unless a same-branch source selects it and
also supplies stability/HYM/Bianchi data plus the finite `D_E`, `rho_E`, or
torsion response.

Next required artifact:

```text
Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1
```

closure claimed: no
target fitting used: no
