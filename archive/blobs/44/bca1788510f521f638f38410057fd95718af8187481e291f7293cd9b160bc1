# QFT02 Equicausal and Formal State-Transport Assessment

Date: 2026-07-24

## Executive result

Two frontier changes are now implemented.

1. The active q79 gauge-fixed functional domain is corrected from an
   unrestricted microcausal algebra to the equicausal subcomplex.
2. Hadamard-seed, admissible renormalization-prescription and admissible
   gauge-fixing changes now transport the local formal physical algebra and
   state cone by specified formal isomorphisms.

Literal interacting local quasi-equivalence is not closed. It is now cut
sharply at the absent fixed-coupling C*/GNS/von-Neumann layer.

## 1. Primary-source correction

The historical v1 q79 theorem asserted that the usual microcausal class is
closed under the Peierls bracket and supports the standard time-slice
homotopy.

Hawkins, Rejzner and Visser prove that:

- the Peierls bracket of regular functionals can fail to be smooth;
- unrestricted microcausal functionals are therefore not closed under the
  Peierls bracket in general;
- the microcausal multivector complex is not closed under the standard
  time-slice homotopy;
- the equicausal subclass contains local functionals and Wick polynomials,
  closes under the star product and Peierls bracket, and satisfies
  time-slice.

Their counterexample fixes a linear Green-hyperbolic operator. The q79
fixed-background/free-linearization hypothesis therefore does not evade it.

Primary source:

- https://arxiv.org/abs/2312.15203

## 2. What survives unchanged

The correction does not alter:

- A57 field-block consumption;
- the rational principal-symbol identities;
- Green hyperbolicity;
- existence of advanced and retarded propagators;
- free BRST nilpotency;
- the exact antighost/auxiliary contracting homotopy;
- local anomaly cancellation;
- the all-orders formal QME scheme;
- the exact quartet positivity witness;
- local formal positive state existence;
- the contravariant state-space functor;
- common-parent finite compatibility;
- the Bell obstruction to arbitrary state gluing.

Only the infinite-dimensional functional carrier and the claims derived
directly from its closure are replaced.

## 3. Equicausal successor

The successor theorem is:

`proof_corpus/q79_SM_GaugeFixed_Hyperbolic_BV_and_Equicausal_BRST_Algebra_Theorem_v2.md`.

The generated certificate is:

`certificates/q79_sm_gaugefixed_hyperbolic_bv_equicausal.certificate.json`.

It records 54 theorem-dependency, exact finite, domain and guardrail checks.
The active statements are:

- \(\mathcal F_{\rm ec}\) contains the local/Wick domain used by the
  interaction;
- the Peierls bracket closes on \(\mathcal F_{\rm ec}\);
- the compatible Hadamard star product closes on
  \(\mathcal F_{\rm ec}[[\hbar]]\);
- the equicausal multivector complex is stable under the time-slice
  homotopy;
- unrestricted \(\mathcal F_{\mu c}\) is retained only as an ambient
  wavefront class.

No extension of Epstein-Glaser time ordering to every equicausal functional
is claimed. The downstream interacting algebra is generated on the
local/multilocal Wick subalgebra, which is equicausal.

## 4. Formal presentation groupoid

The new state-transport theorem is:

`proof_corpus/q79_SM_Equicausal_Formal_State_Transport_and_Local_QuasiEquivalence_Cutset_Theorem_v1.md`.

The generated certificate is:

`certificates/q79_sm_equicausal_formal_state_transport.certificate.json`.

Its objects are admissible triples

\[
(H,T,\Psi)
\]

of Hadamard covariance, renormalized time-ordering prescription and
gauge-fixing fermion.

Its arrows are:

- normal-ordering isomorphisms for smooth Hadamard-covariance changes;
- Stueckelberg-Petermann maps between admissible prescriptions;
- formal BV-cohomology isomorphisms under admissible gauge-fixing changes.

These arrows transport normalized formal positive physical states and commute
with admissible local restriction.

## 5. Exact witnesses

### Hadamard seed

On polynomials of degree at most four, the certificate represents

\[
\beta_t=\exp\left(\frac t2\frac{d^2}{dx^2}\right)
\]

as an exact rational \(5\times5\) matrix. It verifies the identity, inverse
and additive cocycle, then checks star-product intertwining on all 15
degree-bounded monomial pairs.

### State transport

The rational orthogonal matrix

\[
U=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix}
\]

transports a positive trace-one density matrix by

\[
\rho'=U\rho U^T.
\]

The certificate checks the unital star-algebra identities on the full matrix
basis and exact equality of source/transported expectations and positive
squares.

These are finite exact witnesses of the transport identities. They do not
replace the cited infinite-dimensional pAQFT/BV theorems.

## 6. Local quasi-equivalence cutset

Presentation-isomorphic formal state cones are not the same statement as
local quasi-equivalence.

Literal local quasi-equivalence requires:

1. a fixed-coupling local C*-net;
2. a declared physical state class;
3. local GNS representations;
4. local von Neumann closures;
5. comparison of normal folia.

The current q79 interacting construction is a formal power-series algebra
with formal pre-Hilbert representations. It has none of items 1, 3 or 4 for
the full interacting SM gauge-BRST theory.

Buchholz and Fredenhagen provide a useful scalar dynamical C*-algebra
benchmark, but their construction does not supply the missing full q79 SM
completion:

- https://arxiv.org/abs/1902.06062

The correct current truth value is therefore:

`not_yet_well_typed_without_fixed_coupling_Cstar_von_Neumann_completion`.

This is sharper than leaving the phrase "local quasi-equivalence" as an
unstructured open item.

## 7. Affected historical documents

The following historical theorem documents contain microcausal terminology:

- `q79_SM_GaugeFixed_Hyperbolic_BV_and_Microcausal_BRST_Algebra_Theorem_v1.md`;
- `q79_SM_Renormalized_TimeOrdering_and_Local_QME_Anomaly_Cohomology_Theorem_v1.md`;
- `q79_SM_Local_Formal_BRST_Physical_State_and_Positivity_Theorem_v1.md`;
- `q79_SM_Local_Formal_Physical_State_Space_Compatibility_and_Gluing_Theorem_v1.md`.

Their finite calculations and later theorem applications remain current.
Whenever they rely on closure or time-slice of the unrestricted microcausal
class, the active reference is the equicausal v2 successor.

## 8. Parameter impact

No new physical continuous parameter, discrete selector, fit or measured
input is added.

\(H\), \(T\) and \(\Psi\) are presentation choices connected by the proved
formal arrows. The result removes presentation dependence; it does not
select a preferred presentation.

## 9. Verification

Canonical commands:

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```

Result:

- canonical verifier: `ok: true`;
- equicausal successor: 54/54 checks;
- formal state transport/cutset: 41/41 checks;
- unit suite: 34/34 tests passed.

The same command results are recorded in the durable MTT handoff and Git
checkpoint for this assessment.
