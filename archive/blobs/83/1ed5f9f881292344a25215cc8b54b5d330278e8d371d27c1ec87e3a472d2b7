# q79 Augmented Heterotic Total Complex Route Correction v1

**Date:** 2026-07-30

**Executable packet:** `q79_augmented_heterotic_total_complex_route_correction.packet.json`

**Builder:** `build_q79_augmented_heterotic_total_complex_route_correction.py`

**Independent verifier:** `verify_q79_augmented_heterotic_total_complex_route_correction.py`

## 1. Decisive correction

The previous result correctly proved that a Maurer-Cartan plus gauge residual
has a Hodge Hessian. Its provisional next target was too small: the finite
heterotic `L_3` differential is not just the rank-102 operator `Dbar_Q`.

The primary heterotic construction uses

```text
Y_n = Omega^(0,n)(Q) + Omega^(0,n+1)(X)
```

and

```text
ell_1(y,b) = (Dbar y - 1/2 partial b, dbar b).
```

Thus `Dbar_Q` is an invariant diagonal subcomplex, but the full upper
differential is an upper-triangular extension by the `b`-form complex.

## 2. Why q79 cannot discard the b sector by the standard shortcut

Condition on the q79 Fu-Yau complex structure making

```text
pi: X_q79 -> K3
```

a holomorphic principal elliptic bundle. Let `Omega_K3` be the nonzero
holomorphic two-form on K3.

Because `pi` is a holomorphic submersion, `d pi` is surjective. Its dual is
injective, so

```text
pi* Omega_K3 != 0.
```

Holomorphic pullback commutes with `dbar`; hence this is a nonzero
holomorphic `(2,0)` form on `X_q79`. Equivalently its conjugate is a nonzero
anti-holomorphic `(0,2)` form. Therefore

```text
h^(2,0)(X_q79) >= 1
```

at this conditional complex-geometric tier.

More concretely, set

```text
b_K3 = pi* conjugate(Omega_K3).
```

The K3 form is `d`-closed and pullback commutes with `d`, so

```text
partial b_K3 = 0,
dbar b_K3 = 0,
ell_1(0,b_K3)=0.
```

Thus the augmented linear operator has a nonzero `b`-sector kernel direction
before quotienting by gauge. Whether it is exact, gauge removable, or a
physical zero mode remains open.

The heterotic `L_3` paper integrates out `b` in its reduced massless theory
under the sufficient premise `h^(2,0)=0`. That premise is unavailable on this
q79 branch. This does not prove that `b` is a new physical particle. It proves
that eliminating the sector requires a different gauge, quotient, mass or
connecting-map theorem.

The executable pointwise witness represents

```text
d pi = [[1,0,0],[0,1,0]]
```

and the K3 holomorphic symplectic form by its antisymmetric `2x2` matrix. Its
pullback has rank two and is nonzero.

## 3. Correct short exact sequence

Write

```text
Q_n = Omega^(0,n)(Q_phys),
B_n = Omega^(0,n+1)(X).
```

The primary differential carries the cohomological degree sign

```text
ell_1(y,b) = (Dbar y + 1/2 (-1)^n partial b, dbar b)
```

on `Y_n`. Thus the linear heterotic total differential has block form

```text
L_n = [[D_n, (1/2)(-1)^n A_n],
       [  0,                C_n]],
```

where

```text
D_n = Dbar_Q,
A_n = partial into the T*X component of Q,
C_n = dbar on the b-form sector.
```

The cochain law `L_(n+1)L_n=0` is equivalent to

```text
D_(n+1)D_n = 0,
C_(n+1)C_n = 0,
D_(n+1)A_n - A_(n+1)C_n = 0.
```

There is therefore a short exact sequence of complexes

```text
0 -> (Q_*,D) -> (Y_*,L) -> (B_*,C) -> 0.
```

The inclusion `i(y)=(y,0)` is a chain map:

```text
L i = i D.
```

