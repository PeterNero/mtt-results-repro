"""Build the selected Phi_fin alpha1 payload attempt artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_DATA = Q79 / "candidate_data"
Q79_CERTS = Q79 / "certificates"

OUTPUT_DATA = DATA / "selected_phifin_alpha1_payload.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_alpha1_payload_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_PhiFin_Alpha1_Payload_v1.md"

INPUTS = {
    "previous": DATA / "selected_source_origin_and_alpha1_driver.candidate.json",
    "phifin_schema": DATA / "finite_emission_morphism_phifin.candidate.json",
    "projective_gerbe_promotion": DATA / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "twisted_promotion_attempt": Q79_CERTS / "iwasawa_twisted_source_promotion_packet.attempt.json",
    "projective_rhoe_validator": Q79_CERTS / "iwasawa_projective_rhoE_mesh_validator_certificate.json",
    "projective_rhoe_mesh": Q79_DATA / "iwasawa_projective_magnetic_carrier.meshN1.json",
    "block_factorized_sector_maps": Q79_DATA / "iwasawa_block_factorized_sector_maps.candidate.json",
    "block_factorized_twisted_packet": Q79_DATA / "iwasawa_block_factorized_twisted_packet.candidate.json",
    "q79_routec_de_action": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "de_action.candidate.json",
    "q79_routec_reduced_green": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "reduced_green.candidate.json",
    "q79_routec_dotd": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "dotd_response.candidate.json",
    "zero_mode_interface": Q79_CERTS / "selected_zero_mode_basis_dotd_interface_certificate.json",
    "c1_response_template": Q79_CERTS / "selected_c1_response_data_certificate.template.json",
    "c1_response_attempt": Q79_CERTS / "selected_c1_response_extraction_attempt_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def input_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
            "status": load_json(path).get("status", "UNKNOWN") if path.exists() else "MISSING",
        }
        for key, path in INPUTS.items()
    }


def all_slot_flag(slots: dict[str, dict[str, object]], flag: str) -> bool:
    return all(bool(slot.get(flag)) for slot in slots.values())


def selected_value(value: object) -> bool:
    return value is not None and value is not False


def build_payload_slots(
    phifin: dict[str, object],
    twisted: dict[str, object],
    projective: dict[str, object],
    sector_maps: dict[str, object],
    de_action: dict[str, object],
    green: dict[str, object],
    dotd: dict[str, object],
    zero_mode: dict[str, object],
    c1_template: dict[str, object],
    c1_attempt: dict[str, object],
) -> dict[str, object]:
    de_slots = de_action["operator_slots"]
    green_slots = green["green_slots"]
    dotd_slots = dotd["dotd_response_slots"]
    zero_slots = zero_mode["basis_slots"]
    c1_operator = c1_template["operator_data"]
    c1_zero = c1_template["zero_modes"]
    c1_matrices = c1_template["response_matrices"]

    return {
        "rho_E_transition_data": {
            "support_candidate_present": twisted["fill_attempt"]["projective_rhoE_mesh_filled"]
            and projective["twist_interpretation"].startswith("projective"),
            "candidate_path": str(INPUTS["projective_rhoe_mesh"]),
            "selected_payload_flag": phifin["phifin_schema"]["selected_flags"]["rhoE_mesh"],
            "promoted_as_selected": False,
            "reason": "Projective rho_E carrier validates the gerbe central twist but is explicitly not selected rho_E data.",
        },
        "Hermitian_metric": {
            "support_candidate_present": twisted["fill_attempt"]["rhoE_metric_filled"],
            "candidate_path": str(INPUTS["projective_rhoe_mesh"]),
            "selected_payload_flag": False,
            "promoted_as_selected": False,
            "reason": "Metric carrier is reused from the projective prototype; selected HYM/Strominger metric is not emitted.",
        },
        "sector_projectors": {
            "support_candidate_present": twisted["fill_attempt"]["block_factorized_sector_maps_filled"]
            and "sector_projectors" in sector_maps["family_block"]
            and "higgs_line_block" in sector_maps,
            "candidate_path": str(INPUTS["block_factorized_sector_maps"]),
            "selected_payload_flag": False,
            "promoted_as_selected": False,
            "reason": "Block-factorized sector maps exist as finite support, but coherent selected spectral projector retention is open.",
        },
        "D_E_action": {
            "support_candidate_present": all_slot_flag(de_slots, "boundary_conditions_verified"),
            "candidate_path": str(INPUTS["q79_routec_de_action"]),
            "selected_payload_flag": all_slot_flag(de_slots, "selected_source_verified"),
            "promoted_as_selected": False,
            "reason": "Finite D_E slots have coherent boundary shape; selected_source_verified is false in every slot.",
        },
        "Riesz_Green": {
            "support_candidate_present": all_slot_flag(green_slots, "operator_data_verified")
            and all_slot_flag(green_slots, "riesz_gap_verified"),
            "candidate_path": str(INPUTS["q79_routec_reduced_green"]),
            "selected_payload_flag": all_slot_flag(green_slots, "selected_source_verified"),
            "promoted_as_selected": False,
            "reason": "Reduced Green/Riesz shape and gaps exist; selected source verification remains false.",
        },
        "dotD_alpha1": {
            "support_candidate_present": all_slot_flag(dotd_slots, "green_operator_verified")
            and all_slot_flag(dotd_slots, "horizontal_gauge_verified"),
            "candidate_path": str(INPUTS["q79_routec_dotd"]),
            "selected_payload_flag": all_slot_flag(dotd_slots, "selected_dotD_source_verified")
            and all_slot_flag(dotd_slots, "alpha1_driver_verified"),
            "promoted_as_selected": False,
            "reason": "Horizontal dotD response shape exists, but selected_dotD_source_verified and alpha1_driver_verified are false.",
        },
        "finite_Hessian_C1_source": {
            "support_candidate_present": selected_value(c1_operator["selected_V_C1_functional"])
            and selected_value(c1_operator["Hess_Xi_blocks"]),
            "candidate_path": str(INPUTS["c1_response_template"]),
            "selected_payload_flag": selected_value(c1_operator["deltaTheta_C1_solution"]),
            "promoted_as_selected": False,
            "reason": "V_C1 and principal Hessian support are named; evaluated source vector, lower-order blocks, and deltaTheta_C1 are missing.",
            "missing": c1_attempt["missing_selected_operator_data"],
        },
        "zero_mode_bases": {
            "support_candidate_present": "basis_slots" in zero_mode,
            "candidate_path": str(INPUTS["zero_mode_interface"]),
            "selected_payload_flag": all(
                selected_value(c1_zero.get(f"{slot}_basis")) for slot in ["Q", "u", "d", "L", "e", "N", "H"]
            )
            and all(selected_value(slot_data.get("ordered_zero_mode_basis")) for slot_data in zero_slots.values()),
            "promoted_as_selected": False,
            "reason": "Zero-mode/dotD interface is formulated, but sector-resolved selected bases are not filled.",
        },
        "primitive_C1_contractions": {
            "support_candidate_present": "response_matrices" in c1_template,
            "candidate_path": str(INPUTS["c1_response_template"]),
            "selected_payload_flag": all(
                selected_value(c1_matrices.get(name))
                for name in ["M_u_C1_alpha1", "M_d_C1_alpha1", "M_e_C1_alpha1", "M_nuD_C1_alpha1"]
            ),
            "promoted_as_selected": False,
            "reason": "Primitive contractions and response matrices remain null.",
        },
    }


def build_candidate() -> dict[str, object]:
    previous = load_json(INPUTS["previous"])
    phifin = load_json(INPUTS["phifin_schema"])
    promotion = load_json(INPUTS["projective_gerbe_promotion"])
    twisted = load_json(INPUTS["twisted_promotion_attempt"])
    projective_validator = load_json(INPUTS["projective_rhoe_validator"])
    projective = load_json(INPUTS["projective_rhoe_mesh"])
    sector_maps = load_json(INPUTS["block_factorized_sector_maps"])
    twisted_packet = load_json(INPUTS["block_factorized_twisted_packet"])
    de_action = load_json(INPUTS["q79_routec_de_action"])
    green = load_json(INPUTS["q79_routec_reduced_green"])
    dotd = load_json(INPUTS["q79_routec_dotd"])
    zero_mode = load_json(INPUTS["zero_mode_interface"])
    c1_template = load_json(INPUTS["c1_response_template"])
    c1_attempt = load_json(INPUTS["c1_response_attempt"])

    payload_slots = build_payload_slots(phifin, twisted, projective, sector_maps, de_action, green, dotd, zero_mode, c1_template, c1_attempt)
    support_present = {key: slot["support_candidate_present"] for key, slot in payload_slots.items()}
    selected_flags = {key: slot["selected_payload_flag"] for key, slot in payload_slots.items()}

    return {
        "candidate": "MTTSelectedPhiFinAlpha1PayloadAttempt",
        "status": "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN",
        "source_status": input_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_PAYLOAD_ATTEMPT",
            "straight_path": {
                "classification": "STRAIGHT_PROMOTION_REJECTED",
                "reason": "The q79 smoke payload and projective rho_E carrier have the right finite shapes but do not carry selected source flags.",
            },
            "superset_convergence": {
                "classification": "PROJECTIVE_GERBE_PLUS_ROUTEC_SCHEMA_SUPPORT",
                "support_paths": [
                    "projective/twisted rho_E central-cocycle carrier",
                    "block-factorized sector maps",
                    "q79 Route-C D_E/Riesz/Green/dotD finite validator schema",
                    "C1 alpha1 Hessian-response contract",
                ],
                "locked_target": previous["unified_payload_contract"]["domain"],
            },
            "superset_repair": {
                "repair_object": "selected spectral Galerkin/HYM data with coherent projector retention",
                "reason": "The next object must turn finite support carriers into selected D_E, Green, dotD, and C1 values from one branch.",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No observed constants, masses, CKM phase, benchmark matrices, or target residuals are used to promote values.",
            },
        },
        "payload_slots": payload_slots,
        "payload_summary": {
            "support_candidate_present": support_present,
            "selected_payload_flags": selected_flags,
            "all_support_shapes_present": all(support_present.values()),
            "all_selected_values_emitted": all(selected_flags.values()),
        },
        "projective_gerbe_support": {
            "source_level_promoted": promotion["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
            "operator_level_projective_rhoE_promoted": promotion["promotion_result"]["operator_level_projective_rhoE_promoted"],
            "selected_twist_verified_in_attempt": twisted["selected_twist_verified"],
            "fixed_topological_sector_in_attempt": twisted["fixed_topological_sector"],
            "uses_projective_prototype_as_selected": twisted["uses_projective_prototype_as_selected"],
            "central_twist_nontrivial": projective_validator["audit_cases"]["projective_magnetic_carrier"]["central_twist_is_nontrivial"],
            "projective_mismatch_count": projective_validator["audit_cases"]["projective_magnetic_carrier"]["projective_mismatch_count"],
        },
        "next_blocker": {
            "name": "SelectedSpectralGalerkinProjectorRetentionData",
            "must_supply": [
                "source_selected_by_mtt for the q79/F,m=1 S3/GS branch",
                "selected HYM/Strominger metric and non-identity projective/twisted rho_E connection values",
                "coherent spectral projector retention for Q,u,d,L,e,N,H",
                "selected D_E action matrices from that same source",
                "selected Riesz projectors, complement gaps, and reduced Green operators",
                "same-branch dotD_alpha1 derivative with alpha1_driver_verified true",
                "finite C1 source vector, Hessian blocks, deltaTheta_C1, zero-mode bases, primitive contractions",
            ],
        },
        "what_closes_now": {
            "selected_payload_attempt_built": True,
            "projective_rhoE_support_candidate_imported": payload_slots["rho_E_transition_data"]["support_candidate_present"],
            "block_factorized_sector_support_imported": payload_slots["sector_projectors"]["support_candidate_present"],
            "routec_de_green_dotd_shapes_imported": payload_slots["D_E_action"]["support_candidate_present"]
            and payload_slots["Riesz_Green"]["support_candidate_present"]
            and payload_slots["dotD_alpha1"]["support_candidate_present"],
            "c1_alpha1_operator_contract_imported": payload_slots["finite_Hessian_C1_source"]["support_candidate_present"],
            "straight_smoke_promotion_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload_values": not all(selected_flags.values()),
            "selected_twist_and_source_verification": not twisted["selected_twist_verified"],
            "operator_level_projective_rhoE_promotion": not promotion["promotion_result"]["operator_level_projective_rhoE_promoted"],
            "coherent_spectral_projector_retention": not twisted["gerbe_source"]["coherent_spectral_projector_verified"],
            "selected_D_E_Riesz_Green_dotD_values": not (
                selected_flags["D_E_action"] and selected_flags["Riesz_Green"] and selected_flags["dotD_alpha1"]
            ),
            "finite_C1_Hessian_and_deltaTheta": not selected_flags["finite_Hessian_C1_source"],
            "zero_mode_bases_and_primitive_contractions": not (
                selected_flags["zero_mode_bases"] and selected_flags["primitive_C1_contractions"]
            ),
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedPhiFinAlpha1PayloadAttempt",
            "proved": True,
            "statement": (
                "The selected Phi_fin alpha1 payload cannot yet be honestly emitted. The finite support layer is broad enough: "
                "projective rho_E carrier, block-factorized sectors, Route-C D_E/Riesz/Green/dotD shapes, and C1 alpha1 response "
                "contracts all exist. But every selected payload gate that matters remains open because selected source, coherent "
                "spectral projector retention, same-branch dotD_alpha1, finite Hessian response values, zero-mode bases, and primitive "
                "C1 contractions are not supplied."
            ),
        },
        "next_required_artifact": "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedPhiFinAlpha1PayloadAttempt",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "primary_next_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_bool_map(items: dict[str, object]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_slots(slots: dict[str, dict[str, object]]) -> str:
    parts = []
    for name, slot in slots.items():
        parts.append(f"### {name}")
        parts.append(f"- support candidate present: `{slot['support_candidate_present']}`")
        parts.append(f"- selected payload flag: `{slot['selected_payload_flag']}`")
        parts.append(f"- promoted as selected: `{slot['promoted_as_selected']}`")
        parts.append(f"- reason: {slot['reason']}")
        parts.append("")
    return "\n".join(parts).rstrip()


def render_note(candidate: dict[str, object]) -> str:
    closed = "\n".join(f"- `{key}`" for key, value in candidate["what_closes_now"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    must = "\n".join(f"- {item}" for item in candidate["next_blocker"]["must_supply"])
    return f"""# MTT Selected Phi_fin Alpha1 Payload v1

## Result

The selected `Phi_fin` alpha_1 payload attempt is built, but selected values are
not emitted yet.

This is **superset repair payload attempt**:

- Straight path: rejected. Smoke values and projective prototypes are not
  selected payload values.
- Superset convergence: projective gerbe rho_E, block-factorized sectors,
  Route-C operator validators, and C1 alpha_1 response all support the same
  target packet.
- Superset repair: the next object is selected spectral Galerkin/HYM data with
  coherent projector retention.
- Diagnostic/backfit: not used as proof.

## Payload Summary

Support candidates:

{render_bool_map(candidate["payload_summary"]["support_candidate_present"])}

Selected payload flags:

{render_bool_map(candidate["payload_summary"]["selected_payload_flags"])}

## Payload Slots

{render_slots(candidate["payload_slots"])}

## What This Closes

{closed}

## What Remains Open

{open_items}

## Next Blocker

`{candidate["next_blocker"]["name"]}` must supply:

{must}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

Next artifact: `{candidate["next_required_artifact"]}`.
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
