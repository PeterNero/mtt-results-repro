# MTT Foundational Geometry Reconciliation

Date: 2026-07-15

Status: current authority for dimensional and topology language until a stronger
same-source globalization theorem is proved.

## Executive Decision

The calculation program does **not** need to restart. It does need one
foundational repair before further papers claim that all layers are one selected
geometry.

The original "three-dimensional world pushed into three dimensions" idea is
mathematically coherent when it is represented by a local rank-nine map

```text
Q_x in Hom(T_x P, T I_x) ~= Mat(3,R),
```

not by multiplying manifold dimensions. The pointwise internal embedding
`E -> P` with three-dimensional base and three-dimensional fibers has ordinary
total dimension six. A `3 x 3` array instead counts the nine components of the
local comparison map `Q_x`.

The exact local decomposition is

```text
1 ordering component + 9 world-in-world map components
  = (1 ordering + 3 orientation components)
    + (1 scalar + 2 diagonal-shape + 3 shear components)
  = 4 + 6
  = 10.
```

This reconciles the original `1 + 3 x 3` picture with the later `4 + 6`
physical realization at the level of local carrier components. It does **not**
by itself prove that the six local components globalize to the selected compact
six-manifold, that the two-dimensional block is a Lens base, or that physical
time is a compact circle.

## 1. Three Objects That Must Not Be Confused

### 1.1 Proto-local fibered space

The proto-spinor papers define an oriented three-manifold `P` and a fibered
space `E -> P` with a three-manifold `I_x` over every `x`. If this is an ordinary
smooth fiber bundle, then

```text
dim(E) = dim(P) + dim(I_x) = 3 + 3 = 6.
```

This is consistent with the papers' statement that the construction is an
intermediate encoding and not the underlying ten-dimensional realization.

### 1.2 World-in-world comparison field

To formalize "each outer direction receives an internal direction," introduce

```text
Q in Gamma(Hom(TP, TI)).
```

At each point, `Q_x` is a real `3 x 3` matrix and has nine components. This is a
field/order parameter over `P`; it is not a nine-dimensional manifold fiber.

### 1.3 Physical ten-dimensional realization

The string, flux, fixed-point, and q79 papers use a physical realization of the
form

```text
M10 = Y4 x X6.
```

This is an ordinary manifold-dimension statement. It can be a downstream
globalization of the world-in-world carrier only after a source theorem maps
the six non-orientational components of `Q` to the tangent/operator data on
`X6`.

## 2. Exact Local Algebra

Equip the two three-dimensional tangent spaces with oriented Euclidean metrics
and restrict to `det(Q)>0`. Polar decomposition gives uniquely

```text
Q = R S,
R in SO(3),
S = (Q^T Q)^(1/2) in SPD(3).
```

The dimensions are

```text
dim SO(3) = 3,
dim SPD(3) = dim Sym(3,R) = 6.
```

At the identity, the Frobenius-orthogonal decomposition is

```text
Mat(3,R) = so(3) direct_sum Sym(3,R),
Sym(3,R) = R I direct_sum D0 direct_sum O,
dim(R I, D0, O) = (1,2,3).
```

Here `D0` is the traceless diagonal subspace and `O` is the symmetric
off-diagonal subspace. The three summands are pairwise orthogonal under
`<A,B>_F = tr(A^T B)`.

This proves the component census

```text
1 + 3 x 3 = (1+3) + (1+2+3) = 10.
```

It does not prove that the `SO(3)` orbit coordinates are physical spatial
coordinates. In a field theory on `P`, they are local frame/orientation data;
the three spatial coordinates are already the coordinates of `P`. A physical
identification requires the coframe and synchronization map.

## 3. Why Nil Appears Naturally

The same invertible matrix has a unique positive-diagonal QR/Iwasawa form

```text
Q = K A N,
K in SO(3),
A = positive diagonal matrices,
N = upper unitriangular 3 x 3 matrices.
```

The dimensions are `3+3+3`. Split

```text
A = A_central x A_traceless,
dim(A_central) = 1,
dim(A_traceless) = 2.
```

An element of `N` is

```text
n(x,y,z) = [[1,x,z],[0,1,y],[0,0,1]],
```

with multiplication

```text
n(x,y,z)n(x',y',z')
  = n(x+x', y+y', z+z'+x y').
```

