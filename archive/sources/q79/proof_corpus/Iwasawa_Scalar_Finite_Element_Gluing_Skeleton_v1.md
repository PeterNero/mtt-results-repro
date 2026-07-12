# Iwasawa Scalar Finite-Element Gluing Skeleton

## Purpose

The scalar deck-mode filter gave the analytic boundary conditions. This note
turns the same deck data into a finite-element nodal gluing skeleton on the
candidate standard Iwasawa six-cell.

This is only the scalar finite-element layer. It does not select `Gamma0`, does
not supply bundle transition matrices, does not construct `D_E`, and does not
compute Gram or stiffness matrices.

## Grid

Choose a subdivision parameter:

```text
N >= 1.
```

Use closed-cell nodes:

```text
(x1,x2,y1,y2,t1,t2) in {0,...,N}^6.
```

The half-open representative grid is:

```text
{0,...,N-1}^6.
```

The closed cell has:

```text
(N+1)^6
```

nodes before gluing. The scalar quotient nodal degrees of freedom are:

```text
N^6
```

after imposing the deck boundary identifications below.

## Boundary Identifications

The finite-element constraints are:

```text
x1 face:
(N,x2,y1,y2,t1,t2)
  ~ (0,x2,y1,y2,(t1-y1) mod N,(t2-y2) mod N)

x2 face:
(x1,N,y1,y2,t1,t2)
  ~ (x1,0,y1,y2,(t1+y2) mod N,(t2-y1) mod N)

y1 face:
(x1,x2,N,y2,t1,t2)
  ~ (x1,x2,0,y2,t1,t2)

y2 face:
(x1,x2,y1,N,t1,t2)
  ~ (x1,x2,y1,0,t1,t2)

t1 face:
(x1,x2,y1,y2,N,t2)
  ~ (x1,x2,y1,y2,0,t2)

t2 face:
(x1,x2,y1,y2,t1,N)
  ~ (x1,x2,y1,y2,t1,0).
```

The first two are the nonabelian Iwasawa identifications. They are the reason a
naive six-torus periodic mesh is not valid.

## Constraint Rule

For a scalar nodal vector `u`, impose:

```text
u[source_node] - u[target_node] = 0
```

for every listed boundary identification.

Equivalently:

```text
one scalar nodal degree of freedom per deck-equivalence class.
```

The audit constructs those equivalence classes with a disjoint-set union.

## Sample Counts

The audit checks:

```text
N=1: closed nodes 64,    quotient dofs 1
N=2: closed nodes 729,   quotient dofs 64
N=3: closed nodes 4096,  quotient dofs 729
N=4: closed nodes 15625, quotient dofs 4096
```

Each equivalence class has exactly one representative in the half-open grid
`{0,...,N-1}^6`.

These maps are inverse deck maps: a node on a closed boundary face is mapped
back to its half-open representative.  The analytic scalar equations still use
the forward deck action.

## Relation To The Galerkin Basis

Once a scalar quotient degree count `s_N` is selected, the existing skeleton
still gives:

```text
dim V_N^(0,p) = s_N * 3 * binomial(3,p).
```

For the scalar nodal grid at subdivision `N`:

```text
s_N = N^6
```

before polynomial enrichment or mode truncation.

For bundle-valued sections, scalar equality must be replaced by:

```text
s(source) = rho_E(gamma,source) s(target).
```

That datum is still missing.

## Guardrail

This skeleton uses the inverse Iwasawa deck maps needed to identify closed
boundary nodes with half-open representatives. It does not use naive periodic
six-torus gluing. In particular, the `x1` and `x2` face maps shift the central
coordinates by `(-y1,-y2)` and `(y2,-y1)` respectively.

Do not claim that this constructs selected zero modes. It only constructs the
scalar finite-element boundary constraint layer.

## Verdict

We have moved from:

```text
scalar deck admissibility equations
```

to:

```text
explicit scalar finite-element nodal gluing constraints.
```

The next missing inputs are:

```text
rho_E,
shape functions and quadrature,
selected D_E action,
Gram and stiffness matrices,
Riesz projector and gap/error certificate.
```
