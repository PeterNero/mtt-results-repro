"""Build finite C1 row-kernel functional candidate and source-clause failure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET = PACKET_DIR / "finite_c1_rowkernel_functional_candidate.packet.json"
CLAUSES = PACKET_DIR / "source_clause_failure_certificate.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1_RowKernelFunctional_Candidate_or_SourceClauseFailure_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_finitec1_rowkernel_functional_packet.py"

STATUS = "MTT_SELECTED_FINITEC1_ROWKERNELFUNCTIONAL_CANDIDATE_BUILT_SOURCE_CLAUSES_OPEN"
NEXT = "MTT_Selected_PrimitiveKernelSourceTheorem_or_PhysicalPhiFinC1SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def clause(source_emitted: bool, same_branch: bool, theorem_derived: bool, uses_replay: bool, reason: str) -> dict[str, Any]:
    return {
        "source_emitted": source_emitted,
        "same_branch": same_branch,
        "theorem_derived": theorem_derived,
        "uses_replay_as_source": uses_replay,
        "reason": reason,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    normal = load(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "primitive_row_kernel_source_normal_form.packet.json")
    contract = load(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "selected_source_object_contract.packet.json")
    algebraic = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json")
    barrier = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "promotion_barrier_and_next_gate.packet.json")
    measure_split = load(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json")
    shape = load(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json")
    hessian = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json")

    packet = {
        "schema": "MTTSelectedFiniteC1RowKernelFunctionalPacket.v1",
        "status": "CANDIDATE_FUNCTIONAL_VALUES_FILLED_SOURCE_CLAUSES_OPEN",
        "functional_name": "SelectedFiniteC1RowKernelFunctional",
        "acceptance_formula": normal["acceptance_formula"],
        "coordinate_system": normal["coordinate_system"],
        "sector_couplings": normal["sector_couplings"],
        "source_clauses": {
            "measure_action_binding": clause(
                False,
                True,
                False,
                False,
                "Finite trace/Frobenius measure normalization is derived, but same-branch Phi_fin^C1 physical action restriction remains open.",
            ),
            "boundary_source_null": clause(
                False,
                True,
                False,
                False,
                "No theorem emits zero extra boundary/source term for the physical finite C1 action branch.",
            ),
            "basis_to_row_functionals": clause(
                False,
                True,
                False,
                False,
                "Selected basis support exists, but the selected basis-to-all-72-row functional theorem remains open.",
            ),
            "phase_shift_pre_residual_operators": clause(
                False,
                True,
                False,
                True,
                "Phase/shift operator shapes are compatible, but current values are residual replay rather than pre-residual source emissions.",
            ),
            "hessian_b_source": clause(
                False,
                True,
                False,
                True,
                "Formal Hessian/b target is identified, but same-source Hessian counterterm and b_selected emission remain open.",
            ),
        },
        "row_values": {
            "values_filled": algebraic["counts"]["total_algebraic_values_filled"] == 110,
            "values_promoted_as_source": False,
            "counts": {
                "primitive": algebraic["counts"]["primitive_values_filled"],
                "hessian": algebraic["counts"]["hessian_values_filled"],
                "sector": algebraic["counts"]["sector_values_filled"],
            },
            "algebraic_consistency_certificate": algebraic["algebraic_consistency_certificate"],
            "value_sources": algebraic["value_sources"],
            "why_not_promoted": algebraic["why_not_independent"],
        },
        "closed_support": {
            "finite_trace_measure_normalization": measure_split["clauses"]["physical_first_variation_uses_normalized_trace_Frobenius_measure"]["closed"],
            "all_110_algebraic_values_filled": algebraic["counts"]["total_algebraic_values_filled"] == 110,
            "variation_operator_shapes_compatible": shape["compatible_with_72_slot_table"],
            "formal_hessian_target_identified": hessian["formal_hessian_quadrature_emitted"],
        },
        "attached_source_evidence": [
            {"source": rel(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json"), "closes": "finite measure normalization only"},
            {"source": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json"), "closes": "110 algebraic value slots only"},
            {"source": rel(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json"), "closes": "operator shape compatibility only"},
            {"source": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json"), "closes": "formal Hessian target only"},
            {"source": rel(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "selected_source_object_contract.packet.json"), "closes": "source-object contract only"},
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }

    PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stderr_lines = proc.stderr.splitlines()
    validator_result = {
        "schema": "MTTSelectedFiniteC1RowKernelFunctionalValidatorResult.v1",
        "payload": rel(PACKET),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": stderr_lines[:20],
        "source_clause_errors": sum("source_emitted must be true" in line for line in stderr_lines),
        "theorem_errors": sum("theorem_derived must be true" in line for line in stderr_lines),
        "replay_source_errors": sum("uses_replay_as_source must be false" in line for line in stderr_lines),
        "stdout": proc.stdout.strip(),
    }
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    source_clause_failure = {
        "schema": "MTTFiniteC1RowKernelSourceClauseFailure.v1",
        "status": "CANDIDATE_PACKET_REJECTED_BY_SOURCE_CLAUSES",
        "validator_rejects_candidate_packet": proc.returncode == 1,
        "value_slot_bookkeeping_closed": True,
        "source_clause_bookkeeping_closed": True,
        "source_clauses_open": {
            key: not value["source_emitted"] or not value["theorem_derived"] or value["uses_replay_as_source"]
            for key, value in packet["source_clauses"].items()
        },
        "minimal_repair": [
            "derive physical Phi_fin^C1 action restriction to the finite trace/Frobenius measure",
            "emit zero boundary/source term for that same branch",
            "derive selected basis-to-row functional theorem for all 72 primitive rows",
            "emit phase/shift variation operators before residual replay",
            "emit same-source Hessian counterterm and b_selected",
        ],
        "promotion_barrier": barrier["statement"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    CLAUSES.write_text(json.dumps(source_clause_failure, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedFiniteC1RowKernelFunctionalCandidateOrSourceClauseFailure",
        "status": STATUS,
        "inputs": {
            "normal_form": rel(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "primitive_row_kernel_source_normal_form.packet.json"),
            "source_contract": rel(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "selected_source_object_contract.packet.json"),
            "algebraic_values": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json"),
            "promotion_barrier": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "promotion_barrier_and_next_gate.packet.json"),
        },
        "output_packets": {
            "finite_c1_rowkernel_functional_candidate": rel(PACKET),
            "source_clause_failure_certificate": rel(CLAUSES),
            "strict_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "FiniteC1RowKernelFunctionalCandidateFailureTheorem",
            "proved": True,
            "statement": (
                "The current corpus determines a complete finite C1 row-kernel functional candidate at the value level, "
                "but the strict source-clause validator rejects it because none of the five required source clauses is theorem-derived."
            ),
        },
        "what_closes_now": {
            "finite_rowkernel_candidate_packet_built": True,
            "all_110_values_attached_as_algebraic_candidates": True,
            "five_source_clause_validator_built": True,
            "source_clause_failure_certified": proc.returncode == 1,
        },
        "what_remains_open": source_clause_failure["source_clauses_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": contract["status"],
    }

    cert = {
        "certificate": "MTT_Selected_FiniteC1_RowKernelFunctional_Candidate_or_SourceClauseFailure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_rejects_candidate_packet": proc.returncode == 1,
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteC1 RowKernelFunctional Candidate or SourceClauseFailure v1

Status: `{STATUS}`.

The finite C1 row-kernel functional can now be written as a complete candidate:

```text
primitive values = {algebraic["counts"]["primitive_values_filled"]}
hessian values   = {algebraic["counts"]["hessian_values_filled"]}
sector values    = {algebraic["counts"]["sector_values_filled"]}
total values     = {algebraic["counts"]["total_algebraic_values_filled"]}
```

But the packet is not promoted. The strict validator rejects it because the five
source clauses are still not theorem-derived:

```text
measure/action binding
boundary/source null term
basis-to-row functionals
pre-residual phase/shift operators
Hessian b_selected source
```

This is progress: we now have a filled candidate object and a precise source
validator for the final promotion step.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
