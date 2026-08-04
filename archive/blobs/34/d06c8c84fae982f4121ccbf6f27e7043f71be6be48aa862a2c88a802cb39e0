# q79 R-only `u1=2`, `u2=25` Execution Contract

## Coordinator Search Record

The live kernel was queried on 2026-07-22 with:

```text
q79 u2 25                                      scope=all
Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1 scope=status,claims
NO_EXACT_REDUCED_BASIS u2 25                   scope=all
```

The exact status and claims searches return no curated row. The broad searches
return indexed material and non-authoritative claims only; none classifies either
requested line. Therefore the committed prefix certificate is the calculation
authority input and candidate evidence, not a kernel promotion.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: edc295c600f318531e74c256e5ecb13b4b2d729528418a4a87b0a7c55f23a42e
theorem SHA256:     7e87627bf2b32f90c96a3d3d0b79ff9c1ab0efe042b846a81920a7b240f908e9
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,24; space 6 u2=1,...,24
blocker:     space 5 u2=25 and space 6 u2=25: NO_EXACT_REDUCED_BASIS
Git input:   6865f3f0d4129fee32ef26fadd2eab82f1867de5
```

The Laurent-coordinate theorem maps `u2=25` to the canonical pair
`(scalar class,a)=(1,20)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7604 SHA256=1acd4a446ab88e0f7b19cdb3515d80ad7761a026ce8e8b8be3fc7fd94a84b061
space 6 bytes=7602 SHA256=5512ba896d815b60f2a7c88be3cb4e5d511527db3ca7eaf1e090d762dbdc9bb7
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=25` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 48-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_025_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
