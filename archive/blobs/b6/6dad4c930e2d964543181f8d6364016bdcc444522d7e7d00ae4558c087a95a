# Iwasawa `rho_E` Hermitian Metric Validator

## Purpose

The finite-mesh `rho_E` validator checks that a supplied transition table is
invertible and path-independent on the Iwasawa finite-element cell.  That is
not enough to build normalized zero modes.  The bundle-valued Galerkin route
also needs a Hermitian metric convention compatible with the same transitions.

This note adds the next executable gate:

```text
rho_E(gamma,z)^* H(gamma*z) rho_E(gamma,z) = H(z).
```

It is a validator for candidate data, not a construction of the selected
metric.

## Convention

The section convention remains:

```text
s(gamma*z) = rho_E(gamma,z) s(z).
```

If a boundary node is:

```text
source = gamma * target,
```

then a fiber vector at `target` is transported to `source` by:

```text
v_source = rho_E(gamma,target) v_target.
```

Metric compatibility is therefore:

```text
h(source)(rho_E v, rho_E w) = h(target)(v,w),
```

or in matrices:

```text
rho_E(gamma,target)^* H(source) rho_E(gamma,target) = H(target).
```

The validator applies this equation on every boundary face of the finite mesh.

## Input Format

A candidate file must include:

```text
rank = 3,
mesh_N >= 1,
generator_data for g1,...,g6,
metric_data.
```

The `generator_data` format is the same constant or table-valued format used by
the finite-mesh `rho_E` validator.

The metric may be constant:

```json
{
  "metric_data": {
    "matrix": [[1,0,0],[0,1,0],[0,0,1]]
  }
}
```

or node-table-valued:

```json
{
  "metric_data": {
    "values": {
      "0,0,0,0,0,0": {
        "matrix": [[1,0,0],[0,1,0],[0,0,1]]
      }
    }
  }
}
```

A constant metric may also be supplied with node overrides.  Complex entries
are represented as real numbers or as:

```text
[real, imag].
```

## Implemented Checks

The script:

```text
scripts/validate_iwasawa_rhoE_metric.py
```

checks:

```text
rank=3 declaration,
mesh_N positive integer,
all six generator entries present,
metric_data present,
3x3 complex matrix shape,
Hermitian metric on every visited node,
positive definiteness on every visited node,
boundary-face metric compatibility.
```

The script returns:

```text
0: complete finite-mesh rho_E plus metric candidate passes,
1: complete candidate fails,
2: candidate is incomplete/open.
```

## Smoke Tests

The audit runs four tests.

First, the open template is refused with exit code `2`.

Second, identity transition data with the identity metric on `mesh_N=2` pass.
This is only a schema smoke test, not selected metric data.

Third, a scaled transition:

```text
rho_E(g1,z)=diag(2,1,1)
```

with identity metric fails, as it should, because:

```text
rho_E^* I rho_E != I.
```

Fourth, a candidate with transition data but no `metric_data` is treated as
incomplete/open, not as a mathematical failure.

## What This Closes

This closes:

```text
finite-mesh Hermitian metric compatibility validator,
positive-definite Hermitian metric gate,
unitary-transition gate for a supplied metric convention.
```

It does not close:

```text
actual selected rho_E values or functions,
proof that rho_E comes from the selected MTT bundle E,
actual selected Hermitian/HYM metric,
proof the metric solves the HYM or selected Strominger system,
sector projection maps Q,u,d,L,e,N,H,
selected D_E action,
Gram and stiffness matrices.
```

## Guardrail

Do not identify the identity metric with the selected HYM metric unless that is
derived from the selected bundle and Strominger/HYM equations.

Do not choose a metric to tune masses, CKM angles, or benchmark matrices.

Do not treat metric compatibility as full SM closure.  It is a necessary input
gate for normalized finite-basis computations.

## Verdict

The `rho_E` executable stack now checks:

```text
constant generator algebra,
finite-mesh corner path-independence,
Hermitian metric compatibility.
```

The next selected-data step is to supply a genuine selected `rho_E` plus
Hermitian metric candidate, then validate sector projection maps before
constructing the selected `D_E`, Gram matrix, and stiffness matrix.
