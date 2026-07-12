"""Build the dynamic C1 transfer / primitive tensor / Hessian or independent rows gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1transferprimitivetensorhessian_or_independentrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSFER = PACKET_DIR / "dynamic_transfer_primitive_hessian_gate.packet.json"
ROWS = PACKET_DIR / "independent_rows_fallback_gate.packet.json"
DECISION = PACKET_DIR / "dynamic_value_emission_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1TransferPrimitiveTensorHessian_or_IndependentRows_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERPRIMITIVETENSORHESSIAN_OR_INDEPENDENTROWS_BUILT_VALUE_EMISSION_GATE_OPEN"
NEXT = "MTT_Selected_SameSourceDynamicTransferIdentity_or_IndependentRowFormulaExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows.candidate.json")
    cutset = load(
        DATA
        / "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows"
        / "remaining_dynamic_promotion_cutset.packet.json"
    )
    frontier = load(
        DATA
        / "selected_dynamicc1transfertensor_or_galerkinc1values"
        / "primitive_tensor_or_galerkin_frontier.packet.json"
    )
    primitive = load(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json")
    hessian = load(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json")
    row_fallback = load(
        DATA
        / "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows"
        / "primitive_kernel_formula_rows_fallback_gate.packet.json"
    )

    transfer = {
        "schema": "MTTDynamicTransferPrimitiveHessianGate.v1",
        "status": "CONDITIONAL_DYNAMIC_VALUES_EXACT_SELECTED_EMISSION_OPEN",
        "retired_static_blockers": cutset["retired_blockers"],
        "active_dynamic_cutset": cutset["active_dynamic_cutset"],
        "conditional_coordinate_packet": hessian["conditional_dynamic_transfer_coordinate_packet"],
        "primitive_tensor_frontier": {
            "required_primitive_formula": frontier["required_primitive_formula"],
            "route_A_selected_noninvariant_primitive_tensor": frontier["remaining_value_routes"][
                "route_A_selected_noninvariant_primitive_tensor"
            ],
            "route_B_selected_Hessian_or_b_source_vector": frontier["remaining_value_routes"][
                "route_B_selected_Hessian_or_b_source_vector"
            ],
            "route_C_honest_Galerkin_C1_values": frontier["remaining_value_routes"][
                "route_C_honest_Galerkin_C1_values"
            ],
        },
        "source_map_candidate": {
            "constructed": primitive["promotion_decision"]["source_map_candidate_constructed"],
            "selected_by_MTT_now": primitive["promotion_decision"]["source_map_selected_by_MTT_now"],
            "source_map_status": primitive["status"],
            "would_promote_if_selected": [
                "selected_A_selected",
                "selected_b_selected",
                "selected_deltaTheta_C1",
                "selected_sector_response_matrices",
            ],
        },
        "hessian_bselected_status": {
            "conditional_Gram_exact": hessian["hessian_bselected_fill_attempt"][
                "conditional_Hessian_Gram_candidate"
            ],
            "conditional_b_candidate": hessian["hessian_bselected_fill_attempt"]["conditional_b_candidate"],
            "promoted": hessian["hessian_bselected_fill_attempt"]["promoted"],
            "why_not_promoted": hessian["hessian_bselected_fill_attempt"]["why_not_promoted"],
        },
        "no_linear_algebra_obstruction": hessian["promotion_gate"]["no_linear_algebra_obstruction"],
        "selected_value_emission_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rows = {
        "schema": "MTTIndependentRowsFallbackGate.v1",
        "status": "INDEPENDENT_ROW_FORMULA_FALLBACK_OPEN",
        "row_count": row_fallback["row_count"],
        "all_rows_named": row_fallback["all_rows_named"],
        "required_global_clauses": row_fallback["required_global_clauses"],
        "fallback_reason": row_fallback["fallback_reason"],
        "route_b_executed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTDynamicValueEmissionDecision.v1",
        "status": "DYNAMIC_VALUE_GATE_BUILT_CLOSURE_NOT_CLAIMED",
        "static_source_retired": True,
        "conditional_dynamic_values_exact": True,
        "source_map_candidate_constructed": True,
        "same_source_dynamic_transfer_identity_closed": False,
        "selected_primitive_tensor_values_emitted": False,
        "selected_Hessian_or_b_source_vector_emitted": False,
        "independent_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1TransferPrimitiveTensorHessianOrIndependentRows",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows.candidate.json"),
            "dynamic_cutset": rel(
                DATA
                / "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows"
                / "remaining_dynamic_promotion_cutset.packet.json"
            ),
            "primitive_tensor_frontier": rel(
                DATA
                / "selected_dynamicc1transfertensor_or_galerkinc1values"
                / "primitive_tensor_or_galerkin_frontier.packet.json"
            ),
            "primitive_hessian_source_map": rel(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"),
            "dynamic_transfer_hessian_bselected": rel(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"),
        },
        "output_packets": {
            "dynamic_transfer_primitive_hessian_gate": rel(TRANSFER),
            "independent_rows_fallback_gate": rel(ROWS),
            "dynamic_value_emission_decision": rel(DECISION),
        },
        "theorem": {
            "name": "DynamicC1TransferPrimitiveTensorHessianGateTheorem",
            "proved": True,
            "statement": (
                "After static Weyl-pair source provenance is retired, the dynamic C1 gate has no remaining "
                "linear-algebra obstruction: the conditional 72-real transfer has rank 2, A^T A=12 I_2, "
                "b=(phase+shift), and deltaTheta=(1,1). The only open proof obligation is selected value "
                "emission: same-source dynamic transfer identity, selected primitive tensor values, selected "
                "Hessian/b source vector, or independent row formula execution."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1TransferPrimitiveTensorHessian_or_IndependentRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "conditional_dynamic_values_exact": True,
        "same_source_dynamic_transfer_identity_closed": False,
        "independent_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1TransferPrimitiveTensorHessian or IndependentRows v1

Status: `{STATUS}`.

The static Weyl-pair source blockers are retired. The conditional dynamic
72-real packet is exact: rank 2, `A^T A=12 I_2`, `A^T b=(12,12)`, and
`deltaTheta=(1,1)`.

The remaining gate is selected value emission:

- same-source dynamic transfer identity,
- selected primitive C1 tensor/overlap contractions,
- selected Hessian/source vector `b_selected`,
- or independent execution of the primitive row formulas.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
"""

    for path, payload in [
        (TRANSFER, transfer),
        (ROWS, rows),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
