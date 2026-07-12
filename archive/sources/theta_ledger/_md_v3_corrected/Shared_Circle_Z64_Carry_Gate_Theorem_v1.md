---
abstract: |
  We advance the dyadic side of the MTT order-448 CP program by formulating
  the exact shared-circle theorem needed to derive the Z64 factor.  The corpus
  strongly supports the central circle as the unique shared coherence channel,
  a finite Z3 family holonomy on that circle, central-circle phases in Yukawa
  and CP data, and proto-spinorial Z2 return memory.  These facts do not by
  themselves prove Z64.  Six independent binary memories give Z2^6 with
  exponent 2.  A true order-64 character requires the six memories to be
  linked as one dyadic carry chain 2x_i=x_{i+1}, with terminal closure
  2x_5=0.  The relation matrix has Smith normal form [64].  The remaining
  proof obligation is to derive those exact carry rows from MTT projector,
  refinement, Wilson-line, or shared-circle holonomy data.
author:
- Peter Nero
date: May 2026
title: |
  Shared-Circle Z64 Carry Gate Theorem
---

# Purpose

This note isolates the dyadic theorem that remains to be proved.

The CP program needs:

```text
Gamma_2 ~= Z_64
```

or at least a selected character of dyadic order `64`.

The corpus does support the ingredients for a dyadic lift, but not yet the
exact relation rows.  This note separates the evidence from the theorem.

# Corpus support

The current corpus supports:

```text
one shared central circle S^1_cen,
finite holonomy on that circle,
family Z3 from central-circle holonomy,
central-circle phases in Yukawa and CP data,
ProtoSpinor Z2 return/loop memory,
refinement stability and coherent projector selection.
```

This is real support.  It means the dyadic factor should live on one shared
circle, not on six unrelated phase circles.

But it does not yet prove:

```text
2x_i=x_{i+1}.
```

# What fails

Six independent binary memories give:

```text
Z_2^6.
```

This group has:

```text
64 elements,
exponent 2.
```

Therefore it cannot support the CKM CP character with denominator `64`.

So the invalid inference is:

```text
six binary memories => Z_64.
```

# The required carry theorem

Let:

```text
x_0,x_1,x_2,x_3,x_4,x_5
```

be six refinement levels of the same shared central-circle character.

The needed theorem is:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

Equivalently:

```text
x_i = 2^i x_0,
64 x_0 = 0.
```

Thus:

```text
coker(A_carry) ~= Z_64.
```

# Proof if the rows are supplied

The proof is immediate.

From:

```text
2x_i=x_{i+1}
```

we get:

```text
x_1=2x_0,
x_2=4x_0,
x_3=8x_0,
x_4=16x_0,
x_5=32x_0.
```

The terminal row:

```text
2x_5=0
```

then gives:

```text
64x_0=0.
```

The Smith normal form of the full relation matrix is:

```text
[64].
```

# Why terminal closure matters

The chain without:

```text
2x_5=0
```

has a free generator.  It is not a finite dyadic quotient.

So the proof needs two ingredients:

```text
1. carry from one refinement level to the next;
2. terminal finite closure at level six.
```

# Possible sources of the rows

The carry rows could come from one of five places:

```text
1. projector refinement:
   the coherent projector maps level i memory into doubled level i+1 memory;

2. proto-spinor return:
   each admissible return requires a double-cover lift into the next level;

3. central-circle holonomy:
   finite phase refinement on S^1_cen imposes a dyadic inverse tower;

4. Wilson/orbifold remnant:
   a discrete remnant imposes the same integer relation matrix;

5. string/flux integral sector:
   the compactification supplies an exact integral row set with SNF [64].
```

The first three are most MTT-native.  The fourth and fifth are useful backup
routes.

# Current gate status

```text
shared central circle exists                     CORPUS-SUPPORTED
family Z3 holonomy on central circle exists      CORPUS-SUPPORTED
central-circle phases contribute to CP           CORPUS-SUPPORTED
proto-spinor supplies structural Z2 memory       CORPUS-SUPPORTED
six independent Z2 memories give Z64             FAIL
six carry rows plus terminal closure give Z64    FORMAL PASS
six-level dyadic refinement tower gives rows     PROVED*
spectral P_fl derives the D_2 tower              PROVED**
operator-identification stability criterion      PROVED***
extract concrete L_fl,MTT block and norm bound   OPEN
```

`*` See `Recursive_Shared_Circle_Z64_Row_Origin_Theorem_v1.md`: once the shared
central circle is equipped with six cumulative dyadic carry refinements and a
terminal two-torsion return, the rows `2x_i=x_{i+1}`, `2x_5=0` are forced.
The natural concrete candidate is `R=D_2^*`, induced by the degree-two
central-circle cover `D_2(z)=z^2`.

`**` See `Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md`.
`***` See `MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md`.
The remaining task is to extract the actual MTT coherent projector,
central-circle Wilson/refinement data, proto-spinor return memory, or
string/flux relation matrix and prove the correction bound
`||E|| < 9 alpha/2`.

# Executable check

The check:

```text
shared_circle_z64_carry_gate_check.py
```

compares:

```text
Z_2^6 independent bits,
carry chain without terminal closure,
six-stage carry chain,
direct selected Z64 row.
```

It confirms that only the carry chain or a direct `64x=0` row gives the needed
dyadic exponent.

# Bottom line

The dyadic side is now a precise theorem target:

```text
derive the six-stage dyadic refinement tower of the shared central circle.
```

Until that is done, `Z_64` is a formally correct candidate, not a completed MTT
derivation from concrete projector data.

# Minimality refinement

The successor check:

```text
Z64_Carry_Minimality_and_Row_Obligation_v1.md
z64_carry_minimality_check.py
```

shows that all rows matter:

```text
full carry matrix                    -> SNF [64],
remove any one row                   -> not finite Z64,
carry rows without terminal closure  -> free rank 1,
terminal m*x_5=0                     -> exponent 32m.
```

Thus `2x_5=0` is the minimal terminal closure that gives exactly `Z_64`.
If a longer recursive topology supplies a larger dyadic carrier, the proof must
also show why the physical CP character descends to order `64`.
