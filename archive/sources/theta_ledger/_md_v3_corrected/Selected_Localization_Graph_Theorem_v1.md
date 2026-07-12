---
abstract: |
  We formulate the next proof gate after the selected overlap-kernel source
  clues: the selected localization graph theorem.  The theorem says that once
  MTT supplies a fixed theta/lens/nil/proto-spinor localization operator with
  isolated three-family spectral clusters, the zero-mode localization graph
  and finite overlap channel sets are canonical.  This closes the
  graph-construction schema needed by the no-proxy overlap-kernel certificate,
  while leaving the concrete spectral computation of the actual graph open.
author:
- Peter Nero
date: June 2026
title: |
  Selected Localization Graph Theorem for the Overlap-Kernel Program
---

# Purpose

The selected overlap-kernel certificate requires:

```text
G_loc,
Gamma_x[i,j],
zero-mode bases,
kinetic metrics.
```

The corpus source clues identify `G_loc` as the allowed localization graph of
zero modes.  This note defines how `G_loc` should be selected by MTT rather
than chosen entry by entry.

# Selected Localization Operator

Let the selected branch supply a sectorwise proto-spinor/localization operator:

```text
L_loc,x =
  L_theta,x
  + L_lens,x
  + L_nil,x
  + L_Wilson,x
  + J_x
```

on each matter sector:

```text
x in {Q,u,d,L,e,nu,Hu,Hd}.
```

The terms mean:

```text
L_theta,x    shared-circle/theta closure contribution
L_lens,x     lens localization contribution
L_nil,x      nil-survivor/coherence contribution
L_Wilson,x   finite Wilson/deck character contribution
J_x          closure-cost or anchor/cancellation penalty
```

This is not an additional fit.  In a closed proof every term must be derived
from the same selected source map `Sigma_MTT`.

# Family Projector

Assume `L_loc,x` is self-adjoint or sectorially reducible to a self-adjoint
positive operator on the retained coherent sector.  Assume it has an isolated
three-dimensional family cluster:

```text
spec(L_loc,x) cap Omega_x = {lambda_x,1, lambda_x,2, lambda_x,3},
dim Ran P_x = 3,
```

where:

```text
P_x = (1/2 pi i) integral_{partial Omega_x}
        (z - L_loc,x)^(-1) dz.
```

Choose the normalized basis:

```text
psi_x,i,  i=1,2,3,
```

by diagonalizing the commuting selected label operators:

```text
theta label,
lens label,
nil label,
finite CP/family label,
anchor/cancellation label.
```

If degeneracies remain, they must be resolved by a stated MTT symmetry or kept
as exact family symmetry rather than fitted.

# Localization Graph

Define vertices:

```text
V(G_loc) = {(x,i) : x matter or Higgs sector, i family/mode index}.
```

Define admissible overlap channels:

```text
gamma in Gamma_x[i,j]
```

when all of the following hold:

```text
1. psi_left,i, psi_right,j, and Higgs mode h_x have common selected support
   or an allowed instanton/exceptional-cycle bridge;
2. the pairwise line-bundle product is trivial on the trilinear channel;
3. the finite CP weight w_gamma is defined in Z448;
4. the nil-survivor projector does not kill the channel;
5. anchor/cancellation constraints are satisfied;
6. anomaly/tadpole/global consistency constraints are satisfied.
```

Then `G_loc` is the graph whose edges/hyperedges are the nonempty selected
channel sets.

# Theorem: Canonical Localization Graph

If the selected source map `Sigma_MTT` fixes all operators in `L_loc,x`, the
Riesz contours `Omega_x`, the commuting label operators, and the global
bundle/flux constraints before comparison with observed flavor data, then
`G_loc` and all finite channel sets `Gamma_x[i,j]` are canonical outputs of
MTT.

Proof.  The family projectors `P_x` are Riesz projectors of fixed operators on
fixed contours, hence their ranges are invariantly determined.  The basis is
then fixed up to exact degeneracies by the commuting selected labels.  The
channel admissibility conditions are all predicates on the selected supports,
line bundles, CP weights, nil/coherence projectors, anchor/cancellation data,
and global consistency constraints.  Therefore the resulting graph and finite
channel sets are determined by `Sigma_MTT`.  No matrix entry or mixing angle
is used in their construction.

# Corollary: No Entry-Wise Localization Fitting

If `G_loc` is produced by the theorem above, then distances, allowed channels,
and CP weights may not be changed independently for individual Yukawa matrix
entries.

Any such change modifies `Sigma_MTT` itself and must be counted as a different
branch, not as a parameter choice inside one closed theory.

# Relation to Proto-Spinor Simulation

A proto-spinor simulation can approximate this construction by evolving
particle states:

```text
(theta, lens, nil, J, coherence, anchor, cancellation, CP weight, family)
```

under a discrete or continuous version of `L_loc`.  Stable particle-like
behavior in such a simulation is a useful check that the rules are coherent.
The proof gate, however, is the spectral theorem above: the simulation becomes
proof-relevant only if its update kernel is an approximation to the selected
operator `L_loc`.

# Status

```text
localization graph construction schema          PROVED
no entry-wise localization fitting              PROVED
actual L_loc,x from MTT geometry                OPEN
three-family spectral clusters                  OPEN
zero-mode basis computation                     OPEN
finite channel computation                      OPEN
kinetic metrics                                 OPEN
```

# Next Computation

The next concrete computation is:

```text
construct a candidate L_loc,x
from theta/lens/nil/shared-circle/proto-spinor data,
compute its first three retained eigenmodes,
and extract G_loc plus Gamma_u/Gamma_d.
```

This is the first place where a particle simulation and the analytic proof
program can meet.

