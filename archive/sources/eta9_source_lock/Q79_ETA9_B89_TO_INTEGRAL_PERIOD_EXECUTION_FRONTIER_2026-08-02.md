# q79 eta9: B89-to-integral-period execution frontier

Date: 2026-08-02  
Authority: A01  
Controlling blocker: B.ETA9.01  
Kernel model: `74017e07ff95cbbf366747cececdc3211eb7d4e24aadf94a054c4693e5cd9983`

## Purpose

This note freezes the active proof route from the selected B89 pencil to the
integral meridian and its 248 period/residue coordinates. It is an anti-loop
record: an older packet, a larger benchmark, or a successful process does not
change the frontier unless it passes the stated independent verifier and
discharges one of the gates below.

## Exact upstream facts retained

1. B68-B87 provide the selected smooth coefficient, characteristic-zero
   relative residue rank, rank-1509 basis, finite normal operator, normalized
   integral source cocycle, and saturation index one at their declared tiers.
2. B89 is a fixed projective Lefschetz pencil with an exact degree-5976
   projective critical discriminant.
3. The B103 good-fiber residue basis has the frozen block order
   `H20(248) + H11(1013) + H02(248) = 1509`.
4. The H20 and H11 recursive source blocks and their associated-graded B104
   arrows are already exact over GF(11).
5. The first targeted original-Jacobian column and 22 Cox-degree blocks are
   independently replayed, giving 166 of 225 certified columns before the
   current seven-group campaign.

## Exact no-go now closed

The frozen chart operator `K=C0^{-1}C1` is not promoted as the invariant
Gauss-Manin connection. For the selected B89 F1 H02 source:

- 12,000 quotient rows have exact scalar Berlekamp-Massey complexity 4,985;
- the scalar polynomial has exact K-adic valuation 2, leaving a degree-4,983
  finite chart-pole candidate;
- the degree-5,976 projective critical discriminant fails the selected source
  recurrence in 14,411 GF(11) entries across 64 windows, with 220 of 248
  entries already nonzero in the first window.

Therefore the equality

```text
frozen chart-resolvent denominator = projective critical discriminant
```

is false for this source. This eliminates a shortcut; it does not refute the
selected B89 pencil or the original-Jacobian Griffiths-Dwork route.

Dedicated verifiers:

```text
python verify_q79_eta9_B89_F1_H02_quotient_resolvent.py
python verify_q79_eta9_B89_F1_H02_projective_denominator_nogo.py
```

## Frozen completion gates

### Gate 1: complete original-Jacobian transform

Current campaign: durable job
`35d787b2-31ce-4c1b-98dd-cceac2de3585`.

It computes and independently replays groups 25, 22, 24, 26, 27, 28, and 29.
The exit is exactly 225/225 certified support columns and zero missing groups.

Afterward, the 30 intervals are concatenated in frozen support order into one
canonical `10 x 225` polynomial transform. Verification has three layers:

1. each source block already has an independent zero-residual identity;
2. every canonical polynomial entry is compared with its source block;
3. a fresh Singular process recomputes all 225 identities
   `selectedG = J_original * T`.

The already completed H02 original-Jacobian factorization does not make this
gate redundant. That factorization targets the post-divergence pole-five Cox
degree `(9,1,2)`. The representation needed before divergence is the pole-six
degree `(9,1,3)`. A direct full Macaulay construction there would have 208,570
ambient rows and 602,597 original-Jacobian multiplier columns, so the selected
225-generator transform is the smaller exact route.

### Gate 2: complete selected good-fiber coefficient operator

Durable job `2f1132d7-aeea-4447-96ca-714f1a983bfe` runs after Gate 1. It must:

1. execute all 248 H02 pole-six return rows;
2. recursively return through H11 and H20;
3. concatenate the existing H20 and H11 blocks with the new H02 block;
4. emit and independently verify the exact `1509 x 1509` GF(11) coefficient
   operator.

This gate closes a selected good-fiber coefficient operator only. It does not
by itself establish a characteristic-zero flat family, integral monodromy, or
period values.

### Gate 3: complete the certified D6 global chain

The current independently rebuilt campaign state is 24/644 work units closed,
with a strict lower bound of 282 roots in 206 occupied leaves. The first static
job completed fifteen of its twenty assigned units before exposing one phase-B
root-containment edge case. The v11 worker now reserves every coarse cell
containing an imported Krawczyk root before any Taylor closure. The v12
compatibility wrapper retains original strict verification for legacy parents,
and its v5 manifest partitions the exact 620-unit remainder. Partial shard packets are
resume state and are verified afresh after every run; completed units retain
strict hash verification.

