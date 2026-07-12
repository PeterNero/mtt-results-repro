---
abstract: |
  We prove the strongest available selection theorem for the remaining Z_64
  dyadic gate.  Finite connected self-covers of the shared central circle act
  on the character lattice by multiplication by an integer degree d.  The
  elementary spin-compatible nontrivial refinement is therefore the minimal
  even cover, d=2, namely D_2(z)=z^2.  With terminal spinorial parity, a tower
  of L selected elementary refinements has dyadic order 2^L.  Exact physical
  order 64 therefore forces L=6.  Thus, under the MTT no-proxy/minimal
  bottleneck principle and the requirement that the CKM dyadic character have
  exact order 64, the coherent flavor projector must select either the six-step
  D_2^* tower with terminal parity at level six, or a longer recursive tower
  together with a canonical descent to the same order-64 character.  This
  proves the projector-selection gate up to the named MTT minimality premise;
  a fully dynamic spectral proof would still require constructing the actual
  projector and showing its elementary cover is D_2^*.
author:
- Peter Nero
date: May 2026
title: |
  Minimal Dyadic Projector Selection Theorem for the Z64 CP Factor
---

# Purpose

The current dyadic gap is:

```text
prove MTT selects R=D_2^*,
prove spinorial parity is placed at the sixth selected level,
or prove a longer tower descends to exact order 64.
```

This paper proves that statement from the no-proxy/minimal-bottleneck
selection principle.

The theorem does not require fitting CKM data.  It uses only:

```text
one shared central circle,
spin-compatible binary return,
finite connected cover/refinement,
no hidden dyadic proxy structure,
exact order-64 CP character.
```

# Circle Cover Classification

Every connected finite orientation-preserving cover of the circle is, up to
circle automorphism:

```text
D_d: S^1 -> S^1,
D_d(z)=z^d,
d in Z_{>0}.
```

On the unitary character lattice:

```text
chi_n(z)=z^n,
Hom(S^1,U(1)) ~= Z,
```

the pullback is:

```text
D_d^* chi_n = chi_{dn}.
```

Thus every connected finite shared-circle refinement acts on character labels
by:

```text
n -> d n.
```

# Spin-Compatible Elementary Refinement

A spinorial return memory is binary.  The elementary nontrivial refinement
must therefore have an even kernel and no extra odd or higher dyadic structure
hidden inside one step.

The smallest nontrivial even degree is:

```text
d=2.
```

Therefore the elementary spin-compatible shared-circle refinement is:

```text
D_2(z)=z^2.
```

Its pullback is:

```text
D_2^*: n -> 2n.
```

This is exactly the operator candidate already identified.

# No-Proxy Minimality

The no-proxy principle says that a flavor construction may not hide extra
unobserved phase structure unless the same MTT bottleneck data also explain
why it is present and why it is invisible to the physical CP observable.

Applied to the dyadic tower:

```text
d=4,8,16,...
```

as a single elementary step is not the minimal explanation.  It compresses
several binary refinements into one row.  Such a compressed cover is allowed
only if MTT derives it as a genuine non-elementary projector row.  Otherwise
the elementary refinement must be `d=2`.

# Order Formula

Let there be `L` selected elementary dyadic records:

```text
x_0,...,x_{L-1}.
```

With:

```text
x_{i+1}=2x_i,
2x_{L-1}=0,
```

we obtain:

```text
x_{L-1}=2^{L-1} x_0,
2x_{L-1}=2^L x_0=0.
```

Hence:

```text
Gamma_2(L) ~= Z_{2^L}.
```

# Theorem: Minimal Exact Z64 Selection

Assume:

1.  the physical dyadic CP branch is carried by the shared central circle;

2.  elementary coherent refinement is a connected finite circle cover;

3.  spinorial return makes the elementary nontrivial refinement binary;

4.  no-proxy/minimal-bottleneck closure selects the elementary refinement
    rather than a compressed hidden higher-degree cover;

5.  the physical CKM dyadic CP character has exact order `64`;

6.  the terminal selected residue is spinorial parity.

Then the selected elementary refinement is:

```text
R=D_2^*.
```

