# MTT Selected Alpha1 Tangent Promotion or Sector-Routing Normalization Theorem v1

Status: `MTT_SELECTED_ALPHA1_TANGENT_PROMOTION_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN`

## Context

Let `eta_00^unit` be the selected normalized Ext representative and set

```text
rho = |eta_00^unit|^2.
```

Let `u` be the zero-mean solution of the selected diagonal HYM row equation

```text
Delta u = q - mean(q),      q = rho exp(-2u).
```

The selected determinant-one metric and induced End0 connection are

```text
H = diag(exp(u), exp(-u)),
A_diag = du T3,
D_E = d + ad(du T3).
```

The selected row-model Ext moment-map source is `E12`; its metric adjoint is
proportional to `E21`, hence `[E12,E21]` is Cartan and has zero `T1/T2`
projection.  Therefore the already-computed Ext-density tangent remains in the
protected `T3` lane.

## Theorem Slot

In the selected q79/F,m=1 S3/Green-Schwarz branch, the continuous
Ext-density-scale tangent

```text
L h_ext = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h)
```

is a well-defined zero-mean tangent of the selected HYM row equation.  Its
Frechet response is

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3).
```

This tangent may be promoted to physical `dotD_alpha1` if and only if MTT
supplies one of the following same-branch normalizations:

1. a selected source-normalization theorem identifying the discrete `alpha1`
   Chern/source row with the infinitesimal Ext-density scaling direction in
   the solved HYM row equation; or
2. a selected End0-to-sector routing functor, with normalization, sending the
   End0 response above to the physical sector `dotD_alpha1` matrices.

Without one of these two normalizations, the computed tangent is support data
only.  It does not promote `alpha1`, does not emit sector values, and cannot be
used as a validator-ready physical response.

## Proof

The selected HYM row equation fixes `q=rho exp(-2u)` and imposes the zero-mean
gauge slice.  Linearizing the source-density scaling `rho -> exp(t) rho` at
`t=0`, while preserving the zero-mean slice, gives

```text
L h = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h).
```

The existing Galerkin replay solves this equation with zero mean and residual
below `1e-12`, so the tangent is a verified selected local HYM response in the
row model.

Because the induced End0 connection is `D_E=d+ad(du T3)`, differentiating the
connection in a scalar `T3` direction gives

```text
delta D_E = ad(dh T3),
dotD_a[h] = (partial_a h) ad(T3).
```

The row-model off-diagonal control proves that the selected Ext source has no
`T1/T2` leakage: `E12` paired with its metric adjoint produces only the Cartan
direction.  Thus the Ext-density tangent is compatible with the protected
diagonal End0 lane and with the pure-gauge covariant Green theorem already
proved for `T1/T2`.

The remaining issue is not analytic existence.  It is typing and source
normalization.  The physical `alpha1` row is discrete Chern/source data for the
selected branch.  A derivative with respect to it is not defined merely by
choosing a nearby continuous scale parameter unless MTT proves that this scale
is the selected infinitesimal representative of the `alpha1` row.  Equivalently,
MTT may bypass the source-normalization route by proving a selected
End0-to-sector routing functor whose normalization maps the above End0 response
to sector matrices.  These are the only two legal promotion routes recorded by
this theorem.

Therefore the local tangent and its Frechet `dotD` replay are closed, but the
physical `dotD_alpha1` and sector response matrices remain open until one of
the two selected normalizations is supplied.

## Forbidden Shortcuts

- Do not treat the continuous Ext-density scale as a free physical knob.
- Do not identify `h_ext` with `alpha1` by notation alone.
- Do not import q79/constants support artifacts as proof of selected sector
  routing.
- Do not use observed masses, mixings, CP phases, thresholds, or benchmark
  matrices to select the normalization.
- Do not set selected validator flags from diagnostic lifted packets.

## Paper Use

This theorem should be inserted under the `dotD_alpha1` / C1 response sections
of the Theta execution and nonabelian-overlap papers.  It can also be cited by
the Strominger/HYM paper as the analytic row-tangent gate.  The safe conclusion
is: the selected row tangent is rigorous support; physical alpha1 promotion
requires the next source-normalization or sector-routing value fill.

Next artifact: `MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1`.
