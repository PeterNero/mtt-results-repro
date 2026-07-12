# Selected GR Hessian Block Source Theorem v1

## Result

The current corpus closes the target operator class but not the selected source
block.

Closed:

- the spacetime response target is the TT/Lichnerowicz Einstein block
- the gauge quotient is the BRST/diffeomorphism quotient
- the retarded response class is the positive Stieltjes/proper-time kernel class
- the effective Einstein-Hilbert coefficient has the structural form
  `G_eff^{-1}=V_int/G_10`

Open:

- the selected numeric anchored closure Hessian `H_anchor`
- the selected derivative/projection map `P_GR` from closure strain into TT
  metric perturbations
- the selected retarded measure for this same block
- the selected stress-response map
- absolute `G_eff` normalization

## Why The Z64 Block Does Not Close GR

The existing exact `Z64` central-circle branch is important evidence that MTT can
certify a Hessian block and retarded kernel in a finite selected sector. But it
is not the GR block. It lives on the central-circle tower carrier, while the GR
target lives in the TT metric response sector.

So the correct use of `Z64` here is methodological:

`Z64 proves the style of certificate can exist; it does not supply K_GR.`

## Required Closing Data

The generated template is:

`candidate_data/selected_gr_hessian_block_source.template.json`

To close the theorem, fill it with source-certified data:

- closure basis labels
- TT/gauge response basis labels
- positive selected `H_anchor`
- selected `P_GR`
- `K_GR = P_GR^T H_anchor P_GR` after quotient
- positive retarded Stieltjes/proper-time measure
- selected stress-response map
- normalization statement, either absolute or explicitly dimensionless-only

