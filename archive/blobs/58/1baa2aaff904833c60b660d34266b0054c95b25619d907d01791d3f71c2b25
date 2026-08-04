# MTT q79 Height-Four Reverse-Main Preconditioning Frontier (A380B) v1

The A128 outbound root-tube leg and the A380 main path are the same geometric
line after the exact coordinate change

\[
w=0.25+0.25i+i\,p.
\]

This makes reverse transport from the smooth base toward a source-derived
cutoff a legitimate numerical preconditioning candidate. A128 supplies the
continuous root tubes, the interval-certified braid, and the resulting compact
`H_1` vanishing-cycle class.

It does **not**, by itself, supply the full five-coordinate affine period lift.
The first two period rows are compact-homology observables, whereas `p2,p3,p4`
retain the puncture-at-infinity lift described by the compact-H1 orientation
gate. For `d030`, direct base-cut reconstruction from the A128 compact class
reproduces `p0,p1` of the validated main endpoint, while the largest difference
among `p2,p3,p4` is about `11.53`. This is expected puncture-lift dependence,
not a failure of the root-tube theorem.

Therefore a rigorous reverse-main implementation must initialize its five
coordinates from one of these same-source authorities:

1. the validated full affine endpoint enclosure of the ordinary A380 carrier;
2. an independently selected affine/puncture-lift theorem for that thimble; or
3. a direct affine cycle quadrature carrying the selected puncture lift.

Promoting the four-component A128 class directly to a five-component lift is
forbidden. The current source-derived far-cut route avoids this issue and is
numerically preferred while it clears the full Frobenius budgets. Reverse
preconditioning remains a certified backup once one of the three affine
initializers above is attached.

## d082 factor-order conditioning

At the source-derived cutoff `epsilon=10^-3`, the `d082` quantitative Hensel
disk is geometrically valid but numerically nonmonotone in Taylor order. Direct
Arb preflight gives:

- order 10: contraction `< 0.43`;
- order 12: contraction `< 7.3e-3`;
- order 24: contraction `< 1.6e-13`;
- order 32: the coefficient inverse is noncontractive.

The production source-route tail order is therefore fixed to `24`. Raising the
formal order past the conditioning optimum is not a strengthening and must not
be used to reopen this target.