Thus `N` is the real three-dimensional Heisenberg group. Quotienting by its
integer lattice gives the standard compact `Nil3` manifold. This is a genuine
mathematical reason that a three-dimensional nil sector is natural in the
world-in-world `3 x 3` carrier.

The Iwasawa split is a direct coordinate/group decomposition, but it is not the
same as the Frobenius-orthogonal polar split. A selected MTT Hessian or metric
must prove that the two descriptions are compatible in the physical branch.

## 4. The `1+2+3` Carrier: Correction to the Nested-Flag Reading

The earlier A45 result proved a correct conditional linear-algebra statement:
if a complete flag of dimensions `1<2<3` is supplied, it is unitarily
equivalent to

```text
p1 = diag(1,0,0),
p2 = diag(1,1,0),
p3 = I3.
```

It did not prove the missing premise. Three bundle ranks `1,2,3`, even with a
verbal reuse hierarchy, do not by themselves supply bundle injections making
a complete flag. The Book says that the three bundles add `1`, `2`, and `3`
filter directions and that their vertical Laplacians commute. That supports
three incremental lanes more directly than one globally ordered sheet flag.

The q79 degree-three spectral cover now supplies the correct global carrier.
For the finite locally free cover `pi:C->K3`, put

```text
A = pi_* O_C,                         rank(A)=3,
p_cen = (1/3) unit o Tr,              rank(im p_cen)=1,
A_0 = ker(Tr),                        rank(A_0)=2.
```

Since `Tr(1)=3`, `p_cen` is an idempotent and

```text
A = O direct-sum A_0.
```

Pulling these carriers to `X6_q79` and twisting every lane by the same
shared-circle line/local-system carrier gives

```text
H_CLN = L_shared tensor (O direct-sum A_0 direct-sum A),
rank(H_CLN)=1+2+3=6.
```

The rank-one and rank-two lanes are orthogonal trace and trace-zero sectors;
the rank-three lane is a reused full copy. They are not nested sheet choices.
This distinction is forced globally: the q79 spectral surface is connected,
so its three sheets have transitive monodromy and no individual sheet can be
selected everywhere without splitting the cover.

On the unbranched locus the canonical orientation correction

```text
rho_plus(sigma)=sign(sigma) P_sigma
```

sends all six sheet permutations into `SO(3)`. The q79 map to the elliptic
hyperplane linear system is surjective and has ordinary tangencies, so the
actual sheet monodromy is `S3`. Its inverse image in `Spin(3)` is the non-split
binary dihedral group `Dic_3` of order 12. Exact quaternion generators close
the local braid lift; the remaining Spin question is the finite central sign
of the global q79 branch-complement relators.

These results are recorded in
`MTT_Selected_q79TraceSplitCLNCarrierAndWorldInWorldBridge_v1` and
`MTT_Selected_q79SignedSheetSpinLiftReduction_v1` in the SM-parity proof repo.

## 5. Circle, Lens, and Nil: Local Versus Global

### Circle

The shared circle should be represented as common `U(1)` phase/holonomy data
acting in every lane. It must not be counted again as an extra Cartesian
coordinate after it has been used as a fiber or phase bundle.

Physical Lorentzian time should be a noncompact oriented bookkeeping order, or
the universal-cover lift `R -> S1` of a phase variable. A literal compact time
circle would introduce closed-time identifications not derived in the corpus.

### Lens

The local rank-two/proto-spinor lane naturally supplies a projective two-sphere:
the projectivization of a complex two-component spinor is `CP1 ~= S2`. A circle
bundle of Chern number `p` over `S2` has total space `L(p,1)`. This gives a
lawful route to `L(3,1)`, but the corpus still needs a same-source theorem that
selects Chern number three and identifies its circle with the common phase
bundle.

The two diagonal Iwasawa coordinates alone are noncompact and do not prove Lens
topology.

### Nil

The upper-unitriangular `N` sector is already the Heisenberg group, so its
integer quotient gives `Nil3` without a dimensional analogy. What remains is
to derive the lattice and metric/flux data from the selected MTT source.

### No literal manifold nesting

The string

```text
S1 inside Lens3 inside Nil3
```

is not a valid literal nesting of those three manifolds. Lens and Nil are
different circle-bundle total spaces (over `S2` and `T2`, respectively). The
valid recursive object is a filtration of carrier/operator data, with possible
global circle-bundle realizations supplied separately.

