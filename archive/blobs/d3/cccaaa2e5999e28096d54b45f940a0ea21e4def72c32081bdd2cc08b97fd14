# Selected Qa/SU3 Complex-Rotated C-Twist Normalization v1

## Claim

The selected Iwasawa/Strominger transgression computed in
`Selected_Qa_SU3_CTwist_Transgression_Pairing_Computation_v1` proves a
primitive complex-polarized `c`-twist generator in the scaled invariant frame.
It does not yet prove the absolute same-branch period unit or finite quotient.

## Inputs

- `candidate_data/ctwist_transgression_pairing_computation.candidate.json`
- `candidate_data/ctwist_deligne_cech_template.candidate.json`

The transgression input gives four base two-plane slants of the selected
Iwasawa `H` form:

```text
(g1,g3) -> -i g6
(g1,g4) -> +i g5
(g2,g3) -> +i g5
(g2,g4) -> +i g6
```

All four slants are nonzero, central, and have unit magnitude after suppressing
the common positive Iwasawa scale `A = r3/(r1*r2)`.

## Proof

Let the central real plane be `C_R = span_R{g5,g6}`.  The obstruction in the
literal line-bundle route came from treating the third coordinate as an
ordinary abelian line-bundle axis.  The transgression computation shows a
different object: the `H` slants do not land on the raw nil commutator axes,
but they do land on `C_R` after a complex phase rotation.

Each computed slant is a unit imaginary multiple of exactly one primitive
central basis vector.  Therefore, after choosing the complex-polarized central
generator

```text
tau_c = primitive generator in the complex-polarized central plane span{g5,g6},
```

the signs `+tau_c` and `-tau_c` can be used as the two gerbe/twisted-module
twist classes required by the Deligne/Cech template.  The phase `+/- i` is a
polarization convention, not a fitted numerical parameter.

The existing Deligne/Cech template requires only the tensor rule

```text
T_c tensor T_d -> T_(c+d)
```

and the five monad products all have opposite twists:

```text
F1 tensor G1 -> P,  +1 + -1 = 0
F2 tensor G2 -> P,  -1 + +1 = 0
F3 tensor G3 -> P,   0 +  0 = 0
F4 tensor G4 -> P,  -1 + +1 = 0
F5 tensor G5 -> P,  +1 + -1 = 0
```

Thus the computed transgression supplies the primitive complex support needed
for `c = +/-1` twisted-module typing in the scaled invariant frame.

## What This Closes

- The slants are not zero.
- The slants are purely central.
- The slants are primitive unit classes in the scaled Iwasawa frame.
- Direct raw nil-axis matching is not required for the twisted-module product
  law.
- The `c = +/-1` module typing is conditionally normalized once the selected
  period unit identifies the scaled primitive with `tau_c`.

## What Remains Open

This is not yet the full Qa/SU3 source theorem.  The missing step is the scalar
normalization gate:

```text
selected flux/Deligne period unit or selected finite quotient
```

on the same branch.  Without that, the proof has a primitive scaled generator,
but not the absolute statement that the selected finite MTT object is exactly
`c = +/-1`.

The next required artifact is:

```text
Selected_Qa_SU3_CTwist_Period_Normalization_or_A01_Exit_v1
```
