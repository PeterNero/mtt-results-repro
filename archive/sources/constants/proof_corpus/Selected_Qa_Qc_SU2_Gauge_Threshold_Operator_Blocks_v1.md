# Selected Qa Qc SU2 Gauge Threshold Operator Blocks v1

## Purpose

The selected gauge-threshold heat-kernel theorem reduced the live electroweak
gate to operator blocks:

```text
D_Qa, D_Qc, D_SU2.
```

This note builds the block scaffold.  It does not compute selected spectra or
finite determinant values.

## Calculator

```text
scripts/build_selected_qaqcsu2_gauge_threshold_operator_blocks.py
```

The scaffold is machine-readable in:

```text
certificates/selected_qaqcsu2_gauge_threshold_operator_blocks_certificate.json
```

## Common Operator Form

Each threshold block is represented schematically as:

```text
D = Pi_phys (nabla_A^* nabla_A + E_curv
             + gauge_fixing_terms
             + ghost_measure_terms) Pi_phys.
```

This matches the corpus-level requirements:

```text
principal Laplace-type part,
bundle representation,
ghost/subtraction rule,
endomorphism or curvature term,
physical quotient/projector,
domain and normalization,
spectral or heat-coefficient data.
```

## Block Scaffold

### D_Qa

Role:

```text
Q_a component carried by the U(3)_a/SU3 stack.
```

Candidate trace/index clue:

```text
C_A(SU3) = 3.
```

Ghost/quotient rule:

```text
non-abelian Faddeev-Popov quotient determinant must be included.
```

Missing:

```text
selected SU3-stack connection,
curvature endomorphism,
gauge-fixing condition,
ghost operator,
domain and quotient conditions,
selected spectrum or heat finite part.
```

### D_Qc

Role:

```text
Q_c abelian circle stack entering Y=(1/6)Q_a-(1/2)Q_c.
```

Candidate trace/index clue:

```text
Tr(T^2)=1.
```

Ghost/quotient rule:

```text
the abelian Faddeev-Popov determinant is field-independent.
```

Any universal constant from this decoupled determinant must cancel or be
discarded from weak-split accounting.

Missing:

```text
selected abelian connection,
circle/line domain,
boundary or quotient conditions,
selected eigenvalues,
multiplicities,
charge weights.
```

### D_SU2

Role:

```text
weak SU2 determinant subtracted from hypercharge-normalized U1 response.
```

Candidate trace/index clue:

```text
C_A(SU2) = 2.
```

Ghost/quotient rule:

```text
non-abelian Faddeev-Popov quotient determinant must be included.
```

Missing:

```text
selected SU2 connection,
curvature endomorphism,
gauge-fixing condition,
ghost operator,
domain and quotient conditions,
selected spectrum or heat finite part.
```

## Determinant Handoff

The block scaffold does not fill the determinant spectrum template:

```text
certificates/selected_local_determinant_spectrum.template.json
```

The template still requires:

```text
eigenvalue,
multiplicity,
index_weight.
```

for each selected gauge-factor mode.

## No-Knob Discipline

The operator blocks, domains, spectra, and index weights must be selected
before electroweak comparison.

The following are forbidden as inputs:

```text
lambda_12,
sin^2(theta_W),
alpha_EM,
measured gauge couplings.
```

## Verdict

The block schema is built and aligned with the gauge-fixing/projection corpus.

It is not closure.

The next true gate is:

```text
Selected_Qa_Qc_SU2_Operator_Spectra_or_Heat_Coefficients_v1.
```
