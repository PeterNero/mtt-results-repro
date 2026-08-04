# q79 R-only `u1=2`, `u2=21` Execution Contract

## Coordinator Search Record

The live kernel was queried on 2026-07-21 with:

```text
q79 u2 21                                      scope=all
Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1 scope=status,claims
NO_EXACT_REDUCED_BASIS                         scope=status,claims
```

The first query returns the repository theorem and certificate as indexed
material. The scoped searches return no curated status or claim row. Therefore
the committed certificate is the calculation input and candidate evidence,
not a kernel promotion.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: f46e19860a1abfca548b3d5af5f93dc164d0de469581577751c56103788c77c4
theorem SHA256:     ead6f767b07e8e1706560942c57282756942053dab12fcd3757014a4b0eaa558
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,20; space 6 u2=1,...,20
blocker:     space 5 u2=21 and space 6 u2=21: NO_EXACT_REDUCED_BASIS
Git input:   e54211938b4b6b9c5ac8fac3ea8ad8b760d38571
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver logs
for both `u2=21` R-only lines. The result packet must hash-bind:

- both family packets and symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the runner source, Git commit, Python/OS environment, and dynamic libraries.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_021_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, or quantum gravity.
