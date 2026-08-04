# q79 Selected-Side Strict-Spin No-Go and SpinC Lift v1

Date: 2026-07-15

## Certified selected-side branch test

The A125/A126 source packet supplies a complex `3x3` alignment interval with
roughly `1e-100` radii. Its convention is

```text
L=A*[a,b,1]^T,
L dot X=0.
```

Branching occurs when `A^T X` lies on the dual cubic. On its elliptic
normalization, therefore,

```text
X=A^(-T)[1-3a^2,2b,a^3+a]^T,
b^2=a^3-a.
```

Substitution into the exact K3 sextic gives `P(a)+bQ(a)`. Its norm

```text
N(a)=P(a)^2-(a^3-a)Q(a)^2
```

has degree `36`. A direct Arb/ACB Sylvester determinant encloses
`Res(N,N')` for every alignment in the matrix balls and excludes zero. Its
absolute lower bound is approximately `5.37e364`. Thus the norm is square-free
throughout the interval and cannot be a square in the elliptic function field.

The same interval calculation also evaluates the resultant with the elliptic
three-division polynomial `3a^4-6a^2-1`. It excludes zero, and the leading
pullback coefficient excludes zero at the flex point at infinity. Hence the K3
branch sextic avoids all nine flex points of the cubic throughout the interval.

Consequently, throughout the current executed selected-side carrier,

```text
branch divisor reduced and irreducible,
H1(branch complement;Z)=Z6,
sign character has no Z4 lift,
w2=a^2 != 0,
strict Spin: NO-GO.
```

The packet uses this selected-side interval but still declares
`integral_branch_selected=false`; this result is not a claim that the gerbe-zero
or final MTT alignment source gate has closed.

## Exact SpinC lift

The strict-Spin obstruction has an exact representation-level repair. In

```text
SpinC(3)=(Spin(3)xU(1))/{(1,1),(-1,-1)},
```

take the existing binary lifts `q1,q2` and define

```text
g1=[q1,i],
g2=[q2,i].
```

Then

```text
g1^2=g2^2=[-1,-1]=1,
g1 g2 g1=g2 g1 g2,
(g1 g2)^3=[-1,-1]=1.
```

They generate an order-six image projecting isomorphically to the signed-sheet
`S3`. The SpinC determinant character is `z^2`, so a transposition maps to
`-1`: precisely the sheet-sign character. Its determinant line is the
complexification of the real sign local system and

```text
c1(L_det)=beta_Z(a),
c1(L_det) mod 2=a^2=w2.
```

Thus abstract global SpinC lifting of the signed-sheet monodromy is closed; it
does not require a new relator search.

## Physical frontier

What remains is no longer the existence of a spinorial carrier on the branch
complement. It is the MTT identification theorem:

```text
SpinC determinant sign line
= selected order-two restriction of L_shared,
```

together with the common-base transverse-line comparison and extension or
smooth HYM replacement through ramification. No observed datum or fitted
parameter enters this result.

Current status:

```text
EXECUTED_SELECTED_SIDE_STRICT_SPIN_NOGO_AND_SPINC_LIFT_CLOSED_SHARED_LINE_HYM_OPEN
```
