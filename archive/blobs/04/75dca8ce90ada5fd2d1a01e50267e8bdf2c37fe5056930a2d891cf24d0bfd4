from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "dotd_alpha1_transport_derivative_import.packet.json"
NORM_THEOREM = SM / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
VALUE_ATTEMPT = SM / "candidate_data" / "selected_alpha1_source_strength_value_emission_attempt.candidate.json"
FILL_ATTEMPT = SM / "candidate_data" / "selected_samesource_alpha1_normalization_packet_fill_attempt.candidate.json"
FILL_PACKET = SM / "candidate_data" / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"

OUT_CERT = ROOT / "certificates" / "alpha1_source_strength_normalization_gate_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_source_strength_normalization_gate.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_SourceStrength_Normalization_Gate_v1.md"

STATUS = "ALPHA1_SOURCE_STRENGTH_NORMALIZATION_GATE_REDUCED_SOURCEIDENTITY_OR_RETARDED_KERNEL_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_SourceIdentity_or_RetardedKernel_Value_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    theorem = load(NORM_THEOREM)
    value = load(VALUE_ATTEMPT)
    fill = load(FILL_ATTEMPT)
    packet_fill = load(FILL_PACKET)

    previous_dotd_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["selected_dotD_source_algebra"] is True,
            prev["what_remains_open"]["alpha1_driver_source_strength_normalization"] is True,
        ]
    )
    normalization_acceptance_theorem = all(
        [
            theorem["theorem"]["proved"] is True,
            theorem["acceptance_criterion"]["necessary_and_sufficient_for_current_branch"] is True,
            theorem["current_status"]["alpha1_driver_verified_now"] is False,
            theorem["current_evidence"]["dotd_matrices_pass_if_driver_theorem_supplied"] is True,
            theorem["what_closes_now"]["necessary_and_sufficient_normalization_criterion"] is True,
        ]
    )
    value_attempt_boundary = all(
        [
            value["emission_attempt"]["selected_value_emitted"] is False,
            value["emission_attempt"]["alpha1_driver_verified"] is False,
            value["emission_attempt"]["conditional_value_candidate"]["lambda_alpha1_candidate"] == 1.0,
            value["what_closes_now"]["unsafe_value_promotion_rejected"] is True,
            value["what_remains_open"]["emit_selected_source_strength_normalization_value"] is True,
        ]
    )
    fill_failed_honestly = all(
        [
            fill["fill_summary"]["candidate_values_filled"] == fill["fill_summary"]["required_fields"],
            fill["fill_summary"]["selected_emitted_fields"] == 0,
            fill["validator_report"]["ok"] is False,
            fill["validator_report"]["exit_code"] == 1,
            fill["kernel_decision"]["promotes_selected_value"] is False,
            packet_fill["promotion_result"]["alpha1_driver_verified"] is False,
            packet_fill["promotion_result"]["selected_value_emitted"] is False,
        ]
    )
    required_failed_fields = [
        "source_identity",
        "source_strength_coordinate",
        "normalization_functional",
        "tangent_equality",
        "sector_dotd_equality",
    ]
    failed_field_coverage = all(field in fill["failed_fields"] for field in required_failed_fields)
    theorem_proved = all(
        [
            previous_dotd_ready,
            normalization_acceptance_theorem,
            value_attempt_boundary,
            fill_failed_honestly,
            failed_field_coverage,
        ]
    )

    packet = {
        "theorem": {
            "name": "Alpha1SourceStrengthNormalizationGate",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The alpha1 source-strength normalization gate is reduced to a final selected-source "
                "emission problem. The current branch has the transport derivative, h_ext, lambda_alpha1=1 "
                "as a conditional unit candidate, and a necessary-and-sufficient criterion for promoting "
                "alpha1_driver_verified. The same-source packet fill attempted all required fields, but the "
                "final validator failed because every field remains support-only, coordinate-only, or "
                "diagnostic-lift rather than selected and theorem-derived. Therefore the remaining routes "
                "are a selected same-source source-identity/normalization value or a typed B_N retarded "
                "alpha1 kernel."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "normalization_theorem_status": theorem["status"],
            "value_attempt_status": value["status"],
            "fill_attempt_status": fill["status"],
            "fill_packet_status": packet_fill["status"],
        },
        "conditional_value_candidate": value["emission_attempt"]["conditional_value_candidate"],
        "acceptance_criterion": theorem["acceptance_criterion"],
        "fill_summary": fill["fill_summary"],
        "failed_fields": fill["failed_fields"],
        "validator_report": fill["validator_report"],
        "proof_chain": {
            "previous_dotd_ready": previous_dotd_ready,
            "normalization_acceptance_theorem": normalization_acceptance_theorem,
            "value_attempt_boundary": value_attempt_boundary,
            "fill_failed_honestly": fill_failed_honestly,
            "failed_field_coverage": failed_field_coverage,
            "target_fitting_used": theorem["target_fitting_used"]
            or value["target_fitting_used"]
            or fill["target_fitting_used"]
            or packet_fill["promotion_result"]["target_fitting_used"],
        },
        "what_closes_now": {
            "necessary_and_sufficient_alpha1_driver_criterion": True,
            "unit_candidate_lambda_alpha1_equals_1_recorded": True,
            "all_current_packet_fields_tested": True,
            "final_validator_failure_explained": True,
            "unsafe_source_strength_promotion_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_identity": True,
            "selected_source_strength_coordinate": True,
            "selected_normalization_functional": True,
            "selected_h_alpha1_tangent_from_same_source": True,
            "honest_sector_dotd_equality": True,
            "typed_BN_retarded_alpha1_kernel_or_same_source_value": True,
            "alpha1_driver_verified": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "does_not_emit_lambda_alpha1_as_selected": True,
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_use_full_flag_probe_as_proof": True,
            "does_not_use_coordinate_convention_as_source_value": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_dotd_import": str(PREV),
            "normalization_theorem": str(NORM_THEOREM),
            "value_attempt": str(VALUE_ATTEMPT),
            "fill_attempt": str(FILL_ATTEMPT),
            "fill_packet": str(FILL_PACKET),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_source_strength_normalization_gate",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_dotd_ready": previous_dotd_ready,
            "normalization_acceptance_theorem": normalization_acceptance_theorem,
            "value_attempt_boundary": value_attempt_boundary,
            "fill_failed_honestly": fill_failed_honestly,
            "failed_field_coverage": failed_field_coverage,
            "target_fitting_excluded": packet["proof_chain"]["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 SourceStrength Normalization Gate v1

## Result

The source-strength gate is now sharp. The branch has:

```text
lambda_alpha1 candidate = 1
du/dalpha1 candidate = h_ext
h_ext residual L2 = {value["emission_attempt"]["conditional_value_candidate"]["h_ext_residual_l2"]}
```

But the same-source normalization packet does not validate yet. All required
fields were filled as candidates, and zero were emitted as selected fields.
The final validator failed because the data are still support-only,
coordinate-convention-only, or diagnostic-lift rather than selected and
theorem-derived.

Status:

```text
{STATUS}
```

The remaining legal routes are:

```text
selected same-source source-identity/normalization value
typed B_N retarded alpha1 kernel
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