## 6. The Two Current Global Six-Manifold Candidates

### Lens-Nil product model

The corrected smooth model

```text
X6_LN = L(3,1) x Nil3
```

is a genuine six-manifold and supports an explicit product Dirac family. It is
useful as an effective neutral-sector or local-normal-form model. It is not
currently selected as the physical compactification.

### q79 rank-one Fu-Yau model

The active compactification branch is topologically

```text
X6_q79 = P_delta x S1_shared,
```

where `P_delta` is the nontrivial circle bundle over K3 and the second circle is
topologically trivial. This branch supports the current c3, spectral-cover,
gerbe, HYM, and Bianchi program.

The two spaces are not the same topology. Over the reals,

```text
b1(L(3,1) x Nil3) = 2,
b1(P_delta x S1_shared) = 1.
```

Therefore no paper may identify them as the same manifold without an explicit
duality/effective-reduction theorem. The recommended interpretation is:

```text
global physical candidate: q79 Fu-Yau X6,
CLN: obstruction/rank/operator filtration on that candidate,
Lens-Nil product: auxiliary local/effective model.
```

## 7. Corpus Disposition

| Corpus layer | Current status | Required wording/action |
| --- | --- | --- |
| B0 obstruction paper | Retain as a conditional three-profile taxonomy | Remove `exactly three and only three` unless the descent category is specified; flat circle holonomy does not require nonzero curvature; 10D is not derived there because `dim Y=4` is assumed. |
| World-in-World Genesis | Retain as generative/conjectural architecture | Treat `P` and `E -> P` as intermediate encodings; introduce `Q in Hom(TP,TI)` for the `3 x 3` idea; do not call causal reconstruction a proof selecting dimension four. |
| Proto-Spinor v4 | Retain conditionally | The `Spin(3)` lift follows after the discrete-return premise; Dirac/Weyl/twistor are common-carrier encodings only after Lorentzian tetrad/connection data are supplied. |
| Closure-Strain Geometry | Retain its local normal-form layer | Replace the loose strain tuple by the `3 x 3` tensor where appropriate; a positive Hessian does not select one radial Higgs direction without a one-dimensional quotient theorem. |
| Unified ten-dimensional action | Retain as an action ansatz | It imports metric and Einstein-Hilbert structure; it is not a derivation of GR or the full SM. |
| Fixed Points I and corrected analytic lemmas | Retain conditionally | State domains, strong commutation, invariant sets, coherent-sector coercivity, and the distinction between stabilization time and physical time. |
| Fixed Points II v2 | Major correction required | `S1 x T2 x T2 x T2` is seven-dimensional; use a genuine `X6` and treat the common `U(1)` as bundle/phase data rather than another factor. |
| Book v9 | Exposition, not proof authority | Keep `4+6` and the reuse hierarchy as the canonical model, but mark time/space selection and gauge-group inevitability as conditional on the later source theorems. |
| A45 nested projector source interpretation | Retain only conditionally | The displayed complete-flag matrices are correct if inclusion maps are supplied. Replace their claimed native source with the q79 trace/trace-zero/full `1+2+3` carrier unless a separate nested-flag theorem is proved. |
| Old Iwasawa `c3=6` construction | Retire as proof source | Its displayed Chern forms/connection do not define the claimed bundle. It remains a structural clue only. |
| `L(3,1) x Nil3` packet | Retain as an auxiliary candidate | Do not call it the selected q79/Fu-Yau geometry. |
| q79 A102-A135 branch | Strongest current global branch | Exact/certified results survive. The selected gerbe/period branch, balanced HYM/Bianchi completion, and global MTT source bridge remain active. |
| finite `27 x 27`, SM-parity/profile packets | Retain at their declared tier | Their finite algebra and replay/profile equalities survive this repair; full physical equivalence still needs the same-source globalization and continuum EFT theorem. |

## 8. What Survives Without Recalculation

The following work does not depend on choosing the wrong dimension story and
therefore should not be restarted:

- exact finite arithmetic and CRT/q79 branch results;
- finite rank-signature, family/gauge representation, and anomaly checks;
- the internal `27 x 27` finite-algebra calculations at their stated tier;
- the exact TT-support and `3 x 3` closure-strain decompositions;
- fixed-point functional analysis once attached to a corrected six-manifold and
  supplied with its stated analytic hypotheses;
