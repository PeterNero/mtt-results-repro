# Selected Qc Circle Gauge Block Equivalence v1

## Purpose

This note closes the easiest determinant block:

```text
D_Qc.
```

The claim is limited and precise:

```text
For weak-split threshold accounting, the selected Qc gauge block equals the
q79 selected circle zeta determinant with abelian trace weight one.
```

It does not claim an absolute universal determinant normalization.

## Inputs

The exact circle zeta artifact gives:

```text
p_Qc = 2 log(2 pi R1)
     = 2.442340583291322.
```

The trace convention source gives:

```text
Tr(T^2)=1
```

for abelian generators.

The gauge-fixing source gives:

```text
For U(1), the Faddeev-Popov determinant is field-independent and ghosts decouple.
```

## Lemma

In the abelian Qc sector, gauge fixing contributes only a field-independent
projection Jacobian to the physical quotient.  Field-independent universal
determinant constants do not contribute to:

```text
lambda_12 = p_U1 - p_SU2
```

because the weak-split accounting keeps only selected threshold pieces, not
absolute path-integral normalization constants.

Therefore the selected Qc contribution for weak-split accounting is:

```text
p_Qc = 2.442340583291322.
```

## Status Change

Before this lemma:

```text
D_Qc = exact scalar proxy, not gauge-selected.
```

After this lemma:

```text
D_Qc = selected circle gauge block for weak-split accounting.
```

## Remaining Caveat

This closure relies on the already certified q79 central-circle scaffold.  It
does not independently reselect the central circle.

It also does not close:

```text
D_SU2,
D_Qa,
absolute universal determinant normalization.
```

## Verdict

The Qc block is closed for electroweak weak-split accounting.

The next block should be:

```text
Selected_SU2_Sphere_Gauge_Block_Equivalence_v1.
```
