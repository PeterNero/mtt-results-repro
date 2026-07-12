"""Audit the q79 Route-C primitive-source counterexample and Weyl-pair gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analyze_q79_routec_basis_transport_primitive_source_theorem.py"
CERT = ROOT / "certificates" / "q79_routec_basis_transport_primitive_source_theorem_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_routec_basis_transport_primitive_source_theorem.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_routec_basis_transport_primitive_source_theorem"
    / "primitive_span_counterexample_table.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_RouteC_BasisTransport_Primitive_Source_Theorem_v1.md"

EXPECTED_STATUS = (
    "Q79_ROUTEC_BASISTRANSPORT_PRIMITIVE_COUNTEREXAMPLE_CLOSED_WEYLPAIR_GATE_BUILT_SOURCE_PROOF_OPEN"
)
EXPECTED_NEXT = "Q79_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1"

EXPECTED_ADJACENT_STATUSES = {
    "constants_phifin_trace_existence": "SELECTED_PHIFIN_FINITE_TRACE_EXISTENCE_PROVED_VALUES_OPEN",
    "constants_phifin_s1s2_value_emission": (
        "SELECTED_PHIFIN_S1S2_VALUE_EMISSION_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_VALUES"
    ),
    "gr_basis_transport_reduction": "ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN",
    "gr_weylpair_source_gate_import": "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN",
    "sm_basis_transport_counterexample": (
        "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_COUNTEREXAMPLE_BUILT_PRIMITIVE_ONLY_SPAN_INSUFFICIENT"
    ),
    "sm_weylpair_source_gate": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN"
    ),
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def close_to(value: float, expected: float, tol: float = 1.0e-12) -> bool:
    return math.isclose(float(value), expected, rel_tol=tol, abs_tol=tol)


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    failures: list[str] = []
    require(proc.returncode == 0, f"generator failed:\n{proc.stdout}", failures)

    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)

    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["primitive_span_counterexample"], "counterexample table mismatch", failures)
    require(cert["status"] == EXPECTED_STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure_claimed must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must be false", failures)

    adjacent = cert["adjacent_input_statuses"]
    for name, status in EXPECTED_ADJACENT_STATUSES.items():
        require(adjacent[name]["status"] == status, f"unexpected adjacent status for {name}", failures)

    require(all(cert["support_reductions"].values()), "not all support reductions are true", failures)

    primitive = cert["primitive_span_counterexample"]
    fixed = primitive["fixed_fiber_primitives"]
    envelope = primitive["fixed_plus_all_fiber_envelope"]
    require(primitive["target_dimension"] == 72, "primitive target dimension must be 72", failures)
    require(
        primitive["primitive_only_counterexample_proved"] is True,
        "primitive-only counterexample not proved",
        failures,
    )
    require(
        primitive["primitive_only_theorem_sufficient"] is False,
        "primitive-only theorem must be insufficient",
        failures,
    )
    require(fixed["target_in_span"] is False, "fixed-fiber target unexpectedly in span", failures)
    require(fixed["rank"] == 3, "fixed-fiber primitive rank must be 3", failures)
    require(
        float(fixed["relative_residual"]) > 0.7,
        "fixed-fiber residual too small for counterexample",
        failures,
    )
    require(
        envelope["target_in_span"] is False,
        "fixed-plus-envelope target unexpectedly in span",
        failures,
    )
    require(envelope["rank"] == 3, "fixed-plus-envelope rank must be 3", failures)
    require(
        float(envelope["relative_residual"]) > 0.7,
        "fixed-plus-envelope residual too small for counterexample",
        failures,
    )

    weyl = cert["weyl_pair_algebraic_gate"]
    require(weyl["target_dimension"] == 72, "Weyl-pair target dimension must be 72", failures)
    require(weyl["target_in_span"] is True, "Weyl-pair target must be in span", failures)
    require(weyl["rank"] == 2, "Weyl-pair rank must be 2", failures)
    require(float(weyl["residual_norm"]) < 1.0e-12, "Weyl-pair residual too large", failures)
    require(float(weyl["relative_residual"]) < 1.0e-12, "Weyl-pair relative residual too large", failures)
    require(weyl["exact_to_tolerance"] is True, "Weyl-pair exact-to-tolerance flag false", failures)
    require(weyl["phase_and_shift_packets_present"] is True, "phase/shift packets missing", failures)
    require(
        weyl["locked_splitter_reconstructed_by_weyl_pair"] is True,
        "locked splitter not reconstructed by Weyl pair",
        failures,
    )
    require(
        close_to(weyl["coefficients"][0], 1.0) and close_to(weyl["coefficients"][1], 1.0),
        "Weyl-pair coefficients must be 1,1",
        failures,
    )
    require(
        weyl["selected_source_provenance_proved"] is False,
        "source provenance must remain open",
        failures,
    )
    require(weyl["A_selected_emitted"] is False, "A_selected must remain unemitted", failures)
    require(weyl["b_selected_emitted"] is False, "b_selected must remain unemitted", failures)

    decision = cert["decision"]
    require(
        decision["original_target_closed_as_positive_source_theorem"] is False,
        "positive primitive theorem must not be claimed",
        failures,
    )
    require(
        decision["original_target_closed_as_counterexample_decision"] is True,
        "primitive counterexample decision must close",
        failures,
    )
    require(decision["refined_weyl_pair_theorem_required"] is True, "refined theorem not required", failures)
    require(decision["weyl_pair_algebraic_gate_built"] is True, "Weyl-pair gate not built", failures)
    require(
        decision["selected_weyl_pair_source_provenance_proved"] is False,
        "source provenance overclaimed",
        failures,
    )
    require(decision["A_selected_emitted"] is False, "A_selected overclaimed", failures)
    require(decision["b_selected_emitted"] is False, "b_selected overclaimed", failures)
    require(decision["target_fitting_used"] is False, "target fitting overclaimed", failures)

    closed = cert["closed_by_this_attempt"]
    for key in (
        "primitive_only_span_counterexample_closed",
        "s1s2_value_emission_criterion_imported",
        "weyl_pair_algebraic_gate_imported",
        "locked_splitter_reconstructed_by_weyl_pair",
        "source_contract_for_A_selected_imported",
        "next_target_advanced_to_Aselected_assembly",
        "target_fitting_excluded",
    ):
        require(closed[key] is True, f"closed flag false: {key}", failures)

    still_open = cert["still_open"]
    for key in (
        "prove_selected_phase_like_qutrit_Z_or_basis_holonomy_source",
        "prove_selected_shift_like_qutrit_X_vertex_source",
        "assemble_theorem_derived_A_selected",
        "emit_theorem_derived_b_selected",
        "solve_or_reject_splitter_equation",
        "selected_PhiFin_alpha1_payload_values",
        "full_SM_or_no_knob_closure",
    ):
        require(still_open[key] is True, f"open flag missing: {key}", failures)

    require(all(value is False for value in cert["guardrails"].values()), "guardrail false-map violated", failures)
    require(cert["theorem"]["proved"] is True, "theorem flag must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "theorem is **not** proved",
        "Weyl-Pair Algebraic Gate",
        "phase-plus-shift packet",
        "Q79PrimitiveOnlySpanCounterexampleAndWeylPairTargetTheorem",
        EXPECTED_NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 Route-C primitive-source theorem audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 Route-C primitive-source theorem audit PASS")
    print(f"status: {cert['status']}")
    print(
        "primitive residuals: "
        f"fixed={fixed['relative_residual']}, envelope={envelope['relative_residual']}"
    )
    print(
        "Weyl-pair residuals: "
        f"residual={weyl['residual_norm']}, relative={weyl['relative_residual']}"
    )
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
