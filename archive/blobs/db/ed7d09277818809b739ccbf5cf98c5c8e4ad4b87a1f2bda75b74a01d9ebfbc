# MTT Selected ZeroModeBasis From HYM Projector Source Theorem v1

Status: `MTT_SELECTED_ZEROMODE_BASIS_HYM_PROJECTOR_THEOREM_REDUCED_VALUES_OPEN`.

## Theorem

If the selected HYM/Strominger source emits same-branch sector operators
`D_E,s` and Riesz projectors `P_s` with:

- rank `3` for `Q,u,d,L,e,N` and rank `1` for `H`,
- positive complement gaps and truncation error bounds,
- coherent spectral projector retention,
- `End0(V_alpha)` equivariance for `T1,T2,T3`,
- an ordered selected `L2` basis `K_s` and Gram/trace convention,

then the already constructed canonical map

```text
rho_candidate,s(T_i)=ad(T_i),  s=Q,u,d,L,e,N
rho_candidate,H(T_i)=0
```

promotes uniquely to the selected physical sector source map `rho_s`.

## Proof

The source-payload artifact has already emitted the canonical map and checked
the finite `su(2)` representation identities.  The adjoint-triplet theorem
removes representation-choice freedom: a selected real three-dimensional
nonzero irreducible `End0(V_alpha)` action is the adjoint triplet, and a
one-dimensional Higgs carrier is the trivial singlet.

The only missing step is physical selection of the carrier.  A same-source
HYM/Strominger Riesz projector `P_s` with positive spectral gap, coherent
retention, and `End0` equivariance makes `im(P_s)` the selected zero-mode
carrier rather than a model carrier.  The selected Gram convention fixes the
remaining orthogonal ambiguity, so conjugating `rho_candidate` into the ordered
`K_s` basis gives a unique `rho_s`.

## Superset Use

We are using a constrained superset strategy, not a patchwork proof:

- straight `End0` supplies the algebra and canonical `rho_candidate`,
- HYM/projector data must supply the physical selected bases,
- Route-C/Galerkin is the execution path for finite projectors and gaps,
- SU(5)/E6, q79/S3/gerbe, and Theta/Weyl-pair encodings constrain matter-slot
  routing but cannot promote `rho_s` without the same selected projector packet.

Thus several encodings reduce the search space to the same finite target, but
none of them is allowed to become an independent proof source unless it emits
the selected payload.

## Current Boundary

The bridge theorem is proved, but the values are not emitted yet.  Current
honest data still have:

```text
coherent_spectral_projector_retention = false
zero_mode_slot_values_filled = false
selected_HYM_operator_source_verified = false
```

Next artifact: `MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1`.
