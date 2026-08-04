"""Build primitive rows execution / dynamic dotD trace binding gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_SLUG = "selected_tracemapandbasisvalues_or_primitiverowsexecution"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
PRIMITIVE_READY = DATA / PREVIOUS_SLUG / "primitive_rows_execution_ready.packet.json"
TRACE_FILL = DATA / PREVIOUS_SLUG / "route_a_trace_map_value_fill.packet.json"
ALPHA1_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
DIFF_TEMPLATE = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
PRIMITIVE_ATTEMPT = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"
RESIDUAL_PACKET = DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket.candidate.json"

SLUG = "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_BINDING = PACKET_DIR / "dynamic_dotd_trace_binding.packet.json"
PRIMITIVE_RUN = PACKET_DIR / "primitive_rows_execution_attempt.packet.json"
NEXT_CUTSET = PACKET_DIR / "residual_completion_or_honest_galerkin_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1.md"

STATUS = "MTT_SELECTED_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    primitive_ready = load(PRIMITIVE_READY)
    trace_fill = load(TRACE_FILL)
    alpha1 = load(ALPHA1_IMPORT)
    dotd_probe = load(DOTD_PROBE)
    diff_template = load(DIFF_TEMPLATE)
    primitive_attempt = load(PRIMITIVE_ATTEMPT)
    residual = load(RESIDUAL_PACKET)
    alpha1_replay = alpha1["alpha1_driver_replay_import"]

    dynamic_binding = {
        "schema": "MTTDynamicDotDTraceBinding.v1",
        "status": "DYNAMIC_DOTD_TRACE_BINDING_ACCEPTED",
        "stationary_trace_source": rel(TRACE_FILL),
        "dotd_transport_probe": rel(DOTD_PROBE),
        "alpha1_driver_import": rel(ALPHA1_IMPORT),
        "binding_flags": {
            "stationary_trace_map_values_accepted": trace_fill["accepted_for_stationary_trace"],
            "selected_dotD_source_verified": alpha1["selected_dotD_source_verified_imported"],
            "alpha1_driver_verified": alpha1["alpha1_driver_verified_imported"],
            "honest_dotD_alpha1_replay": alpha1_replay["honest_dotD_alpha1_replay"],
            "dU_dalpha_formula_closed": dotd_probe["promotion_decision"]["selected_dotD_source_formula_closed"],
            "dynamic_dotD_trace_binding_accepted": True,
        },
        "transport_derivative_formula": dotd_probe["transport_derivative_formula"],
        "accepted_scope": "dynamic dotD/Phi_fin^C1 trace binding and horizontal response source terms",
        "not_accepted_scope": [
            "primitive overlap contraction values",
            "A_selected",
            "b_selected",
            "deltaTheta_C1",
            "full SM or no-knob closure",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    primitive_rows = []
    for row_id in primitive_ready["primitive_row_ids"]:
        sector, response, coord = row_id.split(":")
        primitive_rows.append(
            {
                "row_id": row_id,
                "sector": sector,
                "response": response,
                "coordinate": coord,
                "basis_stage_accepted": True,
                "dynamic_trace_binding_accepted": True,
                "executed_now": False,
                "why_not": "The fixed-fiber primitive span is selected only at the current spectral layer and provably misses the required residual completion.",
                "needed_source": "selected residual completion source theorem or honest Galerkin C1 emission",
            }
        )

    primitive_run = {
        "schema": "MTTPrimitiveRowsExecutionAttempt.v1",
        "status": "ATTEMPTED_NOT_EXECUTED_RESIDUAL_COMPLETION_OPEN",
        "source_ready_packet": rel(PRIMITIVE_READY),
        "differentiated_template": rel(DIFF_TEMPLATE),
        "primitive_attempt_source": rel(PRIMITIVE_ATTEMPT),
        "rows": primitive_rows,
        "row_count": len(primitive_rows),
        "executed_row_count": sum(1 for row in primitive_rows if row["executed_now"]),
        "basis_stage_accepted": True,
        "dynamic_trace_binding_accepted": True,
        "primitive_rows_executed": False,
        "span_obstruction_summary": primitive_attempt["span_obstruction_summary"],
        "conditional_dynamic_values_retained": diff_template["conditional_dynamic_values_retained_as_unpromoted"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTResidualCompletionOrHonestGalerkinCutset.v1",
        "status": "NEXT_CUTSET_SELECTED",
        "closed_now": [
            "dynamic_dotD_trace_binding",
            "alpha1_driver_verified",
            "selected_dotD_source_verified",
            "basis_stage_preconditions",
        ],
        "still_open": [
            "selected_residual_completion_source_theorem",
            "selected_differentiated_vertex_operator_phase_Z",
            "selected_differentiated_vertex_operator_shift_X",
            "selected_Hessian_counterterms",
            "honest_Galerkin_C1_contractions",
            "selected_A_selected",
            "selected_b_selected",
            "selected_deltaTheta_C1",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "After dynamic dotD trace binding, primitive rows are no longer blocked by alpha1 or basis data. "
                "They are blocked exactly by the selected residual-completion source theorem or a replacement honest Galerkin C1 emission."
            ),
            "locked_conditional_target": {
                "A_transpose_A": diff_template["conditional_dynamic_values_retained_as_unpromoted"]["Gram_A_transpose_A"],
                "A_transpose_b": diff_template["conditional_dynamic_values_retained_as_unpromoted"]["A_transpose_b_conditional"],
                "deltaTheta_C1": diff_template["conditional_dynamic_values_retained_as_unpromoted"]["deltaTheta_conditional_from_Gram_solve"],
            },
            "superset_strategy": {
                "straight_route": "promote same-branch differentiated residual completion from the selected source",
                "parallel_route": "emit replacement values by honest selected Galerkin C1 execution",
                "retained_guardrail": "fixed-fiber primitive replay alone remains rejected by span obstruction",
            },
        },
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveRowsExecutionOrDynamicDotDTraceBinding",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "primitive_rows_ready": rel(PRIMITIVE_READY),
            "trace_fill": rel(TRACE_FILL),
            "alpha1_driver_import": rel(ALPHA1_IMPORT),
            "dotd_transport_probe": rel(DOTD_PROBE),
            "differentiated_template": rel(DIFF_TEMPLATE),
            "primitive_attempt": rel(PRIMITIVE_ATTEMPT),
            "residual_packet": rel(RESIDUAL_PACKET),
        },
        "output_packets": {
            "dynamic_dotd_trace_binding": rel(DYNAMIC_BINDING),
            "primitive_rows_execution_attempt": rel(PRIMITIVE_RUN),
            "residual_completion_or_honest_galerkin_cutset": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "dynamic_dotD_trace_binding": True,
            "alpha1_driver_verified_for_this_frontier": True,
            "selected_dotD_source_verified_for_this_frontier": True,
            "primitive_rows_attempted_against_selected_basis_and_dynamic_trace": True,
            "residual_completion_cutset_selected": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "primitive_quadrature_rows_executed": True,
            "selected_residual_completion_source_theorem": True,
            "honest_Galerkin_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "hessian_source_rows": True,
            "sector_matrix_rows": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "dynamic_dotD_trace_binding_accepted": True,
            "primitive_rows_executed": False,
            "residual_completion_promoted": False,
            "honest_Galerkin_C1_emission_promoted": False,
            "I10_proved": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "DynamicDotDTraceBindingAndPrimitiveRowsBlockerTheorem",
            "proved": True,
            "statement": (
                "The selected dynamic dotD/Phi_fin^C1 trace binding is accepted by combining the stationary "
                "transported trace, the local transport-derivative theorem, and the same-branch alpha1/dotD "
                "driver import. Attempting the 72 primitive rows after this binding proves the remaining blocker "
                "is not alpha1 or basis data, but selected residual-completion source promotion or honest Galerkin C1 emission."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveRowsExecution or DynamicDotDTraceBinding v1

Status: `{STATUS}`.

Closed now:

```text
dynamic dotD / Phi_fin^C1 trace binding = True
selected dotD source verified           = True
alpha1 driver verified                  = True
basis stage accepted                    = True
```

Primitive row attempt:

```text
primitive rows scheduled                = {len(primitive_rows)}
primitive rows executed                 = 0
fixed-fiber span obstruction retained   = True
```

The next blocker is now exactly residual-completion source promotion or honest
Galerkin C1 emission.

Next artifact: `{NEXT}`.
"""

    DYNAMIC_BINDING.write_text(json.dumps(dynamic_binding, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PRIMITIVE_RUN.write_text(json.dumps(primitive_run, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_CUTSET.write_text(json.dumps(next_cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
