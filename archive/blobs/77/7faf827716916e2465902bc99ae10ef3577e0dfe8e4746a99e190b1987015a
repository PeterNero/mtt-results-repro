# MTT Selected q79 Alignment Integral H2 Presentation v1

## Result

A130 converts A129's selected global monodromy representation into a complete
integral surface-cycle basis on the selected endpoint carrier. It first fixes
the two hyperelliptic central handle lifts directly from interval winding data,
then computes the coupled thimble/Fox quotient and appends the primitive
rank-two Leray edge pair.

The result is an exact rank-92 integral `H2` basis on the same carrier as the
A126/A127 beta. This closes the basis half of the same-carrier requirement. It
does not yet evaluate any of the eight period rows.

## Central lifts without periods

Branch-point braiding determines a genus-two handle action only up to the
central hyperelliptic involution. In the common reciprocal coordinate

```text
s=1/(t-(2+3i)),
u^2=q0(w)+...+q6(w)s^6,
```

the value at the marked point `s=infinity` is controlled by

```text
q6(w)=F6(t=2+3i,w).
```

If `q6` is nonzero on a closed handle loop, continuation of its square root
returns with sign `(-1)^wind(q6)`. A fourth-order Arb elliptic-flow Taylor
cover proves nonvanishing on every handle segment. A certified rotated-ray
crossing count gives

```text
handle A: wind(q6)= 6, central lift +1,
          min |q6| > 7038.6951065063467

handle B: wind(q6)=-5, central lift -1,
          min |q6| > 11617.247009277342.
```

Only three additional coefficient subdivisions are needed on `A` and none on
`B`. No period value, observed value, or fitted sign is used. The result agrees
with the identity-carrier A119 signs but is independently derived on the
selected endpoint.

## Vanishing lattice

Choose the primitive vector of each positive Picard-Lefschetz factor so that
its first nonzero coordinate is positive, and orient the corresponding
thimble compatibly. This is an integral orientation convention; changing it
multiplies a chain column by `-1` and cannot change the lattice.

The selected boundary map

```text
W: Z^90 -> H1(fiber,Z)=Z^4
```

has rank four and Smith diagonal

```text
(1,1,1,1).
```

Its image is saturated. The lexicographically first unimodular block is in
columns `1,2,4,5`, with determinant `1`, and its kernel is a saturated
rank-86 thimble lattice.

## Coupled handle quotient

With the certified lifts `+A,-B`, form the 98-chain module

```text
Z^90_thimbles direct_sum Z^8_handle-cylinders
```

and boundary

```text
D=[-W | (A-I) | (B-I)].
```

The central-lift handle-only Fox block has Smith diagonal `(1,1,1,0)`, so it
cannot be quotiented independently: one relation direction is supplied by
the ordered thimble tail. The exact local extension satisfies

```text
W L = M90...M1-I,
D_handle F = M90...M1-I.
```

Consequently the four combined thimble/Fox columns are cycles. In coordinates
of the saturated rank-94 kernel of `D`, those four relations have Smith
diagonal

```text
(1,1,1,1).
```

They are therefore primitive. A unimodular completion with determinant `1`
emits a torsion-free rank-90 primary basis. In the resulting deterministic
completion, 82 columns are pure thimbles and 8 have handle support; the
largest absolute basis coefficient is `3`.

## Leray edge and full basis

The invertible alignment changes the incidence fibration but not the ambient
divisor class

```text
[C_A]=p_K3^*H+3 p_E^*[point].
```

The primitive fiber `F` and an adjusted primitive ambient horizontal class
`Gamma_0` therefore retain the hyperbolic intersection matrix

```text
[[0,1],
 [1,0]].
```

The known Betti numbers are `(1,2,92,2,1)`. The 90 primary columns plus this
primitive rank-two edge pair give the emitted exact integral basis

```text
primary_01,...,primary_90,Leray_F,Leray_Gamma0.
```

## Remaining calculation

The basis question is no longer open. The same-carrier frontier is now the
actual period evaluation:

1. integrate the eight selected residue forms over 90 canonically oriented
   thimbles;
2. integrate them over the eight primitive handle cylinders;
3. multiply by the emitted `98x90` primary basis and append the two Leray
   columns;
4. certify the resulting `8x92` table and decide exact integral membership of
   the tight selected beta.

Next artifact:
`MTT_Selected_q79SelectedAlignmentEightByNinetyTwoPeriodExecution_v1`.
