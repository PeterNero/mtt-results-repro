# q79 R-only `u1=2`, `u2=26` Execution Contract

## Kernel Search Record

The MTT Research Kernel was bootstrapped on 2026-07-23 against repository
`mtt-q79-proof-repro` and current model hash
`79076e8fe7aaefb793e491513c99812d9720d2f8d2714d74210aeec1c48a7f7f`.
The controlling authorities are A08, A11, and A12. The exact search

```text
q79 R-only u1=2 u2=26 NO_EXACT_REDUCED_BASIS
```

returns the committed prefix and verifier as non-authoritative discovery
material. It returns no curated classification of either requested line.
Durable handoff `a4077b35-dc41-45d4-9b3f-0b7fc2c79e23` therefore locks the
committed prefix certificate as the calculation input, not as a new authority.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: 7c020f68054ff0a54c2c33e64450e72f4cced56245606737e2ad7e23a7182785
theorem SHA256:     987adb95b456603853dcbe5955ef6067ff7caf412549df064bd4e666e37b1d1b
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,25; space 6 u2=1,...,25
blocker:     space 5 u2=26 and space 6 u2=26: NO_EXACT_REDUCED_BASIS
Git input:   98ca614cdd473c1a49007e5a3950f26b6fe8d75f
```

The Laurent-coordinate theorem maps `u2=26` to the canonical pair
`(scalar class,a)=(2,26)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7621 SHA256=4bcbb6bf024e265cbcdf0e6b2a8ed9354e80b87f291de0728e8423dfcb16e77d
space 6 bytes=7609 SHA256=9a1a7a4179e00319402c00bf6941fe099ed6e1eb41256a5037e6833cc091b8db
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=26` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 50-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_026_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
