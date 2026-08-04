---
abstract: |
  We derive the six Z_64 carry rows from a precise recursive shared-circle
  refinement theorem.  The existing carry papers proved that the relation
  matrix 2x_i=x_{i+1}, 2x_5=0 has Smith form [64], but left open why MTT
  should supply those rows.  Here we show that the rows follow from a
  six-level dyadic refinement tower of the single shared central circle when
  the variables x_i are cumulative carry classes: each coherent refinement
  transports one level of unresolved spinorial/phase memory into twice the
  next-level carry class, and the terminal return is two-torsion.  Under these
  hypotheses the quotient is cyclic Z_64.  A longer recursive tower gives a
  larger dyadic carrier Z_{2^L}; then the physical CKM branch must descend to
  the selected order-64 character.  The spectral flavor-projector construction
  now proves that the selected central-circle tower operator chooses the
  five-step D_2 tower with terminal two-torsion.  The remaining MTT-specific
  obligation is to identify the actual flavor closure operator with that tower
  operator, up to corrections smaller than the spectral selection gap.
author:
- Peter Nero
date: May 2026
title: |
  Recursive Shared-Circle Z64 Row-Origin Theorem
---

# Purpose

The dyadic CP gate needs:

```text
Gamma_2 ~= Z_64
```

or at least a selected dyadic character of order `64`.

Earlier notes proved:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0
```

implies:

```text
coker A ~= Z_64.
```

The open question was why MTT should provide exactly these rows.

This paper supplies the row-origin theorem:

```text
six-level dyadic refinement of the shared central circle
+ cumulative carry convention
+ terminal two-torsion return
=> the six Z_64 carry rows.
```

# Convention: Cumulative Carry Classes

Let:

```text
x_0,x_1,x_2,x_3,x_4,x_5
```

be cumulative carry classes, not six independent binary bits and not six
separate circles.

The convention is:

```text
x_i = unresolved coherent phase memory after i dyadic refinements,
x_{i+1} = the carry produced by resolving x_i one level deeper.
```

Thus one refinement step doubles the carried class:

```text
x_{i+1} = 2x_i.
```

Written as an integer relation:

```text
2x_i - x_{i+1}=0.
```

This is the convention used in the existing carry matrix.

If instead one used level-unit character generators for a degree-two circle
cover, the relation would appear with the opposite indexing.  The two
descriptions are equivalent after choosing whether variables record local
units or cumulative transported memory.  The CKM carry matrix uses cumulative
memory.

# Shared-Circle Refinement Tower

Assume the flavor CP sector contains one shared central-circle bookkeeping
channel:

```text
S^1_cen.
```

Assume the coherent projector refines this shared phase through six dyadic
levels:

```text
C_0 -> C_1 -> C_2 -> C_3 -> C_4 -> C_5.
```

These are not six unrelated carriers.  They are six records of one central
circle under successive admissible refinements.

The tower is dyadic when each transition satisfies:

```text
R_i(x_i)=x_{i+1}=2x_i.
```

for `i=0,...,4`.

# Terminal Return

The terminal row is:

```text
2x_5=0.
```

Interpretation:

```text
after six dyadic refinements, the remaining spinorial/phase-return memory is
two-torsion.
```

This is the finite closure analogue of the proto-spinorial `Z_2` return
obstruction.  It is not optional: without it, the carry tower has a free
generator and no finite `Z_64` quotient.

# Theorem: Row Origin from Dyadic Refinement

Assume:

1.  the CP dyadic sector is carried by one shared central-circle refinement
    tower;

2.  the variables `x_i` are cumulative carry classes of that same shared
    phase;

3.  each of the first five coherent refinement steps doubles the cumulative
    carry:

    ```text
    x_{i+1}=2x_i, i=0,...,4;
    ```

4.  the sixth level has terminal two-torsion:

    ```text
    2x_5=0.
    ```

Then the relation matrix is exactly:

```text
A_64 =
[
  2 -1  0  0  0  0
  0  2 -1  0  0  0
  0  0  2 -1  0  0
  0  0  0  2 -1  0
  0  0  0  0  2 -1
  0  0  0  0  0  2
].
```

Moreover:

```text
coker A_64 ~= Z_64.
```

## Proof

The first five hypotheses give the carry rows:

```text
2x_i - x_{i+1}=0, i=0,...,4.
```

The terminal return gives:

```text
2x_5=0.
```

Substituting along the carry chain:

```text
x_1=2x_0,
x_2=4x_0,
x_3=8x_0,
x_4=16x_0,
x_5=32x_0.
```

The terminal row becomes:

```text
2x_5 = 64x_0 = 0.
```

Every generator is a multiple of `x_0`, and `x_0` has order `64`.  Hence:

```text
coker A_64 ~= Z_64.
```

Equivalently, the Smith normal form of `A_64` is:

```text
[64].
```

This proves the theorem.

# Why This Is Stronger Than the Previous Carry Gate

The previous carry gate said:

```text
if the rows are supplied, then Z_64.
```

This theorem says:

```text
if MTT supplies a six-level dyadic refinement tower of the shared circle,
then the rows are forced.
```

So the old open problem moved one level deeper:

```text
old open gate: derive rows 2x_i=x_{i+1}, 2x_5=0;
new open gate: derive the six-level shared-circle dyadic refinement tower
               and terminal two-torsion return.
