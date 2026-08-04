# q79 R-only `u1=2`, `u2=28` Execution Contract

## Kernel Search Record

The MTT Research Kernel was bootstrapped on 2026-07-23 against repository
`mtt-q79-proof-repro` and current model hash
`79076e8fe7aaefb793e491513c99812d9720d2f8d2714d74210aeec1c48a7f7f`.
The controlling authorities are A08, A11, and A12. The exact search

```text
q79 R-only u1=2 u2=28 NO_EXACT_REDUCED_BASIS
```

returns only non-authoritative discovery material, including an older indexed
prefix and a different symbolic-exception row whose selected coordinate is
`u2=21`. It returns no curated classification of either requested line.
Durable handoff `01d03282-0a67-4c15-9a46-a9f9ffdf9dc3` therefore locks the
current committed prefix certificate as the calculation input, not as a new
authority.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: 8def90b387d733ed826dc39c9d7aaa6aa1878b992fbcfdd66475a1a709593d1c
theorem SHA256:     fa369ef0638f9f5ad8beff7087fe51367792eebaa939e3598ac5ea19ac32ea96
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,27; space 6 u2=1,...,27
blocker:     space 5 u2=28 and space 6 u2=28: NO_EXACT_REDUCED_BASIS
Git input:   0aea407677284f3762843fa165d31b85f5a9c6fc
```

The Laurent-coordinate theorem maps `u2=28` to the canonical pair
`(scalar class,a)=(2,41)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7584 SHA256=98b988c7e281ffff2e0e3370c1d03d045f491a5e2a88d29a4a13c61a6291999c
space 6 bytes=7605 SHA256=9d6052a0a37c8aae3aae3b9827ce7917a6d41887730288828077ba6c046c99c9
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=28` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 54-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_028_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
