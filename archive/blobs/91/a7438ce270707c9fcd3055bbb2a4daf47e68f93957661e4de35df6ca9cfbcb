"""Audit Route-C Weyl-pair conditional A solve import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_weylpair_conditional_a_solve_import.candidate.json"
CERT = ROOT / "certificates" / "routec_weylpair_conditional_a_solve_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Conditional_A_Solve_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_weylpair_conditional_a_solve.py"

STATUS = "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_IMPORTED_SOURCE_PROVENANCE_OPEN"
NEXT = "Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem"]["proved"] is True, "certificate theorem not proved")
    require(all(data["checks"].values()), "not all import checks passed")

    counter = data["primitive_only_counterexample"]
    require(counter["source_attempt"]["counterexample_proved"] is True, "primitive counterexample missing")
    require(counter["source_attempt"]["selected_source_emission_proved"] is False, "primitive-only source overproved")
    require(counter["span_tests"]["fixed_fiber_primitives"]["target_in_span"] is False, "fixed primitives span target")
    require(counter["span_tests"]["fixed_plus_all_fiber_envelope"]["target_in_span"] is False, "envelope spans target")

    gate = data["weylpair_source_gate"]
    require(gate["span_test"]["target_in_span"] is True, "Weyl-pair gate does not span target")
    require(gate["span_test"]["rank"] == 2, "Weyl-pair rank mismatch")
    require(gate["span_test"]["relative_residual"] < 1e-12, "Weyl-pair residual too large")
    require(gate["source_contract"]["operator_emission_status_imported"]["A_selected_currently_emitted"] is False, "A_selected overemitted at gate")
    require(gate["source_contract"]["operator_emission_status_imported"]["b_selected_currently_emitted"] is False, "b_selected overemitted at gate")

    solve = data["conditional_solve_summary"]
    require(solve["operator_shape"] == [72, 2], "conditional operator shape mismatch")
    require(solve["operator_is_A_selected"] is False, "conditional operator promoted to A_selected")
    require(solve["columns"] == ["phase_packet", "shift_packet"], "conditional columns mismatch")
    require(solve["rank"] == 2, "conditional rank mismatch")
    require(solve["relative_residual"] < 1e-12, "conditional residual too large")
    require(solve["deltaTheta_conditional"] == [1.0, 1.0000000000000002], "conditional deltaTheta mismatch")
    require(solve["exact_to_tolerance"] is True, "conditional solve not exact to tolerance")

    q79 = data["q79_conditional_assembly"]
    require(q79["decision"]["conditional_A_weylpair_assembled"] is True, "q79 conditional A not assembled")
    require(q79["decision"]["conditional_deltaTheta_solve_exact"] is True, "q79 conditional solve not exact")
    require(q79["decision"]["conditional_A_promoted_to_A_selected"] is False, "q79 conditional A overpromoted")
    require(q79["decision"]["A_selected_emitted"] is False, "q79 A_selected overemitted")
    require(q79["decision"]["b_selected_emitted"] is False, "q79 b_selected overemitted")
    require(q79["conditional_solve"]["provenance_reduction"]["status"] == "NEXT_LEMMA_REQUIRED", "provenance reduction missing")

    require(len(data["source_provenance_obligations"]) == 4, "source-provenance obligation count mismatch")
    closes = data["what_closes_now"]
    for key in [
        "primitive_only_span_counterexample_imported",
        "weylpair_packet_algebraically_sufficient",
        "conditional_A_weylpair_assembled",
        "conditional_deltaTheta_solve_exact",
        "rank_and_consistency_obstruction_removed",
        "remaining_gap_reduced_to_source_provenance",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "prove_selected_weylpair_source_provenance",
        "promote_conditional_A_to_A_selected",
        "emit_theorem_derived_b_selected",
        "run_honest_selected_deltaTheta_C1_solve",
        "full_SM_or_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "conditional_A_is_A_selected",
        "A_selected_emitted",
        "b_selected_emitted",
        "selected_source_provenance_proved",
        "honest_selected_deltaTheta_solve_run",
        "observed_flavor_data_used",
        "benchmark_flavor_entries_used",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Primitive-only basis transport is now a counterexample branch" in note, "note missing counterexample")
    require("not promoted to `A_selected`" in note, "note missing A_selected guard")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
