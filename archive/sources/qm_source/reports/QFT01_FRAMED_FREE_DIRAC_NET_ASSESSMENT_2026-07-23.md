# B.QFT.01 Framed Free-Dirac Net Assessment

Date: 2026-07-23

## Verdict

`B.QFT.01` is complete at the **selected q79 framed free massless Dirac
even-observable-net tier**.

This is a narrower result than full QFT closure, but it is not merely a
support packet. On the already selected Lorentzian branch it constructs one
continuum local net with:

- a selected-category covariant Dirac/CAR functor;
- a functorially unique even observable subnet on the chosen spin category;
- graded locality and Einstein locality;
- the time-slice property;
- a nonempty positive Hadamard state space;
- an exact continuum component map for the finite q79 \(P/Q\) projectors.

The executable certificate passes 43 of 43 checks. Thirty-three checks are
exact finite-algebra identities over \(\mathbb Q(i)\); ten verify that every
theorem input and primary theorem dependency is registered and current.

## What changed

Before this packet, the repository had:

1. exact finite q79 quantum kinematics;
2. an exact Cauchy-slice finite-symbol model;
3. an exact canonical binary Fock recorder and output measure;
4. only conditional finite-domain QFT support from A18.

It did not have a continuum local field algebra on the selected Lorentzian
branch.

The new construction composes the selected q79 coframe with the finite
parallel carrier:

\[
(Y_4,e,F_{q79},\nabla^{q79})
\longmapsto
D_{q79}
\longmapsto
K(O)
\longmapsto
\operatorname{CAR}(K(O))
\longmapsto
\mathfrak A_{q79}^{\rm even}(O).
\]

This directly discharges the declared CAR, locality, covariance, time-slice,
positive-state, Hadamard and continuum-observable clauses at the free tier.

## Exact finite result

The certificate reconstructs a \(+---\) Dirac Clifford representation and
checks:

\[
\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}I_4,\qquad
\gamma_5^2=I_4,\qquad
\operatorname{rank}\frac{I\pm\gamma_5}{2}=2.
\]

Tensoring the spinor factor with the q79 rank-six carrier gives:

\[
\dim_{\mathbb C}=24,\qquad
\operatorname{rank}(I_4\otimes P)=8,\qquad
\operatorname{rank}(I_4\otimes Q)=16.
\]

Each chirality has rank 12 and splits as \(4+8\) across \(P/Q\). The
certificate also proves that both q79 projectors commute with every Clifford
matrix.

A two-mode Jordan-Wigner representation checks exact CAR:

\[
\{a_i,a_j\}=0,\qquad
\{a_i,a_j^*\}=\delta_{ij}I.
\]

The odd separated modes anticommute, while the even number observables
commute. This is the finite witness for graded field locality and observable
Einstein locality.

## Why the state is a space, not one vacuum

The physically correct output is the locally compatible set of positive
normalized Hadamard states. The 2025/2026 Fewster-Strohmaier theorem supplies
existence for formally self-adjoint definite-type Dirac operators; Sanders
and Sahlmann-Verch supply the local-covariance and microlocal properties.

The geometry does not select one preferred element of this set. A generic
locally covariant preferred vacuum is obstructed by the natural-state no-go.
The result is therefore stronger and more credible when it preserves the
state space rather than inventing a q79 vacuum.

## Spin-lift boundary

A chosen global coframe induces a spin lift, so the odd field algebra can be
constructed. The q79 Lorentzian certificate selects the coframe only up to
local Lorentz gauge, and globally nonliftable gauge changes can alter the odd
field representative.

On a fixed spin category, the even observable algebra removes the functorial
sign/cohomology ambiguity in constructing the Dirac field functor. Sanders'
theorem establishes this natural uniqueness. It does not establish
equivalence of inequivalent global spin structures. This is why the certified
object is explicitly tied to the chosen framed representative.

This result does not prove that the finite q79 SpinC determinant line is
identical to the continuum Lorentzian SpinC line. That same-shared-line
intertwiner remains open.

## Objective comparison

Relative to standard curved-spacetime QFT, the algebraic construction is not a
new replacement for CAR/AQFT. Its new MTT-specific content is the composition
with a previously selected q79 Lorentzian coframe and exact finite \(P/Q\)
carrier, including the zero-parameter component map and exact sector ranks.

Relative to the earlier MTT packets, the advance is substantial: the result
crosses from finite quantum mechanics and conditional QFT support to an
actual continuum free local observable net on the selected branch.

## Parameter count

- New continuous parameters: 0.
- New discrete numerical selectors: 0.
- Fits: 0.
- Observed values: 0.
- Inherited discrete inputs: `A_QG`, `A_causal`.

The massless restriction is a zero-order-free baseline tier. It is not a
prediction of zero fermion masses.

## Remaining frontier

The next theorem must add selected interactions without reopening this free
net:

1. source the mass/Yukawa and nonflat gauge terms on the same continuum
   bundle;
2. construct the corresponding perturbative interacting local net;
3. close BRST/BV/QME for gauge sectors;
4. prove compatibility with the already certified finite SM representation
   packet;
5. keep the Hadamard state-space and renormalization ambiguities explicit.

The immediate high-value target is therefore the same-source map

\[
(D_{q79},\,\mathcal A_F,\,D_F,\,A_\mu,\,\Phi)
\longmapsto
\mathfrak A_{q79,\mathrm{int}}(O),
\]

with its gauge, microlocal and renormalization certificates. Reconstructing
the free CAR net again would be a loop.
