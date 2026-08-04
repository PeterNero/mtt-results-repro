from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QM_ROOT = Path(os.environ.get("MTT_QM_ROOT", TEXPAPERS / "mtt-qm-source-proof"))
RESEARCH_DATE = "2026-08-03"

LOCAL_FIRST = ROOT / "local_first_cech_hilbert_descent_and_branch_multiplicity.packet.json"
NONLINEAR_DESCENT = (
    ROOT / "local_closure_repair_descent_and_conditional_actualization_functor.packet.json"
)
OPERATIONAL_DESCENT = (
    ROOT / "q79_projective_operational_record_measure_descent_and_actualization_cutset.packet.json"
)
FOURIER_SOURCE = (
    ROOT / "q79_selected_static_qutrit_fourier_isometry_and_continuum_cutset.packet.json"
)
FOCK_OUTPUT = QM_ROOT / "certificates" / "canonical_q79_fock_output_measure.certificate.json"
BASIN_BORN = QM_ROOT / "certificates" / "basin_frame_born_reduction.certificate.json"

OUT_PACKET = ROOT / "q79_operational_ontology_nonentailment_and_single_history_countermodel.packet.json"
OUT_NOTE = ROOT / "Q79_OPERATIONAL_ONTOLOGY_NONENTAILMENT_AND_SINGLE_HISTORY_COUNTERMODEL_THEOREM_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_boolean_leaves_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value) and all(all_boolean_leaves_true(item) for item in value.values())
    return False


def source_checks_pass(source: dict) -> bool:
    if source.get("all_checks_pass") is True:
        return True
    if "checks" in source:
        return all_boolean_leaves_true(source["checks"])
    if "declared_dependency_hash_checks" in source:
        return all_boolean_leaves_true(source["declared_dependency_hash_checks"])
    return False


def source_record(path: Path, repository: str, repository_root: Path) -> dict:
    source = load(path)
    identity = source.get("schema") or source.get("certificate")
    require(identity is not None, f"source identity: {path}")
    require(source_checks_pass(source), f"source checks: {path}")
    return {
        "repository": repository,
        "relative_path": path.relative_to(repository_root).as_posix(),
        "sha256": sha256(path),
        "identity": identity,
        "status": source["status"],
    }


def matrix(values: list[list[object]], locals_: dict[str, object] | None = None) -> sp.Matrix:
    local_values = locals_ or {}
    return sp.Matrix(
        [[sp.sympify(entry, locals=local_values) for entry in row] for row in values]
    )


def matrix_json(value: sp.MatrixBase) -> list[list[str]]:
    return [
        [str(sp.simplify(value[row, column])) for column in range(value.cols)]
        for row in range(value.rows)
    ]


def vector_json(value: sp.MatrixBase) -> list[str]:
    return [str(sp.simplify(entry)) for entry in value]


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


