"""Build selected physical variation-principle source / quadrature-kernel values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_physical_source_theorem_template.packet.json"
ROUTE_B = PACKET_DIR / "route_b_quadrature_kernel_value_manifest.packet.json"
CONTRACT = PACKET_DIR / "source_or_kernel_acceptance_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalVariationPrincipleSource_or_QuadratureKernelValues_v1.md"

STATUS = "MTT_SELECTED_PHYSICALVARIATIONPRINCIPLESOURCE_OR_QUADRATUREKERNELVALUES_BUILT_VALUE_SLOTS_OPEN"
NEXT = "MTT_Selected_C1KernelValuesExecution_or_PhysicalSourcePromotion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rows_for_stage(schedule: dict[str, Any], stage_name: str) -> list[str]:
    for stage in schedule["execution_order"]:
        if stage["stage"] == stage_name:
            return list(stage["rows"])
    raise KeyError(stage_name)


def primitive_kernel_slot(row_id: str) -> dict[str, Any]:
    sector, response, coord = row_id.split(":")
    r_token, c_token = coord.split("c")
    i = int(r_token.removeprefix("r"))
    j = int(c_token)
    return {
        "row_id": row_id,
        "sector": sector,
        "response": response,
        "matrix_coordinate": [i, j],
        "kernel_template": f"ReImPair(<K_{sector}^{response} e_{j}, e_{i}>_C1)",
        "selected_kernel_defined": False,
        "independent_value_emitted": False,
        "replay_value_allowed_as_check_only": True,
    }


def sector_matrix_slot(row_id: str) -> dict[str, Any]:
    sector, _, coord = row_id.split(":")
    r_token, c_token = coord.split("c")
    i = int(r_token.removeprefix("r"))
    j = int(c_token)
    return {
        "row_id": row_id,
        "sector": sector,
        "matrix_coordinate": [i, j],
        "kernel_template": f"M_{sector}[{i},{j}] = response_matrix(K_{sector}, basis, b_selected)",
        "selected_kernel_defined": False,
        "independent_value_emitted": False,
        "replay_value_allowed_as_check_only": True,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun.candidate.json")
    cutset = load(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "minimal_engine_or_principle_cutset.packet.json")
    route_a_prev = load(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_a_variation_principle_derivation_attempt.packet.json")
    route_b_prev = load(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_b_quadrature_engine_run_attempt.packet.json")
    schedule = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json")
    replay_rows = load(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json")

    primitive_rows = rows_for_stage(schedule, "primitive_contractions")
    hessian_rows = rows_for_stage(schedule, "hessian_source")
    sector_rows = rows_for_stage(schedule, "sector_matrices")

    route_a = {
        "schema": "MTTPhysicalVariationPrincipleSourceTemplate.v1",
        "status": "PHYSICAL_SOURCE_THEOREM_TEMPLATE_BUILT_NOT_PROMOTED",
        "source_cutset": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "minimal_engine_or_principle_cutset.packet.json"),
        "theorem_name": "SelectedPhiFinC1PhysicalVariationSourceTheorem",
        "minimal_statement_to_prove": (
            "For the selected q79/F,m=1 terminal/Theta/Strominger branch and its admissible differentiated "
            "Phi_fin^C1 trace variations, the physical C1 action has first variation equal to the "
            "C1DefectLeakageFunctional normal equation; its boundary term vanishes; therefore the same "
            "source emits Q_residual, R_Z, R_X, b_selected, and the locked sector response packet."
        ),
        "required_clauses": cutset["route_A_minimal_requirements"],
        "formal_support_available": route_a_prev["finite_dimensional_derivation"],
        "source_promoted_now": False,
        "why_not_promoted": [
            "No corpus theorem yet identifies the physical C1 action with the candidate leakage functional.",
            "No selected admissible-variation class and boundary-cancellation proof is emitted here.",
            "b_selected remains replay/contract data until the same source theorem emits it.",
        ],
        "paper_insertion_targets": [
            "Theta-Closure execution principle paper",
            "Phi_fin finite emission paper",
            "SM-parity dynamic C1 packet appendix",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTQuadratureKernelValueManifest.v1",
        "status": "KERNEL_VALUE_MANIFEST_BUILT_VALUES_OPEN",
        "source_engine_skeleton": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_b_quadrature_engine_run_attempt.packet.json"),
        "basis_stage": {
            "row_count": route_b_prev["engine_spec"]["stage_counts"]["basis"],
            "ready": route_b_prev["engine_spec"]["basis_stage_ready"],
        },
        "primitive_kernel_slots": [primitive_kernel_slot(row) for row in primitive_rows],
        "hessian_source_slots": [
            {
                "row_id": row,
                "kernel_template": f"{row} = d^2 Phi_fin^C1 / d{row} at selected trace",
                "selected_kernel_defined": False,
                "independent_value_emitted": False,
                "replay_value_allowed_as_check_only": True,
            }
            for row in hessian_rows
        ],
        "sector_matrix_slots": [sector_matrix_slot(row) for row in sector_rows],
        "counts": {
            "primitive_kernel_slots": len(primitive_rows),
            "hessian_source_slots": len(hessian_rows),
            "sector_matrix_slots": len(sector_rows),
            "total_value_slots": len(primitive_rows) + len(hessian_rows) + len(sector_rows),
            "independent_values_emitted": 0,
            "replay_rows_available_as_checks": replay_rows["filled_by_replay_count"],
        },
        "selected_measure_pairing_defined": False,
        "exactness_or_error_bound_certificate": False,
        "run_executed_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    contract = {
        "schema": "MTTSourceOrKernelAcceptanceContract.v1",
        "status": "ACCEPTANCE_CONTRACT_FIXED_VALUES_OPEN",
        "accept_if_route_A": {
            "physical_source_theorem_proved": True,
            "emits_Q_residual_RZ_RX": True,
            "emits_b_selected": True,
            "boundary_terms_vanish": True,
            "locked_target_matches": True,
        },
        "accept_if_route_B": {
            "selected_measure_pairing_defined": True,
            "all_primitive_kernel_values_independent": len(primitive_rows),
            "all_hessian_source_values_independent": len(hessian_rows),
            "all_sector_matrix_values_independent": len(sector_rows),
            "exactness_or_error_bound_certificate": True,
            "locked_target_matches": True,
        },
        "locked_target_check": route_b_prev["locked_acceptance_oracle"],
        "current_result": {
            "route_A_accepts_now": False,
            "route_B_accepts_now": False,
            "closure_claimed": False,
        },
        "forbidden_shortcuts": cutset["forbidden_shortcuts"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalVariationPrincipleSourceOrQuadratureKernelValues",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun.candidate.json"),
            "minimal_cutset": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "minimal_engine_or_principle_cutset.packet.json"),
            "engine_skeleton": rel(DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_b_quadrature_engine_run_attempt.packet.json"),
            "quadrature_schedule": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"),
            "replay_rows": rel(DATA / "selected_firstvariationboundary_or_primitivequadraturerows_valuefill" / "route_b_replay_backed_primitive_rows.packet.json"),
        },
        "output_packets": {
            "route_a_physical_source_theorem_template": rel(ROUTE_A),
            "route_b_quadrature_kernel_value_manifest": rel(ROUTE_B),
            "source_or_kernel_acceptance_contract": rel(CONTRACT),
        },
        "theorem": {
            "name": "PhysicalSourceOrKernelValuesAcceptanceTheorem",
            "proved": True,
            "statement": (
                "The remaining dynamic C1 closure can be accepted only by a selected physical source theorem "
                "emitting the residual/Hessian packet or by independent selected kernel values for all finite "
                "C1 row slots with a locked-target certificate."
            ),
        },
        "what_closes_now": {
            "physical_source_theorem_template_built": True,
            "quadrature_kernel_value_manifest_built": True,
            "all_value_slots_enumerated": True,
            "acceptance_contract_fixed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "prove_physical_source_theorem": True,
            "define_selected_measure_pairing": True,
            "emit_72_independent_primitive_kernel_values": True,
            "emit_2_independent_hessian_source_values": True,
            "emit_36_independent_sector_matrix_values": True,
            "exactness_or_error_bound_certificate": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_physical_source_promoted": False,
            "route_B_kernel_values_executed": False,
            "replay_values_promoted_as_independent": False,
            "locked_target_used_as_selector": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalVariationPrincipleSource_or_QuadratureKernelValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
    }

    note = f"""# MTT Selected PhysicalVariationPrincipleSource or QuadratureKernelValues v1

Status: `{STATUS}`.

This gate converts the remaining proof phrase into fillable objects.

```text
Route A physical-source theorem promoted = False
Route B selected measure/pairing defined = False
primitive kernel value slots             = {len(primitive_rows)}
hessian/source value slots               = {len(hessian_rows)}
sector matrix value slots                = {len(sector_rows)}
independent values emitted               = 0
replay rows available only as checks     = {replay_rows["filled_by_replay_count"]}
```

The next step is no longer a broad search. It is either proving the named
`SelectedPhiFinC1PhysicalVariationSourceTheorem` or filling the selected finite
C1 kernel-value manifest with independent values and a certificate.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
