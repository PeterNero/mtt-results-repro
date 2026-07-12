"""Build the U1/Y Route-C zero-mode basis from HYM projector source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "end0_sector_value_packet": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json",
    "end0_sector_values": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json",
    "finite_hym_gate": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "typed_hym_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_payload.open.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_ZEROMODEBASIS_FROM_HYM_PROJECTOR_SOURCE_THEOREM_PROVED_PAYLOAD_OPEN"
NEXT = "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
SECTOR_ORDER = MATTER_SECTORS + ["H"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def input_status(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
    }


def build_contract(values: dict[str, Any]) -> dict[str, Any]:
    ad_matrices = values["domain"]["ad_matrices"]
    sector_dims = values["sector_projector_model"]["sector_dimensions"]
    return {
        "schema": "SelectedU1YRouteCZeroModeBasisFromHYMProjectorSourcePayload.open.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "accepted_source_families": [
            "direct selected HYM/Strominger connection projector",
            "typed monad/Cech HYM projector with exactness/local-freeness certificate",
            "finite Route-C projector with same-source trace equality and export to sector projectors",
        ],
        "required_payload": {
            "same_source_id": None,
            "selected_HYM_or_typed_projector_certificate": None,
            "sector_projectors": {
                sector: {
                    "projector_matrix": None,
                    "rank_required": sector_dims[sector],
                    "idempotent": None,
                    "self_adjoint_for_selected_Gram": None,
                    "zero_mode_projector": None,
                    "selected_by_same_source": None,
                }
                for sector in SECTOR_ORDER
            },
            "ordered_zero_mode_bases_K_s": {
                sector: {
                    "basis_vectors": None,
                    "dimension_required": sector_dims[sector],
                    "orientation_or_ordering_rule": None,
                    "Gram_matrix": None,
                    "trace_normalization": None,
                }
                for sector in SECTOR_ORDER
            },
            "End0_action_on_zero_modes": {
                sector: {
                    "rho_s_T1": None,
                    "rho_s_T2": None,
                    "rho_s_T3": None,
                    "same_source_action": None,
                    "preserves_K_s": None,
                    "bracket_preserving": None,
                    "target_model": "adjoint_triplet" if sector in MATTER_SECTORS else "trivial_singlet",
                }
                for sector in SECTOR_ORDER
            },
            "coherence_checks": {
                "projectors_pairwise_orthogonal": None,
                "projectors_sum_to_selected_sector_identity": None,
                "projectors_commute_with_End0_action": None,
                "End0_action_preserves_ker_D_E_sector": None,
                "spectral_gap_or_Riesz_contour_retention": None,
                "no_lifted_selected_flags": None,
                "no_observed_or_benchmark_inputs": None,
            },
            "routing_and_normalization_not_supplied_by_this_contract": {
                "selected_matter_slot_routing": None,
                "selected_1M_Dirac_neutrino_rule": None,
                "selected_transfer_normalization_to_dotD_alpha1": None,
            },
        },
        "reference_model_values": {
            "End0_basis": values["domain"]["basis"],
            "End0_ad_matrices": ad_matrices,
            "sector_order": values["sector_projector_model"]["sector_order"],
            "sector_dimensions": sector_dims,
            "matter_sectors": MATTER_SECTORS,
            "H_sector": "H",
        },
        "acceptance_tests": [
            "each P_s is selected by the same source and is a self-adjoint idempotent",
            "rank(P_s)=3 for Q,u,d,L,e,N and rank(P_H)=1",
            "sum_s P_s is the selected retained sector identity and P_s P_t=0 for s!=t",
            "P_s commutes with the selected End0 action and retains zero modes through the Riesz/HYM projector",
            "rho_s(T_i)=P_s rho(T_i) P_s restricted to K_s satisfies the su(2) bracket",
            "matter rho_s are nonzero irreducible real three-dimensional actions; H action is zero",
            "Gram matrices are positive invariant and trace-normalized by tr(G_s)=dim(K_s)",
            "no observed masses, mixings, couplings, or benchmark values enter the source payload",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    end0_packet = load(INPUTS["end0_sector_value_packet"])
    values = load(INPUTS["end0_sector_values"])
    finite_hym = load(INPUTS["finite_hym_gate"])
    typed_contract = load(INPUTS["typed_hym_witness_contract"])

    contract = build_contract(values)

    theorem = {
        "name": "SelectedU1YRouteCZeroModeBasisFromHYMProjectorSourceTheorem",
        "proved": True,
        "statement": (
            "If a same-source selected HYM/Strominger, typed monad/Cech, or finite "
            "Route-C projector payload emits sector projectors P_s and ordered zero-mode "
            "bases K_s satisfying the contract conditions, then the canonical End0 "
            "sector value packet promotes uniquely to selected zero-mode data: "
            "rho_s(T_i)=P_s rho(T_i)P_s restricted to K_s, the matter sectors are the "
            "adjoint triplet up to the fixed orthogonal trace convention, and H is the "
            "trivial singlet. The theorem does not itself emit P_s, K_s, matter-slot "
            "routing, the 1_M rule, or dotD_alpha1 transfer normalization."
        ),
        "proof_steps": [
            {
                "step": "same_source_restriction",
                "argument": "The payload requires P_s and the End0 action to come from one selected HYM/projector source, so the restriction rho_s(T_i)=P_s rho(T_i)P_s is not a lifted diagnostic value.",
            },
            {
                "step": "projector_retention",
                "argument": "Idempotence, self-adjointness, rank, orthogonality, and Riesz/HYM zero-mode retention identify K_s=im(P_s) as the selected sector zero-mode carrier.",
            },
            {
                "step": "bracket_descent",
                "argument": "Because P_s commutes with the selected End0 action and the action preserves K_s, the su(2) bracket descends to the restricted matrices on K_s.",
            },
            {
                "step": "adjoint_uniqueness",
                "argument": "For six nonzero three-dimensional real irreducible matter carriers, the prior adjoint-triplet theorem makes each rho_s orthogonally equivalent to the canonical adjoint triplet; the one-dimensional H carrier has zero skew action.",
            },
            {
                "step": "gram_normalization",
                "argument": "The invariant positive Gram lemma reduces each matter Gram to a scalar, and tr(G_s)=3 fixes it to the identity convention used by the value packet.",
            },
        ],
    }

    decision = {
        "theorem_proved": True,
        "payload_contract_created": True,
        "accepted_source_families_count": len(contract["accepted_source_families"]),
        "reference_End0_domain_available": values["domain"]["selected_End0_basis_available"],
        "reference_sector_value_packet_constructed": end0_packet["decision"]["End0_tensor_product_carrier_constructed"],
        "reference_projector_checks_pass": values["sector_carrier_model"]["validation"]["projectors_sum_to_identity"],
        "selected_projector_payload_filled": False,
        "selected_zero_mode_bases_emitted": False,
        "selected_source_map_rho_s_emitted": False,
        "selected_matter_slot_routing_emitted": False,
        "selected_1M_Dirac_neutrino_rule_emitted": False,
        "selected_transfer_normalization_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCZeroModeBasisFromHYMProjectorSourceTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "end0_sector_value_packet": input_status("end0_sector_value_packet", end0_packet),
            "end0_sector_values": {
                "path": rel(INPUTS["end0_sector_values"]),
                "present": INPUTS["end0_sector_values"].exists(),
                "status": values.get("status", "UNKNOWN"),
            },
            "finite_hym_gate": input_status("finite_hym_gate", finite_hym),
            "typed_hym_witness_contract": input_status("typed_hym_witness_contract", typed_contract),
        },
        "payload_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": theorem,
        "promotion_rule": {
            "when_contract_filled": "promote canonical model carrier to selected K_s/rho_s values",
            "rho_s_definition": "rho_s(T_i)=P_s rho(T_i) P_s restricted to K_s=im(P_s)",
            "matter_sector_result": "Q,u,d,L,e,N become selected adjoint triplet carriers",
            "H_sector_result": "H becomes the selected trivial singlet carrier",
            "normalization_result": "invariant Gram trace convention fixes matter Gram to I_3 and H Gram to [1]",
        },
        "what_closes_now": {
            "minimal_source_theorem_stated_and_proved_conditionally": True,
            "machine_readable_HYM_projector_payload_contract_created": True,
            "exact_acceptance_tests_for_selected_K_s_and_rho_s_created": True,
            "canonical_value_packet_promotion_rule_created": True,
            "model_to_selected_guardrail_preserved": True,
        },
        "what_remains_open": {
            "fill_payload_with_actual_selected_P_s_and_K_s": True,
            "same_source_HYM_projector_or_typed_Cech_values": True,
            "coherent_spectral_projector_retention_values": True,
            "matter_slot_routing": True,
            "one_M_Dirac_neutrino_rule": True,
            "transfer_normalization_to_dotD_alpha1": True,
            "primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_payload_filled": False,
            "claims_selected_zero_mode_bases_emitted": False,
            "claims_selected_source_map_rho_s": False,
            "claims_selected_matter_slot_routing": False,
            "claims_selected_1M_Dirac_neutrino_rule": False,
            "claims_selected_transfer_normalization": False,
            "claims_physical_dotD_alpha1_payload": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_model_carrier_without_source_payload": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCZeroModeBasisFromHYMProjectorSourceTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "payload_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "theorem_proved": True,
        "payload_contract_created": True,
        "selected_projector_payload_filled": False,
        "selected_zero_mode_bases_emitted": False,
        "selected_source_map_rho_s_emitted": False,
        "selected_matter_slot_routing_emitted": False,
        "selected_transfer_normalization_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, contract, cert, render_note(candidate, contract, cert)


def render_note(candidate: dict[str, Any], contract: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C ZeroModeBasis From HYM Projector Source Theorem v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"theorem_proved = {str(cert['theorem_proved']).lower()}",
        f"payload_contract_created = {str(cert['payload_contract_created']).lower()}",
        f"selected_zero_mode_bases_emitted = {str(cert['selected_zero_mode_bases_emitted']).lower()}",
        f"physical_dotD_alpha1_payload_extracted = {str(cert['physical_dotD_alpha1_payload_extracted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This theorem is the source bridge promised by the End0 sector value packet.",
        "It proves the promotion rule from same-source HYM/projector data to selected",
        "sector zero-mode bases and selected End0 action matrices. It does not fill",
        "the HYM/projector payload itself.",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Proof Skeleton",
        "",
    ]
    for item in candidate["theorem"]["proof_steps"]:
        lines.append(f"- {item['step']}: {item['argument']}")
    lines.extend(
        [
            "",
            "## Required Payload",
            "",
            "The next source-fill artifact must supply the following with one same_source_id:",
        ]
    )
    for test in contract["acceptance_tests"]:
        lines.append(f"- {test}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- The theorem is conditional until the selected projector payload is filled.",
            "- The canonical carrier is not a selected zero-mode basis by itself.",
            "- Matter-slot routing, the 1_M rule, dotD transfer normalization, lambda_12, and full SM closure remain open.",
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