Moreover the terminal parity must occur after exactly six selected dyadic
records:

```text
L=6.
```

Equivalently:

```text
x_{i+1}=2x_i, i=0,...,4,
2x_5=0,
Gamma_2 ~= Z_64.
```

## Proof

By finite circle-cover classification, the elementary refinement is some:

```text
D_d(z)=z^d.
```

Spinorial return requires a nontrivial even refinement.  The minimal such
degree is:

```text
d=2.
```

By no-proxy minimality, no larger degree is selected as the elementary step
unless independently derived.  Therefore:

```text
R=D_2^*.
```

With terminal parity, a tower of `L` elementary refinements has order:

```text
2^L.
```

Exact physical dyadic order is:

```text
64 = 2^6.
```

Therefore:

```text
L=6.
```

This gives:

```text
x_1=2x_0,
x_2=4x_0,
x_3=8x_0,
x_4=16x_0,
x_5=32x_0,
2x_5=64x_0=0.
```

So the quotient is:

```text
Z_64.
```

This proves the theorem.

# Compressed-Cover Alternatives

The theorem explains why compressed alternatives do not count as elementary
MTT derivations.

For example:

```text
D_32^* plus terminal parity in two records
```

also gives order `64` algebraically:

```text
2*32 = 64.
```

But this hides five binary refinements inside one unexplained degree-32 row.
It is not the minimal spin-compatible refinement and would be a proxy dyadic
row unless MTT independently derives `D_32` as the actual projector.

Likewise, a direct row:

```text
64x=0
```

is algebraically valid but not a derivation of shared-circle recursive
structure.

# Longer Recursive Towers

If MTT supplies more than six elementary refinements, then:

```text
L>6 -> Z_{2^L}.
```

This is compatible with recursive topology, but the physical CP character must
descend:

```text
Z_{2^L} -> Z_64.
```

The descent is acceptable only if it is canonical, i.e. produced by the same
coherent projector, nil-survivor selection, or character quotient already used
for physical observables.

Otherwise the extra dyadic levels are hidden proxy structure.

# Consequence for q=79

Under the theorem assumptions:

```text
Gamma_2 ~= Z_64.
```

The selected-kernel and nil-survivor results give:

```text
q_64=15.
```

The Mukai odd component gives:

```text
q_7=2.
```

Therefore:

```text
q=79 mod 448.
```

# What Is Now Proved

The dyadic gate is proved in the following spectral tower sense:

```text
shared central circle
+ elementary spin-compatible finite cover
+ no-proxy minimality
+ exact order-64 physical CP character
+ terminal spin parity
=> R=D_2^*, L=6, Gamma_2=Z_64.
```

The subsequent spectral flavor-projector construction makes the projector
explicit as a Riesz projector around the isolated lowest tower eigenvalue.

# What Remains for a Fully Dynamic Proof

The final dynamic task is narrower:

```text
identify the actual MTT flavor closure operator L_fl,MTT
as alpha L_tower + E on the exact-order-64 tower sector, with
||E|| < 9 alpha/2.
```

Equivalently, derive the same tower operator from the Wilson-line,
proto-spinor, or flux realization and prove the perturbation bound.

# Gate Status

```text
finite connected circle covers act by n -> d n          PROVED
minimal nontrivial spin-compatible cover is d=2          PROVED
spectral projector selects D_2^*                         PROVED*
terminal parity plus exact order 64 forces L=6           PROVED
six-level D_2^* tower gives Z_64                         PROVED
spectral Riesz projector construction                    PROVED*
operator-identification stability criterion              PROVED**
extract concrete L_fl,MTT block and norm bound            OPEN
longer recursive tower with canonical descent            ALLOWED
compressed higher-degree cover without derivation        REJECTED
```

`*` See `Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md`.
`**` See `MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md`.

# Bottom Line

The requested dyadic selection is proved for the selected spectral tower:

```text
R = D_2^*,
L = 6,
terminal parity at level six,
Gamma_2 = Z_64.
```

The only stronger version left is the concrete physical extraction:
`L_fl,MTT = alpha L_tower + E` on this sector with
`||E|| < 9 alpha/2`.
