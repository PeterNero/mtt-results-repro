# MTT Selected Proto-Spinor Alignment to Dirac Mass Readout v1

## Finite Dirac encoding

The selected rank-three `L` and `N^c` carriers are the two Weyl blocks. The
selected full-rank transfer `Y=dY=I3+X3` defines

```text
D_F^D(Y) = [[0,Y],[Y^dagger,0]],
Gamma_F  = diag(-I3,+I3).
```

The resulting `6x6` operator is self-adjoint and anticommutes with `Gamma_F`.
This closes a finite proto-spinor-to-Dirac encoding. It does not prove that a
separate Majorana extension is impossible.

## Alignment readout

The selected response obeys

```text
Y(h)=Y0+h*dY,
G(h)=Y(h)Y(h)^dagger=Y0Y0^dagger+h*H1+h^2*H2.
```

`H1` has eigenvalues `[-1.3678359791715602, -0.6839179895857803, 0.6839179895857807]` and is indefinite. It therefore cannot
be identified with the positive physical mass-squared Hessian. `H2=dY dY^dagger`
has eigenvalues `[0.9999999999999993, 1.0, 3.9999999999999987]` and is positive semidefinite.

The coefficient-matched trial `h=a_internal` gives singular values
`[0.0, 0.34195899479289, 0.6839179895857801]` and Gram spectrum `[0.0, 0.11693595411976376, 0.46774381647905516]`. It
automatically contains a nil-anchored zero mode, but its splitting ratio is
`0.24999999999999994`, not the downstream postcheck `0.029805013927576625`. Since the corpus
has not selected `h=a_internal` as the physical VEV coordinate, this remains a
diagnostic rather than a prediction.

## Exact frontier

The next theorem must emit the radial second variation and the selected VEV
coordinate, then evaluate

```text
Y_nu,ij=(partial_h partial_barL_i partial_Nc_j J)|align,
M_D=v_align*Y_nu.
```

Next artifact: `MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1`.