The exit is 644/644 independently verified units, including every certified
root block and every root-free complement. A root count, numerical seed, or
partially refined cover is not this exit.

The versioned execution checks are:

```text
python verify_q79_eta9_D6_occupied_cover_unit_v2.py
python verify_q79_eta9_D6_static_dispatch_manifest_v4.py
python verify_q79_eta9_D6_static_dispatch_manifest_v5.py
python verify_q79_eta9_D6_global_cover_campaign_progress.py
```

This campaign exhausts the four Lefschetz thimble disks, not the fibre filling
needed to make their homological boundary cancellation chain-level. That
filling is now closed separately: the matching pairs form the simple
quadrilateral `0-2-3-4-0`, and the difference of its two square-root graphs
has the unique primitive boundary relation `(-1,+1,-1,+1)`. Exact
classification of the already certified reference-fibre collision balls
finds `28,29,34,28,23,29` strict interior points in the six alternative field
embeddings and none on the quadrilateral boundary. Therefore the full Gate 3
exit is now:

```text
644/644 thimble-disk units
+ selected-embedding quadrilateral interior subset
+ certified square-root graph assignment from +sqrt(F(0))
```

The last line is now closed for all 171 embedding-labelled alternatives:
strict quadratic Rouche continuation from `s=0` assigns every point to exactly
one of `Q+` and `Q-`, and an independent twice-finer replay reproduces the
assignments. It introduces zero local sheet choices. Selection of one physical
field embedding remains open. The support paths are closed: 342 exact
rational paths implement the two global normal branches, including uniform
detours around the ten intervening collisions on six radial routes, with no
local detour choices. The ordered three-root data are now closed as well. A
canonical base frame is transported through a certified projective atlas to all
171 collisions; exact linear and quadratic Rouche disks identify 342
transpositions with no local label choices. The two global branches agree at
every target, and a 640-bit replay reproduces every ordered pair. No new
square-root isolation is required for the filling points. The dedicated filling
verifiers are:

```text
python verify_q79_eta9_reference_fibre_quadrilateral_filling.py
python verify_q79_eta9_quadrilateral_filling_sheet_transport.py
python verify_q79_eta9_quadrilateral_filling_collision_paths.py
python verify_q79_eta9_quadrilateral_filling_A2_transpositions.py
python verify_q79_eta9_archimedean_embedding_selection_boundary.py
```

The remaining six-to-one coefficient-field selection cannot come from the
existing rational algebraic identities. The coefficient field has exact
Archimedean signature `(2,2)`, while `(11,gamma-3)` selects only a
non-Archimedean good-reduction place. A physical selector must therefore be an
additional same-source Archimedean functional or structure; root ordering or
the good-reduction prime cannot be used as a substitute.

The ordered filling labels now settle one route before that selection is
available. In each of the six embedding alternatives, the quadrilateral
filling contains at least 23 strict interior simple `A2` collisions. Every
local root-stack meridian is a certified nonidentity transposition, with the
same label on the two global normal branches. The selected oriented physical
root has trivial `S3` stabilizer, so the exact Shapiro criterion excludes a
fundamental-type physical `A2` lift on the current unsurgered support in all
six alternatives. This removes the physical-embedding and full-644-inventory
prerequisites for deciding that specific support. It does not exclude a
homologous repaired support: the complete signed inventory is now required for
an explicit intersection-cancelling surgery or replacement representative.
The dedicated verifier is:

```text
python verify_q79_eta9_quadrilateral_filling_physical_A2_lift_nogo.py
```

The filling signs and ordered labels also emit a finite repair candidate. In
the fixed transposition-channel order `(01,02,12)`, only embedding 0 has zero
signed charge in all three channels; the six charge `L1` norms are
`0,5,2,2,5,5`. Its 28 points split into fourteen deterministic opposite-sheet,
equal-label pairs. This is an exact combinatorial prerequisite for one
filling-internal surgery route, not yet a physical embedding selector or a
framed geometric surgery. The dedicated verifier is:

```text
python verify_q79_eta9_quadrilateral_filling_signed_transposition_balance.py
```

Those fourteen pairs now have explicit base-projection collision-free paths on
both global normal branches. The 28 rational polygonal arcs contain 80 exact
segments; every segment lies strictly inside the quadrilateral, avoids its
boundary and avoids all nontarget collision boxes. Pairwise simultaneous
projected embeddedness is closed separately: deleting the 28 collision rectangles
gives a connected genus-zero PL surface with 29 boundary components, and the
nonseparating-arc induction emits 14 pairwise-disjoint prescribed arcs on each
global branch. Relative rational PL approximation preserves the certified
clearances. This does not supply a lifted support arc or framing and does not
select a unique simultaneous isotopy class. The remaining surgery clauses are
boundary sheet switches, a compatible lifted support isotopy class, `D6`-side
arcs, ambient Whitney framings, homology preservation and the post-surgery
restricted-holonomy check. The
dedicated verifiers are:

```text
python verify_q79_eta9_embedding0_pair_surgery_arc_atlas.py
python verify_q79_eta9_embedding0_simultaneous_support_arc_system.py
python verify_q79_eta9_embedding0_basepoint_resolution_nogo.py
```

The local fan-out shortcut for selecting that simultaneous system is now
excluded. Holding the explicit path germs fixed outside a small basepoint disk
leaves at least 16 alternating matching chords on the plus branch and 13 on
the minus branch after every exact ordering of coincident rays is tested.
Consequently the selected surgery must use a genuinely global
puncture-relative rerouting bound to the completed `D6` inventory.

One such global base-projection candidate is now explicit. A frozen rational
grid emits 14 pairwise-disjoint routes with 1,270 grid vertices and 1,284
segments; exact tests prove interior containment, boundary separation,
nontarget-box avoidance, embeddedness and pairwise disjointness. This is a
computational projected-isotopy witness, not yet a same-source physical
selector or a continuous lifted support system. The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_explicit_simultaneous_support_arcs.py
```

The lift obstruction is exact. All 14 balanced pairs join `Q+` to `Q-`, while
the two graphs are disjoint over the open quadrilateral. Every lifted path must
therefore meet the boundary sheet-joining locus. At most four pairwise-disjoint
arcs can use the four branch vertices, so at least ten require nonvertex
matching-thimble bridges. Their collision-free selection is an explicit
dependency on the signed 644-unit inventory, after which ordered root-stack
words can be replayed. The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_sheet_switch_necessity.py
```

The support-side existence consequence is now closed quantitatively. The
exhaustive degree-108 reference-fibre inventory has no `D6` zero on the
boundary matching cycles. Closedness of the global divisor and compactness of
`T28` give a `D6`-free boundary collar, and an adaptive dyadic nested-Taylor
partition certifies the first `1/64` of `T28.L0000` on both sheets. Joined to
the punctured `Q+` and `Q-` graphs, this is a connected oriented lifted
subsurface; nonseparating-arc induction emits 14 pairwise-disjoint genuine
support arcs. The canonical label `(transposition pair, local pair index)` is
an exact bijection between the balanced filling pairs, these arcs, and the 14
distinct collar transitions `(alpha_j,v_j)=(j/960,j/15)`. Thus the lifted
support system is quantitative and label preserving. Pairwise-disjoint planar
projections and graph-side PL connector coordinates are optional stronger
coordinate witnesses, not prerequisites for this result. Selected isotopy and
root-stack replay, ambient meridian identifications, `D6`-side arcs, Whitney
framings, and the integral rank-1509 lift remain open. The dedicated verifiers
are:

```text
python verify_q79_eta9_embedding0_lifted_support_arc_existence.py
python verify_q79_eta9_embedding0_T28_quantitative_D6_free_collar.py
python verify_q79_eta9_embedding0_quantitative_labelled_lifted_arc_existence.py
```

The abstract `D6` side of the fourteen pairs is now closed as well.  The
degree-108 norm on the selected reference line has an irreducible good
reduction over `GF(617^6)` and a squarefree factor pattern `(3,10,95)` over
`GF(17^6)`.  The latter cycle type is incompatible with every proper block
size dividing 108, so the line Galois action is primitive.  A geometric
factorization of the global norm curve would induce exactly such a block
system on the full-degree squarefree line section; therefore the norm curve
and its graph divisor `P_D+wQ_D=0` on the selected K3 are geometrically
irreducible.  The connected smooth locus admits fourteen pairwise-disjoint
unlabelled arcs joining the balanced endpoints, and the complex normal line
is trivial over every interval.  What remains is the ordered-transposition
lift of those arcs, their selected isotopy relative to the completed thimble
inventory, compatible ambient tube/Whitney framings and the post-surgery
restricted-holonomy calculation.  The dedicated verifier is:

```text
python verify_q79_eta9_D6_geometric_irreducibility_and_side_arcs.py
```

The ordered-root lift of those arcs is also closed at existence tier.  The
exact normalization `t^3-r^3=1`, `[A0:A1:A2]=[1:r^2:t^2]` gives the cubic
factorization

```text
(R-r)^2 ((2r^3+1)R+r^4+2r).
```

