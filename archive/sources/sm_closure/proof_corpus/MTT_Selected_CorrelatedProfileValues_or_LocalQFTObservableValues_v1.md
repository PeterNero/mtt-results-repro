# MTT Selected CorrelatedProfileValues or LocalQFTObservableValues v1

Status: `MTT_SELECTED_CORRELATEDPROFILEVALUES_OR_LOCALQFTOBSERVABLEVALUES_BUILT_CORRELATION_ENVELOPE_QFT_VALUES_OPEN`.

This artifact corrects the correlated-profile basis: `g1_GUT(Mt)` is exactly
`sqrt(5/3) gY(Mt)`, so it must not be double-counted when covariance is used.

On the compressed basis it builds an equicorrelation stress envelope over the
measured inputs. The current weak-scale boundary replay passes this coarse
correlation envelope, but the envelope is not a published or reconstructed
profile likelihood.

The local-QFT observable value gate is also made explicit. The functor interface
exists, but concrete propagator/correlator/S-matrix or low-energy observable
rows remain open.
