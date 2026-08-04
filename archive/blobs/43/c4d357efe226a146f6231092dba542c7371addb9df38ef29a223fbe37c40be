---
title: |
  Time-Oriented m=1 Visible Green-Schwarz Source Gate
author: MTT proof reproduction program
---

# Purpose

We now create the next object explicitly: a selected visible Green-Schwarz
source packet for the time-oriented `q79/F,m=1` branch.

This object is stricter than the previous coefficient requirement.  It must
show not only that the correct row is known, but that the row is realized by a
selected visible HYM/Route-C source.

The selected visible Green-Schwarz source packet is therefore a source
promotion object, not another coefficient-only certificate.

# Required Row

The previous requirement certificate derived:

```text
Tr F_visible^2 =
[
  8*r3^2/(r1^2*r2^2) + 4*r3^2,
  0,
  0
]
```

in the invariant basis:

```text
alpha_1 = a wedge b,
alpha_2 = a wedge c,
alpha_3 = b wedge c.
```

# Source Gate

The new validator requires:

```text
selected_by_mtt = true,
same_branch_as_q79_m1 = true,
fixture_only = false,
no observed flavor data,
no benchmark flavor entries,
Tr F_visible^2 equals the derived row,
residual = 0,
selected visible bundle model supplied,
Chern-Weil row derived from that source,
HYM or Route-C residual verified.
```

# Current Attempt

The current attempt can fill the required curvature row exactly, but it cannot
mark the source as selected.  The strongest available HYM/operator-source
attempt still says:

```text
selected visible SM bundle model: open,
selected HYM operator source: not verified.
```

Therefore the attempt packet is rejected by the validator.

# What This Closes

This closes:

```text
executable selected visible-source gate,
packet schema for the source object,
exact row insertion from the requirement certificate,
machine rejection of the current unselected attempt.
```

# What Remains

This does not close:

```text
selected visible bundle construction,
HYM or Route-C residual verification,
Chern-Weil derivation from selected source,
projector retention,
selected D_E/dotD/Riesz/Green files,
primitive C1 contractions,
full SM closure.
```

# Artifacts

The validator is:

```text
scripts/validate_time_oriented_m1_visible_gs_source.py
```

The attempt constructor is:

```text
scripts/attempt_time_oriented_m1_visible_gs_source.py
```

It writes:

```text
certificates/time_oriented_m1_visible_gs_source.template.json
certificates/time_oriented_m1_visible_gs_source.attempt.json
candidate_data/time_oriented_m1_visible_gs_source_attempt.candidate.json
certificates/time_oriented_m1_visible_gs_source_attempt_certificate.json
```

# Verdict

The object has been created as an executable proof gate.  The gate is not yet
passed by current data.  The next proof input is a selected visible HYM/Route-C
source whose Chern-Weil row realizes the derived `alpha_1` coefficient.
