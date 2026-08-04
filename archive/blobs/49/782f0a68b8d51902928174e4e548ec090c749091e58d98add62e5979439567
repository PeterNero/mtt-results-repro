# Route-C WeylPair Aselected Assembly Import v1

## Result

The conditional Weyl-pair operator is assembled:

```text
A_weylpair_conditional = [phase_packet, shift_packet]
shape = [72, 2]
rank = 2
condition number = 1
deltaTheta_conditional = [1.0, 1.0000000000000002]
relative residual = 1.570e-16
```

This closes the algebraic assembly obstruction for the enriched Weyl-pair
packet. If the selected source emits these two columns, the locked splitter
equation is solved exactly up to numerical roundoff.

## Boundary

This does not promote `A_weylpair_conditional` to `A_selected`. The current
selected emission flags remain:

```text
A_selected_currently_emitted = False
b_selected_currently_emitted = False
```

The remaining blocker is:

```text
SelectedWeylPairSourceProvenanceLemma
```

It must prove that the selected `q79/F,m=1` `S3`/Green-Schwarz Route-C source
emits the phase-like `I+Z` basis-holonomy packet and the shift-like `I+X`
active-vertex packet in the same `B_N`/projector/dotD/zero-mode basis, with
internal normalization.
