# MTT Selected SectorCharge / 1_M Dirac Rule Attempt

Status: `MTT_SELECTED_SECTORCHARGE_1M_DIRAC_RULE_ATTEMPT_BUILT_SOURCE_POLARIZATION_OPEN`

This artifact tries the sector charge/chirality route requested by the current
frontier, including the `1_M` Dirac-neutrino rule.

## What Closes

The E6/SU(5) representation dictionary gives the structural rule:

- `10_M = Q + u^c + e^c`,
- `bar5_M = d^c + L`,
- `1_M = N^c`,
- `dirac_neutrino: bar5_M 1_M 5_H -> L N^c H_u`.

So the natural structural partition is:

- phase/clock candidate side: `u,e`,
- non-10/shift candidate side: `d,nuD`.

The `nuD` entry is not forced by treating `1_M` as another `bar5_M`; it is
forced by the Dirac operator itself.  Since `1_M=N^c` appears in
`bar5_M 1_M 5_H`, the `1_M` neutrino slot is attached to the same non-10
Dirac-neutrino channel as `bar5_M`, hence to the shift-side candidate with
`d`.

No observed constants, measured masses, CKM/PMNS data, or lifted diagnostic
flags are used.

## What Does Not Close Yet

This is still not a selected MTT theorem.  It imports a correct structural
dictionary, but the repo does not yet emit the same-branch selected source
packet proving:

- selected `U_10` clock/polarization source,
- selected `U_bar5` shift/polarization source,
- selected `1_M` Dirac-neutrino shift rule,
- selected source-to-C1 transfer and overlap normalization.

Therefore the sector charge/chirality table and the alpha1 transfer
normalization remain unpromoted.

## Superset Use

This uses a constrained superset strategy.  The straight path is the E6/SU(5)
matter-slot dictionary.  The support path is the q79 retarded/transversality
and source-level Weyl-carrier work.  These paths are combined only to localize
the remaining selected-source object; they are not used as a numerical fit.

Next artifact: `MTT_Selected_1M_DiracNeutrino_Source_or_SelectedU10Ubar5Polarization_v1`.