The coordinate projection onto `Q` is generally not a chain map:

```text
p_Q L_n - D_n p_Q = (1/2)(-1)^n A_n p_B.
```

Consequently, the rank-102 cohomology is a genuine subcomplex input, but it
cannot be declared the full physical zero-mode space until the connecting map
induced by `A` is evaluated.

## 4. Hodge compression theorem

Equip the two summands with the declared orthogonal Hilbert pairing. At degree
one,

```text
Delta_Y,1 = L_1* L_1 + L_0 L_0*.
```

Compressing to the `Q_1` summand gives

```text
p_Q Delta_Y,1 i_Q
  = D_1*D_1 + D_0D_0* + 1/4 A_0A_0*
  = Delta_Q,1 + 1/4 A_0A_0*.
```

The correction is positive semidefinite. Therefore the rank-102 Hodge
operator equals the compressed full upper-action Hessian only after proving

```text
A_0*|_(declared Q_1 domain) = 0
```

or after a certified reduction that removes the extra term.

This is not a numerical correction inserted by hand. It is forced by the
off-diagonal `partial b` entry in the primary heterotic total differential.

## 5. Exact finite witness

The verifier uses one-dimensional blocks

```text
D0=0, D1=1,
C0=1, C1=0,
A0=2, A1=2.
```

Then

```text
L0 = [[0, 1],[0,1]],
L1 = [[1,-1],[0,0]],
L1 L0 = 0.
```

The `Q` subcomplex has degree-one Hodge operator `1`, while

```text
p_Q Delta_Y,1 i_Q = 2 = 1 + 1/4 A0 A0*.
```

This proves by exact counterexample that the full total-complex Hodge
compression need not equal the bare `Q` Hodge operator, even though `Q` is an
invariant subcomplex.

## 6. Corrected frontier

The structural/conditional contract is now

```text
8/8
```

and the physical instantiation contract remains

```text
0/6.
```

The remaining physical gates are:

- `selected_physical_visible_hidden_zero_defect_endpoint`
- `physical_A_and_C_maps_domains_and_boundary_conditions`
- `selected_total_complex_Hilbert_or_cyclic_pairing`
- `q79_b_mode_gauge_quotient_and_connecting_map`
- `selected_q79_nonlinear_l2_l3_and_D_term_completion`
- `upper_cohomology_products_and_finite_operator_projection`

The former direct-equality target

```text
full heterotic L3 differential = rank-102 Dbar_Q
```

is retired. The correct next object is:

```text
q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1
```

It must instantiate the full triangular differential, its pairing, the
connecting map and nonlinear products on one selected physical q79 endpoint.

## 7. Interpretation

This strengthens rather than discards the rank-102 work:

- `Q_phys` remains the correct coupled geometric deformation carrier;
- `Dbar_Q` remains an exact invariant linear block;
- the full closure-repair action must also track the form-sector extension;
- q79's K3/elliptic geometry supplies a concrete reason that this extension
  cannot be silently removed.

The surviving `b` direction is naturally related to the heterotic B-field and
may become a four-dimensional scalar or axionic mode, but that physical
identification is not proved here.

## 8. Primary-source boundary

The total-complex formula, the `L_3` products and the `h^(2,0)=0` reduction
premise come from:

```text
https://arxiv.org/abs/1806.08367
```

The rigorous `Dbar_Q`, formal adjoint and overdetermined ellipticity results
for the linear heterotic deformation complex are in:

```text
https://doi.org/10.1007/s00220-025-05309-2
```

The latter source does not supply the full nonlinear Maurer-Cartan equation.
This packet therefore uses the two results as a compatibility target, not as
an already-proved identity on the selected q79 endpoint.

## 9. Reproduction

```powershell
python .\build_q79_augmented_heterotic_total_complex_route_correction.py
python .\verify_q79_augmented_heterotic_total_complex_route_correction.py
```

Expected output:

```text
Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_BUILD_PASS
Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_VERIFY_PASS
```
