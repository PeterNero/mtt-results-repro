---
abstract: |
  We add an executable finite validator for the remaining SU(5) qutrit
  polarization packet.  The validator rejects the open template, rejects
  complete packets with bad transport or forbidden flavor inputs, and accepts
  an explicitly unselected qutrit fixture only as a smoke test.  A future
  selected packet must supply U_10, U_bar5, selected L2 metrics, sector
  qutrit operators, a common family pairing, and source guardrails before the
  SU(5) qutrit heavy-link candidate can be promoted to selected MTT data.
author:
- Peter Nero
date: May 2026
title: |
  Selected SU(5) Qutrit Polarization Validator
---

# Purpose

The previous gate identified the exact remaining object:

```text
U_10,
U_bar5,
U_10^dagger C U_bar5 = F or F^*
```

where `C` is the selected cross-sector family pairing or the certified common
family frame.

This note adds the executable validator:

```text
scripts/validate_selected_su5_qutrit_polarization.py
```

# Packet Contract

The future selected packet is:

```text
certificates/selected_su5_qutrit_polarization_data.template.json
```

It must supply:

```text
schema = SelectedSU5QutritPolarizationData.v1,
candidate_role = SELECTED_DATA,
source certificate,
U_10 and U_bar5,
selected L2 metrics,
sector clock and shift operators,
common family frame or cross-pairing metric,
acceptance-test flags.
```

# Finite Checks

The validator checks:

```text
U_10^dagger G_10 U_10 = I,
U_bar5^dagger G_bar5 U_bar5 = I,
Z^3 = X^3 = I,
Z X = omega X Z,
10_M diagonalizes the clock operator,
bar5_M diagonalizes the shift operator,
U_10^dagger C U_bar5 = F or F^* modulo rephasing/permutation,
q=79 orientation selects F,
observed masses, CKM entries, and benchmark flavor matrices are not inputs.
```

# Smoke Fixture

The finite qutrit fixture:

```text
candidate_data/selected_su5_qutrit_polarization.unselected_fixture.json
```

uses:

```text
U_10 = I_3,
U_bar5 = F.
```

It passes finite algebra and detects the `F` orientation.  However, it is
marked:

```text
candidate_role = UNSELECTED_FIXTURE,
selected_by_mtt = false.
```

Therefore it cannot promote the heavy-link candidate to selected data.

# Result

The validator closes the finite acceptance layer, not the geometric source.

The remaining research problem is now smaller:

```text
derive U_10 and U_bar5 from selected zero-mode data,
fill the packet,
rerun the validator.
```

Only then can the SU(5) qutrit heavy-link candidate become a selected
basis-connection input.
