# q79 SM Diffeomorphism-Transported Regulator-Orbit Naturality and Reduced-Quotient Theorem v1

Date: 2026-07-24

## Verdict

The q79 diffeomorphism freedom has now been lifted through the full linear
Standard-Model BV regulator, including its boundary data.

There are two exact cases.

```text
Based case:
  Phi_t:X->X,
  Phi_t=identity on a boundary collar.

Transported-region case:
  X_t=Phi_t(X_0),
  every metric, coframe, bundle, BV field and boundary datum is pushed
  forward by Phi_t.
```

For orientation- and time-orientation-preserving spin-liftable isotopies,
the induced bulk and boundary unitaries `U_t` and `V_t` satisfy

```text
Q_t       = U_t Q_0 U_t^-1,
Delta_t   = U_t Delta_0 U_t^-1,
trace_t U_t = V_t trace_0,
A_t       = V_t A_0 V_t^-1,
P_APS,t   = V_t P_APS,0 V_t^-1.
```

After the canonical pullback by `U_t` and `V_t`, the complete regulated
package is constant. Therefore

```text
relative APS spectral flow = 0,
relative BV-BFV flux       = 0,
determinant transport      = canonical.
```

This closes diffeomorphism-presentation independence. It does not prove
independence under a physical shape or metric deformation made while the
ambient background is held fixed.

## 1. Selected q79 source

The pinned q79 causal-coframe certificate states that:

```text
the global Lorentzian coframe is closed up to diffeomorphism
and local Lorentz gauge;

the Q_WW spatial soldering is closed up to diffeomorphism
and frame gauge.
```

The existing Cauchy quantum-kinematics theorem already constructs the exact
unitary pull-push map

```text
(U_Phi,u psi)(x)=u_x psi(Phi^-1 x)
```

for orientation-preserving Cauchy diffeomorphisms carrying the coframe-induced
metric and measure. It intertwines the q79 carrier projectors with zero error.

The present theorem extends that same declared gauge freedom from finite-symbol
Cauchy kinematics to:

```text
the continuum Standard-Model BV fields;
the auxiliary positive elliptic metric;
the BRST/BV differential and Hodge Laplacian;
relative, Dirichlet and APS domains;
finite Hodge spectral projectors;
boundary BFV phase space;
finite-shell BV pushforward and determinant data.
```

No new geometric freedom is introduced.

## 2. Admissible diffeomorphism paths

Let `X_0` be the rounded compact q79 chart used by the local auxiliary
regulator theorem. An admissible path `Phi_t` must:

1. preserve orientation and time orientation;
2. lie in the spin-liftable identity component selected by the q79 spin
   structure;
3. preserve the Cauchy character of the chart;
4. transport the faithful `S(U(3) x U(2))` bundle and its fields;
5. act on ghosts, antifields and nonminimal pairs by the cotangent BV lift;
6. transport the auxiliary positive metric, coframe and boundary data.

There are two boundary variants.

### 2.1 Based interior isotopy

Require

```text
Phi_t=identity
```

on a collar of `boundary(X_0)`. Then `X_t=X_0`, the boundary unitary is the
identity, and every boundary operator and domain is literally fixed.

### 2.2 Ambient transported-region isotopy

Let

```text
X_t=Phi_t(X_0)
```

and transport the collar as well. The boundary is not fixed in raw
coordinates. Instead, `Phi_t` induces a unitary

```text
V_t:H_boundary,0 -> H_boundary,t.
```

All comparisons are made through this canonical identification. A deformation
of `X` inside a fixed metric, without transporting the source geometry, is not
in this class.

## 3. Full-BV naturality

Natural tensor, spinor, connection, ghost and antifield pull-push maps combine
to a graded unitary BV map

```text
U_t:E_BV,0 -> E_BV,t.
```

Because the complete field stack, background connection, coframe and metric
are transported together, every natural differential block is conjugate:

```text
Q_t=U_t Q_0 U_t^-1.
```

The cotangent lift preserves the odd BV pairing:

```text
U_t^* omega_BV,t U_t=omega_BV,0.
```

Adjoints are taken in the transported positive Hilbert structures, hence

```text
Q_t^dagger=U_t Q_0^dagger U_t^-1
```

and

```text
Delta_t
 =Q_t Q_t^dagger+Q_t^dagger Q_t
 =U_t Delta_0 U_t^-1.
```

Functional calculus then gives

```text
C_Lambda,t
 =1_[0,Lambda](Delta_t)
 =U_t C_Lambda,0 U_t^-1.
```

The Hodge contraction and ultraviolet Lagrangian cycle are transported by the
same map:

```text
h_t=U_t h_0 U_t^-1,
L_UV,t=U_t L_UV,0.
```

Thus the finite BV complexes and free Gaussian pushforwards are canonically
equivalent.

## 4. Boundary and APS naturality

Let `r_t` be the boundary trace. Naturality gives

```text
r_t U_t=V_t r_0.
```

The transported tangential boundary operator is

```text
A_t=V_t A_0 V_t^-1.
```

The APS projector is obtained by functional calculus, so

```text
P_APS,t
 =1_(-infinity,0)(A_t)
 =V_t P_APS,0 V_t^-1.
```

Relative, Dirichlet and adjoint APS domains therefore obey

```text
Dom_t=U_t Dom_0.
```

In the based case `V_t=1`, so the boundary package is literally constant. In
the transported-region case its pullback is constant:

```text
V_t^-1 A_t V_t=A_0,
V_t^-1 P_APS,t V_t=P_APS,0.
```

