# QFT02 Gauge-Compatible Finite BV Regulator Assessment

Date: 2026-07-24

## Decision

The existing finite HYM, finite spectral-triple, A57 and finite-QME objects
must not be promoted to the missing q79 spacetime regulator. Their domains are
internal or finite algebraic. The exact tensor-rank theorem now excludes that
promotion.

The best current bridge is a Hodge-spectral construction. One selected
positive self-adjoint compact-resolvent operator

```text
Delta_BV=d_BV d_BV^dagger+d_BV^dagger d_BV
```

would emit the complete nested finite family

```text
C_Lambda=1_[0,Lambda](Delta_BV)
```

with no independent per-mode choices.

## What Advanced

Before this pass, `B.QFT.02` named a selected regulator and continuum limit as
a general requirement.

After this pass:

1. the exact operator type and domain are specified;
2. finite rank, nesting, BRST compatibility, strong convergence and the
   contracting homotopy follow automatically from one operator theorem;
3. the previous q79 physical quartet projector is identified exactly as a
   zero-mode Hodge projector;
4. internal-projector promotion is ruled out;
5. the ultraviolet Hessian elimination mechanism is executed exactly by a
   Schur complement;
6. the distinction between a finite QME seed and a physical QME-preserving
   regulator family is explicit.

This is a frontier reduction, not nonperturbative completion.

## Why A57 Is Not Yet Enough

A57 supplies gauge, ghost, Weyl and Higgs fluctuation slots and finite
internal heat-index data. The q79 QFT composition supplies Lorentzian
normally hyperbolic or Dirac principal symbols. Neither selects:

```text
a compact spatial or Euclidean domain,
BRST-compatible elliptic boundary conditions,
a positive self-adjoint compact-resolvent Delta_BV,
a nested external spectral family natural under region maps,
an ultraviolet integration cycle and determinant orientation.
```

Those are exactly the missing clauses.

## Recommended Next Attack

Construct the package first on one bounded `H1=0` q79 Cauchy domain already
used by the local physical-state theorem.

The sharp next target is:

```text
q79 Local Gauge-Fixed BV Hodge Laplacian and
BRST-Compatible Elliptic Boundary-Domain Theorem.
```

It should:

1. write the full free linearized BV differential, including the
   Koszul-Tate kinetic block;
2. define its Hilbert adjoint from the selected q79 spatial metric and bundle
   metrics;
3. prove the mixed gauge, ghost, Higgs and fermion boundary conditions make
   the squared block strongly elliptic and self-adjoint;
4. prove compact resolvent and gauge/BV-pairing equivariance;
5. emit `C_Lambda`, `G_Lambda` and the local finite BV pushforward data;
6. audit compatibility when one bounded domain embeds in another.

If domain naturality fails for sharp spectral projectors, the honest fallback
is a heat-kernel/functional-RG family at the formal effective-action tier.
That fallback is not finite rank and should be labeled separately.

## Claim Boundary

`B.QFT.02` remains open. The new result closes the finite-regulator criterion
and rules out a false shortcut. It does not close:

```text
the selected q79 external operator/domain;
the physical regulated interacting QME;
regulator removal;
the fixed-coupling interacting C*-net;
the selected global interacting state.
```

New physical continuous parameters: `0`.

New fits or observed inputs: `0`.