- A103-A207 topology, spectral-cover, monodromy, period, and interval work on
  the explicit q79 branch, including all seventy-one selected E32 thimbles,
  their integer-weighted enclosure, and the frozen-carrier decision.

The claims that must be revised, rather than recalculated, are the claims of
unique dimensional necessity, literal Circle-Lens-Nil product/nesting, compact
circle equals physical time, and automatic identity of the Lens-Nil and Fu-Yau
geometries.

## 9. Most Promising Direction

The best unified route is:

1. Adopt `Q in Hom(TP,TI)` as the precise world-in-world variable.
2. Keep the proved local polar quotient `9=3+6`: three orientation directions
   and six symmetric strain directions.
3. Use the now-proved q79 trace/trace-zero/full carrier as the global
   `1+2+3=6` CLN target; do not globally order the three spectral sheets.
4. Compute the central signs of the q79 `S3` branch-complement relators. This
   decides strict `Spin(3)` versus a possible shared-circle `SpinC` repair.
5. Construct the same-source real-carrier map and emit the actual `Q`, or the
   equivalent selected closure-Hessian endomorphism, on the signed q79 carrier.
6. Extend that carrier through the branch locus and prove compatibility with
   the eventual inverse-Fourier-Mukai/HYM connection. This is the physical
   world-in-world-to-q79 intertwiner.
7. Derive the Lens Chern class and Nil lattice only as additional topology if
   they are needed; do not use them as substitutes for the q79 global space.
