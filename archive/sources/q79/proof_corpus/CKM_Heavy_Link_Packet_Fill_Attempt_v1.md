---
abstract: |
  We attempt to fill the selected CKM heavy-link packet.  The attempt scans the
  current proof package and the broader local MTT corpus for the eight required
  entries t_u13,t_u23,t_d13,t_d23,c_u13,c_u23,c_d13,c_d23.  No selected entries
  are available.  The selected C1 primitive contractions still have 24 missing
  matrices, the selected C1 response Delta_v is null, and no selected C6 support
  file is present.  Therefore the packet is not numerically filled; the blocked
  attempt records exactly what must be supplied next.
author:
- Peter Nero
date: May 2026
title: |
  CKM Heavy-Link Packet Fill Attempt
---

# Purpose

The CKM heavy-link calculator is ready, but it needs the selected packet:

```text
t_u13, t_u23,
t_d13, t_d23,
c_u13, c_u23,
c_d13, c_d23.
```

This note records the attempted fill.

# Attempt

The executable attempt is:

```text
scripts/attempt_fill_ckm_heavy_link_packet.py
```

It writes:

```text
certificates/selected_ckm_heavy_link_packet.attempt.json
```

The attempt checks:

```text
selected C1 primitive contractions,
selected C1 response data,
selected C6 support packet locations,
direct heavy-link entry tokens in the proof package,
direct heavy-link entry tokens in the broader local MTT corpus.
```

# Result

The fill attempt is blocked:

```text
status = BLOCKED_SELECTED_HEAVY_LINK_SOURCES_MISSING.
```

The exact missing heavy-link entries are:

```text
inputs.character_trivial_heavy_link.u.entries[0]
inputs.character_trivial_heavy_link.u.entries[1]
inputs.character_trivial_heavy_link.d.entries[0]
inputs.character_trivial_heavy_link.d.entries[1]
inputs.c6_heavy_link.u.entries[0]
inputs.c6_heavy_link.u.entries[1]
inputs.c6_heavy_link.d.entries[0]
inputs.c6_heavy_link.d.entries[1]
```

The current selected C1 primitive template still has:

```text
24 missing primitive 3x3 matrices.
```

The selected C1 response template has:

```text
Delta_v_ud = null.
```

No selected C6 support file is present at the expected packet locations:

```text
certificates/selected_c6_support_matrices_certificate.json
certificates/iwasawa_c6_support_matrices_certificate.json
certificates/selected_c6_support_data_certificate.json
candidate_data/selected_c6_support_matrices.json
candidate_data/iwasawa_c6_support_matrices.selected.json
```

The broader local MTT corpus scan finds no direct occurrences of the eight
entry tokens.  Therefore no no-proxy selected values can be copied into the
packet.

# Interpretation

The heavy-link test is finished as an executable gate, but not numerically
closed:

```text
Delta_v = Delta_t + chi_q Delta_c
```

cannot be evaluated until `Delta_t` and `Delta_c` are selected data.

For the character-trivial part:

```text
t_u,t_d
```

we need selected primitive contractions or an equivalent selected aggregate
support calculation.

For the C6 part:

```text
c_u,c_d
```

we need selected C6 amplitude-support matrices.

# What This Closes

```text
heavy-link fill attempt executed,
external local corpus direct-entry scan executed,
selected C1 primitive absence confirmed,
selected C6 support absence confirmed,
blocked attempt packet written.
```

# What Remains Open

```text
selected t_u,t_d,
selected c_u,c_d,
selected Delta_v,
leading CKM noncommutation pass/fail,
Jarlskog value,
Yukawa magnitudes,
full SM closure.
```

# Next Required Data

The next actual selected-data packet must provide either:

```text
selected primitive contractions that compute M_u13,M_u23,M_d13,M_d23,
```

or a sector-resolved equivalent for the character-trivial heavy-link aggregate,
plus:

```text
selected C6 amplitude-support matrices C_u and C_d.
```

Only then can the existing calculator evaluate:

```text
Delta_t + chi_q Delta_c != (0,0).
```
