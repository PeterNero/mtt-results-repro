# Plan to the Unified Source Theorem

**Plan ID:** `UST.PLAN.v1`

**Primary blocker:** `B.ACTION.01`

**Rule:** A milestone closes only when it changes a named frontier truth value
or discharges an exit-certificate clause. New notation, a new packet, or a
passing self-replay does not by itself count as progress.

## Dependency Graph

```text
ETA9 meridian/period representative              B.ETA9.01
  -> physical Deligne/Brauer value               B.ETA9.02
  -> physical visible-hidden endpoint            B.HS.01
  -> geometry/operator naturality                B.GEO.01
  -> rank-102 continuum execution                B.OP.01
  -> upper action and automorphism transfer      B.ACTION.01
  -> no-knob values and precision tests          B.SM.01 / B.SM.02
  -> selected worldsheet/nonperturbative tests   B.QG.01 / B.QFT.02
```

`B.ACTION.01` formally depends on `B.HS.01` and `B.OP.01`. The longer chain is
shown because those blockers have their own strict prerequisites.

## Milestone 0: Freeze the Question

**State:** complete in this repository.

- Lock the Kernel model, upstream commits, authorities and blockers.
- Define "one source" as one selected derived solution germ, not one scalar.
- Record repair/action, finite/continuum and profile/prediction boundaries.
- Freeze already proved finite and cohesive benchmark results against looping.

**Exit:** `HYPOTHESIS.md`, branch ownership and the machine-readable frontier
agree and pass `verify.py`.

## Milestone 1: Candidate-Class Adjudication

**State:** complete at finite two-presentation classification tier.

1. Formalize the q79 Hull-Strominger configuration stack \(\mathcal C_Y\).
2. Type every component of the augmented defect target \(\mathcal D_Y\).
3. Compare the full heterotic defect against the finite Reynolds action,
   cohesive Maurer-Cartan benchmark, Hodge-square and spectral-action routes.
4. Prove which candidates are equivalent local presentations and which omit a
   physical equation.
5. Derive the minimal hypotheses under which a solution point has an augmented
   elliptic \(L_\infty\) formal neighborhood and may admit a cyclic enhancement.

**Exit achieved:** two explicit source presentations remain, ordinary bundle
and derived-cohesive, with one reverse physical-representability test. Partial
constraints, shadows, subcomplexes and tangent outputs are typed and excluded
as complete sources.

## Milestone 1E: Presentation Equivalence or Obstruction

**State:** one-way embedding closed; reverse physical representability active.

The canonical functor

\[
\mathcal I:\mathfrak S_{\mathrm{bun}}\longrightarrow
\mathfrak S_{\mathrm{coh}}
\]

is now proved to preserve the augmented differential, nonlinear residual,
gauge data and higher products, and to preserve pairing and Hodge data when the
same Hermitian structure is used. The active task is the reverse cutset for a
selected physical cohesive object after its declared transform to `X_q79`:
amplitude zero, local freeness, physical Chern/twist rows, augmentation,
metric, dynamics and finite readout.

**Exit:** prove that the selected cohesive source lies on the physical bundle
locus, or certify that it is a genuinely derived physical source with all
same-source metric, action and readout rows. The current `S_HS` benchmark is
excluded only from direct physical promotion by its Chern rows.

## Milestone 2: Nonlinear Defect-to-Hodge Theorem

**State:** universal theorem and symbolic physical residual complete; endpoint
coefficients and projector open.

1. Construct the gauge-fixed augmented Hull-Strominger defect \(\Phi_Y\).
2. Prove equivariance and the nonlinear Bianchi identities.
3. Compute its linearization on an arbitrary admissible smooth solution.
4. Prove the exact Maurer-Cartan-plus-gauge formula, then classify the extra
   physical rows. With \(K=DR_{\mathrm{phys}}\), the general target is

   \[
   \operatorname{Hess}\frac12\|\Phi_Y\|^2
   =\Delta_{\mathcal Y,1}+K^\dagger K.
   \]

5. Prove when a moment-map, redundancy or target-metric identity absorbs
   \(K^\dagger K\), or retain it as a positive physical correction. Preserve
   the forced rank-102 compression correction \(\tfrac14A_0A_0^\dagger\).
6. Prove what additional theorem is required for a cyclic/BV or Lorentzian
   physical action shadow.

**Exit achieved universally:**

