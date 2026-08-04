# QG Actual DG Source Frontier Synthesis

Date: 2026-07-16

## What changed

The earlier terminal packet did not calculate the metric source map. It first
filled

```text
B0^* P_TT := U_TT
```

and its own packet retained the status
`CANONICAL_PACKET_FILLED_TESTS_PASS_SOURCE_ACCEPTANCE_OPEN`. A later script then
set `source_acceptance=True`. That is a consistent model declaration, but it is
not an independent proof of the source identity. The prior countermodel remains
valid against the old assumptions.

This pass replaces that declaration with displayed maps that can actually be
differentiated.

## New exact chain

On the q79 sheet carrier, the exact opposite-edge intertwiner is

```text
J: (O direct-sum A0) direct-sum A -> Sym(3,R).
```

It is an isometry, respects all six `S3` monodromies, and preserves the `1+2+3`
lanes. On the orientation-fixed polar slice,

```text
Q(f)=exp(Jf),
G(f)=Q(f)^T Q(f)=exp(2Jf),
DG(0)=2J.
```

The map is now also classified intrinsically. If `A` is the cubic q79 sheet
algebra, then

```text
J(a,b)(x,y)=Tr_A(a*x*y)+D^2 N_A|_b(x,y)/sqrt(2).
```

For `A=R^3`, the norm is `N=x1*x2*x3`, so its Hessian is exactly the
opposite-edge block. The regular representation fixes the diagonal block, and
the complement bijection from one sheet to its opposite edge is the unique
`S3`-equivariant atom bijection. This removes the apparent intertwiner signs
and scales without a fit parameter.

The same formula also exposes the branch obstruction. For a generic cubic,

```text
det(J_flat)=(-Disc)^3.
```

At simple ramification its Smith profile has three units and three first-order
zeros, so the coarse finite-flat map has rank three and cannot be the required
global six-lane isomorphism. Newton-Puiseux analysis on the certified
three-blowup cusp resolution gives full sheet-monodromy orders

```text
strict transform, E1, E2, E3 = 2,3,2,1.
```

The earlier order-two root stack is precisely the determinant/sign substack.
Adding the forced order-three root on every `E1` gives the unique minimal full
monodromy completion. On it, `J` descends as a rank-six isometric parallel
bundle isomorphism and its finite orthogonal connection is flat orbifold HYM.
Thus branch continuation is closed at strict same-source minimal tier; primitive
MTT selection of that physical continuation remains open. The later
sheet-symbol theorem below gives the correct Fourier-Mukai relation and rules
out literal equality with a nonzero-Chern full HYM connection.

On the exact `Z64` TT realization,

```text
S(psi)=<c2,psi>e_plus+<s2,psi>e_cross,
G(psi)=exp(2S(psi)),
DG(0)^*e_plus=2c2,
DG(0)^*e_cross=2s2.
```

This `Z64` map now factors through the global q79 carrier rather than merely
landing in the same six-dimensional target. The unique q79 preimages are

```text
f_plus =(1/sqrt(2),-1/sqrt(2),0;0,0,0) in A0,
f_cross=(0,0,0;0,0,1)               in A,
Phi_q79(psi)=<c2,psi>f_plus+<s2,psi>f_cross.
```

Thus `S=J Phi_q79`, `Q_WW=exp(S)`, and `G=Q_WW^T Q_WW`. Helicity fixes the
Fourier plane, the natural root-stack `J` fixes its preimage, polar strain fixes
`Q_WW`, and pullback fixes `G`. On the selected minimal-rootstack TT branch this
source realization is unique up to polarization, frame, and diffeomorphism
gauge and contains no fitted parameter.

The relation to the future inverse Fourier-Mukai bundle is now typed exactly.
For three local spectral eigenlines,

```text
Herm(V)=D direct-sum S direct-sum K,
dim_R(D,S,K)=(3,3,3).
```

The diagonal sheet modes `D` and real symmetric edge modes `S` are exactly the
q79 six-lane strain symbol; the imaginary skew modes `K` are the three
orientation directions. Their `S3` decompositions are

```text
D direct-sum S = 2*trivial direct-sum 2*standard,
K              = sign direct-sum standard.
```

The normalized fiberwise trace overlap on the strain symbol is exactly `I6`.
A shared central circle phase cancels in endomorphism conjugation, while
relative spectral phases rotate each strain edge into its orientation partner.

This is a sheet/Weyl-symbol bridge, not an identity of full connections. The
root-stack connection is flat. A visible `SU(3)` HYM realization with
`c2(V)=9` has

