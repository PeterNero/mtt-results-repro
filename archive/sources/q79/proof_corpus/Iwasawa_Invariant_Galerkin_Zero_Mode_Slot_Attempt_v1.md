# Iwasawa Invariant Galerkin Zero-Mode Slot Attempt

## Purpose

This note executes the first pass requested by the selected zero-mode/`dotD`
interface:

```text
try to fill the Q,u,d,L,e,N,H zero-mode slots in the Iwasawa invariant
Galerkin basis.
```

The result is useful but negative:

```text
the closed invariant Iwasawa data reproduce the rank-one E33 seed,
but they do not yet supply a valid sector-resolved slot fill.
```

This is not a collapse of the program.  It identifies the exact missing maps
needed before the primitive C1 blocks can be computed.

## Invariant Iwasawa Data Available

The flux/string corpus supplies a concrete left-invariant Iwasawa branch:

```text
d omega^1 = d omega^2 = 0,
d omega^3 = omega^1 wedge omega^2,

J = (i/2) sum_j r_j^2 omega_j wedge bar(omega_j),
Omega = omega_1 wedge omega_2 wedge omega_3.
```

It defines invariant `(1,1)` forms:

```text
a = (i/2) omega_1 wedge bar(omega_1),
b = (i/2) omega_2 wedge bar(omega_2),
c = (i/2) omega_3 wedge bar(omega_3),
```

and invariant `(2,2)` basis:

```text
alpha_1 = a wedge b,
alpha_2 = a wedge c,
alpha_3 = b wedge c.
```

The selected C1 curvature row is:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
alpha_2 = alpha_3 = 0.
```

The same Iwasawa source supplies three orthonormal harmonic representatives:

```text
Psi_i in H^1(X,E), i=1,2,3,
```

with normalized cubic:

```text
integral_X Omega wedge Tr(Psi_1 wedge Psi_2 wedge Psi_3) = 1
```

after rephasing.  This closes the rank-one tree seed:

```text
Y_seed = E33.
```

## Attempted Slot Fill

The zero-mode/`dotD` interface requires seven slots:

```text
Q, u, d, L, e, N, H.
```

The tempting invariant-Galerkin fill would be:

```text
Q_basis = u_basis = d_basis = L_basis = e_basis = N_basis
        = {Psi_1, Psi_2, Psi_3},
```

with one Higgs carrier selected from the same invariant algebra.

That is not a valid completed fill.  The reason is structural:

```text
Psi_1, Psi_2, Psi_3 live in the pre-SM E6 bundle cohomology H^1(X,E).
The E6-to-SM dictionary gives representation labels and operator channels,
but it does not supply projection maps from H^1(X,E) into the separate
Q,u,d,L,e,N,H internal zero-mode slots.
```

So the invariant data give a rank-one cubic seed, not the sector-resolved
operators:

```text
D_Q, D_u, D_d, D_L, D_e, D_N, D_H,
```

and not their C1 derivatives:

```text
dotD_Q, dotD_u, dotD_d, dotD_L, dotD_e, dotD_N, dotD_H.
```

## Rank-One Collapse Witness

If one ignores the missing projection maps and uses only the closed invariant
seed, the result is necessarily rank one.  In the chosen family basis:

```text
E33 =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 1]].
```

The light-family C1 rank-lift test for this matrix is:

```text
C33(E33) = E33_11*E33_22 - E33_12*E33_21 = 0.
```

If all sectors share only this universal orientation, then the leading CKM
heavy-link mismatch is also zero:

```text
Delta_v = (M_d13 - M_u13, M_d23 - M_u23) = (0,0).
```

Thus the closed invariant seed by itself cannot prove light-family masses or
CKM angle magnitudes.

This witness is not saying C1 fails.  It says the current invariant seed is
only the zeroth-order rank-one input.  C1 still may succeed after the selected
sector `dotD` operators and Green-operator responses are computed.

## What The First Pass Closes

The first pass closes the following negative result:

```text
Iwasawa invariant data currently in the corpus are insufficient to fill the
Q,u,d,L,e,N,H zero-mode/dotD slots.
```

It also closes the first obstruction witness:

```text
using only the closed invariant cubic gives E33, C33=0, and no up/down
orientation mismatch.
```

This prevents a subtle overclaim:

```text
one may not promote the three E6 harmonic representatives into all SM family
slots without sector projection maps and slot operators.
```

## Missing Data For A Valid Fill

The minimal missing objects are:

```text
sector projection maps:
  pi_Q, pi_u, pi_d, pi_L, pi_e, pi_N, pi_H
  from the E6 bundle/cohomology data into SM slots;

slot operators:
  D_Q, D_u, D_d, D_L, D_e, D_N, D_H
  including their domains, bundles, quotient conditions, and kernels;

Higgs internal representative:
  H, plus sector conjugation H or H^dagger already fixed by the single-Higgs
  projection;

C1 response data:
  deltaTheta_C1, dotD_a, P_a, Q_a, G_a, complement gaps, and horizontal gauge;

primitive blocks:
  B_s,Theta, B_s,L, B_s,R, B_s,H, B_s,vertex, B_s,basis.
```

The flux corpus does contain an explicit left-invariant holomorphic structure
for a monad bundle.  That suggests the next concrete calculation:

```text
extract the finite left-invariant Dolbeault/monad complex,
compute H^1(X,E) representatives in that finite complex,
then derive or supply the E6-to-SM sector projection maps.
```

Only after those maps exist can the invariant Galerkin program decide whether
the invariant subcomplex is enough or whether non-invariant family modes are
required.

## Correct Next Step

The next artifact should be:

```text
Iwasawa Monad Dolbeault Complex Extraction.
```

It should turn the source's explicit:

```text
barpartial_E = barpartial + A^(0,1)
```

into matrices on the left-invariant `(0,p)` form basis and compute the kernel
and cohomology representatives.  Then the representation projection maps can
be tested against the `Q,u,d,L,e,N,H` slot contract.

## Bottom Line

We did try the first Galerkin fill.

The answer is:

```text
rank-one invariant seed: closed,
sector-resolved slot fill: blocked,
reason: missing E6-to-SM cohomology projection maps and slot dotD operators.
```

This sharpens the path.  The next computation is not to guess primitive C1
matrices.  It is to extract the finite Iwasawa monad/Dolbeault complex and the
sector projection maps that would make those matrices calculable.
