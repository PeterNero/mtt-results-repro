# MTT Selected MatterSlot Transversality Readout Functional

Status: `MTT_SELECTED_MATTERSLOT_TRANSVERSALITY_READOUT_FUNCTIONAL_ATTEMPT_RHOS_INVARIANT_NOGO_GRADING_OPEN`

This artifact tries to build the selected readout that would turn the selected
stationary `rho_s` source into the SU(5)/E6 matter-slot split.

## Result

The selected stationary `rho_s` source is not enough by itself.

The honest `rho_s`/projector/Gram invariants are identical across the right
matter sectors `u,d,e,N`.  They distinguish the Higgs singlet from matter, but
they do not distinguish:

- `10_M` clock side,
- `bar5_M` shift side,
- `1_M=N^c` Dirac-neutrino shift side.

This is a useful no-go, not a failure of the program: it says the matter-slot
readout is an additional selected grading/label object, not a hidden consequence
of the universal adjoint action.

## What Still Works

The SU(5)/E6 dictionary and q79 finite transversality still give the intended
support:

- `10_M -> u,e`,
- `bar5_M -> d`,
- `1_M=N^c` through `bar5_M 1_M 5_H -> L N^c H_u`, giving `nuD`,
- `U_10=I_3`, `U_bar5=F` under the transversality/readout hypothesis.

But the locked C1 columns and conditional SU(5) fixture are not allowed to act
as selected source selectors.

## New Frontier

The next object is:

`SelectedMatterSlotGradingOrSectionRingReadout`.

It should come from one of:

- typed monad/Cech cohomology labels,
- line-bundle section-ring degree data,
- selected SU(5)/E6 matter-slot source identity,
- selected zero-mode operator-channel grading from the same HYM/Strominger branch.

Next artifact: `MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1`.
