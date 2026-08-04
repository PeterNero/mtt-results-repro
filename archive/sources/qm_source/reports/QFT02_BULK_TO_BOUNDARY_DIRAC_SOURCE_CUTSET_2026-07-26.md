# B.QFT.02 Bulk-to-Boundary Dirac Source Cutset

Date: 2026-07-26

## Result

The finite APS crossing is no longer only a matrix witness. The continuum
circle Dirac family

```text
B_a = -i d/dtheta + a
```

based at the q79-compatible sign holonomy has one exact unit-winding path with
spectral flow `+1`. Restriction to modes `(-3,-1,2)` and a gapped flattening
homotopy produces the earlier family `diag(-2,t,3)` exactly without adding or
removing a crossing.

The bulk-to-boundary map is also now explicit. Given a moving cooriented
boundary, collar/adapted-operator convention, restricted physical connection,
endpoint transport and zero-mode taming, the selected q79 bulk Dirac operator
canonically emits:

```text
boundary Clifford bundle
  -> tangential Dirac family
  -> APS projectors
  -> BFV Green form
  -> regular crossing kernels.
```

No arbitrary boundary matrix entries remain after those geometric inputs.

## Exact obstruction

The same sign-holonomy basepoint admits:

```text
constant loop     -> spectral flow 0
unit-winding loop -> spectral flow 1.
```

Their endpoint connection classes are gauge equivalent. Therefore the finite
q79 sign line and selected bulk coframe do not select the physical boundary
history. `A_causal` may orient a supplied history, but it does not supply the
history or identify the compact shared circle with physical time.

## Frontier delta

Before:

```text
selected physical noncollar boundary family
  = unspecified operator source.
```

After:

```text
selected physical noncollar boundary family
  = one typed boundary source package;

all Dirac/APS/BFV operator data
  = functorial outputs of that package.
```

Closed:

- conditional bulk-to-boundary Dirac/APS/BFV functor;
- exact continuum origin of the finite crossing witness;
- exact no-go for selection from bulk geometry plus endpoint sign alone.

Open:

- selection of the physical moving boundary and connection history;
- the resulting physical crossing-kernel line;
- its unitary parallel map to the q79 shared line;
- Dai--Freed determinant transgression;
- eta/Maslov/BFV/counterterm normalization.

## Objective assessment

This is a real narrowing of `B.QFT.02`, not physical phase closure. It removes
the possibility that arbitrary finite matrix entries are the missing source
and identifies the minimum geometric source package. It also proves that the
already selected q79 sign cannot, by itself, be promoted to the missing
history-dependent anomaly phase.

No physical parameter, fit or observed value was added.
