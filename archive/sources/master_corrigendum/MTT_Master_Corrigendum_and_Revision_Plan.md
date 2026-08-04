
---
title: "MTT Master Corrigendum and Revision Plan"
subtitle: "Authoritative corpus corrections including the Fixed-Points, Foundation, and foundational-geometry reconciliation passes"
document_type: "Codex implementation specification"
version: "1.1"
date: "2026-07-15"
intended_use: "Authoritative migration guide for revising the MTT Markdown corpus"
status: "Revision specification; not itself a replacement for the source papers"
---

# MTT Master Corrigendum and Revision Plan

## Purpose

This document consolidates the complete correction program developed during the full-corpus audit and the subsequent detailed reconstruction of:

- the MTT Foundation;
- Fixed Points I–VI;
- Projection–Admissibility;
- quantum mechanics and probability;
- QFT and AQFT;
- GR and signature;
- quantum gravity;
- topology, Standard Model, strings, proto-spinors, capacity, causal sets, and numerical execution.

It is written for direct use in Codex or another repository-editing workflow.

The document has two levels:

1. **Corpus-wide rules** that every paper must obey.
2. **Paper-specific instructions** giving the required disposition, theorem replacement, retitling, withdrawal, recalculation, or scope correction.

The central conclusion of the audit is not that the MTT fixed-point core must be abandoned. The core remains viable when stated as:

\[
\boxed{
\text{local upper-world dynamics}
+
\text{fiberwise spectral projection}
+
\text{gap-controlled complementary-mode suppression}
+
\text{basin-local coherent stability}
+
\text{controlled reduction}.
}
\]

The principal problem is that many downstream papers ask this core to prove claims it does not yet prove.

---

# Part I — Revision policy

## Priority codes

Use the following priorities in commits, issues, and pull requests.

| Code | Meaning |
|---|---|
| **P0 — Blocker** | A false theorem, contradictory construction, decisive numerical error, or claim combination that cannot remain as written |
| **P1 — Major** | A missing hypothesis, invalid proof step, incorrect map typing, or central scope overstatement |
| **P2 — Substantive** | A result remains useful but must be narrowed, reclassified, or connected to the correct upstream theorem |
| **P3 — Editorial** | Notation, naming, dependency, dimensional, or presentation cleanup that does not alter the mathematical result |

## Disposition labels

| Label | Meaning |
|---|---|
| **KEEP** | Core result survives; only minor clarification is needed |
| **REVISE** | Result survives after theorem or hypothesis repair |
| **RETITLE** | The paper can remain but its current title overstates the result |
| **RECLASSIFY** | Change “derivation/prediction/theorem” to reconstruction, realization, characterization, calibration, or interpretation |
| **RECALCULATE** | Numerical chain is invalid until recomputed |
| **WITHDRAW CLAIM** | Remove the identified claim while retaining the rest of the paper |
| **WITHDRAW PAPER PENDING REBUILD** | The central explicit construction is not valid as written |
| **INTERPRETIVE ONLY** | Keep as conceptual proposal, not theorem or quantitative model |

## Claim-status vocabulary

Every abstract, theorem summary, index entry, and conclusion must use one of the following labels.

| Status | Definition |
|---|---|
| **Axiom / assumption** | Upstream premise inserted into the realization |
| **Conditional theorem** | Proved from explicitly listed assumptions |
| **Characterization** | Any object satisfying the assumptions must have the stated form |
| **Reconstruction** | Recovers an established framework after target-compatible structure is supplied |
| **Embedding / containment** | Represents a known framework inside MTT |
| **Realization** | Exhibits one concrete model satisfying the abstract architecture |
| **Calibration** | Determines parameters from measured data |
| **Postdiction / round-trip check** | Reproduces data used directly or indirectly in fitting or model selection |
| **Held-out prediction** | Computes data not used in construction, calibration, scale choice, or model selection |
| **Interpretation** | Conceptual reading without independent theorem status |

Do not use “derived,” “forced,” “inevitable,” “exact prediction,” “closed,” or “proved” unless the paper meets the corresponding standard.

## Current-version delta requirement

Every revised paper must place a section titled `Revision note for this
edition` immediately after its abstract. The note records only the delta from
the directly superseded edition and must contain:

1. **Supersedes:** the preceding title and version or `first edition`;
2. **Reason:** the concrete mathematical, numerical, provenance, or scope
   defect requiring revision;
3. **Resolution:** what this edition changed to repair that defect;
4. **Retained result:** the theorem or construction that survives; and
5. **Remaining boundary:** the strongest related claim not established by the
   revision.

Do not invent a retrospective history for editions whose source delta is not
available. Detailed evidence belongs in the external revision audit; the
in-paper note is the concise reader-facing contract for the current edition.

---

# Part II — Authoritative dependency order

The revised corpus must use this dependency spine:

\[
\boxed{
\begin{aligned}
&\text{Mathematical conventions}\\
&\quad\rightarrow\text{Foundation}\\
&\quad\rightarrow\text{Fixed Points I–VI}\\
&\quad\rightarrow\text{Projection, descent, recovery, and admissibility}\\
&\quad\rightarrow\text{controlled reconstructions}\\
&\quad\rightarrow\text{specific realizations}\\
&\quad\rightarrow\text{numerical execution and phenomenology}.
\end{aligned}
}
\]

The Fixed Points series is authoritative for:

- the upper-world geometry used in the physical realization;
- the coherent projector;
- complementary-mode suppression;
- coherent-sector contraction;
- locality descent;
- fixed-point existence and equilibrium identification;
- the meaning of an admissibility barrier.

The structural A0–B5 papers may classify these objects. They may not redefine them in a way that conflicts with the FP spine.

---

## Foundational-geometry reconciliation authority

The 2026-07-15 reconciliation adds a second dependency constraint. The local
world-in-world carrier and the selected q79 global carrier must be distinguished
until an explicit intertwiner is proved:

\[
Q_{\mathrm{WW}}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right),
\qquad
\mathcal H_{\mathrm{CLN}}
=L_{\mathrm{shared}}\otimes
(\mathcal O\oplus\mathcal A_0\oplus\mathcal A).
\]

The first object is locally a `3 x 3` comparison matrix. The second is the
selected q79 trace-split carrier of rank `1+2+3=6`. Equality of component
counts is not an identification of bundles, metrics, connections, or source
operators.

The following status statements control all revisions:

- `1 + 3 x 3 = (1+3) + (1+2+3) = 4+6` is a component identity, not a proof of a ten-dimensional manifold or Lorentzian spacetime.
- A three-dimensional base with a rank-three fiber has six-dimensional total space; dimensions are added, not multiplied.
- The q79 degree-three cover proves the trace split `A = O + A0` and the common rank-six carrier `O + A0 + A`.
- The signed q79 sheet action has a local `Dic_3` lift. Strict global Spin closure remains conditional on all branch-complement relator signs, or equivalently the relevant obstruction class.
- The shared circle is common `U(1)` phase/holonomy data and is counted once. It is not physical time.
- The q79 Fu--Yau branch is the current selected global compactification candidate. `L(3,1) x Nil3` is auxiliary/effective. Literal `S1 x Lens x Nil`, literal manifold nesting, and equality of these topologies are retired as proof sources.

The common open theorem is the same-source world-in-world/strain-to-q79
bundle-and-connection intertwiner. No paper may silently replace this theorem
with rank matching.

---

# Part III — Corpus-wide canonical conventions

## 1. Canonical geometry

On each admissible physical slab, use:

\[
\boxed{
\pi:M_{10}\to Y_4,
\qquad
\dim M_{10}=10,
\quad
\dim Y_4=4,
\quad
\dim X_x=6,
}
\]

where

\[
X_x=\pi^{-1}(x).
\]

In a trivialization:

\[
\boxed{
M_{10}\simeq Y_4\times X_6.
}
\]

- \(Y_4\) is Lorentzian and globally hyperbolic in the physical realization.
- \(X_6\) is compact and Riemannian.
- Positive elliptic modal operators act vertically on \(X_6\).
- The internal directions do not add new causal directions.

### Triplet convention

Use:

\[
(\mathcal E_i,A_i,P_i),
\qquad i=1,2,3,
\]

for three compatible vertical structures on the same internal Hilbert bundle.

The joint projector is:

\[
P_{\mathrm{coh}}=P_1P_2P_3.
\]

Do not interpret the triplet as three additional coordinate manifolds unless a factorization is explicitly stated.

### Factorized internal realization

If:

\[
X_6\simeq F_1\times F_2\times F_3,
\]

require:

\[
\dim F_1+\dim F_2+\dim F_3=6.
\]

For an equal minimal factorization:

\[
\dim F_i=2.
\]

### Central circle

Represent a central phase circle by a principal \(U(1)\) bundle or Hermitian line bundle:

\[
L_{\mathrm{cen}}\to X_6.
\]

Do not write:

\[
X_6=S^1_{\mathrm{cen}}\times T_1^2\times T_2^2\times T_3^2,
\]

because the right-hand side is seven-dimensional.

### World-in-world comparison carrier

The lawful `3 x 3` construction is a field between two rank-three tangent
spaces,

\[
Q_{\mathrm{WW}}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right).
\]

In local orthonormal frames it has nine components. At a nonsingular
background, polar decomposition gives

\[
\operatorname{Mat}(3,\mathbb R)
=\mathfrak{so}(3)\oplus\operatorname{Sym}(3,\mathbb R),
\qquad 9=3+6,
\]

and a selected flag gives

\[
\operatorname{Sym}(3,\mathbb R)
=\mathbb RI_3\oplus\mathcal D_0\oplus\mathcal O,
\qquad 6=1+2+3.
\]

Thus

\[
1+3\times3=(1+3)+(1+2+3)=4+6=10
\]

is a component count after an ordering scalar is supplied. Do not rewrite it
as three independent three-manifolds, and do not use it to derive `M10`, `Y4`,
Lorentzian signature, or the selected q79 global geometry.

The q79 carrier has the matching rank profile

\[
\mathcal H_{\mathrm{CLN}}
=L_{\mathrm{shared}}\otimes
(\mathcal O\oplus\mathcal A_0\oplus\mathcal A),
\qquad \operatorname{rank}=1+2+3,
\]

but the local and global objects may be identified only after constructing an
intertwiner that respects transition functions, metrics, covariant
derivatives, and the selected vertical operators.

## 2. Symbol conventions

Reserve:

| Symbol | Meaning |
|---|---|
| \(Y_4\) | physical Lorentzian spacetime |
| \(X_6\), \(X_x\) | internal compact six-dimensional fiber |
| \(F_i\) | actual coordinate factor of \(X_6\) |
| \(\mathcal E_i\) | internal bundle or representation structure |
| \(A_i,\Delta_i\) | vertical positive operator |
| \(P_i,\Pi_i\) | vertical spectral projector |
| \(P\) | coherent projector or explicitly named reduction map; never both in one section |
| \(Q_{\mathrm{inc}}=I-P\) | noncoherent projector |
| \(Q_{\mathrm{WW}}\) | world-in-world comparison field in \(\operatorname{Hom}(TP,TI)\); never a projector |
| \(\mathcal A_0\) | trace-zero rank-two summand of the selected q79 degree-three carrier |
| \(L_{\mathrm{shared}}\) | common phase/holonomy line bundle; not physical time |
| \(Q_\xi=BB^\ast\) | stochastic noise covariance |
| \(\mathcal R\) | reduction channel |
| \(\mathcal J\) | lifting/preparation channel |
| \(\mathbf P=\mathcal J\mathcal R\) | genuine projection superoperator on one operator space |

Deprecate unqualified \(B_i\) where it ambiguously means bundle, factor, fiber, or filter.

## 3. Time and scale parameters

Use:

\[
t=\text{physical Lorentzian time},
\]

\[
\tau=\text{stabilization, heat, proper-time, or evolve–project parameter},
\]

\[
s=\log k=\text{renormalization-group scale}.
\]

A paper may identify two of these only after proving the relation in a concrete realization.

Use:

\[
U(t_2,t_1)
\]

for physical local hyperbolic evolution and:

\[
R_\tau=e^{-\tau A_{\mathrm{stab}}}
\]

for stabilization/filtering.

The evolve–project map is:

\[
T_\tau=P_{\mathrm{coh}}R_\tau.
\]

## 4. Strong commutation

For unbounded self-adjoint vertical operators, require commuting spectral measures, not merely a formal commutator on an unspecified domain.

Use:

\[
[A_i,A_j]_{\mathrm{strong}}=0
\]

as shorthand for a joint functional calculus.

If only approximate commutation is available, add:

- a common domain;
- a norm or form bound on the perturbation;
- a gap larger than the perturbation;
- constant spectral rank;
- a Kato/Riesz projector perturbation estimate.

## 5. Gap logic

The internal gap controls:

- noncoherent internal-mode damping;
- resolvent estimates;
- projector conditioning;
- Kaluza–Klein mass thresholds;
- Schur-complement truncation error.

It does **not** by itself control:

- coherent zero modes;
- four-dimensional external momentum;
- a universal minimum spacetime length;
- four-dimensional UV finiteness;
- fixed-point existence;
- probability;
- Lorentzian signature.

Use distinct scales:

\[
M_{\mathrm{KK}}^2\sim\lambda_\ast^{\mathrm{int}},
\]

\[
\mu_{\mathrm{coh}}=\text{coherent contraction rate},
\]

\[
\Lambda_{\mathrm{4D}}=\text{independently derived EFT cutoff},
\]

\[
\tau_{\mathrm{ext}}^{-1/2}=\text{external filter scale, if one is separately introduced}.
\]

## 6. Generator sign

For a positive stabilization operator \(A_Q\ge\lambda_Q I\), write the stable generator as:

\[
G_Q=-A_Q+B_Q.
\]

Require:

\[
\operatorname{Re}\langle G_Qq,q\rangle
\le
-\gamma_Q\|q\|^2,
\]

or:

\[
\|e^{\tau G_Q}\|
\le
M_Qe^{-\gamma_Q\tau}.
\]

Do not combine positive accretivity of \(L\) with decay of \(e^{tL}\) under the same sign convention.

For nonnormal generators, eigenvalue real parts are not enough. Use a semigroup bound or a weighted dissipativity inequality.

