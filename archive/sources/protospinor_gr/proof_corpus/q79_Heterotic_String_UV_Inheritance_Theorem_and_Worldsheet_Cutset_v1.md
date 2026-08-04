# q79 Heterotic String UV Inheritance Theorem and Worldsheet Cutset v1

Date: 2026-07-16

## Result

The surviving primary MTT route to perturbative ultraviolet completion is not
permanent Gaussian damping of a four-dimensional graviton. It is inheritance
from an exact heterotic string background on the selected q79/F Fu-Yau branch.

The alternatives are now separated exactly:

- local Einstein gravity has the nonzero two-loop `Riemann^3` divergence;
- finite internal projection does not change four-dimensional loop momentum
  power counting;
- a positive massless Stieltjes propagator cannot have permanent Gaussian
  decay;
- asymptotic safety lacks an exact selected fixed functional in the corpus;
- the finite product spectral action lacks its full remainder, measure, and
  continuum theorem.

The q79 string route is compatible with every one of those boundaries and has
real same-branch support: the time-oriented `q=79/F` representative, Fu-Yau
Mukai charge sector, Green-Schwarz Bianchi data, and the curvature-level visible
Green-Schwarz row are computed.

## Exact universal checks

The critical heterotic central charges cancel:

```text
c_L = 10 + 16 - 26 = 0,
c_R = 10 + 10/2 - 15 = 0.
```

For the standard torus modular fundamental domain,

```text
|Re tau| <= 1/2,
|tau| >= 1,
Im tau >= sqrt(3)/2 = 0.866025403784439.
```

Thus the `tau_2 -> 0` point-particle UV region is absent once the actual
partition function is modular invariant. The remaining `tau_2 -> infinity`
boundary is a degeneration/factorization or infrared region, not a local UV
counterterm region.

## Conditional inheritance theorem

Assume one same-source q79/F background supplies an exact anomaly-free modular
heterotic `(0,2)` SCFT, a tachyon-free GSO projection, factorization, and the
heterotic quantum BV master action, with tadpoles and infrared degenerations
treated by the standard vacuum-shift prescription. Then every fixed-genus,
fixed-multiplicity q79 heterotic amplitude is free of local ultraviolet
divergences.

This is the correct replacement for the invalid SPT all-loop theorem. It does
not damp the physical massless graviton propagator. Ultraviolet softness comes
from integration over worldsheet moduli modulo modular equivalence.

## Current q79 readiness: 5/12 available, 2 partial

Available rows:

1. time-oriented q79/F target branch;
2. Fu-Yau/Mukai charge and Green-Schwarz Bianchi sector;
3. visible curvature-level Green-Schwarz cancellation;
4. universal critical heterotic central-charge cancellation;
5. q79 low-energy GR and quantum-EFT limit.

W8 is now partially constructed by an explicit smooth degree-two K3 in the
splitting-conic family. Its isomorphic `U(1)^2` incidence GLSM has exact
Calabi-Yau charge sums, paired `(2,2)` gauge-anomaly cancellation and the
`E/J` identity. Its divisor ring exposes the primitive Fu-Yau source
`delta=H-L`, with `H.delta=0` and `delta^2=-4`, while the second marked shared
circle remains untwisted. This retains the exact K3-reference allocation
`9+11+4=24`.

The local worldsheet Green-Schwarz row is now exact as well. In the `(H,L)`
basis the one-loop anomaly is

```text
A = [[ 2,-2],
     [-2, 2]] = 2 delta delta^T.
```

It is cancelled over the integers by `M1=(1,-1)`, `N1=(4,-4)` and
`k1^2=2`; the shared second circle has `M2=N2=0`. An anomaly-equivalent
rank-12 Fermi monad with `c1=0,c2=20` exists. It is not the physical
`SU(3) x SU(9)` split: the even Picard lattice proves that line-bundle
complexes cannot separately emit odd `c2=9,11`.

