---
title: "VAlpha/S3 Two-Block Mod-3 Lift"
version: v1
---

# Result

The rank obstruction for one selected `S3` active quotient is sharp.  Two
independent S3-active blocks exactly recover the full V_alpha mod-3 form.

# Construction

The selected finite `S3` commutator is:

```text
J_S3 = [[0,1],
        [2,0]]
```

The one-block obstruction says no map from one `F3^2` active quotient can
produce the full rank-four `V_alpha` form.  The finite repair is the direct sum:

```text
J_2 = J_S3 oplus J_S3
```

Using the block transform already recorded in the mod-3 compatibility
certificate:

```text
T = [[0,1],
     [1,0]]
```

and applying it blockwise:

```text
T_2 = T oplus T
```

gives:

```text
T_2^T J_2 T_2 =
[[0,2,0,0],
 [1,0,0,0],
 [0,0,0,2],
 [0,0,1,0]]
```

which exactly recovers the full V_alpha mod-3 form on `(g1,g2,g3,g4)`.

# Meaning

The finite source requirement is now precise:

```text
not one S3-active block,
but two independent S3-active blocks,
or an integral/geometric source whose mod-3 reduction supplies those two blocks.
```

This does not select the two blocks by MTT.  It identifies the finite shape
that any successful same-source theorem must emit.

# Guardrail

This is a finite mod-3 construction.  It does not select the integral
`L3-K2` source, does not resolve `Pic0`, does not prove same-source binding,
and does not supply `D_E`, `Riesz/Green`, `dotD`, or primitive `C1` data.
