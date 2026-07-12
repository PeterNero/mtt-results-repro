---
title: "Selected Qa/SU3 Source Augmentation Packet"
---

# Selected `Qa/SU3` Source Augmentation Packet

The current source problem is now local:

```text
the monad charges are compatible,
but the selected section ring is not printed.
```

The eleven required section spaces are:

```text
F1=(-3,0,1), F2=(-2,1,-1), F3=(0,-1,0), F4=(0,0,-1), F5=(1,1,1)
G1=(2,1,-1), G2=(1,0,1), G3=(-1,2,0), G4=(-1,1,1), G5=(-2,0,-1)
P=(-1,1,0)
```

The first useful computation is that every symbolic product has the right
charge:

```text
F_i + G_i = P, for i=1,...,5.
```

So the obstruction is not the line-bundle charge bookkeeping.  The obstruction
is value-level:

```text
f_i in H0(F_i),
g_i in H0(G_i),
g_i f_i in H0(P),
sum_i g_i f_i = 0.
```

To close this, the next artifact must supply a selected automorphy or section
ring model for the compact Iwasawa quotient.  Flat characters and literal
constant sections are not enough, because all eleven charges are nonzero.

## Next Solver

Build:

```text
Selected_Qa_SU3_Automorphy_Factor_Ansatz_Constraint_Solver_v1
```

It should accept candidate factors `a_q(gamma,z)`, check the cocycle law, verify
the first Chern class, solve equivariant section equations, and compute the
product constants.