```text
p1(V_R)=-2*c2(V)=-18,
```

so it cannot be isomorphic as a bundle with connection to the flat root-stack
carrier. The literal full-connection identity is closed no-go for a nonzero
Chern realization. After the gerbe branch, inverse Fourier-Mukai local
freeness, and balanced HYM are constructed, the honest dynamic comparison is
one symmetric `2x2` standard-isotypic Hessian block. Exact TT equality requires
`h_DE=0` and `h_DD=h_EE>0`.

There is now an exact symmetry route to those two equalities. The unique
positive `S3`-equivariant map from each sheet to its opposite edge identifies
the two strain copies and defines

```text
J_DE(d,e)=(-e,d),
J_DE^2=-I6,
[J_DE,S3]=0.
```

A real self-adjoint `S3`-equivariant Hessian has six coefficients. Lane
exchange alone leaves four, but commutation with this order-four structure
leaves exactly two:

```text
H=kappa_trivial*(P1 direct-sum P1)
 +kappa_standard*(Pstd direct-sum Pstd),
H_std=kappa_standard I2.
```

Thus quarter-turn invariance forces `h_DE=0` and
`h_DD=h_EE=kappa_standard`; strict stability supplies positivity. This is
currently a conditional physical theorem. A107's Fu-Yau Chern-pair orbit uses
the same abstract quarter-turn matrix, but a single rank-one Chern branch has
an exact order-four no-go. The minimal parent is the four-branch orbit
`(delta,0),(0,delta),(-delta,0),(0,-delta)`.

The shared `Z64` now supplies the parent quarter-turn without a root choice. Its
unique order-four subgroup is

```text
C4=<16>={0,16,32,48},
chi_1(16m)=chi_33(16m)=i^m.
```

On the active Fu-Yau topology its integral action sends the Chern pair around
exactly that four-orbit. This still does not prove one observed branch is
quarter-turn invariant. The exact covariant family

```text
H_m=J_DE^m H_0 J_DE^-m,
H_0=diag(I3,2I3),
```

retains all six branch-Hessian coefficients and has `[H_0,J_DE]` nonzero.
Thus covariance is not invariance. If the four orientations are instead Lens
redundancy and the HYM operator descends autonomously to the quotient, branch
independence plus covariance does imply `[H,J_DE]=0` and hence scalarization.
Whether MTT selects that redundancy interpretation remains open.

The simplest direct algebra action has also been tested and excluded. On the
trial square elliptic cubic the exact degree-three action is

```text
U_theta=diag(-1,i,1).
```

Its direct adjoint on `Herm(3)` has `+1`, `-1`, and `J^2=-1` dimensions
`3,2,4`; moreover `D direct-sum S` mixes into `K` with rank two. Since the
desired `J_DE` has `J_DE^2=-I6`, no basis change can turn this four-dimensional
rotation sector into the required six-dimensional action. Therefore the direct
square-theta adjoint is a closed no-go.

A genuinely nontrivial common-source functor is now constructed on the flat
sheet symbol. For the sheet-permutation bundle `E_D`,

```text
Lambda^2 E_D=sign tensor E_D,
E_S=det(E_D) tensor Lambda^2 E_D.
```

The determinant sign is the root-independent shared-Z64 SpinC line. Realifying
either odd root on `C4` and tensoring with `E_D`, with the imaginary copy
identified with `E_S` by the unique positive opposite-edge map, induces

```text
J_DE=[[0,-I3],[I3,0]]
```

exactly. This action commutes with every `S3` holonomy and is parallel on the
minimal flat root-stack symbol. It is not yet a functor on the nonzero-Chern
inverse-Fourier-Mukai HYM connection. In fact no direct unital unitary or
antiunitary adjoint on `Herm(3)` can realize full `J_DE`: such maps fix the
identity, while `J_DE` sends the trace mode to the edge-sum mode.

The ordinary bundle-functor extension has now also been decided. For a
rank-three connection,

```text
A_dual=-A^T,
A_Lambda2=tr(A)I-A^T.
```

On the trace-free `SU(3)` curvature both preserve the HYM equations and norm,
but their exact action preserves `D`, `S`, and `K` separately. It cannot equal
`J_DE`, which exchanges `D` and `S` and squares to `-I`. Moreover duality sends
`c3` to `-c3`; a nonzero-`c3` chiral branch cannot be complex-linearly
self-dual. Opposite-chirality HYM energy equality is therefore not same-branch
Hessian invariance.

