# Apparatus-Response Frame Normalization Theorem

## Raw Response Data

Let a physical apparatus context `C` emit finite linear response channels
`R_C,a` on the finite carrier. Define its frame operator

\[
G_C=\sum_aR_{C,a}^*R_{C,a}.
\]

Assume `G_C` is positive and invertible on the detected support. No normalized
POVM is assumed.

## Theorem

Define

\[
M_{C,a}=R_{C,a}G_C^{-1/2},
\qquad
E_{C,a}=M_{C,a}^*M_{C,a}.
\]

Then every `E_C,a` is positive and

\[
\sum_aE_{C,a}=I
\]

on the detected support. Thus the raw response channels canonically determine a
normalized POVM context.

### Proof

Positivity is immediate from `E=M* M`. Summing gives

\[
\sum_aE_{C,a}
=G_C^{-1/2}\left(\sum_aR_{C,a}^*R_{C,a}\right)G_C^{-1/2}
=I.
\]

A common scaling `R_C,a -> c R_C,a` cancels between `R` and `G_C^{-1/2}`.
Therefore detector normalization introduces no continuous response parameter.
The construction is covariant under simultaneous unitary re-encoding.

## Exact Nonprojective Example

Take raw intensity diagonals `(1,1)` and `(1,0)`. Their frame diagonal is
`(2,1)`, giving effects

\[
E_1=\operatorname{diag}(1/2,1),
\qquad
E_2=\operatorname{diag}(1/2,0).
\]

For `rho=diag(1/3,2/3)`, the exact probabilities are `(5/6,1/6)`. Multiplying
both raw channels by any common nonzero scale leaves the effects unchanged.

## Source Boundary

This theorem closes normalization and removes a possible detector-response
knob. It does not emit the raw channels. The remaining apparatus theorem is a
map

```text
selected system + apparatus configuration + MTT action
    -> interaction Hessian / linear response channels R_C,a.
```

The apparatus configuration is physical context data, not a universal theory
parameter. Nevertheless, the rule producing its response channels must come
from the selected MTT action rather than being chosen to reproduce a target
POVM.
