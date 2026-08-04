# q79 R-only `u1=2`, `u2=24` Execution Contract

## Coordinator Search Record

The live kernel was queried on 2026-07-22 with:

```text
q79 u2 24                                      scope=all
Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1 scope=status,claims
NO_EXACT_REDUCED_BASIS u2 24                   scope=all
```

The exact status and claims searches return no curated row. The broad searches
return indexed material and non-authoritative claims only; none classifies either
requested line. Therefore the committed prefix certificate is the calculation
authority input and candidate evidence, not a kernel promotion.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: 38d90a40b7f28fa28114ac749f4f459ecc61d9d6425c643e8efbf7c03abf3b08
theorem SHA256:     8a7387e595adfe50c52e24e3284ea6df45273b520ce0e480e765bb464d56dd20
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,23; space 6 u2=1,...,23
blocker:     space 5 u2=24 and space 6 u2=24: NO_EXACT_REDUCED_BASIS
Git input:   c748563df5e98dc993fe86a467794a980889c961
```

The Laurent-coordinate theorem maps `u2=24` to the canonical pair
`(scalar class,a)=(1,22)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7607 SHA256=acc13e6b018353e7cf85e4ba631ca2f11f96d423c9064cffb1321898cae97c87
space 6 bytes=7598 SHA256=9db2246e056feebdbd579e1d029f6009bcde8b750620e87cd5ad9b627e019862
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=24` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 46-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_024_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