\[
H_{\mathrm{phys}}
=\Delta_{\mathcal Y,1}+K^\dagger K,
\qquad
\ker H_{\mathrm{phys}}
=\ker\Delta_{\mathcal Y,1}\cap\ker K.
\]

The exact rescaling test is
\(K^\dagger K=(\kappa-1)\Delta_{\mathcal Y,1}\). `UST.G2P` now fixes the six
extra physical rows and their Frechet derivative formulas. A minimal
orthogonal `L2` repair metric is bound with zero fitted parameters. The
physical endpoint, numerical `K`, source-forced/action metric and corrected
harmonic projector remain open.

The real anomaly row makes the complete rank-102 allowable mask dense across
its five lanes: 25 ordered blocks and 10,404 positions. The older 19-block,
7,716-position mask remains only the base/non-anomaly support. It must not be
used as the full physical Hessian mask.

## Milestone 3: Ingest the Selected Physical Source

**State:** ingestion/anti-splicing contract closed; physical source blocked by
`B.ETA9.01`, `B.ETA9.02` and `B.HS.01`.

`UST.G3A` proves that the seven representability rows compile from four
geometric source objects, at most one separately declared positive
normalization ray, and one same-source finite readout. It also proves that
rows from the reference bundle pair, `S_HS/kappa_hol` and the hidden `P(3,9)`
topological endpoint cannot be spliced without certified transports. The
strict current promotable-candidate count is zero.

`UST.G3B` proves that, after all relative target weights are selected, the one
remaining common positive scale leaves the kernel, spectral projectors,
eigenspaces, dimensionless ratios, normalized finite operator and Newton
direction unchanged. It rescales absolute eigenvalues, Green operators and
clock units. This permits dimensionless execution before absolute scale
selection, but does not remove unselected relative sector weights.

`UST.G3C` proves that compatible target metrics are the positive cone in the
complete source-structure commutant. Relative weights are selected exactly
when that cone is one positive ray. Its connected-binding corollary counts one
independent positive factor per connected metric-binding component, and its
exact rational compiler retains cross terms. A finite certificate requires a
separate completeness theorem before it can select the continuum physical
metric.

`UST.G3D` now closes the analytic common-chamber criterion. The q79 lattice
relation (H\cdot\delta=0) gives an explicit balanced Gauduchon ray

\[
\omega_t=\sqrt t\,\pi^*\omega_H+t^{-1/2}i\zeta\wedge\bar\zeta.
\]

For each selected irreducible spectral factor, exact data

\[
A(F)\le -a_E<0,
\qquad
\mu_{\omega_1}(F)\le M_E
\]

compile the strict threshold

\[
t>1+\frac{(r_E-1)M_E}{a_E}.
\]

One rational `t` above the visible and hidden thresholds supplies their common
stable or polystable chamber, and twisted Kobayashi-Hitchin then supplies the
HYM connections. This is a universal conditional theorem, not the physical
endpoint: the selected visible twisted Prym module, the hidden length-nine
module or three-factor unitary orbit, their physical topology rows and their
certified `M_E` bounds remain open. The canonical gaps are fixed by q79. The
existing hidden degree-three transformed support cannot stand in for physical
rank-nine `W9`.

The bound minimal orthogonal repair metric is usable at structural repair
tier, but has not passed G3C as a uniquely source-forced metric and has not
been identified with a cyclic, BV or ten-dimensional action.

Required upstream artifacts:

- finite meridian word or smaller detecting subsystem;
- integral rank-1509 representative;
- certified 248-coordinate period/residue image;
- projected-normal Deligne obstruction decision;
- characteristic-zero visible eta9/Prym source;
- selected visible twisted Prym module and locally free twisted hidden
  \(W_9^\tau\), or its certified three-factor unitary orbit;
- the canonical q79 fiber gaps `2` and `2/3`, plus certified fixed-metric
  slope upper bounds for both sectors;
- one same-source rational `common_t` accepted by the G3D compiler;
- anomaly/Bianchi and source-hash certificate;
- for a source-forced or physical-action metric upgrade, a full target-metric
  constraint packet with an analytic continuum commutant proof or exact
  finite-to-continuum completeness map.

The eta9 Gate-2 output and characteristic-zero factorization are now promoted.
The worker should use the proved small detecting-subsystem route, then execute
the reduced H20/H11/H02 kernels along the labeled path with certified interval
balls. Exhaustive D6 enumeration is background evidence, not the primary
critical path.

