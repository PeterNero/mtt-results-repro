# q79 R-only `u1=2`, `u2=23` Execution Contract

## Coordinator Search Record

The live kernel was queried on 2026-07-22 with:

```text
q79 u2 23                                      scope=all
Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1 scope=status,claims
NO_EXACT_REDUCED_BASIS u2 23                   scope=all
```

The exact status and claims searches return no curated row. The broad searches
return indexed material only, plus one non-authoritative lexical claim about the
generic exceptional locus; none classifies either requested line. Therefore the
committed prefix certificate is the calculation authority input and candidate
evidence, not a kernel promotion.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: 4fe1a39f2471635590dec2f491ae29c8d751cfadca3bd417ec8643f3aa8b1801
theorem SHA256:     01f0ff2acd42bdb81e6c483a0e996c9c7607577ea7e64d8e0a08543d43297b14
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,22; space 6 u2=1,...,22
blocker:     space 5 u2=23 and space 6 u2=23: NO_EXACT_REDUCED_BASIS
Git input:   a4531c531b52562992706a998bb2f773565814cd
```

The Laurent-coordinate theorem maps `u2=23` to the canonical pair
`(scalar class,a)=(1,27)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7606 SHA256=154766b1102bb803080343a0ec3d900fe1157a42ef390f01d342db095102c67e
space 6 bytes=7581 SHA256=139632a883b89aad588cf33e9a072e5e5e95809cfd6cd8131582add71dfc9e52
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=23` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 44-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_023_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
