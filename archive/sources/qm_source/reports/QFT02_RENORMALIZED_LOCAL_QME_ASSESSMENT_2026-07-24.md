# B.QFT.02 Renormalized Local QME Assessment

Date: 2026-07-24

## Verdict

The selected q79 Standard-Model field stack now has a formal renormalized
interacting BV algebra on each declared on-shell background chart.

The complete four-dimensional power-counting local gauge-anomaly vector is
computed directly from the exact A46 three-family carrier:

\[
(A_{333},A_{33Y},A_{22Y},A_{YYY},A_{\mathrm{grav}\,\mathrm{grav}\,Y})
=(0,0,0,0,0).
\]

The result holds already per family. Standard local BRST cohomology therefore
makes any remaining QME breaking BRST exact and removable by finite local
counterterms. The Adler-Bardeen theorem supplies an all-orders formal
subtraction scheme.

The executable certificate passes 62 of 62 checks.

## New closures

- Epstein-Glaser time-ordered products on the prior microcausal algebra.
- Stueckelberg-Petermann renormalization freedom.
- The formal Bogoliubov interacting algebra.
- The complete power-counting ghost-number-one gauge-anomaly basis.
- Exact zero of every nontrivial local coefficient.
- An all-orders formal renormalized-QME scheme.
- Nilpotent interacting quantum-BV differential.
- Ghost-number-zero interacting observable cohomology.
- Formal gauge-fixing independence.
- Vanishing global spin gauge-anomaly bordism obstruction for the faithful
  `/Z6` quotient.

## Exact arithmetic

In integer hypercharge normalization \(q_6=6Y\), the six left-Weyl rows are:

```text
Q, u^c, d^c, L, e^c, N^c
q6 = 1, -4, 2, -3, 6, 0.
```

Their per-family coefficient rows sum to:

```text
SU3^3       :  2 - 1 - 1                 = 0
SU3^2 U1    :  2 - 4 + 2                 = 0
SU2^2 U1    :  3 - 3                     = 0
U1^3        :  6 - 192 + 24 - 54 + 216 = 0
grav^2 U1   :  6 - 12 + 6 - 6 + 6      = 0
```

All rows also satisfy

\[
2t_3+3p_2+q_6=0\pmod 6,
\]

so the calculation is on the actual faithful quotient rather than only its
Lie algebra.

There are four weak doublets per family and 12 in total.

## Global refinement

For

\[
G=(SU(3)\times SU(2)\times U(1))/\mathbb Z_6,
\]

the established spin-bordism result is

\[
\Omega^{\mathrm{Spin}}_5(BG)=0.
\]

Together with the local zero vector, this removes the residual spin global
gauge-anomaly obstruction. It does not itself choose a preferred determinant
phase convention.

## Objective meaning

This is genuine progress from a free QFT platform to a formal interacting,
renormalized, anomaly-free local gauge theory. It uses no measured masses,
couplings, or mixings and adds no physical parameter.

It is also standard-model structural consistency, not a new numerical
prediction. MTT-specific content is the composition with the already selected
q79 spacetime, faithful global group, and finite chiral carrier.

## Remaining frontier

`B.QFT.02` remains open because its physical exit also requires:

1. positive interacting physical states or representations;
2. selected numerical RG evolution and matching;
3. uncertainty transport and observable comparison;
4. any required infrared scattering limit;
5. nonperturbative completion.

`B.ACTION.01` remains open because the upper q79 action and vacuum source are
not fully selected.

The next high-value target is therefore not another anomaly table. It is a
positive-state construction for the interacting BRST cohomology, or selected
RG/matching if the action-value source becomes available first.
