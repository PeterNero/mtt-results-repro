# MTT Selected Route-C Non-Invariant C1 Primitive Search

Status: `MTT_SELECTED_ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_BUILT_UNSELECTED_CANDIDATES_OPEN`

The canonical C1 tensor vanishes because the dotD response has active mode
`(-1,-1)` while zero modes have `(0,0)`.  This search tests the minimal
non-invariant repair: a primitive or basis-transport insertion carrying active
shift `(1,1)`.

## Result

- Tested fiber shifts: `0`, `1`, `2`, and `all`.
- Nonzero unselected candidates found: `4`.
- Selected C1 closure now: `False`.

The active shift is forced by finite momentum bookkeeping; this is a real
structural clue.  But the fiber rule is still not selected by theorem, and no
source theorem yet proves that this non-invariant primitive, vertex correction,
or basis transport is emitted by the selected q79/F,m=1 S3/GS branch.

## Next Gate

Prove a primitive-source selection theorem or fiber-rule audit:

- derive active shift `(1,1)` from the selected gerbe/Strominger data,
- derive the qutrit fiber rule from the selected rho_E/Chan-Paton source,
- or prove a selected basis-transport map with the same finite effect.

No observed Yukawa, CKM, PMNS, or mass data were used.
