from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

REPOS = {
    "current": ROOT,
    "nonsm": TEXPAPERS / "mtt-nonsm-constants-no-knob",
    "q79": TEXPAPERS / "mtt-q79-proof-repro",
    "qa_su3": TEXPAPERS / "mtt-qa-su3-packet-proof",
    "sm_parity": TEXPAPERS / "mtt-sm-parity-closure",
}

INPUTS = {
    "current_einstein_assembly": ("current", "certificates/one_anchor_einstein_response_assembly_certificate.json"),
    "current_stress_gate": ("current", "certificates/physical_normalization_stress_response_gate_certificate.json"),
    "current_gr_tt_identity_gate": ("current", "certificates/gr_tt_exact_branch_identity_final_gate_certificate.json"),
    "current_noise_gate": ("current", "certificates/gr_tt_character_channel_identification_stress_test_certificate.json"),
    "nonsm_dimensionful_obstruction": ("nonsm", "certificates/dimensionful_constant_obstruction_certificate.json"),
    "qa_su3_minimal_hsel_gret": ("qa_su3", "certificates/minimal_hsel_gret_finite_galerkin_candidate_certificate.json"),
    "qa_su3_chi_qa": ("qa_su3", "certificates/selected_response_functional_chi_qa_certificate.json"),
    "sm_projective_gerbe_rhoe": ("sm_parity", "certificates/projective_gerbe_rhoe_source_promotion_certificate.json"),
    "sm_phifin_alpha1_payload": ("sm_parity", "certificates/selected_phifin_alpha1_payload_certificate.json"),
    "q79_selected_full_sm_data": ("q79", "certificates/selected_full_sm_data_theorem_attempt_certificate.json"),
    "q79_matter_two_paths": ("q79", "certificates/selected_matter_source_two_path_exploration_certificate.json"),
}

OUT_CERT = ROOT / "certificates" / "cross_repo_remaining_gates_source_triage_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Cross_Repo_Remaining_Gates_Source_Triage_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "cross_repo_remaining_gates_source_triage.packet.json"


def load_json(repo_key: str, rel_path: str) -> dict:
    path = REPOS[repo_key] / rel_path
    return json.loads(path.read_text(encoding="utf-8"))


def repo_path(repo_key: str, rel_path: str) -> str:
    return str(REPOS[repo_key] / rel_path)