## 7. Fixed-point logic

Keep the following implications distinct:

\[
\text{gap}
\not\Rightarrow
\text{existence},
\]

\[
\text{invariance}
\not\Rightarrow
\text{existence},
\]

\[
\text{projected time-step fixed point}
\not\Rightarrow
\text{stationary equilibrium},
\]

\[
\text{strict contraction self-map on a complete invariant domain}
\Rightarrow
\text{existence and uniqueness}.
\]

A projected fixed point becomes a true equilibrium only through, for example:

- a strict Lyapunov/gradient-flow identity; or
- uniqueness combined with the semigroup property.

Multiple outcomes require basin-local contraction:

\[
T(D_\alpha)\subseteq D_\alpha,
\qquad
\operatorname{Lip}(T|_{D_\alpha})<1.
\]

A single global strict contraction cannot have several fixed-point outcomes.

## 8. Locality descent

The coherent projector is decomposable:

\[
P=\int_{Y_4}^{\oplus}P_x\,d\mu(x),
\]

so:

\[
[P,M_f]=0
\]

for base multiplication operators.

For coherent-preserving local observables:

\[
[A_i,P]=0.
\]

Then:

\[
[A_1,A_2]=0
\quad\Rightarrow\quad
[PA_1P,PA_2P]=0.
\]

For arbitrary observables:

\[
[PA_1P,PA_2P]
=
P[A_1,A_2]P
-
PA_1Q_{\mathrm{inc}}A_2P
+
PA_2Q_{\mathrm{inc}}A_1P.
\]

Therefore use either:

- the coherent-preserving local algebra; or
- a locality-preserving conditional expectation before compression.

Global state nonfactorization is compatible with local commutativity and no-signaling.

Do not call this Bell-local factorization.

## 9. Map typing and inverses

For \(T:X\to Y\):

### Right inverse / section

\[
S:Y\to X,
\qquad
T\circ S=\operatorname{id}_Y.
\]

A right inverse selects one representative. Noninjectivity does not prevent it.

### Left inverse / exact decoder

\[
D:Y\to X,
\qquad
D\circ T=\operatorname{id}_X.
\]

A left inverse requires injectivity and recovers the actual input.

### Autonomous reduced dynamics

For \(P_0:X\to Y_0\), \(P_t:X\to Y_t\), and microscopic flow \(\Phi_t\), a reduced map \(F_t:Y_0\to Y_t\) exists exactly when:

