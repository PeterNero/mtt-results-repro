---
abstract: |
  We package the viable block-factorized Route B continuation as an executable
  five-slot calculator.  The calculator maps selected u-versus-d
  sector-resolved overlap differences to the two CKM heavy-link entries
  Delta_t, using the rank-two coefficient matrix computed by the dual-route
  closure attempt.  It refuses open templates and does not promote algebraic
  witnesses to selected data.
author:
- Peter Nero
date: May 2026
title: |
  Route B Heavy-Link Overlap-Difference Calculator
---

# Purpose

The dual-route attempt leaves Route B as the live continuation:

```text
selected sector-resolved C1/dotD overlaps
  -> five u-d overlap-difference slots
  -> Delta_t = (Delta_13, Delta_23).
```

This note records the executable packet contract for those five numbers.

# Packet

The packet schema is:

```text
RouteBHeavyLinkOverlapDifferencePacket.v1
```

It requires selected values for:

```text
A_left_delta,
B_right_row1_delta,
B_right_row2_delta,
C_higgs_row1_delta,
C_higgs_row2_delta.
```

It also requires selected values, or selected zero certificates, for:

```text
theta_overlap_variation_delta,
explicit_vertex_delta,
basis_connection_delta.
```

# Calculation

For each branch, the calculator loads the coefficient matrix from:

```text
candidate_data/dual_route_closure_attempt.candidate.json
```

and evaluates:

```text
Delta_t = A * overlap_differences
        + theta_overlap_variation_delta
        + explicit_vertex_delta
        + basis_connection_delta.
```

The q79 and q369 matrices both have complex rank two, so the map can reach both
heavy-link directions once selected values are supplied.

# Guardrail

The open template is intentionally refused.  The calculator accepts an
unselected algebraic witness only as an `UNSELECTED_FIXTURE`, and such a packet
does not promote to selected CKM input.

Forbidden fill sources remain:

```text
observed masses,
observed CKM or PMNS data,
Execution II benchmark Yukawa entries,
post-hoc fitted threshold factors.
```

# Status

Closed:

```text
Route B five-slot packet contract,
Route B Delta_t calculator,
template refusal for missing values,
unselected witness non-promotion.
```

Still open:

```text
selected overlap-difference values,
selected extra-term values or zero certificate,
selected CKM heavy-link packet,
Yukawa magnitudes,
full SM closure.
```
