# MTT Selected Baseline-Cost Multiplicity Source and Noncentral-Spectator Exclusion v1

## Later-authority correction

A69's sevenfold factor is no longer merely a candidate. The q79 repository now has a closed
Fu-Yau/Mukai charge-sector certificate for `Z7`, and A77 proves that primitive `q7=2` generates the
full seven-character orbit. The selected family carrier is the separate common-circle `Z3`. A76's
equivariance no-go remains essential: the rank-three Lens-`Z4` augmentation is **not** used as the
family carrier. The Lens input instead supplies A77's selected quarter-turn and its conjugate as the
opposed `+1/-1` orientation pair, with A81 supplying the anchor-to-complement map.

## Shared-circle multiplicity theorem

The selected ambient carrier is

```text
Z1344 ~= Z64 x Z7 x Z3.
```

Its family/odd marginal is the minimal common quotient `Z21 ~= Z3 x Z7`. In character coordinates,
the dual `Z21` action permutes all 21 minimal projectors transitively. An invariant positive trace
therefore gives equal weight to every character. The unnormalized regular trace consequently counts
the family and q marginals as exactly `3` and `7`; there is no relative `Z3`/`Z7` weight knob once
this common carrier is selected.

## Exact parent functional

On the selected structural carriers define the finite positive quadratic functional

```text
S_base = (1/2) sum_(g in Z3) ||diag(1,-1)e_g||^2
       + sum_(r in Z7) min_(a_r+c_r=delta_r) (||a_r||^2+||c_r||^2),
||delta_r||_color^2 = tau_3(q^* sum_a T_a^*T_a q).
```

The opposed-loop trace gives

```text
c_e = (1/2)*3*(1^2+(-1)^2) = 3.
```

Two equivalent hidden color-completion channels give the Schur minimum `delta^2/2`, while
`sum_a T_a^*T_a=(4/3)I_3` in the selected `SU3` fundamental normalization. Hence

```text
c_q = 7*(1/2)*(4/3) = 14/3.
```

This is an explicit zero-parameter finite parent functional, not a fit. Adding A81's selected
positive defect reproduces A80's full operator with residual `8.882e-16` and
the frozen ratio candidate `[1.9568437044693519, 1.0, 0.3098373950028702]`.

## Spectator theorem and exact boundary

For diagonal sector weights respecting the declared classes

```text
{Q,u,d}, {e}, {L,N},
```

the full invariant space has dimension three and is exactly

```text
span{I,P_colored,P_e}.
```

Modulo common identity it has dimension two, so there is no additional diagonal spectator direction
inside this class. This does not exclude sector-dependent family matrices, non-diagonal fluctuation
blocks, fermion/Higgs loop terms, or A75's rank-two relative local-counterterm space.

The remaining proof is now one operator-identification theorem, not two unexplained numbers: prove
that the selected MTT closure Hessian is the displayed shared-circle parent functional and that its
second variation restricts to A65's gauge-zero-mode `W_kin`, with the remaining blocks/counterterms
neutral or absent. The central-circle paper itself labels its universality discussion as structural
synthesis, so this identification is not silently assumed. Strict gauge values accepted here: zero.

Next artifact: `MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1`.