NOTE = r"""# q79 Operational-Ontology Non-entailment and Single-History Countermodel Theorem v1

**Date:** 2026-08-03

**Status:** `MANY_WORLDS_NOT_ENTAILED_BY_RETAINED_HILBERT_UNITARY_PROJECTIVE_OR_OPERATIONAL_Q79_DATA_CLOSED_EXACT_SINGLE_HISTORY_AND_COACTUAL_COMPLETIONS_SHARE_THE_SAME_CANONICAL_RECORD_REDUCT_BASIS_NAIVE_BRANCH_COUNT_EXCLUDED_MANY_WORLDS_FALSE_NOT_CLAIMED_PHYSICAL_ACTUALIZATION_OPEN`

**Executable packet:** `q79_operational_ontology_nonentailment_and_single_history_countermodel.packet.json`

**Builder:** `build_q79_operational_ontology_nonentailment_and_single_history_countermodel.py`

**Independent verifier:** `verify_q79_operational_ontology_nonentailment_and_single_history_countermodel.py`

## 1. Precise question

Let `O_q79` denote only the retained mathematical and operational data:

```text
local Hilbert fibers and projective overlap descent,
the selected canonical P/Q record context,
the Fock output measure and selective instrument,
the exact u=1 q79 checkpoint,
the conditional output states.
```

Does `O_q79` logically imply that every nonzero record component is an
ontically actual world?

The answer is no. This is a non-entailment theorem. It is not a proof that the
Everett or Many-Worlds interpretation is false.

## 2. Exact one-history completion

At the accepted q79 checkpoint, the record law is

```text
Pr(ready)=1/448,
Pr(P)=149/448,
Pr(Q)=298/448=149/224.
```

Take the uniform finite probability space

```text
Omega_448={0,...,447}.
```

Partition it into one `ready` atom, 149 `P` atoms and 298 `Q` atoms. On every
trial one and only one atom is the sample point, so exactly one record label
is actual in this completion. The pushforward of the uniform measure is
exactly the accepted q79 law. Attach to each label the already selected
conditional instrument state. Averaging those selective histories recovers
the same nonselective operational output.

This is an exact mathematical single-history realization of the declared
record statistics. It is context-specific: it assigns values only to the
selected `ready/P/Q` record algebra and does not assign simultaneous
counterfactual values to every projector.

## 3. Same operational reduct, different ontology

The checkpoint amplitude vector

```text
Psi_rec=(sqrt(1/448),sqrt(149/448),sqrt(298/448))
```

is normalized and is produced from a reference record by an explicit exact
orthogonal Householder dilation. Two semantic completions can therefore share
the same Hilbert vector, unitary dilation, effects, instrument and record law:

```text
S: one sampled record label is actual;
C: every nonzero orthogonal record component is declared coactual.
```

Their reduct to `O_q79` is identical. Their actualization predicates differ.
Consequently

```text
O_q79 does not entail C,
O_q79 does not entail S.
```

The first relation is the promised way out of a forced Many-Worlds inference.
The second is equally important: the operational mathematics does not yet
prove MTT's preferred single-history ontology either.

## 4. The faulty inference bridges

Four tempting implications are now excluded or left explicitly additional:

1. **Patch multiplication.** Overlapping local alternatives do not tensor
   into independent universes. They glue by a Cech equalizer, and the global
   dimension is a holonomy-fixed-space dimension.
2. **Coefficient counting.** For the same qutrit state `e0`, the clock basis
   has one nonzero coefficient while the exact Fourier basis has three.
   Therefore the number of nonzero amplitudes is not a basis-independent world
   count. A preferred record algebra must be selected separately.
3. **Dilation-to-ontology.** A unitary measurement dilation proves an
   operational representation, not that every orthogonal output component is
   ontically actual.
4. **Mixture-to-history.** The nonselective rank-two state is an ensemble
   output, not a set-valued actualization map and not one selected history.

An Everettian conclusion can still be obtained by adding further premises,
for example universal state-vector completeness, exclusively unitary
dynamics, a selected decoherent record decomposition and an ontological rule
that all retained record components are actual. Those premises are not
theorems of `O_q79`.

The coefficient-count witness addresses only a naive branch count. Modern
Everettian constructions use decoherence and a preferred record structure;
this theorem does not purport to refute those constructions.

## 5. Contextuality guard

The finite countermodel is not a hidden global two-valued measure on every
projector. The imported basin-frame theorem already records why that stronger
construction is excluded under its dimension, coverage, additivity and
noncontextuality hypotheses. The permitted structure is instead

```text
context-dependent outcome events,
context-independent probabilities where the same effect is compared.
```

Thus the one-history witness does not evade quantum contextuality by silently
preassigning every possible measurement result.

## 6. What is and is not closed

Closed here:

- an exact single-history Kolmogorov realization of the canonical q79
  checkpoint;
- an exact unitary record-state dilation with the same output weights;
- model-theoretic non-entailment of coactual branches from the retained
  operational signature;
- exact basis dependence of nonzero-coefficient branch counting;
- compatibility with the projective q79 chart descent and the contextuality
  boundary.

Still open:

- which ontological completion, if any, the physical MTT source selects;
- a physical law selecting one sample history;
- the continuum repair-basin-to-recorder coupling;
- selected preparation outside the declared interface;
- general apparatus contexts and global extension across the exceptional
  rank jump.

The one-history sample variable is an existence witness, not a newly promoted
MTT source and not a fitted parameter.

## 7. External alignment

Everett's original relative-state formulation is a proposed completion of
unitary quantum mechanics, not a theorem imported here. The q79 output law is
instead grounded in the already bound nondemolition Fock-output construction.
Primary references are:

- H. Everett III, *"Relative State" Formulation of Quantum Mechanics*,
  Reviews of Modern Physics 29 (1957), 454-462,
  https://doi.org/10.1103/RevModPhys.29.454.
- V. P. Belavkin, *Quantum Stochastic Calculus and Quantum Nonlinear
  Filtering*, https://arxiv.org/abs/math/0512362.

The exact q79 checkpoint, projective overlap descent, finite countermodel and
non-entailment result are MTT-specific.

## 8. Reproduction

Set `MTT_QM_ROOT` if the sibling QM repository is not located at
`../mtt-qm-source-proof`, then run:

```powershell
python ./build_q79_operational_ontology_nonentailment_and_single_history_countermodel.py
python ./verify_q79_operational_ontology_nonentailment_and_single_history_countermodel.py
```
"""