Consequently the ordered discriminant boundary has three components
`Delta_01`, `Delta_02`, `Delta_12`, each a copy of the smooth `D6`
normalization.  Pullback to the selected K3 divisor preserves those fixed-label
copies.  The fourteen balanced pairs split `4+4+6`, and the disjoint side arcs
lift with constant transposition label.  The remaining surgery clauses are
therefore selected coordinate isotopy relative to the exhaustive thimble
punctures, compatibility of the support- and `D6`-side normal framings,
ambient tube/Whitney execution and post-surgery restricted holonomy.  The
dedicated verifier is:

```text
python verify_q79_eta9_D6_ordered_label_side_arc_lift.py
```

At the ordinary topological level, the filling surgery itself is now closed at
existence tier.  Equal positive and negative counts in each fixed-label
boundary component are necessary and sufficient for elementary
label-preserving tube cancellation.  For an opposite-sign pair joined by
`beta`, remove its two support disks and attach `beta x S1` in the boundary of
`beta x D2`; the modification preserves integral homology and removes both
intersections.  Embedding 0 has total filling charge `(0,0,0)` and the
`4+4+6` matching, hence fourteen disjoint tubes remove all 28 filling
intersections.  This does not touch the unfinished thimble intersections or
decide the handle-longitude `S3` holonomy.  Once the 644-unit campaign is
complete, its signed labels reduce the full-support surgery question to three
integer charge tests per embedding, followed by selected normal-phase and
holonomy replay.  The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_labelwise_tube_surgery_criterion.py
```

There is no further topological existence obstruction from the tube normal
framings.  The oriented normal two-plane bundle restricted to each `D6`-side
interval is trivial, and path-connectedness of `SO(2)` extends every compatible
pair of endpoint frames.  This applies simultaneously to all fourteen disjoint
tubes.  The relative extension classes form `pi1(SO(2))=Z`; they are not fit
parameters and are not selected by this existence proof.  After the complete
inventory closes the charge test, the selected connection must emit these
integer windings and the corresponding handle-longitude `S3` words.  The
local meridian has fixed-label transposition image, so the `S3` calculation
depends on each winding only modulo two.  This reduces the later transport
output to fourteen selected parities without treating them as fit knobs.  The
dedicated verifier is:

```text
python verify_q79_eta9_embedding0_tube_framing_obstruction.py
```

Fixed-label transport has an exact `S3` reduction.  For each transposition
`tau`, direct enumeration gives `C_S3(tau)={1,tau}`.  A fixed-label handle
longitude is `tau^(s+d+f)` and is trivial exactly when `s+d+f=0 mod 2`.
Fourteen equation templates are emitted.  The T28 bridge theorem below now
certifies the required ordered-root condition for all fourteen bridges
individually; only simultaneous disjoint realization of the correction loops
remains open.  No transport value is a fit parameter.  The dedicated verifier
for the reduction is:

```text
python verify_q79_eta9_embedding0_handle_holonomy_centralizer_reduction.py
```

The available reference-fibre correction-loop image is now exact.  Closing the
four certified cycle permutations in each of the 24 embedding/deck/normal-side
branches gives image orders `2:4`, `3:2`, `6:18`.  All four embedding-0
branches have image `{1,(12)}`, not full `S3`; the two embedding-5 minus-deck
branches have `A3`, and all remaining branches have `S3`.  For embedding 0,
the packet emits the exact left- and right-coset criterion deciding whether a
future certified `T28` bridge word can be corrected into the centralizer of
its assigned transposition.  Therefore arbitrary correction freedom must not
be assumed.  The dedicated verifier is:

```text
python verify_q79_eta9_A2_reference_fibre_monodromy_image.py
```

The selected global T28 collar supplies the missing correction generator.  At
the ninth exact anchor, the two rigorously continued sheet-switch paths through
matching branch roots 0 and 2 have words `(02)` and `(012)`.  Their relative
closed loop has word `(01)`.  Combined with the exact reference-fibre `(12)`
loop, this generates full `S3` without changing the smaller reference-fibre
classification.  The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_T28_A2_collar_loop_image.py
```

