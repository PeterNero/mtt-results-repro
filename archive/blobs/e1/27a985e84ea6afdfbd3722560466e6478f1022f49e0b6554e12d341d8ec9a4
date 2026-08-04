---
abstract: |
  After the pure finite qutrit/C6 route gives Delta_c=(0,0), the leading CKM
  heavy-link calculation moves to the character-trivial part Delta_t.  We reduce
  that calculation from full C1 primitive 3x3 matrices to only the 24 scalar
  heavy-link primitive entries needed for t_u,t_d.  The calculator refuses the
  open template and computes Delta_t once those selected scalar entries are
  supplied.  This closes the reduced computation contract, not the values.
author:
- Peter Nero
date: May 2026
title: |
  C1 Heavy-Link DeltaT Reduction
---

# Purpose

The heavy-link gate is:

```text
Delta_v = Delta_t + chi_q Delta_c.
```

The pure finite qutrit/C6 calculation gives:

```text
Delta_c = (0,0)
```

for the C6-only conjugate finite pairing.  Therefore the next live source is:

```text
Delta_t = t_d - t_u.
```

# Reduced Data

The full C1 primitive template asks for:

```text
4 sectors x 6 primitive 3x3 matrices.
```

But the leading CKM heavy-link test only needs the up/down entries:

```text
M_u13, M_u23, M_d13, M_d23.
```

For the C1 part, this reduces to:

```text
2 sectors x 6 primitive terms x 2 heavy-link entries = 24 scalars.
```

# Packet

The reduced packet is:

```text
certificates/selected_c1_heavy_link_primitives.template.json
```

For each of `u` and `d`, it asks for the `(13,23)` vector from:

```text
theta_overlap_variation,
left_zero_mode_response,
right_zero_mode_response,
higgs_zero_mode_response,
explicit_vertex,
basis_connection.
```

# Calculator

The calculator is:

```text
scripts/compute_c1_heavy_link_delta_t.py
```

It computes:

```text
t_s = sum over six selected C1 primitive heavy-link vectors in sector s,
Delta_t = t_d - t_u.
```

It then reports whether:

```text
Delta_t != (0,0).
```

# Current Status

The current packet is open and all 24 scalar entries are `null`.  The
calculator refuses the template rather than manufacturing values.

# What This Closes

```text
reduced C1 heavy-link packet schema,
Delta_t calculator,
missing-entry refusal,
proof that full 3x3 primitive matrices are not required for the leading CKM gate.
```

# What Remains Open

```text
selected C1 heavy-link 24 scalars,
selected Delta_t value,
selected Delta_v value,
leading CKM noncommutation pass/fail,
Jarlskog value,
Yukawa magnitudes,
full SM closure.
```

# Next Calculation

Instead of trying to fill all 24 C1 primitive matrices immediately, the next
minimal calculation should fill only:

```text
u/d sector, six primitive terms, entries 13 and 23.
```

This is the smallest selected-data packet that can decide the leading CKM
orientation once the pure C6 route is removed.
