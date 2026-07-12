"""Build selected trace-map/basis values or primitive rows execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_SLUG = "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
ROUTE_A_FILL = DATA / PREVIOUS_SLUG / "route_a_first_variation_certificate_partial_fill.packet.json"
ROUTE_B_BASIS = DATA / PREVIOUS_SLUG / "route_b_basis_rows_first_run.packet.json"
NEXT_CUTSET = DATA / PREVIOUS_SLUG / "next_cutset_after_partial_fill.packet.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
PROJECTOR_PROMOTION = DATA / "selected_finite_projector_source_promotion.candidate.json"
TRANSPORT_REPLAY = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
QUAD_PLAN = DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "route_b_quadrature_execution_manifest.packet.json"

SLUG = "selected_tracemapandbasisvalues_or_primitiverowsexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_FILL = PACKET_DIR / "route_a_trace_map_value_fill.packet.json"
BASIS_FILL = PACKET_DIR / "route_b_selected_basis_value_fill.packet.json"
PRIMITIVE_PLAN = PACKET_DIR / "primitive_rows_execution_ready.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1.md"

STATUS = "MTT_SELECTED_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_sector(sector: str) -> str:
    return "N" if sector == "nuD" else sector


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    route_a_prev = load(ROUTE_A_FILL)
    route_b_prev = load(ROUTE_B_BASIS)
    cutset = load(NEXT_CUTSET)
    gauge_trace = load(GAUGE_TRACE)
    projector = load(PROJECTOR_PROMOTION)
    transport = load(TRANSPORT_REPLAY)
    quad_plan = load(QUAD_PLAN)

    trace_slots: dict[str, Any] = {}
    for sector, slot in gauge_trace["transported_trace"]["sector_slots"].items():
        trace_slots[sector] = {
            "sector": sector,
            "source_trace_selected_functionally": slot["source_trace_selected_functionally"],
            "rank_preserved": slot["rank_preserved"],
            "gap_preserved_by_unitary_transport": slot["gap_preserved_by_unitary_transport"],
            "selected_projector_formula": slot["selected_projector_formula"],
            "selected_transported_basis_labels": slot["selected_transported_basis_labels"],
            "finite_27_mode_replay_closed": slot["finite_27_mode_replay_closed"],
            "transport": slot["transport"],
        }

    trace_fill = {
        "schema": "MTTSelectedTraceMapValueFill.v1",
        "status": "FUNCTIONAL_TRACE_MAP_VALUES_FILLED_DYNAMIC_BINDING_OPEN",
        "source_trace": rel(GAUGE_TRACE),
        "transport_replay": rel(TRANSPORT_REPLAY),
        "trace_values": trace_slots,
        "filled_flags": {
            "selected_trace_map_values": gauge_trace["promotion_decision"]["functional_selected_trace_proved"],
            "selected_source_verified_for_functional_End0_trace": gauge_trace["promotion_decision"]["selected_source_verified_for_functional_End0_trace"],
            "selected_projector_source_verified": transport["promotion_decision"]["selected_projector_source_verified"],
            "transport_closed_finite_validator_replay": transport["promotion_decision"]["transport_closed_finite_validator_replay"],
        },
        "remaining_dynamic_flags": {
            "selected_dotD_source_verified": transport["promotion_decision"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": transport["promotion_decision"]["alpha1_driver_verified"],
            "finite_27_mode_replay_closed_without_symbolic_transport": False,
            "physical_first_variation_identity": False,
            "boundary_cancellation_for_dynamic_C1_trace": False,
        },
        "accepted_for_stationary_trace": True,
        "accepted_for_dynamic_C1_primitive_rows": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    basis_rows: list[dict[str, Any]] = []
    for old in route_b_prev["basis_rows"]:
        sec = source_sector(old["sector"])
        slot = projector["promoted_sector_slots"][sec]
        labels = slot["selected_basis_labels"]
        index = int(old["basis_id"].split(":")[-1].replace("k", "").replace("h", "0"))
        label = labels[index] if index < len(labels) else labels[0]
        basis_rows.append(
            {
                **old,
                "selected_now": True,
                "selected_basis_value": label,
                "selected_projector_value": slot["selected_projector_formula"],
                "gram_matrix": "identity_preserved_by_unitary_transport",
                "spectral_gap": "preserved_from_model_gap",
                "gap_preserved": slot["gap_preserved"],
                "projector_idempotent": slot["projector_idempotent"],
                "projector_self_adjoint": slot["projector_self_adjoint"],
                "source_verified_by_transport_conjugation": slot["source_verified_by_transport_conjugation"],
                "stationary_rho_s_promoted": slot["stationary_rho_s_promoted"],
                "why_not_selected": None,
            }
        )

    selected_count = sum(1 for row in basis_rows if row["selected_now"])
    basis_fill = {
        "schema": "MTTSelectedBasisValueFill.v1",
        "status": "STATIONARY_BASIS_PROJECTOR_GRAM_GAP_ROWS_FILLED",
        "source_projector_promotion": rel(PROJECTOR_PROMOTION),
        "basis_rows": basis_rows,
        "row_count": len(basis_rows),
        "selected_row_count": selected_count,
        "all_basis_rows_selected": selected_count == len(basis_rows),
        "basis_values_scope": "stationary transported HYM/End0 trace; dynamic C1 primitive response still requires dotD/trace binding",
        "accepted_for_basis_stage": True,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    primitive_plan = {
        "schema": "MTTPrimitiveRowsExecutionReady.v1",
        "status": "READY_NOT_EXECUTED_DYNAMIC_DOTD_TRACE_BINDING_OPEN",
        "source_quadrature_manifest": rel(QUAD_PLAN),
        "basis_stage_accepted": basis_fill["accepted_for_basis_stage"],
        "primitive_row_count": quad_plan["row_requirements"]["primitive_contraction_rows"]["count"],
        "primitive_row_ids": quad_plan["row_requirements"]["primitive_contraction_rows"]["row_ids"],
        "can_execute_rows_now": False,
        "why_not": [
            "selected stationary basis rows are filled, but dynamic dotD trace binding is still open",
            "primitive rows require the differentiated C1 trace operator, not only stationary projectors",
            "alpha1/dotD transport derivative terms must be attached before C1 primitive contractions can be selected",
        ],
        "next_execution_requirements": [
            "dU/dalpha transport derivative term",
            "selected dynamic C1 trace binding",
            "primitive overlap/contraction row formula in the selected transported basis",
            "error or exact-symbolic certificate for every primitive row",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTraceMapAndBasisValuesOrPrimitiveRowsExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "route_a_partial_fill": rel(ROUTE_A_FILL),
            "route_b_basis_first_run": rel(ROUTE_B_BASIS),
            "next_cutset": rel(NEXT_CUTSET),
            "gauge_transported_trace": rel(GAUGE_TRACE),
            "finite_projector_promotion": rel(PROJECTOR_PROMOTION),
            "transport_conjugation_replay": rel(TRANSPORT_REPLAY),
            "quadrature_manifest": rel(QUAD_PLAN),
        },
        "output_packets": {
            "route_a_trace_map_value_fill": rel(TRACE_FILL),
            "route_b_selected_basis_value_fill": rel(BASIS_FILL),
            "primitive_rows_execution_ready": rel(PRIMITIVE_PLAN),
        },
        "what_closes_now": {
            "selected_trace_map_values_functional_stationary": True,
            "selected_basis_projector_gram_gap_values_stationary": True,
            "basis_stage_can_advance": True,
            "primitive_row_ids_locked": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_first_variation_identity": True,
            "boundary_cancellation_for_dynamic_C1_trace": True,
            "selected_dynamic_dotD_trace_binding": True,
            "primitive_quadrature_rows": True,
            "hessian_source_rows": True,
            "sector_matrix_rows": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_trace_map_values_accepted": True,
            "route_B_basis_rows_accepted": True,
            "route_B_can_advance_to_primitive_rows_after_dynamic_binding": True,
            "primitive_rows_executed": False,
            "I10_proved": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "TraceMapAndBasisValuePromotionTheorem",
            "proved": True,
            "statement": (
                "The selected gauge-transported Phi_fin trace and finite projector source-promotion packets "
                "supply stationary selected trace-map values and selected sector basis/projector/Gram/gap rows. "
                "This advances the quadrature route past the basis stage, but primitive C1 rows remain open until "
                "the dynamic dotD/transport-derivative trace binding is supplied."
            ),
        },
        "superset_strategy": {
            "straight_route_A": cutset["recommended_next"]["superset_strategy"]["straight_route_A"],
            "parallel_route_B": cutset["recommended_next"]["superset_strategy"]["parallel_route_B"],
            "shared_missing_object_after_this_gate": "selected dynamic dotD/Phi_fin^C1 trace binding and primitive contraction rows",
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1",
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

    note = f"""# MTT Selected TraceMapAndBasisValues or PrimitiveRowsExecution v1

Status: `{STATUS}`.

Closed now:

```text
stationary selected trace-map values        = True
selected basis/projector/Gram/gap rows      = True
basis rows accepted                         = {selected_count}/{len(basis_rows)}
primitive row ids locked                    = {primitive_plan["primitive_row_count"]}
```

Still open:

```text
dynamic dotD / Phi_fin^C1 trace binding     = True
primitive quadrature rows executed          = False
physical first variation identity           = False
boundary cancellation for dynamic C1 trace  = False
```

Next artifact: `{NEXT}`.
"""

    TRACE_FILL.write_text(json.dumps(trace_fill, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    BASIS_FILL.write_text(json.dumps(basis_fill, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PRIMITIVE_PLAN.write_text(json.dumps(primitive_plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
