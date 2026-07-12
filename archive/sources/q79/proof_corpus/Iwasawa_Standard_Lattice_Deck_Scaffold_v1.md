# Iwasawa Standard Lattice Deck Scaffold

## Purpose

The Galerkin basis skeleton reduced the basis problem to:

```text
scalar quotient/deck basis plus bundle transition data.
```

The corpus states the Iwasawa quotient as:

```text
X = Gamma \ H_3(C),
```

with the standard left-invariant coframe and:

```text
d omega1 = d omega2 = 0,
d omega3 = omega1 wedge omega2.
```

It does not list explicit `Gamma` deck generators. This note supplies a
standard Gaussian-lattice scaffold compatible with that coframe. It is a
candidate deck scaffold, not yet an MTT-selected basis.

## Candidate Complex Heisenberg Model

Use complex coordinates:

```text
z1,z2,z3 in C.
```

Take the group law:

```text
(z1,z2,z3)*(w1,w2,w3)
  = (z1+w1, z2+w2, z3+w3+z1*w2).
```

Use the left-invariant coframe:

```text
omega1 = dz1,
omega2 = dz2,
omega3 = z1 dz2 - dz3.
```

Then:

```text
d omega1 = 0,
d omega2 = 0,
d omega3 = omega1 wedge omega2.
```

So this sign convention matches the corpus.

## Candidate Gaussian Lattice

Let:

```text
Gamma0 = Z[i]^3
```

with the same group law. For `a,b,c in Z[i]`, left deck action is:

```text
L_(a,b,c)(z1,z2,z3) = (a+z1, b+z2, c+z3+a*z2).
```

The six elementary generators are:

```text
g1: (z1,z2,z3) -> (z1+1, z2,   z3+z2)
g2: (z1,z2,z3) -> (z1+i, z2,   z3+i*z2)
g3: (z1,z2,z3) -> (z1,   z2+1, z3)
g4: (z1,z2,z3) -> (z1,   z2+i, z3)
g5: (z1,z2,z3) -> (z1,   z2,   z3+1)
g6: (z1,z2,z3) -> (z1,   z2,   z3+i)
```

The coframe is invariant under this left action. For example:

```text
omega3' = (z1+a) d(z2+b) - d(z3+c+a*z2)
        = z1 dz2 - dz3
        = omega3.
```

This is why the scaffold is compatible with the Iwasawa structure equation.

## Galerkin Gluing Rules

For scalar functions:

```text
phi(gamma*z) = phi(z)
```

for every `gamma in Gamma0`.

For bundle-valued sections:

```text
s(gamma*z) = rho_E(gamma,z) s(z),
```

where `rho_E` is the selected bundle transition or equivariance datum. This is
still missing.

## Consequence For The Basis

The tensor skeleton already says:

```text
b = phi_m tensor fiber_a tensor baromega_I.
```

This deck scaffold supplies candidate gluing maps for the scalar part. It does
not yet supply:

```text
the selected scalar functions phi_m,
the bundle transition matrices rho_E,
the selected D_E action,
Gram entries,
stiffness entries.
```

It does, however, make the finite-element route concrete:

```text
use a unit real six-cell,
identify boundaries by g1..g6,
impose scalar gluing phi(gamma*z)=phi(z),
impose bundle gluing with rho_E once supplied.
```

The spectral route is also constrained:

```text
ordinary torus Fourier modes are allowed only if they satisfy these nonabelian
deck identifications.
```

## Guardrail

Do not claim this as the selected MTT lattice without a source or selection
argument. Do not use torus Fourier modes as if the quotient were abelian. Do
not construct the family projector until `rho_E`, `D_E`, `G_N`, and `K_N` are
actually supplied.

## Verdict

We have moved from:

```text
need scalar/deck data
```

to:

```text
candidate standard deck scaffold with explicit generators g1..g6.
```

The remaining step is to either confirm/select this `Gamma0` scaffold and
build scalar modes, or instantiate the finite-element route with these gluing
maps plus selected bundle transition matrices.
