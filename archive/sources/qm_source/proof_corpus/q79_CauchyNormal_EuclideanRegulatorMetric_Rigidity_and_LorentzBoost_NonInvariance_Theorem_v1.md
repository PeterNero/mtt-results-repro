# q79 Cauchy-Normal Euclidean-Regulator Metric Rigidity and Lorentz-Boost Non-Invariance Theorem v1

Date: 2026-07-24

## Verdict

The auxiliary positive metric used by the local q79 BV regulator is not an
independent arbitrary metric once a future unit Cauchy normal is fixed.

For Lorentzian signature `(-+++)`, let `n` be future unit timelike and write

```text
n_flat=g_L(n,.).
```

Then the unique adapted sign-flip metric is

```text
g_E(g_L,n)=g_L+2 n_flat tensor n_flat.
```

In an adapted orthonormal coframe with `e0=-n_flat`,

```text
g_L=-e0 tensor e0+sum_i ei tensor ei
```

and therefore

```text
g_E=sum_a ea tensor ea.
```

This is exactly the positive metric used in the local regulator theorem.

Consequently the earlier status rows

```text
positive metric;
Cauchy normal / Euclideanization
```

are not two independent choices. They reduce to one open source object:

```text
future-unit-Cauchy-normal/Euclideanization class
modulo diffeomorphism and residual SO(3).
```

An exact rational Lorentz boost proves that a boost changing `n` is not
regulator-neutral: it preserves `g_L` and volume but changes the scalar
elliptic principal symbol from `1` to `41/9`. Thus only the residual spatial
frame group belongs to the fixed-normal regulator presentation orbit.

## 1. Source and scope

The pinned q79 causal-coframe certificate supplies:

```text
Y4 diffeomorphic to R x Sigma3;
an adapted global Lorentzian coframe;
theta0=N dt;
thetaa=Q_WW^a_i(dxi+N^i dt);
future/retarded causal orientation after A_causal.
```

The local regulator theorem defines

```text
g_E=sum_a ea tensor ea
```

and explicitly classifies it as an auxiliary analytic metric, not a physical
Wick rotation.

The present theorem determines exactly what data that formula depends on. It
does not turn Lorentzian time into a compact or Euclidean physical direction.

## 2. Sign-flip theorem

Let `(V,g_L)` be a Lorentzian vector space of signature `(-+++)`, and let

```text
g_L(n,n)=-1.
```

Every vector decomposes uniquely as

```text
v=a n+x,
g_L(n,x)=0.
```

Since

```text
n_flat(v)=g_L(n,v)=-a,
```

the sign-flip form obeys

```text
g_E(v,v)
 =g_L(v,v)+2 n_flat(v)^2
 =-a^2+g_L(x,x)+2a^2
 =a^2+g_L(x,x).
```

The restriction of `g_L` to `n_perp` is positive definite. Therefore

```text
g_E(v,v)>0
```

for every nonzero `v`.

## 3. Uniqueness

Suppose `h` is a symmetric form satisfying:

```text
h(n,n)=1;
h(n,x)=0 for every x in n_perp;
h(x,y)=g_L(x,y) for x,y in n_perp.
```

For `v=a n+x` and `w=b n+y`, bilinearity gives

```text
h(v,w)=ab+g_L(x,y).
```

The same calculation for

```text
g_L+2 n_flat tensor n_flat
```

gives exactly this expression. Hence

```text
h=g_E(g_L,n).
```

No positive-metric coefficient or anisotropy parameter remains after the
adapted sign-flip contract is imposed.

## 4. Adapted coframe identity

Choose an adapted Lorentz-orthonormal coframe

```text
(e0,e1,e2,e3),
e0=-n_flat.
```

Then

```text
g_L=-e0^2+e1^2+e2^2+e3^2
```

and

```text
2 n_flat^2=2 e0^2.
```

Therefore

```text
g_E=e0^2+e1^2+e2^2+e3^2.
```

This proves that the coordinate-free formula and the local regulator's
coframe sum are the same object.

## 5. Exact neutral directions

### 5.1 Residual spatial frame

An adapted frame transformation fixes `n` and acts by

```text
R in SO(3)
```

on `n_perp`. It preserves both `g_L|n_perp` and `n_flat`. Hence

```text
g_E(g_L,n)
```

is invariant.

