# q79 R-only `u1=2`, Remaining `u2=29,...,100` Batch Contract

## Kernel Lock

This calculation was opened through MTT Research Kernel handoff
`e402eaa9-f0c1-474e-8b11-31ca36ec6885` on 2026-07-23 under model hash
`79076e8fe7aaefb793e491513c99812d9720d2f8d2714d74210aeec1c48a7f7f`.
The controlling authorities are A08, A11, and A12. Kernel search found the
single-line runner and historical prefix packets, but no existing accepted
batch classification of the requested 144 lines.

## Frozen Source

```text
Git input: fd5409547d565f6356b47a08f280e65cf76376bd
prefix: certificates/Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json
prefix SHA256: 22d66acc7cbb3987bb0c874389fcc7d1941af3afe89e0b3c06f0cef607aef936
prefix theorem SHA256: 5566a581531f0e464f1c2fad421efb32466b8b65e648d73eb84c0367781c64ba
closed before execution: u2=1,...,28 in spaces 5 and 6
requested range: u2=29,...,100 in spaces 5 and 6
requested lines: 144
input bytes: 1,095,915
canonical input-row digest:
dab8dd378995a01b12c9e72b7d574f9982e356a6f53b0749472c8086f76c4824
```

The committed `input_manifest.json` lists and hash-binds every selected
symbolic input before execution. No solver output is a manifest input.

## Execution Design

The batch must:

- run serially in ascending `u2`, then space 5 and space 6;
- use deterministic seed `790000 + u2` for both spaces at a fixed `u2`;
- run `msolve 0.10.1` in exact `F_101`, DRL, one-thread mode;
- cap each line at 12 GiB and two hours;
- accept only complete reduced bases with complete exact-mode logs;
- checkpoint atomically after every line;
- validate every checkpoint artifact before resuming;
- write the accepted batch result only after all 144 lines finish;
- bind the clean Git commit, both runners, manifest, contract, prefix, solver
  binary, Python/OS environment, and dynamic-library report.

The mean of the six fresh `u2=26,27,28` line executions is 266.1 seconds,
giving an estimated serial runtime of 10.64 hours. This is an estimate, not a
timeout or theorem input.

## Interruption and Resume

An interruption leaves a runtime checkpoint and completed `.out`/`.log`
artifacts but no accepted final batch packet. Resume must use the same
committed source state and the `--resume` flag. Completed rows are rehashed,
reclassified, and log-validated before the next line starts.

## Promotion Boundary

The batch performs exact R-only classification. A literal reduced basis `[1]`
is eligible for later line promotion. Every nonunit basis remains open until
an independent selected finite-quotient R/`y`/D unit certificate is built and
audited. Batch completion alone does not promote the contiguous prefix,
characteristic zero, the physical q79 branch, HYM, QFT, quantum gravity,
Standard Model values, or any paper claim.
