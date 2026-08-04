# Matrix Construction Routes for SM Closure

## Purpose

The current proof package has reduced the missing flavor problem to a very
specific object:

```text
selected primitive contractions -> finite C1 response matrices
```

and then, after kinetic normalization and matching:

```text
selected raw matrices -> canonical Yukawa matrices -> masses, CKM, PMNS.
```

This note explores how to create those matrices without using benchmark
entries, observed masses, observed mixings, or post-hoc fitted textures.  It
uses the MTT corpus as the primary constraint and borrows external methods only
as construction technology.

## Corpus Constraints

The corpus already fixes several matrix ingredients:

```text
rank-one tree seed:           E33, lambda_123 = 1
low-energy Higgs projection:  H_u -> H, H_d -> H^dagger
finite channel sets:          Gamma_u, Gamma_d, Gamma_e, Gamma_nuD
channel weights:              W = A exp(-S) chi
q79 character restriction:    C6 only carries q79 or conjugate
C1 driver:                    Tr_grav R_+^2 = v1_tilde alpha_1
finite C1 assembly:           six primitive 3x3 blocks per sector
```

The missing data are equally sharp:

```text
selected family zero-mode bases,
sector Dirac or Dolbeault operators D_a,
selected first variations dotD_a,
reduced Green operators G_a,
direct Theta variation,
explicit C1 vertex if present,
family kinetic metrics,
RG and threshold matching.
```

Therefore the matrix-construction problem is not "choose a texture."  It is:

```text
derive the selected zero modes and their C1/Theta responses,
contract them through the selected overlap functional,
then normalize and run them.
```

## External Inspiration

The external heterotic literature suggests useful construction patterns:

```text
cohomology/cup-product/Yoneda maps for exact holomorphic Yukawas,
selection rules from topology and discrete structure,
physical normalization from harmonic representatives and kinetic metrics,
modular or enhanced-symmetry texture constraints when derived from geometry.
```

These methods are admissible only as machinery.  They do not select the MTT
branch by themselves.

## Route A: Algebraic Cohomology Product

ID:

```text
route_A_algebraic_cohomology_cup_product
```

Construct the raw holomorphic Yukawa matrices by representing matter families
as cohomology classes and evaluating the trilinear product:

```text
H^1(V_L) x H^1(V_R) x H^1(V_H)
  -> H^3(End structure)
  -> C.
```

Concrete tools:

```text
Cech representatives,
cup products,
Yoneda products in Ext,
residue formulas when the geometry permits,
selection rules from the quotient and bundle data.
```

Why it fits MTT:

```text
the corpus already speaks in zero modes, overlap kernels, E6 trilinears,
Mukai/Fu-Yau sectors, and selected finite characters.
```

What it could close:

```text
which entries are exactly zero,
which holomorphic entries are equal or related,
the raw holomorphic rank beyond the E33 seed,
sector-specific selection rules.
```

What remains open:

```text
the actual selected bundle/cohomology representatives,
physical kinetic normalization,
non-Kahler torsional corrections if the Iwasawa/Fu-Yau branch is used,
C1 alpha-prime response values.
```

This is the best exact-symbolic route for the holomorphic part, but not by
itself a physical mass prediction.

## Route B: Physical Harmonic Representative Route

ID:

```text
route_B_physical_normalization_numeric_harmonic
```

Construct the physical matrices directly from normalized harmonic
representatives:

```text
Y_raw,ij = integral_X Omega wedge Tr(Psi_L,i wedge Psi_R,j wedge H)
K_ab     = integral_X <Psi_a, Psi_b> vol_X
Y_phys   = K_L^{-1/2} Y_raw K_R^{-1/2} K_H^{-1/2}.
```

Concrete tools:

```text
finite spectral/Galerkin approximation,
machine-learned or variational metric approximation,
harmonic projection for each zero-mode class,
L2 kinetic metric computation,
error bounds from spectral gaps.
```

Why it fits MTT:

```text
the Theta scaffold already records overlap ratios and a gap floor,
the C1 theorem already uses reduced Green operators,
the final SM theorem needs canonical rather than merely holomorphic matrices.
```

What it could close:

```text
raw and canonical Yukawa magnitudes,
family kinetic metrics,
whether the selected rank-one lift survives physical normalization,
numerical mass ratios before RG matching.
```

What remains open:

```text
explicit selected geometry and bundle data,
convergence and basis-independence checks,
RG and threshold matching to measured low-energy quantities.
```

This is the route that can eventually produce physical numbers, but it is the
heaviest computational route.

## Route C: Modular and Selection-Rule Texture Route

ID:

```text
route_C_modular_selection_texture
```

Derive texture constraints from selected automorphisms, quotient characters,
topological fusion rules, modular behavior, or enhanced symmetry loci:

```text
selected quotient/action -> allowed couplings -> texture support
selected moduli region   -> modular weights/forms -> hierarchy pattern
small selected departure -> controlled rank lift and CKM orientation.
```

Why it fits MTT:

```text
q79 is already a selected character,
the Z64 and Z7 branches are finite quotient data,
the corpus repeatedly emphasizes lens/circle/nil selection rather than
arbitrary dimensions.
```

What it could close:

```text
texture zeros,
entry relations,
allowed phase locations,
family symmetry explanation for why rank-one is the leading seed.
```

What remains open:

