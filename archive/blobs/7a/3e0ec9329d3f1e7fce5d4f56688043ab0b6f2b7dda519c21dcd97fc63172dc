# MTT Selected Step71 SMParityMatrixComparison or RowLocalTargets v1

Status: `MTT_SELECTED_STEP71_SMPARITY_MATRIX_COMPARISON_BUILT_ROWLOCAL_TARGETS_OPEN`.

## Comparison

The earlier SM-parity matrix is an admitted replay/profile-input object.  It is
accepted for SM-parity comparison, not as a no-knob source selector.

Step70 is different: it is the upstream source contract

```text
C_HYMthr.* = D_fin.class * L_rowlocal.* * T_scheme.*
Omega      = C_HYMthr.* * epsilon_Theta^n
```

The SM-parity replay matrix projects exactly onto the ten Step70 scalar slots as
a postcheck:

```text
diagonal projection rows: 10
projection matches declared common-scale magnitudes: True
accepted row-local source rows: 0
accepted Omega source rows: 0
```

## Matrix Scope

The current Step70 scalar contract covers diagonal magnitudes and `lambda_H`.
It does not yet derive the full physical mixing matrix.

```text
Y_u offdiag/frob: 1.58755513665e-24
Y_d offdiag/frob: 0.042282516133
Y_e offdiag/frob: 0
```

So `Y_u` and `Y_e` are effectively diagonal in the replay convention, while
`Y_d` carries the CKM/down-sector offdiagonal replay content.  That mixing layer
is outside the current scalar-prefactor closure.

## Older Gap Matrix

The older final SM-parity gap matrix was a gate/blocker matrix, not the Yukawa
matrix itself.  Later artifacts supersede it at the parity-replay tier.  Its
`full_no_knob_constants` blocker is now refined into the Step70/Step71 row-local
overlap and threshold factors.

Next artifact: `MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1`.
