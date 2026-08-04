from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
QM_ROOT = Path(os.environ.get("MTT_QM_ROOT", TEXPAPERS / "mtt-qm-source-proof"))
PACKET = ROOT / "q79_operational_ontology_nonentailment_and_single_history_countermodel.packet.json"


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


def matrix(values: list[list[object]], locals_: dict[str, object] | None = None) -> sp.Matrix:
    local_values = locals_ or {}
    return sp.Matrix(
        [[sp.sympify(entry, locals=local_values) for entry in row] for row in values]
    )


def vector(values: list[object], locals_: dict[str, object] | None = None) -> sp.Matrix:
    local_values = locals_ or {}
    return sp.Matrix([sp.sympify(entry, locals=local_values) for entry in values])


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def verify_inputs(packet: dict) -> dict[str, dict]:
    roots = {
        "closure-dynamics": ROOT,
        "mtt-qm-source-proof": QM_ROOT,
    }
    sources: dict[str, dict] = {}
    for label, record in packet["inputs"].items():
        repository = record["repository"]
        require(repository in roots, f"repository: {label}")
        path = roots[repository] / record["relative_path"]
        require(path.is_file(), f"source exists: {label}")
        require(sha256(path) == record["sha256"], f"source hash: {label}")
        source = load(path)
        identity = source.get("schema") or source.get("certificate")
        require(identity == record["identity"], f"source identity: {label}")
        require(source["status"] == record["status"], f"source status: {label}")
        require(source_checks_pass(source), f"source checks: {label}")
        sources[label] = source
    require(len(sources) == 6, "six sources")
    return sources


def verify_single_history_countermodel(packet: dict, sources: dict[str, dict]) -> None:
    model = packet["single_history_countermodel"]
    counts = model["record_partition_cardinalities"]
    require(counts == {"ready": 1, "P": 149, "Q": 298}, "partition counts")
    require(sum(counts.values()) == 448, "partition total")
    probabilities = {
        label: sp.Rational(count, 448) for label, count in counts.items()
    }
    require(probabilities == {
        "ready": sp.Rational(1, 448),
        "P": sp.Rational(149, 448),
        "Q": sp.Rational(149, 224),
    }, "exact probabilities")
    require(
        model["pushforward_probabilities"]
        == {label: str(value) for label, value in probabilities.items()},
        "stored probabilities",
    )
    require(sum(probabilities.values()) == 1, "normalization")
    require(model["actual_record_count_per_atom"] == 1, "one history")
    require(model["source_tier"].endswith("NOT_SELECTED_PHYSICAL_MTT_DYNAMICS"), "source tier")

    fock = sources["canonical_q79_Fock_output_measure"]
    require(
        fock["exact_checkpoint"]["q79_ready_p_q_probabilities"]
        == ["1/448", "149/448", "149/224"],
        "bound Fock checkpoint",
    )
    operational = sources["projective_operational_record_descent"]
    require(
        operational["exact_q79_open_stratum_witness"]["ready_P_Q_checkpoint"]
        == ["1/448", "149/448", "149/224"],
        "bound projective checkpoint",
    )


def verify_unitary_reduct(packet: dict) -> None:
    locals_ = {"I": sp.I, "sqrt": sp.sqrt}
    witness = packet["unitary_record_witness"]
    e0 = vector(witness["reference_state"], locals_)
    state = vector(witness["record_amplitude"], locals_)
    dilation = matrix(witness["householder_dilation"], locals_)
    require(sp.simplify((state.H * state)[0]) == 1, "state norm")
    require(is_zero(dilation.H * dilation - sp.eye(3)), "dilation unitarity")
    require(is_zero(dilation * e0 - state), "dilation action")
    weights = [sp.simplify(abs(entry) ** 2) for entry in state]
    expected = [sp.Rational(1, 448), sp.Rational(149, 448), sp.Rational(149, 224)]
    require(weights == expected, "dilation probabilities")
    require(witness["output_weights"] == [str(value) for value in expected], "stored weights")


