"""Build selected finite packet emission for heterotic projective rho_E."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "finite_quotient_theorem": DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json",
    "finite_quotient_obligations": DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_remaining_obligations.json",
    "representative_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "minimal_finite_galerkin": DATA / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json",
    "chi_qa": DATA / "selected_response_functional_chi_qa.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SelectedPacketEmission_or_OperatorIdentity_v1.md"
OUTPUT_PACKET = DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_SELECTED_FINITE_PACKET_EMITTED_SMOOTH_OPERATOR_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_EQa_or_ThresholdFinitePart_v1"

LABELS = ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def diag(values: list[int]) -> list[list[int]]:
    return [[value if i == j else 0 for j in range(len(values))] for i, value in enumerate(values)]


def main() -> dict[str, Any]:
    finite_quotient = load(INPUTS["finite_quotient_theorem"])
    obligations = load(INPUTS["finite_quotient_obligations"])
    representatives = load(INPUTS["representative_tables"])
    finite = load(INPUTS["minimal_finite_galerkin"])
    chi_qa = load(INPUTS["chi_qa"])

    finite_values = representatives["projective_representative_tables"]["fills_finite_candidate_leaves"]
    tau = finite_values["tau_values"]
    tau_vector = [tau[label] for label in LABELS]

    finite_operator_packet = {
        "schema": "SelectedHeteroticProjectiveRhoEFiniteInternalOperatorPacket.v1",
        "scope": "selected_finite_internal_Qa_SU3_projective_response_only",
        "selected": True,
        "selected_because": [
            "the finite physical quotient theorem closes the selected domain as exactly F_i,G_i,P",
            "the representative-table source identity emits the finite Galerkin branch selection rule",
            "the minimal Galerkin proof validates H_sel, G_ret, Pi_tw, and tau on that same domain",
            "chi_Qa fixes the finite trace/admissibility normalization without observed data",
        ],
        "labels": LABELS,
        "tau_vector": tau_vector,
        "tau_values": tau,
        "rho_E_central_character": {
            label: f"exp(2*pi*i*{tau[label]}/3)" for label in LABELS
        },
        "D_E_diagonal_matrix_on_labels": diag(tau_vector),
        "H_sel": finite["hessian"]["matrix"],
        "Green_operator": finite_values["Green_operator"],
        "Riesz_projector": finite_values["Riesz_projector"],
        "Pi_tw": finite["selection_proof"]["selected_covector"],
        "dotD": finite_values["dotD"],
        "finite_trace": finite_values["finite_part"],
        "chi_Qa": chi_qa["decision"]["selected_chi_Qa"],
        "trace_normalization": finite_values["trace_normalization"],
        "target_fitting_used": False,
    }

    emission_checks = {
        "finite_domain_selected": finite_quotient["decision"]["finite_physical_quotient_domain_closed"],
        "finite_trace_admissibility_closed": finite_quotient["decision"]["finite_trace_admissibility_closed"],
        "representative_finite_candidate_built": representatives["decision"]["finite_projective_candidate_built"],
        "same_labels": finite_operator_packet["labels"] == finite_quotient["expected_labels"],
        "tau_matches_finite_galerkin": tau == finite["tau"]["values"],
        "green_inverse_validated": finite["green"]["inverse_verified"],
        "chi_Qa_closed": chi_qa["decision"]["selected_chi_Qa"] == "1",
        "no_target_fitting": not finite_quotient["target_fitting_used"] and not representatives["target_fitting_used"] and not chi_qa["target_fitting_used"],
    }

    selected_finite_packet_emitted = all(emission_checks.values())
    remaining = {
        "schema": "SelectedHeteroticProjectiveRhoEAfterFinitePacketEmissionRemaining.v1",
        "status": "OPEN",
        "finite_contract_remaining_before_this_artifact": obligations["missing"],
        "finite_rhoE_packet_selected_not_validator_only": selected_finite_packet_emitted,
        "still_open": {
            "smooth_Deligne_Cech_transition_matrices": True,
            "same_source_smooth_operator_identity": True,
            "E_Qa_or_Weitzenbock_zero_order_block": True,
            "heat_zeta_torsion_threshold_finite_part": True,
            "physical_threshold_value": True,
        },
        "next_required_artifact": NEXT,
    }

    decision = {
        "selected_finite_internal_packet_emitted": selected_finite_packet_emitted,
        "finite_rhoE_packet_selected_not_validator_only": selected_finite_packet_emitted,
        "smooth_rhoE_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "full_heterotic_threshold_closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESelectedPacketEmissionOrOperatorIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "finite_quotient_theorem": finite_quotient["status"],
            "representative_tables": representatives["status"],
            "minimal_finite_galerkin": finite["status"],
            "chi_qa": chi_qa["status"],
        },
        "selected_finite_operator_packet_path": rel(OUTPUT_PACKET),
        "emission_checks": emission_checks,
        "decision": decision,
        "remaining_after_emission": remaining,
        "guardrails": {
            "does_not_claim_smooth_transition_matrices": True,
            "does_not_claim_smooth_Deligne_Cech_representative": True,
            "does_not_claim_E_Qa": True,
            "does_not_claim_physical_threshold_value": True,
            "does_not_import_q79_or_observed_values": True,
            "does_not_use_target_fitting": True,
        },
        "theorem": {
            "name": "SelectedFiniteProjectiveRhoEPacketEmission",
            "proved": selected_finite_packet_emitted,
            "statement": (
                "At the selected finite internal Qa/SU3 quotient scope, the projective "
                "rho_E packet is no longer merely a validator candidate: the selected "
                "finite domain F_i,G_i,P, the finite Galerkin selection proof, the "
                "representative-table source rule, and chi_Qa trace normalization jointly "
                "emit rho_E central characters, D_E, Riesz, Green, dotD, and finite trace "
                "convention as selected finite operator data. This does not emit smooth "
                "heterotic transition matrices, E_Qa, or the physical threshold finite part."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_PACKET.write_text(json.dumps(finite_operator_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_finite_operator_packet_path": rel(OUTPUT_PACKET),
        "selected_finite_internal_packet_emitted": selected_finite_packet_emitted,
        "finite_rhoE_packet_selected_not_validator_only": selected_finite_packet_emitted,
        "smooth_rhoE_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "full_heterotic_threshold_closure_claimed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SelectedPacketEmission or OperatorIdentity v1

## Result

```text
status = {STATUS}
selected_finite_internal_packet_emitted = {str(selected_finite_packet_emitted).lower()}
smooth_rhoE_transition_tables_emitted = false
E_Qa_computed = false
threshold_value_computed = false
next_required_artifact = {NEXT}
```

## Closed Here

The finite `rho_E/D_E` packet is now selected at the internal finite quotient
scope, not merely retained as a validator candidate. The selected packet is:

```text
{rel(OUTPUT_PACKET)}
```

It emits:

- `rho_E` central characters on `F_i,G_i,P`;
- finite diagonal `D_E`;
- `H_sel`, `G_ret`, Riesz projector, `Pi_tw`, and `dotD`;
- finite trace convention and `chi_Qa=1`.

## Still Open

This is not yet a smooth heterotic operator identity. The next gate is to emit
the threshold operator finite part:

```text
{NEXT}
```

That object must supply `E_Qa` or an equivalent Weitzenbock/heat/zeta/torsion
finite part for the selected finite packet without target fitting.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
