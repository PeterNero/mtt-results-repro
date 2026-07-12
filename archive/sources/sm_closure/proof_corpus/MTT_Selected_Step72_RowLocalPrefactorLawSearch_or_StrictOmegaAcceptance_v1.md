# MTT Selected Step72 RowLocalPrefactorLawSearch or StrictOmegaAcceptance v1

Status: `MTT_SELECTED_STEP72_ROWLOCAL_PREFACTOR_LAW_SEARCH_BUILT_STRICT_OMEGA_STILL_OPEN`.

## Result

Step72 fixes the strict acceptance predicate for the remaining scalar rows and
tests the tempting shortcut: using the earlier SM-parity replay matrix as the
row-local source.  That shortcut is rejected.

```text
accepted row-local source rows : 0
accepted threshold scheme rows : 0
accepted Omega source rows     : 0
strict Omega acceptance closed : False
```

The earlier matrix is still valuable: it gives an exact postcheck target table,
not a source selector.

## Target Table

```text
Omega_u.gen1     C_diag=3.70339305765 target=(3.703393057649859) / D_fin.family
Omega_u.gen2     C_diag=4.07588204575 target=(4.075882045746991) / D_fin.family
Omega_u.gen3     C_diag=1.0254272111 target=(1.02542721110437) / D_fin.family
Omega_d.gen1     C_diag=7.84756037806 target=(7.847560378056674) / D_fin.family
Omega_d.gen2     C_diag=0.291281116039 target=(0.2912811160389499) / D_fin.family
Omega_d.gen3     C_diag=1.65715602654 target=(1.6571560265441605) / D_fin.family
Omega_e.gen1     C_diag=0.836142639557 target=(0.8361426395567477) / D_fin.family
Omega_e.gen2     C_diag=0.322858023551 target=(0.32285802355070764) / D_fin.family
Omega_e.gen3     C_diag=0.668642641588 target=(0.6686426415879114) / D_fin.family
Omega_H.lambda   C_diag=1.19386993168 target=(1.193869931683266) / D_fin.H
```

All ten diagnostic prefactors remain finite and order-one, but the table is
postcheck-only.

## Source-Law Search

The closed source-only material through Step71 contains theta weights plus two
finite heat/torsion classes: `D_fin.family` and `D_fin.H`.  That cannot emit the
ten row-local values.  The family diagnostic span is
`26.9415349844`, while the source-class-only diagnostic model has max
multiplicative residual `6.03792483154`.

Replay-fitted 1-3 knob checks remain diagnostic only:

```text
one global knob max factor error       : 6.08943076391
three family-sector knobs uncovered    : 1
three family-sector knobs max error    : 5.3516923018
```

A 1-3 knob lane remains scientifically possible only if the knobs are selected
by MTT geometry before replay.  Fitting them to the replay table is not accepted.

## SM-Parity Matrix Comparison

Compared with the earlier SM-parity matrix, Step72 keeps the same boundary as
Step71: diagonal scalar slots are aligned as postchecks, while down-sector
mixing remains outside the scalar-prefactor proof.

```text
Y_d offdiag/frob = 0.042282516133
```

## Next Object

The next non-looping proof object is an honest same-branch Galerkin/HYM row-local
execution:

```text
L_rowlocal.Omega =
  normalized finite Galerkin matrix element
  <psi_L, Pi0^perp G_E (delta_Omega D_E) Pi0^perp psi_R>

Omega.value =
  D_fin.class * L_rowlocal.Omega * T_scheme.Omega * epsilon_Theta^n
```

Next artifact: `MTT_Selected_HonestRowLocalHYMGalerkinExecution_or_SelectedPrefactorSourceRows_v1`.
