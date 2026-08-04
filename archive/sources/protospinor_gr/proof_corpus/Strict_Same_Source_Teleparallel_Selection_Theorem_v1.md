# Strict Same-Source Teleparallel Selection Theorem v1

Date: 2026-07-15

## Result

The remaining teleparallel-neutrality clause closes exactly for the current
strict same-source candidate branch. It does not require a new fitted number or
an independent gravitational axiom.

The displayed source packet is

```text
psi -> S(psi) -> Q(psi)=exp S(psi) -> G(psi)=Q(psi)^T Q(psi).
```

Its selected-branch provenance is now explicit rather than assumed. On the
minimal full-monodromy q79 root stack,

```text
Phi_q79(psi)=<c2,psi>(1/sqrt(2),-1/sqrt(2),0;0,0,0)
             +<s2,psi>(0,0,0;0,0,1),
S=J Phi_q79(psi).
```

The first vector is the rank-two trace-zero shape lane and the second is the
rank-three shear lane. Helicity two fixes the `Z64` plane, the natural q79 map
fixes its preimage, `Q_WW=exp(S)` fixes the positive polar representative, and
pullback fixes the metric. Thus this source realization is unique up to
polarization, frame, and diffeomorphism gauge on the selected branch, with no
fitted physical parameter.

It contains symmetric strain coordinates and no skew/orientation source
coordinate. The metric quotient

```text
r(Q)=Q^T Q
```

has differential

```text
Dr_I[dQ]=dQ^T+dQ.
```

The exact Jacobian has rank six and a three-dimensional kernel, precisely
`so(3)`. Thus the three left-orientation directions are the fiber erased by the
selected candidate observable.

The metric formula itself is now selected exactly once `Q_WW` is supplied. The
inner bundle already has its declared Euclidean metric `delta_I`, and

```text
G_Q(v,w)=delta_I(Q_WW v,Q_WW w)
```

is the pullback metric. This universal property uniquely fixes every bilinear
value, has local matrix `Q_WW^T Q_WW`, is positive on the invertible branch,
and obeys the correct metric transition law. Any nonlinear replacement
`f(Q_WW^T Q_WW)` requires an additional observable rule and is not the induced
metric of the comparison field. Thus the old "which metric observable?" gate
is closed given `Q_WW`. The old "which q79/Z64-to-Q_WW map?" gate is also
closed on the selected massless-helicity-two minimal-rootstack branch. What
remains is primitive MTT selection of that physical branch and the dynamic
spectral-HYM calculation. The root-stack carrier is now exactly the
real-symmetric sheet/Weyl symbol of three spectral eigenlines, with normalized
overlap `I6`. It is not the full visible HYM connection: for a nonzero-Chern
realization such as conditional `c2=9`, literal equality with the flat
root-stack connection is topologically impossible. The honest operator target
is the projected symmetric block `H_std`. Its abstract symmetry problem is now
solved. The unique positive sheet-to-opposite-edge complement defines
`J_DE(d,e)=(-e,d)`, with `J_DE^2=-I6` and exact `S3` equivariance. If the
selected HYM functional carries that same typed quarter-turn, its physical
block is forced to

```text
H_std=kappa_standard I2,
h_DE=0,
h_DD=h_EE=kappa_standard>0.
```

The Fu-Yau four-branch Chern orbit carries the same abstract order-four matrix,
and the shared `Z64` now supplies its unique root-independent parent
`C4=<16>={0,16,32,48}`. Both odd roots restrict as `i^m`. A single Fu-Yau
Chern branch is ruled out, but the four-branch parent alone is not enough:
free-orbit covariance admits a six-parameter family
`H_m=J_DE^m H_0 J_DE^-m`, so covariance is not one-branch invariance.

If the four orientations are autonomous Lens redundancy and the HYM operator
descends, scalarization follows conditionally. The obvious direct theta-space
shortcut has also been tested: `U_theta=diag(-1,i,1)` on the square cubic gives
only a four-dimensional `J^2=-1` sector on `Herm(3)` and mixes `D+S` into `K`.
It therefore cannot realize the six-dimensional `J_DE` in any basis.

