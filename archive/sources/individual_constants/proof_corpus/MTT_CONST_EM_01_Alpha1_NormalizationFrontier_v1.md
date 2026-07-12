# MTT CONST EM 01 Alpha1 Normalization Frontier v1

Status: `MTT_CONST_EM_01_ALPHA1_NORMALIZATION_FRONTIER_BUILT_INTERNAL_INDEX_SUPPORT_PHYSICAL_CY_OPEN`

Label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY`

## Result

The corpus/repo search found strong normalization support, but not yet a
physical `C_Y` value.

Promotable now:

- source-side `N_alpha1(h_ext)=1`,
- internal `K_gauge,int=1`,
- selected internal kernel vector `(U1, SU2, Qa/SU3)=(2/3, 1, log(2008))`.

Not promotable yet:

- physical `C_Y` in `alpha_Y = C_Y * N_alpha1(h_ext)`,
- `alpha_Y`,
- `alpha_em`,
- `alpha(0)` or `alpha(M_Z)`.

## Superset Strategy

We combine four source paths but lock the target:

- QA alpha1 driver replay gives the source-side unit.
- QA quotient-projector/U1-SU2 path gives the internal U1 index `2/3`.
- QA gauge-kinetic route gives internal `K_gauge,int=1`.
- non-SM exhaustion theorem forbids physical electroweak closure without a
  selected normalization/threshold kernel.

This gives a clean current-source no-go for physical `C_Y`: the best current
candidate is internal and inverse-kernel/index scoped, while the physical
coupling multiplier still needs a typed convention and source row.

## Forbidden Shortcuts

- Do not set `C_Y=2/3` as a physical coupling multiplier.
- Do not set `C_Y=3/5` or `5/3` merely by convention.
- Do not solve `C_Y` from measured `alpha`, `sin^2(theta_W)`, or `g2`.
- Do not identify internal `K_gauge,int=1` with physical `K_phys`.

## Next

Next label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION`

Decide how the internal U1 index, GUT hypercharge factors, and determinant
finite parts legally map into the `C_Y` slot.