The shared-circle marking decides the proposed Lens shortcut. In the active
topology the vertical basis is the twisted circle `e1` and the marked
`S1_shared=e2`, but `J e1=e2` and `J e2=-e1`. The marked stabilizer has no
order-four element, and the existing `c3=+/-6` construction clutches explicitly
along `S1_shared`. Thus autonomous `C4`/Lens descent is a no-go in the current
marked setup. An unmarked modular replacement is a different construction with
a separate five-row contract, currently `0/5`.

The exact HYM frontier now has two live routes: construct a genuinely nonlocal
same-branch Fourier-Mukai autoequivalence satisfying the new 11-row
kernel/`Ext1`/Hessian contract (currently `2/11` topological rows), or compute
the actual projected `2x2` HYM block directly. Abstract matrix agreement,
free-orbit covariance, direct algebra adjoints, ordinary dual/exterior
transport, and marked-circle Lens descent are no longer admissible shortcuts.

Therefore the exact-support identity is directly verified for this source map:

```text
Pi_exact64 DG(0)^*P_TT = DG(0)^*P_TT.
```

The literal metric derivative gives `C=2I2`; the half-log metric/closure-strain
coordinate gives `C=I2`. This is a new normalization result. It leaves the
selected gapped internal eigenvalue at `lambda=15` but changes the unnormalized
residue.

The associated-bundle Hessian is no longer an unknown matrix. The symmetric
commutant of the real weight-two `SO(2)` representation is one-dimensional, so
under the stated stability and covariance hypotheses it patches globally as

```text
H_e = kappa_e Id_E.
```

Because `h=delta G=2e`, the literal metric-coordinate Hessian is

```text
H_h = (kappa_e/4) Id_E,
kappa_h := kappa_e/4.
```

Thus the old `kappa_STF` notation must be split: the repository's
`(32 pi G_eff)^(-1)` coefficient is `kappa_h`, while the half-log strain
coefficient is `kappa_e=4 kappa_h`.

There is also an exact action reduction. For the most general local,
parity-even, Lorentz-covariant, formally self-adjoint two-derivative metric
operator, the off-shell Bianchi identity gives a rank-four system on five
coefficients. Its one-dimensional nullspace is

```text
(1,-1,1,1,-1),
```

the Fierz-Pauli/linearized-Einstein operator. The same identity excludes an
algebraic mass term. This is a uniqueness theorem under four explicit action
hypotheses, not yet a proof that MTT selects those hypotheses.

## Massless-pole and ultraviolet correction

The computed `lambda=15` compression cannot be the physical graviton pole. At
zero external momentum the existing matrices are exactly

```text
Delta_metric(0) = 4/15 I,
Delta_strain(0) = 1/15 I.
```

They are finite. More generally, any positive compressed spectral measure
supported in `[15,infinity)` obeys

```text
lim_(E->0) E Delta(E) = 0,
```

whereas a normalized massless propagator requires a nonzero limit. The physical
source must therefore contain a coherent internal zero-mode atom. The external
bundle `E_TT` carries helicity two, so this zero-mode internal factor does not
erase the helicity topology. The exact `d_*` rows and `lambda=15` survive as a
gapped correction/suppression channel.

That missing geometric atom is now constructed on the active q79 Fu-Yau
branch. The reconciled topology is

```text
X6_q79 = P_delta x S1_shared,
P_delta -> K3 a principal circle bundle.
```

Connectedness of K3 and both circle factors makes `X6_q79` connected. Fixed
Points I then makes its scalar joint harmonic kernel the one-dimensional space
of constants. With

```text
phi_0=Vol(X6_q79)^(-1/2),
i_0(v)=phi_0 tensor v,
```

the embedding of `E_TT` is isometric and the exact compression is

```text
i_0^*(E+Delta_X)^(-1)i_0=E^(-1)Id_E_TT.
```

The internal residue is therefore exactly one with no fitted parameter. This
does not fix the physical metric residue, which is `kappa_h^(-1)Id_E_TT`, and
does not yet prove that one selected action fuses this massless row with the
`lambda=15` gapped correction.

A second exact no-go corrects the ultraviolet claim. A positive Stieltjes
propagator with massless residue `r0>0` satisfies `Delta(E)>=r0/E`. It cannot
also satisfy `Delta(E)<=C exp(-tau E)/E` for all large `E`. Thus positive
spectral density, a massless pole, and permanent Gaussian damping of the same
physical propagator cannot all hold. The conservative route retains positivity
and the massless pole, treats proper-time damping as removable coarse graining,
and reopens the all-loop ultraviolet-finiteness claim.

## Same-circle advance

