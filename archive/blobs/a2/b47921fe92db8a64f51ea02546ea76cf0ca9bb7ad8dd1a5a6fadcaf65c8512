from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

PREV_CERT = ROOT / "certificates" / "selected_phifin_alpha1_payload_value_emission_certificate.json"
PREV_PACKET = ROOT / "candidate_data" / "selected_phifin_alpha1_payload_value_emission.packet.json"
SOURCE_DRIVER = (
    NONSM
    / "candidate_data"
    / "selected_dotd_alpha1_source_and_driver_theorem_attempt.candidate.json"
)
DERIVATIVE_PAYLOAD = (
    NONSM
    / "candidate_data"
    / "selected_dotd_alpha1_source_derivative_payload_attempt.candidate.json"
)

OUT_CERT = ROOT / "certificates" / "selected_dotd_alpha1_source_driver_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_dotd_alpha1_source_driver_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_dotD_alpha1_Source_Driver_Reduction_v1.md"

STATUS = "SELECTED_DOTD_ALPHA1_SOURCE_DRIVER_REDUCED_TO_TANGENT_OR_RETARDED_KERNEL"
NEXT = "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev_cert = load(PREV_CERT)
    prev = load(PREV_PACKET)
    source_driver = load(SOURCE_DRIVER)
    derivative = load(DERIVATIVE_PAYLOAD)

    source_driver_attempt_honest = all(
        [
            source_driver["theorem"]["proved"] is False,
            source_driver["requirements"]["R0_selected_D_E_gap_layer"] is True,
            source_driver["requirements"]["R1_selected_projective_rhoE_trace"] is True,
            source_driver["requirements"]["R2_same_basis_dotD_value_packet"] is True,
            source_driver["requirements"]["R3_operator_level_projector_retention_for_dotD"] is False,
            source_driver["requirements"]["R4_selected_alpha1_deformation_parameter"] is False,
            source_driver["requirements"]["R5_retarded_overlap_derivative_source"] is False,
            source_driver["requirements"]["R6_honest_dotD_replay_without_lifted_flags"] is False,
        ]
    )
    derivative_attempt_honest = all(
        [
            derivative["theorem"]["proved"] is False,
            derivative["derivative_payload_checks"]["D0_locked_basis_and_D_E_gap_available"] is True,
            derivative["derivative_payload_checks"]["D1_same_basis_dotD_values_available"] is True,
            derivative["derivative_payload_checks"]["D2_diagnostic_horizontal_response_available"] is True,
            derivative["derivative_payload_checks"]["D3_source_level_projective_support_available"] is True,
            derivative["derivative_payload_checks"]["D4_operator_level_selected_projector_retention_for_dotD"] is False,
            derivative["derivative_payload_checks"]["D5_selected_alpha1_tangent_parameter"] is False,
            derivative["derivative_payload_checks"]["D6_retarded_overlap_derivative_formula"] is False,
            derivative["derivative_payload_checks"]["D7_sector_equality_from_selected_derivative_to_dotD_matrices"] is False,
            derivative["derivative_payload_checks"]["D8_honest_dotD_replay_without_lifted_flags"] is False,
        ]
    )
    previous_prefix_available = all(
        [
            prev_cert["dotD_alpha1_value_matrices_imported"] is True,
            prev["payload_emission_status"][
                "dotD_alpha1_value_matrices_emitted_as_unpromoted_prefix"
            ]
            is True,
            prev["payload_emission_status"]["selected_dotD_source_theorem_proved"] is False,
            prev["payload_emission_status"]["same_branch_alpha1_driver_theorem_proved"] is False,
        ]
    )
    support_not_closure = all(
        [
            derivative["classification"]["not_missing_D_E_gap_or_Green"] is True,
            derivative["classification"]["not_missing_finite_values"] is True,
            derivative["classification"]["not_missing_source_level_S3_gerbe_support"] is True,
            derivative["classification"]["missing_selected_tangent_object"] is True,
            derivative["classification"]["missing_variational_identity"] is True,
            derivative["classification"]["missing_honest_replay_without_lift"] is True,
        ]
    )
    guardrails = all(
        [
            source_driver["guardrails"]["does_not_promote_dotD_flags"] is True,
            source_driver["guardrails"]["does_not_claim_alpha1_driver"] is True,
            source_driver["guardrails"]["does_not_claim_A_selected_or_b_selected"] is True,
            source_driver["guardrails"]["does_not_use_diagnostic_lift_as_proof"] is True,
            derivative["guardrails"]["does_not_treat_support_level_gerbe_as_operator_derivative"]
            is True,
            derivative["guardrails"]["does_not_use_observed_or_benchmark_inputs"] is True,
        ]
    )

    theorem_proved = all(
        [
            previous_prefix_available,
            source_driver_attempt_honest,
            derivative_attempt_honest,
            support_not_closure,
            guardrails,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedDotDAlpha1SourceDriverReduction",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected dotD_alpha1 source and same-branch alpha1 driver "
                "theorem is reduced to one exact missing operator-level object: "
                "a selected alpha1 tangent or retarded-overlap kernel in the "
                "locked q79/F,m=1 F3xF3 B_N basis. Existing finite values, D_E "
                "gap/Green data, projectors, and source-level S3 gerbe support "
                "are not the obstruction."
            ),
        },
        "imported_attempts": {
            "source_driver_attempt_status": source_driver["status"],
            "source_driver_attempt_proved": source_driver["theorem"]["proved"],
            "derivative_payload_attempt_status": derivative["status"],
            "derivative_payload_attempt_proved": derivative["theorem"]["proved"],
        },
        "closed_support": {
            "same_basis_dotD_value_matrices": previous_prefix_available,
            "selected_D_E_gap_layer": source_driver["requirements"]["R0_selected_D_E_gap_layer"],
            "selected_projective_rhoE_trace": source_driver["requirements"][
                "R1_selected_projective_rhoE_trace"
            ],
            "diagnostic_horizontal_response": derivative["derivative_payload_checks"][
                "D2_diagnostic_horizontal_response_available"
            ],
            "source_level_projective_support": derivative["derivative_payload_checks"][
                "D3_source_level_projective_support_available"
            ],
        },
        "exact_missing_object": {
            "name": "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel",
            "description": source_driver["obstruction"]["exact_missing_object"],
            "must_emit": derivative["minimal_closure_contract"]["must_emit"],
        },
        "what_closes_now": {
            "source_driver_attempt_imported": source_driver_attempt_honest,
            "derivative_payload_attempt_imported": derivative_attempt_honest,
            "finite_value_gap_projector_not_obstruction": support_not_closure,
            "selected_tangent_or_kernel_identified_as_cutset": True,
            "no_diagnostic_lift_promotion": guardrails,
        },
        "what_remains_open": {
            "operator_level_selected_projector_retention_for_dotD": True,
            "selected_alpha1_tangent_parameter": True,
            "retarded_overlap_derivative_formula": True,
            "sector_equality_from_selected_derivative_to_dotD_matrices": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "A_selected_and_b_selected": True,
        },
        "guardrails": {
            "does_not_claim_source_driver_theorem": True,
            "does_not_promote_dotD_flags": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "input_artifacts": {
            "previous_packet": str(PREV_PACKET),
            "previous_certificate": str(PREV_CERT),
            "source_driver_attempt": str(SOURCE_DRIVER),
            "derivative_payload_attempt": str(DERIVATIVE_PAYLOAD),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "theorem_proved": theorem_proved,
        "previous_prefix_available": previous_prefix_available,
        "source_driver_attempt_honest": source_driver_attempt_honest,
        "derivative_attempt_honest": derivative_attempt_honest,
        "support_not_closure": support_not_closure,
        "guardrails": guardrails,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_dotd_alpha1_source_driver_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "source_driver_theorem_proved": False,
        "reduced_to": NEXT,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected dotD alpha1 Source Driver Reduction v1

## Result

The selected `dotD_alpha1` source and same-branch alpha1 driver theorem is not
proved yet. It is now reduced to one exact missing operator-level object:

```text
Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel
```

The obstruction is not the finite value layer. We already have same-basis
`dotD_alpha1` matrices, a locked `D_E`/Riesz/Green gap layer, clean projectors,
and source-level S3 gerbe support.

## Boundary

What is still missing is the selected tangent/retarded kernel that proves the
existing matrices are the derivative of the selected PhiFin source, not a
diagnostic source-lift:

```text
operator-level selected projector retention for dotD = open
selected alpha1 tangent parameter = open
retarded-overlap derivative formula = open
sector equality to existing dotD matrices = open
honest dotD replay without lifted flags = open
```

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