8. Treat the A136-A207 E32 interval program as closed. All 71 selected thimbles
   and the weighted sum are certified; A207 rejects the frozen height-four
   carrier. Remove that carrier and continue only on other selected covariant
   carrier branches. The computation began with a first full ball
   centered at `0.61634458064238262 + 1.58329472957163 i`, has radius
   `1.4359496802285323e-5`, and lies below the A134 per-unit fallback by
   `8.727105126516604e-6`. A137 also closes the coefficient-minus-three d061
   ball with radius `1.2423092840663232e-5`. A138 closes the
   coefficient-plus-three d019 ball with radius `2.853320921758496e-7` and
   installs a reusable ranked frontier ledger. A139 append-only closes the
   coefficient-plus-two d028 ball with radius `5.072241506809406e-6`. A140
   closes the coefficient-minus-three d020 ball with radius
   `2.9053709624804473e-6` and installs a reusable queue-head append builder.
   A141 uses that builder unchanged to close the coefficient-plus-one d062
   ball with radius `1.4539264334700876e-6`. A142 closes the
   coefficient-minus-three d021 ball with radius `6.163389905111672e-6` after
   replacing the invalid cutoff-nearest-pair shortcut by a certified-node
   pair selector in both the main and tail transports. A143 applies that
   stronger method uniformly to close the coefficient-plus-two d029 ball with
   radius `2.6350986672696312e-6`. A144 closes the borderline
   coefficient-minus-three d005 ball using a 120-digit, order-64 main transport;
   its full radius is `4.783742618030829e-6`. A145 closes the
   coefficient-plus-three d057 ball by carrying an uncompressed
   physical-generator zonotope instead of repeatedly reboxing transported
   errors. Its full radius is `1.640566262040011e-5`. Intermediate endpoint
   radii are not monotone, so aborted probes are not no-go certificates. A146
   reuses the same frozen zonotope builder to close the coefficient-minus-two
   d037 ball with full radius `7.755247146690182e-7`. A147 combines the same
   zonotope builder with a geometry-only null-homotopic route scan and closes
   the coefficient-plus-one d060 ball with full radius
   `5.63375292017554e-6`. Its main transport now consumes the cutoff-period
   ball already certified by the tail packet, including explicit binary64
   serialization inflation. A148 applies that same-source handoff to the
   coefficient-minus-one d087 row. A geometry-only scan certifies 534 routes;
   the selected `(0.25,0,0.74)` route gives main radius
   `4.921072286600216e-8` and full radius `4.365527402683257e-6`. A149 and A150
   close d011 and d086 with full radii `2.647258515509066e-6` and
   `2.523348872074394e-6`. A151 executes the first complete native `z`-chart
   row, d048, using A123 projective covariance and the interval-isolated `L2=0`
   wall; its full radius is `1.1264182253611922e-7`. The chart-parametric
   source is a byte-certified conservative extension: its `y` specialization
   reconstructs the recorded historical transport, augmented-main, and
   full-splice hashes exactly. A152 closes d088 after refining a correctly
   rejected 48-cell tail to the established 384-cell partition. A geometry-only
   scan accepts 527 of 1122 routes; the selected `(0.35,0.01,0.82)` route gives
   main radius `4.0606162630066217e-7` and full radius
   `5.876571353979899e-7`. A153 closes d033 across a narrow conditioning
   pocket: 171 accepted zonotope steps reject 84 noncontractive or locally
   over-budget proposals and finish with main radius `6.326398650143199e-7`.
   Its tail-dominated full radius is `4.933663213080309e-6`. A154 closes d035
   on the certified `(0.20,0,0.74)` route: 191 accepted steps and 97 rejected
   trial steps give main radius `1.4173551537312103e-6`, and the full splice
   radius is `3.893695826207023e-6`. A155 closes coefficient-plus-two d063 on
   the scanner-selected `(0.20,0.02,0.78)` route. Its 100 accepted steps and
   17 rejected trial steps give main radius `3.4309395125334205e-6`; the full
   splice radius is `5.04381816313071e-6`. A156 closes coefficient-minus-one
   d026 on the scanner-selected `(0.20,0,0.74)` route. Its 148 accepted steps
   and 46 rejected trial steps give main radius `1.330671149301234e-6`; the
   full splice radius is `1.8933050220937277e-6`. A157 closes
   coefficient-plus-one d032 after the deeper radial selector identifies its
   correct colliding pair. On `(0.45,-0.02,0.86)`, 100 accepted steps and 33
   rejected trial steps give main radius `2.0334266570578483e-7`; the full
   splice radius is `2.3554023620420143e-6`. A158 closes
   coefficient-plus-one d030 and corrects the orientation gate to consume the
   existing compact-H1 synchronization theorem: only the two holomorphic rows
   select orientation, while the three higher meromorphic rows retain
   puncture-lift dependence. Its 91 accepted steps and 24 rejected trials give
   main radius `6.576746775026099e-8`; the full splice radius is
   `1.4630221993883199e-6`. A159 closes coefficient-plus-one d085 on the
   certified `(0.20,0,0.70)` route, reusing the cutoff-period balls already
   proved by its 384-cell tail. The order-20 interval transport retains the
   unchanged local remainder gate, accepts 148 steps, rejects 53 trials, and
   gives main radius `1.1901906201071195e-5`; the full splice radius is
   `1.8597572761791529e-5` and contains the independent floating center. The
   A160 closes coefficient-plus-one d010 on the scanner-selected
   `(0.20,-0.01,0.65)` route. A completed compressed-frame attempt is rejected
   above the selected main-radius cap; the same order, precision, local gate,
   node, tail, and route close under the physical-generator zonotope. Its 193
   accepted steps and 102 rejected trials give main radius
   `9.198311075311998e-7`; the full splice radius is
   `4.560701455602612e-6` and contains the independent floating center. A161
   closes coefficient-plus-one d012 on the scanner-selected
   `(0.32,0.01,0.86)` route. Its order-20 physical-generator zonotope accepts
   190 steps and rejects 100 trials, giving main radius
   `5.743632409585513e-7`; the 384-cell tail splices to full radius
   `2.3084341584933558e-6` with independent-center containment and positive
   fallback margin. A162 closes coefficient-plus-two d017 despite its more
   weakly conditioned node. The scanner-selected `(0.45,0.01,0.86)` route has
   critical clearance `0.010732452056156522`; its order-20 zonotope accepts 182
   steps and rejects 95 trials, giving main radius `3.831653826366047e-7` and
   full radius `1.8720345043021782e-6` with independent-center containment.
   A163 then closes coefficient-minus-two d051 through its narrow
   critical-value tube on the radial-class `(0.2,0,0.74)` representative. Its
   order-20 zonotope accepts 259 steps and rejects 153 guarded trials, giving
   main radius `1.1786789306105185e-6` and full radius
   `2.019519840246176e-6` with independent-center containment. The certified
   A164 closes coefficient-plus-one d055 on the scanner-selected
   `(0.6,0.01,0.65)` route. Its order-20 zonotope accepts 243 steps and rejects
   145 guarded trials; the intermediate enclosure contracts under later
   transport to main radius `1.3338361979199125e-6`, and the full splice radius
   is `4.647876217234171e-6` with independent-center containment. A165 then
   closes coefficient-minus-three d034 on the radial-class `(0.2,0,0.74)`
   representative. The default 384-segment endpoint tail was correctly
   rejected because its orientation intervals overlapped; the same-geometry
   768-segment refinement closes the tail without changing the selected path
   or sign rule. Its order-20 zonotope accepts 288 steps and rejects 183
   guarded trials, giving main radius `2.20656062847174e-6` and full splice
   radius `8.64753941698382e-6` with independent-center containment. The A165
   ledger was 30/71 support and L1 weight 55/123. The finite y-chart queue was
   thereby exhausted, with coefficient-plus-three d059/selected_042 frozen as
   the native z-chart head. A166 now closes that row on the ranked
   `(0.2,0,0.82)` route. Its 384-cell tail radius is
   `3.2196170278442353e-9`; the order-20 zonotope accepts 74 steps and rejects
   21 guarded trials, giving main radius `8.601425856598232e-8` and full
   splice radius `1.2486213707418872e-7` with independent-center containment.
   The A166 ledger was 31/71 support and L1 weight 58/123, with
   coefficient-minus-two d031/selected_048 frozen next. A167 now closes d031
   on the ranked `(0.2,0,0.65)` route. Its 384-cell tail radius is
   `1.0621430429624825e-8`; the order-20 zonotope accepts 132 steps and rejects
   67 guarded trials, giving main radius `1.816473192839754e-7` and full
   splice radius `2.675095345239243e-7` with independent-center containment.
   The A167 ledger was 32/71 support and L1 weight 60/123, with
   coefficient-minus-two d039/selected_037 frozen next. A168 now closes d039
   on the ranked `(0.45,-0.01,0.86)` route. Its refined 96-segment tail radius
   is `1.4066956168790059e-6`; the order-20 zonotope accepts 103 steps and
   rejects 32 guarded trials, giving main radius `1.0881261871947691e-7` and
   full splice radius `1.5605798893147951e-6` with independent-center
   containment. The A168 ledger was 33/71 support and L1 weight 62/123, with
   coefficient-minus-one d014/selected_059 frozen next. A169 now closes d014
   on the ranked `(0.2,0,0.65)` route. Its refined 768-segment tail radius is
   `1.1550937359383619e-8`; the order-20 zonotope accepts 75 steps and rejects
   23 guarded trials, giving main radius `1.2239440876842448e-7` and full
   splice radius `1.8464276241303426e-7` with independent-center containment.
   The A169 ledger was 34/71 support and L1 weight 63/123, with
   coefficient-minus-two d075/selected_067 frozen next. A170 now closes d075
   on the ranked `(0.2,0,0.65)` route. Its 384-segment tail radius is
   `5.82789970593467e-6`; the order-20 zonotope accepts 149 steps and rejects
   55 guarded trials, giving main radius `2.127205331505899e-7` and full splice
   radius `6.12873136418557e-6` with independent-center containment. The
   The A170 ledger was 35/71 support and L1 weight 65/123, with
   coefficient-minus-two d018/selected_054 frozen next. A171 now closes d018
   on the ranked `(0.45,-0.01,0.86)` route. Its 384-segment tail radius is
   `1.2428286488841425e-6`; the order-20 zonotope accepts 111 steps and rejects
   55 guarded trials, giving main radius `1.1239108844990107e-7` and full
   splice radius `1.4017736589266863e-6` with independent-center containment.
   The A171 ledger was 36/71 support and L1 weight 67/123, with
   coefficient-plus-one d001/selected_033 frozen next. A172 now closes d001 on
   the ranked `(0.55,0.03,0.86)` route. Its 384-segment tail radius is
   `5.4652383241204927e-7`; the order-20 zonotope accepts 117 steps and rejects
   36 guarded trials, giving main radius `4.5844626040661814e-6` and full
   splice radius `7.0299094261372383e-6` with independent-center containment.
   The A172 ledger was 37/71 support and L1 weight 68/123, with
   coefficient-plus-three d046/selected_045 frozen next. A173 now closes d046
   on the ranked `(0.45,0.02,0.70)` route. Its same-contour 768-segment tail
   radius is `1.0406598907053424e-6`; the order-20 zonotope accepts 164 steps
   and rejects 66 guarded trials, giving main radius `6.883023908842079e-7`
   and full splice radius `2.0140664531709267e-6` with independent-center
   containment. The A173 ledger was 38/71 support and L1 weight 71/123, with
   coefficient-minus-one d089/selected_032 frozen next. A174 now closes d089
   on the ranked `(0.35,0,0.70)` route. Its 384-segment tail radius is
   `2.1323743014389777e-9`; the order-20 zonotope accepts 71 steps and rejects
   16 guarded trials, giving main radius `2.9346360173223173e-7` and full
   splice radius `4.171525822549427e-7` with independent-center containment.
   The A174 ledger was 39/71 support and L1 weight 72/123, with
   coefficient-minus-two d069/selected_078 frozen next. A175 now closes d069
   on the ranked `(0.35,-0.02,0.70)` route. Its 384-segment tail radius is
   `9.208371682944972e-7`; the order-20 zonotope accepts 138 steps and rejects
   37 guarded trials, giving main radius `3.0482279579327836e-7` and full
   splice radius `1.3519217159085886e-6` with independent-center containment.
   The A175 ledger was 40/71 support and L1 weight 74/123, with
   coefficient-plus-one d050/selected_047 frozen next. A176 now closes d050
   on the ranked `(0.20,-0.01,0.86)` route. Its same-contour 768-segment tail
   radius is `3.890338897381829e-10`; the order-20 zonotope accepts 92 steps
   and rejects 30 guarded trials, giving main radius `1.258544559744545e-7`
   and full splice radius `1.78374099046863e-7` with independent-center
   containment. The certified ledger is now 41/71 support and L1 weight
   75/123; 30 supports remain and the weighted budget is
   `0.0025093956717539695`. Twenty-nine are untouched native z-chart rows,
   headed by coefficient-minus-three d066/selected_040, while
   d047/selected_058 remains the separate partially
   certified y-chart row. This was the A176 checkpoint, not the final state.
   A177-A205 close all 29 native-z rows, and A206 promotes d047 after a
   768-segment tail refinement plus certified main-input containment. The final
   ledger is 71/71 support and L1 weight 123/123, with remaining triangle
   budget `0.0023441998400158598`. A207 applies the frozen A130/A131 canonical
   orientation signs and obtains weighted-thimble radius
   `0.0004842494354306837`, center displacement
   `2.677700007837837e-06`, and full period cost
   `0.0011918737811637164 < 0.003338125011653557`. The residual imaginary
   interval excludes zero and gives `|R_E32| >= 0.0016980843713102275`.
   Therefore this frozen carrier is rigorously rejected; no alternative
   covariant carrier is thereby proved to solve the alignment equations.

