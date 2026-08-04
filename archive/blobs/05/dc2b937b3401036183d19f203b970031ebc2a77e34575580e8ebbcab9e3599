# Iwasawa Bundle Finite-Element Gluing Contract

## Purpose

The scalar finite-element gluing skeleton constructs quotient nodal degrees of
freedom on the candidate standard Iwasawa six-cell.  The selected Galerkin
space is not scalar, however.  It must use rank-three bundle-valued sections.

This note records the exact `rho_E` transition data required to lift scalar
gluing to bundle gluing.  It is an input contract, not a construction of the
selected bundle.

## Section Convention

Use:

```text
s(gamma*z) = rho_E(gamma,z) s(z),
```

where:

```text
rho_E(gamma,z) is a 3x3 complex invertible matrix.
```

The cocycle law is:

```text
rho_E(gamma*delta,z)
  = rho_E(gamma,delta*z) rho_E(delta,z).
```

Also:

```text
rho_E(e,z) = I_3,
rho_E(gamma^-1,gamma*z) = rho_E(gamma,z)^-1.
```

## Boundary Constraint

The finite-element boundary maps use inverse deck maps to send a closed-cell
boundary node back to its half-open representative.

If:

```text
source_node = gamma * target_node
```

under the forward deck action, then the rank-three nodal vector must satisfy:

```text
u[source_node] - rho_E(gamma,target_node) u[target_node] = 0.
```

This replaces the scalar condition:

```text
u[source_node] - u[target_node] = 0.
```

If `rho_E=I_3`, this is exactly three copies of the scalar gluing rule.  That
identity case is useful as a schema smoke test, not as selected bundle data.

## Generator Face Slots

The required face transition slots are:

```text
x1 face:
target = (0,x2,y1,y2,(t1-y1) mod N,(t2-y2) mod N)
u[N,x2,y1,y2,t1,t2] = rho_E(g1,target) u[target]

x2 face:
target = (x1,0,y1,y2,(t1+y2) mod N,(t2-y1) mod N)
u[x1,N,y1,y2,t1,t2] = rho_E(g2,target) u[target]

y1 face:
target = (x1,x2,0,y2,t1,t2)
u[x1,x2,N,y2,t1,t2] = rho_E(g3,target) u[target]

y2 face:
target = (x1,x2,y1,0,t1,t2)
u[x1,x2,y1,N,t1,t2] = rho_E(g4,target) u[target]

t1 face:
target = (x1,x2,y1,y2,0,t2)
u[x1,x2,y1,y2,N,t2] = rho_E(g5,target) u[target]

t2 face:
target = (x1,x2,y1,y2,t1,0)
u[x1,x2,y1,y2,t1,N] = rho_E(g6,target) u[target].
```

## Cocycle Checks

Closed-cell corners can often be reduced by more than one deck-word path.  For
example, a node on both the `x1=N` and `y1=N` faces can be reduced by the
`g1` path followed by the `g3` path, or by the `g3` path followed by the `g1`
path with the correct shifted target.

The two ordered products of `rho_E` matrices must agree.  This is the finite
mesh version of:

```text
rho_E(gamma*delta,z)
  = rho_E(gamma,delta*z) rho_E(delta,z).
```

Without this path-independence check, the same corner nodal value can receive
contradictory bundle constraints.

## Required Data

A completed `rho_E` certificate must supply:

```text
rho_E(g_j,z) for j=1..6 at all boundary targets,
or an evaluable symbolic/numeric rule for those matrices;

an invertibility certificate;

a cocycle/path-independence certificate on all mesh corner overlaps;

Hermitian metric compatibility or a controlled non-unitary convention;

sector projection maps for Q,u,d,L,e,N,H.
```

The future fill-in slot is:

```text
certificates/iwasawa_bundle_rhoE_data.template.json.
```

## Trivial Schema Smoke Test

The audit checks the identity transition system:

```text
rho_E(g_j,z)=I_3.
```

Then the bundle quotient degrees of freedom are:

```text
N=1: 3
N=2: 192
N=3: 2187
N=4: 12288.
```

These are simply:

```text
3*N^6.
```

Again: this is not a selected bundle. It only verifies that the rank-three
constraint schema reduces correctly to the scalar gluing skeleton.

## Guardrail

Do not set `rho_E=I_3` just because it makes the calculation easy.  The
transition data must come from the selected bundle or selected operator source.

Do not choose `rho_E` from desired masses, CKM angles, or benchmark matrices.
It must be fixed before any comparison with observed SM data.

## Verdict

We have moved from:

```text
scalar finite-element deck gluing
```

to:

```text
rank-three bundle gluing input contract.
```

The next step is to fill `rho_E`, prove its cocycle and metric compatibility,
and then assemble the selected `D_E`, Gram matrix, and stiffness matrix.