The first compatibility clause is now sharply reduced. On a common
correspondence base, let `L_sh` be the pullback of the q79 shared line and
`L_perp` the pullback of the physical transverse weight-one line. TT sees only
their squares. Thus

```text
L_sh^2 ~= L_perp^2
```

if and only if `D=L_sh tensor L_perp^(-1)` is an order-two flat line. At the
finite level, `chi_2` has kernel `{0,32}` and exactly two `Z64` roots,
`chi_1` and `chi_33`, whose quotient is `chi_32`. Every even-weight observable
is blind to this quotient; an odd-weight/spinorial observable detects it.

The local q79 `Dic_3` center, terminal spinorial parity, and ambient Majorana
two-torsion have the same abstract `Z2` representation type. No current source
yet proves that they are the same line/holonomy or chooses one root.

For the actual signed-sheet representation, the universal obstruction is now
computed:

```text
w2=a cup a,
strict Spin iff the sign character a lifts to Z4.
```

The q79 spectral branch divisor has class `6H`. In the exact identity-alignment
test carrier, its pullback to the normalization of the dual cubic has an
irreducible square-free degree-36 norm. Therefore that branch divisor is
irreducible, its complement has `H1=Z6`, and strict Spin is obstructed.

That formerly open alignment-membership test is now executed on the A125/A126
selected-side interval. After the exact inverse-transpose alignment
substitution, Arb/ACB encloses the degree-36 norm and its derivative resultant
for every matrix in the input balls. The resultant excludes zero with absolute
lower bound about `5.37e364`. Hence the branch remains reduced and irreducible
throughout this interval, its complement has `H1=Z6`, and strict Spin is
obstructed on the current executed selected-side carrier.

There is nevertheless an exact `SpinC(3)` lift. If `q1,q2` are the computed
binary lifts of the two transpositions, then `[q1,i]` and `[q2,i]` satisfy the
`S3` relations, generate an order-six image, and project isomorphically to the
signed-sheet representation. Their determinant character `z^2` is exactly the
sheet sign. This closes the representation-level SpinC existence problem.

The determinant/shared-circle finite bridge is now also exact. Since
`H1=Z6`, the only generator images of a homomorphism `Z6->Z64` are `0` and
`32`. The unique nontrivial map sends a meridian to `32`, and

```text
chi_1|_h = chi_33|_h = sheet sign,
chi_2|_h = chi_32|_h = 1.
```

Thus either admissible shared-circle root pulls back to the SpinC determinant
line as a flat line with connection. The determinant bridge requires no root
choice or fitted parameter. The finite same-source map is now also forced:
`S3->Z64` has only the trivial map and the sign-half-turn map, and the
nontrivial SpinC determinant selects the latter.

The central half-turn also closes the old proto-spinor return statement at an
explicit same-source tier. For either odd root the sequence is

```text
+1 -> -1 -> +1,
```

whereas the weight-two metric sequence is `+1 -> +1 -> +1`. On the minimal
odd-plus-even carrier, `g=diag(-1,+1)` canonically gives `D=1-g` and `N=1+g`.
Folding the two-periodic `C2` complex with the corresponding parity projectors
produces a differential `d` with `d^2=0`, rank two, and `im(d)=ker(d)`. This is
an exact, parameter-free Circle-Lens-Nil operator complex: Circle is the shared
`Z64` carrier, Lens is signed-sheet finite transport through its central `C2`,
and Nil is the acyclic difference/norm complex. No literal CLN product or
nesting is inferred.

The same character calculation rules out a tempting overclaim. The nonzero TT
strain `diag(log(2),-log(2),0)` gives `G=diag(4,1/4,1)`, and the half-turn fixes
it. Thus spinorial double return does not force metric strain to vanish. The
world-in-world source nevertheless has the exact zero-defect point `Q_WW=I`.
In the canonical inertial Lorentzian representative (`N=1`, shift zero,
spatial triad `I3`) its coframe is Minkowski and has zero teleparallel torsion,
TEGR scalar, Riemann curvature, Ricci tensor, and Einstein tensor. This is flat
spacetime, not absence of time or space. Dynamic selection of this endpoint
remains open, and with zero stress it is a vacuum only when `Lambda_eff=0`.

Even that condition is not sufficient to select flatness. The exact
plus-polarized Brinkmann metric

```text
ds^2=(x^2-y^2)du^2-2du dv+dx^2+dy^2
```

has determinant `-1`, vanishing Ricci and Einstein tensors, but
`R_uxux=-1` and `R_uyuy=+1`. Its null coframe has nonzero anholonomy. Hence the
same Einstein/TEGR vacuum equation class contains curved helicity-two waves.
Flat-vacuum selection is now reduced to an explicit five-row state/boundary
contract, currently `0/5`, or to a separately derived positive defect
functional with the zero source as its unique physical ground state.