The decisive falsification test is now steps 5-6. The former rank mismatch is
closed; what can still fail is the same-source `Q`/Hessian and connection
intertwiner. If that fails, CLN remains a canonical carrier taxonomy on q79 but
not the physical closure dynamics. If it succeeds, the world-in-world idea and
the string-compatible `4+6` branch become two levels of one construction.

## 10. Bottom Line

Continue; do not start over. Freeze the ontology as:

```text
upstream: 3D proto-local base plus a 3x3 world-in-world comparison field,
local quotient: 3 orientation plus 6 strain components,
CLN: q79 trace-line, trace-zero-plane, and reused rank-three carrier (1+2+3),
downstream physical candidate: Y4 x X6_q79,
shared circle: common phase/holonomy data, with noncompact time as its ordered lift.
```

Everything stronger than this remains a theorem target, not a premise.

## External Mathematical Anchors

- [Iwasawa decomposition for `GL(n,R)`](https://web.math.ku.dk/~schlicht/Liegroups/IwasawaDecomp.pdf)
- [The `3 x 3` upper-unitriangular realization of the Heisenberg group](https://arxiv.org/abs/1712.07152)
- [Fu and Yau's non-Kahler flux construction](https://arxiv.org/abs/hep-th/0604063)
- [Hull-Strominger solutions on torus bundles over K3-type bases](https://arxiv.org/abs/1901.10322)
- [Finite locally free morphisms](https://stacks.math.columbia.edu/tag/02K9)
- [Trace of a finite locally free algebra](https://stacks.math.columbia.edu/tag/0BVH)
- [Direct summands of finite locally free sheaves](https://stacks.math.columbia.edu/tag/01C5)
