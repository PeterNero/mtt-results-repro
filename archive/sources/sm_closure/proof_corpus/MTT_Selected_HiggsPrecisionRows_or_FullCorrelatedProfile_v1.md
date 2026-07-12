# MTT Selected HiggsPrecisionRows or FullCorrelatedProfile v1

Status: `MTT_SELECTED_HIGGSPRECISIONROWS_OR_FULLCORRELATEDPROFILE_BUILT_PROMOTION_GATE_VALUES_OPEN`.

This artifact builds the promotion gate for all ten Higgs partial-width rows and
the readiness matrix for the full correlated Higgs profile. It promotes zero
rows to precision. That is the point: the repo now knows exactly what must be
filled before the total width or branching-ratio replay can be promoted.

The near-term fork is now explicit: either fill accepted precision formula or
import values row by row, or import/build a full correlated Higgs profile
convention. No benchmark value is used as a source selector.
