"""Build the U1/Y Route-C dotD alpha1 source-normalization or End0 routing gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1y_finite_hym_gate": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "q79_alpha1_value_fill": Q79 / "certificates" / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json",
    "q79_phifin_alpha1_payload": Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json",
    "sm_physical_dotd_or_end0_routing": SM / "certificates" / "selected_physical_dotd_alpha1_or_end0_sector_routing_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_u1y_routec_end0_to_sector_functor_value_packet.open.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_SOURCENORM_NOGO_END0SECTOR_FUNCTOR_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "guardrails": data.get("guardrails"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    parent = load(INPUTS["u1y_finite_hym_gate"])
    q79_alpha1 = load(INPUTS["q79_alpha1_value_fill"])
    q79_phifin = load(INPUTS["q79_phifin_alpha1_payload"])
    sm_dotd = load(INPUTS["sm_physical_dotd_or_end0_routing"])

    route_a = q79_alpha1["route_A_source_normalization"]
    route_b = q79_alpha1["route_B_end0_to_sector_routing"]
    q79_contract = q79_alpha1["next_end0_sector_functor_value_packet_contract"]

    contract = {
        "schema": "SelectedU1YRouteCEnd0ToSectorFunctorSourceAndValuePacket.v1",
        "status": "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED",
        "branch": q79_contract["codomain"]["branch"],
        "domain": q79_contract["domain"],
        "codomain": q79_contract["codomain"],
        "required_fields": q79_contract["required_fields"],
        "validator_flags_that_must_be_theorem_derived": q79_contract["validator_flags_that_must_be_theorem_derived"],
        "acceptance_tests": q79_contract["acceptance_tests"],
        "forbidden_shortcuts": q79_contract["forbidden_shortcuts"],
        "values": {
            "End0_basis_map_T1_T2_T3_to_sector_carrier_basis": None,
            "sector_projectors_in_selected_End0_image": None,
            "normalization_dotD_h_ext_to_sector_dotD_alpha1": None,
            "selected_Z_X_or_SU5_E6_routing_proof": None,
            "sector_charge_routing_table_with_1M_rule": None,
            "same_BN_basis_Riesz_Duhamel_response": None,
            "honest_validator_replay": None,
        },
    }

    decision = {
        "naive_source_normalization_rejected": route_a["naive_Ext_scale_to_alpha1_source_normalization_rejected"],
        "shared_circle_guardrail_retained": route_a["central_shared_circle_retained"],
        "End0_sector_route_primary": q79_alpha1["decision"]["sector_routing_route_remains_primary"],
        "selected_Ext_density_scale_tangent_closed_in_SM_support": sm_dotd["selected_Ext_density_scale_tangent_closed"],
        "physical_dotD_alpha1_payload_extracted": False,
        "selected_End0_to_sector_functor_values_extracted": False,
        "selected_transfer_normalization_closed": False,
        "same_basis_dotD_matrices_exist_conditionally": route_b["same_basis_dotD_matrices_exist"],
        "honest_bn_validator_fails_only_by_source_flags": route_b["honest_bn_validator_fails_only_by_source_flags"],
        "phifin_alpha1_payload_status_imported": q79_phifin["status"],
        "dotD_alpha1_source_closed": False,
        "primitive_C1_values_computed": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCDotDAlpha1SourceNormalizationOrEnd0SectorRoutingReductionTheorem",
        "proved": True,
        "statement": (
            "The dotD_alpha1 value route is reduced to the selected End0-to-sector "
            "functor packet. The naive route that identifies continuous Ext-density "
            "scale with physical alpha1 source normalization is rejected because it "
            "does not vary the integral Chern/source row, and the shared circle stays "
            "degree-zero. Existing same-basis dotD matrices, projectors, and SM Ext "
            "tangent support are compatible support only. Closure now requires "
            "theorem-derived End0-to-sector routing values and transfer normalization, "
            "followed by honest dotD replay without lifted flags."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCdotDAlpha1SourceNormalizationOrEnd0SectorRouting",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_finite_hym_gate": parent,
                "q79_alpha1_value_fill": q79_alpha1,
                "q79_phifin_alpha1_payload": q79_phifin,
                "sm_physical_dotd_or_end0_routing": sm_dotd,
            }.items()
        },
        "contract_path": rel(OUTPUT_CONTRACT),
        "route_A_source_normalization_nogo": route_a,
        "route_B_end0_to_sector_routing": route_b,
        "contract": contract,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "naive_Ext_scale_source_normalization_route_rejected": True,
            "shared_circle_degree_zero_guardrail_preserved": True,
            "End0_to_sector_route_selected_as_primary_frontier": True,
            "SM_Ext_density_tangent_imported_as_support_not_promotion": True,
            "machine_readable_End0_sector_value_contract_created": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_End0_to_sector_functor_values": True,
            "selected_transfer_normalization": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_dotD_source_theorem": True,
            "same_branch_alpha1_driver_theorem": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "selected_primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_alpha1_driver": False,
            "claims_physical_alpha1_value_extracted": False,
            "claims_selected_End0_to_sector_routing": False,
            "claims_selected_dotD_source": False,
            "claims_selected_transfer_normalization": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_diagnostic_lift_as_proof": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCdotDAlpha1SourceNormalizationOrEnd0SectorRouting",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "naive_source_normalization_rejected": decision["naive_source_normalization_rejected"],
        "End0_sector_route_primary": decision["End0_sector_route_primary"],
        "selected_Ext_density_scale_tangent_closed_in_SM_support": decision["selected_Ext_density_scale_tangent_closed_in_SM_support"],
        "selected_End0_to_sector_functor_values_extracted": False,
        "selected_transfer_normalization_closed": False,
        "dotD_alpha1_source_closed": False,
        "primitive_C1_values_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, contract, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C dotDAlpha1 SourceNormalization or End0SectorRouting v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"naive_source_normalization_rejected = {str(cert['naive_source_normalization_rejected']).lower()}",
        f"End0_sector_route_primary = {str(cert['End0_sector_route_primary']).lower()}",
        f"selected_Ext_density_scale_tangent_closed_in_SM_support = {str(cert['selected_Ext_density_scale_tangent_closed_in_SM_support']).lower()}",
        f"selected_End0_to_sector_functor_values_extracted = {str(cert['selected_End0_to_sector_functor_values_extracted']).lower()}",
        f"dotD_alpha1_source_closed = {str(cert['dotD_alpha1_source_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The direct scalar-normalization route is now rejected locally. The live",
        "route is the End0-to-sector functor and transfer-normalization packet.",
        "",
        "## Required Contract Fields",
        "",
    ]
    for item in candidate["contract"]["required_fields"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not identify continuous Ext-density scale with integral alpha1 source normalization.",
            "- Do not promote same-basis dotD matrices until End0-to-sector routing and transfer normalization are selected.",
            "- Do not use locked target columns, observed masses, CKM angles, or benchmark Yukawa entries.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, contract, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