There is a second exact obstruction. A standard compact TLSM Fermi bundle is
pulled back from K3, so its third Chern class vanishes. It cannot realize the
already-constructed topological non-pullback visible bundle with `c3=+/-6`.
The new shared-circle clutching calculation strengthens the positive side:
`H.delta=0` supplies a primitive Gysin lift `Hhat`, and independent degree-three
and degree-five clutching channels give a smooth `SU(3)` candidate with
`c2=9(Hhat cup t)` and `c3=+/-6`. The instanton and chirality targets are
therefore simultaneously admissible topologically. The mixed class has the
closed `(2,2)` representative `(i/2) Theta wedge conjugate(Theta) wedge H`,
so the target also passes the selected Fu-Yau Hodge-type test; holomorphic
bundle existence, HYM, and
the differential total-space Bianchi equation remain open.
The remaining physical bundle must therefore come from the same-carrier
twisted spectral/Fourier-Mukai route or a genuinely non-Abelian fibered
current algebra. The first route is no longer at its old A127 cutset: all 90
continuous root tubes, both handles, the global surface relation, and the exact
92-column integral `H2` presentation are closed. The floating `8 x 92` period
table and effective `Z^90` quotient are closed, and A151 has certified 16 of 71
weighted `E32` intervals with L1 weight 36 of 123. The covariant z-chart
adapter and its first native row are closed. The remaining 55 intervals,
weighted branch decision, inverse-gerbe sheaf, holomorphic/HYM structure,
differential Bianchi representative, global GSO currents, and exact IR `(0,2)`
SCFT remain open.

The modular row W9 is also partially constructed. The selected `F_3^2` gerbe
cocycle gives an exact discrete-torsion phase on all 81 torus twist sectors,
and the modular `S,T` action reduces those sectors to seven seed character
blocks with orbit sizes `1,8,8,8,8,24,24`. Its selected twisted group algebra
is exactly `Mat_3(C)`, with one three-dimensional projective module and finite
topological torus index one. The seven seed stabilizers and modular induction
are exact; finite covariance has rank 74 and nullity seven, so it cannot reduce
the analytic seed count further. The full oscillator, gauge-current,
spin-structure, `Gamma(3)` multiplier, GSO, and factorization characters are
not yet supplied.

The decisive missing object is not another four-dimensional Hessian. It is an
exact q79 heterotic worldsheet packet containing:

1. the global Deligne gerbe and Freed-Witten restrictions on the full visible
   cycle set;
2. the physical non-pullback visible/hidden Fermi bundle beyond the now-closed
   aggregate local anomaly, followed by its differential Bianchi row and exact
   IR SCFT;
3. the seven q79 seed characters, their modular mixing/GSO completion, and
   factorization data;
4. q79-specific string-field vertices satisfying the quantum BV master equation;
5. tadpole/vacuum-shift and massless soft/IR control.

The current flux paper explicitly works only to first order in `alpha'`, and
the current string paper proves beta-function vanishing only to a controlled
order while invoking modular invariance only in the CY/toroidal corner. Those
statements cannot be promoted to an exact q79 CFT.

## Nonperturbative boundary

Fixed-genus UV finiteness does not prove convergence of the sum over genera and
does not provide a nonperturbative definition at finite string coupling. Even
after the worldsheet packet closes, all-genus summability or a genuine
nonperturbative completion remains a separate final gate.

## Primary mathematical sources

- [Superstring Perturbation Theory Revisited](https://arxiv.org/abs/1209.5461)
- [Ultraviolet and Infrared Divergences in Superstring Theory](https://arxiv.org/abs/1512.00026)
- [BV Master Action for Heterotic and Type II String Field Theories](https://arxiv.org/abs/1508.05387)
- [Linear Models for Flux Vacua](https://arxiv.org/abs/hep-th/0611084)
- [Anomaly Cancellation and Smooth Non-Kahler Solutions](https://arxiv.org/abs/hep-th/0604137)
