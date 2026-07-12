# MTT Selected Route-C Smooth BN Galerkin Lift

Status: `MTT_SELECTED_ROUTEC_SMOOTH_BN_GALERKIN_LIFT_SCAFFOLD_BUILT_SELECTED_DE_STILL_OPEN`

This builds the first smooth numerical lift of the finite `F3^2 x C3`
twisted scaffold.

## Emitted

- basis dimension: `27`
- zero cluster dimension: `3`
- complement gap: `4.38649084493`
- quadrature: 3x3 active-deck trapezoid rule
- Gram matrix: identity
- model stiffness: diagonal active-deck Laplacian
- Riesz projector and reduced Green operator: emitted for the model active
  Laplacian

## Interpretation

This is a superset repair path, not a full straight proof.  It constructs a
legal gerbe-twisted smooth Galerkin scaffold over the selected active deck
shadow and previous non-identity projective `rho_E` packet.  It does not yet
claim the selected Iwasawa/Strominger `D_E` action, sector projectors, `dotD`,
or full truncation-error certificate.

## Next

Build `MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1`: place the selected
`D_E` action on this basis, derive sector projectors and `dotD_alpha1` in the
same basis, then replay the Route-C manifest without lifted flags.
