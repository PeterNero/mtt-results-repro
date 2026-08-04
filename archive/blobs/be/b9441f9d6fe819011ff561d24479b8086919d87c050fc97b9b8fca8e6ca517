# Iwasawa Scalar Deck Mode Filter

## Purpose

The standard lattice deck scaffold supplied candidate generators `g1..g6`.
This note extracts the scalar admissibility equations those generators impose.
It does not select the MTT lattice, does not build the selected scalar basis,
and does not supply bundle transitions.

The point is narrower:

```text
before a scalar function can enter the Galerkin basis, it must pass the
candidate Iwasawa deck filter.
```

## Real Coordinates

Write:

```text
z1 = x1 + i*x2,
z2 = y1 + i*y2,
z3 = t1 + i*t2.
```

The unit real six-cell is:

```text
0 <= x1,x2,y1,y2,t1,t2 < 1,
```

with boundary identifications induced by the deck generators.

## Scalar Gluing Equations

For a scalar mode `phi`, deck invariance gives:

```text
g1: phi(x1+1,x2,y1,y2,t1+y1,t2+y2)
      = phi(x1,x2,y1,y2,t1,t2)

g2: phi(x1,x2+1,y1,y2,t1-y2,t2+y1)
      = phi(x1,x2,y1,y2,t1,t2)

g3: phi(x1,x2,y1+1,y2,t1,t2)
      = phi(x1,x2,y1,y2,t1,t2)

g4: phi(x1,x2,y1,y2+1,t1,t2)
      = phi(x1,x2,y1,y2,t1,t2)

g5: phi(x1,x2,y1,y2,t1+1,t2)
      = phi(x1,x2,y1,y2,t1,t2)

g6: phi(x1,x2,y1,y2,t1,t2+1)
      = phi(x1,x2,y1,y2,t1,t2).
```

These six equations are the first scalar basis filter.

## Central Character Decomposition

The central translations `g5,g6` allow an integer central character split:

```text
k = (k1,k2) in Z^2,
phi = exp(2*pi*i*(k1*t1+k2*t2))*F_k(x1,x2,y1,y2).
```

The `g1` equation has central shift:

```text
(t1,t2) -> (t1+y1,t2+y2).
```

Therefore:

```text
F_k(x1+1,x2,y1,y2)
  = exp(2*pi*i*(-k1*y1-k2*y2))*F_k(x1,x2,y1,y2).
```

The `g2` equation has central shift:

```text
(t1,t2) -> (t1-y2,t2+y1).
```

Therefore:

```text
F_k(x1,x2+1,y1,y2)
  = exp(2*pi*i*(k1*y2-k2*y1))*F_k(x1,x2,y1,y2).
```

The `g3,g4` equations give:

```text
F_k(x1,x2,y1+1,y2) = F_k(x1,x2,y1,y2),
F_k(x1,x2,y1,y2+1) = F_k(x1,x2,y1,y2).
```

## Consequence

For the central-zero sector:

```text
k = (0,0),
```

all twist multipliers are one. Ordinary Fourier modes on the four-torus
`(x1,x2,y1,y2)` are admissible in this sector.

For every nonzero central character:

```text
k != (0,0),
```

ordinary four-torus Fourier modes are not admissible as scalar modes by
themselves. The `x1` and `x2` shifts carry `y`-dependent phase multipliers.
The basis must instead use theta/magnetic modes satisfying the twisted
conditions, or a finite-element basis with the same boundary constraints.

## Galerkin Implication

The scalar part of:

```text
b = phi_m tensor fiber_a tensor baromega_I
```

must be chosen from modes passing the above filter.

For the spectral route:

```text
choose central labels k,
build F_k,n satisfying the twisted base conditions,
set phi_k,n = exp(2*pi*i*(k1*t1+k2*t2))*F_k,n.
```

For the finite-element route:

```text
build functions on the unit six-cell,
identify boundaries by g1..g6,
or, after central decomposition, impose the twisted four-dimensional
boundary conditions for each k.
```

For bundle-valued sections this is only the scalar half. The full basis still
requires:

```text
s(gamma*z)=rho_E(gamma,z)s(z).
```

## Guardrail

Do not use ordinary torus Fourier modes in nonzero central sectors. They are
valid only in the central-zero sector unless they are upgraded into functions
satisfying the twisted deck conditions.

Do not claim that this constructs the selected MTT scalar basis. It only
constructs the admissibility filter that any such basis must pass.

## Verdict

We have moved from:

```text
candidate deck generators g1..g6
```

to:

```text
explicit scalar mode filter and central-character/twisted-boundary split.
```

The next step is to choose or compute an actual finite scalar basis satisfying
this filter, then combine it with `rho_E` and the selected `D_E`.

