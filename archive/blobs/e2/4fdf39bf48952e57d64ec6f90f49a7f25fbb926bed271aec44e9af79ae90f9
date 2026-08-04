---
abstract: |
  We decompose the CKM label q=79 under the product isomorphism
  Z_448 = Z_64 x Z_7.  The result is structurally suggestive:
  q=79 corresponds to (15,2), the PMNS quarter-turn label 336 corresponds
  to (16,0), and the phase-sum partner 33 corresponds to (33,5).
  The sevenfold component 2 is exactly the numerator of the selected Mukai
  discriminant quadratic value b(theta_7,theta_7)=2/7.  The dyadic component
  15 is one primitive dyadic unit below the quarter-turn 16.  Thus the exact
  numerator 79 can be replaced by two smaller proof gates: derive the Mukai
  discriminant component 2, already strongly supported, and derive the dyadic
  predecessor rule q_64=16-1 from the shared-circle refinement/overlap
  orientation.  If both gates hold, the Chinese remainder theorem forces
  q=79 exactly.
author:
- Peter Nero
date: May 2026
title: |
  CRT Decomposition of the CKM Label 79 into Dyadic and Mukai Gates
---

# Purpose

The overlap-filter note showed that `q=79` is selected by the CKM phase target
inside the admissible `Z_448` label set.  This paper records a stronger
structural clue:

```text
79 is not arbitrary in Z_64 x Z_7.
```

It decomposes into a dyadic predecessor of the quarter-turn and the Mukai
discriminant numerator.

# Product coordinates

Since

```text
448 = 64 * 7,
gcd(64,7)=1,
```

the Chinese remainder theorem gives

```text
Z_448 ~= Z_64 x Z_7.
```

The three physical labels decompose as:

```text
CKM label q=79          -> (15,2)
PMNS quarter l=336      -> (16,0)
phase partner r=33      -> (33,5)
```

Componentwise closure is exact:

```text
15 + 16 + 33 = 64 = 0 mod 64,
 2 +  0 +  5 =  7 = 0 mod 7.
```

# Sevenfold component

The selected Mukai block has Gram matrix

```text
K = [[2,1],
     [1,4]],
det(K)=7.
```

For the selected discriminant generator

```text
theta_7 = (1/7,5/7),
```

we computed

```text
K theta_7 = (1,3),
b(theta_7,theta_7) = theta_7^T K theta_7 = 16/7 = 2/7 mod 1.
```

Thus the Mukai discriminant form naturally supplies the numerator

```text
2 mod 7.
```

This is exactly the sevenfold component of the CKM label:

```text
q_7 = 2.
```

The phase-sum partner has

```text
r_7 = 5 = -2 mod 7,
```

so the sevenfold sector closes with the lepton branch neutral in `Z_7`.

# Dyadic component

The lepton quarter-turn in the dyadic factor is

```text
l_64 = 64/4 = 16.
```

The CKM dyadic component is

```text
q_64 = 15 = 16 - 1.
```

The phase-sum partner is then forced:

```text
r_64 = -(15+16) = 33 mod 64.
```

So the dyadic part is a predecessor rule:

```text
quark CP branch = one primitive dyadic unit before the lepton quarter-turn.
```

This is currently a conjectural structural rule, not yet a proved theorem.
It is, however, exactly the kind of rule one would expect from a recursive
shared-circle carry with an oriented overlap branch:

```text
lepton branch: exact quarter-turn,
quark branch: pre-quarter overlap survivor,
partner branch: closure complement.
```

# Exact CRT reconstruction

If

```text
q = 15 mod 64,
q =  2 mod 7,
```

then the Chinese remainder theorem gives

```text
q = 79 mod 448.
```

Likewise,

```text
l = 16 mod 64,  l = 0 mod 7  -> l = 336 mod 448,
r = 33 mod 64,  r = 5 mod 7  -> r = 33 mod 448.
```

Thus the full label triple is forced:

```text
(q,l,r)=(79,336,33).
```

# Conditional theorem

Assume:

1.  the selected CP quotient is `Z_64 x Z_7`;

2.  the lepton branch is the dyadic quarter-turn and sevenfold-neutral:

    ```text
    l = (16,0);
    ```

3.  the Mukai discriminant form selects the sevenfold CKM component:

    ```text
    q_7 = 2;
    ```

4.  the shared-circle dyadic overlap orientation selects the predecessor of
    the quarter-turn:

    ```text
    q_64 = 16-1 = 15;
    ```

5.  pairwise phase-sum closure holds.

Then the unique selected labels in `Z_448` are

```text
q=79,
l=336,
r=33.
```

# What this changes

This is the first exact structural explanation of the numerator `79` that does
not start from the CKM/Jarlskog decimal.

It does not finish the proof, because the dyadic predecessor rule still has to
be derived from MTT overlap geometry, recursive carry, or projector orientation.

But it substantially improves the target:

```text
old open problem: derive q=79 directly;
new open problem: derive q_64=15 as the pre-quarter dyadic survivor.
```

The sevenfold part is no longer mysterious: it matches the Mukai discriminant
quadratic value already selected by the positive charge-lattice route.

# Compatibility with the recursive/shared-circle setup

This decomposition respects the current architecture:

```text
Z_64  from recursive shared-circle carry,
Z_7   from the selected Mukai discriminant group,
Z_3   family holonomy orthogonal to CP.
```

No spacetime dimension count is being used.  The labels are character labels
in the selected finite quotient.  The shared circle remains the phase carrier;
the Mukai block supplies the sevenfold discriminant component; and the lepton
quarter-turn remains the complex/lens orientation benchmark.

# Gate status

```text
CRT decomposition of 79 as (15,2)                         PASS
Mukai discriminant supplies q_7=2                          PASS
lepton quarter-turn supplies l_64=16, l_7=0                PASS
phase-sum partner becomes (33,5)                           PASS
derive dyadic predecessor q_64=15 from MTT dynamics        OPEN
derive full q=79 without CKM/Jarlskog target               CONDITIONAL
```

# Bottom line

The exact numerator `79` now has a plausible structural factorization:

```text
79 = CRT(16-1 mod 64, 2 mod 7).
```

The next proof should focus narrowly on the dyadic statement:

```text
Why does the quark CP overlap branch sit one primitive dyadic unit before the
lepton quarter-turn?
```

If that predecessor rule is proved, the Mukai discriminant and CRT finish the
numerator without using the empirical CKM phase as an input.
