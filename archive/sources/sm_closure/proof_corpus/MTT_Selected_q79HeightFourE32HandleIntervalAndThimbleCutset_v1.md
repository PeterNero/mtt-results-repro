# MTT Selected q79 Height-Four E32 Handle Interval and Thimble Cutset v1

## Result

A134 rigorously evaluates the handle part of the A132 height-four carrier in
the sole separating row selected by A133. The exact primitive identity is

```text
-A:a1 + A:a2 + A:b2 = A:(sigma3 + sigma4).
```

The marked base cycles are computed as direct algebraic-cut integrals. The
selected root-label cuts are `(3,4)` for `sigma3` and `(1,4)` for `sigma4`;
their five-period centers agree with the independently synchronized A131
marking to at most `1.690e-10`.
Validated homogeneous Gauss-Manin transport around the full A handle gives

```text
H_E32 = -0.11453011578466389
          +1.825133847274548 i
radius <= 0.00049847272443570394.
```

Its center differs from the independent A131 handle value by only
`2.500e-10`. This is a rigorous interval result, not a
two-precision convergence proxy.

## Remaining exact cutset

The A133 total period budget is `0.003338125011653557`. Charging both the
rigorous handle radius and its displacement from the A131 reference leaves

```text
0.0028396520372426367
```

for the weighted 71-thimble `E32` combination. The chain has primitive
coefficient L1 norm `123`. Certifying the weighted sum directly is
sufficient; 71 independent theorem packets are not logically required. A
uniform per-unit bound of `2.3086601928801926e-05` would also
suffice, but is only a fallback strategy.

## Scope

A134 closes the handle interval and fixes the numerical target for the last
period component. It does not yet claim the weighted thimble interval,
frozen-carrier separation, or a covariant PGL3 zero. No observed Standard
Model value is used.