The integration task is to prove that the existing four-row minimal seed is
the presentation of one point of the selected moduli stack, and to classify
any residual gauge or finite branch ambiguity. Any upstream candidate must
conform to `state/ust_g3_source_ingestion.schema.json` and its metric data must
conform to `state/ust_g3c_target_metric.schema.json`; conditional and partial
rows do not count as passes.

The non-looping object-level recipe is recorded in
`docs/G3D_PHYSICAL_SPECTRAL_OBJECT_CUTSET.md`. It separates the visible twisted
Prym construction from the two admissible hidden routes and gives the exact
threshold formulas and slope-bound certificate method.

**Exit:** one source id and hash replace separately selectable endpoint rows.

## Milestone 4: Physical Cohesive and Cyclic Enhancement

**State:** benchmark theorem exact; physical instantiation open.

1. Instantiate the cohesive superconnection on the physical \(V_3/W_9\)
   endpoint rather than the current nonphysical benchmark.
2. Construct its Hermitian/HYM metric, adjoint and compact-resolvent Hodge
   realization.
3. Include the form/B-field extension, connecting map, balanced, anomaly and
   coframe rows in one cyclic structure.
4. Prove the moment-map and action normalization.
5. Decide whether the physical object is unique, a finite pair of causal
   orientations, or a positive-dimensional moduli family.

**Exit:** a hash-addressed physical \(\mathfrak S_*\) with one cyclic pairing,
one differential and one declared scale ray.

## Milestone 5: Five Commuting Readout Maps

**State:** full-Hessian/projector transfer criterion exact; same-source
physical maps and remaining readouts open.

Construct and certify, from the same source hash:

1. `AUT`: automorphisms to the accepted gauge quotient and representations;
2. `COH`: cohomology/index to particles, chirality and three families;
3. `HT`: homotopy transfer to interactions, Yukawas and BV vertices;
4. `FIN`: spectral/Galerkin reduction to qutrit-27 and rank-102 finite data;
5. `GR`: coframe/torsion response to the TEGR/Einstein low-energy sector.

Every square must preserve the structures it claims: differential, connection,
pairing, product, Hessian, holonomy and normalization as applicable.

`UST.G5A` now closes the `FIN` Hessian/projector transfer criterion. Forward
`K` intertwining is insufficient for a nonreducing isometric image; the
adjoint-leakage term or an exact reducing-image certificate is mandatory. The
physical `T_fin` and the other four readout maps remain open.

**Exit:** the literal `B.ACTION.01` exit certificate is satisfied.

## Milestone 6: Numerical and Physical Stress Tests

**State:** downstream and blocked by Milestone 5.

- execute the 25 allowable ordered rank-102 blocks, permitting zeros only when
  the selected endpoint calculation or an exact symmetry proves them;
- compute harmonic projection, reduced Green operator and tail bounds;
- test the radii inequalities and positivity ball;
- calculate transferred quark/lepton products and test the higher-order rank
  prediction;
- derive dimensionless SM rows without observed construction inputs;
- transport through RG, thresholds and covariance;
- compare held-out observables with an uncertainty budget.

**Exit:** either a held-out same-source prediction packet or a precise
falsification of the candidate.

## Milestone 7: UV and Interpretation Boundary

**State:** downstream.

- complete the 12-row q79 heterotic worldsheet contract;
- construct a fixed-coupling nonperturbative QFT realization or prove the
  retained theory is only formal/EFT;
- determine whether a retarded branch or basin-selection law is selected;
- keep operational quantum predictions separate from ontology.

**Exit:** the UV and actualization claims are stated at their real proof tiers.

## Immediate Work Order

Work that can begin now in this repository:

1. validate incoming spectral endpoint packets with the G3D threshold and
   anti-substitution compiler;
2. validate promoted physical-source packets against the G3A anti-splicing
   contract;
3. test any source-forced/action metric claim with the G3C cone compiler;
4. ingest endpoint coefficients into the already fixed six-row `K` formula;
5. verify physical `T_fin` against the closed G5A transfer cutset;
6. compute G3B scale-free spectra and the remaining four readout squares.

Work that must remain in the upstream branches:

1. eta9 meridian, period and Deligne execution;
2. physical visible-hidden spectral modules and exact G3D topology/slope-bound
   packet;
3. source/action metric upgrade, if claimed, and endpoint coefficient
   execution after G3D acceptance.

Work that should remain frozen until the source exists:

1. new empirical SM row searches;
2. new finite matrices with no continuum symbol map;
3. new interpretive actualization claims;
4. new UV claims based only on a low-energy Hessian.
