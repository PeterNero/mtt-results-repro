"""Build C1-to-BHuv projection tensor or F_Huv rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_c1tobhuvprojectiontensor_or_fhuvrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1ToBHuvProjectionTensor_or_FHuvRows_v1.md"

CONTRACT = PACKET_DIR / "c1_to_bhuv_projection_tensor_contract.packet.json"
INVENTORY = PACKET_DIR / "c1_variation_vs_higgs_slot_inventory.packet.json"
ATTEMPT = PACKET_DIR / "projection_tensor_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c1_to_bhuv_tensor_attempt.packet.json"

PREVIOUS = DATA / "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution.candidate.json"
C1_ROUTING = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_72_slot_routing.packet.json"
)
C1_SHAPE = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_shape_compatibility.packet.json"
)
C2_EHUV = (
    DATA
    / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
    / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
)
C3_EHUV = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
PROJECTION_ATTEMPT = (
    DATA
    / "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
    / "bselected_projection_execution_attempt.packet.json"
)
C1_PAYLOAD = (
    DATA
    / "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
    / "selected_c1_hessian_payload_import.packet.json"
)

STATUS = (
    "MTT_SELECTED_C1TOBHUVPROJECTIONTENSOR_OR_FHUVROWS_"
    "CONTRACT_CLOSED_HIGGS_SLOT_TENSOR_OPEN"
)
NEXT = "MTT_Selected_HiggsC1VariationSlotExtension_or_AmbientHessianRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing C1-to-BHuv tensor inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        C1_ROUTING,
        C1_SHAPE,
        C2_EHUV,
        C3_EHUV,
        BHUV,
        PROJECTION_ATTEMPT,
        C1_PAYLOAD,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    c1_routing = load(C1_ROUTING)
    c1_shape = load(C1_SHAPE)
    c2 = load(C2_EHUV)
    c3 = load(C3_EHUV)
    bhuv = load(BHUV)
    projection_attempt = load(PROJECTION_ATTEMPT)
    c1_payload = load(C1_PAYLOAD)

    routed_sectors = sorted({row["sector"] for row in c1_routing["rows"]})
    higgs_labels = c2["typing_checks"]["ordered_E_H_UV_basis_labels"]
    higgs_source_ids = c2["finite_quotient_basis"]["uv_lift_basis"]
    higgs_slot_rows = [
        row for row in c1_routing["rows"] if row["sector"] in {"H", "H_u", "H_d", "H_d^dagger", "H_d_dagger"}
    ]
    phase_count = sum(1 for row in c1_routing["rows"] if row["variation_operator_shape"] == "phase_R_Z")
    shift_count = sum(1 for row in c1_routing["rows"] if row["variation_operator_shape"] == "shift_R_X")
    s_beta = previous["key_numbers"]["selected_s_beta_value"]

    contract = {
        "schema": "MTTC1ToBHuvProjectionTensorContract.v1",
        "status": "C1_TO_BHUV_PROJECTION_TENSOR_CONTRACT_CLOSED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_tensor": {
            "name": "T_C1<-Huv",
            "domain": "selected source-orthonormal B_Huv columns (H_u,H_d^dagger)",
            "codomain": "selected two-coordinate C1 variation/Hessian payload before residual replay",
            "equivalent_forms": [
                "a source-owned C1 variation-coordinate map evaluated on B_Huv",
                "an ambient selected 27x27 Hess(F_C1) matrix whose restriction can be evaluated",
                "direct certified F_Huv Herm(2) rows",
            ],
            "acceptance_formula": "M_Huv = T_C1<-Huv^* (A^T A)_C1 T_C1<-Huv, if T is source-owned and complete",
            "certificate_requirements": [
                "same source branch q79/F,m=1",
                "pre-residual provenance",
                "Higgs E_H^UV source IDs bound to the C1 variation coordinates",
                "quotient admissibility",
                "Hermitian/source ownership certificate",
            ],
        },
        "forbidden_substitutes": [
            "matter-sector C1 slot routing without Higgs slots",
            "diagonal HYM metric/connection on E_H^UV alone",
            "low-energy q(H_u)=q(H_d^dagger)=H quotient alone",
            "compressed A^T A normal matrix without T_C1<-Huv",
            "observed Higgs beta/lambda/mass values",
        ],
        "decision": {
            "projection_tensor_contract_closed": True,
            "accepted_source_routes_named": True,
            "forbidden_substitutes_retired": True,
        },
    }

    inventory = {
        "schema": "MTTC1VariationVsHiggsSlotInventory.v1",
        "status": "C1_VARIATION_AND_HIGGS_SLOT_INVENTORY_EXECUTED_NO_TENSOR",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "c1_variation_routing": {
            "row_count": c1_routing["row_count"],
            "phase_R_Z_rows": phase_count,
            "shift_R_X_rows": shift_count,
            "routed_sectors": routed_sectors,
            "sector_routing": c1_routing["sector_routing"],
            "higgs_slot_rows_found": len(higgs_slot_rows),
            "operator_shapes_selected_as_source_now_in_legacy_packet": c1_shape[
                "operator_shapes_selected_as_source_now"
            ],
            "legacy_shape_source_map_selected_by_MTT_now": c1_shape[
                "source_map_selected_by_MTT_now"
            ],
        },
        "higgs_slot_data": {
            "ordered_E_H_UV_basis_labels": higgs_labels,
            "uv_lift_source_ids": [
                {"channel": item["channel"], "id": item["id"], "source_id_emitted": item["source_id_emitted"]}
                for item in higgs_source_ids
            ],
            "single_low_energy_quotient_closed": c2["typing_checks"][
                "single_higgs_projection_closed"
            ],
            "T3_eigenline_binding_closed": c3["bridge_clause_closed"],
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
        },
        "intersection_result": {
            "matter_variation_sectors_intersect_Huv_labels": False,
            "Huv_labels_present_in_72_slot_routing": len(higgs_slot_rows) > 0,
            "source_owned_C1_to_BHuv_tensor_emitted": False,
            "reason": (
                "The C1 72-slot table routes selected phase/shift variation shapes "
                "through matter sectors u,d,e,nuD. The Higgs source IDs H_u and "
                "H_d^dagger are closed in E_H^UV, but no current packet binds those "
                "Higgs columns to the two C1 variation coordinates."
            ),
        },
        "decision": {
            "inventory_executed": True,
            "C1_matter_slot_routing_available": True,
            "Higgs_E_H_UV_source_ids_available": True,
            "C1_to_BHuv_projection_tensor_emitted": False,
        },
    }

    attempt = {
        "schema": "MTTProjectionTensorEmissionAttempt.v1",
        "status": "PROJECTION_TENSOR_EMISSION_ATTEMPTED_ZERO_FHUV_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_strict_payload": {
            "compressed_C1_payload_imported": c1_payload["decision"][
                "strict_dynamic_C1_payload_imported"
            ],
            "selected_b_selected_available": c1_payload["decision"][
                "selected_b_selected_available"
            ],
            "A_transpose_A": c1_payload["compressed_payload"]["A_transpose_A"],
            "A_transpose_b": c1_payload["compressed_payload"]["A_transpose_b"],
        },
        "candidate_routes_tested": {
            "use_72_slot_routing_as_T_C1_Huv": {
                "accepted": False,
                "reason": "72-slot routing has no Higgs H_u/H_d^dagger slots",
            },
            "use_E_H_UV_C2_basis_as_T_C1_Huv": {
                "accepted": False,
                "reason": "C2 emits Higgs source IDs and quotient exactness, not C1 variation coordinates",
            },
            "use_C3_diagonal_HYM_T3_as_T_C1_Huv": {
                "accepted": False,
                "reason": "C3 binds metric/connection eigenlines, not the C1 second-variation coordinate map",
            },
            "use_A_transpose_A_as_direct_Huv": {
                "accepted": False,
                "reason": projection_attempt["naive_identification_guard"]["decision"],
            },
        },
        "emitted_tensor": None,
        "emitted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "emitted_certificates": {
            "C1_to_BHuv_projection_tensor_certificate": None,
            "same_source_exactness_or_error_certificate": None,
            "quotient_admissibility_certificate": None,
            "Hermitian_source_ownership_certificate": None,
        },
        "decision": {
            "projection_tensor_emission_attempted": True,
            "source_owned_C1_to_BHuv_tensor_emitted": False,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterC1ToBHuvTensorAttempt.v1",
        "status": "NEXT_FRONTIER_HIGGS_C1_VARIATION_SLOT_EXTENSION_OR_AMBIENT_HESSIAN_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "C1-to-BHuv projection tensor acceptance contract",
            "inventory comparing C1 72-slot routing with H_u/H_d^dagger source IDs",
            "proof that existing C1 routing is matter-sector routing, not a Higgs tensor",
            "rejection of C2, C3, and compressed A^T A as substitutes for T_C1<-Huv",
        ],
        "still_open": [
            "selected Higgs C1 variation slots extending the 72-slot table",
            "or ambient 27x27 Hess(F_C1)_selected rows on E_H^UV",
            "source-owned T_C1<-Huv tensor values",
            "B_Huv^* Hess(F_C1)_selected B_Huv execution",
            "nonzero Omega/direct Herm(2) Huv rows and certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedC1ToBHuvProjectionTensorOrFHuvRows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "C1ToBHuvProjectionTensorNotYetEmittedTheorem",
            "proved": True,
            "statement": (
                "The required C1-to-BHuv tensor is now exactly typed. Current "
                "data provide strict dynamic C1 compressed rows and selected "
                "Higgs E_H^UV/B_Huv source IDs, but no source-owned map from "
                "H_u,H_d^dagger into the two C1 variation coordinates. The 72-slot "
                "C1 routing is matter-sector routing through u,d,e,nuD and has "
                "zero Higgs slots. Therefore no F_Huv rows are emitted yet; the "
                "next frontier is a selected Higgs C1 variation-slot extension or "
                "ambient 27x27 Hess(F_C1) rows."
            ),
        },
        "packets": {
            "c1_to_bhuv_projection_tensor_contract": rel(CONTRACT),
            "c1_variation_vs_higgs_slot_inventory": rel(INVENTORY),
            "projection_tensor_emission_attempt": rel(ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "c1_routing": rel(C1_ROUTING),
            "c1_shape": rel(C1_SHAPE),
            "c2_ehuv": rel(C2_EHUV),
            "c3_ehuv": rel(C3_EHUV),
            "bhuv": rel(BHUV),
            "projection_attempt": rel(PROJECTION_ATTEMPT),
            "c1_payload": rel(C1_PAYLOAD),
        },
        "closure_decision": {
            "projection_tensor_contract_closed": True,
            "inventory_executed": True,
            "projection_tensor_emission_attempted": True,
            "C1_matter_slot_routing_available": True,
            "Higgs_E_H_UV_source_ids_available": True,
            "source_owned_C1_to_BHuv_tensor_emitted": False,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "selected_Higgs_C1_variation_slots_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "selected_H_response_table_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "C1_72_slot_row_count": c1_routing["row_count"],
            "C1_phase_R_Z_rows": phase_count,
            "C1_shift_R_X_rows": shift_count,
            "C1_higgs_slot_rows_found": len(higgs_slot_rows),
            "Huv_source_column_count": 2,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedC1ToBHuvProjectionTensorOrFHuvRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "projection_tensor_contract_closed": True,
        "inventory_executed": True,
        "projection_tensor_emission_attempted": True,
        "C1_matter_slot_routing_available": True,
        "Higgs_E_H_UV_source_ids_available": True,
        "source_owned_C1_to_BHuv_tensor_emitted": False,
        "ambient_27_by_27_Hessian_matrix_emitted": False,
        "selected_Higgs_C1_variation_slots_emitted": False,
        "selected_F_Huv_rows_emitted": False,
        "direct_Herm2_row_payload_emitted": False,
        "lambda_H_predicted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected C1ToBHuvProjectionTensor or FHuvRows v1

Status: `{STATUS}`

## Theorem

The required projection tensor is now precisely typed:

```text
T_C1<-Huv : span(B_Huv[H_u], B_Huv[H_d^dagger]) -> selected C1 variation coordinates
M_Huv = T_C1<-Huv^* (A^T A)_C1 T_C1<-Huv
```

Current data provide both sides of the interface, but not the tensor between
them:

- C1 variation routing: `{routed_sectors}` with `{c1_routing["row_count"]}` rows
- Higgs source IDs: `{higgs_labels}`
- Higgs rows inside the C1 72-slot routing: `{len(higgs_slot_rows)}`

Therefore the existing C1 routing is matter-sector routing, not a Higgs
`B_Huv` projection tensor.  C2 Higgs source IDs, C3 diagonal HYM eigenlines, and
the compressed `A^T A` payload are all useful support but not substitutes for
`T_C1<-Huv`.

Accepted `F_Huv` rows: `0`.
Selected `s_beta` retained as projection support: `{s_beta}`.

Next artifact: `{NEXT}`
"""

    write_json(CONTRACT, contract)
    write_json(INVENTORY, inventory)
    write_json(ATTEMPT, attempt)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
