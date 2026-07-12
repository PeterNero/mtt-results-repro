---
abstract: |
  We try to close the selected gerbe/B-field source promotion step for the
  qutrit projective Iwasawa route.  The finite arithmetic is already strong:
  a flat Z3 B-field/discrete-torsion cocycle has zero finite Bianchi residual
  and reproduces the qutrit zeta3 corner phase.  The remaining issue is
  selection.  In the current Strominger/Fu-Yau MTT flux slice, the selection
  functional depends on the B-field through the Green-Schwarz curvature Hhat
  and fixed topological sector data.  Flat torsion changes holonomy but leaves
  Hhat unchanged.  Therefore the existing curvature/Bianchi selection data
  cannot choose between the three Z3 flat torsion labels unless the discrete
  torsion class is already included in the fixed differential-cohomology
  sector.  This closes the reason the source cannot yet be promoted, and
  identifies the exact extra datum required.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Flat-Torsion Gerbe Selection Gap
---

# Purpose

The previous certificate supplied a candidate finite gerbe map:

```text
B((a,b),(a',b')) = -a' b / 3 mod Z,
Hol_B(x,y)=exp(2*pi*i*B(x,y)).
```

It matches the qutrit projective cocycle and has finite `dB=0`.  Here we test
whether the already selected Strominger/Fu-Yau curvature/Bianchi sector selects
this nontrivial `Z3` torsion label.

# Calculation

For `m=0,1,2`, define:

```text
B_m((a,b),(a',b')) = m*(-a' b)/3 mod Z.
```

The executable calculation checks all triples in `F_3^2` and finds:

```text
dB_m = 0 for m=0,1,2,
delta Hhat = 0 for m=0,1,2,
Green-Schwarz Bianchi residual is unchanged,
Freed-Witten curvature obstruction is unchanged.
```

The holonomy distinguishes the labels:

```text
m=0: trivial cocycle,
m=1: current qutrit zeta_3^2 orientation,
m=2: conjugate zeta_3^1 orientation.
```

# Selection Gap

The Strominger/heterotic-flux corpus fixes the B-field as a Deligne 2-gerbe
connection and formulates the selection potential in terms of the
Green-Schwarz curvature `Hhat`, Chern-Simons terms, and fixed topological
sector data.

That is enough to select the Fu-Yau/Strominger curvature/Bianchi sector, but it
does not by itself choose a flat torsion holonomy representative:

```text
flat torsion changes holonomy,
flat torsion does not change Hhat,
the present curvature functional cannot distinguish m=0,1,2.
```

So the nontrivial qutrit gerbe is not wrong.  It is not yet selected.

# Exact Missing Datum

To promote the twisted source, one must supply one of:

```text
fixed differential-cohomology torsion label m=1 or m=2,
or an equivalent selected gerbe/B-field period table,
or a selected projector/zero-mode construction that forces the same label.
```

Once that discrete label is supplied, the finite Bianchi and holonomy checks are
already ready for the promotion validator.  The remaining downstream tasks are
then selected projector retention, selected `D_E`, selected `dotD`, primitive C1
contractions, and finally the Yukawa/CKM/PMNS magnitudes.

# Verdict

Full selected-source closure cannot honestly be claimed from the current corpus
alone.  What is now closed is the reason:

```text
the missing datum is not another continuous metric or curvature calculation;
it is a selected flat differential-cohomology torsion label.
```

This is a smaller and sharper problem than before.