The resulting determinant connection is flat and therefore HYM on the branch
complement. Its `-1` meridian holonomy forbids ordinary smooth extension across
the branch divisor. The interval flex resultant and genus calculation sharpen
the alternative: the selected branch has exactly eighteen ordinary cusps.
Resolving each cusp by the explicit three-blowup SNC resolution and taking the
order-two root stack along the odd-multiplicity components yields a smooth
resolved flat-HYM carrier.

For the full six-lane sheet carrier, that determinant construction has now
been upgraded rather than merely assumed sufficient. The intrinsic cubic map
has determinant `(-Disc)^3`, proving that its coarse extension loses three
directions at simple branching. The full local monodromies on the resolution
are a transposition, three-cycle, transposition, and identity. Therefore the
unique minimal rank-preserving completion has root orders `2,3,2,1`. The
existing `S3`-equivariant `J` then extends as an isometric parallel isomorphism
with a flat orbifold-HYM connection. What remains is primitive physical-branch
selection and the inverse-Fourier-Mukai Hessian/overlap identification, not the
construction of another local six-by-six map.

A literal global comparison with the physical transverse line is, however,
the wrong theorem: the internal determinant/shared line is flat, while the
physical helicity `+2` line over the momentum sphere has Chern number `-4`.
They cannot be globally isomorphic. The correct replacement is now constructed.
The real `k=2/k=62` Z64 plane is the restriction of the continuous `SO(2)`
weight-two representation; associating that fiber to the oriented transverse
frame bundle produces the global helicity bundle with its nontrivial topology.
The `SO(3)`-equivariant TT projector

```text
T_n(S)=P_n S P_n-(1/2)tr(P_n S P_n)P_n
```

globalizes the local `DG`. Its exact `d_*` support identity and internal
`lambda=15` hold fiberwise for the gapped channel. What remains is primitive
MTT promotion of the uniquely minimal strict-same-source root-stack
continuation, its inverse-Fourier-Mukai/HYM operator identification, and a
same-source proof that this covariant observable comes from a local
diffeomorphism-natural spacetime action with two-derivative infrared order. The
source packet also retains
`integral_branch_selected=false`, so the final integral/gerbe source gate has
not been silently promoted.

The action reduction has advanced beyond the old four-hypothesis list. Because
the revised closure functional is a real `C^3` scalar, its finite Hessian is
self-adjoint by symmetry of second derivatives. If the physical response is
promoted through one real local action, formal self-adjointness is therefore not
an independent assumption. Under local diffeomorphism naturality and an at-most
second-order metric equation, the four-dimensional Lovelock classification
then gives the unique nonlinear Einstein-Hilbert completion, up to `Lambda`,
boundary terms, and topological densities. Variation against the same metric
gives the Hilbert stress tensor and

```text
G_mn+Lambda g_mn=(4 kappa_h)^(-1)T_mn=8 pi G4 T_mn.
```

There is no extra stress-normalization knob beyond `kappa_h`. The still-open
source obligation is selection of that local diffeomorphism-natural action and
its two-derivative infrared order, not a new matrix or arbitrary nonlinear
completion.

The direct action exit is now constructive rather than an unspecified search.
An algebraic closure potential `J(S)` cannot produce the graviton kinetic term:
its coframe Hessian has an order-zero principal symbol, whereas the certified
Fierz-Pauli block has symbol `kappa_h p^2 P_TT`. The correct literal
non-closure object is instead the torsion of a coframe,

```text
T^a=d theta^a+omega^a_b wedge theta^b.
```

For a flat metric-compatible teleparallel connection, the independent
quadratic torsion invariants have the unique Einstein-equivalent combination

```text
T_TEGR=(1/4)I1+(1/2)I2-I3,
e R(LC)=-e T_TEGR+2 partial_mu(e T^mu).
```

Thus a closure-anholonomy action with this constitutive vector is exactly
Einstein-Hilbert up to a boundary term and yields all nonlinear classical GR
equations. This introduces no new dimensionless number. The local `Q_WW`
field supplies a spatial-triad candidate. Moreover, because
`G=Q_WW^T Q_WW` quotients local orientation, requiring the coframe action to
descend to this metric with no independent frame modes forces the TEGR vector.
This is now checked directly: pure local Lorentz frame perturbations have bulk
coefficients `2c1+c2+c3` and `-4c1+2c2`; setting both closure-neutral leaves
the unique ray `(c1,c2,c3)=lambda(1/4,1/2,-1)`. The TEGR residual is exactly
zero and the boundary identity gives nonlinear sufficiency. MTT has not yet
selected every premise needed to apply this result globally.