All fourteen five-piece T28 bridges have then been executed with validated
Taylor models and strict projective Rouche continuation.  The campaign uses
1,424 certified segments, reaches maximum depth 11, and emits every open `S3`
word together with an explicit global-generator correction into the
centralizer of its assigned label.  Thus individual ordered-root support
transport is `14/14` closed.  The remaining support-side problem is the
simultaneous pairwise-disjoint realization of the finite correction loops, not
another bridge-word calculation.  The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_T28_A2_bridge_transport.py
```

The individual corrected classes also promote to one simultaneous filling
surgery.  Truncate them in disjoint endpoint collars.  Relative general
position in the real four-dimensional K3 complement gives expected dimensions
`-2`, `-2` and `-1` for self-, mutual- and old-support intersections, so the
fourteen classes have pairwise-disjoint embedded core representatives that
preserve their A2 words.  The trivial oriented interval normal bundles thicken
these cores to fourteen disjoint bands.  Hence the 28 filling intersections
are removed with homology preserved and root-stack compatibility retained.
For every construction support bit and either D6 bit, one framing parity solves
the handle equation; restricted filling holonomy has `2^14` topological
solutions and no existence obstruction.  These are not selected connection
values.  The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_simultaneous_corrected_filling_surgery.py
```

The remaining binary filling choices do not obstruct or parameterize the
integral period class. The regular flat `A2` root-stack carrier extends over a
handle's three-dimensional surgery trace exactly when its longitude is
trivial. Every one of the two admitted `D6`/framing rows per handle satisfies
that condition. Hence all `2^14` simultaneous filling repairs differ by an
integral `A2` local-coefficient boundary and pair identically with every closed
dual cocycle. Connection-selected geometric windings are still uncomputed,
but they are not required before forming the filling's twisted homology class
or closed period pairing. The dedicated verifier is:

```text
python verify_q79_eta9_embedding0_twisted_surgery_trace_invariance.py
```

The ordinary divisor-avoidance existence question is now closed separately
for the exact `gamma` candidate in the emitted effective K3 marking.  Since
`[D6]=54H` and `H.gamma=0`, its algebraic intersection with `D6` is zero.
A generic integral representative avoids the finite singular set; geometric
irreducibility makes the smooth divisor locus connected, and disjoint
opposite-sign tube surgeries remove every remaining crossing while preserving
ordinary integral homology.  Consequently the 644-unit inventory is no longer
a prerequisite for proving that *some* ordinary representative of this class
lies in the divisor complement.  It remains a prerequisite for executing and
certifying the frozen four-thimble coordinate representative, its signed
intersection inventory and ordered `A2` transport.  The result also does not
promote the effective-marking candidate to the physically selected splitting
class.  The dedicated verifier is:

```text
python verify_q79_eta9_gamma_ordinary_D6_removal.py
```

### Gate 4: select and lift the meridian subsystem

Use the completed D6/root-stack data and the selected B89 pencil to emit a
finite meridian word or smaller detecting subsystem. Then express it as an
integral vector in the saturated rank-1509 B82/B103 marking. Required checks
include orientation, intersection pairing, transport consistency, and exact
source hashes.

The local root-stack side ambiguity has now been reduced exactly. The
certified physical D6 orientation sign, multiplied by the signed thimble
coefficient and one global `+i0/-i0` normal-framing branch, determines every
upper/lower bypass. This leaves two global conjugate branches and zero
independent local side knobs. Conversely, the four `H1` boundary rows cannot
be substituted for chain-level path words: certified `S3` generator images
are noncommuting, and equal homology words can have different endpoint
permutations. The square-root graph coefficients on the fibre filling are also
closed independently for every embedding alternative. The remaining Gate 4
geometry is therefore precisely a selected support cell carrying the now-closed
ordered-root labels, followed by its integral meridian lift. It is not a repeat
of the closed homology, double-cover, path or ordered-label calculations.
The dedicated verifier is:

```text
python verify_q79_eta9_A2_oriented_normal_side_and_homology_nogo.py
```

### Gate 5: execute the period/residue image

Apply the selected lifted subsystem to the 248 holomorphic period/residue
coordinates, with certified continuation and normalization. The final B.ETA9.01
exit requires:

```text
finite meridian word or detecting subsystem
+ integral rank-1509 representative
+ certified 248-coordinate period/residue image
```

Only then may the normalized beta_C residual be decided and B.ETA9.01 be
considered for promotion.

## Non-negotiable scope distinctions

- A GF(11) matrix is not automatically a characteristic-zero connection.
- A one-fiber coefficient operator is not automatically a flat family.
- Chart poles may be apparent and are not automatically geometric critical
  values.
- A D6 numerical root candidate is not an integral Picard-Lefschetz class.
- Process success is not theorem promotion; packet hashes and independent
  verifiers control every gate.
- Closed upstream q79, SM, fixed-point, and paper tiers are not reopened by
  this execution program.

## Current next action

Complete Gate 1 without changing routes. The canonical assembly is already
wired into the queued Gate 2 pipeline, so no additional transform design step
remains after the seven groups finish.
