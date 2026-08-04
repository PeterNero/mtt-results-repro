# MTT Selected q79 E32 Clearance-Ranked Second Full Interval v1

## A137 result

A137 closes the second complete selected E32 thimble interval. The chosen row
is `d061 / selected_088`, whose exact height-four coefficient is `-3`. Its
node and local Weierstrass/Hensel factor are certified, the endpoint tail uses
384 desingularized interval segments, and the main
transport uses a six-dimensional augmented fundamental frame on a segmented
copy of the already-certified radial homotopy class.

```text
tail radius      = 1.450424708338005e-06
main radius      = 7.758847945657284e-06
full ball radius = 1.242309284066323e-05
A134 fallback    = 2.308660192880193e-05
fallback margin  = 1.066350908813869e-05
```

The independent A131 floating value lies inside the full ball and is not used
as an error bound. Together with A136, 2 of 71 selected thimbles and L1 weight
5 of 123 are now interval-closed. After charging both exact coefficients, the
remaining strict weighted budget is `0.002773556839845063`.

## Batch lesson

The useful scaling policy is now explicit: enforce the local defect bound at
every Taylor step, but apply the E32 radius budget to the final transported
coordinate. Intermediate fundamental-frame radii need not be monotone. The
`d047` row separately has an exact node/Hensel factor and endpoint tail, but
its main ray remains a hard checkpointed execution target. This diagnostic is
not counted as a third closed thimble.

## Still open

- 69 full E32 thimble intervals, with L1 weight 118;
- the z-chart interval adapter;
- the exact weighted 71-thimble sum and frozen-carrier separation decision;
- the later covariant PGL3 continuation if the frozen carrier survives.