def verify_basis_guard(packet: dict, sources: dict[str, dict]) -> None:
    locals_ = {"I": sp.I, "sqrt": sp.sqrt}
    fourier_source = sources["selected_static_qutrit_Fourier"]
    f3 = matrix(
        fourier_source["exact_selected_qutrit_Fourier_witness"]["F3"], locals_
    )
    e0 = sp.Matrix([1, 0, 0])
    clock = e0
    fourier = sp.simplify(f3.H * e0)
    require(is_zero(f3.H * f3 - sp.eye(3)), "F3 unitary")
    clock_support = sum(sp.simplify(entry) != 0 for entry in clock)
    fourier_support = sum(sp.simplify(entry) != 0 for entry in fourier)
    require((clock_support, fourier_support) == (1, 3), "support mismatch")
    require(sp.simplify((fourier.H * fourier)[0]) == 1, "Fourier norm")
    stored = packet["basis_dependence_witness"]
    require(stored["clock_nonzero_support"] == 1, "stored clock support")
    require(stored["Fourier_nonzero_support"] == 3, "stored Fourier support")
    require("without a separately selected" in stored["excluded_rule"], "preferred-basis guard")
    require("does not refute" in stored["scope_guard"], "Everett scope guard")


def verify_logic_and_context(packet: dict, sources: dict[str, dict]) -> None:
    signature = packet["operational_signature"]
    require("ontic actualization predicate" in signature["does_not_contain"], "signature boundary")
    completions = packet["two_ontological_completions"]
    require(completions["same_operational_predictions"] is True, "same predictions")
    require(completions["different_predicate"] == "Actual_S differs from Actual_C", "different ontology")
    require(completions["logical_result"] == [
        "O_q79 does not entail coactual support",
        "O_q79 does not entail singleton actualization",
    ], "logical result")

    basin = sources["basin_frame_Born_reduction"]
    context = packet["contextuality_guard"]
    require(context["declared_context"] == ["ready", "P", "Q"], "declared context")
    require(
        context["imported_allowed_structure"]
        == basin["event_level_no_go"]["allowed_structure"],
        "allowed contextual structure",
    )
    require(
        context["imported_forbidden_strengthening"]
        == basin["event_level_no_go"]["forbidden_strengthening"],
        "forbidden valuation",
    )

    local_first = sources["local_first_Cech_Hilbert_descent"]
    nonlinear = sources["nonlinear_repair_descent"]
    require(
        local_first["claim_tiers"]["global_Hilbert_implies_many_actual_worlds"]
        == "CLOSED_NOGO_INFERENCE",
        "local-first no inference",
    )
    require(
        nonlinear["claim_tiers"]["unique_physical_actualization"] == "OPEN",
        "physical actualization open",
    )


def verify_packet_contract(packet: dict) -> None:
    require(
        packet["schema"]
        == "MTTQ79OperationalOntologyNonentailmentAndSingleHistoryCountermodel.v1",
        "schema",
    )
    require(all_boolean_leaves_true(packet["checks"]), "checks")
    require(all(value is False for value in packet["guardrails"].values()), "guardrails")
    tiers = packet["claim_tiers"]
    require(
        tiers["many_worlds_required_by_retained_q79_operational_math"]
        == "CLOSED_NOGO_INFERENCE",
        "non-entailment tier",
    )
    require(tiers["many_worlds_false"] == "NOT_CLAIMED", "non-disproof tier")
    require(tiers["MTT_physically_selects_single_history_completion"] == "OPEN", "selection tier")
    require(tiers["objective_actualization_dynamics"] == "OPEN", "actualization tier")
    require(
        packet["parameter_ledger"]
        == {
            "new_continuous_fit_parameters": 0,
            "new_discrete_fit_parameters": 0,
            "new_observed_probabilities": 0,
            "inherited_clock_anchors": 1,
            "inherited_categorical_apparatus_contexts": 1,
            "candidate_ontological_sample_variables_if_single_history_is_adopted": 1,
            "candidate_sample_variable_promoted_to_MTT_source": False,
        },
        "parameter ledger",
    )
    require(
        packet["frontier_delta"]["next_theorem"]
        == "mttSelectedPhysicalRepairBasinToRecorderInstrumentAndOntologyDeclaration.v1",
        "next theorem",
    )


def main() -> None:
    packet = load(PACKET)
    sources = verify_inputs(packet)
    verify_single_history_countermodel(packet, sources)
    verify_unitary_reduct(packet)
    verify_basis_guard(packet, sources)
    verify_logic_and_context(packet, sources)
    verify_packet_contract(packet)
    print("Q79_OPERATIONAL_ONTOLOGY_NONENTAILMENT_AND_SINGLE_HISTORY_COUNTERMODEL_VERIFY_PASS")


if __name__ == "__main__":
    main()
