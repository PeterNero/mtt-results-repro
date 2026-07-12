---
abstract: |
  We refine the shared-circle Z64 theorem by checking the minimality of the
  six-stage carry relation matrix.  The full matrix with five carry rows
  2x_i=x_{i+1} and terminal closure 2x_5=0 has Smith form [64].  Removing any
  one row destroys the finite Z64 conclusion.  The five carry rows without
  terminal closure leave a free generator, while changing the terminal
  multiplier to m*x_5=0 gives order 32m.  Thus 2x_5=0 is the minimal terminal
  closure giving exactly Z64.  This sharpens the future MTT derivation: it
  must supply both inter-level carry and a terminal finite closure, or else
  explain a larger recursive carrier whose selected CP character descends to
  order 64.
author:
- Peter Nero
date: May 2026
title: |
  Z64 Carry Minimality and Row Obligation
---

# Purpose

The shared-circle dyadic candidate is:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

This note checks how much of that matrix is actually necessary.

# Full result

The full matrix has:

```text
SNF=[64],
free rank=0.
```

So it gives:

```text
coker A_carry ~= Z_64.
```

# Remove-one-row test

Removing any one row destroys the conclusion:

```text
remove one carry row      -> no exact Z64 carry conclusion,
remove terminal row       -> free rank 1.
```

The interpretation is:

```text
all five carry rows are needed to tie the six memories into one cyclic chain,
and the terminal row is needed to make the quotient finite.
```

# Terminal multiplier test

Keep the five carry rows but replace the terminal row by:

```text
m x_5=0.
```

Since:

```text
x_5=32x_0,
```

this gives:

```text
32m x_0=0.
```

So:

```text
terminal m*x_5=0 -> exponent 32m.
```

Therefore:

```text
m=1 -> Z_32,
m=2 -> Z_64,
m=3 -> Z_96,
m=4 -> Z_128,
...
```

The minimal exact terminal closure giving `Z_64` is:

```text
2x_5=0.
```

# Consequence for recursive topology

If the topology is recursive beyond six stages, a larger terminal order is not
automatically fatal.  For example:

```text
Z_128
```

contains order-64 characters.  But then MTT must prove a selected quotient or
character descent to the physical `Z_64` CP branch.

So there are two acceptable dyadic proof patterns:

```text
1. exact minimal pattern:
   six-stage carry + 2x_5=0 -> Z_64;

2. larger recursive pattern:
   longer or larger dyadic carrier -> selected order-64 CP character.
```

# What the future derivation must supply

The derivation must supply:

```text
1. why the six memories are levels of one shared-circle phase;
2. why each level carries into the next by doubling;
3. why level six has terminal two-torsion closure;
4. or, if the carrier is larger, why the physical CP character descends to
   order 64.
```

The row-origin theorem refines this obligation.  The rows follow once MTT
supplies:

```text
a six-level cumulative dyadic refinement tower of S^1_cen
+ terminal two-torsion return.
```

Thus the remaining proof is now a projector/refinement construction problem,
not a Smith-normal-form problem.

# Executable check

The check:

```text
z64_carry_minimality_check.py
```

verifies:

```text
full carry matrix -> SNF [64],
removing any row -> not SNF [64] finite,
terminal m -> exponent 32m.
```

# Bottom line

The dyadic theorem target is now exact:

```text
derive all five carry rows and the terminal closure,
or derive a larger recursive dyadic carrier with selected order-64 character.
```
