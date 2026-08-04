# MTT Selected Neutral Recursive Shared-Circle Dirac Domain and Spin-Branch Reduction v1

## Correct native domain

The displayed carrier shorthand `S1_cen x L(3,1) x Nil3` cannot be a literal
Cartesian product in the native 10D theory: its ordinary dimension would be
`1+3+3=7` internally and `11` in spacetime. The corpus itself supplies the
consistent recursive interpretation:

```text
S1_cen -> L(3,1) -> S2,
X6 = L(3,1) x (Gamma\Nil3),
M10 = Y4 x X6.
```

The lens layer adds two directions over the reused central circle, and the nil
layer adds three. Thus the effective rank is exactly `1+2+3=6`. A91's topology
string must be read in this nested sense.

## Spin and Dirac family

`L(3,1)` has `H1=Z3` and therefore one spin structure. The standard Heisenberg
nilmanifold has abelianization `Z^2`, hence four spin structures. The product has
four. The explicit global balanced `SU(3)` coframe in the flux corpus defines an
orientation, a metric family, and one framing-induced spin candidate, but the
corpus does not yet exclude the other three neutral spin backgrounds.

On the resulting six-manifold the smooth operator family is now explicit:

```text
D_X6 = D_L31 tensor I tensor sigma1 + I tensor D_Nil3 tensor sigma2,
D_X6^2 = D_L31^2 tensor I + I tensor D_Nil3^2.
```

Twisting this by the selected q79/F,m=1 Dirac-neutral carrier, `H_cen`, and the
LensNil bundle gives `D_nu(R1,R;f,h,chi)`. The mathematical family is `6/6`
defined. Physical value selection is `0/8`: the metric point, flux pair, spin
branch, Wilson loop, reduced eta, retarded/counterterm convention, map to
`arg det H_nu`, and absolute Hessian scale remain unselected.

## Exact flat-holonomy no-go

The reused lens fiber has `pi1(L(3,1))=Z3`. A flat character multiplying
`H_nu(phi)=exp(i phi)H_cen` must satisfy

```text
H_nu(phi)^3=I  iff  exp(3 i phi)=1.
```

Modulo the physical `2*pi/3` shape period this forces `phi=0`, with cosine
spectrum `[1,-1/2,-1/2]`. The central Nil3 generator is a commutator and is also
killed by every one-dimensional flat character. Therefore `pi/120` cannot come
from a flat internal central-circle character. A non-flat connection or a
determinant-line holonomy around a selected loop in the two Nil base Wilson
coordinates is required.

No observed neutrino value was used and no parameter was added.

Next artifact: `MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1`.
