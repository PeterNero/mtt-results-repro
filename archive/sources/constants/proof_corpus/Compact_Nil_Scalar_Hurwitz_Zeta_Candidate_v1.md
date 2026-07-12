# Compact Nil Scalar Hurwitz Zeta Candidate v1

This artifact computes the sourced compact Nil scalar determinant as a diagnostic
candidate.

It uses the compact scalar spectrum imported in
`Sourced_Compact_Nil_Scalar_Spectrum_v1` and analytically sums the oscillator
index with a Hurwitz zeta:

```text
Z_p!=0(s) = sum_{k>=1} 2k*(4*pi*k)^(-s)*zeta_H(s, 1/2 + pi*k/c_nil^2).
```

The remaining `k` sum is assigned a finite part by fitting the large-cutoff
sequence to the asymptotic basis

```text
K^3 log K, K^3, K^2 log K, K^2, K log K, K, log K, 1.
```

The generated calculation is:

```text
scripts/compute_compact_nil_scalar_hurwitz_zeta_candidate.py
```

and the audit is:

```text
proof_corpus/compact_nil_scalar_hurwitz_zeta_candidate_audit.py
```

## Central Result

For the central cutoff window `[30, 120]`, the scalar finite-logdet candidate is:

```text
p_scalar_Nil = 3.8540439660345185
```

The direct scalar path does not close the `Qa` gate.  In the generated
calculation, the central value is far from the required unweighted `Qa` value:

```text
required unweighted Qa = 4.648486359430842
gap = 0.7944423933963232
```

If one naively used this scalar determinant as the `Qa` determinant, the weak
split would be:

```text
lambda_12 = 2.1279495941575286
target lambda_12 = 2.194153126940556
residual = -0.06620353278302726
```

## Interpretation

This is a useful near miss.  The sourced compact scalar determinant is stable
under the tested cutoff windows, and it lands close to the required `Qa` value,
but it does not equal it.

Therefore the remaining electroweak gate cannot be closed by simply replacing
the old Nil proxy with the compact scalar zeta determinant.

This is not the selected Qa/SU3 gauge determinant.  The selected gauge block may
include:

```text
nonabelian gauge fluctuation structure,
BRST/ghost quotient subtraction,
physical coherent-sector projection,
bundle endomorphism or curvature terms.
```

The next required artifact is:

```text
Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1
```
