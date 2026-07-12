# SameSourceSymmetryBreaking Reduction Import v1

Status: `SAME_SOURCE_SYMMETRY_BREAKING_IMPORTED_ORIENTATION_DE_DOTD_OPEN`.

The same-source symmetry breaker is now reduced to an orientation-carrying
`D_E/dotD` source packet.  The current invariant data are not enough:
topology, `h1`, the finite qutrit label, Appell-Humbert existence, equal-radius
data, and curvature rows are all base-swap/Pic0 or conjugation insensitive at
the required gate.

The primary route is now `MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1`.
It must supply selected source origin, q79/q369 orientation handling, selected
`D_E`, reduced Green, same-branch `dotD_alpha1`, and validator-passing source
flags without observed CP sign, benchmark flavor matrices, or lifted selected
flags.

Repair paths remain live but secondary: the Gauduchon wall route is blocked by
the current equal-radius source, ordered integral/Appell-Humbert data still need
a source certificate, and Pic0-only is necessary but not sufficient.

Next artifact: `MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1`.
