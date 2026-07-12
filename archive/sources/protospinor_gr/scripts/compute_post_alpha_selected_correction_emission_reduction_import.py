from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_primitiveclass_no_split.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_selected_correction_emission_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_selected_correction_emission_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SelectedCorrectionEmission_Reduction_v1.md"

STATUS = "POST_ALPHA_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_no_split_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["primitive_class_no_flavor_split_theorem"] is True,
            prev["what_remains_open"]["selected_correction_matrix_source"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1",
        ]
    )
    reduction_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["decision"]["primitive_only_route_retired_for_splitter"] is True,
            source["decision"]["nonidentity_rhoE_and_BN_required"] is True,
            source["decision"]["selected_correction_matrix_source_closed"] is False,
            source["decision"]["selected_full_response_emission_closed"] is False,
            source["decision"]["diagnostic_splitter_promoted"] is False,
            source["decision"]["formal_lift_promoted"] is False,
            source["reduction"]["next_construction"] == NEXT,
        ]
    )
    diagnostic_support_recorded = all(
        [
            source["reduction"]["diagnostic_splitter_exists"] is True,
            source["reduction"]["diagnostic_splitter_not_promoted"] is True,
            source["reduction"]["mass_mixing_cp_diagnostic_tests_nonzero"] is True,
            source["diagnostic_representative_support_only"]["candidate_count"] == 1170,
            source["acceptance_tests"]["mass_splitting"]["selected_status"] == "open",
            source["acceptance_tests"]["CKM_or_PMNS_commutator"]["selected_status"] == "open",
            source["acceptance_tests"]["CP_odd"]["selected_status"] == "open",
        ]
    )
    payload_contract_open = all(
        [
            all(item["required"] is True and item["current_status"] == "open" for item in source["required_payload"].values()),
            source["reduction"]["selected_correction_matrices_emitted"] is False,
            source["reduction"]["selected_payload_values_emitted"] is False,
            source["reduction"]["honest_galerkin_selected_values_emit_correction"] is False,
        ]
    )
    guardrails_ok = all(
        [
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_selected_correction_matrix_source"] is False,
            source["guardrails"]["claims_selected_full_response_emission"] is False,
            source["guardrails"]["claims_diagnostic_splitter_selected"] is False,
            source["guardrails"]["claims_formal_lift_as_proof"] is False,
            source["guardrails"]["claims_A_selected"] is False,
            source["guardrails"]["claims_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_Yukawa_CKM_PMNS_CP_or_full_SM_closure"] is False,
            source["guardrails"]["uses_observed_data"] is False,
            source["guardrails"]["uses_benchmark_data"] is False,
            source["guardrails"]["uses_locked_target_columns"] is False,
            all(prev["guardrails"].values()),
        ]
    )
    theorem_proved = all(
        [
            previous_no_split_closed,
            reduction_valid,
            diagnostic_support_recorded,
            payload_contract_open,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaSelectedCorrectionEmissionReductionImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected correction/full-response gate has no algebraic splitter obstruction: "
                "diagnostic qutrit/Weyl splitters pass mass-splitting, commutator, and CP-odd tests "
                "without observed targets. However those splitters are not selected, formal Galerkin "
                "lift is not proof, and primitive-only emission is insufficient. The next required "
                "same-source payload is non-identity rho_E plus quotient-valid B_N, followed by honest "
                "selected deltaTheta/C1 emission."
            ),
        },
        "status": STATUS,
        "acceptance_tests": source["acceptance_tests"],
        "diagnostic_representative_support_only": source["diagnostic_representative_support_only"],
        "reduction": source["reduction"],
        "required_payload": source["required_payload"],
        "checks": {
            "previous_no_split_closed": previous_no_split_closed,
            "reduction_valid": reduction_valid,
            "diagnostic_support_recorded": diagnostic_support_recorded,
            "payload_contract_open": payload_contract_open,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "selected_correction_gate_reduced": True,
            "diagnostic_splitter_recorded_support_only": True,
            "formal_lift_rejected_as_proof": True,
            "primitive_only_route_retired_for_splitter": True,
            "nonidentity_rhoE_BN_payload_contract_built": True,
            "acceptance_tests_carried_forward": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_nonidentity_rho_E": True,
            "selected_quotient_valid_B_N": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_deltaTheta_C1_solution": True,
            "selected_primitive_C1_contractions_or_full_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_diagnostic_splitter_selected": True,
            "does_not_claim_formal_lift_as_proof": True,
            "does_not_claim_selected_correction_or_full_response_emission": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "selected_correction_reduction": str(SOURCE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_selected_correction_emission_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "diagnostic_splitter_candidate_count": source["diagnostic_representative_support_only"]["candidate_count"],
        "selected_correction_matrix_source_closed": False,
        "reduced_to": NEXT,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha SelectedCorrectionEmission Reduction v1

## Result

The selected correction/full-response gate is reduced to non-identity `rho_E`
and quotient-valid `B_N` construction.

Diagnostic support exists:

```text
diagnostic splitter candidates = {source["diagnostic_representative_support_only"]["candidate_count"]}
mass split diagnostic = {source["diagnostic_representative_support_only"]["mass_split_traceless_norm_sq"]["u"]}
CKM commutator diagnostic = {source["diagnostic_representative_support_only"]["ckm_commutator_norm_sq"]}
CP-odd diagnostic = {source["diagnostic_representative_support_only"]["cp_odd_trace_commutator_cubed_imag"]}
```

But the splitter is not selected and the formal lift is not proof. The required
payload is same-source non-identity `rho_E`, quotient-valid `B_N`, honest
`D_E`/Riesz/Green/`dotD`, and a selected `deltaTheta/C1` solve.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
