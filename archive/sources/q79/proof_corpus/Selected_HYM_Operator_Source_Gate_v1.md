---
title: |
  Selected HYM Operator Source Gate
author: MTT proof reproduction program
---

# Target

The two-path exploration identified the first hybrid blocker:

```text
selected HYM/Strominger operator/source packet for D_E.
```

This note turns that blocker into an executable gate.

# Gate

The gate requires more than the closed Fu-Yau/Mukai charge sector.  A closing
packet must prove:

```text
selected MTT source, not a fixture,
closed Fu-Yau/Strominger background,
selected visible SM bundle/operator source,
retarded q79/F branch with antiunitary conjugate retained,
Route C residual validator passing honestly,
selected-source promotion passing at de_response level,
selected same-branch D_E, dotD, Riesz/Green, and projector retention.
```

The validator is:

```text
scripts/validate_selected_hym_operator_source.py
```

The open template is:

```text
certificates/selected_hym_operator_source.template.json
```

# First Fill Attempt

The strongest current input is:

```text
closed Z7 Fu-Yau/Strominger charge sector,
current q79/F Route C branch-smoke finite files.
```

The attempt writes:

```text
certificates/selected_hym_operator_source.attempt.json
certificates/selected_hym_operator_source_promotion.attempt.json
candidate_data/selected_hym_operator_source_attempt.candidate.json
```

# Result

The attempt fails for the precise expected reason:

```text
the Fu-Yau/Strominger sector is closed as a charge sector,
but it is still charge-sector-only;
no selected visible SM bundle/operator source is constructed;
Route C residual validation fails selected_source_verified;
D_E/Riesz/Green/dotD validators fail selected-source flags;
selected-source promotion fails at de_response level.
```

This is not a regression.  It closes a possible ambiguity: the terminal q79
charge-sector closure is not secretly enough to produce the selected matter
operator.  We need one more object.

# New Sharp Target

The next object must be:

```text
a selected visible SM bundle/operator source whose Route C residual, D_E,
Riesz/Green, and dotD validators pass honestly.
```

Once that exists, it can feed the spectral Galerkin path to compute:

```text
zero modes,
L2 metrics,
projectors,
U_10 and U_bar5,
matter-slot transport.
```

# Guardrail

This gate does not claim selected `D_E`, ordered SU(5) packet selection, or full
SM closure.  It records exactly why Path A remains open and what must be
supplied next.
