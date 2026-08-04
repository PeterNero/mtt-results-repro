# q79 SM Finite-Shell BV Pushforward and Gapped-Regulator Comparison Theorem v1

Date: 2026-07-24

## Verdict

The ultraviolet integration-cycle problem is closed at the free finite-shell
tier.

For every positive finite spectral shell of the already constructed local
q79 full-linear-BV operator, with the declared BV-Hodge compatibility,

```text
W_shell = im(Q) direct_sum im(Q^dagger),
L_shell = im(Q^dagger)
```

is an exact Hodge split and `L_shell` is a Lagrangian gauge-fixing cycle.
Moreover,

```text
h_shell = Q^dagger Delta^-1,
Q h_shell + h_shell Q = 1,
Q:L_shell -> im(Q)
```

is an isomorphism. The free quadratic BV action is nondegenerate on
`L_shell`; its finite BV pushforward preserves the free QME and is a
quasi-isomorphism on BV observables.

Regulator comparison is also closed on every admissible **gapped** path. A
common Riesz contour gives constant-rank finite spectral complexes, and Kato
parallel transport identifies their Hodge cycles and free pushforwards,
provided the transport also preserves the BV pairing, boundary BFV data and
determinant half-density.

This is not yet full q79 regulator-choice independence. The remaining
obstruction is now the explicit five-component vector

```text
actual admissible path;
spectral-flow stabilization;
boundary-BFV flux;
determinant-line holonomy;
uniform interacting cutoff removal.
```

The executable certificate passes all declared exact checks and introduces no
physical parameter, fit or observed value.

## 1. Input package

Let `(H,Q,omega,<,>)` be one of the admissible local auxiliary packages from
the preceding theorem:

```text
Q^2 = 0,
Delta = Q Q^dagger + Q^dagger Q,
(Delta+1)^-1 compact.
```

The finite spectral projectors commute with `Q`. Field and antifield rows are
retained together, and the Hodge metric is required to be compatible with the
BV cotangent pairing. In particular, on every retained positive shell,

```text
omega(im(Q^dagger),im(Q^dagger)) = 0.
```

This compatibility is part of the admissible package. It is not true for an
arbitrary unrelated Hilbert metric.

Choose regular shell endpoints

```text
0 <= Lambda_0 < Lambda_1,
Lambda_0,Lambda_1 not in spec(Delta),
```

and define

```text
W_(0,1) =
  1_(Lambda_0,Lambda_1](Delta) H
```

with the harmonic rows excluded. Compact resolvent makes `W_(0,1)`
finite-dimensional.

## 2. Finite-shell Hodge theorem

On `W_(0,1)`, `Delta` is invertible and commutes with `Q` and `Q^dagger`.
Set

```text
h = Q^dagger Delta^-1.
```

Then

```text
Qh+hQ
= (Q Q^dagger + Q^dagger Q) Delta^-1
= 1.
```

Therefore the shell is acyclic. The two operators

```text
P_ex = Qh,
P_coex = hQ
```

are complementary projectors, so

```text
W_(0,1) = im(Q) direct_sum im(Q^dagger).
```

Since `Q` is an odd-symplectic differential, `im(Q)` is isotropic. Acyclicity
gives

```text
dim im(Q) = 1/2 dim W_(0,1),
```

so it is Lagrangian. BV-Hodge compatibility gives the same conclusion for

```text
L_(0,1) = im(Q^dagger).
```

The contraction identity also shows that

```text
Q:L_(0,1) -> im(Q)
```

is bijective.

## 3. Free shell action and BV pushforward

On the Hodge cycle define

```text
S_shell(x) = 1/2 omega(x,Qx).
```

If `S_shell(x,-)` vanishes, nondegeneracy of `omega` between the two
Lagrangian summands and bijectivity of `Q` force `x=0`. Thus the restricted
quadratic form is nondegenerate.

The cotangent-lift differential is divergence-free with respect to the
canonical BV half-density:

```text
Str(Q)=0.
```

Together with `Q^2=0`, this gives the free QME. Finite-dimensional BV
pushforward over `L_(0,1)` therefore produces an effective half-density on
the retained modes satisfying the QME. The pushforward is a
quasi-isomorphism of BV complexes.

This statement is algebraic/formal and finite-dimensional. It does not call
an oscillatory Lorentzian integral absolutely convergent.

The unnormalized Gaussian factor is naturally determinant-line data. A
choice of orientation or half-density gives a scalar representative, but the
theorem does not promote that representative to a selected physical q79
phase. Normalized BV-cohomology observables are insensitive to a common
nonzero scalar.

## 4. Exact finite witness

For amplitudes

```text
a = 1,2,3
```

take three cotangent-lift contractible pairs. On each four-dimensional pair,

```text
Q e_0 = a e_1,
Q f_1 = -a f_0,
Q e_1 = Q f_0 = 0.
```

The exact certificate verifies

```text
Q^2 = 0,
Q^T omega + omega Q = 0,
Delta = diag(1 I_4,4 I_4,9 I_4),
Qh+hQ = I_12.
```

The Hodge cycle has basis

```text
(e_0,f_1) for each pair
```

and dimension six. The restricted differential is

```text
diag(1,-1,2,-2,3,-3),
```

while the restricted quadratic form has determinant

```text
-36.
```

This is an exact rational witness of the cycle, contraction and
nondegenerate pushforward mechanism.

