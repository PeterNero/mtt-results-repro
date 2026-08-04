---
abstract: |
  We calculate the current exact Route B heavy-link object from the strongest
  available SU(5) qutrit polarization packet.  The finite packet gives
  U_10=I_3 and U_bar5=F, hence the relative transport U_10^dagger U_bar5=F.
  The five Route B overlap-difference slots are zero in this representation;
  the nonzero object sits in the selected-basis-connection slot and equals
  Delta_t=(1/sqrt(3), omega^2/sqrt(3)).  Because the upstream polarization
  packet remains an UNSELECTED_FIXTURE, this is an exact conditional
  calculation, not yet selected SM closure.
author:
- Peter Nero
date: May 2026
title: |
  Route B Final Missing Object Calculation Attempt
---

# Purpose

The Route B calculator needs:

```text
five u-d overlap-difference slots
plus selected theta/vertex/basis terms.
```

The strongest current finite packet supplies:

```text
U_10 = I_3,
U_bar5 = F.
```

This lets us calculate the equivalent heavy-link primitive.

# Calculation

The relative transport is:

```text
U_10^dagger U_bar5 = F.
```

With:

```text
F_jk = omega^(j k)/sqrt(3),
omega = exp(2*pi*i/3),
```

the heavy links are the entries:

```text
(1,3), (2,3).
```

Therefore:

```text
Delta_t = (1/sqrt(3), omega^2/sqrt(3)).
```

Numerically:

```text
Delta_t =
  (0.5773502691896258,
   -0.28867513459481287 - 0.5 i).
```

# Route B Packet

In the Route B five-slot format this is:

```text
A_left_delta       = 0,
B_right_row1_delta = 0,
B_right_row2_delta = 0,
C_higgs_row1_delta = 0,
C_higgs_row2_delta = 0,
```

with:

```text
theta_overlap_variation_delta = (0,0),
explicit_vertex_delta         = (0,0),
basis_connection_delta        = (1/sqrt(3), omega^2/sqrt(3)).
```

The Route B calculator then returns a structurally nonzero `Delta_t`.

# Selection Status

The calculation is exact, but the source is not selected yet.

The upstream packet is:

```text
UNSELECTED_FIXTURE_STRONGEST_CURRENT_ROUTE.
```

So the current object does not promote to selected CKM input.  It becomes the
selected final missing object only if the remaining source lemma closes:

```text
derive U_10=I_3 and U_bar5=F from selected gerbe/twisted-bundle,
monad/Cech, or spectral Galerkin zero-mode data.
```

# Status

Closed:

```text
exact conditional Route B object,
five-slot packet fill,
Delta_t calculation,
nonzero heavy-link gate at the structural level.
```

Still open:

```text
selected source promotion for U_10,U_bar5,
selected overlap-kernel prefactor,
canonical kinetic metrics,
Yukawa magnitudes,
full SM closure.
```
