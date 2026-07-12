from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

STRESS_GATE = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
TRIAGE = ROOT / "certificates" / "cross_repo_remaining_gates_source_triage_certificate.json"
PHIFIN_PAYLOAD = SM_PARITY / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
FULL_SM = Q79 / "certificates" / "selected_full_sm_data_theorem_attempt_certificate.json"
MATTER_VALIDATOR = Q79 / "certificates" / "selected_matter_slot_transversality_source_validator_certificate.json"
HYM_VALIDATOR = Q79 / "certificates" / "selected_hym_operator_source_validator_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_matter_payload_import_interface_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Matter_Payload_Import_Interface_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "selected_matter_payload_import_interface.template.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    stress = load(STRESS_GATE)
    triage = load(TRIAGE)
    phifin = load(PHIFIN_PAYLOAD)
    full_sm = load(FULL_SM)
    matter_validator = load(MATTER_VALIDATOR)
    hym_validator = load(HYM_VALIDATOR)

    required_slots = {
        "selected_source_branch": {
            "purpose": "prove all payload values come from the same q79/F,m=1 S3/GS branch",
            "source_status": phifin["next_blocker"]["must_supply"][0],
            "filled": False,
        },
        "selected_sector_projectors_and_zero_modes": {
            "purpose": "retain Q,u,d,L,e,N,H matter sectors under coherent spectral projection",
            "source_status": "coherent spectral projector retention and zero-mode bases are open",
            "filled": False,
        },
        "selected_DE_Riesz_Green_dotD": {
            "purpose": "provide the selected differential operator and retarded Green response data",
            "source_status": "D_E, Riesz/Green, and dotD shapes exist as support candidates; selected values are open",
            "filled": False,
        },
        "finite_C1_Hessian_deltaTheta": {
            "purpose": "compute finite C1 source vector, Hessian blocks, and deltaTheta response",
            "source_status": "finite C1 Hessian and deltaTheta values are open",
            "filled": False,
        },
        "primitive_overlap_contractions": {
            "purpose": "emit the primitive overlap tensors that become raw channel weights and stress coefficients",
            "source_status": "primitive C1 contractions remain null/open",
            "filled": False,
        },
        "family_kinetic_metrics": {
            "purpose": "canonicalize raw matter payloads before stress-response import",
            "source_status": "K_Q,K_u,K_d,K_L,K_e,K_N and Higgs normalization are open",
            "filled": False,
        },
        "neutral_higgs_matching_data": {
            "purpose": "keep the matter payload compatible with full SM closure rather than only charged Yukawa blocks",
            "source_status": "neutral-sector, Higgs boundary, and RG/threshold matching are open",
            "filled": False,
        },
    }

    stress_import_map = {
        "scalar_sector": {
            "needs": ["selected_sector_projectors_and_zero_modes", "family_kinetic_metrics", "primitive_overlap_contractions"],
            "stress_form_available": stress["stress_response"]["matter_examples_closed_as_forms"],
            "coefficients_available": False,
        },
        "yang_mills_sector": {
            "needs": ["selected_source_branch", "selected_DE_Riesz_Green_dotD", "family_kinetic_metrics"],
            "stress_form_available": stress["stress_response"]["matter_examples_closed_as_forms"],
            "coefficients_available": False,
        },
        "dirac_yukawa_sector": {
            "needs": [
                "selected_sector_projectors_and_zero_modes",
                "finite_C1_Hessian_deltaTheta",
                "primitive_overlap_contractions",
                "family_kinetic_metrics",
            ],
            "stress_form_available": stress["stress_response"]["matter_examples_closed_as_forms"],
            "coefficients_available": False,
        },
        "neutral_higgs_threshold_sector": {
            "needs": ["neutral_higgs_matching_data", "family_kinetic_metrics"],
            "stress_form_available": stress["stress_response"]["matter_examples_closed_as_forms"],
            "coefficients_available": False,
        },
    }

    readiness = {
        "universal_stress_forms_ready": stress["stress_response"]["matter_examples_closed_as_forms"],
        "selected_source_support_shapes_present": phifin["payload_summary"]["all_support_shapes_present"],
        "selected_payload_values_emitted": phifin["payload_summary"]["all_selected_values_emitted"],
        "matter_slot_validator_formulated": matter_validator["verdict"]["validator_formulated"],
        "hym_operator_validator_formulated": hym_validator["verdict"]["validator_formulated"],
        "selected_matter_stress_import_ready": False,
    }

    blocked_by = [
        name for name, slot in required_slots.items() if not slot["filled"]
    ]

    verdict = {
        "interface_built": True,
        "selected_matter_payload_import_closed": False,
        "selected_matter_stress_coefficients_closed": False,
        "full_SM_closure_claim_allowed": False,
        "full_GR_response_claim_allowed": False,
        "next_required_object": "SelectedSpectralGalerkinProjectorRetentionData_or_SelectedHYMOperatorPayloadValues",
        "blocked_by": blocked_by,
    }

    guardrails = {
        "does_not_promote_support_candidates_to_selected_values": True,
        "does_not_use_benchmark_or_observed_flavor_inputs": True,
        "does_not_claim_full_SM_data": full_sm["attempt_result"]["safe_to_claim_theorem"] is False,
        "does_not_claim_selected_matter_stress_coefficients": True,
        "keeps_universal_stress_form_separate_from_selected_coefficients": True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_matter_payload_import_interface",
        "status": "SELECTED_MATTER_PAYLOAD_IMPORT_INTERFACE_BUILT_VALUES_OPEN",
        "input_certificates": {
            "physical_normalization_stress_response_gate": str(STRESS_GATE),
            "cross_repo_remaining_gates_source_triage": str(TRIAGE),
            "selected_phifin_alpha1_payload_candidate": str(PHIFIN_PAYLOAD),
            "selected_full_sm_data_theorem_attempt": str(FULL_SM),
            "selected_matter_slot_transversality_source_validator": str(MATTER_VALIDATOR),
            "selected_hym_operator_source_validator": str(HYM_VALIDATOR),
        },
        "required_slots": required_slots,
        "stress_import_map": stress_import_map,
        "readiness": readiness,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    template = {
        "candidate": "SelectedMatterPayloadImportInterfaceTemplate",
        "instructions": "Fill only with same-branch selected q79/F,m=1 S3/GS source values. Do not use observed masses, CKM data, Newton/Planck data, or benchmark matrices.",
        "required_slots": {
            key: {
                "filled": False,
                "source_certificate": None,
                "values": None,
                "validation_status": "OPEN",
            }
            for key in required_slots
        },
        "stress_import_map": stress_import_map,
    }

    note = """# Selected Matter Payload Import Interface v1

## Result

The next remaining gate has been turned into an executable interface.

The GR repo already has the universal variational stress form:

```text
T_{mu nu} = -2/sqrt(-g) * delta S_matter / delta g^{mu nu}
```

What is missing is not the stress-tensor definition. What is missing is the
same-branch selected matter payload that supplies the scalar, Yang-Mills, Dirac,
Yukawa, neutral/Higgs, and matching coefficients that feed that definition.

## Required Payload

```text
selected source branch
selected sector projectors and zero-mode bases
selected D_E, Riesz/Green, and dotD values
finite C1 Hessian blocks and deltaTheta response
primitive overlap contractions
family kinetic metrics
neutral-sector, Higgs, and matching data
```

The q79 and sm-parity repos provide support shapes and validators for these
objects. They do not yet emit the selected values.

## What This Closes

This closes the interface between the selected matter/source program and the GR
stress-response program. It tells us exactly what must be imported before the
selected full matter stress coefficient gate can close.

## What Remains Open

The template in:

```text
candidate_data/selected_matter_payload_import_interface.template.json
```

must be filled with selected same-branch values. Until then, the universal
stress forms are closed, but the selected matter stress coefficients are open.
"""

    OUT_PACKET.write_text(json.dumps(template, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: SELECTED_MATTER_PAYLOAD_IMPORT_INTERFACE_BUILT_VALUES_OPEN")


if __name__ == "__main__":
    main()
