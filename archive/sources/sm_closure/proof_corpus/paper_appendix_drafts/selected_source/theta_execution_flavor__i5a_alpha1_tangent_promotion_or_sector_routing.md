# I5a. Selected Alpha1 Tangent Promotion or Sector-Routing Normalization

Target paper: `theta_execution_flavor`

Target file: `C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md`

## Theorem

Let `eta_00^unit` be the selected normalized Ext representative, let
`rho=|eta_00^unit|^2`, and let `u` solve the selected diagonal HYM row equation

```text
Delta u = q - mean(q),      q = rho exp(-2u),      mean(u)=0.
```

The Ext-density-scale tangent is the zero-mean solution

```text
L h_ext = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h).
```

For the induced determinant-one End0 connection

```text
D_E = d + ad(du T3),
```

the corresponding Frechet response is

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3).
```

This response may be called physical `dotD_alpha1` only after one of two
same-branch normalizations is proved: either MTT identifies the discrete
`alpha1` Chern/source row with this Ext-density tangent, or MTT supplies a
selected End0-to-sector routing functor with normalization sending this End0
response to the physical sector matrices.

## Proof Sketch

Linearizing the selected HYM row equation under `rho -> exp(t)rho` gives the
operator `L` above in the zero-mean slice.  The selected Galerkin replay solves
this equation with residual below `1e-12`, so the local tangent is closed.  Since
`D_E=d+ad(du T3)`, differentiating in a scalar `T3` direction gives
`dotD_a[h]=(partial_a h)ad(T3)`.  The selected row-model Ext source has zero
`T1/T2` projection, so the tangent stays in the protected Cartan lane.

## Safe Wording Before Promotion

The paper may state that MTT has a selected local HYM Ext-density tangent and a
closed Frechet `dotD` replay in the End0 row model.  It must also state that this
does not promote physical `alpha1`, does not emit sector matrices, and does not
close C1/SM response until selected source-normalization or selected
End0-to-sector routing values are theorem-derived.

No observed masses, mixings, CP phases, thresholds, benchmark entries, or
diagnostic lifted flags are used as source selectors.