The spectrum cannot cross zero on a conjugacy orbit. Therefore the relative
APS spectral flow is exactly zero.

## 5. BV-BFV flux

The induced boundary map is symplectic:

```text
V_t^* omega_BFV,t V_t=omega_BFV,0.
```

The correct relative boundary displacement is

```text
D_t=V_t^-1 r_t U_t-r_0.
```

The trace intertwining identity gives `D_t=0`. Hence the relative flux matrix
and the corresponding transported boundary variation vanish:

```text
Flux_BFV(Phi_t)=D_t omega_BV D_t^*=0.
```

For a moving region the raw expression `r_t U_t-r_0` need not vanish, because
its two terms live in differently presented boundary spaces. Using it as the
physical flux would omit the canonical boundary identification.

## 6. Determinant and eta transport

Bulk and boundary spectra are unchanged under unitary conjugation. Therefore:

```text
the eta spectrum is constant;
the finite-shell determinant is constant;
the determinant-line fibers have canonical unitary transport.
```

For open isotopies this is the complete comparison statement. For closed
spin-gauge loops, the prior vanishing faithful-`Z6` spin-bordism obstruction is
the declared anomaly guard. Disconnected mapping classes and inequivalent spin
structures are not included.

No standalone numerical partition-function phase is selected. Normalized
pushforward comparison only uses the transported determinant half-density.

## 7. Exact transported-boundary witness

The certificate contains an eight-dimensional rational BV model with one
boundary and one interior contractible block.

The nontrivial boundary and interior transports are:

```text
R_boundary = [[3/5,-4/5],
              [4/5, 3/5]],

R_interior = [[ 5/13,-12/13],
              [12/13,  5/13]].
```

Each is applied to both field and antifield rows. Thus

```text
V_boundary=diag(R_boundary,R_boundary),
U_region=diag(V_boundary,R_interior,R_interior).
```

With boundary trace `r=[I_4,0]`, exact rational arithmetic proves

```text
r U_region=V_boundary r;
U_region^T omega U_region=omega;
det(U_region)=1;
Q_1=U_region Q_0 U_region^-1;
Delta_1=U_region Delta_0 U_region^-1.
```

Choose

```text
A_0=diag(-3,2,-1,4),
P_0=diag(1,0,1,0).
```

Then

```text
A_1=V_boundary A_0 V_boundary^-1,
P_1=V_boundary P_0 V_boundary^-1.
```

Here `P_1` differs from `P_0` in raw coordinates, so this is not a disguised
fixed-boundary example. Nevertheless:

```text
V_boundary^-1 A_1 V_boundary=A_0;
V_boundary^-1 P_1 V_boundary=P_0;
relative displacement=0;
relative BFV flux=0;
relative spectral flow=0;
det(H_shell,0)=det(H_shell,1)=4.
```

Replacing `V_boundary` by the identity while retaining the interior rotation
gives the based-collar case.

## 8. Extended presentation group

The regulator presentation group is now:

```text
G_presentation_extended
  = Diff_spin,0^+(Y; transported collar)
      semidirect
    (
      Gauge_0,boundary^faithful
      x Frame_0^Spin
      x BVGaugeFix_c
    ).
```

The physical regulator-choice problem is therefore reduced to

```text
R_admissible / G_presentation_extended.
```

This quotient removes:

```text
interior coordinate changes;
boundary-collar diffeomorphisms;
ambient-isotopic transported region embeddings;
based faithful gauge changes;
liftable residual frame changes;
compactly supported BV gauge-fixing changes.
```

## 9. Genuine remaining quotient coordinates

The following are not closed by this theorem:

```text
nonisotopic or nontransported region embeddings;
positive-metric deformations not related by diffeomorphism/frame gauge;
Cauchy-normal or Euclideanization changes not induced by the isotopy;
boundary-condition or BFV-polarization changes not related by transport;
inequivalent spin structures or disconnected domain data;
nonconjugate spectral crossings and crossing torsion;
uniform interacting cutoff removal.
```

This is the corrected meaning of the earlier open phrase "region shape or
embedding." Shape is not a physical selector when all source geometry is
merely transported. It remains a selector when the deformation changes the
geometry rather than its presentation.

## 10. Frontier

Closed:

```text
q79 spin-liftable diffeomorphism regulator path;
based-collar full-BV naturality;
ambient-isotopic transported-region naturality;
relative zero APS spectral flow;
relative zero BV-BFV flux;
canonical Hodge, determinant and free-shell pushforward transport.
```

Open:

```text
comparison or selection across the reduced quotient;
nonconjugate crossings and torsion;
uniform interacting cutoff removal;
fixed-coupling gauge-BRST C-star completion and selected state.
```

`B.QFT.02` remains open overall.

## 11. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The isotopy coordinates are presentation coordinates and disappear in the
extended quotient.

## 12. External theorem boundary

The functorial spacetime interpretation uses the
[generally covariant locality principle](https://arxiv.org/abs/math-ph/0112041).
Spinor covariance and observable-level uniqueness use the
[locally covariant Dirac field](https://arxiv.org/abs/0911.1304).
Bulk-to-boundary typing uses the
[classical BV-BFV framework](https://arxiv.org/abs/1201.0290), and
determinant/eta transport uses
[Dai-Freed](https://arxiv.org/abs/hep-th/9405012).

Those external results do not select a q79 regulator. The q79 coframe and
local-regulator certificates supply the selected source class; the external
theorems justify its natural transport.

## 13. Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_sm_diffeomorphism_transported_regulator_orbit.certificate.json
```
