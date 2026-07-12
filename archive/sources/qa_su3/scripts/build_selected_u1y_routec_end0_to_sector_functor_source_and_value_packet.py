"""Build the U1/Y Route-C End0-to-sector functor source/value packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1y_end0_contract": DATA / "selected_u1y_routec_end0_to_sector_functor_value_packet.open.json",
    "u1y_dotd_source_gate": DATA / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing.candidate.json",
    "sm_end0_to_sector_packet": SM / "candidate_data" / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json",
    "sm_sector_realization_functor": SM / "candidate_data" / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json",
    "sm_adjointtriplet_theorem": SM / "candidate_data" / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json",
    "sm_value_fill": SM / "candidate_data" / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json",
    "sm_source_payload_search": SM / "candidate_data" / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json"
OUTPUT_VALUE_PACKET = DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1.md"

STATUS = "U1Y_ROUTEC_END0_TO_SECTOR_VALUE_PACKET_CONSTRUCTED_MODEL_VALUES_ZERO_MODE_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"


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
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
    }


def sector_summary(realization: dict[str, Any]) -> dict[str, Any]:
    validation = realization["validation"]
    return {
        "sector_order": realization["constructed_End0_tensor_product_carrier"]["sector_order"],
        "sector_dimensions": realization["constructed_End0_tensor_product_carrier"]["sector_dimensions"],
        "sector_block_starts": realization["constructed_End0_tensor_product_carrier"]["sector_block_starts"],
        "projector_checks": validation["projector_checks"],
        "projectors_sum_to_identity": validation["projectors_sum_to_identity"],
        "all_distinct_projectors_orthogonal": validation["all_distinct_projectors_orthogonal"],
        "sector_T3_response_norms": validation["sector_T3_response_norms"],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    contract = load(INPUTS["u1y_end0_contract"])
    parent = load(INPUTS["u1y_dotd_source_gate"])
    sm_packet = load(INPUTS["sm_end0_to_sector_packet"])
    realization = load(INPUTS["sm_sector_realization_functor"])
    adjoint = load(INPUTS["sm_adjointtriplet_theorem"])
    value_fill = load(INPUTS["sm_value_fill"])
    source_search = load(INPUTS["sm_source_payload_search"])

    carrier = realization["constructed_End0_tensor_product_carrier"]
    value_packet = {
        "schema": "SelectedU1YRouteCEnd0ToSectorFunctorSourceAndValuePacket.values.v1",
        "status": "MODEL_VALUES_CONSTRUCTED_SELECTED_ZERO_MODE_SOURCE_OPEN",
        "domain": {
            "basis": carrier["selected_domain_basis"],
            "ad_matrices": carrier["domain_ad_matrices"],
            "ad_T3_matrix": carrier["domain_ad_matrices"]["T3"],
            "selected_End0_basis_available": source_search["source_chain"]["selected_End0_adjoint_basis_available"],
        },
        "sector_carrier_model": {
            "construction_rule": carrier["construction_rule"],
            "matter_sectors": carrier["matter_sectors"],
            "higgs_sector": "H",
            "total_dimension": carrier["total_dimension"],
            "rank_match": realization["rank_match"],
            "validation": realization["validation"],
        },
        "sector_projector_model": sector_summary(realization),
        "normalization": {
            "conditional_gram_theorem": value_fill["conditional_gram_normalization_theorem"],
            "raw_T3_frobenius_norm_per_matter_sector": realization["normalization_boundary"]["raw_T3_frobenius_norm_per_matter_sector"],
            "unit_trace_option": realization["normalization_boundary"]["unit_trace_option"],
            "physical_transfer_normalization_selected": False,
        },
        "source_promotion": {
            "conditional_promotion_rule": source_search["conditional_promotion_rule"],
            "source_chain": source_search["source_chain"],
            "promotion_decision": source_search["promotion_decision"],
        },
        "matter_routing": {
            "selected_matter_slot_routing_extracted": False,
            "selected_1M_Dirac_neutrino_rule": False,
            "structural_su5_e6_support_present": realization["matter_slot_routing_boundary"]["structural_su5_e6_support_present"],
            "reason": realization["matter_slot_routing_boundary"]["reason"],
        },
        "honest_replay": {
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
            "selected_End0_to_sector_routing_verified": False,
            "selected_transfer_normalization_verified": False,
            "validator_replay_passes": False,
        },
    }

    decision = {
        "End0_domain_values_filled": True,
        "End0_tensor_product_carrier_constructed": realization["decision"]["End0_tensor_product_carrier_constructed"],
        "sector_projectors_constructed": realization["decision"]["sector_projectors_constructed"],
        "commutator_and_projector_checks_pass": realization["decision"]["commutator_and_projector_checks_pass"],
        "conditional_adjoint_triplet_theorem_proved": adjoint["theorem"]["proved"],
        "conditional_gram_normalization_theorem_proved": value_fill["conditional_gram_normalization_theorem"]["proved"],
        "selected_zero_mode_bases_emitted": False,
        "selected_source_map_emitted": False,
        "selected_sector_zero_mode_realization_extracted": False,
        "selected_matter_slot_routing_extracted": False,
        "selected_1M_Dirac_neutrino_rule": False,
        "selected_transfer_normalization_extracted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "honest_dotD_replay_passes": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCEnd0ToSectorFunctorValuePacketConstructionTheorem",
        "proved": True,
        "statement": (
            "The End0-to-sector value packet can be constructed at the canonical "
            "model level: the selected End0 domain has basis T1,T2,T3, six matter "
            "sectors carry the adjoint triplet action, H is the trivial singlet, "
            "sector projectors are orthogonal/idempotent, and the su(2) bracket "
            "and conditional invariant-Gram normalization checks pass. This is "
            "not yet the physical dotD_alpha1 payload, because no same-source "
            "HYM/projector theorem emits the selected sector zero-mode bases K_s "
            "or selected source map rho_s, and the matter-slot/1_M routing plus "
            "transfer normalization remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCEnd0ToSectorFunctorSourceAndValuePacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_end0_contract": contract,
                "u1y_dotd_source_gate": parent,
                "sm_end0_to_sector_packet": sm_packet,
                "sm_sector_realization_functor": realization,
                "sm_adjointtriplet_theorem": adjoint,
                "sm_value_fill": value_fill,
                "sm_source_payload_search": source_search,
            }.items()
        },
        "value_packet_path": rel(OUTPUT_VALUE_PACKET),
        "decision": decision,
        "constructed_values_summary": {
            "domain_basis": value_packet["domain"]["basis"],
            "ad_T3_matrix": value_packet["domain"]["ad_T3_matrix"],
            "sector_dimensions": value_packet["sector_projector_model"]["sector_dimensions"],
            "rank_match": value_packet["sector_carrier_model"]["rank_match"],
            "sector_T3_response_norms": value_packet["sector_projector_model"]["sector_T3_response_norms"],
        },
        "promotion_blocker": {
            "minimal_new_theorem_needed": source_search["promotion_decision"]["minimal_new_theorem_needed"],
            "why_not_promoted": source_search["promotion_decision"]["why_not_promoted"],
            "proof_obligation_remaining": source_search["conditional_promotion_rule"]["proof_obligation_remaining"],
        },
        "theorem": theorem,
        "what_closes_now": {
            "canonical_End0_domain_values_emitted": True,
            "six_triplet_plus_H_singlet_model_constructed": True,
            "sector_projector_model_constructed": True,
            "su2_commutator_checks_pass": True,
            "conditional_adjoint_triplet_uniqueness_imported": True,
            "conditional_Gram_normalization_imported": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_zero_mode_bases_K_s": True,
            "selected_source_map_rho_s": True,
            "coherent_spectral_zero_mode_projector_retention": True,
            "selected_matter_slot_routing_or_chirality_table": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "selected_transfer_normalization": True,
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
            "claims_physical_dotD_alpha1_payload_extracted": False,
            "claims_selected_zero_mode_bases_emitted": False,
            "claims_selected_source_map_rho_s": False,
            "claims_selected_matter_slot_routing": False,
            "claims_selected_1M_Dirac_neutrino_rule": False,
            "claims_selected_transfer_normalization": False,
            "claims_honest_dotD_replay_passes": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_model_carrier_as_selected_zero_modes": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCEnd0ToSectorFunctorSourceAndValuePacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "value_packet_path": rel(OUTPUT_VALUE_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "End0_domain_values_filled": decision["End0_domain_values_filled"],
        "End0_tensor_product_carrier_constructed": decision["End0_tensor_product_carrier_constructed"],
        "sector_projectors_constructed": decision["sector_projectors_constructed"],
        "commutator_and_projector_checks_pass": decision["commutator_and_projector_checks_pass"],
        "conditional_adjoint_triplet_theorem_proved": decision["conditional_adjoint_triplet_theorem_proved"],
        "conditional_gram_normalization_theorem_proved": decision["conditional_gram_normalization_theorem_proved"],
        "selected_zero_mode_bases_emitted": False,
        "selected_source_map_emitted": False,
        "selected_matter_slot_routing_extracted": False,
        "selected_transfer_normalization_extracted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, value_packet, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    summary = candidate["constructed_values_summary"]
    lines = [
        "# Selected U1Y Route-C End0 to SectorFunctor Source and Value Packet v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"End0_domain_values_filled = {str(cert['End0_domain_values_filled']).lower()}",
        f"End0_tensor_product_carrier_constructed = {str(cert['End0_tensor_product_carrier_constructed']).lower()}",
        f"sector_projectors_constructed = {str(cert['sector_projectors_constructed']).lower()}",
        f"commutator_and_projector_checks_pass = {str(cert['commutator_and_projector_checks_pass']).lower()}",
        f"selected_zero_mode_bases_emitted = {str(cert['selected_zero_mode_bases_emitted']).lower()}",
        f"physical_dotD_alpha1_payload_extracted = {str(cert['physical_dotD_alpha1_payload_extracted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The value packet is now constructed at the canonical model level. It is",
        "not promoted to the selected physical dotD payload until the selected",
        "zero-mode bases and source map are emitted by the same HYM/projector source.",
        "",
        "## Constructed Values",
        "",
        f"- domain basis: `{summary['domain_basis']}`",
        f"- ad(T3): `{summary['ad_T3_matrix']}`",
        f"- sector dimensions: `{summary['sector_dimensions']}`",
        f"- rank match: `{summary['rank_match']}`",
        "",
        "## Promotion Blocker",
        "",
    ]
    for item in candidate["promotion_blocker"]["proof_obligation_remaining"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote the canonical carrier as selected zero-mode bases.",
            "- Do not infer matter-slot routing or the 1_M rule from the carrier alone.",
            "- Do not infer primitive C1, lambda_12, Yukawa, or full SM closure.",
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
    candidate, value_packet, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_VALUE_PACKET.write_text(json.dumps(value_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_VALUE_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