This is why the earlier regulator-orbit theorem correctly used residual
spatial `Spin(3)` rather than the full local Lorentz group.

### 5.2 Diffeomorphism

For an orientation- and time-orientation-preserving diffeomorphism `Phi`,
tensor naturality gives

```text
g_E(Phi_*g_L,Phi_*n)
 =Phi_*g_L
  +2 (Phi_*n_flat) tensor (Phi_*n_flat)
 =Phi_*g_E(g_L,n).
```

Thus the diffeomorphism-transported orbit proved in the preceding theorem is
unchanged.

## 6. Why a boost is different

A local Lorentz boost preserves the physical Lorentzian metric. However, a
boost mixing the adapted time leg with a spatial leg changes the unit normal.
The boosted coframe is adapted to the boosted normal, not to the original
normal.

Since `g_E` is a functor of `(g_L,n)`, changing `n` changes the regulator
metric in general. This is a change of Euclideanization, not a residual frame
change within one fixed-normal regulator.

## 7. Exact rational boost witness

Use the `0-1` boost

```text
B = [[5/3,4/3,0,0],
     [4/3,5/3,0,0],
     [0,0,1,0],
     [0,0,0,1]].
```

For

```text
eta=diag(-1,1,1,1)
```

exact rational arithmetic gives

```text
B^T eta B=eta,
det(B)=1.
```

Start with

```text
n=(1,0,0,0)^T,
g_E(eta,n)=I4.
```

The normal adapted to the boosted coframe is

```text
n'=(5/3,-4/3,0,0)^T.
```

It remains future unit timelike:

```text
eta(n',n')=-1.
```

Its sign-flip metric is

```text
g_E' =
[[41/9,40/9,0,0],
 [40/9,41/9,0,0],
 [0,0,1,0],
 [0,0,0,1]].
```

The leading principal minors are

```text
41/9, 1, 1, 1,
```

so `g_E'` is positive definite. Its determinant is one, equal to that of
`g_E`, but `g_E'` is not `g_E`.

The inverse is

```text
(g_E')^-1 =
[[41/9,-40/9,0,0],
 [-40/9,41/9,0,0],
 [0,0,1,0],
 [0,0,0,1]].
```

For the scalar covector

```text
k=(1,0,0,0)^T,
```

the elliptic principal symbols are

```text
sigma_0(k)=k^T g_E^-1 k=1,
sigma_1(k)=k^T (g_E')^-1 k=41/9.
```

A scalar has no nontrivial internal spin or gauge conjugation that can turn
one scalar symbol into the other. Hence full-boost regulator neutrality is
excluded exactly.

## 8. Interpretation

This no-go is not physical Lorentz violation. The Lorentzian metric is
unchanged:

```text
B^T eta B=eta.
```

The object that changes is the auxiliary positive metric used to form an
elliptic spectral regulator. A regulator may depend on auxiliary data before
regulator independence or the physical limit is established.

The correct conclusion is:

```text
fixed n:
  residual SO(3), diffeomorphism and previously proved gauge paths are
  presentation;

changed n:
  a different Euclideanization whose equivalence still needs proof or
  whose representative must be selected.
```

## 9. Corrected quotient

Replace the two earlier entries

```text
positive metric modulo frame/diffeomorphism;
Cauchy normal or Euclideanization;
```

by the single entry

```text
future-unit-Cauchy-normal/Euclideanization class
modulo diffeomorphism and residual SO(3).
```

The positive metric is then generated by the exact deterministic map

```text
(g_L,n) -> g_L+2 n_flat tensor n_flat.
```

## 10. Frontier

Closed:

```text
positive and unique sign-flip metric given n;
equality with the q79 adapted-coframe sum;
residual SO(3) invariance;
diffeomorphism naturality;
reduction from two named choices to one source object.
```

Excluded:

```text
an arbitrary extra positive-metric parameter;
full local-Lorentz-boost neutrality at fixed scalar spectral regulator.
```

Open:

```text
selection of one future unit Cauchy normal/Euclideanization class;
or regulator independence under deformation of that class;
boundary-polarization comparison outside transported paths;
uniform interacting cutoff removal and fixed-coupling completion.
```

`B.QFT.02` remains open overall.

## 11. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The open normal is a geometric source field, not a fitted number.

## 12. Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_cauchy_normal_euclidean_metric_rigidity.certificate.json
```
