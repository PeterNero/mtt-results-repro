---
title: "VAlpha/S3 Full Mod-3 Pullback Obstruction"
version: v1
---

# Result

The selected `S3` finite class is compatible with each active `V_alpha` block
separately, but it cannot be the full `V_alpha` source by itself.

# Calculation

The selected `S3` commutator form over `F_3^2` is:

```text
J_S3 = [[0,1],
        [2,0]]
```

It has rank `2`.

The full active `V_alpha` mod-3 Appell-Humbert form on
`(g1,g2,g3,g4)` is:

```text
[[0,2,0,0],
 [1,0,0,0],
 [0,0,0,2],
 [0,0,1,0]]
```

It has rank `4`, so the proposed full pullback has a rank mismatch with any
single selected `S3` active quotient.

For any map:

```text
Q : F_3^4 -> F_3^2
```

the pullback has the form:

```text
Q^T J_S3 Q
```

and therefore has rank at most `2`.  A brute force check over all `3^8 = 6561`
maps finds zero maps whose pullback equals the full `V_alpha` active form.

# Meaning

The blockwise compatibility remains true.  The selected `S3` class matches the
finite symplectic type seen by each `V_alpha` block.

But one `S3` active qutrit quotient cannot be the full V_alpha source.  The
same-source theorem must supply additional structure:

```text
an integral two-block lift,
or a second active block,
or a physical quotient theorem explaining how the second V_alpha block is
supplied beyond the single selected S3 quotient.
```

# Proof Discipline

This prevents an overclaim.  The selected `S3`/Green-Schwarz support is real
and useful, but it is support/obstruction-control data, not the entire
rank-two `V_alpha` Cech/Appell-Humbert source.
