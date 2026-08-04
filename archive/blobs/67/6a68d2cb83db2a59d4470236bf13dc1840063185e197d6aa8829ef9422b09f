---
abstract: |
  We close the next finite gate after the Iwasawa C6 global phase block.  Since
  all surviving C6 channels carry the same q79 phase, the phase is not an
  entry-wise knob.  At leading order near the rank-one seed, selected C6 support
  can affect CKM noncommutation only through the up/down heavy-link mismatch
  Delta_v=(M_d13-M_u13,M_d23-M_u23).  Writing M_s=T_s+chi_q C_s, the exact
  criterion is Delta_v=Delta_t+chi_q Delta_c != (0,0).  The current package
  contains no selected C6 support matrices or amplitudes, so this note closes
  the support criterion and keeps the numeric values, Jarlskog invariant, and
  Yukawa magnitudes open.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa C6 Support Noncommutation Gate
---

# Purpose

The previous C6 calculation closed the pure holonomy phase:

```text
u:C6, d:C6, e:C6, nuD:C6 all carry chi_79
```

or all carry the conjugate `chi_369`.  Thus the remaining C6 freedom is a
global branch, not four independently assignable channel phases.

The next question is sharper:

```text
can the selected C6 support enter the CKM noncommutation test?
```

This note answers that question as a finite criterion.

# Setup

Near the rank-one seed:

```text
Y_s = E33 + epsilon M_s + O(epsilon^2),
H_s = Y_s Y_s^dagger.
```

The leading CKM noncommutation theorem already gives:

```text
[H_u,H_d] = epsilon [E33,A_d-A_u] + O(epsilon^2),
```

with:

```text
A_s = E33 M_s^dagger + M_s E33.
```

Only the heavy-link vector enters the leading term:

```text
v_s = (M_s13, M_s23).
```

Therefore:

```text
Delta_v = v_d - v_u
        = (M_d13-M_u13, M_d23-M_u23).
```

The leading commutator is nonzero exactly when:

```text
Delta_v != (0,0).
```

# C6 Decomposition

Separate the leading correction matrix into a character-trivial aggregate and
the selected C6 contribution:

```text
M_s = T_s + chi_q C_s.
```

Here:

```text
T_s = aggregate of selected non-C6 or character-trivial supports,
C_s = selected C6 amplitude-support matrix,
chi_q = exp(2*pi*i*79/448) or its conjugate.
```

For the heavy-link vectors:

```text
t_s = (T_s13,T_s23),
c_s = (C_s13,C_s23),
v_s = t_s + chi_q c_s.
```

Thus:

```text
Delta_v = Delta_t + chi_q Delta_c,
Delta_t = t_d - t_u,
Delta_c = c_d - c_u.
```

# Gate

The finite C6 support gate is:

```text
Delta_t + chi_q Delta_c != (0,0).
```

The C6 part affects the leading heavy-link mismatch exactly when:

```text
Delta_c != (0,0).
```

This is not yet the full CKM CP theorem.  It is the leading orientation gate
that a selected C6 support packet must pass before the q79 phase can contribute
to the leading noncommutation test.

# Cases

```text
Delta_c = (0,0):
  C6 does not affect the leading heavy-link gate.
  Noncommutation, if present, comes from Delta_t.

c_d = c_u:
  C6 support cancels between up and down at order epsilon.

Delta_c != (0,0):
  C6 enters the leading gate.
  Leading noncommutation passes unless Delta_t = -chi_q Delta_c.

full CP:
  still requires nondegenerate spectra and Im det([H_u,H_d]) != 0.
```

# Current Data Scan

The executable calculator searches for selected C6 support packet locations:

```text
certificates/selected_c6_support_matrices_certificate.json
certificates/iwasawa_c6_support_matrices_certificate.json
certificates/selected_c6_support_data_certificate.json
candidate_data/selected_c6_support_matrices.json
candidate_data/iwasawa_c6_support_matrices.selected.json
```

None are present in the current package.

The open fields in the existing certificates also agree:

```text
C6 amplitudes A_gamma remain open,
C6 nonzero matrix support remains open,
Delta_v remains uncomputed,
selected Y_u,Y_d remain uncomputed.
```

# What This Closes

```text
C6 support entry target,
leading C6 heavy-link gate,
guardrail against treating the global C6 phase as a fitting knob,
confirmation that selected C6 support values are absent from this package.
```

# What Remains Open

```text
selected C6 amplitude-support matrices C_u and C_d,
character-trivial heavy-link vectors t_u and t_d,
Delta_t + chi_q Delta_c,
selected Y_u,Y_d,
nondegenerate singular-value spectra,
Im det([Y_uY_u^dagger,Y_dY_d^dagger]),
Yukawa magnitudes and full SM closure.
```

# Next Packet

The next no-proxy data packet should provide:

```text
C_u13, C_u23, C_d13, C_d23,
t_u = (T_u13,T_u23),
t_d = (T_d13,T_d23).
```

Then the first executable CKM test is:

```text
Delta_t + chi_q Delta_c != (0,0).
```

If it passes, the branch has leading up/down noncommutation.  The final CKM CP
claim still waits for the full basis-invariant Jarlskog calculation.
