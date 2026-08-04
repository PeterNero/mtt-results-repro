# q79 Shared-Z64 Fu-Yau Parent Quarter-Turn and Descent Dichotomy v1

Status:
`Q79_SHARED_Z64_FUYAU_PARENT_QUARTERTURN_CLOSED_CONDITIONAL_FREE_ORBIT_HESSIAN_INFERENCE_NOGO_LENS_DESCENT_OR_DIRECT_HYM_OPEN`

## Exact finite source

The selected shared finite carrier already contains a canonical order-four
sector. The cyclic group `Z64` has one and only one subgroup of order four:

```text
C4=<16>={0,16,32,48}.
```

The two still-possible odd character roots are `chi_1` and `chi_33`. On this
subgroup they agree exactly:

```text
chi_1(16m)=chi_33(16m)=i^m.
```

Their ratio `chi_32` is trivial there. The realification of this character on
the oriented integral rank-two lattice is

```text
J=[[0,-1],[1,0]],
J^2=-I,
J^4=I.
```

Thus the order-four source is root-independent and introduces no numerical
parameter. Reversing the generator replaces `J` by `-J` and reverses the orbit;
it does not change the parent set or the Hessian commutant.

## Fu-Yau parent action

At the active rank-one topology tier,

```text
X=P_delta x S1_shared,
```

the two vertical circle directions form an integral `T2` lattice with Chern
pair `(delta,0)`. Acting by `J` gives

```text
(delta,0) -> (0,delta) -> (-delta,0) -> (0,-delta).
```

This is exactly the A107 minimal Chern orbit. It closes the integral lattice
action on the four-branch parent and explains the square-fiber `tau=i`
candidate without choosing between `chi_1` and `chi_33`.

The scope is conditional. The A102 source guard still says that primitive MTT
has not selected the identification of `S1_shared` with the untwisted Fu-Yau
circle. The action above is an automorphism of the four-branch parent family,
not of the single branch `(delta,0)`.

## New no-go: covariance is not invariance

This distinction matters for the HYM Hessian. Let `J_DE` be the canonical
quarter-turn on the diagonal/edge strain multiplicity plane. A covariant
operator family on the four branches obeys

```text
H_{m+1}=J_DE H_m J_DE^{-1}.
```

Every self-adjoint `S3`-equivariant `H_0` extends uniquely by this formula.
Therefore free-orbit covariance retains all six branch Hessian coefficients;
it does not imply `[H_0,J_DE]=0`. The exact counterexample is

```text
H_0=diag(I3,2I3),
H_m=J_DE^m H_0 J_DE^{-m}.
```

The family is perfectly `C4`-covariant, but `H_0` is anisotropic and does not
commute with `J_DE`. Consequently the Fu-Yau parent orbit by itself cannot be
used to claim `H_std=kappa_standard I2` on our observed branch.

## The exact dichotomy

There are now two mathematically distinct exits.

### Lens-redundancy exit

If the four Chern orientations are alternative representatives of one reduced
state, the quarter-turn is genuinely Lens-type redundancy. Foundation v8's
autonomous-descent criterion then requires the HYM operator to be constant on
the reduction fibers. Combining branch-independence with covariance gives

```text
[H,J_DE]=0.
```

The complement-quarterturn theorem then closes

```text
H_std=kappa_standard I2,
h_DE=0,
h_DD=h_EE=kappa_standard>0.
```

### Physical-branch exit

If the four orientations are physical retarded or superselection branches,
they are not quotient redundancy. Covariance relates their Hessians but does
not scalarize any one of them. The selected inverse-Fourier-Mukai/HYM operator
must then be constructed and its `2x2` block computed directly.

## Remaining decision

The old broad source theorem has been replaced by a sharper binary theorem:

```text
prove the C4 parent is Lens redundancy with autonomous HYM descent,
or treat it as physical branch data and calculate H_std directly.
```

Primitive shared-circle/Fu-Yau selection, the typed retarded representative,
and the actual balanced-HYM operator remain open. No observed datum and no
fitted parameter enters this result.