```

The spectral flavor-projector construction proves this new gate for the
central-circle tower operator `L_tower`.  The operator-identification criterion
then proves that any actual MTT flavor operator of the form
`alpha L_tower + E`, with `||E|| < 9 alpha/2`, has the same selected tower
label.  The last remaining step is to extract that concrete MTT block and
prove the bound.

# Recursive Topology Option

The user correctly warned that the topology might be recursive.  This theorem
does not require the full topology to stop at six levels.

For `L` dyadic levels with terminal two-torsion:

```text
2x_i=x_{i+1}, i=0,...,L-2,
2x_{L-1}=0,
```

the quotient is:

```text
Z_{2^L}.
```

Therefore:

```text
L=6 -> Z_64,
L=7 -> Z_128,
L=8 -> Z_256,
...
```

If the MTT topology continues beyond six levels, the CKM proof can still work,
but it must add a selected descent:

```text
Z_{2^L} -> Z_64
```

or prove that the physical CP character has exact order `64`.

# Relation to the Shared Circle

This row-origin theorem is compatible with the corpus only because the six
variables are levels of one shared circle.

It does not say:

```text
six binary memories -> Z_64.
```

That remains false; six independent binary memories give:

```text
Z_2^6,
```

whose exponent is only `2`.

The correct statement is:

```text
one shared central circle
+ six cumulative dyadic carry levels
+ terminal two-torsion
=> Z_64.
```

# MTT-Specific Remaining Obligation

The row-origin theorem is now instantiated for the spectral central-circle
tower operator.  To finish the dyadic derivation inside full MTT, the corpus
must identify the actual MTT flavor closure-strain operator:

```text
L_fl,MTT | exact-order-64 central-circle tower sector
= alpha L_tower + E
```

with:

```text
||E|| < 9 alpha/2.
```

Equivalently, it must supply one of the following data:

1.  an explicit coherent projector/refinement operator `R` on the shared
    central-circle CP sector that reduces to:

    ```text
    R(x_i)=2x_i=x_{i+1};
    ```

2.  a central-circle Wilson/refinement tower whose character pullback, after
    converting to cumulative carry variables, yields:

    ```text
    2x_i-x_{i+1}=0;
    ```

3.  a proto-spinor return-memory theorem whose Hessian/closure generator has
    the same isolated lowest tower eigenvalue: five dyadic refinements and
    terminal two-torsion;

4.  a string/flux/projector relation matrix whose Smith form contains the same
    dyadic carry block;

5.  a larger recursive carrier `Z_{2^L}` plus an explicit selected descent to
    the physical order-64 CP character.

# Consequence for q=79

Once the row-origin theorem is instantiated in MTT:

```text
Gamma_2 ~= Z_64.
```

The previously proved chain applies:

```text
nil-survivor execution
-> retarded primitive predecessor
-> q_64=15.
```

With the Mukai component:

```text
q_7=2,
```

CRT gives:

```text
q=79 mod 448.
```

# Gate Status

```text
six independent Z2 memories give Z64                         FAIL
carry rows imply Z64                                         PROVED
six-level dyadic refinement tower implies carry rows          PROVED
terminal two-torsion gives exact order 64                     PROVED
longer recursive tower gives Z_{2^L}                          PROVED
candidate R=D_2^* on S^1_cen characters                       IDENTIFIED*
spectral P_fl selection of R=D_2^*                              PROVED**
terminal two-torsion from spinorial return                      PROVED*
spectral P_fl level-six placement                               PROVED**
operator-identification stability criterion                     PROVED***
extract concrete L_fl,MTT block and norm bound                  OPEN
larger tower descends to selected order-64 CP character        OPEN IF NEEDED
```

`*` See `Shared_Circle_Doubling_Operator_Candidate_for_Z64_Carry_v1.md`.
For terminal parity, see `Terminal_Spinorial_Return_Gate_for_Z64_Carry_v1.md`.
`**` See `Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md`.
`***` See `MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md`.

# Bottom Line

The dyadic gate has advanced from:

```text
derive these six rows.
```

to:

```text
derive a six-level dyadic refinement tower of the shared central circle
with terminal two-torsion.
```

The spectral projector now derives that tower for `L_tower`.  That is the
right MTT-native object.  It respects recursive topology, preserves the
shared-circle constraint, and avoids the false `Z_2^6 = Z_64` inference.  The
remaining proof is the operator-identification and perturbation-bound step.
