# Selected Qa/SU3 HYM Full Real Delta_A Hessian With OU Weights

## Purpose

This note answers the request to compute the full real Hessian as far as the
corpus permits.

The real unitary Chern/HYM algebraic block is computable.  The complete
Strominger Hessian with torsion, metric weights, gauge quotient, and OU
weights is not fully supplied by the corpus.

## Real Chern/HYM Algebraic Block

Using the extracted HYM matrices `B_i`, the trivial Hermitian metric stated in
the source, and the Chern unitary conjugate pieces `-B_i^*`, compute:

```text
H_real(mu)[X,Y]
  = sum_i <[B_i,X],[B_i,Y]> + <[-B_i^*,X],[-B_i^*,Y]>
```

for anti-Hermitian `X,Y in u(3)`.

The normalized real basis is:

```text
central_i_identity,
cartan_i_lambda3,
cartan_i_lambda8,
skew_real_12, skew_imag_12,
skew_real_13, skew_imag_13,
skew_real_23, skew_imag_23.
```

## Eigenvalues

Sample real Hessian eigenvalues:

```text
mu = 0.25:
0, 0.1812707, 0.5625, 0.5625, 0.625, 0.625, 1.0625, 1.0625, 2.0687293

mu = 1:
0, 2.53589838, 3, 3, 4, 4, 5, 5, 9.46410162

mu = 4:
0, 20.28718708, 24, 24, 32, 32, 40, 40, 75.71281292
```

The zero mode is the central `u(1)` identity direction.  The eight `su(3)`
directions are positive in this real algebraic Chern block.

## What Is Still Missing For The Full Strominger Hessian

The complete Hessian still requires:

```text
Iwasawa metric/radius weights on one-form directions,
torsional Weitzenbock/endomorphism terms from R_+ and Hhat,
differential derivative pieces beyond the invariant algebraic band,
fixed-gauge quotient beyond the central u(1) commutator zero mode,
OU weights gamma_{n,k}^{-1},
zeta/heat regularized determinant of the full operator.
```

The sampled log-det-prime remains monotone in `mu`, so this real block alone
does not select an interior `mu`.

## Verdict

```text
real u(3) Chern/HYM Hessian block computed: yes
full Strominger Hessian including OU weights computed: no
mu selected: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1
```
