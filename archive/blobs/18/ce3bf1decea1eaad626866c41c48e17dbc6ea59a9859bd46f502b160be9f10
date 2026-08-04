# MTT Selected q79 Non-Pullback Chiral Visible Bundle and Full SU9 Holonomy Selection v1

Status: `MTT_U6_HIDDEN_FULL_SU9_HOLONOMY_CLOSED_VISIBLE_C3_TOPOLOGICAL_AND_SPECTRAL_CANDIDATES_CLOSED_TWISTED_HOLOMORPHIC_HYM_BIANCHI_LIFT_OPEN`

## What A103 changes

A103 closes the hidden full-holonomy question and advances the visible
three-family question from a desired Chern number to two exact constructions.
It also removes an old false shortcut: the printed Iwasawa monad cannot be used
as the proof of `c3=6`.

## Iwasawa correction

The Iwasawa source defines

```text
c=(i/2) omega3 wedge bar(omega3),
d omega3=omega1 wedge omega2.
```

Therefore `dc` is nonzero. Four of the five displayed `L_i` labels contain a
nonzero `c` coefficient, so they are not closed first Chern forms. Independently,
the printed matrix has

```text
(barpartial A + A wedge A)_12
  = mu bar(omega1) wedge bar(omega2) != 0.
```

Finally, the source places that matrix in a global trivial smooth frame. Such a
connection may have curvature, but its bundle has `c1=c2=c3=0`. Hence the
printed line table, A01 matrix and `integral c3=6` cannot all describe one
bundle. The Iwasawa object remains a conceptual circle/nil clue, not a valid
three-family proof source.

## Shared-circle clutching theorem

The A102 rank-one Fu-Yau topology splits topologically as

```text
X = P_delta x S1_shared,
```

because the second circle has zero Chern class. The Gysin sequence for the
primitive class `delta` gives

```text
b(P_delta)=(1,0,21,21,0,1),
b(X)=(1,1,21,42,21,1,1).
```

In particular `H4(P_delta)=0`, so the pullback of the K3 `SU(3)` bundle is
topologically trivial on the five-manifold while retaining its slice
connection. Trivialize it smoothly, glue the two ends of
`P_delta x [0,1]` by a map `g:P_delta->SU(3)` of winding `k`, and use the
untwisted shared circle as the gluing direction. Bott normalization gives

```text
integral c3(E_g)=2k.
```

The two choices `k=+3,-3` therefore give smooth non-pullback `SU(3)` bundles
with `integral c3=+6,-6`. This is an exact topological existence theorem and
uses the shared circle directly. It does not yet supply an integrable
holomorphic structure, balanced HYM connection or the differential Bianchi
representative.

## q79 genus-two spectral cover

The selected polarization has `H^2=2`, hence genus two and `h0(H)=3`. On the
base-point-free representative, `|H|` gives the double-cover map

```text
phi_H:K3 -> P2.
```

For an elliptic curve `E`, the zero-determinant fiber of
`Sym^3(E)->Pic^3(E)=E` is `|3*0|=P2`. After choosing an isomorphism
`iota:|H|^*->|3*0|`, the composite `iota o phi_H` defines a determinant-zero
degree-three spectral cover

```text
C subset K3 x E,  [C]=3 sigma + H.
```

The identification `iota` is an unfixed `PGL(3)` alignment with complex
dimension eight. It is not counted as a measured fit, but it is not selected
by the current MTT source and must remain visible in the moduli ledger.

On the sectioned reference geometry, the integral odd-rank spectral parameter
`lambda=3/2` has line-class coefficients `(6,-1,5)` and gives

```text
c3=2 lambda H^2=6,
c2=H sigma + 6 F.
```

This independently agrees with the shared-circle clutching value. The equality
`lambda=(q7+1)/2=3/2` is recorded only as an arithmetic clue; the corpus does
not prove that source map.

Brinzanescu-Halanay-Trautmann provide the correct twisted Fourier-Mukai and
spectral-cover framework for a principal non-Kahler elliptic bundle, but their
theorem gives local representability and a global corepresenting moduli map,
not automatic global surjectivity from every cover to a bundle. The actual
Fu-Yau promotion therefore still requires an inverse-gerbe twisted line object
on `C`, a locally free inverse transform, balanced stability/HYM and a new
Bianchi calculation. The sectioned reference `c2=H sigma+6F` must not be
silently identified with A102's nine-unit K3 instanton row.

## Full hidden SU9 holonomy

Let `W9` be any A102 stable bundle with `det W9=O` and `c2(W9)=11`. Its HYM
holonomy is connected because K3 is simply connected and irreducible because
`W9` is stable. A connected irreducible proper subgroup of `SU(9)` can act in
dimension nine only through:

```text
SO(9) vector,
Sym^8(SU(2)),
or a 3 x 3 tensor product,
```

apart from the full `SU(9)` fundamental case.

All proper cases are impossible. An orthogonal rank-nine bundle has even
`c2=-p1` on the even K3 lattice. For a stable possibly twisted rank-`r` K3
factor, the Mukai inequality gives

```text
Delta >= r - 1/r.
```

Hence `Sym^8` has `Delta >= 120*(3/2)=180`, and even allowing a nonzero Brauer
obstruction the tensor case has

```text
Delta(A tensor B)=3 Delta(A)+3 Delta(B)
                 >= 3*(8/3)+3*(8/3)=16.
```

Both contradict `Delta(W9)=c2(W9)=11`. Therefore

```text
Hol(W9)=SU(9).
```

Under the exact A102 embedding `SU(9)/Z3 subset E8`, the hidden commutant is
the finite group `Z3`. There is no continuous hidden gauge factor and hence no
hidden gaugino-condensate amplitude to tune. The 38 complex bundle moduli still
matter for thresholds; full holonomy does not select a unique point.

## Remaining cutset

1. Construct the inverse-gerbe twisted rank-one spectral object on `C` and
   prove its inverse Fourier-Mukai transform is a locally free `SU(3)` bundle.
2. Prove balanced stability/HYM and compute its `c3` directly on the actual
   principal Fu-Yau torsor.
3. Recompute the full differential Bianchi identity; do not reuse `9+11+4`
   without the non-pullback curvature terms.
4. Derive the discrete MTT selector for the orientation/winding and finish the
   hidden threshold plus A98 numerical NS5 rows.

Next artifact: `MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1`.

## Primary references

- [Balaji and Kollar, Holonomy groups of stable vector bundles](https://arxiv.org/abs/math/0601120)
- [Yoshioka, Irreducibility of moduli spaces of vector bundles on K3 surfaces](https://arxiv.org/abs/math/9907001)
- [Brinzanescu, Halanay and Trautmann, Vector Bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Friedman, Morgan and Witten, Vector Bundles over Elliptic Fibrations](https://arxiv.org/abs/alg-geom/9709029)
