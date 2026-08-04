# MTT Selected q79 E32 Thimble Hensel Seed and First Full Interval v1

## What A136 closes

For the selected `d004 / selected_009` thimble, A136 replaces the open A135
value placeholders by an interval-certified local object. Interval Newton
isolates the nodal parameter and double root at radius
`1.414e-80`. The nodal sextic
admits a monic quadratic times quartic factor with

```text
|H(r)| > 163.819804908858,
|det J_Hensel| > 26836.9284803764.
```

The quantitative Taylor-Hensel disk has residual at most
`4.992e-74`
and contraction bound
`4.021e-69`. It gives a
rigorous desingularized endpoint-tail ball. The ordinary segment is certified
in a six-dimensional homogeneous augmented fundamental frame, which keeps the
`E32` integral error correlated with the five period coordinates.

The reproducible main command used for this packet is:

```text
python scripts/certify_q79_selected_alignment_single_E32_thimble_main_interval.py --distinguished-index 4 --order 48 --maximum-lift-correction 1e-8 --target-main-radius 1e-5 --initial-radius-allowance 1e-6
```

The final result is

```text
E32(d004) in ball(
  0.61634458064238262
  + 1.58329472957163 i,
  1.4359496802285323e-05
).
```

The independent A131 floating center differs by only
`6.900e-09` and lies inside this ball, but it is never used as
an error bound. The A134 sufficient per-unit fallback is
`2.3086601928801926e-05`,
so the first full interval passes with margin
`8.7271051265166037e-06`.

## Exact frontier

This is the first complete numerical instantiation of A135, not the weighted
closure. One of 71 selected thimbles (L1 weight 2 of 123) is closed. The
remaining budget after charging both its radius and its displacement from the
A131 reference center is `0.0028109192430079829`. The next task is to add a
chart parameter to the validated engine and execute the same certificate for
29 remaining y-chart and 41 z-chart thimbles.

No observed Standard Model value is used.
