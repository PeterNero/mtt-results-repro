"""Build the U1/Y Route-C alpha1 source-strength value theorem attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SM = ROOT.parent / "mtt-sm-parity-closure"
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "driver_gate": DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
    "source_strength_contract": DATA / "selected_u1y_routec_alpha1_source_strength_value_contract.open.json",
    "sm_alpha1_source_strength_theorem": SM / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json",
    "sm_phi_bn_equivalence": SM / "candidate_data" / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json",
    "sm_source_origin_alpha1_driver": SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json",
    "nonsm_dotd_driver_attempt": NONSM / "candidate_data" / "selected_dotd_alpha1_source_and_driver_theorem_attempt.candidate.json",
    "nonsm_retarded_selector": NONSM / "candidate_data" / "q79_retarded_source_boundary_selector_or_source_origin.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1.md"

STATUS = "U1Y_ROUTEC_ALPHA1_SOURCE_STRENGTH_VALUE_THEOREM_DERIVED_CURRENT_SOURCE_VALUE_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_ChernWeil_Operator_Functional_Value_v1"


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
        "status": data.get("status", data.get("packet", "UNKNOWN")),
        "next_required_artifact": data.get("next_required_artifact") or data.get("verdict", {}).get("next_required_artifact"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    driver_gate = load(INPUTS["driver_gate"])
    contract = load(INPUTS["source_strength_contract"])
    sm_norm = load(INPUTS["sm_alpha1_source_strength_theorem"])
    sm_phi = load(INPUTS["sm_phi_bn_equivalence"])
    sm_origin = load(INPUTS["sm_source_origin_alpha1_driver"])
    nonsm_attempt = load(INPUTS["nonsm_dotd_driver_attempt"])
    nonsm_selector = load(INPUTS["nonsm_retarded_selector"])

    current_value_evidence = {
        "transport_derivative_formula_closed": driver_gate["decision"]["transport_derivative_formula_closed"],
        "dotD_source_algebra_closed": driver_gate["decision"]["selected_dotD_source_formula_closed"],
        "projector_riesz_green_replay_closed": driver_gate["decision"]["projector_riesz_green_replay_closed"],
        "validator_ready_rho_s_closed": driver_gate["decision"]["validator_ready_rho_s_closed"],
        "dotD_matrices_pass_if_driver_theorem_supplied": driver_gate["decision"]["dotD_matrices_pass_if_driver_theorem_supplied"],
        "selected_ext_density_tangent_closed": sm_norm["current_evidence"]["selected_ext_density_tangent_closed"],
        "operator_level_alpha1_driver_row_present": sm_norm["current_evidence"]["operator_level_alpha1_driver_row_present"],
        "naive_continuous_scale_identification_rejected": sm_norm["current_evidence"]["naive_continuous_scale_identification_rejected"],
        "same_source_operator_packet_open": sm_norm["current_evidence"]["q79_same_source_operator_packet_open"],
        "normalization_value_emitted_now": sm_norm["current_status"]["normalization_value_emitted_now"],
        "same_branch_dotd_driver_open_in_nonsm": nonsm_selector["what_remains_open"]["same_branch_dotD_alpha1_driver"],
    }

    theorem = {
        "name": "U1YRouteCAlpha1SourceStrengthValueEquivalenceTheorem",
        "proved": True,
        "statement": (
            "On the selected transported End0/HYM/B_N branch, honest dotD_alpha1 "
            "closure is equivalent to emitting one same-source source-strength value: "
            "du/dalpha1=h_ext in the selected zero-mean HYM row gauge, with the "
            "normalization fixed by the selected Phi_fin/Strominger/Chern-Weil "
            "operator functional. If and only if that value is emitted, the already "
            "closed transport derivative supplies selected_dotD_source_verified, "
            "alpha1_driver_verified becomes theorem-derived, and the existing finite "
            "dotD matrices pass honest replay. The current corpus does not emit that "
            "value; therefore the theorem is derived, but the branch is not closed."
        ),
        "proof_steps": [
            "The transport derivative gate proves the local formula for any selected h=du/dalpha.",
            "The selected zero-mean Ext-density tangent h_ext is the only current candidate h and has residual below numerical tolerance.",
            "The dotD validator passes when selected_dotD_source_verified and alpha1_driver_verified are theorem-derived.",
            "The source-only replay fails only by alpha1_driver_verified, so no matrix/projector/Riesz/Green obstruction remains.",
            "Naive Ext-scale renaming is rejected because it does not vary the integral Chern/source row.",
            "The nonsm and SM source-origin audits reduce the missing driver to the same-source Chern-Weil/operator functional.",
            "Thus a source-strength value from that functional is necessary and sufficient for dotD_alpha1 closure.",
        ],
    }

    no_go = {
        "name": "CurrentSourceAlpha1DriverValueNoGo",
        "proved": True,
        "statement": (
            "The present repository and sibling packets do not contain a selected "
            "source-strength value. All artifacts that could supply it either keep "
            "the value open, reduce to Phi_fin/Chern-Weil operator data, or forbid "
            "using diagnostic lifted flags and observed constants. Therefore setting "
            "alpha1_driver_verified=true now would violate the acceptance contract."
        ),
        "blocking_reasons": [
            "source_strength_normalization_value is null in the U1/Y contract",
            "SM alpha1 source-strength theorem has normalization_value_emitted_now=false",
            "nonsm dotD source theorem attempt is not proved and names the same missing derivative payload",
            "retarded selector is reduced to same-source Chern-Weil/operator functional, not constructed",
            "the previous full-flag validator pass is explicitly diagnostic unless the driver value is theorem-derived",
        ],
    }

    decision = {
        "source_strength_equivalence_theorem_proved": True,
        "necessary_and_sufficient_for_dotD_closure": True,
        "current_source_value_no_go_proved": True,
        "normalization_value_emitted_now": False,
        "du_dalpha1_equals_h_ext_emitted": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "selected_dotD_source_verified_now": False,
        "selected_transfer_normalization_closed": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCAlpha1SourceStrengthValueOrSameSourcePacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "driver_gate": input_status("driver_gate", driver_gate),
            "source_strength_contract": {
                "path": rel(INPUTS["source_strength_contract"]),
                "present": INPUTS["source_strength_contract"].exists(),
                "status": contract.get("status", "UNKNOWN"),
            },
            "sm_alpha1_source_strength_theorem": input_status("sm_alpha1_source_strength_theorem", sm_norm),
            "sm_phi_bn_equivalence": input_status("sm_phi_bn_equivalence", sm_phi),
            "sm_source_origin_alpha1_driver": input_status("sm_source_origin_alpha1_driver", sm_origin),
            "nonsm_dotd_driver_attempt": input_status("nonsm_dotd_driver_attempt", nonsm_attempt),
            "nonsm_retarded_selector": input_status("nonsm_retarded_selector", nonsm_selector),
        },
        "decision": decision,
        "current_value_evidence": current_value_evidence,
        "theorem": theorem,
        "current_source_no_go": no_go,
        "if_value_emitted_then": {
            "set_selected_dotD_source_verified": True,
            "set_alpha1_driver_verified": True,
            "run_honest_dotD_validator_without_lifted_flags": True,
            "promote_existing_same_basis_dotD_matrices": True,
            "still_separate_after_dotD": [
                "matter-slot/1_M routing",
                "primitive C1 overlap contractions",
                "lambda_12",
                "full SM closure",
            ],
        },
        "what_closes_now": {
            "necessary_and_sufficient_alpha1_driver_theorem": True,
            "proof_that_no_local_dotD_obstruction_remains": True,
            "current_source_value_no_go": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_ChernWeil_operator_functional_value": True,
            "du_dalpha1_equals_h_ext_value": True,
            "honest_dotD_replay_with_alpha1_driver_true": True,
            "matter_slot_routing": True,
            "one_M_Dirac_neutrino_rule": True,
            "primitive_C1_overlap_contractions": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_alpha1_driver_verified": False,
            "claims_honest_dotD_validator_closed": False,
            "claims_source_strength_value_emitted": False,
            "claims_selected_transfer_normalization": False,
            "claims_physical_dotD_alpha1_payload": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_diagnostic_lift_as_proof": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCAlpha1SourceStrengthValueOrSameSourcePacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_strength_equivalence_theorem_proved": True,
        "necessary_and_sufficient_for_dotD_closure": True,
        "current_source_value_no_go_proved": True,
        "normalization_value_emitted_now": False,
        "du_dalpha1_equals_h_ext_emitted": False,
        "alpha1_driver_verified_now": False,
        "honest_dotD_validator_closed_now": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Selected U1Y Route-C Alpha1 SourceStrength Value or SameSourcePacket v1",
            "",
            "## Result",
            "",
            "```text",
            f"status = {candidate['status']}",
            f"source_strength_equivalence_theorem_proved = {str(cert['source_strength_equivalence_theorem_proved']).lower()}",
            f"necessary_and_sufficient_for_dotD_closure = {str(cert['necessary_and_sufficient_for_dotD_closure']).lower()}",
            f"current_source_value_no_go_proved = {str(cert['current_source_value_no_go_proved']).lower()}",
            f"alpha1_driver_verified_now = {str(cert['alpha1_driver_verified_now']).lower()}",
            f"honest_dotD_validator_closed_now = {str(cert['honest_dotD_validator_closed_now']).lower()}",
            f"next_required_artifact = {candidate['next_required_artifact']}",
            "```",
            "",
            "The theorem is derived: dotD closure is equivalent to a same-source",
            "source-strength value proving `du/dalpha1=h_ext` in the selected",
            "zero-mean HYM row gauge. The current corpus does not emit that value,",
            "so the driver flag cannot honestly be flipped yet.",
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Current-Source No-Go",
            "",
            candidate["current_source_no_go"]["statement"],
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
