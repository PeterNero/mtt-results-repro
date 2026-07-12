# MTT Selected HYM Validated Fourier Residual Tail Bound v1

## Theorem

Let `A(T4)` be the Wiener algebra and `A_0(T4)` its zero-mean real subspace.
For the selected equation

```text
Delta u = P_0[rho exp(-2u)],
```

the inverse zero-mean Laplacian has norm at most `1/(4*pi^2)`. The weighted
theta density has exact Fourier coefficients

```text
c_(d r,l) = (-1)^(l r)/sqrt(2d)
             * exp(-pi*d*r^2/2 - pi*l^2/(2d)).
```

Gaussian integral tails therefore bound the omitted density coefficients.
The exponential remainder is bounded in the Wiener algebra by
`exp(2||u||)-1-2||u||`.

## Executed contraction

```text
||rho||_A upper       = 6.1688002757446583e+00
||u_bar||_A           = 9.4394163071358547e-02
continuous residual  = 2.1619429232870677e-01
r                     = 1.0000000000000000e-02
Y                     = 5.4762653988655388e-03
Z(r)                  = 3.8507611925757418e-01
Y + Z(r) r            = 9.3270265914412800e-03
r - [Y + Z(r) r]      = 6.7297340855872016e-04
```

Because `Z(r)<1` and `Y+Z(r)r<r`, Banach's fixed-point theorem supplies a
unique continuum solution in the certified Wiener ball. The previously proved
Chern transition law patches that solution globally. Thus the selected literal
Cech and literal global HYM witness families are now `2/2`.

## Scope

Uniqueness is local to the certified ball. This theorem does not claim global
uniqueness over all HYM branches, rank-three sector transfer, foundational
quantization, or zero-knob Standard Model closure.
