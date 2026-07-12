---
abstract: |
  We compute an explicit finite flat gerbe/B-field holonomy model for the
  qutrit projective twist.  On `F_3^2`, the torsion period
  `B((a,b),(a',b'))=-a' b/3 mod Z` has holonomy
  `exp(2*pi*i*(-a' b)/3)`, satisfies the finite cocycle identity, has zero
  discrete Bianchi residual, and has nondegenerate alternating commutator form.
  This closes the candidate holonomy map from flat discrete torsion to the
  `zeta_3` projective cocycle.  It does not select the twist in MTT, nor does it
  verify the full heterotic Green-Schwarz Bianchi or Freed-Witten conditions on
  the actual compactification.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Discrete Gerbe Holonomy Candidate
---

# Calculation

Use the finite base:

```text
F_3^2 = {(a,b)}.
```

Define a flat torsion B-field period:

```text
B((a,b),(a',b')) = -a' b / 3 mod Z.
```

The holonomy is:

```text
Hol_B(x,y) = exp(2*pi*i*(-a' b)/3).
```

This is exactly the qutrit clock/shift multiplication cocycle:

```text
U_x U_y = Hol_B(x,y) U_(x+y).
```

# Bianchi Check

The finite coboundary is:

```text
dB(x,y,z)=B(y,z)-B(x+y,z)+B(x,y+z)-B(x,y).
```

The executable calculation finds:

```text
dB = 0 on all triples.
```

So the flat finite model has zero discrete Bianchi residual.

# Nontriviality

The alternating commutator form is:

```text
B_alt(x,y)=B(x,y)-B(y,x).
```

On the standard basis its matrix is:

```text
[[0,1],
 [2,0]] mod 3.
```

This has rank `2`, so the discrete torsion is nontrivial and nondegenerate.

# Guardrail

This closes a candidate map:

```text
flat Z3 gerbe/discrete torsion -> qutrit zeta3 cocycle.
```

It does not close:

```text
MTT selection,
full heterotic Green-Schwarz Bianchi,
Freed-Witten restriction on selected cycles,
twisted projector retention,
selected D_E/dotD.
```

The next missing source is no longer merely "some gerbe".  It is a selected
Deligne/Cech or B-field period representative whose restriction to the finite
twisted carrier is the above `1/3` torsion class.
