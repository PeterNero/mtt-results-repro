# Iwasawa Finite-Mesh `rho_E` Validator

## Purpose

The constant-generator `rho_E` validator checks the special case in which each
deck generator has one global `3x3` matrix.  The finite-element gluing contract
allows more general data:

```text
rho_E(g_j,z)
```

evaluated at the boundary target nodes of the closed Iwasawa six-cell.

This note adds the next executable gate: a finite-mesh validator for supplied
boundary-target transition tables.  It does not construct the selected bundle.
It only defines what a candidate table must pass before it can be used in the
bundle-valued finite-element space.

## Input Format

A candidate file must declare:

```text
rank = 3,
mesh_N >= 1,
generator_data for g1,g2,g3,g4,g5,g6.
```

Each generator entry may be constant:

```json
{
  "matrix": [[1,0,0],[0,1,0],[0,0,1]]
}
```

or table-valued:

```json
{
  "values": {
    "0,0,0,0,0,0": {
      "matrix": [[1,0,0],[0,1,0],[0,0,1]]
    }
  }
}
```

A generator may also supply a constant `matrix` plus `values` overrides.  In
that case, a listed boundary-target value overrides the constant fallback.
Complex entries are represented either as real numbers or as:

```text
[real, imag].
```

## Face Reductions

The validator uses exactly the scalar finite-element face reductions already
recorded in the gluing skeleton.  For a closed-cell node

```text
(x1,x2,y1,y2,t1,t2) in {0,...,N}^6,
```

the boundary reductions are:

```text
x1=N:
(N,x2,y1,y2,t1,t2)
  -> (0,x2,y1,y2,(t1-y1) mod N,(t2-y2) mod N)

x2=N:
(x1,N,y1,y2,t1,t2)
  -> (x1,0,y1,y2,(t1+y2) mod N,(t2-y1) mod N)

y1=N:
(x1,x2,N,y2,t1,t2)
  -> (x1,x2,0,y2,t1,t2)

y2=N:
(x1,x2,y1,N,t1,t2)
  -> (x1,x2,y1,0,t1,t2)

t1=N:
(x1,x2,y1,y2,N,t2)
  -> (x1,x2,y1,y2,0,t2)

t2=N:
(x1,x2,y1,y2,t1,N)
  -> (x1,x2,y1,y2,t1,0).
```

If a node lies on more than one boundary face, it can be reduced to its
half-open representative in several orders.  The finite-mesh validator checks
that all such orders give the same target node and the same ordered product of
transition matrices.

## Absorbed Word Convention

The validator is a face-transition-table check.  It assumes that any central
wrap, deck-word convention, or coordinate-dependent lifting choice has already
been absorbed into the supplied value of:

```text
rho_E(g_j,target).
```

Therefore the gate is:

```text
For the supplied finite face values, all corner reduction products agree.
```

It is not a symbolic proof of the full cocycle on every point of the manifold.
A future selected symbolic `rho_E` can feed this validator by evaluating its
face values on one or more meshes.

## Implemented Checks

The script:

```text
scripts/validate_iwasawa_rhoE_mesh.py
```

checks:

```text
rank=3 declaration,
mesh_N positive integer,
all six generator entries present,
3x3 complex matrix shape,
matrix lookup at every visited boundary target,
nonzero determinant at every visited boundary target,
finite corner path-independence.
```

The script returns:

```text
0: complete finite-mesh candidate passes,
1: complete finite-mesh candidate fails,
2: candidate is incomplete/open.
```

## Smoke Tests

The audit runs three smoke tests.

First, the open template:

```text
certificates/iwasawa_bundle_rhoE_data.template.json
```

is refused with exit code `2`.

Second, the identity transition system on `mesh_N=2` passes.  This is only a
schema smoke test:

```text
rho_E(g_j,z)=I_3
```

is not selected bundle data.

Third, a coordinate override is inserted so that the `g1` value at one
boundary target differs from the `g1` value at the corresponding alternative
corner reduction path.  The validator rejects this candidate with a finite
corner product mismatch.

## What This Closes

This closes:

```text
finite mesh rho_E table validator,
corner path-independence test for supplied face values,
coordinate-table extension beyond the constant rho_E validator.
```

It does not close:

```text
actual selected rho_E values or functions,
proof that rho_E comes from the selected MTT bundle E,
symbolic/all-mesh cocycle for nontrivial data,
Hermitian metric compatibility,
sector projection maps Q,u,d,L,e,N,H,
selected D_E action,
Gram and stiffness matrices.
```

## Guardrail

Do not use the identity transition table as the selected bundle.

Do not choose a table to force CKM entries, Yukawa magnitudes, masses, or any
benchmark matrix.

Do not treat a successful finite-mesh table check as a proof of full SM
closure.  It is one input gate in the finite-element route.

## Verdict

The project now has two `rho_E` validators:

```text
constant generator matrix validator,
finite-mesh boundary-target table validator.
```

The next selected-data step is to fill a candidate `rho_E` from typed monad,
Cech, HYM, or selected spectral data; run the relevant validator; then add the
Hermitian metric and sector-projection checks before assembling the selected
`D_E`, Gram matrix, and stiffness matrix.
