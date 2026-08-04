---
abstract: |
  We identify the concrete operator candidate behind the recursive
  shared-circle Z_64 carry theorem.  On the common central circle
  S^1_cen, the degree-two self-cover D_2(z)=z^2 induces multiplication by two
  on the character lattice Hom(S^1,U(1)) ~= Z: D_2^* chi_n = chi_{2n}.  If
  the coherent flavor projector selects a six-step stable refinement tower of
  this one shared circle, and if the sixth lifted return has spinorial
  two-torsion, then the cumulative carry classes satisfy
  x_{i+1}=2x_i and 2x_5=0, hence the dyadic quotient is Z_64.  This paper
  supplies the natural mathematical candidate for the refinement operator R.
  The spectral flavor-projector construction now proves that the selected
  central-circle tower operator chooses this D_2 tower and places the terminal
  parity at level six.  The remaining MTT-specific gate is to identify the
  actual flavor closure operator with that tower operator up to a perturbation
  smaller than the selection gap.
author:
- Peter Nero
date: May 2026
title: |
  Shared-Circle Doubling Operator Candidate for the Z64 Carry
---

# Purpose

The row-origin theorem reduced the dyadic gap to:

```text
identify the concrete shared-circle refinement operator R,
prove R(x_i)=x_{i+1}=2x_i,
prove terminal two-torsion at the sixth selected level.
```

This paper identifies the natural mathematical candidate for `R`.

# The Operator

Let:

```text
S^1_cen = {z in C : |z|=1}.
```

Define the degree-two self-cover:

```text
D_2: S^1_cen -> S^1_cen,
D_2(z)=z^2.
```

The unitary characters of the circle are:

```text
chi_n(z)=z^n,
n in Z.
```

The pullback by `D_2` is:

```text
D_2^* chi_n
= chi_n(D_2(z))
= (z^2)^n
= z^{2n}
= chi_{2n}.
```

Therefore:

```text
D_2^*: n -> 2n
```

on the character lattice.

# Relation to Carry Variables

Let `x_i` be cumulative carry classes, as in the row-origin theorem.  If the
coherent flavor projector transports the selected central-circle character
through one `D_2` refinement step, then:

```text
x_{i+1}=D_2^*(x_i)=2x_i.
```

The integer relation is:

```text
2x_i-x_{i+1}=0.
```

Thus the degree-two shared-circle cover supplies exactly the inter-level carry
row.

# Six Selected Iterates

If MTT selects six stable dyadic refinement records:

```text
x_0,x_1,x_2,x_3,x_4,x_5,
```

then repeated pullback gives:

```text
x_i = 2^i x_0.
```

This is not six independent binary data.  It is one central-circle character
transported through six cumulative refinements.

# Terminal Spinorial Return

The terminal row needed for exact `Z_64` is:

```text
2x_5=0.
```

The natural MTT interpretation is spinorial return parity.  After the selected
sixth refinement, the remaining loop-return obstruction is a two-torsion sign:

```text
terminal return = Z_2.
```

Then:

```text
2x_5 = 2(32x_0)=64x_0=0.
```

Therefore:

```text
coker A ~= Z_64.
```

# Theorem: Doubling Operator Gives Carry Rows

Assume:

1.  the selected CP dyadic sector is carried by the shared central circle
    `S^1_cen`;

2.  the coherent refinement operator on the selected character lattice is the
    pullback by the degree-two cover `D_2(z)=z^2`;

3.  the selected variables `x_i` are cumulative carry classes;

4.  MTT selects six stable iterates of this refinement;

5.  the terminal selected return is two-torsion:

    ```text
    2x_5=0.
    ```

Then:

```text
2x_i-x_{i+1}=0, i=0,...,4,
2x_5=0,
```

and hence:

```text
Gamma_2 ~= Z_64.
```

## Proof

By direct computation:

```text
D_2^* chi_n = chi_{2n}.
```

So each selected refinement doubles the cumulative character:

```text
x_{i+1}=2x_i.
```

This gives the five carry rows.  The terminal spinorial return gives the sixth
row:

```text
2x_5=0.
```

The carry-chain proof then gives:

```text
x_5=32x_0,
64x_0=0,
coker A ~= Z_64.
```

This proves the theorem.

# What Is Now Proved

The actual operator behind the carry rows is no longer mysterious:

```text
R = D_2^* on the shared-circle character lattice.
```

The row:

```text
2x_i-x_{i+1}=0
```

is exactly the pullback relation for cumulative carry classes.

# What Remains Open

The remaining open MTT gates are now narrower:

```text
1. identify the actual MTT flavor closure operator L_fl,MTT on the
   exact-order-64 central-circle tower sector;
2. prove L_fl,MTT = alpha L_tower + E with ||E|| < 9 alpha/2, so the
   Riesz projector keeps selecting the D_2 tower with terminal parity;
3. if the full topology continues recursively, derive the selected descent to
   the physical order-64 CP character;
4. prove this dyadic tower is compatible with the ambient family Z_3 and the
   Mukai Z_7 odd block.
```

# Recursive Topology Compatibility

If the shared-circle refinement continues beyond six steps, then the same
operator gives:

```text
L steps -> Z_{2^L}.
```

This does not break the CKM branch if the physical CP character descends:

```text
Z_{2^L} -> Z_64.
```

Thus recursive topology is compatible with this operator.  What must be
selected is the physical order-64 CP quotient or character.

# Relation to q=79

Once this dyadic operator is accepted as the MTT refinement operator and the
terminal row is established:

```text
Gamma_2 ~= Z_64.
```

The already-proved selected-kernel and nil-survivor chain gives:

```text
q_64=15.
```

Together with:

```text
q_7=2,
```

CRT gives:

```text
q=79 mod 448.
```

# Gate Status

```text
D_2(z)=z^2 induces n->2n on circle characters        PROVED
cumulative carry convention gives 2x_i-x_{i+1}=0     PROVED
six D_2 iterates plus terminal parity give Z_64       PROVED
spectral P_fl selection of D_2^*                      PROVED**
terminal spinorial two-torsion row                    PROVED*
spectral P_fl level-six placement                     PROVED**
longer tower descends to order-64 CP character        OPEN IF NEEDED
```

`*` See `Terminal_Spinorial_Return_Gate_for_Z64_Carry_v1.md`.
For minimal selection, see
`Minimal_Dyadic_Projector_Selection_Theorem_for_Z64_v1.md`.
`**` See `Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md`.

# Bottom Line

The concrete `R` candidate is:

```text
R = D_2^*, where D_2(z)=z^2 on S^1_cen.
```

This operator exactly explains the doubling rows, and the spectral projector
now selects its six-record tower with terminal two-torsion.  The remaining work
is not to invent another algebraic mechanism; it is to identify the actual MTT
flavor closure operator with the spectral tower operator, with corrections
below the selection gap.