## 5. Gapped comparison theorem

Let

```text
t -> (H_t,Q_t,omega_t,Delta_t), 0<=t<=1,
```

be a smooth family after unitary trivialization of its graph domains. Assume:

1. one contour `Gamma` remains in the resolvent set of every `Delta_t`;
2. the Riesz projectors

   ```text
   P_t = (2 pi i)^-1 integral_Gamma (z-Delta_t)^-1 dz
   ```

   have constant finite rank;
3. Kato transport preserves the BV pairing and intertwines `Q_0` with
   `Q_t`;
4. boundary BFV polarizations are fixed or canonically transported with
   zero or quantum-exact boundary flux;
5. the determinant half-density is parallel transported along the path.

Then the Kato equation

```text
dU_t/dt = [dP_t/dt,P_t] U_t,
U_0 = 1
```

gives

```text
U_t P_0 U_t^-1 = P_t.
```

By hypotheses 3-5, `U_t` is a BV chain isomorphism carrying the initial
Hodge cycle, action and half-density to the corresponding data at `t`.
Finite-shell BV pushforwards are therefore related by a quantum canonical
map. Their normalized physical cohomology observables agree.

### Exact endpoint witness

The certificate mixes the first two contractible pairs by

```text
R =
[ 3/5 -4/5  0 ]
[ 4/5  3/5  0 ]
[ 0     0   1 ]
```

and uses `U=R tensor I_4`. It verifies exactly that `U` is orthogonal and
BV-symplectic, transports `Q`, `Delta`, the rank-four low projector and the
Hodge cycle, and leaves the restricted quadratic form unchanged. The fixed
cut `Lambda=2` remains between eigenvalues `1` and `4`.

This closes a nontrivial comparison class. It does not construct a path
between every analytic q79 package.

## 6. Why crossings are different

The APS boundary witness

```text
A(s)=diag(-2,s,3), -1<=s<=1
```

has one positive spectral-flow crossing. With zero assigned to the
complementary adjoint domain, the negative APS projector ranks are

```text
rank P_-(A(-1)) = 2,
rank P_-(A(0))  = 1,
rank P_-(A(1))  = 1.
```

No fixed-rank Kato transport can identify the two sides through `s=0`.
Simultaneously, the corresponding zero-amplitude contractible BV pair loses
its Hodge inverse and its Gaussian form becomes degenerate.

Crossings are not necessarily physical inequivalence. They can be handled by
adding or removing contractible BV pairs, but then the comparison acquires:

```text
spectral-flow grading;
crossing torsion;
boundary BFV change-of-data term;
determinant-line/eta phase.
```

Those data must cancel, be canonically transported, or be selected. Merely
noting that cohomology is unchanged is insufficient for equality of
unnormalized partition functions.

## 7. Relation to anomaly cancellation

The prior q79 theorem proves:

```text
local SM gauge-anomaly vector = 0,
Omega_5^Spin(BG_SM/Z6) = 0.
```

This removes the corresponding local and closed-spin global gauge-anomaly
obstructions to a consistent determinant choice. It does not by itself prove
that a regulator loop with boundary has trivial eta holonomy, nor that a
varying APS polarization has zero BFV flux. No such implication is used here.

## 8. Frontier

Closed now:

```text
positive finite-shell Hodge contraction:          exact;
BV-Hodge Lagrangian integration cycle:            exact;
nondegenerate free shell action:                  exact;
free finite-shell QME pushforward:                exact up to determinant line;
gapped regulator-path comparison:                 conditional theorem;
APS crossing obstruction typing:                  exact.
```

Still open for the actual q79 physical exit:

```text
construct a path joining the relevant auxiliary packages;
prove zero spectral flow or supply selected stabilization;
prove boundary BFV flux is zero or quantum exact;
trivialize the physical determinant-line holonomy;
obtain uniform interacting estimates and remove the cutoff;
construct the fixed-coupling gauge-BRST C*-net and selected state.
```

Thus `B.QFT.02` remains open, but the integration-cycle problem has been
removed and regulator independence is no longer an undifferentiated
sentence. Its finite comparison theorem and its failure modes are explicit.

## 9. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

Shell endpoints and the comparison coordinate are regulator/proof
coordinates. A determinant trivialization along one interval is comparison
data, not a measured constant. Nontrivial loop holonomy would be an
obstruction, not a parameter to fit.

## 10. External theorem boundary

The finite BV integral and gauge-fixing theorem use
[Schwarz](https://arxiv.org/abs/hep-th/9205088). Family pushforward,
modified-QME preservation and boundary change-of-data control use
[Cattaneo, Mnev and Reshetikhin](https://arxiv.org/abs/1507.01221). The
pushforward quasi-isomorphism uses
[Cattaneo and Mnev](https://arxiv.org/abs/2605.30558).

Riesz-projector transport is the standard Kato theorem; spectral crossings
are typed using
[Booss-Bavnbek, Lesch and Phillips](https://arxiv.org/abs/math/0108014).
Boundary eta phases and determinant-line holonomy use
[Dai and Freed](https://arxiv.org/abs/hep-th/9405012).

These results establish the comparison mechanism. They do not supply the
actual q79 path, cancel its boundary flux, trivialize its determinant
holonomy, or prove the interacting limit.

## 11. Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_sm_finite_shell_bv_pushforward_regulator_comparison.certificate.json
```
