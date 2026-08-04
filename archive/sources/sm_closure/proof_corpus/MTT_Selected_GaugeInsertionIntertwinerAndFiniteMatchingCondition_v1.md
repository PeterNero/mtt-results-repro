# MTT Selected Gauge Insertion Intertwiner and Finite Matching Condition v1

## Exact dimension coincidence

Removing the trivial projector directions gives

```text
dim(C16_L64 tensor Aug(Z7)) = 16*6 = 96,
dim(C16_tower tensor Aug(Z4)) = 16*3 = 48.
```

These equal the selected particle/antiparticle finite-carrier dimension `96` and three-family chiral
dimension `48`. This is a real structural clue, not yet an identification.

## Equivariance obstruction

The factors have different selected meanings. `C16_L64` is the recursive composition tower while
`H16_SM` is one family's chiral gauge representation. No selected map identifies them. More sharply,
the nontrivial `Z7` character space cannot be identified with `Z3` family times a twofold conjugation
label: every homomorphism `Z7 -> Z3 x Z2` is trivial. Likewise every homomorphism `Z4 -> Z3` is
trivial, and the Lens augmentation generator has phases `(pi/2,pi,3pi/2)` rather than the family
phases `(0,2pi/3,4pi/3)`.

Therefore the exact `96/48` dimension matches do not produce gauge-equivariant physical
intertwiners. This prevents a dimension-only promotion of A73 onto the existing matter carrier.

## Constructed product domains

The mathematical domains and projectors are canonical once their carriers are supplied:

```text
Vq = C16_L64 tensor C[Z7],   P7 = I-|1><1|/7,
Ve = C16_tower tensor C[Z4], P4 = I-|1><1|/4.
```

Identity maps on these product domains replay the A73 blocks exactly. What is not emitted is the
physical statement that the gauge one-form/ghost/Higgs/fermion fluctuation complex lives on these
domains with the declared routing and common background.

## Matching condition

The finite relative determinant is exact and regulator-free. Setting its value to zero at the base
point does not remove an additive finite term linear in the gauge invariant, so the first-derivative
matching condition must still be selected by the microscopic action.

The next object is `MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1`. It must construct the actual BRST gauge-fixed fluctuation complex on the
tower-augmentation domains or provide a different selected intertwiner, then fix the two relative
matching directions without observed gauge values.
