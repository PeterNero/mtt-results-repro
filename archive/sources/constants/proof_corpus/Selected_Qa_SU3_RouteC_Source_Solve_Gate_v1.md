# Selected Qa/SU3 Route C Source Solve Gate

## Claim

The selected Qa/SU3 spectral fallback has now been reduced to a first genuinely
new source object:

```text
Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1
```

current q79 evidence exhausts the presently available source routes:

```text
R1 corrected non-invariant Dolbeault operator: BLOCKED
R2 typed monad sections: BLOCKED
R3 direct selected HYM solve: ABSTRACT_EXISTENCE_ONLY
twisted/S3 packet: PARTIAL_PROMOTION_OPEN
```

So the current blocker cannot be closed by recombining existing certificates.
The finite validator pipeline is ready, and the promotion gate is ready, but no
current artifact justifies the selected-source flags.

## What Is Closed

The following are now certified:

```text
current route exhaustion proved
promotion contract ready
typed monad route absent from current corpus
closed charge/Strominger sector is not enough for operator source
twisted/S3 progress is partial but not a selected D_E/dotD source
finite validator pipeline ready from the previous gate
first new object identified
```

This is a useful hardening of the proof program.  It prevents the common false
move of promoting:

```text
abstract HYM existence,
route-c smoke residuals,
typed monad labels without sections,
or S3/twisted class closure
```

into the actual selected operator source.

## Minimal New Data

The next object must supply:

```text
selected visible SM bundle or sheaf model on the q79/F branch
finite rho_E transition data from that selected bundle
selected HYM/Strominger residual packet with selected_source_verified true
sector D_E action matrices for Q,u,d,L,e,N,H
Riesz projector, complement gap, reduced Green, and truncation data
same-branch dotD_alpha1 and horizontal responses
projector retention for qutrit matter-slot polarizations
```

Once supplied, it must pass:

```text
validate_iwasawa_route_c_residuals.py
validate_iwasawa_de_action.py
validate_iwasawa_riesz_gap.py
validate_iwasawa_reduced_green.py
validate_iwasawa_dotd_response.py
validate_selected_hym_operator_source.py
```

## Guardrail

This gate does not construct `D_E`, the Route C residual solve, the selected
visible bundle, primitive C1 contractions, or full SM closure.  It proves that
the next proof step is a new selected visible SM bundle/operator source, not a
different arrangement of already closed certificates.

In short: this is not a different arrangement of already closed certificates.
