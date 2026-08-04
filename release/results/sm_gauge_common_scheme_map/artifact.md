# MTT Selected Gauge-Action Coefficient to Common-Scheme Coupling Map and Prospective Validation v1

## Convention fixed without mixing prefactors

The existing product-triple theorem supplies the convention

```text
g_i^(-2) = c K_i,    c = 6 f0.
```

With `K2=1`, one common anchor fixes `c=g2^(-2)`. The electroweak/H-threshold prefactor
`P_EW=A_EW=0.0685013467625` is a different typed object; it is not substituted for
`c=2.3844493555491852`. This corrects the diagnostic `P_EW*K` product in A86: it is not an inverse-coupling
row.

## One-anchor reconstruction

At the frozen SMDR v1.3 scale and scheme, use only

```text
g2 = 0.6475986707537685
```

as the common normalization anchor. The selected shape predicts

```text
g1/g2 = 0.7148615365744185
g3/g2 = 1.7965242495219076
g1     = 0.46294338085858994
g3     = 1.1634267159672989
```

against SMDR central values `g1=0.46294351430107883` and `g3=1.1634274089369543`. The residuals are
`-1.3344248889213262e-07` and `-6.9296965543586e-07`. Propagating the actual SMDR covariance, including the shared
`g2` anchor and `g1=sqrt(5/3)gY`, gives marginal pulls `-0.0023926676772101038` and
`-0.00017140147765620138` sigma and correlated `chi2=5.725295700053512e-06` for two coordinates.

This is exact convention closure and a strong compatibility result. It is not independent evidence:
the gauge profile was known while the K chain was developed. At the corpus-action tier the structure
reduces three gauge coupling coordinates to one common continuous anchor, replacing two relative
coordinates with the selected K shape. It adds no parameter beyond the existing SM profile. The
primitive-core zero-anchor derivation remains open.

## Prospective test frozen

The two ratio predictions, scheme, scale, source hashes, covariance statistic, 95-percent rejection
threshold, and no-retuning rule are now registered. A genuinely new or previously unused common-scheme
determination can test the frozen branch. No such prospective validation is claimed here.

Next artifact: `MTT_Selected_GaugeRatioProspectiveValidationRegistration_or_PrimitiveKineticNormalizationSource_v1`.
