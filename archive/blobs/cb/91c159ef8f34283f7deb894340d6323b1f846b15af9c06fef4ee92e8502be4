# QFT02 Local Formal State-Space Gluing Assessment

Date: 2026-07-24

## Decision

The local-state compatibility clause is closed at the correct mathematical
tier.

The local formal physical state families constructed at the preceding
checkpoint are not merely unrelated nonempty sets. On the declared
`q79Chart_0` category they form a nonempty contravariant state-space functor:

```text
psi: O -> O'
alpha_psi: A_phys(O) -> A_phys(O')
alpha_psi^*(omega') = omega' composed with alpha_psi
```

The pullback preserves normalization, formal positivity, continuity,
Hadamard/microlocal admissibility and ghost-number-zero quantum BRST
cohomology. Composition is exact.

## What glues

If finitely many admissible regions have one admissible common parent, choose
one formal positive physical state on the parent and restrict it. The
resulting local states agree on every retained overlap by functoriality.

The executable witness uses an exact rational GHZ density matrix on `ABC`.
The two routes

```text
ABC -> AB -> B
ABC -> BC -> B
```

both equal direct restriction `ABC -> B` and emit `I2/2`.

## What cannot be demanded

Arbitrary independently selected quantum states do not form a sheaf.

The exact counterexample chooses Bell states on `AB` and `BC`. Both restrict
to `I2/2` on `B`, but no positive `ABC` state has both marginals. Purity of
the `AB` marginal would force factorization across `AB|C`, making the `BC`
expectation of `X tensor X` equal to zero; the requested Bell `BC` state has
expectation one.

This is a theorem boundary, not a missing numerical calculation.

## Frontier change

Closed:

- `B.QFT.02_local_formal_state_space_functor`;
- `B.QFT.02_common_parent_finite_compatible_family`;
- the exact classification of arbitrary overlap-state gluing as impossible
  in general.

Still open:

- one selected global q79 state;
- interacting local quasi-equivalence;
- a fixed-coupling Hilbert completion;
- numerical RG, matching, uncertainties and physical observables;
- infrared and nonperturbative completion;
- the upper MTT action and state-selection theorem.

No physical parameter, selector, fit or observed value was added.

## Relation to established QFT

The construction follows the Brunetti-Fredenhagen-Verch distinction between
a covariant observable-algebra functor and a contravariant state-space
functor. Hollands-Ruan supports the perturbative continuity and Hadamard
state-space criterion, while its scalar scope is not promoted to a full
gauge-theory local-quasi-equivalence theorem. Hollands and
Duetsch-Fredenhagen supply the gauge-BRST positivity/deformation ingredients
already used by the prior q79 theorem.

The Fewster-Verch natural-state no-go explains why a state-space functor is
the correct generally covariant output and why it must not be relabeled as a
preferred vacuum.

## Artifacts

- theorem:
  `proof_corpus/q79_SM_Local_Formal_Physical_State_Space_Compatibility_and_Gluing_Theorem_v1.md`
- certificate:
  `certificates/q79_sm_local_formal_state_space_gluing.certificate.json`
- generator:
  `mtt_qm_source/build.py`
- canonical verifier:
  `scripts/verify.py`