def main() -> None:
    docs = {name: load_json(*locator) for name, locator in INPUTS.items()}

    gate_triage = {
        "absolute_SI_metrology": {
            "classification": "CONFIRMED_OPEN",
            "best_source": "mtt-nonsm-constants-no-knob dimensionful obstruction",
            "evidence_status": docs["nonsm_dimensionful_obstruction"]["status"],
            "why": docs["nonsm_dimensionful_obstruction"]["verdict"]["next_required_object"],
            "promote_to_closed": False,
        },
        "selected_full_matter_stress_coefficients": {
            "classification": "PARTIAL_SOURCE_REDUCTION_OPEN",
            "best_source": "q79 plus sm-parity selected source/Phi_fin alpha1 chain",
            "q79_status": docs["q79_selected_full_sm_data"]["status"],
            "q79_matter_strategy": docs["q79_matter_two_paths"]["recommended_strategy"],
            "sm_payload_status": docs["sm_phifin_alpha1_payload"]["status"],
            "why": "SM/source repos reduce the target to selected payload, projector, D_E/Riesz/Green/dotD, and C1 values; they do not emit selected matter-stress coefficients.",
            "promote_to_closed": False,
        },
        "unconditional_GR_TT_operator_identity": {
            "classification": "CURRENT_REPO_BEST_GATE_OPEN",
            "best_source": "current exact-branch GR identity gate",
            "evidence_status": docs["current_gr_tt_identity_gate"]["status"],
            "why": "The current repo closes exact-branch support and the conditional TT response, while preserving the full-GR operator-identity gap.",
            "promote_to_closed": False,
        },
        "literal_GR_TT_noise_channel_identity": {
            "classification": "OPTIONAL_STRENGTHENING_OPEN",
            "best_source": "current GR TT character-channel stress test plus Qa/SU3 finite response patterns",
            "current_status": docs["current_noise_gate"]["status"],
            "qa_su3_status": docs["qa_su3_chi_qa"]["status"],
            "why": "The repos align on shared exact Z64/q64 retarded infrastructure, but do not identify the GR TT response plane with the literal stochastic covariance line.",
            "promote_to_closed": False,
        },
    }

    useful_imports = {
        "finite_retarded_kernel_patterns": {
            "repo": "mtt-qa-su3-packet-proof",
            "minimal_hsel_gret_status": docs["qa_su3_minimal_hsel_gret"]["status"],
            "chi_qa_status": docs["qa_su3_chi_qa"]["status"],
            "what_can_be_used": [
                "finite selected Hessian/retarded-kernel packet discipline",
                "retarded trace pairing pattern",
                "guardrail that finite candidates are not full smooth/operator closure",
            ],
            "what_cannot_be_used": "direct substitution as GR matter-stress or full smooth GR operator coefficients",
        },
        "selected_source_support_chain": {
            "repo": "mtt-sm-parity-closure",
            "rhoe_status": docs["sm_projective_gerbe_rhoe"]["status"],
            "payload_status": docs["sm_phifin_alpha1_payload"]["status"],
            "what_can_be_used": [
                "selected S3/source support",
                "Freed-Witten/block-projector/visible-GS support",
                "Phi_fin alpha1 payload interface shape",
            ],
            "what_cannot_be_used": "numeric selected Phi_fin alpha1 payload values or matter stress coefficients",
        },
        "full_sm_data_blocker": {
            "repo": "mtt-q79-proof-repro",
            "full_sm_status": docs["q79_selected_full_sm_data"]["status"],
            "matter_source_status": docs["q79_matter_two_paths"]["status"],
            "recommended_strategy": docs["q79_matter_two_paths"]["recommended_strategy"],
            "first_blocker": docs["q79_matter_two_paths"]["verdict"]["remaining_first_blocker"],
        },
    }

    no_missed_closed_proof = all(not row["promote_to_closed"] for row in gate_triage.values())
    best_next_gate = "selected_full_matter_stress_coefficients"
    next_executable_artifact = "Selected_Matter_Payload_Import_Interface_v1"

    verdict = {
        "all_relevant_sibling_repos_checked": True,
        "missed_closed_remaining_gate_found": False,
        "best_next_gate": best_next_gate,
        "next_executable_artifact": next_executable_artifact,
        "safe_to_claim_full_GR_or_full_SM_closure": False,
        "safe_to_use_sibling_source_support": True,
        "safe_to_import_numeric_matter_coefficients": False,
    }

    guardrails = {
        "does_not_claim_selected_matter_coefficients": True,
        "does_not_claim_absolute_SI_metrology": True,
        "does_not_claim_unconditional_GR_TT_identity": True,
        "does_not_claim_literal_noise_identity": True,
        "does_not_use_observed_masses_or_Newton_as_inputs": True,
        "does_not_promote_benchmark_or_template_packets": True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "cross_repo_remaining_gates_source_triage",
        "status": "CROSS_REPO_REMAINING_GATES_TRIAGED_BEST_NEXT_GATE_SELECTED_MATTER_PAYLOAD",
        "repositories_checked": {key: str(path) for key, path in REPOS.items()},
        "input_certificates": {name: repo_path(*locator) for name, locator in INPUTS.items()},
        "gate_triage": gate_triage,
        "useful_imports": useful_imports,
        "no_missed_closed_proof": no_missed_closed_proof,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    packet = {
        "gate_triage": gate_triage,
        "useful_imports": useful_imports,
        "best_next_gate": best_next_gate,
        "next_executable_artifact": next_executable_artifact,
    }

    note = f"""# Cross-Repo Remaining Gates Source Triage v1

## Result

The four proof repositories adjacent to this one were checked for the remaining
GR-response gates:

```text
mtt-nonsm-constants-no-knob
mtt-q79-proof-repro
mtt-qa-su3-packet-proof
mtt-sm-parity-closure
```

No missed closed theorem was found for the remaining gates. The scan is useful
because it narrows the next move: the best gate to attack is the selected matter
payload/stress map, not another ad hoc normalization shortcut.

## Gate Classification

```text
absolute SI metrology:
  confirmed open by the dimensionful-constant obstruction certificate

selected full matter stress coefficients:
  partially reduced by q79 and sm-parity source work, but still open

unconditional GR TT operator identity:
  current repo remains the best gate; no sibling proof closes it

literal GR TT noise-channel identity:
  optional strengthening open; shared exact Z64 infrastructure is not literal
  identity of the GR TT response plane and the covariance character line
```

## Useful Imports

Qa/SU3 supplies finite selected Hessian and retarded-kernel patterns. These are
good templates for validator discipline, but they cannot be substituted as GR
matter coefficients.

SM-parity supplies selected S3/source support, projective gerbe rhoE promotion,
Freed-Witten/block-projector/visible-GS support, and the Phi_fin alpha1 payload
interface. It still does not emit selected payload values.

q79 supplies the exact warning we need: full SM data are not proved until the
selected overlap kernels, metrics, neutral sector, Higgs data, and matching data
are computed from the same branch.

## Next Artifact

```text
{next_executable_artifact}
```

It should define the exact import interface from the q79/sm-parity selected
source chain into this GR repo's stress-response gate, and it must keep all
numeric selected matter coefficients open until actual payload values exist.
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: CROSS_REPO_REMAINING_GATES_TRIAGED_BEST_NEXT_GATE_SELECTED_MATTER_PAYLOAD")


if __name__ == "__main__":
    main()
