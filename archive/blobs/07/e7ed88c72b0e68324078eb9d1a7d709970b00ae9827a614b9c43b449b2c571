"""Build I11 C1 coordinate-chart support gate or physical source gap."""

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

SLUG = "selected_i11_c1coordinatechart_or_physicalsourcegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CHART = PACKET_DIR / "c1_response_coordinate_chart_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_c1_coordinate_chart_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_physical_source_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_physical_source_boundary_firstvariation_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11_C1CoordinateChart_or_PhysicalSourceGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11_C1_COORDINATE_CHART_BUILT_PHYSICAL_SOURCE_OPEN"
NEXT = "MTT_Selected_I11PhysicalSourceBoundaryFirstVariation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior = load(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json")
    primitive = load(
        DATA
        / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
        / "primitive_rows_execution_attempt.packet.json"
    )
    formal = load(
        DATA
        / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
        / "formal_110_row_replay_integrated.packet.json"
    )
    response = load(DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json")
    boundary = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "physical_action_boundary_promotion_attempt.packet.json"
    )

    coordinate_chart_built = (
        primitive["row_count"] == 72
        and primitive["basis_stage_accepted"]
        and primitive["dynamic_trace_binding_accepted"]
        and primitive["conditional_dynamic_values_retained"]["coordinate_system"]["codomain_real_dimension"] == 72
        and formal["row_counts"]["total_rows"] == 110
        and formal["formal_110_rows_executed"]
        and formal["formal_110_matches_prior_replay"]
    )
    selected_source_execution_open = (
        not primitive["primitive_rows_executed"]
        and not response["emission_audit"]["selected_operator_A_selected_emitted"]
        and not response["emission_audit"]["selected_source_vector_b_selected_emitted"]
        and not formal["hessian_source_rows"]["physical_source_promoted"]
    )
    physical_boundary_closed = boundary["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"][
        "physical_verified_now"
    ]

    chart = {
        "schema": "MTTI11C1ResponseCoordinateChartSublemma.v1",
        "status": "C1_RESPONSE_COORDINATE_CHART_BUILT_SOURCE_EXECUTION_OPEN",
        "proved": coordinate_chart_built,
        "statement": (
            "The selected I11/C1 response coordinate chart is now fixed as a typed finite chart: 72 primitive "
            "real response rows, organized as four sectors times phase/shift times 3x3 complex entries, with a "
            "formal 110-row replay ledger including primitive, sector-matrix, and Hessian/source rows. This closes "
            "coordinate-chart typing and row coverage, not selected physical source execution of those rows."
        ),
        "coordinate_system": primitive["conditional_dynamic_values_retained"]["coordinate_system"],
        "row_counts": formal["row_counts"],
        "formal_110_replay": {
            "executed": formal["formal_110_rows_executed"],
            "matches_prior_replay": formal["formal_110_matches_prior_replay"],
            "max_abs_error": formal["formal_110_max_abs_error"],
        },
        "source_execution_open": selected_source_execution_open,
        "not_closed": [
            "selected primitive row source execution",
            "selected A_selected emission",
            "selected b_selected emission",
            "physical source promotion for Hessian/source rows",
            "physical boundary/no-extra-source clause",
        ],
        "sources": [
            rel(
                DATA
                / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
                / "primitive_rows_execution_attempt.packet.json"
            ),
            rel(
                DATA
                / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
                / "formal_110_row_replay_integrated.packet.json"
            ),
            rel(DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current = {
        "schema": "MTTCurrentI11C1CoordinateChartTraceMapAttempt.v1",
        "status": "CURRENT_TRACE_MAP_HAS_COORDINATE_CHART_BUT_FAILS_PHYSICAL_SOURCE_VALIDATOR",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "c1_coordinate_chart_built": coordinate_chart_built,
        "selected_c1_response_source_execution_open": selected_source_execution_open,
        "physical_boundary_closed": physical_boundary_closed,
        "attached_certificate_evidence": [
            {"source": rel(CHART), "closes": "C1 coordinate chart typing and row coverage"},
            {
                "source": rel(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json"),
                "closes": "functional trace plus transport/dotD trace support",
            },
            {
                "source": rel(
                    DATA
                    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
                    / "formal_110_row_replay_integrated.packet.json"
                ),
                "closes": "formal 110-row replay only",
            },
            {
                "source": rel(DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"),
                "closes": "selected response operator blocker audit",
            },
            {
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "physical_action_boundary_promotion_attempt.packet.json"
                ),
                "closes": "algebraic boundary support only",
            },
        ],
        "why_validator_still_fails": [
            "coordinate chart exists, but the validator requires selected C1 response coordinate map as physical source data",
            "primitive rows are typed and replay-backed but not selected-source executed",
            "A_selected and b_selected are not physically emitted",
            "physical boundary/no-extra-source and first-variation identity remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = {
        "schema": "MTTConditionalPhysicalSourceTraceMapWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_AFTER_PHYSICAL_SOURCE_BOUNDARY_FIRSTVARIATION",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {"source": rel(CHART), "closes": "coordinate chart", "conditional": False},
            {"source": rel(FRONTIER), "closes": "selected C1 response source execution", "conditional": True},
            {"source": rel(FRONTIER), "closes": "A_selected and b_selected source emission", "conditional": True},
            {"source": rel(FRONTIER), "closes": "physical boundary/no-extra-source", "conditional": True},
            {"source": rel(FRONTIER), "closes": "physical first-variation identity", "conditional": True},
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTI11PhysicalSourceBoundaryFirstVariationFrontier.v1",
        "status": "COORDINATE_CHART_BUILT_PHYSICAL_SOURCE_BOUNDARY_FIRSTVARIATION_OPEN",
        "closed_now": {
            **prior["what_closes_now"],
            "c1_response_coordinate_chart": coordinate_chart_built,
            "formal_110_row_replay_integrated": formal["formal_110_rows_executed"],
        },
        "still_open": {
            "selected_c1_response_coordinate_map_as_source": {
                "coordinate_chart_built": coordinate_chart_built,
                "primitive_rows_executed": primitive["primitive_rows_executed"],
                "needs": "selected primitive row source execution or selected physical C1 response operator emission",
            },
            "selected_A_selected_and_b_selected": response["what_remains_open"],
            "physical_boundary_cancellation": {
                "algebraic_support": boundary["available_now"]["algebraic_finite_boundary_cancellation"],
                "physical_verified": physical_boundary_closed,
                "needs": boundary["still_missing_for_physical_promotion"],
            },
            "physical_first_variation_identity": {
                "current_support": "formal Euler projection and formal row replay only",
                "needs": "physical Phi_fin^C1 action identity on the selected response coordinate chart",
            },
        },
        "superset_strategy": {
            "straight_route": "Use the typed 72/110 row machinery to fix the chart without promoting row source execution.",
            "combined_route": "Combine transport/dotD trace support with formal row replay only as compatibility evidence.",
            "locked_target": "physical selected C1 response map and boundary identity, not benchmark or observed data fitting.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    CHART.write_text(json.dumps(chart, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11C1CoordinateChartOrPhysicalSourceGap",
        "status": STATUS,
        "output_packets": {
            "coordinate_chart": rel(CHART),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11C1CoordinateChartAndPhysicalSourceGapTheorem",
            "proved": True,
            "statement": (
                "The I11 C1 response coordinate chart is fixed by the 72 primitive row and formal 110-row ledgers. "
                "This closes row typing, coordinate order, and formal replay compatibility, while selected physical "
                "source execution of the C1 response map, A_selected, b_selected, boundary cancellation, and first "
                "variation remain open."
            ),
        },
        "what_closes_now": {
            "c1_response_coordinate_chart_built": coordinate_chart_built,
            "formal_110_row_replay_integrated": formal["formal_110_rows_executed"],
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_physical_source_witness_passes": witness_result["returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11_C1CoordinateChart_or_PhysicalSourceGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "c1_response_coordinate_chart_built": coordinate_chart_built,
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_physical_source_witness_passes": witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11 C1CoordinateChart or PhysicalSourceGap v1

Status: `{STATUS}`.

The C1 response coordinate chart is now fixed:

```text
primitive rows = 72
formal rows    = 110
chart built    = {coordinate_chart_built}
```

This closes coordinate typing and formal replay compatibility only. It does not
promote the selected physical C1 response source, `A_selected`, `b_selected`,
physical boundary cancellation, or the physical first-variation identity.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