The strict same-source packet now closes the constitutive clause on the
displayed candidate branch. Its source is exactly
`psi -> S(psi) -> Q=exp(S) -> G=Q^T Q`, with no orientation coordinate. The
differential of `r(Q)=Q^T Q` has rank six and a three-dimensional skew kernel.
The metric formula is also no longer an independent observable choice: with
the declared Euclidean metric `delta_I` on `TI`, it is uniquely the pullback
`G_Q(v,w)=delta_I(Qv,Qw)`. In frames this is `Q^T Q`; positivity and the metric
cocycle follow automatically, with no coefficient.
Foundation v8's iff descent criterion therefore makes this kernel neutral for
any autonomous strict completion of the displayed `G` source. A non-TEGR
torsion action would add an unsourced frame degree of freedom and belongs to a
larger modified-teleparallel theory. Thus the direct leading two-derivative
action form is closed on this candidate branch; primitive MTT selection of the
candidate realization itself remains open.

Conditional geometric existence is already enough: the v4 action declares a
globally hyperbolic oriented physical base, so smooth splitting gives
`Y4=R x Sigma3`; orientable three-manifolds are parallelizable. Hence a global
coframe exists, and declaring that frame parallel constructs a flat
metric-compatible teleparallel connection. Lapse and shift are multiplier/gauge
fields rather than numerical knobs. The open clause is now same-source
selection of the displayed `Q_WW` metric-source candidate and the canonical
spacetime realization, not topological coframe existence, frame neutrality, or
an unfixed three-parameter torsion law.

The local same-source coframe formula is also explicit. Select an oriented
Cauchy embedding `i:B->Y4` and type `TP=TB`; then

```text
theta^0=N dt,
theta^a=Q_WW^a_i(dx^i+N^i dt)
```

reproduces the ADM metric with `h=Q_WW^T Q_WW` and satisfies
`det(g)=-N^2 det(Q_WW)^2`; both symbolic residuals are zero. Lapse and shift
are varied constraint fields, not fit parameters. Moreover, the declared
world-in-world transition law
`Q_j=g_I,ij Q_i g_P,ij^(-1)` is exactly the spatial tetrad/solder cocycle.
On the invertible branch, `Q_WW:TB->TI` identifies `TI` automatically with the
internal spatial frame bundle, and `h=Q_WW^* delta` patches globally. The
strict same-source no-extra-map rule also places `B` on a Cauchy support and
types `TP=TB` inside the canonical physical realization. The remaining issue is
primitive selection of that realization, not a missing support map, `TI`
choice, tetrad formula, or cocycle.

The Newton scale has also been classified exactly. The closed q79 topology,
rank-one harmonic projector, and unit internal residue are invariant under
`g_X -> r^2 g_X`, while `V6` and `kappa_h` scale as `r^6`. Consequently the
current scale-free packet cannot determine numerical `kappa_h`. One effective
normalization `V6/G10`, or an equivalent dimensionful primitive together with
the selected dimensionless ratio, is necessary. This retains Theta IV's
one-normalization insight but retires its old `31.8 R1^3` volume formula.

Quadratic data cannot close the remaining action source by themselves. The
explicit family

```text
S_alpha=S_EH+(alpha/kappa_h) integral sqrt(-g) C^3
```

is local and diffeomorphism invariant, has the same value, first variation,
and Fierz-Pauli Hessian at flat space for every `alpha`, but different cubic
vertices. This closes a nonlinear-selection no-go and proves that the
infrared-order clause is indispensable. The corpus now presents two honest
exits: a direct selected two-derivative closure action, or the A51-A53 product
spectral action together with selected base/moments/Lorentzian data and a
controlled Einstein infrared limit. The spectral exit is a superset route and
contains Weyl curvature; it is not already pure GR.

That spectral infrared problem is now partially calculated. The active A49
`96x96` finite Dirac operator has only `Y_u,Y_d,Y_e,Y_nu`, so the Majorana
spectral invariants are exactly `c_R=d_R=0` on this branch. Under A53's
explicit one-atom premise,

```text
beta^2/Lambda^2 = 20/(3 tau_int),
epsilon_W(p) <= (3 tau_int/20)(p/Lambda)^2.
```

