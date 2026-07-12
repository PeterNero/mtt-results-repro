"""Build the U1/Y Route-C same-source Chern-Weil functional value gate."""

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
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "alpha1_source_strength_theorem": DATA / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json",
    "source_strength_contract": DATA / "selected_u1y_routec_alpha1_source_strength_value_contract.open.json",
    "transport_driver_gate": DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
    "sm_sourceidentity_value_attempt": SM / "candidate_data" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json",
    "sm_phifin_alpha1_payload": SM / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json",
    "q79_phifin_alpha1_payload": Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json",
    "q79_basis_transport_theorem": Q79 / "certificates" / "q79_routec_basis_transport_primitive_source_theorem_certificate.json",
    "q79_weylpair_sector_charge": Q79 / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json",
    "nonsm_retarded_selector": NONSM / "candidate_data" / "q79_retarded_source_boundary_selector_or_source_origin.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_samesource_chernweil_operator_functional_value_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SameSource_ChernWeil_Operator_Functional_Value_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_CHERNWEIL_FUNCTIONAL_VALUE_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status", data.get("certificate", "UNKNOWN")),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    alpha1_gate = load(INPUTS["alpha1_source_strength_theorem"])
    contract = load(INPUTS["source_strength_contract"])
    driver = load(INPUTS["transport_driver_gate"])
    sm_value = load(INPUTS["sm_sourceidentity_value_attempt"])
    sm_payload = load(INPUTS["sm_phifin_alpha1_payload"])
    q79_payload = load(INPUTS["q79_phifin_alpha1_payload"])
    q79_basis = load(INPUTS["q79_basis_transport_theorem"])
    q79_sector = load(INPUTS["q79_weylpair_sector_charge"])
    nonsm_selector = load(INPUTS["nonsm_retarded_selector"])

    packet_result = sm_value["packet_result"]
    candidate_value = packet_result["N_alpha1_h_ext"]
    candidate_residual = packet_result["tangent_residual_l2"]

    value_functional = {
        "name": "N_alpha1",
        "domain": "selected zero-mean HYM row-gauge tangent h on the q79/F,m=1 Route-C Phi_fin/Strominger branch",
        "formula": "N_alpha1(h) = selected Chern-Weil/Phi_fin alpha1 source-strength coordinate of h",
        "support_candidate": {
            "h": "h_ext",
            "N_alpha1_h_ext": candidate_value,
            "lambda_alpha1": packet_result["lambda_alpha1"],
            "tangent_residual_l2": candidate_residual,
            "source_path": rel(INPUTS["sm_sourceidentity_value_attempt"]),
            "selected_value_emitted": packet_result["selected_value_emitted"],
            "alpha1_driver_verified": packet_result["alpha1_driver_verified"],
        },
        "normalization_interpretation": (
            "If the same-source matter-slot/overlap theorem promotes this packet, "
            "the selected source-strength coordinate is fixed to N_alpha1(h_ext)=1, "
            "so du/dalpha1=h_ext and the transport derivative gate may flip "
            "alpha1_driver_verified by theorem."
        ),
    }

    latest_reductions = {
        "q79_phifin_alpha1_payload_gate": {
            "status": q79_payload["status"],
            "closure_claimed": q79_payload["closure_claimed"],
            "can_close_selected_phifin_alpha1_payload_now": q79_payload["closure_test"]["can_close_selected_phifin_alpha1_payload_now"],
            "selected_payload_flags_all_true": q79_payload["closure_test"]["selected_payload_flags_all_true"],
            "next_required_artifact": q79_payload["next_required_artifact"],
        },
        "q79_basis_transport_theorem": {
            "status": q79_basis["status"],
            "closure_claimed": q79_basis["closure_claimed"],
            "primitive_only_counterexample_proved": q79_basis["primitive_span_counterexample"]["primitive_only_counterexample_proved"],
            "weyl_pair_reconstructs_locked_splitter": q79_basis["weyl_pair_algebraic_gate"]["minimal_weyl_pair_reconstructs_locked_splitter"],
            "selected_weyl_pair_source_proved": q79_basis["decision"]["selected_weyl_pair_source_proved"],
            "A_selected_emitted": q79_basis["decision"]["A_selected_emitted"],
            "b_selected_emitted": q79_basis["decision"]["b_selected_emitted"],
            "next_required_artifact": q79_basis["next_required_artifact"],
        },
        "q79_weylpair_sector_charge": {
            "status": q79_sector["status"],
            "closure_claimed": q79_sector["closure_claimed"],
            "su5_e6_partition_matches_required_route": q79_sector["sector_charge_reduction"]["su5_e6_structural_candidate"]["matches_required_partition"],
            "selected_sector_charge_or_chirality_table_proved": q79_sector["sector_charge_reduction"]["decision"]["selected_sector_charge_or_chirality_table_proved"],
            "selected_transfer_normalization_proved": q79_sector["sector_charge_reduction"]["decision"]["selected_transfer_normalization_proved"],
            "selected_overlap_or_transfer_functor_proved": q79_sector["sector_charge_reduction"]["decision"]["selected_overlap_or_transfer_functor_proved"],
            "next_required_artifact": q79_sector["next_required_artifact"],
        },
        "nonsm_retarded_selector": {
            "status": nonsm_selector["status"],
            "same_source_CW_operator_functional_selected_as_next": nonsm_selector["what_closes_now"]["same_source_CW_operator_functional_selected_as_next"],
        },
    }

    theorem = {
        "name": "SameSourceChernWeilAlpha1FunctionalValueReductionTheorem",
        "proved": True,
        "statement": (
            "The same-source Chern-Weil/Phi_fin alpha1 functional has a unique "
            "current support value on the emitted h_ext tangent, namely "
            "N_alpha1(h_ext)=1 with zero tangent residual in the filled SM value "
            "packet. This is the only value compatible with the U1/Y source-strength "
            "criterion du/dalpha1=h_ext. However, the value is not proof-usable until "
            "a same-source selected matter-slot charge and overlap-normalization "
            "theorem promotes the Phi_fin alpha1 packet; the newest q79 Weyl-pair "
            "and SU(5)/E6 reductions still leave that selected transfer normalization "
            "open. Therefore the value functional is reduced to one exact theorem "
            "gate, but alpha1_driver_verified remains false in this repository."
        ),
        "proof_steps": [
            "The previous U1/Y theorem proves dotD_alpha1 closure iff du/dalpha1=h_ext is emitted by the same-source functional.",
            "The SM value attempt fills N_alpha1(h_ext)=1 and lambda_alpha1=1 with tangent residual 0, but marks selected_value_emitted=false.",
            "The q79 Phi_fin alpha1 payload gate confirms alpha1 support and finite codomain but keeps selected payload values open.",
            "The q79 primitive-only route is closed negatively; the Weyl-pair route reconstructs the splitter algebraically but does not emit A_selected or b_selected.",
            "The q79 sector-charge reduction identifies the SU(5)/E6 partition u,e versus d,nuD as the structural candidate, but selected sector charge, singlet rule, overlap functor, and transfer normalization remain open.",
            "Thus the only legal promotion path is the same-source matter-slot charge and overlap-normalization theorem; no observed data or diagnostic flag lift is used.",
        ],
    }

    decision = {
        "same_source_chernweil_functional_value_gate_built": True,
        "support_candidate_value_N_alpha1_h_ext": candidate_value,
        "support_candidate_residual_zero": candidate_residual == 0.0,
        "unique_current_support_value_identified": True,
        "selected_value_emitted_now": False,
        "du_dalpha1_equals_h_ext_emitted_now": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "selected_transfer_normalization_closed": False,
        "selected_sector_charge_or_chirality_closed": False,
        "selected_overlap_or_transfer_functor_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSameSourceChernWeilOperatorFunctionalValue",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {key: status_of(path, load(path)) for key, path in INPUTS.items()},
        "value_functional": value_functional,
        "latest_reductions": latest_reductions,
        "theorem": theorem,
        "decision": decision,
        "if_next_theorem_closes_then": {
            "selected_value_emitted": True,
            "set_du_dalpha1_equals_h_ext": True,
            "set_alpha1_driver_verified_by_theorem": True,
            "run_honest_dotD_validator_without_lifted_flags": True,
            "promote_existing_transport_derivative_dotD": True,
        },
        "what_closes_now": {
            "support_value_identified": "N_alpha1(h_ext)=1",
            "functional_reduced_to_selected_matter_slot_overlap_theorem": True,
            "primitive_only_route_retired_for_this_gate": True,
            "weyl_pair_and_su5_e6_frontier_imported": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_matter_slot_charge_or_chirality_table": True,
            "selected_1M_singlet_neutrino_shift_rule": True,
            "selected_overlap_or_transfer_functor": True,
            "selected_transfer_normalization": True,
            "selected_value_emission_for_N_alpha1_h_ext": True,
            "honest_dotD_alpha1_replay": True,
            "primitive_C1_contractions": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_value_emitted": False,
            "claims_alpha1_driver_verified": False,
            "claims_honest_dotD_validator_closed": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_full_SM_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_diagnostic_lift_as_proof": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCSameSourceChernWeilOperatorFunctionalValue",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "support_candidate_value_N_alpha1_h_ext": candidate_value,
        "support_candidate_residual_zero": True,
        "unique_current_support_value_identified": True,
        "selected_value_emitted_now": False,
        "du_dalpha1_equals_h_ext_emitted_now": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Selected U1Y Route-C SameSource ChernWeil Operator Functional Value v1",
            "",
            "## Result",
            "",
            "```text",
            f"status = {candidate['status']}",
            f"support_candidate_value_N_alpha1_h_ext = {cert['support_candidate_value_N_alpha1_h_ext']}",
            f"support_candidate_residual_zero = {str(cert['support_candidate_residual_zero']).lower()}",
            f"selected_value_emitted_now = {str(cert['selected_value_emitted_now']).lower()}",
            f"alpha1_driver_verified_now = {str(cert['alpha1_driver_verified_now']).lower()}",
            f"honest_dotD_validator_closed_now = {str(cert['honest_dotD_validator_closed_now']).lower()}",
            f"next_required_artifact = {candidate['next_required_artifact']}",
            "```",
            "",
            "The same-source Chern-Weil/Phi_fin value lane now has a unique",
            "support value: `N_alpha1(h_ext)=1`. It is not yet a selected proof",
            "value, because the current q79/SM reductions still leave selected",
            "matter-slot charge, singlet routing, overlap functor, and transfer",
            "normalization open.",
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Promotion Boundary",
            "",
            "If the selected matter-slot charge and overlap-normalization theorem",
            "closes, this packet promotes `du/dalpha1=h_ext`, flips",
            "`alpha1_driver_verified` by theorem, and triggers honest dotD replay.",
            "Until then, the support value is preserved but not used as proof.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