\[
P_0(x)=P_0(x')
\Longrightarrow
P_t(\Phi_tx)=P_t(\Phi_tx').
\]

### Effective merger

If:

\[
P_0(x)\neq P_0(x'),
\qquad
P_t(\Phi_tx)=P_t(\Phi_tx'),
\]

the previous effective state is not recoverable.

### Stable section

Physical continuation may require a regularity bound such as:

\[
\operatorname{Lip}(S_A)\le K.
\]

A robust barrier can be characterized by:

\[
K_{\mathrm{sec}}(A_\lambda)\to\infty.
\]

A fixed bounded linear projection always has the inclusion of its range as a continuous right inverse. Never claim otherwise.

## 10. Probability

Noninjectivity supplies unresolved multiplicity, not probabilities.

To obtain a stochastic kernel, specify a measure \(\mu\) and disintegrate it along fibers:

\[
K(y,A)
=
\mu\!\left(
\Phi^{-1}(P^{-1}(A))
\mid
P^{-1}(y)
\right).
\]

The correct chain is:

\[
\boxed{
\text{projection}
+
\text{preparation/invariant measure}
+
\text{mixing or basin geometry}
\Rightarrow
\text{effective probability}.
}
\]

The MTT-specific Born target is:

\[
\boxed{
\nu_\rho(B_i^{\mathsf M})
=
\operatorname{Tr}(\rho E_i^{\mathsf M}).
}
\]

Until this is proved in a concrete model, call the result Born-compatible, not a derivation.

## 11. Reduced density dynamics

If:

\[
\mathcal R:
\mathcal T_1(\mathcal H_{10})
\to
\mathcal T_1(\mathcal H_4)
\]

changes operator spaces, then \(I-\mathcal R\) is not defined.

Introduce:

\[
\mathcal J:
\mathcal T_1(\mathcal H_4)
\to
\mathcal T_1(\mathcal H_{10}),
\]

with:

\[
\mathcal R\mathcal J=\operatorname{id},
\]

and define:

\[
\mathbf P=\mathcal J\mathcal R,
\qquad
\mathbf P^2=\mathbf P,
\qquad
\mathbf Q=I-\mathbf P.
\]

Apply Nakajima–Zwanzig to \(\mathbf P\) on one operator space.

## 12. Lorentzian signature

A positive Gram tensor:

\[
K_{\mu\nu}
=
\langle D_\mu\Psi_\ast,D_\nu\Psi_\ast\rangle
\]

satisfies:

\[
v^\mu K_{\mu\nu}v^\nu\ge0.
\]

It cannot be a Lorentzian metric.

Derive or assume the physical causal metric through the principal symbol:

\[
\sigma_{\mathcal E}(x,\xi)
=
G^{\mu\nu}(x)\xi_\mu\xi_\nu M(x).
\]

A valid conditional theorem requires hyperbolicity, nondegeneracy, a Cauchy problem, and positive spatial energy.

## 13. External Gaussian damping

Internal weights of the form:

\[
e^{-\tau\mu_j^2}
\]

are compatible with a positive four-dimensional Källén–Lehmann spectrum:

\[
G_{4D}(p)
=
\sum_j
\frac{Z_je^{-\tau\mu_j^2}}
{p^2-m_j^2+i\epsilon}.
\]

Exact external-momentum decay:

\[
G_E(p^2)\lesssim e^{-\tau p^2}
\]

is incompatible with a nonzero positive Källén–Lehmann/Stieltjes representation having standard positive spectral measure.

The viable FP interpretation is internal damping. External damping is a separate Euclidean or spatial filter and cannot be claimed as a consequence of the internal gap.

## 14. Admissibility and selection

Define a normalized margin vector:

\[
\mathbf m=
(m_{\mathrm{gap}},
m_{\mathrm{proj}},
m_{\mathrm{well}},
m_{\mathrm{inv}},
m_{\mathrm{coh}},
m_{\mathrm{trunc}},
m_{\mathrm{section}}).
\]

Define:

\[
C(x)=\min_jm_j(x).
\]

The current chart is controlled for \(C>0\) and ends at \(C=0\).

A divergent diagnostic may be:

\[
\mathcal B(x)
=
\log\left(1+\frac{C_0}{C(x)}\right).
\]

This barrier diagnoses chart failure. It does not exert a force unless included in an independently justified action.

A complete boundary model needs:

- a deterministic upper continuation;
- a set-valued reset relation; or
- a transition kernel.

## 15. Numerical provenance

Every numerical paper must explicitly list:

- raw empirical inputs;
- calibration variables;
- scale-choice variables;
- geometry/model-selection inputs;
- nuisance parameters;
- held-out observables;
- uncertainty propagation;
- executable code and tests.

A result is not a prediction when the observable influenced the matching scale, latent ratios, thresholds, geometry, or nuisance choices.

---

# Part IV — Immediate P0 actions

## P0.1 Withdraw the original right-inverse obstruction

Remove every proof using noninjectivity to infer nonexistence of a right inverse.

Replace it with the descent/recovery theorem in Part V.

Affected families include:

- Projection–Admissibility;
- A0;
- Closure and Inevitability;
- black-hole/measurement bridge;
- EFT, horizon, photon, capacity, and coherent-kinematics papers;
- corpus index summaries.

## P0.2 Recalculate the entire \(5\,\mathrm{TeV}\) execution chain

The claimed one-loop \(\alpha_1=\alpha_2\) crossing near \(5\,\mathrm{TeV}\), using GUT-normalized hypercharge and standard SM beta coefficients, is numerically inconsistent with the stated equations.

Using:

\[
b_1=\frac{41}{10},
\qquad
b_2=-\frac{19}{6},
\]

and representative values:

\[
\alpha_1^{-1}(M_Z)\simeq59.0,
\qquad
\alpha_2^{-1}(M_Z)\simeq29.6,
\]

gives:

\[
\log\frac{\Lambda_{12}}{M_Z}
=
\frac{2\pi(59.0-29.6)}
{41/10+19/6}
\simeq25.4,
\]

hence:

\[
\Lambda_{12}\sim10^{13}\,\mathrm{GeV}.
\]

Until independently reproduced, withdraw:

- the \(5\,\mathrm{TeV}\) crossing;
- \(\zeta\)-ratios evaluated there;
- \(K\) calibrated there;
- threshold coefficients derived from those targets;
- the \(5\,\mathrm{TeV}\) coherence scale;
- dependent inflation, GW, and Tier 4 conclusions;
- any \(\alpha_s\) “prediction” that round-trips data used upstream.

## P0.3 Withdraw the explicit Iwasawa bundle construction pending rebuild

The form:

\[
c=\frac{i}{2}\omega_3\wedge\bar\omega_3
\]

is not closed when:

\[
d\omega_3=\omega_1\wedge\omega_2.
\]

It cannot be used as a first Chern class.

A topologically trivial smooth rank-three bundle cannot have nonzero topological \(c_3\).

The monad, Chern classes, stability, HYM, and Bianchi construction must be rebuilt from valid closed integral cohomology classes and global maps.

## P0.4 Withdraw the current external-Gaussian/unitary-QG conjunction

Do not claim simultaneously:

- a nonzero positive physical Källén–Lehmann/Stieltjes propagator; and
- exact Gaussian decay in external \(p_4^2\).

Retain internal spectral weights and positive four-dimensional spectral sums.

## P0.5 Withdraw the current all-loop finiteness theorem

The presence of one Gaussian-damped graviton line does not control every independent loop momentum or divergent matter subgraph.

Any replacement theorem must:

- renormalize undamped subgraphs;
- prove full rank of the residual damping quadratic form;
- state the graph class precisely.

## P0.6 Correct the Fixed Points source errors before using them as official authority

At minimum:

- FP II seven-dimensional example;
- FP III deterministic forcing floor and homogenization normalization;
- FP IV curvature mixing and first-order modulation;
- FP V nonlinear-Gaussian and cross-correlation theorem;
- FP VI Lyapunov sign, nonnormal bounds, locality of bilocal interactions, and coherent uniqueness.

---

# Part V — Replacement theorem blocks

## 1. Projection–Descent and Recovery Theorem

Let:

\[
P_0:A\to Y_0,
\qquad
P_t:\Phi_t(A)\to Y_t,
\]

and define:

\[
T_t=P_t\circ\Phi_t:A\to Y_t.
\]

### Representative selection

A section is:

\[
S_t:Y_t\to A,
\qquad
T_tS_t=\operatorname{id}_{Y_t}.
\]

It selects one compatible representative and does not recover the actual input.

### Exact microscopic recovery

A decoder is:

\[
D_t:Y_t\to A,
\qquad
D_tT_t=\operatorname{id}_A.
\]

It exists only if \(T_t\) is injective.

### Autonomous reduced evolution

A map:

\[
F_t:Y_0\to Y_t
\]

satisfying:

\[
F_tP_0=P_t\Phi_t
\]

exists if and only if:

\[
P_0(x)=P_0(x')
\Longrightarrow
P_t(\Phi_tx)=P_t(\Phi_tx').
\]

### Effective merger

If:

\[
P_0(x)\neq P_0(x'),
\qquad
P_t(\Phi_tx)=P_t(\Phi_tx'),
\]

then \(F_t\) is noninjective and the previous effective state cannot be decoded.

### Robust continuation

A stable section must obey a regularity bound. A barrier may be defined by blow-up of the best section condition number or by failure of bounded projector continuation.

## 2. Valid right-inverse obstruction for a reduced self-map

Let:

\[
T_A:Y_A\to Y_A
\]

act on a finite-diameter space of diameter \(D\), and suppose:

\[
d(T_Ay,T_Ay')
\le
\kappa d(y,y')+c\varepsilon,
\qquad
0<\kappa<1.
\]

Then:

\[
\operatorname{diam}T_A(Y_A)
\le
\kappa D+c\varepsilon.
\]

If:

\[
(1-\kappa)D>c\varepsilon,
\]

then \(T_A\) is not surjective and has no right inverse.

This is a theorem about a reduced self-map, not about a cross-level projection.

## 3. Fixed-Point Locality-Descent Theorem

Let:

\[
P=\int_{Y_4}^{\oplus}P_x\,d\mu(x)
\]

be the fiberwise coherent projector and let:

\[
O\mapsto\mathcal A_{10}(\pi^{-1}O)
\]

be the upper local net.

Define:

\[
\mathcal A_{10}^P(O)
=
\{A\in\mathcal A_{10}(\pi^{-1}O):[A,P]=0\}.
\]

Define:

\[
\mathcal A_4(O)
=
\{PAP|_{\operatorname{Ran}P}:A\in\mathcal A_{10}^P(O)\}.
\]

Then upper isotony and microcausality descend to \(\mathcal A_4\).

States on \(\mathcal A_4\) may remain nonfactorizing.

## 4. Basin-local FCC theorem

For each invariant basin \(D_\alpha\), assume:

\[
T(D_\alpha)\subseteq D_\alpha
\]

and:

\[
\|T(u)-T(v)\|
\le
q_\alpha\|u-v\|,
\qquad
q_\alpha<1.
\]

Then each \(D_\alpha\) contains one unique fixed point.

Do not apply one global contraction to the union of outcome basins.

## 5. Approximate-map theorem

The inequality:

\[
\|T(x)-T(y)\|
\le
\kappa\|x-y\|+\varepsilon
\]

does not make \(T\) a Banach contraction.

Use either:

- \(T=T_0+R\) with \(\operatorname{Lip}(T_0)+\operatorname{Lip}(R)<1\); or
- a separate existence theorem for \(T\), followed by perturbative distance estimates to a fixed point of \(T_0\).

## 6. Measure-dependent stochastic reduction

Let \(\mu\) be an upper preparation or invariant measure. Define:

\[
K(y,A)
=
\mu\left(
\Phi^{-1}(P^{-1}(A))
\mid
P^{-1}(y)
\right).
\]

Then \(K\) is the effective stochastic kernel.

Different conditional measures on the same fibers may produce different stochastic laws.

## 7. Born-compatible theorem decomposition

### Basin capture

\[
p_i=\nu_\rho(B_i^{\mathsf M}).
\]

### Quantum representation

Under normalized, noncontextual, orthogonally additive, continuous, composition-compatible weights:

\[
p_i=\operatorname{Tr}(\rho E_i).
\]

### Missing MTT theorem

Prove:

\[
\nu_\rho(B_i^{\mathsf M})
=
\operatorname{Tr}(\rho E_i^{\mathsf M}).
\]

## 8. Controlled GR reduction theorem

Assume:

- a local higher-dimensional action containing an Einstein–Hilbert sector;
- \(M_{10}\simeq Y_4\times X_6\);
- compact \(X_6\);
- stabilized unwanted zero modes;
- controlled coherent truncation;
- no unsuppressed sourcing of discarded equations.

Then the leading four-dimensional metric action is Einstein–Hilbert plus calculable corrections.

This is a controlled reduction theorem, not projection-only emergence of gravity.

## 9. Curved-sector leakage theorem

If:

\[
\gamma_Q
=
\lambda_Q-\Delta_{\mathrm{curv}}-L_Q>0
\]

and:

\[
b_{\mathrm{mix}}=\|Q\mathcal RP\|,
\]

then:

\[
\|Q\Psi(\tau)\|
\le
e^{-\gamma_Q\tau}\|Q\Psi(0)\|
+
b_{\mathrm{mix}}
\int_0^\tau
e^{-\gamma_Q(\tau-s)}
\|P\Psi(s)\|\,ds.
\]

Curvature that does not commute with the projector generally gives a leakage floor.

## 10. Correct linear covariance theorem

For:

\[
d\zeta_t=A\zeta_tdt+B\,dW_t,
\qquad
Q_\xi=BB^\ast,
\]

the stationary covariance satisfies:

\[
A\Sigma+\Sigma A^\ast+Q_\xi=0.
\]

If:

\[
\|e^{tA}\|\le Me^{-\gamma t},
\]

then:

\[
\|A^{-1}\|\le\frac{M}{\gamma},
\qquad
\|\Sigma\|\le\frac{M^2\|Q_\xi\|}{2\gamma}.
\]

---

# Part VI — Paper-by-paper revision instructions

# Group 0 — Corpus index and navigation

## `Modal_Triplet_Theory__Corpus_Index_and_Reference_v7 / v8`

**Disposition:** REVISE  
**Priority:** P1

### Required changes

- Make the Foundation and Fixed Points I–VI the controlling mathematical dependency spine.
- Replace all `Closed`, `Proved`, `Exhaustive`, and `Completed` statuses that depend on the incorrect inverse theorem, unproved Born rule, constructive-QG claims, or invalid numerical execution.
- Classify every paper as axiom, conditional theorem, characterization, reconstruction, embedding, realization, calibration, prediction, or interpretation.
- Change circle–lens–nil from an exhaustive proved classification to a coarse obstruction taxonomy unless a precise descent category and proof are supplied.
- Change ten-dimensional minimality from universal theorem to a canonical or minimal curvature-based realization under explicit transversality/product assumptions.
- Mark the explicit Iwasawa realization and all \(5\,\mathrm{TeV}\)-dependent execution results as withdrawn pending rebuild/recalculation.
- Change quantum-gravity index descriptions from completed unitary constructive QG to conditional Euclidean/TT/SPT model status.
- State explicitly that locality is inherited from the FP local upper net and fiberwise reduction, not from non-joint representability.

# Group 1 — Core and encoding series

## `Modal_Triplet_Theory__Admissibility__Encodings__and_the_Structure_of_Physical_Description_v11.md`

**Disposition:** MAJOR REVISION  
**Priority:** P1

### Required changes

- Adopt the canonical \(M_{10}\to Y_4\) bundle with six-dimensional fiber and triplet-as-vertical-operators convention.
- Remove all claims that ordinary noninjectivity destroys a right inverse. Use descent, decoder, merger, and stable-section language.
- Replace `circle, lens, and nil are exhaustive and force unique responses` with a taxonomy statement plus explicit open proof obligations.
- Replace `minimal realization is ten-dimensional` with a conditional realization theorem requiring three independent nonzero curvature two-forms on transverse factors and an assumed four-dimensional base.
- Change all summaries of QM, GR, SM, strings, QG, and AQFT from derivation/closure language to typed reconstruction or realization language where target-compatible structure is assumed.
- Update the boundary language: chart failure is detected by loss of gap, projector regularity, descent, coherent stability, or robust section continuation.
- Do not claim that physical description ceases to exist in every mathematical sense outside one chart; state that the current effective encoding ceases to be controlled.

## `Modal_Triplet_Theory__Admissibility__Encodings__and_the_Structure_of_Physical_Description_v8.md`

**Disposition:** MAJOR REVISION  
**Priority:** P1

### Required changes

- Adopt the canonical \(M_{10}\to Y_4\) bundle with six-dimensional fiber and triplet-as-vertical-operators convention.
- Remove all claims that ordinary noninjectivity destroys a right inverse. Use descent, decoder, merger, and stable-section language.
- Replace `circle, lens, and nil are exhaustive and force unique responses` with a taxonomy statement plus explicit open proof obligations.
- Replace `minimal realization is ten-dimensional` with a conditional realization theorem requiring three independent nonzero curvature two-forms on transverse factors and an assumed four-dimensional base.
- Change all summaries of QM, GR, SM, strings, QG, and AQFT from derivation/closure language to typed reconstruction or realization language where target-compatible structure is assumed.
- Update the boundary language: chart failure is detected by loss of gap, projector regularity, descent, coherent stability, or robust section continuation.
- Do not claim that physical description ceases to exist in every mathematical sense outside one chart; state that the current effective encoding ceases to be controlled.

## `The_Modal_Triplet_Theory_Program_A0__A_Structural_Theory_of_Reduced_Description.md`

**Disposition:** REWRITE CENTRAL THEOREM  
**Priority:** P0/P1

### Required changes

- Delete the proof that noninjectivity implies no right inverse.
- Replace the single obstruction theorem with the Projection–Descent and Recovery Theorem.
- Separate failure of reduced autonomy, effective-state merger, microscopic nonrecoverability, and stable-section blow-up.
- Use the valid reduced-self-map non-surjectivity theorem only when the diameter/FCC inequality is satisfied.
- Define admissibility barriers through explicit margins rather than assuming absence of a section and then deriving it.
- Use basin-local FCC.
- Clarify whether the underlying flow is physical hyperbolic evolution or an auxiliary stabilization semigroup.

### Preferred replacement language or theorem

Suggested abstract sentence:

> We classify when microscopic dynamics descends to an autonomous effective map, when effective histories merge, when exact microscopic recovery is impossible, and when compatible encoding sections lose robust continuation. These are distinct obstructions with distinct hypotheses.\n
## `The_Modal_Triplet_Theory_Program_A1__Coherent_Kinematics.md`

**Disposition:** REVISE  
**Priority:** P2

### Required changes

- Retain chart-persistence as a pregeometric kinematic construction.
- Do not infer operator microcausality or a physical light cone from continuation alone. Import these only after selecting the FP VI local hyperbolic realization.
- Replace global-right-inverse horizon language with loss of compatible continuation, exterior decoder, or global chart.
- Distinguish worldline termination in an encoding from termination of upper-world dynamics.
- State that position/worldline constructions are equivalence classes of admissible chart representations.

## `The_Modal_Triplet_Theory_Program_A2__Computation_and_Predictive_Limits.md`

**Disposition:** NARROW THEOREMS  
**Priority:** P1

### Required changes

- Change generic undecidability to a conditional theorem: any realization robustly embedding a universal two-counter machine has undecidable selection reachability.
- Do not infer computational irreducibility from non-Markovianity or finite capacity alone.
- Reconcile unbounded counters with finite admissibility capacity and finite prediction depth.
- Separate undecidability, complexity lower bounds, and inability to predict without full simulation.

## `The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md`

**Disposition:** RETITLE AND NARROW  
**Priority:** P0/P1

### Required changes

- Recommended title: `Circle–Lens–Nil as an Obstruction Taxonomy and Its Minimal Curvature Realizations`.
- Replace `three and only three` by `three coarse obstruction profiles` unless a category of objects, morphisms, refinements, and higher descent data is specified and exhaustiveness is proved.
- Distinguish nontrivial flat holonomy from curvature. A one-dimensional \(S^1\) can carry nontrivial monodromy with zero curvature.
- Make dimension additivity conditional on independent transverse coordinate factors.
- State that the four-dimensional base is an input to the \(4+6\) realization, not selected by this theorem.
- Treat \(2+2+2=6\) as a minimal nonzero-curvature realization class.

## `The_Modal_Triplet_Theory_Program_B1__Gravity_as_Kinematic_Consistency_Encoding.md`

**Disposition:** RECLASSIFY  
**Priority:** P2

### Required changes

- Present gravity as a canonical realization of circle-type consistency/holonomy obstruction, not the unique response to every such obstruction.
- Separate kinematic compatibility, existence of a Lorentzian metric, and Einstein dynamics.
- Use the FP principal-symbol/local-action construction for physical causal geometry.
- Do not infer Einstein equations from obstruction taxonomy alone.

## `The_Modal_Triplet_Theory_Program_B2__Gauge_Structure_as_Redundancy_Encoding.md`

**Disposition:** RECLASSIFY  
**Priority:** P2

### Required changes

- Present principal-bundle gauge redundancy as a canonical lens-type realization.
- Nonuniqueness of representatives is not automatically a failure of global description; principal bundles are globally defined despite lack of a preferred gauge.
- Specify the category in which a lens obstruction prevents a global section or faithful representative.
- Do not claim uniqueness of Yang–Mills structure without a classification theorem.

## `The_Modal_Triplet_Theory_Program_B3__Quantization_as_Discrete_Constraint_Encoding.md`

**Disposition:** RECLASSIFY  
**Priority:** P2

### Required changes

- Present discrete survivor structure as a canonical nil-type response, not a unique proof of complex quantum mechanics.
- Classical symbolic dynamics and topological sectors can also produce discrete survivors.
- Separate spectral discreteness, noncommutative observable algebra, complex amplitudes, and Born probability.
- Move Hilbert/CCR/CAR/probability claims to independent reconstruction theorems.

## `The_Modal_Triplet_Theory_Program_B4__Encoding_Intersections_and_Structural_Rigidity.md`

**Disposition:** NARROW  
**Priority:** P2

### Required changes

- Make rigidity conditional on a specified obstruction category, representation class, anomaly constraints, and overlap maps.
- Do not identify the Standard Model as uniquely selected without an exhaustive classification of alternative representations and topologies.
- Distinguish consistency of one intersection from uniqueness of the observed intersection.

## `The_Modal_Triplet_Theory_Program_B5__Saturated_and_Unified_Encodings.md`

**Disposition:** NARROW  
**Priority:** P2

### Required changes

- Treat string-like extended carriers and dualities as realizations of saturation, not inevitable consequences unless uniqueness is proved.
- State all anomaly, dimensional, and extended-object assumptions.
- Separate existence of a saturated encoding from physical selection of that encoding.

## `The_Modal_Triplet_Theory_Program_C__Realizing_the_Modal_Triplet_Core.md`

**Disposition:** REVISE  
**Priority:** P2/P3

### Required changes

- Make this paper authoritative for the dictionary between coordinate factors, vertical operators, bundles, line bundles, and the spatial-triplet representation.
- Use \(M_{10}=Y_4\times X_6\) consistently.
- State explicitly that realization nonuniqueness limits physical predictivity until one realization is selected.
- Remove or quarantine invalid explicit realizations, especially the Iwasawa construction.

## `The_Modal_Triplet_Theory_Program_D1__The_Dark_Sector_as_Missing_Encodings.md`

**Disposition:** INTERPRETIVE ONLY  
**Priority:** P2

### Required changes

- Do not infer pressureless, collisionless dark matter or accelerated expansion solely from missing encodings.
- Require a covariant effective stress tensor, modified field equation, or action.
- Confront lensing, Bullet-Cluster-type systems, CMB peaks, BAO, structure growth, and equation-of-state data before claiming a physical model.
- Retitle or label as a projection-first dark-sector hypothesis.

# Group 2 — Meta, diagnosis, universality, and closure

## `Closure_and_Inevitability_in_Modal_Triplet_Theory.md`

**Disposition:** RETITLE AND REWRITE  
**Priority:** P0/P1

### Required changes

- Recommended title: `Conditional Closure Relations in Modal Triplet Theory`.
- Delete the claim that one inverse obstruction yields irreversibility, probability, Hilbert structure, gravity, horizons, and area entropy without additional assumptions.
- Replace with separate implications: fiber splitting → no autonomous reduced map; effective merger → no prior-effective-state decoder; mixing plus invariant measure → effective stochasticity; local upper net plus fiberwise reduction → microcausality.
- Keep Born weights, complex Hilbert space, Einstein dynamics, and entropy normalization as independent theorem targets.
- Remove global-right-inverse language.

## `Coherent_Sector_Universality_and_Controlled_Truncation_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE  
**Priority:** P1

### Required changes

- Specify domains of all block operators and the spectral parameter in the Schur/Feshbach reduction.
- Replace schematic \(\|\delta T\|^2/\Delta\) by the actual product \(\|PTQ\|\|(QTQ-z)^{-1}\|\|QTP\|\).
- Do not call internal operator commutator bounds `bounded geometry` without a precise analytic definition.
- State universality only within a class preserving the gap, rank, projector bounds, and block-domain control.
- Do not equate the internal modular generator with physical time evolution without a model-specific theorem.

## `Coherent_Universality_and_the_Inevitability_of_Projection_Based_Quantum_Theories_v2.md`

**Disposition:** NARROW CLASSIFICATION  
**Priority:** P1

### Required changes

- Replace `all viable theories are forced into one universality class` with a conditional classification under explicitly listed empirical and reconstruction assumptions.
- Do not infer a smooth four-dimensional UV filter from internal spectral suppression.
- Do not infer topology-driven observed matter content without fixing representation and topology classes.
- Separate necessary conditions for stable effective theories from sufficiency for quantum theory or gravity.

## `Computational_Irreducibility_from_Projection__Undecidability_of_Selection_Events_in_Coherent_Quantum_Dynamics.md`

**Disposition:** NARROW  
**Priority:** P1

### Required changes

- State the result conditionally on an explicit robust embedding of a universal two-counter machine.
- Prove that counter storage and operations remain admissible for arbitrarily long runs, or limit the theorem to the finite admissible horizon.
- Do not derive universal computation from projection, record stability, or locality alone.
- Separate undecidability of reachability from computational irreducibility of all MTT trajectories.

## `Deterministic_Projection__Diffusive_Limits__and_Knee__Like_Threshold_Transitions.md`

**Disposition:** KEEP WITH SCOPE REFINEMENT  
**Priority:** P2

### Required changes

- Retain the explicit finite-dimensional example as an existence proof.
- State that its invariant measure, mixing, diffusion limit, and knee behavior are model inputs/results, not generic consequences of projection.
- Use a specific first-passage problem before calling a crossover universally logistic.
- Separate deterministic homogenization from Born probability.

## `Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md`

**Disposition:** REVISE  
**Priority:** P1/P2

### Required changes

- Remove `absence of a global right inverse` as a structural falsifier.
- Use falsifiers such as failure of descent, failure of a stated gap/projector/contraction estimate, or failure of a held-out prediction.
- Add the claim-status vocabulary and numerical provenance rules.
- Require admissibility to be computed before comparison with the data it is used to exclude.

## `Selection_Fronts_and_Boundary_Layer_Physics_at_the_Admissibility_Threshold.md`

**Disposition:** REVISE  
**Priority:** P2

### Required changes

- Define a complete margin including gap, projector, well-posedness, descent, coherent stability, and truncation reserves.
- Distinguish diagnostic divergence from a physical force or potential.
- Separate chart exit from the post-exit reset/selection law.
- Do not claim universal sigmoid, metastability, or first-passage scaling without a specified reduced stochastic model.

## `Universality_and_Robustness_of_the_Coherent_Sector_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE  
**Priority:** P1/P2

### Required changes

- Use explicit block-operator and resolvent assumptions.
- State whether robustness is operator-norm, graph-norm, form, or semigroup robustness.
- Treat the result as local to a controlled admissible class, not global universality.
- Separate projector stability from dynamical stability and from physical equivalence.

# Group 3 — Core Foundation papers

## `Modal_Triplet_Theory__Foundation_v6 (1).md`

**Disposition:** MAJOR REVISION; RETAIN AS CORE  
**Priority:** P0/P1

### Required changes

- Adopt the dimension-neutral Hilbert-bundle structural form and the canonical \(Y_4\times X_6\) physical realization.
- Represent the triplet by strongly commuting vertical operators or one total internal operator.
- Separate stabilization flow \(R_\tau\), physical evolution \(U(t_2,t_1)\), and RG scale.
- Correct the generator sign: use a stable semigroup or dissipativity bound.
- Use nonnormal-safe semigroup control.
- Distinguish gap, invariance, existence, contraction, truncation, and selection.
- Call \(T_\tau\Psi_\ast=\Psi_\ast\) a projected time-step fixed point until stationarity is proved.
- State Banach correctly: strict contraction on a complete invariant domain gives existence and uniqueness.
- Use a correct Schur/Feshbach block theorem with domain assumptions.
- Treat selection \(S\) as a hybrid reset law unless derived from upper continuation.
- Replace the positive Gram metric as a Lorentzian candidate with a principal-symbol construction.
- Separate internal gap, coherent contraction, and external cutoff scales.
- Add the complete admissibility-margin ledger.
- Add the typed world-in-world comparison field and prove the local
  `Mat(3,R) = so(3) + Sym(3,R)` decomposition.
- State that `1+3 x 3=4+6` is a component identity, not dimension or signature
  selection.
- Record the selected q79 `1+2+3` trace-split carrier and leave its
  bundle-and-connection intertwiner as an explicit downstream theorem.

## `The_Projection__Admissibility_Principle__Structural_Constraints_on_Effective_Physical_Description (1).md`

**Disposition:** WITHDRAW CENTRAL THEOREM AND REPLACE  
**Priority:** P0

### Required changes

- Delete all uses of noninjectivity to prove absence of a right inverse.
- Replace the definition of effective evolution \(T=P\Phi:X\to Y\) with a factor-through theorem on the effective quotient.
- Separate microscopic decoder, section, reduced dynamics, and effective merger.
- Do not claim probability without a measure.
- Do not claim entropy, geometry, or Hilbert structure as corollaries of one inverse theorem.
- Update every appendix realization accordingly.

## `Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory.md`

**Disposition:** MAJOR SCOPE CORRECTION  
**Priority:** P1

### Required changes

- Replace `the internal gap is the effective cutoff` with `the internal gap is an internal mass/truncation scale`.
- Do not state that modes with high four-dimensional energy are exponentially damped unless an external base operator is derived.
- Do not state that fifth-force, Lorentz-violation, GW, GR, or cosmological constraints are automatically satisfied merely by taking \(\lambda_\ast\) large.
- Separate \(\lambda_\ast^{\mathrm{int}}\), \(\Lambda_{\mathrm{4D}}\), curvature suppression, and coherent contraction.
- Treat Planck-scale relations and curvature corrections as model-dependent.
- Keep the paper as a consistency ledger with no predictions.

## `Coherent_Kinematics_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE  
**Priority:** P2

### Required changes

- Retain chart persistence and worldline equivalence as encoding-level kinematics.
- State that physical locality and null cones come from the selected FP VI hyperbolic realization.
- Replace global-right-inverse language at horizons with loss of compatible encoding, exterior decoder, or chart continuation.
- Do not infer a physical causal order solely from the partial order of admissible continuation.

## `Signature_Selection_and_Exclusion_in_Modal_Triplet_Theory.md`

**Disposition:** WITHDRAW GRAM THEOREM; RETITLE  
**Priority:** P0/P1

### Required changes

- Recommended title: `Lorentzian Base Compatibility and Signature Stability in the MTT Fixed-Point Realization`.
- Delete the claim that a positive Hilbert-space Gram tensor can have Lorentzian signature.
- Use the principal symbol of the local physical field equations.
- State that \(3+1\) base dimension is assumed in the canonical FP realization unless a separate dimension-selection theorem is proved.
- Recast exclusions of Euclidean, \(2+2\), and higher-time signatures as conditional hyperbolicity/stability arguments, not universal no-go theorems.
- State explicitly that neither the `3 x 3` comparison-field count nor the
  rank-six q79 carrier determines principal-symbol inertia.

## `Modal_Triplet_Theory__MTT_as_a_Superset_v2.md`

**Disposition:** RECLASSIFY  
**Priority:** P2

### Required changes

- Replace `derives/contains all frameworks` with typed relationships: reconstruction, embedding, controlled reduction, interpretive correspondence, or conditional bridge.
- Do not use completed constructive QG, exact Born rule, exact SM, or numerical closure as evidence until repaired.
- State that multiple realizations create underdetermination unless a canonical model is selected.

# Group 4 — Fixed Points I–VI

## `Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v5.md`

**Disposition:** KEEP WITH TECHNICAL CORRECTIONS  
**Priority:** P1/P3

### Required changes

- State that the base in FP I is a Riemannian analytic/control geometry, not automatically physical Lorentzian spacetime.
- Preserve the correct distinction between \(H_F^1\) and full \(H^1\).
- For the Schauder route, state the topology in which compactness holds. Use additional smoothing \(H^{1+\delta}\hookrightarrow\!\hookrightarrow H^1\), or apply Schauder in \(L^2\) using \(H^1\hookrightarrow\!\hookrightarrow L^2\).
- Treat global well-posedness and smoothing as standing hypotheses that must be verified in each model.
- Preserve the variational, Schauder, and Darbo routes as separate existence mechanisms.
- Require coherence invariance before a coherent constrained minimizer is a full equilibrium.
- Harmonize the displayed Céa-type prefactor and the surrounding \(w_0\)-normalization.
- Keep the singular \(\varepsilon\downarrow0\) base-regularizer limit conditional on uniform bounds and \(Q\)-sector control.

## `Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v2.md`

**Disposition:** MAJOR TECHNICAL REVISION  
**Priority:** P0/P1

### Required changes

- Replace the seven-dimensional example \(S^1_{\mathrm{cen}}\times T_1^2\times T_2^2\times T_3^2\) with \(T_1^2\times T_2^2\times T_3^2\) plus a central \(U(1)\) bundle.
- State strong commutation of the unbounded vertical operators.
- Use \(M_{10}=Y_4\times X_6\) and treat the triplet as vertical structures.
- Use a Riemannian base control operator or Cauchy-slice Laplacian, not the Lorentzian d'Alembertian.
- Separate physical \(t\) from stabilization \(\tau\).
- Do not use \(e^{-\lambda_A\tau}\) in a global estimate containing coherent modes. Use separate \(P\)- and \(Q\)-sector estimates.
- Do not build a coherent invariant ball from the \(Q\)-sector gap. Use coherent energy, base coercivity, or monotonicity.
- Add a strict Lyapunov/gradient identity before identifying a time-\(\tau\) fixed point with an equilibrium.
- For base-diffusion FCC, remove/lift the scalar zero mode or work in a mean-zero/boundary-conditioned subspace.
- State enough smoothing for Schauder compactness.

## `Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v3.md`

**Disposition:** MAJOR TECHNICAL REVISION  
**Priority:** P1

### Required changes

- Use a joint modal index \(\alpha\) or multi-index on a product internal fiber.
- Write the unabsorbed nonlinear equation as \(\dot a_\alpha=-d_\alpha a_\alpha+R_\alpha+\eta_\alpha\), with a one-sided bound defining \(\gamma_\alpha=d_\alpha-L_\alpha\).
- Separate stochastic noise power \(q_\alpha\) from deterministic force amplitude \(f_\alpha\).
- Use stochastic floor \(q_\alpha/(2\gamma_\alpha)\) and deterministic amplitude floor \(f_\alpha/\gamma_\alpha\).
- Restrict `if and only if \(\gamma_\alpha>0\)` to exact OU dynamics or robust worst-case stability.
- Do not call the nonlinear invariant law Gaussian unless the dynamics is exactly linear OU.
- State bundlewise stability for \(Q\Psi\) unless coherent disturbance is separately controlled.
- Use the appropriate stochastic trace condition or deterministic weighted series.
- Correct the fast–slow scaling so the averaged drift \(\bar g\) appears in the limit.
- Correct the Green–Kubo normalization to \(D=\int_0^\infty(R+R^\ast)\,ds\).
- Add functional CLT, tightness, and rough-path assumptions for the Stratonovich limit.
- Distinguish deterministic fixed points from stochastic invariant measures.

## `Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v3.md`

**Disposition:** MAJOR TECHNICAL REVISION  
**Priority:** P1

### Required changes

- Normalize the Weitzenböck formula as \(L=\nabla^\ast\nabla+\mathcal R\).
- Separate the negative curvature part, coherent/noncoherent mixing, and curvature gradients.
- Prove gap persistence under the full curved operator or rebuild the Riesz projector from that operator.
- If \(Q\mathcal RP\neq0\), include the curvature-induced leakage term and state a leakage floor.
- Use a Karcher/Fréchet mean or a specified normal chart for a centroid on a manifold.
- Use a first-order modulation law for the first-order FP gradient flow.
- Retain a second-order Newtonian law only for an explicitly inertial parent equation.
- From an absolute cross-term estimate conclude \(|E_{\mathrm{int}}|\le C\mathcal O\), not a positive two-sided estimate.
- Require a sign assumption for attraction or repulsion.
- Replace the schematic barrier inequality with a Lyapunov mountain-pass or total-energy-plus-work theorem.
- Separate detection of a transition from determination of the post-transition basin.

## `Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v5.md`

**Disposition:** MAJOR TECHNICAL REVISION  
**Priority:** P0/P1

### Required changes

- Rename the noncoherent projector \(Q_{\mathrm{inc}}\) and stochastic covariance \(Q_\xi\).
- Use a Hermitian-part dissipativity condition for a possibly nonnormal damping matrix.
- State stationary covariance only for frozen/stationary coefficients; use a differential Lyapunov equation otherwise.
- Correct normalized cross-correlation bounds to use the smallest positive eigenvalues of the self-covariance blocks.
- State that the cross-noise-only theorem assumes block-diagonal drift; include off-diagonal deterministic coupling otherwise.
- Replace the claim that a nonlinear Lipschitz transform of a Gaussian process is Gaussian.
- Use Gaussian concentration for Lipschitz functionals and require a pathwise Lipschitz solution map.
- Include the mean and expected supremum in the Borell–TIS threshold.
- Require all-time-pair cross-correlation control for simultaneous path-supremum events.
- Do not infer causal non-propagation from rarity of simultaneous exits.
- Rename \(-\sum w_j\lambda_j\) as a finite gap score or replace it with a complete margin barrier.
- State that a driver/barrier is diagnostic unless it enters a separately derived action.
- Separate exit detection from post-exit selection.

## `Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v3.md`

**Disposition:** MAJOR REVISION; RETAIN AS PHYSICAL SPINE  
**Priority:** P0/P1

### Required changes

- Use the canonical \(Y_4\times X_6\) geometry and separate \(U(t_2,t_1)\) from \(R_\tau\).
- Add the explicit Fixed-Point Locality-Descent Theorem.
- Restrict compressed local observables to the coherent-preserving algebra or use a conditional expectation.
- Replace coherent uniqueness based on internal positive eigenvalues with actual coherent-sector coercivity or monotonicity.
- Treat curvature-dependent masses as local effective parameterizations with spectral perturbation and gap-persistence assumptions.
- Do not infer merger from overlap alone; require attractive interaction and basin accessibility.
- Split the local action from the bilocal double-integral functional. Do not integrate an already integrated functional again.
- Prefer an explicit local mediator for exact causal overlap interactions. An equal-time spatial kernel is a nonlocal effective model.
- Correct the stationary covariance equation to \(A\Sigma+\Sigma A^\ast+Q_\xi=0\).
- Replace spectral-abscissa inverse/covariance bounds with semigroup or weighted dissipativity bounds.
- Add \(\hbar\) and CCR assumptions to the quantum covariance inequality.
- Complete metric variation for \(\xi R|\varphi|^2\), higher-curvature masses, and metric-dependent kernels.
- Strengthen Sobolev and kernel assumptions in the well-posedness statement.
- Use a complete admissibility margin and distinguish exit from selection completion.
- Label the Einstein–gauge–scalar–spinor action as a candidate realization, not a theorem derived from FP I–V.
- Label particles, fermions, entanglement, quantization, time, cosmology, and entropy according to their additional assumptions.

# Group 5 — Dirac-delta and finite-kernel program

## `Canonical_Coherent_Kernels_from_MTT_Fixed_Point_Data.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Specify whether \(A\) acts internally, spatially on a Cauchy slice, or in Euclidean signature.
- If \(AP=0\), state explicitly that \(Pe^{-\tau A}P=P\); there is no additional \(\tau\)-smoothing of the harmonic sector.
- Do not replace every spacetime delta universally. The kernel is a sector identity only in the chart for which \(A,P,\tau\) are derived.
- Changing CCR kernels changes the symplectic algebra and requires an independent consistency proof.

## `Classical_Constraint_Deltas_and_Microcanonical_Shells__Admissibility_Shell_Limits_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- KEEP the coarea and approximate-identity theorems.
- Retain regular-value, compactness, and finite-measure hypotheses.
- Label the MTT admissibility-shell reading as interpretation, not derivation of classical constraints.

## `Coherent_Green_Functions__Replacing_Point_Sources_by_Admissible_Kernels_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- KEEP the spectral/heat-kernel mathematics.
- Do not call a finite source physically selected until a concrete FP sector supplies \(A,P,\tau\).
- Distinguish a sector identity from an approximation to the full identity.
- State whether locality, covariance, and gauge constraints survive the chosen kernel.

## `Contact_Interactions_and_Renormalization_as_Over__Sharp_Projection__Finite_Coherent_Overlap_Vertices_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Treat finite overlap vertices as nonlocal EFT interactions unless a local parent mediator is supplied.
- Do not infer all-loop renormalization or UV completion from finite contact width.
- Check gauge/BRST and Lorentzian causal compatibility.

## `Deriving_the_MTT_Coherence_Scale_from_Fixed__Point_Damping.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Do not identify \(\tau\) or an external spatial width uniquely with \(\lambda_\ast^{-1}\) without a derived operator relation.
- Separate internal damping time, coherent contraction time, Cauchy-slice filter width, and external EFT cutoff.
- Label any proportionality as realization-dependent.

## `Dirac_Delta_Functions_as_Singular_Shadows_of_Admissible_Projection.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep as a structural dictionary.
- Do not imply every delta in physics originates from the same MTT projector.
- Distinguish exact symmetry/bookkeeping deltas from physical resolution kernels.

## `Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Specify the operator variables and spectrum.
- Distinguish sharp projector, smooth filter, and positive measurement effect.
- Do not infer four-dimensional UV filtering from an internal projector.

## `Finite_Time_Scattering_and_S_Matrix_Deltas_as_Asymptotic_Bookkeeping_Limits.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep finite-time delta approximations as standard scattering mathematics.
- Do not claim an MTT correction without a derived preparation, detector, or finite-time window.
- Separate finite experimental time from fundamental admissibility width.

## `Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Right-inverse/section language is appropriate here.
- Add that a gauge section selects a representative and does not recover a unique ontic configuration.
- Address Gribov/global-section obstructions in the actual gauge bundle.

## `Measurement_Effects_as_Finite_Survivor_Basin_Kernel_s_Projective_Collapse.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Ensure the effects form a normalized POVM.
- State that probabilities still require a state and the Born trace rule.
- Do not identify finite effects with outcome selection without a transition instrument.

## `Momentum_Conservation_Deltas_and_Bookkeeping_Closure_Exact_Vertex_Conservation.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Preserve exact momentum-conservation deltas when exact translation symmetry holds.
- Finite windows describe broken symmetry, finite volume/time, or detector resolution—not a universal softening of conservation.
- State the Ward/Noether basis of exact conservation.

## `MTT_Corrected_Contact_Loops_and_Finite_One_Loop_Tadpoles.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep as explicit Euclidean benchmark calculations.
- Do not generalize one-loop finiteness to all diagrams or physical Lorentzian amplitudes.
- State dependence on the chosen external filter.

## `MTT_Corrected_Propagators_and_UV_Behaviour.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Treat external momentum damping as an additional model assumption.
- Do not infer it from the internal gap.
- Prove or separately assume reflection positivity, gauge invariance, and Lorentzian unitarity.

## `Path_Integral_Constraints_as_Finite_Admissibility_Filters.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Label finite constraint filters as a regularization/representation choice unless derived from a physical operator.
- Check BRST/Faddeev–Popov consistency for gauge constraints.
- Distinguish Euclidean weighting from Lorentzian causal evolution.

## `Spectral_Delta_Peaks_and_Resonances_as_Survivor_Basin_Idealizations.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep the standard finite-width resonance interpretation.
- Derive widths and line shapes from a specified generator or self-energy.
- Do not infer universal basin physics from the mathematical limiting relation alone.

## `Wave__Particle_Duality_as_Projection_Duality_in_Modal_Triplet_Theory_v4.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep as an interpretive encoding paper.
- Connect wave and particle encodings to explicit observables/instruments before claiming an operational derivation.
- Do not infer the Born rule from dual encodings.

## `White_Noise_and_Markov_Limits_as_Delta_Correlation_Idealizations.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep the scaling-limit mathematics.
- Require positivity, normalization, mixing, and functional-limit assumptions.
- Distinguish an effective Markov limit from fundamental noise.

# Group 6 — Quantum mechanics and probability

## `Modal_Triplet_Theory__From_MTT_to_Quantum_Mechanics_v3.md`

**Disposition:** RECLASSIFY AS RECONSTRUCTION  
**Priority:** P1

### Required changes

- State explicitly which Hilbert, symplectic, self-adjoint, and unitary structures are assumed.
- Separate compression to a coherent Hilbert sector from derivation of quantum noncommutativity.
- Use a valid clock POVM or Mandelstam–Tamm theorem instead of an unsupported self-adjoint time-operator Robertson bound.
- Separate Gleason-type probability characterization from the MTT basin–trace theorem.
- Do not claim the Born rule until \(\nu_\rho(B_i)=\operatorname{Tr}(\rho E_i)\) is derived.
- Label the result as a coherent-sector reconstruction of QM.

## `Modal_Triplet_Theory__From_MTT_to_Indivisible_Stochastic_Processes.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P1

### Required changes

- Infinite memory does not imply absence of conditional factorization; every path law factorizes sequentially and is Markov on history space.
- Choose a precise concept: failure of Chapman–Kolmogorov, finite Markov order, process-tensor conditional independence, or CP divisibility.
- Do not infer infinite memory from failure of one-step descent; the missing information may be finite-dimensional.
- The exact realization of an arbitrary target kernel demonstrates flexibility, not prediction.
- A classical path-space algebra does not derive noncommutative quantum instruments.

## `Why_the_Born_Rule_and_the_Classical_Limit_Are_the_Same_Problem__A_Projection_Based_Shadow_Bridge_in_Modal_Triplet_Theory.md`

**Disposition:** RETITLE AND NARROW  
**Priority:** P0/P1

### Required changes

- Recommended title: `Born-Compatible Basin Measures and the Classical Concentration Limit`.
- Do not claim a unique squared-norm basin measure from projection alone.
- State the measure assumptions needed for a Gleason-style trace representation.
- Keep the MTT-specific equality between basin and trace weights as an open theorem.
- Separate the classical limit—concentration into one robust basin—from the derivation of quantum probabilities.

## `Why_Quantum_Theory_Must_Be_Complex__A_Sol_er__Admissibility_Rigidity_Theorem_in_Modal_Triplet_Theory.md`

**Disposition:** KEEP AS CONDITIONAL RECONSTRUCTION  
**Priority:** P2

### Required changes

- Put the Solèr hypotheses, infinite orthogonality, local tomography, continuous phase covariance, and no-doubling assumptions in the theorem statement.
- Do not claim projection alone excludes real or quaternionic Hilbert spaces.
- State composition and dimension qualifications.
- Recommended title: `Complex-Hilbert Rigidity under Solèr, Local-Tomography, and Phase-Composition Assumptions`.

## `Gravitationally_Induced_Collapse_as_an_Effective_Limit_of_Coherence_Breakdown_in_Modal_Triplet_Theory.md`

**Disposition:** MAJOR REVISION  
**Priority:** P0/P1

### Required changes

- Use \(Y_4\times X_6\), not \(Y_4\times B_1\times B_2\times B_3\) with unverified dimensions.
- Replace the ill-typed Nakajima–Zwanzig superoperator with reduction/lifting channels and \(\mathbf P=\mathcal J\mathcal R\).
- Normalize filtered density operators when the map is trace-decreasing.
- Do not derive a four-dimensional smearing length from an internal gap.
- Derive the DP kernel from a specified local curvature-coupling correlation function; curvature dominance alone does not fix it.
- A GKSL generator requires an actual Davies/weak-coupling/secular limit.
- Treat the logistic knee as a phenomenological interpolation unless a complete first-passage problem is solved.
- Retain Penrose/DP only as a restricted effective universality class.

# Group 7 — Quantum field theory and AQFT

## `From_Modal_Triplet_Theory_to_Algebraic_Quantum_Field_Theory.md`

**Disposition:** STRUCTURAL REWRITE  
**Priority:** P0/P1

### Required changes

- Base the physical net on the FP VI upper local net and the locality-descent theorem.
- Do not infer commutation from failure of joint representability.
- Do not assume every observable on a smaller chart extends to a larger chart.
- Inherit isotony from upper algebra inclusions and coherent-preserving reduction.
- Absence of a global chart does not imply absence of an abstract quasilocal algebra or colimit.
- Conclude instead that no globally admissible state, chart, or faithful representation may exist.
- Distinguish a pregeometric admissibility-indexed precosheaf from the physical Haag–Kastler net.

## `Modal_Triplet_Theory__From_MTT_to_Quantum_Field_Theory_on_Curved_Spacetime_v3.md`

**Disposition:** RECLASSIFY AS CONDITIONAL RECONSTRUCTION  
**Priority:** P1/P2

### Required changes

- Use the FP local net and Lorentzian principal symbol as upstream input.
- Treat CCR/CAR, Hadamard condition, microlocal spectrum condition, local covariance, time-slice axiom, and positivity as assumptions or independent QFT theorems.
- Use \(Y_4\times X_6\) geometry.
- Do not derive quantum theory from projection or Gaussian expansion alone.

## `Modal_Diagrammatics__The_Origin_of_Feynman_Rules_from_Coherent_Modal_Geometry.md`

**Disposition:** RETITLE / NARROW  
**Priority:** P2

### Required changes

- Recommended characterization: `Universal Perturbative Graph Structure of the Coherent Expansion`.
- Propagators and vertices follow from a quadratic-plus-interaction expansion, but this occurs in classical statistical field theory as well.
- Do not infer CCR/CAR, positivity, microcausality, or unitarity from diagrammatics.
- Use canonical geometry and derive all overlap vertices consistently.

## `Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md`

**Disposition:** RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Make amplitudes conditional on a valid QFT algebra, state, renormalization prescription, and asymptotic or in–in setup.
- Separate overlap-integral parameterization from a first-principles prediction.
- Do not call the amplitude program closed while QFT and QG positivity/scattering remain conditional.
- Publish held-out data and parameter provenance for phenomenological claims.

# Group 8 — Measurement, selection, black holes, and contextuality

## `Black_Hole_Information_Loss_and_Quantum_Measurement_Collapse.md`

**Disposition:** WITHDRAW BRIDGE THEOREM AND REPLACE  
**Priority:** P0

### Required changes

- Delete the right-inverse proof.
- The condition \(\Phi_t(U_+)\cap\Phi_t(U_-)\neq\varnothing\) is incompatible with an invertible flow on disjoint sets. Replace it with projected overlap.
- Separate fiber splitting, effective merger, and microscopic recovery.
- Describe islands through a restricted recovery channel on a code subspace or observable algebra, not a partial right inverse between mismatched spaces.
- Do not claim Born and Hawking weights arise from one measure unless the measure and both pushforwards are explicitly constructed.
- Treat horizon identification as a physical model assumption.

## `Measurement_as_Disturbance_and_Stabilization_in_Modal_Triplet_Theory_v5.md`

**Disposition:** REVISE  
**Priority:** P1/P2

### Required changes

- Keep localized disturbance plus basin-local stabilization.
- Replace `no effective right inverse` with failure of decoder, effective merger, or failure of descent.
- Add the transition-completion map/kernel specifying the post-exit basin.
- Separate decoherence within a basin from outcome selection between basins.
- Keep probabilities conditional on a preparation measure and Born theorem.

## `Determinism_Without_Superdeterminism__Projection_Induced_Stochasticity__Non_Randomness__and_Cascading_Stabilization_in_Modal_Triplet_Theory_v2.md`

**Disposition:** REVISE  
**Priority:** P1

### Required changes

- Use the FP III homogenization mechanism: deterministic fast dynamics + invariant measure + mixing + functional limit.
- Projection alone gives unresolved alternatives, not probabilities.
- Clarify measurement independence and whether the complete upper state includes settings or boundary data.
- Do not claim Bell-local factorization.

## `Measurement_Induced_Phase_Transitions_as_a_Shadow_of_Coherence_Basin_Dynamics.md`

**Disposition:** NARROW  
**Priority:** P2

### Required changes

- Keep basin-margin transitions as a model class.
- Do not call logistic knees, Zeno/anti-Zeno crossovers, or finite-strength thresholds universal.
- Derive each from a specified reduced generator, protocol, and first-passage problem.
- Use basin-local contraction and explicit boundary geometry.

## `Projection__Probability__and_Irreversibility__Shadow_Bridges_Between_Measurement__Black_Holes__and_Cosmology_in_Modal_Triplet_Theory_v2.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P0/P1

### Required changes

- Replace the old inverse theorem with the descent/recovery theorem.
- Separate structural analogy from one common probability measure.
- Do not identify Born, Hawking, and cosmological weights without one explicit upper measure and three derived pushforwards.
- Use restricted recovery maps for islands and codes.
- Label cross-domain comparisons as shadow bridges, not theorem-level equivalence.

## `Why_Decoherence_Cannot_Replace_Measurement__A_Projection_Based_Shadow_Bridge_in_Modal_Triplet_Theory.md`

**Disposition:** KEEP WITH ADDITION  
**Priority:** P2

### Required changes

- Retain the distinction between intra-basin suppression and inter-basin selection.
- Add the missing selection-completion map or kernel.
- Do not infer outcome probabilities from decoherence or chart exit.

## `Why_Quantum_Contextuality_and_Measurement_Order_Dependence_Are_the_Same_Phenomenon.md`

**Disposition:** NARROW  
**Priority:** P2

### Required changes

- Treat contextuality, incompatible valuations, noncommuting instruments, and order effects as related chart incompatibilities, not one theorem unless a categorical equivalence is constructed.
- Distinguish Kochen–Specker contextuality from disturbance-based sequential order effects.
- State the instrument algebra explicitly.

# Group 9 — Bell, entanglement, and time

## `Entanglement__Locality__and_Measurement_from_Coherent_Sector_Dynamics.md`

**Disposition:** KEEP WITH LOCALITY FORMALIZATION  
**Priority:** P1/P2

### Required changes

- Cite and use the FP locality-descent theorem.
- Define the coherent-preserving local algebra.
- Retain the distinction between commuting algebras and nonfactorizing states.
- Do not claim that admissibility alone proves all physically realized states are entangled.
- Treat local measurement instruments and entanglement reduction using standard CP-map assumptions.

## `Modal_Triplet_Theory__Modal_Fixed_Points__Bell_s_Beables__and_the_Limits_of_Factorization.md`

**Disposition:** REVISE INTERPRETATION  
**Priority:** P1

### Required changes

- State explicitly that MTT is not Bell-local in the conditional-factorization sense.
- The consistent package is upper-local dynamics + microcausality + no-signaling + globally nonfactorizing states.
- If \(\xi\) is called complete, explain how the setting-dependent global fixed point is determined: global boundary value, retrocausality, incompleteness, or nonseparable ontology.
- Do not call the construction a classical local hidden-variable completion.

## `Temporal_Bell_Inequalities_and_Global_Consistency_in_Modal_Triplet_Theory.md`

**Disposition:** KEEP WITH CLARIFICATION  
**Priority:** P2

### Required changes

- Separate physical measurement times from stabilization time.
- Attribute Leggett–Garg violation to invasiveness/context dependence and global history constraints, not projection alone.
- State the measurement instruments and update rules explicitly.

# Group 10 — Proto-spinor, closure strain, and unified action

## `The_Proto_Spinor__Triadic_Closure_from_Pointwise_Internal_Embedding_v4.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P1

### Required changes

- A stable right inverse selects a controlled representative; it does not recover the actual microscopic history.
- Distinguish assumed representation assignments from derived matter content.
- Derive mass through a normalized quadratic effective action or propagator pole.
- Do not infer one Higgs mode from a positive Hessian without proving the anchored quotient is one-dimensional.
- Add compact-resolvent or isolated-minimum hypotheses for discrete spectra.
- Place family indices on internal geometry and state all topology inputs.
- Replace universal internal-dimension-three and forced-Spin claims by a
  conditional double-cover theorem with a declared oriented rank-three bundle.
- Distinguish the q79 local `Dic_3` lift from the still-open strict global Spin
  obstruction calculation.
- Treat circle--lens--nil as carrier/operator roles. Do not use literal
  `S1 x Lens x Nil` or manifold nesting as a proof source.

## `Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P1

### Required changes

- Separate Standard Model representation input, anomaly checks, and genuinely selected output.
- Do not claim exact hypercharge derivation when observed charges appear in the constraints.
- Do not claim unique Higgs or family number without dimensional/index classification.
- Derive curvature from an explicit connection/distribution, not from \(\nabla s\neq0\) alone.
- Classify the result as a matter-encoding realization.
- Retain the exact local strain normal form
  `Sym(3,R) = R I + D0 + O` with dimensions `1+2+3`.
- Do not identify that local split with the q79 trace-split carrier by rank
  alone; require an explicit same-source intertwiner.
- Treat family, Higgs, charge, confinement, mixing, and CP statements as
  conditional encodings until their source operators are proved.

## `Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3.md`

**Disposition:** RECLASSIFY AS CONDITIONAL BRIDGE  
**Priority:** P2

### Required changes

- Construct the map between proto-spinor variables and worldsheet couplings explicitly.
- State the domain of validity and truncation error.
- Do not infer worldsheet consistency or target-space physics from analogy alone.
- Keep Weyl/Dirac/twistor regimes as conditional encodings.
- State that the bridge is local/quadratic unless worldsheet beta functions,
  Weyl and modular consistency, ghosts, and truncation errors are controlled.
- Use the q79 carrier as a target of a typed bridge, not as evidence that the
  bridge is already global.

## `World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4.md`

**Disposition:** INTERPRETIVE / CONJECTURAL  
**Priority:** P2

### Required changes

- Separate generative narrative from theorem statements.
- Do not claim time, gravity, matter, and quantization follow from one closure premise without explicit constructions.
- Use the canonical physical-time/stabilization-time split.
- Label the proto-geometric origin proposal as a research program.
- Replace ordinary base/fiber dimension multiplication by
  `Q_WW in Gamma(Hom(TP,TI))`.
- Retain `9=3+6` and `6=1+2+3` only as local representation decompositions.
- Separate a compact shared phase circle from noncompact physical time.
- State the missing globalization, q79 intertwiner, and strict Spin-obstruction
  theorems explicitly.

## `Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md`

**Disposition:** RETITLE AND MAJOR REVISION  
**Priority:** P0/P1

### Required changes

- Recommended title: `Closure Geometry and a Regime-Local Ten-Dimensional Action Ansatz`.
- State that a slab-local pseudo-Riemannian metric is assumed; this is incompatible with saying no metric is assumed while integrating \(\sqrt{-g_{10}}R_{10}\).
- Call the action a minimal ansatz, not the most general action.
- Enumerate omitted symmetry-allowed EFT operators.
- Mass is not identical to a closure cost until a pole/dispersion relation and normalization are derived.
- A positive Hessian does not imply a unique radial Higgs direction.
- Nil-boundary divergence does not guarantee isolated minima or discrete spectrum.
- Nonuniform strain does not imply Frobenius failure. Define the distribution and compute its curvature.
- Analyze degrees of freedom and possible ghosts from curvature–strain derivative couplings.
- The action imports the Einstein–Hilbert term; the reduction is not a projection-only derivation of GR.
- Add a genuine consistent-truncation condition for discarded equations.
- Remove direct claims of deriving the full Standard Model.
- State that `M10 -> Y4` and its Lorentzian metric are realization inputs, not
  consequences of the `1+3 x 3` component count.
- Use q79 Fu--Yau geometry as the current selected compactification candidate
  and Lens--Nil only as an auxiliary/effective model.
- Require the discarded-mode equations, source-normalized pole observables,
  and the same-source local-to-q79 intertwiner before claiming a physical
  reduction.

# Group 11 — General relativity, geometry, and inflation

## `Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md`

**Disposition:** RETITLE AND NARROW  
**Priority:** P1

### Required changes

- Recommended title: `Controlled Coherent Reduction to Four-Dimensional Einstein Gravity`.
- Use \(M_{10}=Y_4\times X_6\).
- State that the higher-dimensional Einstein–Hilbert sector is an input.
- Separate metric/causal emergence, uniqueness of the leading two-derivative metric action, and dimensional reduction.
- Add the consistent-truncation condition \(Q\,\delta S/\delta\Phi|_{\Phi_{\mathrm{coh}}}=O(\lambda_\ast^{-1})\).
- Address harmonic moduli, KK vectors, scalar zero modes, warping, and stabilization.
- Do not use the positive Gram tensor as the Lorentzian metric.

## `Why__GR_Falls_Out_of_String_Theory___A_Coherent_Admissibility_Shadow_Bridge_in_Modal_Triplet_Theory.md`

**Disposition:** RECLASSIFY AS CONDITIONAL BRIDGE  
**Priority:** P1/P2

### Required changes

- State the explicit bridge map between worldsheet beta functions and the spacetime effective equations.
- Do not call fixed-point correspondence ontological identity.
- Make all \(\alpha'\), loop, truncation, and weak-coupling errors explicit.
- Use `under a controlled encoding map` in theorem statements.

## `Why_General_Relativity_and_String_Theory_Are_the_Same_Admissibility_Constraint.md`

**Disposition:** RETITLE / NARROW  
**Priority:** P1

### Required changes

- Replace `same constraint` with `controlled correspondence of diagnostics on an overlap domain` unless a bijective equivalence is proved.
- State shared assumptions and breakdown surfaces.
- Do not transfer fixed points merely by assuming conjugacy and then present the result as a derivation.

## `Inflationary_Measures_and_the_Born_Rule_as_a_Single_Shadow__Bridge_Problem.md`

**Disposition:** INTERPRETIVE MODEL; REMOVE DERIVATION CLAIM  
**Priority:** P1/P2

### Required changes

- The functions \(C(N)=\kappa(N_c-N)\), \(\Delta A/\hbar=\lambda/C^2\), and the volume factor are ansätze.
- Do not claim one basin functional yields the Born rule until the basin–trace theorem is proved.
- Do not claim normalizability or model preference as MTT prediction without deriving the base measure and priors.
- Use current observational data only in a separate, reproducible model-comparison pipeline.
- Retain as an illustrative admissibility-weighted cosmology model.

# Group 12 — Quantum gravity and asymptotic-safety bridges

## `Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md`

**Disposition:** RETITLE AND WITHDRAW CENTRAL CLAIMS  
**Priority:** P0

### Required changes

- Recommended title: `An SPT-Filtered Euclidean TT Model and Its Conditional Perturbative Properties`.
- External Gaussian damping is an additional factorization assumption, not a consequence of the internal gap.
- A positive Laplace representation is not automatically a Stieltjes/Källén–Lehmann representation.
- A nonzero positive physical spectral propagator cannot also have exact external Gaussian asymptotics.
- Withdraw the theorem that one internal graviton line makes every graph absolutely convergent.
- Correct the direction of the Gaussian inequalities and analyze loop-rank control.
- Renormalize undamped matter subgraphs.
- Do not claim OS positivity, causal support, BRST consistency, or unitarity without independent proofs in the filtered theory.

## `Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P0/P1

### Required changes

- Prove trace-class covariance or formulate the measure on a precise abstract Wiener space; Hilbert–Schmidt alone is insufficient for the stated Hilbert-space Gaussian measure.
- Specify a stable/sectorial interaction class. Generic analytic factorial bounds do not imply constructive stability or Borel summability.
- Do not pass \(P\to\infty\) merely from uniform coefficient bounds; prove a Cauchy limit of Borel sums.
- Treat the Einstein–Hilbert interaction separately from stable polynomial examples.
- Reclassify as a conditional Euclidean constructive model until completed.

## `Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md`

**Disposition:** MAJOR NARROWING  
**Priority:** P0/P1

### Required changes

- Do not assume positivity on BRST cohomology follows automatically from TT reflection positivity.
- Prove Borel-summed Ward/QME identities with uniform bounds.
- Verify that SPT filtering preserves BRST/BV structure and boundary conditions.
- Construct the physical Hilbert space only after a genuine OS positivity theorem for the relevant gauge-invariant Schwinger functions.
- Label the current result conditional.

## `Constructive_MTT_Quantum_Gravity_III__Infrared_Limit_and_Scattering_under_SPT_Damping.md`

**Disposition:** RECLASSIFY AS MASSIVE/IR-REGULATED MODEL  
**Priority:** P0/P1

### Required changes

- A positive TT mass gap is not the physical massless graviton.
- Use dressed/inclusive asymptotic states for massless gravity or retain the result as an IR-regulated sector.
- Isometric wave operators imply a partial isometry, not a unitary S-matrix without equality of ranges/asymptotic completeness.
- Remove circular assumptions in which asymptotic flatness already includes existence of Møller operators.
- Address soft-graviton and infrared sectors.

## `Asymptotic_Safety_as_a_Truncation_Shadow_of_a_Coherent_Sector_UV_Endpoint.md`

**Disposition:** RECLASSIFY AS CONDITIONAL BRIDGE  
**Priority:** P1

### Required changes

- Do not infer an approximate fixed point from an additive-error contraction without a separate existence theorem.
- Construct the map between coherent variables and FRG couplings.
- State regulator, scheme, truncation, and domain dependence.
- For finitely many unstable directions, prove an essential spectral-radius/quasi-compactness bound.

## `Modal_Triplet_Theory_and_Asymptotic_Safety__Asymptotic_Safety_as_the_Controlled_FRG_Shadow_of_the_Coherent_Sector_UV_Endpoint.md`

**Disposition:** RECLASSIFY AS CONDITIONAL BRIDGE  
**Priority:** P1

### Required changes

- The scheme conjugacy is the central assumption; present the fixed-point correspondence as conditional on it.
- Do not claim scheme independence beyond the stated conjugacy/remainder norm.
- Add a rigorous unstable-subspace theorem.
- Separate FRG truncation fixed points from an exact UV-complete theory.

## `A_Third_Corner_Shadow_Bridge__Asymptotic_Safety__the_String_Corner__and_the_Coherent_Spine_in_Modal_Triplet_Theory.md`

**Disposition:** NARROW  
**Priority:** P1

### Required changes

- Controlled conjugacies transfer fixed points by assumption; do not present the transfer as an independent derivation of equivalence.
- Replace the additive-error Banach lemma with a valid perturbative fixed-point theorem.
- State all overlap-domain assumptions and errors.
- Use `conditional triple diagnostic correspondence` rather than `equivalence of completions`.

# Group 13 — Photons, topology, and Standard Model constraints

## `Topology__Only_Constraints_in_Modal_Triplet_Theory.md`

**Disposition:** MAJOR CLAIM RECLASSIFICATION  
**Priority:** P0/P1

### Required changes

- Rename exact hypercharge result as a difference-charge encoding when observed hypercharges are inserted.
- Use integer line-bundle powers \(L^{\otimes n}\) and physical charge \(Y=n/N_0\).
- Move family index to the internal manifold \(X_6\) or an internal cycle.
- Topological triviality \(c_1=0\) does not imply a flat connection or trivial holonomy.
- Correct Weyl/Dirac and real/complex scalar beta-function coefficients.
- Move \(c_{\mathrm{em}}=c_{\mathrm{grav}}\) to a conditional principal-symbol theorem.
- Classify anomaly cancellation, PQ, and operator-forbiddance results as consistency checks within supplied representations.

## `Topology_Only_Constraints_and_Forbidden_Operators_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE  
**Priority:** P1/P2

### Required changes

- Specify the exact line-bundle classes and selection rule for each forbidden operator.
- Do not infer all dangerous operators are absent from topology in every realization.
- Correct connection-versus-bundle-triviality statements.
- Separate lattice quantization from unique observed charge assignment.

## `Photons__Entanglement__and_Null_Updating_in_Modal_Triplet_Theory.md`

**Disposition:** REVISE INTERPRETATION  
**Priority:** P1/P2

### Required changes

- Use \(Y_4\times X_6\).
- Derive null propagation and two helicities from the Maxwell principal symbol, gauge constraints, and massless representation—not by excluding static and superluminal options alone.
- Keep global nonfactorizing photon states compatible with local propagation.
- Replace horizon right-inverse language with loss of a globally compatible exterior/interior encoding or decoder.
- Treat lensing/redshift interpretations as downstream readings of standard local equations.

## `The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md`

**Disposition:** INTERPRETIVE / NARROW  
**Priority:** P1/P2

### Required changes

- Represent the central circle as phase-bundle data, not an extra internal coordinate.
- Replace right-inverse barrier language.
- Do not identify closure cost with physical mass without a dispersion/pole theorem.
- Do not derive physical time without an explicit clock model.
- Treat gravity/inertia/time unification as a proposal pending construction.

# Group 14 — Coherence capacity program

## `Coherence_Capacity_as_the_Invariant_Admissibility_Margin_of_Modal_Triplet_Theory_v3.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- KEEP as the primary capacity definition.
- Use a normalized margin vector or distance to the inadmissible set.
- Specify the metric and normalizations.

## `Coherence_Capacity_as_the_Fundamental_Resource_of_Effective_Physics_v3.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Withdraw the old right-inverse proof.
- An arbitrary positive scalar with the correct zero set is not a canonical physical resource.
- Do not derive probability, force, entropy, or gravity from the margin alone.

## `Dynamics_of_Coherence_Capacity__Transport__Concentration__and_Exhaustion_v2.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- A conservation law requires an action/symmetry or explicit constitutive postulate.
- A reparameterization \(C\mapsto f(C)\) changes gradients and fluxes; fix normalization before physical transport claims.
- Label transport equations as model-level.

## `Horizons__Area_Laws__and_Entropy_from_Coherence_Capacity_Bottlenecks_v2.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- A bounded flux yields an area upper bound, not equality.
- Equality requires a saturation hypothesis and an independently derived coefficient.
- Use restricted recovery channels, not partial right inverses.
- Do not claim \(1/4G\) from capacity terminology alone.

## `Particles_and_Forces_as_Coherence_Basins_and_Capacity_Gradients_v2.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- A gradient of a diagnostic margin is not a force unless it enters an action/Hamiltonian/constitutive law.
- Derive particle masses and force laws from effective equations.
- Keep basin interpretation as a model proposal.

## `Capacity_Gated_Projection_Dynamics_v2 (1).md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- The implementation is a hybrid constrained stochastic dynamical system.
- Because it uses \(U=-\log(\varepsilon+C)\) and \(-\nabla U\), the barrier acts as a force/penalty in the algorithm despite the rhetorical denial.
- Define flow domains, guards, reset maps/kernels, and invariants.
- The algorithm is incomplete at \(C=0\) until a reset law is given.
- Call nonfactorizable coordination classical collective correlation unless a quantum algebra is supplied.

## `Projection_Induced_Network_Geometry (1).md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Do not infer a specific network geometry from absence of a section.
- Define the image \(\mathcal R=P(\mathcal A)\) and prove nonfactorization directly.
- Separate correlation constraints from graph edges.

## `Quantum_Field_Theory_Reconstruction_from_Coherence_Basin_Statistics_v2.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Classical basin statistics do not create noncommutative QFT.
- Require an independently defined CCR/CAR/AQFT algebra and state.
- Reclassify as a statistical representation unless the quantum algebra is constructed.

## `Cosmology_as_Global_Coherence_Capacity_Evolution_v2.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Supply a covariant action or field equation.
- Do not infer acceleration from global capacity exhaustion alone.
- Derive observables and confront cosmological data.

## `Projection_Limited_Coherence__A_Structural_Theory_of_Effective_Description_from_Fundamental_Physics_to_Consciousness_and_Civilization (1).md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Label cross-domain applications as analogy or hypothesis.
- Do not transfer physical conservation, entropy, or selection theorems to biology/cognition/civilization without domain-specific models.
- Keep the mathematical capacity definition separate from broad interpretation.

# Group 15 — EFT, KK, LQG, NCG, and pilot-wave encodings

## `Effective_Field_Theory_as_a_Shadow_of_Projection__Admissible_Dynamics.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Replace right-inverse claims with no unique UV decoder/left inverse and coarse-graining noninjectivity.
- Distinguish RG beta-function ODE reversibility from Wilsonian coarse-graining.
- Do not call every EFT cutoff the exact admissibility boundary without a model.
- Keep as structural interpretation.

## `Modal_Triplet_Theory__From_MTT_to_Kaluza__Klein_Theory.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Use the canonical \(4+6\) geometry.
- Treat KK masses as internal eigenvalues.
- Reclassify as controlled dimensional reduction, not derivation of extra dimensions.

## `Modal_Triplet_Theory__From_MTT_to_Loop_Quantum_Gravity_v3.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- State the imported \(3+1\) split, time gauge, SU(2), Holst action, and representation assumptions.
- Reclassify as an LQG embedding of the coherent gravitational sector.
- Do not derive the Immirzi parameter unless the map is explicit.

## `Loop_Quantum_Gravity_as_a_Shadow_of_Coherent_Fixed_Point_Dynamics.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Keep as an interpretive/embedding bridge.
- Do not infer spin networks or area spectra from projection without the Holst/holonomy-flux structure.
- State the overlap regime with FP geometry.

## `Fermions_in_Loop_Quantum_Gravity_from_Modal_Triplet_Theory__Coherent_Compression__Berry_Terms__and_Absence_of_Doubling.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Prove the lattice/operator no-doubling claim; coherent compression alone does not bypass Nielsen–Ninomiya-type conditions.
- State chirality, locality, Hermiticity, and lattice assumptions.
- Treat Berry terms as derived only after an explicit band bundle is constructed.

## `Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Starting from \(\mathbb C\oplus\mathbb H\oplus M_3(\mathbb C)\) is an almost-commutative embedding, not a derivation of the SM finite algebra.
- Specify the Lorentzian-to-Euclidean/Wick-rotation dictionary.
- Separate spectral action assumptions from FP projection.

## `The_Spectral_Action_as_a_Shadow_of_Coherent_Fixed_Point_Geometry.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Reclassify as a spectral-action encoding.
- State which spectral triple is assumed and how it is obtained from the coherent sector.
- Do not infer Standard Model uniqueness.

## `Modal_Triplet_Theory__From_MTT_to_Pilot__Wave_Dynamics.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Replace no-right-inverse barrier language with failure of current descent/velocity field or stable continuation.
- Treat Bohmian dynamics as a regime-limited reconstruction.
- Specify how the global configuration-space velocity remains compatible with upper-world locality and 4D no-signaling.

# Group 16 — String, Calabi–Yau, flux, and M-theory encodings

## `Flux_Compactifications_in_Heterotic_String_Theory_v3.md`

**Disposition:** WITHDRAW IWASAWA CONSTRUCTION PENDING REBUILD  
**Priority:** P0

### Required changes

- Use only closed integral two-forms as first Chern classes.
- Do not use \(c=(i/2)\omega_3\wedge\bar\omega_3\) as a Chern class when \(dc\neq0\).
- A trivial smooth bundle cannot carry nonzero topological \(c_3\).
- Global monad maps between nonisomorphic line bundles require global sections of the corresponding Hom bundles.
- Prove slope stability against all possible destabilizing subsheaves; \(H^0(E)=0\) is insufficient.
- Recompute the Bianchi identity with the rebuilt curvature.
- Correct any reversed small-fiber metric scaling in Fu–Yau-style arguments.

## `Modal_Triplet_Theory__From_MTT_to_Calabi__Yau_Compactifications.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Reclassify as a Calabi–Yau realization/embedding.
- State all supersymmetry, topology, metric, moduli, and stabilization assumptions.
- Do not infer unique CY geometry from MTT.

## `Modal_Triplet_Theory__From_MTT_to_M_theory.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Reclassify as an 11D embedding.
- State which M-theory action, flux, brane, and anomaly data are assumed.
- Do not call the eleventh dimension or branes derived from projection alone.

## `Modal_Triplet_Theory__From_MTT_to_String_Theory.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Reclassify as a string-theoretic encoding of an admissible sector.
- State the worldsheet CFT, Weyl, modular, ghost, and criticality assumptions.
- Do not derive string theory solely from saturation language.

## `Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Keep as a conditional fixed-point correspondence.
- Construct the map between FP variables and the Strominger flow.
- Do not infer existence of solutions without solving anomaly, stability, and global bundle constraints.

## `Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Restrict the selection theorem to the stated ansatz/parameter family.
- Distinguish consistency, dynamical attraction, and physical vacuum selection.
- Do not generalize isolated invariant-sector loci to the full landscape.

## `When_Is_a_Configuration_Physical____Rethinking_the_Vacuum_Selection_Problem.md`

**Disposition:** REVISE / RECLASSIFY  
**Priority:** P1/P2

### Required changes

- Keep as a conceptual admissibility essay.
- Do not identify absence of an admissible chart with nonexistence of the underlying mathematical solution.
- State the measure and dynamical assumptions needed for vacuum selection.

# Group 17 — Causal sets, invariants, and condensed-matter shadows

## `Causal_Sets_as_an_Effective_Limit_of_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Do not identify an internal gap with a four-dimensional sprinkling density without a base-resolution theorem.
- Treat Poisson sprinkling density as an added encoding choice unless derived.
- Keep as an effective coarse-graining construction.

## `Causal_Sets_as_Event_Selection_Shadows_of_Coherence_Breakdown.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Positive stability margins do not prove local finiteness or exclude Zeno accumulation.
- Prove a uniform dwell-time or event-density bound.
- Define the transition/reset law producing selection events.
- Do not claim Lorentz-invariant statistics without a concrete stochastic law.

## `Electromagnetic_Helicity_as_a_Coherent_Sector__Chern__Simons_Functional_in_Modal_Triplet_Theory_v2.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep the Chern–Simons/helicity mathematics under stated boundary and gauge assumptions.
- Do not claim a universal MTT prediction unless the coherent electromagnetic sector is derived.
- Track gauge invariance and boundary terms.

## `ETH_and_Many__Body_Localization_as_a_Single_Shadow__Bridge_Problem.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Treat ETH and MBL as model-dependent basin limits, not a universal equivalence.
- Use an explicit Hamiltonian/operator family and diagnostics.
- Derive any knee/crossover rather than impose it.

## `Topological_Phases_of_Matter_as_Admissible_Overlap_Structures.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep as an encoding/interpretation paper.
- State which topological invariants and symmetry classes are supplied.
- Do not infer all topological phases from generic overlap structure.

## `Twistor_Encodings_as_High_Coherence_Limits_of_Modal_Triplet_Theory.md`

**Disposition:** REVISE / KEEP WITH SCOPE  
**Priority:** P2

### Required changes

- Keep as a conditional high-coherence corner.
- Specify self-dual/integrable assumptions and the map to twistor data.
- Do not generalize to arbitrary MTT regimes.

# Group 18 — Theta closure and numerical execution

## `A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v2.md`

**Disposition:** MAJOR STATUS REVISION  
**Priority:** P0/P1

### Required changes

- Change Tier 3 and Tier 4 from completed to pending independent revalidation.
- Reclassify topology-only outputs according to the corrections in Group 13.
- Distinguish calibration, round-trip consistency, fit, and held-out prediction.
- Require reproducible code, raw inputs, and unit tests.
- Remove the invalid \(5\,\mathrm{TeV}\) crossing and all dependent status claims.

## `Superset_Determinations_in_Modal_Triplet_Theory_v2.md`

**Disposition:** RECALCULATE FROM SCRATCH  
**Priority:** P0

### Required changes

- Rebuild one- and two-loop RGE running from raw electroweak inputs.
- Unit-test against standard SM running and known crossing scales.
- Do not identify a gauge crossing with an MTT coherence scale without a separate theorem.
- Reclassify extracted \(\zeta\)-ratios and \(K\) as calibrations.
- Do not call \(\alpha_s\) a prediction if it participates in latent extraction, scale choice, or threshold fitting.

## `Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md`

**Disposition:** WITHDRAW NUMERICAL RESULTS PENDING UPSTREAM RECALCULATION  
**Priority:** P0

### Required changes

- Do not fit geometry to invalid Tier 3 targets.
- Rebuild global geometry, Kähler moduli, thresholds, and axion normalization after corrected inputs.
- Publish all constraints, priors, and degeneracies.
- Independently verify topology and stability.

## `Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md`

**Disposition:** RECLASSIFY AS FIT; REBUILD AFTER TIER 3/4  
**Priority:** P0/P1

### Required changes

- Do not present fitted Yukawa, CKM, PMNS, neutrino, and Higgs matrices as predictions without held-out tests.
- List all adjustable matrix entries, phases, textures, scale choices, and experimental inputs.
- Recompute only after the geometry and threshold sector is validated.

## `Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v2.md`

**Disposition:** REVISE  
**Priority:** P1/P2

### Required changes

- Separate exact algebraic identities from symmetry assumptions and phenomenological bounds.
- Move wave-speed equality to a principal-symbol condition.
- State when modal democracy, positivity, and PPN relations are assumptions.
- Do not use the internal gap as an external cutoff.

## `Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md`

**Disposition:** RECALCULATE / RECLASSIFY  
**Priority:** P0/P1

### Required changes

- Remove all \(5\,\mathrm{TeV}\)-dependent targets.
- Recompute geometry-to-coupling relations after corrected RGE inputs.
- Distinguish normalization calibration from prediction.

## `Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md`

**Disposition:** RECALCULATE / RECLASSIFY  
**Priority:** P0/P1

### Required changes

- Revalidate geometry independently of fitted coupling targets.
- Prove existence, integrality, positivity, and stability conditions.
- Do not use invalid upstream latents.

## `Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md`

**Disposition:** RECALCULATE / RECLASSIFY  
**Priority:** P0/P1

### Required changes

- Verify whether the normalization is genuinely independent.
- List all shared inputs with gauge and geometry sectors.
- Treat twistor matching as a conditional cross-check.

## `Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md`

**Disposition:** RECALCULATE / RECLASSIFY  
**Priority:** P0/P1

### Required changes

- Withdraw gravity, GW, and inflation conclusions tied to the invalid scale.
- Separate internal, Planck, Hubble, and external filter scales.
- Recompute only from a validated action and cosmological solution.

## `Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md`

**Disposition:** RECALCULATE / RECLASSIFY  
**Priority:** P0/P1

### Required changes

- Determine whether the weak-angle relation is input, symmetry assumption, calibration, or held-out test.
- Avoid double counting correlated gauge data.
- Publish covariance and sensitivity to scale/threshold choices.

# Group 19 — Projection-first reframing essays

## `A_Projection_First_Reframing_of_Physics.md`

**Disposition:** INTERPRETIVE; REVISE CLAIMS  
**Priority:** P2

### Required changes

- Keep as a conceptual overview.
- Use only corrected descent/recovery language.
- Do not state theorem-level inevitability beyond the formal core.

## `A_Projection_First_Reframing_of_Information__Computation__and_Undecidability (1).md`

**Disposition:** INTERPRETIVE; REVISE CLAIMS  
**Priority:** P2

### Required changes

- Make undecidability conditional on explicit computational embedding.
- Do not infer complexity or irreducibility from memory alone.
- Keep information-language claims interpretive.

## `A_Projection_First_Reframing_of_Quantum_Gravity.md`

**Disposition:** INTERPRETIVE; REVISE CLAIMS  
**Priority:** P2

### Required changes

- Remove claims relying on completed constructive QG, external Gaussian UV completion, or global quantum-gravity closure.
- Present local admissible QG sectors as a research program.

## `A_Projection_First_Reframing_of_String_Theory (1).md`

**Disposition:** INTERPRETIVE; REVISE CLAIMS  
**Priority:** P2

### Required changes

- Present strings and branes as possible encodings, not necessary consequences.
- State the worldsheet and consistency assumptions.
- Keep as interpretation.

## `A_Projection_First_Reframing_of_Dark_Matter_and_Dark_Energy (1).md`

**Disposition:** INTERPRETIVE; REVISE CLAIMS  
**Priority:** P2

### Required changes

- Do not infer cold, collisionless behavior or cosmic acceleration from missing encodings.
- Supply a covariant stress tensor/field equation before physical claims.
- Label as a dark-sector hypothesis and diagnostic reframing.


# Part VII — Cross-corpus issues that must be propagated everywhere

## 1. Bell terminology

Allowed package:

\[
\text{upper-local equations}
+
\text{microcausality}
+
\text{no-signaling}
+
\text{nonfactorizing global states}.
\]

Forbidden conjunction:

\[
\text{measurement independence}
+
\text{complete deterministic beables}
+
\text{Bell conditional factorization}
+
\text{quantum CHSH violation}.
\]

Use “Bell-nonfactorizing but microcausal,” not “Bell-local hidden variables.”

## 2. Probability terminology

Replace:

> noninjective projection generates probabilities

with:

> noninjective projection creates unresolved fibers; a preparation or invariant measure and a reduction theorem generate effective probabilities.

## 3. Horizon and island terminology

Replace:

> no global right inverse; islands are partial right inverses

with:

> exterior data do not furnish an exact decoder for the full state; islands/code subspaces may support restricted recovery channels for selected observables.

## 4. EFT terminology

Replace:

> RG flow has no right inverse

with:

> Wilsonian coarse-graining is many-to-one and lacks a unique UV decoder; the beta-function ODE may remain locally invertible where its vector field is regular.

## 5. Quantum-graph terminology

Replace:

> Feynman diagrams derive quantization

with:

> quadratic-plus-interaction expansions generate graph combinatorics; quantum interpretation requires a quantum algebra and state.

## 6. Capacity terminology

Do not use one scalar interchangeably as:

- distance to failure;
- conserved resource;
- force potential;
- entropy;
- probability;
- flux.

Each use needs a normalization and a separate constitutive theorem.

## 7. “No global algebra”

Replace blanket statements with:

> no preferred globally admissible chart, state, section, or faithful representation exists.

An abstract quasilocal algebra or categorical colimit may still exist.

---

# Part VIII — Codex implementation workflow

## Phase 1 — Add authoritative convention files

Create:

1. `MTT_MATHEMATICAL_CONVENTIONS.md`
2. `MTT_ERRATA_AND_DEPENDENCY_REGISTER.md`
3. `MTT_CLAIM_STATUS_LEDGER.md`
4. `MTT_NUMERICAL_PROVENANCE_STANDARD.md`

Do this before editing downstream papers.

## Phase 2 — Patch the spine

Edit in this order:

1. Foundation
2. FP I
3. FP II
4. FP III
5. FP IV
6. FP V
7. FP VI
8. Projection–Admissibility
9. A0
10. Corpus Index

Do not update downstream claims until the definitions above are stable.

## Phase 3 — Patch locality and reduction

Edit:

- AQFT;
- QFT;
- Bell/entanglement;
- measurement;
- black holes;
- EFT;
- coherent kinematics.

## Phase 4 — Patch probability

Edit:

- FP III homogenization wording;
- indivisible stochastic process;
- QM reconstruction;
- Born/classical-limit paper;
- measurement probabilities;
- inflation/Born bridge.

## Phase 5 — Patch gravity and QG

Edit:

- signature;
- GR;
- GR–string bridges;
- QG/SPT;
- constructive QG;
- asymptotic-safety bridges;
- gravity-related delta/filter papers.

## Phase 6 — Patch matter, topology, and realizations

Edit:

- topology/SM;
- photons/central circle;
- proto-spinor;
- unified action;
- strings/flux;
- LQG/NCG/KK.

## Phase 7 — Rebuild numerics

Only after all upstream changes:

- rebuild RGEs;
- regenerate latent parameters;
- revalidate geometry;
- rerun flavor/Higgs/cosmology;
- produce held-out tests.

## Phase 8 — Rebuild the index

Regenerate all group summaries and statuses from the revised papers.

---

# Part IX — Codex search patterns

Search the repository for these strings and inspect every match:

```text
right inverse
global right inverse
no right inverse
partial right inverse
P \circ \Phi
effective evolution is defined by
4+3+3+3
Y_4 \times B_1 \times B_2 \times B_3
S^1_{\mathrm{cen}} \times T
spectral gap functions as a cutoff
effective cutoff scale
minimum length
e^{-\tau k^2}
Stieltjes
Källén
all-loop finite
at least one graviton
Gaussian process
Borell
A\Sigma+\Sigma A
\|A^{-1}\| \le 1/
unique Higgs
mass equals
\nabla s \neq 0
most general action
5 TeV
4.2 TeV
cross-prediction
exact hypercharge
c_1=0
covariantly constant
K3
family number
no global algebra
non-joint representability
indivisible
infinite memory
time-energy
```

---

# Part X — Validation tests

## 1. Geometry tests

- Every physical ten-dimensional realization satisfies \(4+6=10\).
- No coordinate factor is counted twice.
- Every first Chern representative is closed and integral.
- Every central phase circle is clearly a coordinate, quotient, or bundle—not ambiguous.
- Every `3 x 3` count is typed as components of
  `Hom(TP,TI)`, never as multiplication of manifold dimensions.
- Every use of `1+3 x 3=4+6` says whether it is a component identity or a
  separately proved tangent-bundle decomposition.
- Every identification of the local `1+2+3` strain split with the q79
  `1+2+3` trace split supplies transition, metric, connection, and operator
  intertwining data.
- Every q79 spin claim distinguishes the local `Dic_3` lift, strict global
  Spin closure, and any conditional SpinC cancellation.
- Physical time is never identified with the compact shared phase circle
  without a noncompact lift and a physical-evolution theorem.

## 2. Map-typing tests

For every theorem, record:

- domain;
- codomain;
- whether the map is an endomorphism;
- whether the claimed inverse is left or right;
- whether a reduced map factors through the quotient.

## 3. Fixed-point tests

- A Banach theorem has a nonempty complete invariant domain.
- Approximate contraction is not called exact contraction.
- Multiple outcomes use separate invariant basins.
- A time-step fixed point is not called stationary without a Lyapunov or uniqueness argument.

## 4. Operator tests

- Unbounded operators have domains.
- Commutation is strong where spectral projectors are multiplied.
- Nonnormal estimates use semigroup/dissipativity constants.
- Lyapunov equations have the correct sign.

## 5. Locality tests

- Projection is fiberwise in the base.
- Compressed local observables preserve the coherent sector or pass through a conditional expectation.
- Spatially nonlocal kernels are not claimed to have strict finite propagation.

## 6. Probability tests

- Every probability has a measure or state.
- Every Born claim identifies the basin–trace equality.
- Classical path probabilities are not called quantum solely through dilation.

## 7. QG tests

- Internal damping is not external-momentum damping.
- Positive spectral representation is not combined with exact external Gaussian asymptotics.
- Every loop direction and subgraph is accounted for.
- Scattering unitarity includes range equality/asymptotic completeness.
- Physical graviton masslessness and soft sectors are addressed.

## 8. Numerical tests

- RGE code reproduces standard SM running.
- Units and hypercharge normalization are tested.
- Matching scales are not chosen using held-out observables.
- Round-trip checks are not labeled predictions.
- Every result includes uncertainty and provenance.

---

# Part XI — Recommended revised titles

| Current title/claim | Recommended replacement |
|---|---|
| Projection–Admissibility Obstruction Theorem | Projection–Descent and Recovery Theorem |
| Closure and Inevitability | Conditional Closure Relations |
| Why Description Forces Circle, Lens, and Nil | Circle–Lens–Nil Obstruction Taxonomy |
| Signature Selection and Exclusion | Lorentzian Base Compatibility and Signature Stability |
| From MTT to General Relativity | Controlled Coherent Reduction to Four-Dimensional Einstein Gravity |
| Exact SM Hypercharges from Topology | Difference-Charge Encoding of Standard Model Hypercharges |
| Born Rule Derived | Born-Compatible Characterization of Basin Weights |
| UV-Finite, Unitary Quantum Gravity | SPT-Filtered Euclidean TT Model |
| Indivisible Stochastic Processes | Title naming the exact divisibility criterion |
| Dark Sector as Missing Encodings | A Projection-First Dark-Sector Hypothesis |
| The Proto-Spinor: Triadic Closure from Pointwise Internal Embedding | The Proto-Spinor: Conditional Spinorial Closure and the q79 Interface |
| World-in-World Genesis: A Proto-Geometric Origin of Time, Gravity, Matter, and Quantization | World-in-World Genesis: Local Comparison Geometry and a Globalization Program |
| Closure-Strain Geometry and the Structure of the Standard Model | Closure-Strain Geometry: Local Normal Forms and Conditional Matter Encodings |
| Most General Ten-Dimensional Action | Closure Geometry and a Regime-Local Ten-Dimensional Action Ansatz |

---

# Part XII — Final revised status of MTT

After these changes, the strongest defensible MTT core is:

\[
\boxed{
\text{a local upper-world framework for fiberwise spectral reduction, stable coherent sectors, controlled effective dynamics, and mathematically classified breakdown of descent and continuation}.
}
\]

In addition, successor calculation packets close embedded renormalized-SM
equivalence at the explicitly adopted one-shared-physical-primitive/profile
standard.  This is a stronger status than the original audit recorded, but it
is not strict no-knob selection and does not derive standard BRST quantization
from MTT.  Paper revisions must preserve both halves of that statement.

The following remain open research programs rather than completed consequences:

- unique circle–lens–nil exhaustiveness;
- unique ten-dimensional necessity;
- unique Lorentzian \(3+1\) selection;
- the basin–trace Born theorem;
- projection-only derivation of Einstein gravity;
- strict no-knob Standard Model, family, and observed-branch selection;
- the same-source world-in-world/strain-to-q79 bundle-and-connection
  intertwiner;
- the strict global q79 Spin obstruction calculation;
- a constructive interacting unitary quantum gravity;
- a canonical microscopic realization;
- a genuinely held-out quantitative prediction.

The corpus should become narrower in headline claims and stronger in theorem quality.

---

# Part XIII — Completion checklist

A revision is complete only when:

- [ ] the old right-inverse theorem has no remaining downstream citation;
- [ ] all physical geometry uses the canonical \(4+6\) convention;
- [ ] every `3 x 3` world-in-world claim is a typed comparison field, not
  manifold-dimension multiplication;
- [ ] q79 profile equivalence and strict no-knob selection are reported as
  different tiers;
- [ ] all FP source corrections are applied;
- [ ] locality descent is a named theorem;
- [ ] every probability statement has a measure/state;
- [ ] every reconstruction paper lists its imported assumptions;
- [ ] every numerical result has provenance and held-out status;
- [ ] the \(5\,\mathrm{TeV}\) chain is removed or independently corrected;
- [ ] the Iwasawa construction is removed or rebuilt;
- [ ] QG papers no longer combine incompatible positivity and external Gaussian claims;
- [ ] the index reflects actual theorem status;
- [ ] the corpus builds without broken references to withdrawn theorems;
- [ ] all renamed papers and theorem labels are propagated through citations and the index.
