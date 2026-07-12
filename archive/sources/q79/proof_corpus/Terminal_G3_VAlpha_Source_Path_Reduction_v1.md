# Terminal G3 VAlpha Source Path Reduction

## Question

After the terminal-map dual extension sign theorem, do we still need to find
the `r1:r2=sqrt(2):1` Gauduchon wall as the primary way to choose the visible
`L=(1,-2,0)` branch?

## Result

No, not on the terminal `g3` path.

The finite qutrit route is still ambiguous by itself:

```text
(1,-2,0) mod 3 = (1,1),
(-2,1,0) mod 3 = (1,1).
```

So finite qutrit data alone cannot distinguish target from swapped branch.

But the terminal `g3` route now has its sign/order fixed:

```text
printed g3 Hom type = K2-L3 = (-1,2,0),
physical extension line = L3-K2 = (1,-2,0),
L^2 = (2,-4,0).
```

Therefore, on the terminal `g3` path, do not solve branch selection twice.
The Gauduchon wall is no longer the primary sign selector. Its correct role is
now a stability/HYM chamber witness after terminal `g3` fixes `L`.

## Critical Packet

The remaining object is:

```text
Selected_Terminal_G3_VAlpha_Source.v1
```

It must supply:

```text
MTT source principle selecting terminal g3,
selected typed Cech/Appell-Humbert or operator source for L=(1,-2,0),
operator-layer Pic0 rule,
selected h1=8 L^2 cohomology packet with closed non-exact Ext vector,
non-split stability/HYM or Route-C residual from the same source,
same-source Chern-Weil/GS/D_E/Riesz/Green/dotD/C1 contractions.
```

## Reclassification

Use these roles going forward:

```text
terminal g3 dual theorem      -> sign/order binding,
pullback Cech h1=8 packet     -> arithmetic template,
Appell-Humbert L^2 matrix     -> transition/automorphy template,
Gauduchon p=(1,2,1) wall      -> stability chamber witness,
selected VAlpha sufficiency   -> downstream validator stack.
```

Do not use these as proof:

```text
finite qutrit orientation alone,
equal-radius Iwasawa specialization,
split abelian row as selected HYM source,
hypothetical selected flags.
```

## Guardrail

This does not prove that MTT selects g3.

It proves the correct way forward: the solution is one selected terminal-`g3`
`V_alpha` source packet, not another search for a sign-selecting radius ratio.
