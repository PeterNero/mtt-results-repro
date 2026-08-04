# MTT Selected Gauge-Inserted Heat Supertrace Second Variation or Common-Scheme Threshold Payload v1

## Exact Finite-Carrier Execution

All gradings already selected on the explicit `96`-dimensional finite carrier were executed against
the common finite base determinant `L=14.6008251660996`. In `(U1_GUT,SU2,SU3)` order:

```text
ordinary trace                    = [87.6049509965973, 87.6049509965973, 87.6049509965973]
KO6 chiral supertrace             = [0.0, 0.0, 0.0]
uniform fermion-parity supertrace = [-87.6049509965973, -87.6049509965973, -87.6049509965973]
```

The ordinary trace is universal. The KO6 trace vanishes because `J_F` maps every particle state to
an antiparticle state with opposite chirality but the same squared gauge charge. Uniform fermion
parity merely reverses the universal sign. Every available finite-carrier grading therefore has
relative gauge rank zero.

## Consequence

KO6 chirality is not statistics grading. The `96`-state carrier contains fermions and their charge
conjugates, but not the gauge one-form, Faddeev-Popov ghost and Higgs fluctuation Hessians required by
a one-loop effective action. Regrading this carrier cannot produce the non-universal threshold rows.

## Constructed Missing Payload

The machine-readable template now asks for the second variation of one selected gauge-fixed action:
gauge one-forms with `+1/2` determinant weight, ghosts with `-1`, fermion determinants, and Higgs
scalar Hessians. All blocks must share the background, BRST operator, zero-mode policy, regulator,
scale and scheme. Its signed heat supertrace must be checked against the non-universal one-loop index
vector without importing that vector as an MTT source.

Next artifact: `MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1`.
