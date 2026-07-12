---
title: |
  SU(5) Projection Tensor Derivation Attempt
author: MTT proof reproduction program
---

# SU(5) Projection Tensor Derivation Attempt

This note records the attempted derivation of the sector projection data that
would distinguish the up and down Yukawa contractions without using observed
flavor data.

The executable artifact is:

```text
scripts/derive_su5_projection_tensor_attempt.py
```

It writes:

```text
candidate_data/su5_projection_tensor_derivation_attempt.candidate.json
certificates/su5_projection_tensor_derivation_attempt_certificate.json
```

## Finite Derivation

The finite qutrit transport lemma proves:

```text
clock polarization -> shift polarization = F,
```

with the conjugate alternative:

```text
clock polarization -> opposite shift polarization = F*.
```

Therefore, if selected zero-mode data prove:

```text
10_M    is clock-polarized,
bar5_M  is shift-polarized,
```

then the SU(5) projection tensors are forced:

```text
q79 branch:
  U_10   = I_3,
  U_bar5 = F,
  T_u    = U_10^dagger U_10    = I_3,
  T_d    = U_10^dagger U_bar5  = F.

q369 branch:
  U_10   = I_3,
  U_bar5 = F*,
  T_u    = I_3,
  T_d    = F*.
```

This is the finite projection tensor we were trying to derive.

## Heavy-Link Consequence

For the q79 branch:

```text
Delta_t = (T_d13 - T_u13, T_d23 - T_u23)
        = (1/sqrt(3), omega^2/sqrt(3)).
```

Numerically:

```text
Delta_t = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i).
```

For the conjugate q369 branch:

```text
Delta_t = (1/sqrt(3), omega/sqrt(3)).
```

Numerically:

```text
Delta_t = (0.5773502691896258,
           -0.28867513459481287 + 0.5 i).
```

The existing calculators confirm, for both branches:

```text
selected SU(5) qutrit polarization validator: finite algebra PASS,
C1 heavy-link Delta_t calculator: PASS,
CKM heavy-link gate: leading noncommutation PASS.
```

The C6 heavy-link difference is kept zero in this calculation, so the
noncommutation comes from the character-trivial projection tensor.

## Why This Is Not Yet Selected Data

The polarization validator reports:

```text
promotes_to_selected_heavy_link_input = false.
```

The reason is not algebraic failure.  The reason is source failure:

```text
source.selected_by_mtt = false.
```

The current corpus proves the finite qutrit transport, but it does not yet
derive `U_10` and `U_bar5` from selected monad/Cech/Galerkin zero-mode data or
from a selected gerbe/twisted-bundle source.

So the result is:

```text
finite projection tensor: derived conditionally,
selected MTT projection tensor: still open.
```

## What This Closes

This closes:

```text
the exact branch-aware candidate tensor,
the q79 versus q369 conjugate orientation,
the induced Delta_t values,
the validator-ready polarization packet form.
```

It does not close:

```text
selected U_10 and U_bar5,
selected C1 response matrices,
Yukawa magnitudes,
CKM angle magnitudes,
full SM closure.
```

## Next Proof

The next proof is now precise:

```text
derive U_10 and U_bar5 from selected monad/Cech/Galerkin zero-mode data
or from selected gerbe/twisted-bundle data.
```

Once that source proof exists, this finite tensor can be promoted from
conditional data to selected heavy-link input.
