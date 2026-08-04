# q79 R-only `u1=2`, `u2=27` Execution Contract

## Kernel Search Record

The MTT Research Kernel was bootstrapped on 2026-07-23 against repository
`mtt-q79-proof-repro` and current model hash
`79076e8fe7aaefb793e491513c99812d9720d2f8d2714d74210aeec1c48a7f7f`.
The controlling authorities are A08, A11, and A12. The exact search

```text
q79 R-only u1=2 u2=27 NO_EXACT_REDUCED_BASIS
```

returns only non-authoritative discovery material, including an older indexed
prefix ending at `u2=25`. It returns no curated classification of either
requested line. Durable handoff
`9c22ef81-0232-4a02-8e69-41732e2193fb` therefore locks the current committed
prefix certificate as the calculation input, not as a new authority.

## Controlling Input

```text
certificate: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
certificate SHA256: a43de1bd1485c7910b908647f7eaf15186873e37c9dbf3f5b42e82e6a995ec19
theorem SHA256:     4f9d0a0eae707d4802813e6359fdde1c317f8e8163858106bc8100fb4c17b730
status:      EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED
closed:      space 5 u2=1,...,26; space 6 u2=1,...,26
blocker:     space 5 u2=27 and space 6 u2=27: NO_EXACT_REDUCED_BASIS
Git input:   52af955c0a90035dae4657aa3913d3cd203fddb2
```

The Laurent-coordinate theorem maps `u2=27` to the canonical pair
`(scalar class,a)=(2,38)`.

The two selected symbolic inputs are fixed before execution:

```text
space 5 bytes=7617 SHA256=69384bdfd011194e9768edb9536c0ced10f4b0428385f5d16ef48ebc6b1c5a90
space 6 bytes=7574 SHA256=db4638ee1665b6b29967f7e09000c6f3df21e31977698ffdc4954376d92d989e
```

## Required Exit Certificate

One durable job must emit complete exact reduced Groebner bases and solver
logs for both `u2=27` R-only lines. The result packet must hash-bind:

- both family packets and the two preselected symbolic inputs;
- both reduced bases and complete logs;
- the deterministic seed and exact solver mode;
- the selected `msolve 0.10.1` binary hash;
- the normalized v2 runner source, Git commit, Python/OS environment, and
  dynamic libraries;
- this contract and the controlling 52-line prefix certificate.

The dedicated audit is
`proof_corpus/q79_Ronly_u1_002_u2_027_execution_audit.py`.

## Promotion Boundary

A literal basis `[1]` can be offered to the coordinator as an R-only line
certificate. A nonunit basis is only a classification: it still requires an
independent finite-quotient R/`y`/D unit certificate. Exit code zero does not
promote the contiguous-prefix theorem, characteristic zero, the physical q79
branch, HYM, quantum gravity, or any paper claim.
