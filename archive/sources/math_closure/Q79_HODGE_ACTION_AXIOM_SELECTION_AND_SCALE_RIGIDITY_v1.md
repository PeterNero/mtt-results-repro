# q79 Hodge Action Axiom Selection and Scale Rigidity v1

**Date:** 2026-07-30

**Executable packet:** `q79_hodge_action_axiom_selection_audit.packet.json`

**Builder:** `build_q79_hodge_action_axiom_selection_audit.py`

**Independent verifier:** `verify_q79_hodge_action_axiom_selection_audit.py`

## 1. Question

The preceding minimal-action theorem proved that

```text
C(psi)=1/2 (||D psi||^2+||D* psi||^2)
```

is the unique member of a three-coefficient quadratic class after imposing
equal exact/coexact weights, harmonic zero cost and unit normalization. It did
not show why MTT should select those requirements.

This audit separates four logically different questions:

1. Does a shared complex circle force equal exact/coexact weights?
2. Can one upstream first-order closure object force them?
3. Which coefficient is a convention and which is a physical scale?
4. Does the resulting quadratic repair generator equal the full physical
   action?

## 2. General Hodge-sector classification

For a Hilbert complex with `D^2=0`, write

```text
P_ex = D*D,
P_co = DD*,
P_h  = harmonic projector
```

in the normalized finite witness. The most general sector-diagonal
nonnegative Hessian is

```text
A_(x,y,z)=x P_ex+y P_co+z P_h.
```

Pointwise preservation of harmonic cohomology by the repair flow is equivalent
to

```text
A P_h=0,
```

and hence to `z=0`. An isometric adjoint-reversal `S` satisfying

```text
S D S^(-1)=D*,
S P_ex S^(-1)=P_co
```

forces `x=y`. Positivity and nondegeneracy off cohomology then leave exactly
one positive ray:

```text
(x,y,z)=(kappa,kappa,0),  kappa>0.
```

This recovers the preceding coefficient notation through

```text
x=a+c,  y=b+c,  z=c.
```

Thus `z=0` gives `c=0`, and `x=y` gives `a=b`.

The cohomology statement concerns the closure-repair generator. It does not
assert that all physical cohomology states are massless after interactions,
symmetry breaking or transferred products.

## 3. Exact shared-circle no-go

The shared circle alone does not force `x=y`.

The verifier realifies the three-dimensional Hodge witness to six dimensions
and equips it with

```text
J^2=-I,
J^4=I.
```

Both

```text
A_sym  = P_ex+P_co,
A_asym = 2 P_ex+P_co
```

commute with `J`, preserve the same harmonic kernel and admit the same
twofold-sign/fourfold-return circle structure. Yet only `A_sym` has equal
exact/coexact weights.

Therefore:

```text
shared U(1) phase + double return does not by itself select the Hodge ratio.
```

This is useful rather than negative: it tells us exactly what extra structure
the circle must act on.

## 4. Closure-supercharge square theorem

Let the nilpotent closure differential be `Q=D`, with selected Hilbert adjoint
`Q*=D*`. Define the two self-adjoint first-order closure charges

```text
B1 = D+D*,
B2 = i(D-D*).
```

Nilpotence gives the exact algebra

```text
B1^2=B2^2=Delta_D,
{B1,B2}=0,
Delta_D={D,D*}=D*D+DD*.
```

More generally, for real `p,q`,

```text
B_(p,q)=p B1+q B2,
B_(p,q)^2=(p^2+q^2) Delta_D.
```

Equivalently, for `u=rho exp(i theta)`,

```text
B_u=uD+conj(u)D*,
B_u^2=rho^2 Delta_D.
```

This is the decisive reduction. If MTT selects one self-adjoint first-order
closure charge in the single-shared-coefficient class and defines linear
repair by its square, then:

- harmonic zero cost is automatic;
- exact and coexact weights are automatically equal;
- the shared-circle phase `theta` changes the first-order polarization but
  disappears from the repair Hessian;
- only the positive scale `kappa=rho^2` remains.

At quarter turns the charge sequence is

```text
B1 -> B2 -> -B1 -> -B2 -> B1,
```

while every square is `Delta_D`. This gives a precise mathematical role for
the `+i/-i` circle choice: it can mark a closure-charge polarization without
creating a new quadratic action. It does not yet prove that Lens selects one
physical polarization or one arrow of time.

The algebra is standard Hodge/supersymmetric-quantum-mechanics mathematics.
The new MTT result is the source reduction: the former three action-shape
requirements can be replaced by one upstream closure-supercharge
factorization premise.

## 5. Nonlinear repair-to-operator theorem

The generic fixed-point statement

```text
gradient repair linearizes to minus the Hessian
```

is already present in the current SM corpus. It is not being reproved here as
a new MTT result.

The missing upstream link is what makes that Hessian a Hodge operator. Let
`Phi(C)` be a nonlinear closure-defect map into a Hilbert defect space, with

```text
Phi(C_*)=0.
```

Define the closure cost and repair flow by

```text
E(C)=1/2 ||Phi(C)||^2,
partial_tau C=-grad E(C).
```

If `L=D Phi(C_*)`, then exact differentiation at the zero-defect fixed point
gives

```text
Hess E(C_*)=L*L,
D(-grad E)(C_*)=-L*L.
```

The terms involving the second derivative of `Phi` vanish because
`Phi(C_*)=0`. Therefore, if the selected defect Jacobian is the closure charge

```text
L=B_u=uD+conj(u)D*,
```

then

```text
Hess E(C_*)=|u|^2 Delta_D.
```