```text
the selected symmetry must be derived before comparison with data,
modular weights cannot be fitted after the fact,
texture constraints do not determine all magnitudes without overlaps and
kinetic metrics.
```

This route is powerful as a constraint and sanity check.  It is not enough as a
standalone no-proxy calculation unless it is tied to Route A or B.

## Route D: Iwasawa Invariant Galerkin Route

ID:

```text
route_D_iwasawa_invariant_form_galerkin
```

Exploit the left-invariant Iwasawa/Nil algebra already present in the corpus.
Represent all first-pass zero modes and C1 insertions in a finite invariant
form basis and compute the contractions symbolically:

```text
d alpha_1 = selected Nil structure term,
d alpha_2, d alpha_3 as fixed by the Iwasawa branch,
Omega = selected invariant (3,0)-form,
Tr_grav R_+^2 = v1_tilde alpha_1,
Y_ijk = integral_X Omega wedge Tr(Psi_i wedge Psi_j wedge H_k).
```

Why it fits MTT:

```text
the rank-one seed is already Iwasawa-normalized,
C1 support has already reduced to alpha_1,
the finite response theorem only needs primitive contractions.
```

What it could close quickly:

```text
an exact symbolic first candidate for each primitive 3x3 C1 block,
proof that the invariant subcomplex is insufficient if it remains rank-one,
a rigorous seed for the larger spectral computation.
```

What remains open:

```text
left-invariant forms may miss non-invariant family modes,
the invariant truncation must be justified or explicitly marked as a Galerkin
level rather than the final geometry,
sector-specific bundle action still has to be supplied.
```

This is the most natural first computation because it can produce exact finite
matrices or a clean obstruction with minimal extra machinery.

## Route E: Spectral Green-Operator C1 Response Route

ID:

```text
route_E_spectral_green_operator_response
```

Compute the primitive blocks required by the current calculator directly from
the response formula:

```text
dotPsi_a,i = - G_a Q_a dotD_a Psi_a,i.
```

For each sector:

```text
B_s,Theta,
B_s,L,
B_s,R,
B_s,H,
B_s,vertex,
B_s,basis
```

are evaluated as finite contractions and placed into:

```text
certificates/selected_c1_primitive_contractions.template.json
```

Then:

```text
scripts/compute_c1_response_matrices.py
```

computes:

```text
M_u,C1, M_d,C1, M_e,C1, M_nuD,C1,
C33(M_s),
Delta_v = (M_d13-M_u13, M_d23-M_u23).
```

Why it fits MTT:

```text
this is exactly the open interface produced by the C1 finite reduction theorem.
```

What it could close:

```text
the first actual finite C1 response matrices,
rank-lift pass/fail,
leading up/down noncommutation pass/fail.
```

What remains open:

```text
selected D_a and dotD_a,
zero-mode bases,
Green-operator truncation and error bounds,
whether C1 alone is enough for all SM masses and mixings.
```

This is the direct route to the current missing matrices.

## Route F: Dual-Triangulation Route

ID:

```text
route_F_dual_triangulation_consistency
```

Require at least two independent constructions to agree before upgrading any
matrix claim:

```text
Route D invariant/Galerkin seed agrees with Route E spectral response, or
Route A cohomology product agrees with Route B harmonic normalization after
canonical metric conversion, or
Route C selection rules agree with the support of Route A/E matrices.
```

Why it fits MTT:

```text
the theory is already cross-encoded: topology, string/flux, Theta, spectral,
and SM flavor read the same selected data differently.
```

What it could close:

```text
credibility against hidden fitting,
basis-independence checks,
separation between exact support constraints and numerical physical values.
```

What remains open:

```text
at least one primary matrix-construction route must first produce values.
```

This is not a separate source of matrices.  It is the rule that prevents a
single fragile calculation from being mistaken for closure.

## Recommended Way Forward

The correct next artifact is:

```text
Selected Zero-Mode Basis and dotD Certificate
```

It should contain, for each sector:

```text
family zero-mode basis Psi_L,i and Psi_R,j,
Higgs zero mode H_s,
operators D_L, D_R, D_H,
first variations dotD_L, dotD_R, dotD_H along C1 alpha_1,
horizontal gauge convention,
inner-product convention,
allowed finite truncation or exact invariant basis.
```

Then proceed in this order:

```text
1. Run Route D in the invariant Iwasawa/Nil basis.
2. If Route D is nontrivial, fill a first exact primitive-block certificate.
3. If Route D stays rank-one, record it as an obstruction and add the minimal
   non-invariant family modes demanded by the sector cohomology.
4. Run Route E using the same basis data and Green-operator formula.
5. Use Route A and Route C as independent support/zero-pattern checks.
6. Use Route B only when raw matrices exist and physical normalization is the
   remaining issue.
```

The reason for this ordering is simple: Route D is fastest and closest to the
current corpus, while Route E is the exact interface needed by the proof
package.  Route A and Route C protect against accidental textures.  Route B is
where physical numbers finally become credible.

## What This Achieves

This note does not compute the missing matrices.

It does close the strategy question: the matrices should be created as
selected zero-mode response contractions, first in the Iwasawa invariant
Galerkin algebra and then through the spectral Green-operator C1 response
interface.  Algebraic cohomology and modular/selection-rule routes should be
used as independent checks, not as post-hoc texture fitting.

The next genuinely progress-making move is therefore not another benchmark
texture.  It is to write the selected zero-mode basis and dotD certificate and
make the primitive contractions executable.
