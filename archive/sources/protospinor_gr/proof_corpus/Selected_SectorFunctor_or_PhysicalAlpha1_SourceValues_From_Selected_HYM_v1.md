# Selected SectorFunctor or Physical Alpha1 SourceValues From Selected HYM v1

## Result

The attempted ordinary sector functor

```text
End_0(V_alpha) basis T1,T2,T3 -> 27-mode B_N/qutrit sector basis
```

does not close. The obstruction is not numerical looseness but a cocycle
mismatch:

```text
ordinary End0 commutator phase = 1
B_N projective commutator phase = [-0.5, -0.866025403784]
distance from 1 = 1.732050807568658
projective commutator residual = 6.474e-16
```

So the current `B_N` sector basis cannot be identified with the selected
ordinary End0 basis by an ordinary functor preserving equivariance.

## Consequence

The correct positive target is sharper:

1. build a selected gerbe-twisted/central-extension End0-to-B_N sector functor
   carrying the same projective cocycle, or
2. bypass this functor by deriving physical `dotD_alpha1` source values from
   the selected HYM/PhiFin branch.

The existing `27x27` sector projectors and `dotD_alpha1` matrices remain useful
diagnostic shapes, but they are not promoted as selected sector values here.

Status:

```text
ORDINARY_END0_TO_PROJECTIVE_BN_SECTOR_FUNCTOR_NO_GO_GERBE_LIFT_OR_ALPHA1_SOURCE_REQUIRED
```

Next:

```text
MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1
```
