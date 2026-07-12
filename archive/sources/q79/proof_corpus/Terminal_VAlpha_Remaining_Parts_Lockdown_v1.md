# Terminal VAlpha Remaining Parts Lockdown v1

## Purpose

This note locks down the proof frontier after the terminal admissible-section
source result.  It does not add a new physical source proof.  It records which
questions are now closed by executable certificates and which named gates still
have to be supplied before V_alpha can be promoted to the full same-source
operator packet.

## Closed Under The Explicit Terminal Principle

The selected terminal representative is:

```text
source label: g3 / L3-K2
L:            (1,-2,0)
L^2:          (2,-4,0)
c2(V_alpha): (4,0,0)
```

The selected ordered-source packet validates the ordered integral form
E(g1,g2)=+2 and E(g3,g4)=-4.  The selected cohomology packet validates h1=8
and supplies a nonzero Ext class: a closed, non-exact C1 vector.  Thus the old
L-sign, ordered-source, h1, and nonzero Ext searches are no longer the active
blockers under `TerminalAdmissibleSectionSourcePrinciple.v1`.

The split line-bundle or diagonal Cartan HYM shortcut is also retired.  The
positive alpha1 row cannot be realized by such a split HYM source, so the next
source must be genuinely nonabelian stable/sheaf data or an honest Route-C
residual solve.

## What Is Not Closed

This is not full SM closure.  It does not compute Yukawa magnitudes, CKM/PMNS
values, primitive C1 response matrices, kinetic normalizations, thresholds, or
RG matching.

The following gates remain open:

1. `UnconditionalTerminalAdmissibleSectionTheorem`: promote the explicit
   terminal admissible-section principle into the MTT spine, or derive it from
   projection/admissibility rules.
2. `SelectedNonSplitVAlphaStabilityOrRouteCResidual`: prove stability/HYM for
   the selected non-split V_alpha source, or supply a selected Route-C residual
   for the same class.
3. `OperatorLayerPic0Recheck`: the Pic0 quotient is closed only for the ordered
   Chern/H1/ordinary-curvature layer; holonomy-sensitive operator data must
   recheck it.
4. `SameSourceChernWeilGSRow`: derive the visible Chern-Weil/Green-Schwarz row
   from the same selected source.
5. `SameSourceDErhoERieszGreenDotD`: supply same-source D_E/Riesz/Green/dotD
   data, including selected rhoE/transition data and branch-consistent
   alpha1-driver proof.
6. `PrimitiveC1Contractions`: fill the primitive 3x3 contraction blocks used by
   the finite C1 response calculator.
7. `NoProxyYukawaCKMPMNSAndSMClosure`: compute the selected matrices and run
   the no-proxy SM comparison only after the source/operator gates are closed.

## Lockdown Verdict

The remaining problem is no longer a vague sign or h1 ambiguity.  It is a
single selected-source/operator proof problem, with explicit downstream
validators already available.  The correct next proof target is a selected
nonabelian V_alpha HYM or Route-C source that simultaneously provides
stability/HYM, the same-source Chern-Weil row, operator-layer Pic0 behavior,
and same-source D_E/Riesz/Green/dotD data.  Only after that should the primitive
C1 contractions and no-proxy flavor matrices be filled.
