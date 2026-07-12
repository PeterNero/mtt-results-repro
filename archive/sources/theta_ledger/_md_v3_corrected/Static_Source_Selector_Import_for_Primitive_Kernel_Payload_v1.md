# Static Source Selector Import for Primitive Kernel Payload v1

## Result

The sibling SM-parity repo has advanced beyond the earlier workorder in one
important way:

```text
static source selector       closed
static sector routing        closed
static overlap normalization closed
active shift (1,1)           closed
fixed-fiber quotient class   closed for current observables
```

This imports:

```text
SelectedPrimitiveVertexSourceOrBasisTransportSelectionTheorem
SelectedSMSlotFunctorOverlapKernelAndConsistencyTheorem
PrimitiveC1OrWeylPairSectorRoutingSourceEmissionReductionTheorem
```

## What This Closes

The following old blockers are no longer the active wall:

```text
source-level Z/X carrier
Z/clock -> u,e routing
X/shift -> d,nuD routing
static trace-transfer normalization
active deck shift (1,1)
fixed fiber quotient for current observables
alpha1/dotD driver at source-selector level
```

## What It Does Not Close

The same artifacts explicitly do not emit:

```text
primitive overlap contraction values
dynamic source-to-C1 transfer tensor
selected A_selected
selected b_selected
selected Hessian blocks
selected sector response matrices
honest Galerkin C1 values
```

For the right-label payload this means:

```text
u_phase row source selector     available
d_phase row source selector     available
u_phase row value/provenance    still open
d_phase row value/provenance    still open
```

## Consequence

The next payload attempt should no longer describe routing and static
normalization as missing.  It should fail only because the dynamic row operators
remain value-open/source-open.

This changes the active theorem target from:

```text
find the source route
```

to:

```text
emit selected dynamic primitive row values on the already selected source route
```

## Updated Target

```text
SelectedPrimitiveKernelDynamicValueEmissionTheorem
```

or equivalently:

```text
SelectedDynamicOverlapTensorHessianNormalization
HonestSelectedGalerkinC1ValueFill
SelectedPrimitiveOverlapContractionsValueEmission
```

The current routed row names are:

```text
u_phase = Z/clock row routed to u
d_shift = X/shift row routed to d
```

Once a physical-source theorem emits these row operators pre-residual,
`MTTSelectedPrimitiveKernelSourcePayload.v1` can validate.  The formal Route-B
finite trace execution now computes the same right-label value support, but it
still needs promotion from formal quadrature to selected physical source.
