# MTT Selected HiggsRouteAFormulaDerivativeEngines or OfficialLikelihoodDecision v1

Status: `MTT_SELECTED_HIGGSROUTEAFORMULADERIVATIVEENGINES_OR_OFFICIALLIKELIHOODDECISION_BUILT_OFFICIAL_LIKELIHOOD_RETIRED_ROUTEA_PRIMARY`.

This artifact makes the Higgs precision-route decision after the imported
profile replay.

The official route is retired for now because no official public
machine-readable LHCHXSWG/LHC-HCG likelihood or profile workspace matching the
repo ten-decay Higgs basis has been imported. The retirement is reversible if a
versioned official RooWorkspace/profile-likelihood artifact is found later.

The published covariance replay remains accepted as an SM-parity correlated
profile. The primary remaining route is now route-A: differentiate the actual
partial-width formula engines for all ten Higgs rows, then compare the resulting
covariance/profile against the imported replay without using observed values to
select source structure.
