# MTT Selected HiggsExternalProfileData or RouteAFormulaRows v1

Status: `MTT_SELECTED_HIGGSEXTERNALPROFILEDATA_OR_ROUTEAFORMULAROWS_BUILT_HYBRID_CENTRAL_VALUES_FULL_PROFILE_OPEN`.

This artifact fills the Higgs ten-row central-value replay vector from
LHCHXSWG-style downstream sources. It derives central partial widths by
`Gamma_i = BR_i * Gamma_H` and records the tracked residual against the total
width.

This is deliberately not promoted to a full precision-profile proof: the packet
is hybrid-sourced, the uncertainty payload is diagonal-only, and no route-A
formula rows are independently computed. The values are downstream SM-parity
replay seeds, not selected MTT source values.
