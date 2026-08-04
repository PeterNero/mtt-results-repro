# MTT Selected q79 Genus-Two Certified Thimble Period Execution v1

Status: `MTT_U6_Q79_ALL_THIMBLE_PERIODS_FLOATING_CONVERGED_HANDLE_LERAY_INTERVAL_PROMOTION_OPEN`

Supersession notice: A119 preserves all 90 primitive thimble integrations and
their independent floating rerun. The A118 `T K` table used the A117
up-to-sign vanishing representatives, so its 86 columns are retained only as
a reproducible convergence diagnostic. They are not final integral `H2`
columns. A119 performs the orientation-aware coupled thimble/handle assembly.

## A118 target

A117 proves that the selected genus-two Lefschetz fibration contributes a
saturated rank-86 closed-thimble lattice to `H2(C,Z)`.  A118 executes the
periods on that lattice.  It does not identify the remaining four handle and
two Leray-edge columns with transport paths, and it does not promote a
floating table to an interval theorem.

Let the eight A111 residue forms be ordered as

```text
E12, E13, E21, E23, E31, E32, H1, H2.
```

For the 90 A116 distinguished positive rays, A118 computes

```text
T in C^(8x90),
Pi_thimble = T K in C^(8x86),
```

where `K in Z^(90x86)` is the saturated A117 kernel basis.

## Period engine

Write the selected fiber as

```text
u^2=f_w(t),   deg_t(f_w)=6.
```

Five affine forms

```text
t^k dt/u,  k=0,...,4,
```

are propagated.  For every `k`, differentiation in the base is reduced by
solving

```text
P = Q f + (R' f - (1/2) R f'),
deg(R)<=5, deg(Q)<=4.
```

This is an `11x11` Gauss-Manin reduction.  The eight physical rows use only
the propagated periods of `dt/u` and `t dt/u`.  The reciprocal frozen charts
`s=1/t` and `s=1/(t+1)` initialize each vanishing cycle by endpoint-
desingularized Gauss-Legendre quadrature.  The endpoint transposition, not the
nearest pair on a finite meridian, fixes the colliding saved-root labels.

The reduction is equilibrated in double precision.  Whenever its equilibrated
condition exceeds `10^10`, the same linear system is solved with Arb/FLINT
complex balls and only the certified midpoint is passed to the ODE state.  In
the frozen production run this fallback was used 64 times; the largest
solution-ball radius was below `4.6e-41`.

## Desingularized selected segments

Direct Picard-Fuchs transport through a nearly nodal monomial basis can be
numerically stiff even when the geometric cycle is regular.  A118 therefore
uses direct desingularized cycle quadrature on 13 selected near-node segments.
The switches are chosen from two diagnostics only:

1. the colliding chord remains isolated from all four other roots along the
   segment;
2. the outer Gauss-Manin condition drops below the observed stiff regime.

No period value, Standard-Model datum, or target residual selects a switch.
The minimum sampled normalized noncolliding-root clearance over all selected
segments is

```text
1.0887981555925068 > 1.
```

Every ray also uses a direct 24-point desingularized endpoint-tail quadrature.
The minimum endpoint normalized clearance over all 90 rays is

```text
16.114573515221736.
```

The remaining outer segment is integrated by DOP853.  The final production
batch has maximum equilibrated reduction condition about `7.43e11`, maximum
recorded floating reduction residual about `1.36e-9`, and maximum 3,770 ODE
function evaluations for any one ray.

## Full execution

The frozen engine emits:

```text
90/90 primitive thimble columns,
720/720 primitive complex entries,
86/86 closed-thimble columns,
688/688 closed-thimble complex entries.
```

The closed table is assembled from the same primitive table by the exact
integer operation

```text
Pi_thimble = T K.
```

Thus no independent value is inserted into a closed-thimble column.

## Independent convergence execution

All 90 columns were rerun independently with

```text
epsilon: 1e-5 -> 3e-6,
working precision: 70 -> 100 decimal digits,
ODE rtol: 2e-10 -> 8e-11,
ODE atol: 2e-13 -> 8e-14.
```

All 720 primitive entries and all 688 induced closed-thimble entries were
compared.  The resulting maxima are

```text
primitive maximum absolute difference:          1.0066620340255023e-7
primitive maximum scale-normalized difference:  1.4942421223033762e-8
closed maximum absolute difference:              7.782167396491475e-7
closed maximum scale-normalized difference:      6.494312080665152e-9
```

No primitive column exceeds `1e-7` scale-normalized difference.  Two exceed
`1e-8`, and eleven exceed `1e-9`.  A separate three-axis representative audit
varies endpoint cutoff, precision/ODE tolerance, and local quadrature order.

These are convergence observations for a floating state integrator.  They are
not interval enclosures of the 1,408 complex output entries.

## Exact scope

A118 closes at its retained scope:

- execution of all 90 primitive thimble-period columns;
- exact integer assembly of the historical 86-column kernel diagnostic;
- a full 90-column independent floating convergence audit;
- the numerical-stiffness blocker on `a90`, `a01`, and `a02` without weakening
  the ODE tolerance;
- reproducible authority hashes for the engine, per-ray packets, and both
  period tables.

A118 does not promote the historical 86-column table to the final integral
surface basis; A119 supersedes that interpretation.

A118 does not close:

- interval enclosure of every period entry;
- the four punctured-torus handle periods;
- the two explicit Leray-edge lifts or their periods;
- the final integral `8x92` period table;
- the normal-function beta vector;
- an integral `Z^92` branch or separation theorem;
- a gerbe zero/no-go or full U6 strong-CP closure.

No measured Standard-Model value and no fitted parameter enters A118.

The standard algorithmic comparison remains the effective-homology and period
framework used by `lefschetz-family` and by Lairez,
Pichon-Pharabod, and Vanhove:

- https://github.com/ericpipha/lefschetz-family
- https://arxiv.org/abs/2306.05263

Next artifact: `MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1`.
