---
abstract: |
  We turn the next CKM frontier into an executable packet.  The prior C6 support
  gate proved that the leading heavy-link mismatch has the form
  Delta_v=Delta_t+chi_q Delta_c.  This note adds the selected packet schema and
  calculator.  It refuses incomplete data, forbids benchmark and observed
  flavor inputs, and computes the leading noncommutation pass/fail result once
  t_u,t_d,c_u,c_d are supplied from selected no-proxy sources.  The current
  packet is deliberately open: all eight heavy-link entries remain missing.
author:
- Peter Nero
date: May 2026
title: |
  CKM Heavy-Link Gate Calculator
---

# Purpose

The current frontier is:

```text
Delta_v = Delta_t + chi_q Delta_c.
```

This note creates the executable packet that will evaluate that formula once
the selected support data are available.

# Packet Entries

The selected packet is:

```text
certificates/selected_ckm_heavy_link_packet.template.json
```

It requires eight entries:

```text
t_u13, t_u23,
t_d13, t_d23,
c_u13, c_u23,
c_d13, c_d23.
```

Here:

```text
t_s = (T_s13,T_s23),
c_s = (C_s13,C_s23).
```

`T_s` is the aggregate character-trivial support and `C_s` is the selected C6
amplitude-support matrix.

# Calculation

The calculator is:

```text
scripts/compute_ckm_heavy_link_gate.py
```

Given a filled selected packet, it computes:

```text
Delta_t = t_d - t_u,
Delta_c = c_d - c_u,
Delta_v = Delta_t + chi_q Delta_c.
```

The leading CKM gate is:

```text
Delta_v != (0,0).
```

The C6 part affects the leading gate when:

```text
Delta_c != (0,0).
```

# Refusal Behavior

Running the calculator on the current template refuses the packet because all eight entries are still `null`.

This is intentional.  The calculator does not manufacture missing support
values.  It only evaluates selected values once they are supplied.

# No-Proxy Fill Rule

The allowed sources are:

```text
selected primitive C1/C3/C4/C7 or other character-trivial support,
selected C6 amplitude-support matrices,
selected branch orientation data,
normalization compatible with the rank-one E33 seed.
```

The forbidden sources are:

```text
Execution II benchmark entries,
observed fermion masses,
observed CKM angle magnitudes,
observed CKM phase or Jarlskog invariant,
post-hoc threshold fits,
arbitrary entry-wise phases outside the q79 C6 restriction.
```

# What This Closes

```text
heavy-link packet schema,
Delta_v calculator,
missing-entry refusal,
no-proxy fill contract.
```

# What Remains Open

```text
selected t_u,
selected t_d,
selected c_u,
selected c_d,
selected Delta_v value,
leading CKM pass/fail,
Jarlskog value,
Yukawa magnitudes,
full SM closure.
```

# Next Fill

The next successful calculation must replace the eight null entries in:

```text
certificates/selected_ckm_heavy_link_packet.template.json
```

from selected primitive contractions and selected C6 support matrices.  Then:

```powershell
python .\scripts\compute_ckm_heavy_link_gate.py .\certificates\selected_ckm_heavy_link_packet.template.json
```

will compute the first actual no-proxy leading CKM gate result.