This is the exact realization of the proposed hierarchy:

```text
nonlinear closure defect
  -> squared-defect repair functional
  -> first derivative B_u
  -> Hessian B_u^2
  -> heat repair and unitary boundary.
```

The executable witness uses a genuinely nonlinear polynomial defect map. Its
zero-point Jacobian is the stacked pair `(D,D*)`, its cost Hessian is exactly
`Delta_D`, and the Jacobian of its negative-gradient flow is exactly
`-Delta_D`.

## 6. Scale rigidity

For

```text
A_kappa=kappa Delta_D,  kappa>0,
```

the kernel, harmonic projector, positive spectral projector and commutant are
independent of `kappa`. The real and imaginary families obey

```text
exp(-tau A_kappa)=exp(-(kappa tau) Delta_D),
exp(-it A_kappa)=exp(-i(kappa t) Delta_D).
```

Therefore all dimensionless action-shape data determine only a positive ray.
Choosing `kappa_int=1` is a valid internal unit convention. It is not a
prediction of an SI action, time, length, Planck or Newton scale. This agrees
with the existing physical-action-unit certificate, which leaves one absolute
dimensionful anchor open.

The parameter count is consequently:

```text
three sector weights before structure,
two after harmonic preservation,
one positive overall scale after closure-charge factorization,
zero remaining dimensionless Hodge-shape ratios.
```

No observed value or fitted parameter is used.

## 7. Why this is not yet the full physical action

Two independent obstructions remain.

First, the SM closure/action independence certificate proves that a closure
cost cannot be renamed a physical Lagrangian without a selected
shadow/restriction theorem. Second, a quadratic Hessian never selects its
nonlinear completion. The exact scalar family

```text
f_lambda(s)=kappa s^2/2+lambda s^4/4
```

has the same value, gradient and Hessian at `s=0` for every `lambda`, while its
fourth derivative is `6 lambda`.

There is also a domain restriction. The theorem applies to a genuine
first-order Hilbert differential such as the conditional q79 Dolbeault
deformation operator. It does not override the existing mixed-order Maxwell
detour no-go: for that BV complex, the naive adjoint Hodge sum has quartic
rather than Laplace-type principal symbol.

## 8. q79 status after this theorem

The q79 deformation contract already has the structural formula

```text
B_Q=Dbar_Q+Dbar_Q*,
Delta_Q=B_Q^2.
```

Once the four physical endpoint/chamber/metric rows are supplied, `Dbar_Q`,
its adjoint and this factorization are functorial. The new theorem therefore
removes the need to source three unrelated Hodge-action coefficients.

What it does not yet supply is the physical nonlinear q79 defect map whose
Jacobian is `B_Q`, or prove that this repair cost is the SM/QFT/GR action. The
exact next source statement is:

```text
q79SelectedClosureDefectJacobianToHodgeOperator.v1
```

It must show, on the selected metric and operator domain, that one physical
nonlinear closure-defect map vanishes at the q79 fixed point and has derivative

```text
D Phi_Q(C_*)=sqrt(kappa) B_Q.
```

The theorem above then gives the repair-flow derivative
`-kappa B_Q^2` with no further Hessian assumption. One coefficient must be
shared across the full q79 complex, with no additional sector weights.

## 9. Frontier

Closed exactly here:

- classification of sector-diagonal Hodge repair Hessians;
- harmonic preservation iff the harmonic weight vanishes;
- equal-weight positive ray under adjoint reversal;
- shared-circle and double-return insufficiency by explicit counterexample;
- single closure-supercharge square implies equal weights and harmonic zero
  cost automatically;
- a zero-defect squared-residual functional has Hessian `L*L`, so a selected
  closure-charge Jacobian emits the Hodge repair operator rather than assuming
  it;
- phase independence and one-scale rigidity of the repair Hessian;
- nonlinear nonuniqueness by an exact same-Hessian family;
- zero new fitted or observed-value inputs.

Still open:

```text
B.HS.01:     OPEN: the four physical endpoint, hidden carrier, common chamber and metric/connection source rows remain zero of four.
B.GEO.01:    OPEN: the physical projective connection and q79 operator domain have not been instantiated.
B.OP.01:     OPEN: the actual rank-102 Dbar_Q, Delta_Q, harmonic projector and positive spectrum have not been executed.
B.ACTION.01: OPEN BUT NARROWED: three independent Hodge-shape axioms are no longer required if one selected closure-supercharge square principle holds. The generic nonlinear zero-defect gradient bridge is exact. Still missing are the physical q79 defect map/Jacobian source, closure-cost/action shadow theorem, nonlinear completion, transferred products and absolute scale.
```

## 10. External mathematical context

The Hilbert-complex and Hodge-Laplacian framework is standard; see Arnold,
Falk and Winther, *Finite element exterior calculus: from Hodge theory to
numerical stability*, arXiv:0906.4325. The identification of a nilpotent
differential and its adjoint as supercharges whose anticommutator is a Hodge
Hamiltonian is classical; see Witten, *Supersymmetry and Morse Theory*,
J. Differential Geometry 17 (1982), 661-692.

These references support the mathematics, not the MTT physical source claim.

## 11. Reproduction

```powershell
python .\build_q79_hodge_action_axiom_selection_audit.py
python .\verify_q79_hodge_action_axiom_selection_audit.py
```

Expected output:

```text
Q79_HODGE_ACTION_AXIOM_SELECTION_AUDIT_BUILD_PASS
Q79_HODGE_ACTION_AXIOM_SELECTION_AUDIT_VERIFY_PASS
```