Thus the Weyl correction in the retained `a4` action is quadratically
suppressed in the infrared and its dimensionless ratio depends only on the
exact `tau_int`, not on profile `f0`. This is not yet the full Einstein-limit
theorem: A53 does not unconditionally select the point measure, and no bound on
the omitted heat-kernel remainder has been supplied. The same moments give the
bare curvature-equivalent vacuum magnitude `6 Lambda^2/tau_int`, so they do
not solve `Lambda_eff`.

## Interacting low-energy quantum closure

The free sector is no longer the quantum endpoint. Composing the q79
Einstein/TEGR action with standard background-field BRST/BV quantum-GR EFT
gives an interacting observable functor at the same imported-parity standard
already used by the closed SM observable functor. For a connected Einstein
graph,

```text
D=4L+2V-2I,
L=I-V+1,
D=2L+2.
```

Thus only finitely many local diffeomorphism-invariant counterterms are needed
at every declared finite loop/derivative order. The nonanalytic long-distance
quantum terms are UV-independent once the low-energy spectrum, `kappa_h`, and
causal state are fixed. This closes interacting low-energy quantum-GR EFT
parity, not a primitive MTT derivation of the measure.

The UV boundary is equally exact. Pure `Lambda_eff=0` Einstein gravity has no
physically relevant on-shell one-loop divergence, but the two-loop
Goroff-Sagnotti `Riemann^3` counterterm is nonzero. The finite internal carrier
does not alter this spacetime power counting. Therefore `kappa_h` and
`Lambda_eff` cannot be the complete all-scale interacting parameter set unless
MTT supplies a genuine UV completion.

## Selected heterotic UV route

The route-selection question is no longer open. Permanent Gaussian damping of
the physical massless propagator is incompatible with positive Stieltjes
spectral weight; finite internal projection leaves four-dimensional loop
power counting unchanged; and the present spectral-action packet lacks a full
remainder, measure, and continuum theorem. The strongest route compatible with
all closed q79 geometry is heterotic string inheritance on the selected
`q=79/F` Fu-Yau branch.

The inheritance statement is exact but conditional: if one same-source q79
background supplies an exact anomaly-free modular heterotic `(0,2)` SCFT,
tachyon-free GSO projection, factorization, q79 heterotic quantum-BV vertices,
and a tadpole/IR prescription, every fixed-genus fixed-multiplicity amplitude
has no local ultraviolet divergence. At genus one the modular fundamental
domain obeys `Im(tau)>=sqrt(3)/2`, removing the point-particle
short-proper-time region. Higher-genus boundary components are treated through
factorization and infrared degeneration data.

The current contract has five of twelve rows available and two partial rows.
The W8 target-space row now contains an explicit smooth splitting-conic K3,
an isomorphic `U(1)^2` incidence GLSM with exact paired `(2,2)` anomaly and
`E/J` identities, and the divisor source `delta=H-L` with `delta^2=-4`.
It preserves the untwisted marked shared circle and the exact K3-reference
allocation `9+11+4=24`.

The local torsion anomaly is no longer open. Its exact matrix is

```text
A = [[ 2,-2],
     [-2, 2]] = 2 delta delta^T,
```

and the compact TLSM equation closes with integral rows `M=(1,-1)`,
`N=(4,-4)` and `k^2=2`; the shared second circle remains unshifted. An
anomaly-equivalent locally free rank-12 Fermi monad has `c1=0,c2=20`.

That aggregate is not the physical `SU(3) x SU(9)` bundle. The incidence
Picard parity forces every line-bundle complex with `c1=0` to have even `c2`,
so it cannot split into `9` and `11`. Moreover, the standard compact TLSM
bundle is pulled back from K3 and has `c3=0`; it cannot realize the topological
shared-circle clutching target `c3=+/-6`.

The positive topological target is now simultaneous rather than piecemeal.
With `u=Hhat cup t`, smooth non-pullback `SU(3)` mapping-torus bundles realize
`c2=9u` and `c3=+/-6`. On the selected rank-one Fu-Yau complex structure,
`u=(i/2) Theta wedge conjugate(Theta) wedge H` is a closed integral `(2,2)`
representative, while the orientation class is `(3,3)`. Thus topology and the
necessary Hodge-type condition are no longer blockers. This does not yet
construct a holomorphic bundle or HYM connection.

The same-carrier twisted-spectral execution has reached A151: all 90 root
tubes and the exact 92-column integral `H2` presentation are closed, as are
the floating `8 x 92` period table and exact effective `Z^90` quotient. Exact
interval certificates cover 16 of 71 supports with L1 weight 36 of 123. The
covariant z-chart adapter and its first native row are closed. The remaining
W8 object is the other 55 interval rows, the weighted frozen-carrier branch
decision, inverse-gerbe twisted spectral sheaf and inverse-transform local
freeness, balanced HYM, differential Bianchi identity, global GSO currents,
and exact IR `(0,2)` SCFT; a non-Abelian current-algebra construction remains
the independent alternative.