The nontrivial functor is now constructed at the flat-symbol tier. Since
`Lambda^2 E_D=sign tensor E_D`, twisting by the shared SpinC determinant sign
gives the unordered-edge bundle `E_S`. Tensoring `E_D` with the realified odd-
root `C4` plane and using the unique positive opposite-edge map induces exactly
`J_DE=[[0,-I3],[I3,0]]`. It is global and parallel on the minimal root-stack
sheet symbol. No direct unital Herm(3) adjoint can replace it because such an
adjoint fixes the identity while `J_DE` sends trace to edge-sum. What remains
cannot be supplied by ordinary bundle duality or exterior square. Those
functors preserve the `SU(3)` HYM equation, but their exact action preserves
`D`, `S`, and `K` separately and squares as an involution rather than the
quarter-turn. Duality also flips `c3`, so it exchanges opposite-chirality
branches instead of acting within one nonzero-`c3` branch. The surviving
extension is a genuinely nonlocal same-branch Fourier-Mukai autoequivalence
obeying the emitted 11-row kernel/`Ext1`/Hessian contract (currently `2/11`),
or direct computation of the projected HYM block.

The shared-circle marking also closes the apparent Lens shortcut for the
current topology. In the vertical basis `(twisted, shared)`, the quarter-turn
sends the marked shared direction to the twisted direction. Its marked
stabilizer has no order-four element, and the existing `c3=+/-6` construction
clutches specifically along `S1_shared`. Autonomous Lens descent is therefore
a no-go in the marked realization. An unmarked modular replacement would have
to rederive five absent marking, clutching, HYM, and Hessian rows.

Foundation v8's autonomous-descent theorem is an if-and-only-if statement: a
reduced autonomous law exists exactly when the microscopic law is constant
after projection on each reduction fiber. Therefore a strict same-source
gravitational completion of the displayed `G` packet must be neutral on the
orientation fiber. Giving that fiber a bulk kinetic term would add an
orientation/connection source absent from the packet and would define a larger
modified-teleparallel theory instead.

## Exact coefficient selection

For

```text
T_c=c1 I1+c2 I2+c3 I3,
```

the certified pure-frame calculation gives

```text
2c1+c2+c3=0,
-4c1+2c2=0.
```

The constraint matrix has rank two, so its unique ray is

```text
(c1,c2,c3)=lambda(1/4,1/2,-1).
```

This is TEGR. Its pure-frame residual is zero, and

```text
e R(LC)=-e T_TEGR+2 partial_mu(e T^mu)
```

proves nonlinear metric descent modulo the boundary term. Hence the leading
parity-even two-derivative action on this strict same-source branch is exactly
Einstein-Hilbert/TEGR. The overall `kappa_h` and `Lambda_eff` remain values to
select; there is no additional dimensionless torsion parameter.

## Support typing

Inside the already declared canonical physical realization, `Y4` is globally
hyperbolic. If `Q_WW` is to be a local spatial source without introducing a new
support or pullback map, strict same-source typing places its base on an
oriented Cauchy slice `B=Sigma3` up to diffeomorphism and sets `TP=TB`. On the
invertible branch, `Q_WW:TB->TI` identifies `TI` automatically. The lapse and
shift remain constraint fields, and different Cauchy charts are gauge rather
than fitted data.

## Exact boundary of the claim

Closed:

- the q79/`Z64`-to-`Q_WW` source factorization on the selected massless-
  helicity-two minimal-rootstack branch, uniquely up to gauge;
- orientation neutrality for a strict completion of the displayed metric
  source;
- the unique TEGR coefficient ray;
- nonlinear classical Einstein equivalence modulo boundary data;
- Cauchy and bundle typing inside the canonical physical realization without
  an extra support map.

Still open:

- primitive MTT selection of the minimal-rootstack massless-helicity-two
  physical branch;
- the q79 gerbe branch, inverse Fourier-Mukai local freeness, and balanced HYM;
- a genuinely nonlocal same-branch Fourier-Mukai extension of the closed
  flat-symbol root-plane/twisted-exterior `J_DE` functor satisfying the 11-row
  kernel/`Ext1`/Hessian contract (currently `2/11`), or direct calculation of
  the projected operator; ordinary dual/exterior HYM transport and autonomous
  Lens descent in the current marked shared-circle setup are closed no-go;
- primitive selection of the canonical Lorentzian realization itself;
- numerical `kappa_h` and `Lambda_eff`;
- higher-derivative coefficients and quantum/UV completion.

So the action-form problem is closed on the current strict same-source branch.
The remaining classical selection problem is now upstream: select this branch
and its two dimensionful values, rather than search again for a gravitational
coefficient vector.