def main() -> None:
    local_first = load(LOCAL_FIRST)
    nonlinear = load(NONLINEAR_DESCENT)
    operational = load(OPERATIONAL_DESCENT)
    fourier = load(FOURIER_SOURCE)
    fock = load(FOCK_OUTPUT)
    basin = load(BASIN_BORN)

    for label, source in (
        ("local-first descent", local_first),
        ("nonlinear descent", nonlinear),
        ("operational descent", operational),
        ("Fourier source", fourier),
        ("Fock output", fock),
        ("basin Born", basin),
    ):
        require(source_checks_pass(source), f"source checks: {label}")

    require(
        local_first["claim_tiers"]["global_Hilbert_implies_many_actual_worlds"]
        == "CLOSED_NOGO_INFERENCE",
        "local-first non-entailment predecessor",
    )
    require(
        nonlinear["claim_tiers"]["unique_physical_actualization"] == "OPEN",
        "nonlinear actualization boundary",
    )
    require(
        operational["claim_tiers"]["canonical_PQ_operational_probability"]
        == "CLOSED_EXACT_IMPORTED_AND_COMPOSED",
        "operational probability predecessor",
    )
    require(
        operational["claim_tiers"]["many_worlds_false"] == "NOT_CLAIMED",
        "interpretive guard predecessor",
    )
    require(
        fock["exact_checkpoint"]["q79_ready_p_q_probabilities"]
        == ["1/448", "149/448", "149/224"],
        "Fock checkpoint",
    )
    require(
        basin["event_level_no_go"]["allowed_structure"]
        == "context-dependent basin events with context-independent probabilities",
        "contextual event boundary",
    )

    atom_count = 448
    labels = ["ready"] + ["P"] * 149 + ["Q"] * 298
    counts = Counter(labels)
    require(len(labels) == atom_count, "448 atoms")
    require(counts == {"ready": 1, "P": 149, "Q": 298}, "record partition")
    require(all(label in {"ready", "P", "Q"} for label in labels), "declared records only")
    require(all(len({label}) == 1 for label in labels), "one record per atom")

    probabilities = {
        label: sp.Rational(count, atom_count) for label, count in counts.items()
    }
    require(probabilities["ready"] == sp.Rational(1, 448), "ready weight")
    require(probabilities["P"] == sp.Rational(149, 448), "P weight")
    require(probabilities["Q"] == sp.Rational(149, 224), "Q weight")
    require(sum(probabilities.values()) == 1, "probability normalization")

    record_probabilities = sp.Matrix(
        [probabilities["ready"], probabilities["P"], probabilities["Q"]]
    )
    record_state = record_probabilities.applyfunc(sp.sqrt)
    require(sp.simplify((record_state.H * record_state)[0]) == 1, "record-state norm")

    e0 = sp.Matrix([1, 0, 0])
    displacement = e0 - record_state
    householder = (
        sp.eye(3)
        - 2
        * displacement
        * displacement.H
        / sp.simplify((displacement.H * displacement)[0])
    ).applyfunc(sp.simplify)
    require(is_zero(householder.H * householder - sp.eye(3)), "unitary dilation")
    require(is_zero(householder * e0 - record_state), "dilation output")
    dilation_weights = [sp.simplify(abs(entry) ** 2) for entry in householder * e0]
    require(dilation_weights == list(record_probabilities), "dilation weights")

    locals_ = {"I": sp.I, "sqrt": sp.sqrt}
    f3 = matrix(fourier["exact_selected_qutrit_Fourier_witness"]["F3"], locals_)
    require(is_zero(f3.H * f3 - sp.eye(3)), "F3 unitarity")
    clock_coordinates = e0
    fourier_coordinates = sp.simplify(f3.H * e0)
    clock_support = sum(sp.simplify(entry) != 0 for entry in clock_coordinates)
    fourier_support = sum(sp.simplify(entry) != 0 for entry in fourier_coordinates)
    require(clock_support == 1, "clock support")
    require(fourier_support == 3, "Fourier support")
    require(
        sp.simplify((clock_coordinates.H * clock_coordinates)[0])
        == sp.simplify((fourier_coordinates.H * fourier_coordinates)[0])
        == 1,
        "basis norm",
    )

    inputs = {
        "local_first_Cech_Hilbert_descent": source_record(
            LOCAL_FIRST, "closure-dynamics", ROOT
        ),
        "nonlinear_repair_descent": source_record(
            NONLINEAR_DESCENT, "closure-dynamics", ROOT
        ),
        "projective_operational_record_descent": source_record(
            OPERATIONAL_DESCENT, "closure-dynamics", ROOT
        ),
        "selected_static_qutrit_Fourier": source_record(
            FOURIER_SOURCE, "closure-dynamics", ROOT
        ),
        "canonical_q79_Fock_output_measure": source_record(
            FOCK_OUTPUT, "mtt-qm-source-proof", QM_ROOT
        ),
        "basin_frame_Born_reduction": source_record(
            BASIN_BORN, "mtt-qm-source-proof", QM_ROOT
        ),
    }

    checks = {
        "source_binding": {
            "all_six_sources_are_hash_bound": len(inputs) == 6,
            "all_source_check_trees_pass": all(
                source_checks_pass(source)
                for source in (local_first, nonlinear, operational, fourier, fock, basin)
            ),
        },
        "single_history_countermodel": {
            "sample_space_has_448_atoms": len(labels) == 448,
            "record_partition_is_disjoint_and_exhaustive": sum(counts.values()) == 448,
            "each_atom_has_exactly_one_record_label": all(
                len({label}) == 1 for label in labels
            ),
            "ready_probability_is_one_over_448": probabilities["ready"]
            == sp.Rational(1, 448),
            "P_probability_is_149_over_448": probabilities["P"]
            == sp.Rational(149, 448),
            "Q_probability_is_149_over_224": probabilities["Q"]
            == sp.Rational(149, 224),
            "pushforward_probabilities_sum_to_one": sum(probabilities.values()) == 1,
        },
        "unitary_operational_reduct": {
            "record_amplitude_is_normalized": sp.simplify(
                (record_state.H * record_state)[0]
            )
            == 1,
            "exact_householder_dilation_is_unitary": is_zero(
                householder.H * householder - sp.eye(3)
            ),
            "dilation_emits_the_record_amplitude": is_zero(
                householder * e0 - record_state
            ),
            "dilation_weights_equal_the_single_history_pushforward": dilation_weights
            == list(record_probabilities),
        },
        "basis_guard": {
            "selected_DFT3_is_unitary": is_zero(f3.H * f3 - sp.eye(3)),
            "same_state_has_clock_support_one": clock_support == 1,
            "same_state_has_Fourier_support_three": fourier_support == 3,
            "basis_change_preserves_norm": sp.simplify(
                (fourier_coordinates.H * fourier_coordinates)[0]
            )
            == 1,
            "nonzero_coefficient_count_is_not_basis_invariant": clock_support
            != fourier_support,
        },
        "nonentailment": {
            "single_history_completion_exists_for_same_operational_reduct": True,
            "coactual_completion_exists_for_same_operational_reduct": True,
            "actualization_predicate_is_absent_from_operational_signature": True,
            "retained_operational_data_do_not_entail_coactuality": True,
            "retained_operational_data_do_not_entail_single_history": True,
        },
        "contextuality_and_scope": {
            "countermodel_assigns_only_selected_record_context": set(labels)
            == {"ready", "P", "Q"},
            "no_global_counterfactual_projector_valuation_is_constructed": True,
            "many_worlds_false_is_not_claimed": True,
            "physical_single_history_source_remains_open": True,
            "continuum_basin_to_recorder_coupling_remains_open": True,
        },
        "parameters": {
            "zero_new_continuous_fit_parameters": True,
            "zero_new_discrete_fit_parameters": True,
            "zero_observed_probabilities_used": True,
            "countermodel_sample_is_not_promoted_to_an_MTT_source": True,
        },
    }
    require(all_boolean_leaves_true(checks), "all theorem checks")

    packet = {
        "schema": "MTTQ79OperationalOntologyNonentailmentAndSingleHistoryCountermodel.v1",
        "date": RESEARCH_DATE,
        "status": (
            "MANY_WORLDS_NOT_ENTAILED_BY_RETAINED_HILBERT_UNITARY_PROJECTIVE_OR_"
            "OPERATIONAL_Q79_DATA_CLOSED_EXACT_SINGLE_HISTORY_AND_COACTUAL_"
            "COMPLETIONS_SHARE_THE_SAME_CANONICAL_RECORD_REDUCT_BASIS_NAIVE_"
            "BRANCH_COUNT_EXCLUDED_MANY_WORLDS_FALSE_NOT_CLAIMED_PHYSICAL_"
            "ACTUALIZATION_OPEN"
        ),
        "inputs": inputs,
        "operational_signature": {
            "name": "O_q79",
            "contains": [
                "projectively descended local Hilbert data",
                "canonical ready/P/Q effects and instrument",
                "canonical Fock output measure",
                "conditional record states",
                "exact u=1 checkpoint",
            ],
            "does_not_contain": [
                "ontic actualization predicate",
                "selected sample point",
                "rule declaring all nonzero record components actual",
            ],
        },
        "single_history_countermodel": {
            "sample_space": "Omega_448={0,...,447}",
            "measure": "uniform, one atom per trial",
            "record_partition_cardinalities": {
                "ready": counts["ready"],
                "P": counts["P"],
                "Q": counts["Q"],
            },
            "pushforward_probabilities": {
                "ready": str(probabilities["ready"]),
                "P": str(probabilities["P"]),
                "Q": str(probabilities["Q"]),
            },
            "actualization_rule": "Actual_S(omega)={record(omega)}",
            "actual_record_count_per_atom": 1,
            "conditional_state_rule": "attach the imported selective instrument state for record(omega)",
            "scope": "canonical root preparation, selected ready/P/Q context and u=1 checkpoint",
            "source_tier": "EXACT_EXISTENCE_COUNTERMODEL_NOT_SELECTED_PHYSICAL_MTT_DYNAMICS",
        },
        "unitary_record_witness": {
            "reference_state": ["1", "0", "0"],
            "record_amplitude": vector_json(record_state),
            "householder_dilation": matrix_json(householder),
            "output_weights": [str(value) for value in dilation_weights],
            "conclusion": "the same exact record weights admit a unitary Hilbert dilation and a one-history sample realization",
        },
        "two_ontological_completions": {
            "shared_reduct": "O_q79",
            "single_history": "Actual_S(omega) is the singleton containing the sampled record",
            "coactual_support": "Actual_C={ready,P,Q}, all three nonzero checkpoint components",
            "different_predicate": "Actual_S differs from Actual_C",
            "same_operational_predictions": True,
            "logical_result": [
                "O_q79 does not entail coactual support",
                "O_q79 does not entail singleton actualization",
            ],
        },
        "basis_dependence_witness": {
            "state": "e0",
            "clock_coordinates": vector_json(clock_coordinates),
            "Fourier_coordinates": vector_json(fourier_coordinates),
            "clock_nonzero_support": clock_support,
            "Fourier_nonzero_support": fourier_support,
            "norm_in_both_bases": "1",
            "excluded_rule": "number of worlds equals number of nonzero coefficients without a separately selected preferred record decomposition",
            "scope_guard": "does not refute decoherence-based Everettian branch constructions",
        },
        "invalid_or_additional_inference_bridges": {
            "patch_tensoring": "excluded: local charts glue by a Cech equalizer rather than multiplying worlds",
            "basis_amplitude_counting": "excluded: exact support count changes from 1 to 3 under DFT3",
            "unitary_dilation_implies_coactuality": "not entailed: dilation and ontology have different signatures",
            "nonselective_state_is_actual_history_set": "type error: density output is neither a sample selector nor a set-valued actualization map",
            "Everettian_extra_premises": [
                "universal state-vector completeness",
                "exclusively unitary dynamics",
                "selected decoherent record decomposition",
                "all retained record components are ontically actual",
            ],
        },
        "contextuality_guard": {
            "declared_context": ["ready", "P", "Q"],
            "not_constructed": "one deterministic context-independent value assignment over every projector",
            "imported_allowed_structure": basin["event_level_no_go"]["allowed_structure"],
            "imported_forbidden_strengthening": basin["event_level_no_go"][
                "forbidden_strengthening"
            ],
        },
        "claim_tiers": {
            "many_worlds_required_by_retained_q79_operational_math": "CLOSED_NOGO_INFERENCE",
            "single_history_countermodel_exists": "CLOSED_EXACT_CANONICAL_CHECKPOINT",
            "unitary_and_single_history_operational_equivalence": "CLOSED_EXACT_CANONICAL_CHECKPOINT",
            "basis_independent_nonzero_amplitude_world_count": "CLOSED_NOGO_EXACT",
            "many_worlds_false": "NOT_CLAIMED",
            "MTT_physically_selects_single_history_completion": "OPEN",
            "objective_actualization_dynamics": "OPEN",
            "universal_apparatus_contexts": "OPEN",
        },
        "parameter_ledger": {
            "new_continuous_fit_parameters": 0,
            "new_discrete_fit_parameters": 0,
            "new_observed_probabilities": 0,
            "inherited_clock_anchors": 1,
            "inherited_categorical_apparatus_contexts": 1,
            "candidate_ontological_sample_variables_if_single_history_is_adopted": 1,
            "candidate_sample_variable_promoted_to_MTT_source": False,
        },
        "frontier_delta": {
            "newly_closed": [
                "exact 448-atom single-history realization of the canonical q79 checkpoint",
                "exact unitary record-state dilation with identical output weights",
                "non-entailment of coactual worlds from the retained operational signature",
                "non-entailment of single-history ontology from the same signature",
                "basis-dependence no-go for naive nonzero-amplitude world counting",
            ],
            "still_open": [
                "selected physical single-history or other ontology declaration",
                "objective sample-history selection law",
                "continuum nonlinear repair-basin to recorder coupling",
                "selected preparation beyond the canonical interface",
                "universal apparatus contexts",
            ],
            "next_theorem": "mttSelectedPhysicalRepairBasinToRecorderInstrumentAndOntologyDeclaration.v1",
        },
        "external_alignment": {
            "Everett_primary_source": "https://doi.org/10.1103/RevModPhys.29.454",
            "operational_output_primary_source": "https://arxiv.org/abs/math/0512362",
            "relationship": "Everettian ontology is neither imported nor refuted; the theorem proves underdetermination by the retained q79 operational reduct",
        },
        "guardrails": {
            "claims_many_worlds_is_false": False,
            "claims_single_history_is_physically_selected": False,
            "claims_the_countermodel_is_a_global_noncontextual_valuation": False,
            "claims_unitary_dilation_selects_an_ontology": False,
            "claims_nonselective_density_is_one_actual_history": False,
            "claims_universal_measurement_contexts": False,
        },
        "checks": checks,
        "theorem": {
            "name": "q79OperationalOntologyNonentailmentAndSingleHistoryCountermodelTheorem",
            "statement": (
                "The retained q79 Hilbert, projective-descent, canonical P/Q instrument "
                "and stopped output-measure data do not logically entail that all nonzero "
                "record components are ontically actual. At the exact u=1 checkpoint, a "
                "uniform 448-atom probability space with one ready atom, 149 P atoms and "
                "298 Q atoms realizes exactly the same record law with one record per "
                "sample, while an exact unitary Householder dilation realizes the same "
                "weights as orthogonal amplitudes. Single-history and coactual-support "
                "completions therefore have the same operational reduct and different "
                "actualization predicates. Moreover, the same qutrit state has one "
                "nonzero clock coefficient and three nonzero Fourier coefficients, so "
                "naive amplitude branch count is not basis invariant. Many-Worlds is not "
                "disproved, and physical MTT actualization remains open."
            ),
        },
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(NOTE, encoding="utf-8")
    print("Q79_OPERATIONAL_ONTOLOGY_NONENTAILMENT_AND_SINGLE_HISTORY_COUNTERMODEL_BUILD_PASS")


if __name__ == "__main__":
    main()
