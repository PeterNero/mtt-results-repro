# Selected q79 Compact-H1 Thimble Orientation Gate

## Status

This theorem closes the orientation-selection rule used by the polygonal E32
main-interval engine. It does not close the remaining q79 weighted thimbles or
the fixed-carrier decision.

## Inputs

1. The A130/A131 selected q79 marking and the 90-thimble orientation
   synchronization packet.
2. A certified polygonal path in the relative homotopy class of the selected
   distinguished radial path.
3. The interval Gauss-Manin transport of the five period coordinates
   `dt/u,...,t^4 dt/u`.
4. The E32 residue row, which consumes only the first two holomorphic period
   coordinates.

The synchronization packet records

```text
compact_H1_holomorphic_rows_used_for_orientation = 2,
higher_meromorphic_rows_used_for_orientation = 0,
higher_meromorphic_rows_retain_puncture_lift_dependence = true.
```

## Theorem

Let `p=(p0,...,p4)` be the interval-transported base period center and let
`p_ref` be the synchronized floating reference. Define

```text
r_plus  = max(|p0-p0_ref|, |p1-p1_ref|),
r_minus = max(|p0+p0_ref|, |p1+p1_ref|).
```

If the larger residual exceeds 1000 times the smaller residual, the sign with
the smaller residual is the uniquely selected compact-H1 orientation. The
coordinates `p2,p3,p4` are retained as puncture-lift diagnostics but cannot
change this sign.

## Proof

The first two rows are the periods of a basis of holomorphic one-forms on the
compact genus-two fiber. The period-lattice map embeds compact integral `H1`
into their two complex periods, so their synchronized vector identifies the
oriented compact cycle. The three higher meromorphic rows depend on the chosen
puncture-at-infinity lift; changing a polygonal representative can change those
coordinates without changing the compact cycle.

The selected E32 residue map has nonzero period columns only in positions zero
and one. Therefore its transported integral depends on the compact cycle and
its orientation, not on the three lift-dependent coordinates. Selecting a sign
with all five rows would impose a stronger, incorrectly typed relative-lift
condition that neither compact `H1` nor E32 requires.

## d030 Execution

For `d030/selected_034` on route `(0.25,0.02,0.86)`:

```text
selected compact-H1 sign                  = -1
selected compact-H1 residual              = 1.922947248965649e-10
opposite compact-H1 residual              = 0.25870010053171594
higher meromorphic lift diagnostic        = 11.520484471488459
main interval radius                      = 6.576746775026099e-8
full interval radius                      = 1.4630221993883199e-6
floating center contained                 = true
A134 fallback met                         = true
```

Thus the compact-H1 sign is separated by more than the required factor 1000,
while the large higher-row diagnostic correctly records the different
puncture-lift representative. This closes d030 without a manual sign or an
observed Standard Model input.

## Boundary

This theorem selects orientation, not period magnitude or the final weighted
carrier. It does not identify the three meromorphic coordinates across
different puncture lifts, and it does not make them compact-H1 observables.
