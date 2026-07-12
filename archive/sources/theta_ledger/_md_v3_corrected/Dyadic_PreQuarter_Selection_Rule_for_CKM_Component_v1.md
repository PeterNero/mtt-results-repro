---
abstract: |
  We reduce the remaining dyadic component of the CKM label to a finite
  pre-quarter selection rule in Z_64.  Once the lepton branch is the exact
  quarter-turn l_64=16, and the CKM dyadic component is required to be a
  primitive order-64 label whose phase-sum partner is also primitive, the
  nearest admissible label strictly below the quarter-turn is uniquely
  q_64=15.  This does not yet prove the physics of the rule; it isolates the
  final dyadic obligation.  If MTT's shared-circle overlap orientation selects
  the pre-quarter primitive survivor, then the dyadic part of q=79 is forced.
author:
- Peter Nero
date: May 2026
title: |
  Dyadic Pre-Quarter Selection Rule for the CKM Component
---

# Purpose

The CRT decomposition reduced the exact CKM numerator to:

```text
q = CRT(q_64,q_7),
q_7 = 2,
q_64 = 15.
```

The sevenfold component `q_7=2` is explained by the Mukai discriminant
quadratic value.  The remaining question is why the dyadic component is

```text
q_64=15.
```

This paper isolates a finite rule that would force it.

# Dyadic setup

Work in the dyadic carry quotient:

```text
Z_64.
```

The lepton quarter-turn component is:

```text
l_64 = 64/4 = 16.
```

Primitive order-64 labels are exactly the odd labels:

```text
q_64 in {1,3,5,...,63}.
```

Phase-sum closure gives:

```text
r_64 = -(q_64 + 16) mod 64.
```

If `q_64` is odd, then `r_64` is also odd, so the phase-sum partner is
primitive automatically.

# Pre-quarter selection rule

The proposed dyadic rule is:

```text
The CKM dyadic branch is the primitive survivor immediately below
the lepton quarter-turn.
```

Equivalently:

```text
0 < q_64 < 16,
q_64 has order 64,
q_64 maximizes q_64.
```

The unique solution is:

```text
q_64 = 15.
```

Then

```text
r_64 = -(15+16) = 33 mod 64.
```

# Why this is the right remaining physical claim

This rule has the right MTT shape.

The lepton branch occupies the exact complex/lens quarter-turn.  The quark CP
branch is not the quarter-turn itself; it is an oriented overlap survivor
approaching the quarter-turn from the pre-quarter side.  The recursive
shared-circle carry supplies the `Z_64` resolution, while primitiveness keeps
the CKM branch at full dyadic order rather than collapsing to a divisor.

The arithmetic is therefore finished once MTT proves the physical orientation:

```text
quark CP = nearest primitive pre-quarter dyadic survivor.
```

# Finite check

The script

```text
dyadic_prequarter_selection_check.py
```

returns:

```text
selected q_64 = 15
l_64 = 16
r_64 = 33
q_64+l_64+r_64 = 64 = 0 mod 64.
```

# Conditional theorem

Assume:

1.  the dyadic CP factor is `Z_64`;

2.  the lepton component is the exact quarter-turn `l_64=16`;

3.  the CKM component and its phase-sum partner must be primitive order-64
    labels;

4.  the shared-circle overlap orientation selects the nearest primitive
    pre-quarter label.

Then the dyadic CKM component is uniquely

```text
q_64=15,
```

and the dyadic phase-sum partner is

```text
r_64=33.
```

# Relation to the full label

Combining this dyadic result with the Mukai sevenfold component gives:

```text
q_64=15,
q_7=2,
```

and hence by CRT:

```text
q=79 mod 448.
```

So the remaining numerator proof is no longer about `79` directly.  It is the
physical derivation of a nearest-pre-quarter primitive survivor in the
recursive shared-circle dyadic carry.

# Gate status

```text
dyadic quarter-turn l_64=16                         PASS
primitive pre-quarter labels enumerated             PASS
nearest primitive pre-quarter label is q_64=15      PASS
phase-sum partner is r_64=33                         PASS
MTT derives pre-quarter orientation                  OPEN
```

# Bottom line

The arithmetic path is now:

```text
pre-quarter dyadic survivor: q_64=15,
Mukai discriminant survivor: q_7=2,
CRT(q_64,q_7)=79.
```

To finish the non-empirical numerator proof, MTT must justify the
pre-quarter orientation of the quark CP overlap branch relative to the lepton
quarter-turn.
