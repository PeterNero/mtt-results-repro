# q79 R-only `u1=2`, `u2=22` Execution Contract

## Coordinator Search Record

The live kernel was queried on 2026-07-22 with:

```text
q79 u2 22                                      scope=all
Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1 scope=status,claims
NO_EXACT_REDUCED_BASIS u2 22                   scope=all
```

The searches return the committed repository theorem and certificate as
indexed material, including `u2=22` as the next exact obligation. The scoped
status and claims searches return no curated row. Therefore the committed
certificate is the calculation authority input and candidate evidence, not a
kernel promotion.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: 4a4d20f565ceca9169ebc59a297c0402f85bf1b731f680ceb1b8ee1bafa02651
theorem SHA256:     6ae79586a3d637a378af106ce8e3f28e774c8b3e00a552618b3f562f46cb9632
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,21; space 6 u2=1,...,21
blocker:     space 5 u2=22 and space 6 u2=22: NO_EXACT_REDUCED_BASIS
Git input:   ee066a02608e841c3ae7b0ae6d4f9e97754cf2b1
```

The Laurent-coordinate theorem maps `u2=22` to the canonical pair
`(scalar class,a)=(1,15)`.

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=22` R-only lines. The result packet must hash-bind:

- both family packets and symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the runner source, Git commit, Python/OS environment, and dynamic libraries;
- this contract and the controlling 42-line certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_022_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, or quantum gravity.
