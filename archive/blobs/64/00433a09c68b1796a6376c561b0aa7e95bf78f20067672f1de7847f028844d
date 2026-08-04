# Formal Route-B Right-Label Value Import v1

## Result

The newer SM-parity Route-B finite Weyl trace execution computes the routed
primitive rows needed by the right-channel label packet:

```text
u label row source leg  = u:phase = Z/clock
d label row source leg  = d:shift = X/shift
```

This corrects the older legacy diagnostic wording that used `d_phase`.

## Imported Source

```text
C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\candidate_data\selected_routeaemission_or_routebgalerkinrows_execution\formal_110_row_execution.packet.json
```

The packet emits:

```text
primitive rows       72
sector matrix rows   36
hessian/source rows   2
total rows          110
```

The rows are exact finite trace quadrature rows and reproduce the previous
algebraic replay with error below `5e-16`.

## Right-Label Trace Test

Projecting the Hermitianized formal rows against the selected weighted
right-channel projectors gives:

```text
u:phase spectrum = (-0.366025403784, +1.000000000000, +1.366025403784)
u:phase traces   = (0.670132940229, 1.273461339109, 0.056405720662)

d:shift spectrum = (0.000000000000, +0.500000000000, +0.500000000000)
d:shift traces   = (0.226294874209, 0.361687937551, 0.412017188240)
```

The unique affine normalizations on the first two right channels are:

```text
up spin:    scale=+3.314944238847, offset=-3.221453329473
down dyad:  scale=-7.385902758343, offset=+2.671391935618
down nil:   scale=+7.385902758343, offset=-1.671391935618
```

with residuals below `1.5e-15`.

## What This Closes

This closes the value-search part of the support calculation:

```text
formal u:phase row values       computed
formal d:shift row values       computed
formal affine trace labels      computed
observed masses/CKM used        false
target fitting used             false
```

## What This Does Not Close

The same source packet explicitly has:

```text
physical_source_promoted=false
```

Therefore this is still not a full selected MTT proof of the right labels.

The remaining theorem is now sharper:

```text
SelectedFiniteTraceQuadratureEqualsPhysicalPhiFinC1ActionTheorem
```

or equivalently:

```text
SelectedGalerkinReplacementAcceptsFiniteWeylTraceRows
```

If that theorem is proved, the formal Route-B rows can be promoted into
`MTTSelectedPrimitiveKernelSourcePayload.v1`.

