# MTT Selected Anchoring-Parity Insertion Law or Independent Kinetic-Gram Derivation v1

## Central-normalization quotient theorem

Gauge ratios are invariant under a common scalar shift of the sector cost:

```text
C ~ C+cI,
W(C+cI)=exp(-tau*c)W(C),
K_a(C+cI)=exp(-tau*c)K_a(C).
```

Consequently the A78 relative response has the exactly equivalent representative

```text
delta_q P_colored-delta_e P_e
= delta_q P_colored+delta_e(I-P_e)-delta_e I.
```

The non-scalar representative on the right is positive semidefinite. The apparent negative charged-
lepton coefficient is therefore not evidence for a negative closure Hessian or an indefinite physical
metric; it is a coordinate in the quotient by the one common gauge normalization.

## Positive full-anchor defect Hessian

For every orthogonal projector `P`,

```text
D_P(x)=1/2 ||(I-P)x||^2,
Hess(D_P)=I-P >= 0,
ker Hess(D_P)=Ran(P).
```

Using the already selected charged-singlet support `P_e` and colored support `P_colored` gives

```text
D_anchor(x)=(delta_e/2)||(I-P_e)x||^2
            +(delta_q/2)||P_colored x||^2,
H_anchor=delta_e(I-P_e)+delta_q P_colored.
```

Within `span{I,P_colored,P_e}`, this is the unique positive central Hessian with the full-anchor
lane as kernel, universal non-`e` defect magnitude `delta_e`, and the additional partial-anchor
colored magnitude `delta_q`. ProtoSpinor supplies the full-versus-partial anchoring classification;
the existing MTT C1 program independently establishes projector-defect functionals on its own domain.

## Exact gauge execution

The old total relative cost has minimum `-3.0258346667557023`. Its canonical positive representative
adds `3.0258346667557023 I` and has spectrum

```text
[7.69304898011973, 7.69304898011973, 7.69304898011973, 3.0258346667557023, 0.0, 3.0258346667557023].
```

All three gauge rows acquire the same factor `0.29186234773364073`. Their ratios are unchanged:

```text
K/K2 = [1.9568437044693519, 1.0, 0.3098373950028702],
maximum residual to A78 = 4.441e-16.
```

No observed coupling was used and no continuous or discrete sign parameter was added.

## Corrected interpretation of A79

A79 remains valid for two literal positive corrections in one fixed representative. A80 does not
evade that theorem with an indefinite grading: it passes to the physically relevant quotient and
uses the positive projector complement. A literal `J_anchor` insertion, the unsupported `i^2` shortcut,
and an unselected analytic-torsion parity assignment are all unnecessary and are not promoted.

## Remaining physical theorem

The sign parameter is retired, but strict source promotion is not yet claimed. The next theorem is
`MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1`: identify the selected gauge-action second variation with `D_anchor` on the A77 domains and
prove that fermion, Higgs and inactive spectator blocks are common-scalar or cancel, with no extra
relative local quadratic term. Absolute `P_EW` normalization and modern validation remain downstream.
