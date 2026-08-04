---
title: "Orientation Observable Parity"
version: v1
---

# Result

The q79/q369 finite operator pair now has an observable-parity ledger.

At the current finite operator layer:

```text
CP-even norm checks:        133 / 133 pass
complex conjugation checks: 329 / 329 pass
maximum conjugation error:  1.6653345369377348e-16
nonzero imaginary sign flips: 21
```

# Meaning

The q79 and q369 branches are not distinguishable by CP-even finite operator
norm data.  They are related by antiunitary conjugation, so orientation-sensitive
imaginary diagnostics flip sign while norms stay fixed.

This supports the following conditional rule for the future selected Yukawa
matrices:

```text
If Y(q369) = conjugate(Y(q79)), then singular values, mass ratios, and CKM
angle magnitudes agree, while Jarlskog-type CP-odd signs reverse.
```

# Guardrail

This does not compute selected Yukawa matrices, masses, CKM angles, or the
Jarlskog value.  It only proves the parity rule that any future selected
Yukawa packet must obey if it is built from the current antiunitary pair.

# Remaining Selector

The remaining selector is therefore still:

```text
a selected source or retarded boundary theorem that chooses one orientation,
or a theorem that only CP-odd sign depends on that choice.
```
