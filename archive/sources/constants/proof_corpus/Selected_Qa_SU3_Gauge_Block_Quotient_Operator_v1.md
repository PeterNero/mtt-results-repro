# Selected Qa/SU3 Gauge Block Quotient Operator v1

This artifact tests whether the sourced compact Nil co-closed one-form spectrum
closes the remaining `Qa/SU3` gap.

The one-form source gives the co-closed p != 0 eigenvalues

```text
Y_+^{k,l,n}, Y_-^{k,l,n}.
```

Using the sourced formula, these satisfy the exact product identity

```text
Y_+ Y_- = (M_{k,n+1}^2)^2,
```

where `M_{k,n}^2` is the scalar oscillator eigenvalue.  Thus the co-closed
one-form determinant is a shifted scalar oscillator determinant.

The executable test is:

```text
scripts/compute_selected_qa_su3_gauge_block_quotient_operator.py
```

and the audit is:

```text
proof_corpus/selected_qa_su3_gauge_block_quotient_operator_audit.py
```

## Result

The natural p != 0 quotient candidates do not close the gap.  In short, the
plain co-closed one-form quotient does not close the gap.

```text
required unweighted gap = 0.7944423933963232.
```

The tested candidates include:

```text
co-closed one-form logdet,
one-form minus scalar,
half one-form minus scalar,
scalar minus half one-form,
lowest scalar mode logdet.
```

None matches the required gap under the same Hurwitz/asymptotic finite-part
scheme used for the stable scalar candidate.

## Regulator Warning

A direct double-cutoff estimate of `oneform-minus-scalar` can land near the
required gap.  This is rejected here because it uses a different regulator from
the scalar Hurwitz finite part.  We should not turn a regulator mismatch into a
physical correction.

## Boundary

This does not close the `Qa/SU3` determinant.

It does show that the plain co-closed one-form/ghost quotient is not enough.
The remaining source must be more specific:

```text
physical coherent-sector projection, or
bundle curvature / Weitzenbock endomorphism term, or
another selected Qa/SU3 operator ingredient.
```

The next required artifact is:

```text
Selected_Qa_SU3_Physical_Coherent_Projector_or_Endomorphism_Term_v1
```
