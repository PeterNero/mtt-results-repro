---
title: |
  Selected Matter-Slot Transversality Source Gate
author: MTT proof reproduction program
---

# Target

The finite theorem now says:

```text
selected transverse qutrit matter slots + retarded q79
  => U_10=I_3, U_bar5=F.
```

This note builds the missing upstream gate.  The gate asks whether the corpus
has actually supplied the selected source for:

```text
10_M   = clock-polarized qutrit slot,
bar5_M = shift-polarized qutrit slot.
```

# Validator Contract

The source packet must contain:

```text
selected source certificate, not a fixture,
retarded q79/F branch with conjugate q369 retained,
common family frame,
selected L2 metrics,
selected projector retention,
selected zero-mode basis,
U_10 and U_bar5 matrices,
U_10^dagger C U_bar5 = F,
no observed masses, CKM entries, or benchmark flavor entries.
```

The open template is:

```text
certificates/selected_matter_slot_transversality_source.template.json
```

The validator is:

```text
scripts/validate_selected_matter_slot_transversality_source.py
```

# Route C First Attempt

Route C is the first executable path because it already has finite validators
for:

```text
rho_E mesh,
rho_E metric,
sector projectors,
D_E action,
Riesz gap,
reduced Green operator,
dotD response.
```

The existing branch-smoke packet has a useful status:

```text
honest rho_E/metric/sector validators pass,
honest selected-origin D_E/Riesz/Green/dotD validators fail,
lifted selected-flag smoke copies pass algebraically.
```

Therefore the first source fill attempt writes:

```text
certificates/selected_matter_slot_transversality_source.attempt.json
```

It includes the finite `U_10=I_3, U_bar5=F` matrices only as the candidate
shape to be tested.  It deliberately marks selected-source evidence as absent.

# Result

The validator rejects the Route C attempt for the right reason:

```text
source.selected_by_mtt is false,
Route C selected-origin evidence is false,
10_M/bar5_M selected_source_verified flags are false,
selected metrics/projector retention/zero-mode basis are false.
```

This is progress: the finite object is not the blocker.  The blocker is now a
precise source theorem:

```text
replace Route C smoke selected flags with a genuine selected HYM/Strominger or
spectral Galerkin residual solve whose honest validators pass.
```

# Verdict

Closed:

```text
strict source-packet interface,
strict validator,
Route C first fill attempt,
exact blocker identification.
```

Still open:

```text
selected Route C origin,
selected D_E/dotD on the same retarded branch,
selected projector retention,
selected zero-mode bases,
full SM closure.
```