The partial W9 modular row is also substantial: the selected `F_3^2` gerbe cocycle is
modular covariant on all 81 twist sectors, and those sectors form exactly seven
modular orbits of sizes `1,8,8,8,8,24,24`. Thus the missing torus construction
requires seven seed character blocks rather than 81 unrelated blocks. The
selected twisted group algebra is exactly `Mat_3(C)`, with one irreducible
three-dimensional projective module and normalized finite topological torus
index one. The seven orbit stabilizers have orders `24,3,3,3,3,1,1`; the finite
invariance equations have rank 74 and nullity seven. Finite symmetry therefore
cannot reduce the seven analytic seeds further. The oscillator/gauge
characters, `Gamma(3)` multipliers, spin structures, GSO phases, full
factorization, exact q79 worldsheet CFT, and q79 BV realization are not yet
computed.

Fixed-genus perturbative UV inheritance does not establish convergence of the
sum over genera or a nonperturbative definition. Those remain a separate final
gate after the exact worldsheet packet closes.

## Primitive-selection cutset

The revised papers do not secretly select the physical branch. Foundation v8
declares the Lorentzian physical completion as supplied data;
Projection-Admissibility v2 says that admissibility exit does not select a new
state; Fixed Points I gives uniqueness only inside a declared coherent sector
for a fixed flow. An exact countermodel with two isomorphic branches, each with
`C_b(x)=x^2` and `Phi_t(x)=exp(-2t)x`, satisfies all branch-internal hypotheses
and has one unique minimizer per branch. Branch swap preserves every invariant
datum, so no invariant theorem can choose one.

At least one branch-noninvariant datum is therefore necessary. One discrete
axiom `A_QG`, selecting the q79/`Z64`/`Q_WW` minimal-rootstack Lorentzian gauge
class with the finite Reynolds action, is sufficient and adds zero continuous
knobs. After it is adopted, all remaining geometry/operator choices are already
unique up to gauge. Deriving `A_QG` rather than adopting it requires a
target-independent upper-dynamics functional on physical realizations with a
strict q79 gap.

## Current frontier

The old `DG`, Galerkin/Hessian-shape, classical-action, free-graviton, and
low-energy-interaction blockers are closed at their declared tiers. The
remaining frontier is now exactly three source questions:

1. **Primitive physical realization.** Either derive a target-independent
   upper-dynamics realization functional with a strict q79 gap, or explicitly
   adopt the one discrete axiom `A_QG`. The normalized finite `S3` Reynolds action computes
   `h_DE=0` and `h_DD=h_EE=kappa_e>0` with zero dimensionless fits. The
   continuum inverse-Fourier-Mukai/balanced-HYM contract remains `2/11`, but is
   an optional stronger completion rather than a blocker for the finite tier.
2. **Effective values and state.** Derive or supply the one Newton/action
   normalization and `Lambda_eff`. If a unique Minkowski universe is intended,
   separately select causal/initial/asymptotic state data or close the `0/5`
   positive-ground-state contract. Field equations correctly admit curved
   Ricci-flat waves and cannot perform state selection.
3. **Heterotic worldsheet and nonperturbative completion.** The primary UV
   route is selected and its fixed-genus inheritance theorem is closed
   conditionally. Complete the heterotic Fermi bundle and local torsion anomaly
   matrix on the explicit incidence GLSM, the global differential gerbe and
   non-pullback Bianchi identity, the exact IR `(0,2)` SCFT, seven modular seed characters with
   GSO/factorization, q79 BV vertices, and tadpole/IR prescription. Then address
   the independent all-genus convergence or nonperturbative-definition gate.

No dimensionless gravity-shape parameter remains at the two-derivative tier.
There are exactly two effective classical law coordinates, `kappa_h` (or
`G_eff`) and `Lambda_eff`; free quantization adds none. Higher-derivative EFT
coefficients are finite in number at each fixed order but are not yet selected
numerically by MTT. Newton/Planck therefore remains one metrology problem, and
stress response has no independent gravitational normalization after
shared-action selection.

## Supersession

`Selected_Core_B0_TT_Source_Theorem_v1` is retained as historical packet
algebra but is superseded as an unconditional source proof. The present
certificate is the controlling status statement for the `DG` frontier.
