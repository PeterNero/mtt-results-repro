# Selected U1 Quotient Projector Pperp and Trace Policy v1

## Result

This closes the final U1 projector gate for the dimensionless U1/SU2
threshold-index pair.  It does not close measured electroweak matching or
`K_gauge`.

```text
selected_U1_index = 2/3
selected_SU2_index = 1/1
selected_U1_SU2_threshold_index_pair_closed = true
measured_electroweak_closure = false
K_gauge_anchor_closed = false
```

## Projector Theorem

```text
SelectedU1SharedCircleQuotientProjectorTheorem
```

On the selected rank-3 U1/qutrit source carrier, the unique shared central-circle universal line is quotiented before the U1 threshold finite trace.  In a carrier basis where this line is spanned by s=(1,1,1)/sqrt(3), the quotient projector is P_perp=I-(1/3)J. It is idempotent, annihilates s, has rank 2, and gives normalized trace Tr(P_perp)/Tr(I)=2/3.

Basis note:

```text
Choosing s=(1,1,1)/sqrt(3) is a representative basis choice for the one-dimensional shared line; the normalized trace and rank are invariant under unitary changes of carrier basis.
```

Representative:

```text
s = (1/sqrt(3), 1/sqrt(3), 1/sqrt(3))
P_perp =
[['2/3', '-1/3', '-1/3'], ['-1/3', '2/3', '-1/3'], ['-1/3', '-1/3', '2/3']]
```

Checks:

```text
idempotent = True
annihilates_shared_vector = True
rank = 2
trace_P_perp = 2/1
trace_identity = 3/1
normalized_trace = 2/3
same_as_source_theorem_weight = True
```

## Trace Policy

```text
U1PhysicalThresholdTraceUsesSharedCircleQuotient
```

The U1 weak-split threshold finite trace is evaluated on the physical carrier quotient V/<s>, equivalently by inserting P_perp on the selected rank-3 carrier before determinant/trace evaluation.

Reason:

```text
The central circle is the unique shared bookkeeping channel, not a sector-specific gauge threshold load; finite coherent projection in gauge sectors must be quotient-compatible; and Theta gauge overlap accounting evaluates internal harmonic norms on the retained physical threshold subspace.
```

Formula:

```text
I_1_selected_index = Tr(P_perp)/Tr(I_3) = 2/3
```

Scope:

```text
dimensionless U1 threshold-index factor in the same internal weak-split accounting scheme; not a measured electroweak prediction or K_gauge anchor
```

## Guardrails

- This closes the U1/SU2 dimensionless threshold-index pair, not measured electroweak closure.
- Do not use this theorem to set K_gauge or a matching scale.
- Do not reuse the flat FP policy outside weak-split gauge-kinetic threshold accounting.
- The selected projector is unique only up to unitary basis change of the same one-dimensional shared line.

## Next Required Object

```text
Selected_K_Gauge_Anchor_or_Full_Electroweak_Matching_v1
```
