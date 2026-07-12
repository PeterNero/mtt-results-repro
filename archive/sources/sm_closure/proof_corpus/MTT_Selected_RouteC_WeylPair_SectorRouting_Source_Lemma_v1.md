# MTT Selected Route-C WeylPair SectorRouting Source Lemma

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA`

This artifact tries to close the selected sector-routing source lemma.

## External Inspiration

External theta/Heisenberg and heterotic-orbifold literature supports the shape
of the needed rule: finite Weyl pairs naturally split clock/phase and
shift/translation actions, while heterotic Yukawa textures are routed by
discrete selection rules, Wilson-line/holonomy data, and sector charges.  This
is used only as inspiration, not as MTT proof.

## Result

All two-two routings of `{u,d,e,nuD}` were enumerated.  Relative to the locked
C1 packet columns, the intended route is uniquely selected:

```text
Z -> u,e as I+Z
X -> d,nuD as I+X
```

But this is still target-column selection, not independent selected-source selection.

## Remaining Gap

Current selected artifacts do not yet contain an independent theorem-derived
sector charge, chirality, or conjugation table that forces `{u,e}|{d,nuD}`.
The sector projectors retain family kernels, but they treat the family sectors
uniformly and leave selected dotD/alpha1 source verification open.

The next certificate must supply:

- a selected sector charge/chirality/conjugation table for `u,d,e,nuD`,
- a rule assigning `Z` to `u,e`,
- a rule assigning `X` to `d,nuD`,
- normalization compatibility with the selected C1 response basis.

Next artifact: `MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1`.
