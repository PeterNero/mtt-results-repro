from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

ASELECTED_IMPORT = ROOT / "certificates" / "routec_weylpair_aselected_assembly_import_certificate.json"
PROV_CERT = SM / "certificates" / "selected_routec_source_provenance_or_basis_certificate_certificate.json"
PROV_DATA = SM / "candidate_data" / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
PHIFIN_BN_CERT = SM / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
PHIFIN_BN_DATA = SM / "candidate_data" / "selected_phifin_payload_or_bn_basis_emission.candidate.json"
R1R4_CERT = SM / "certificates" / "selected_routec_r1_source_or_r4_bn_basis_fill_certificate.json"
R1R4_DATA = SM / "candidate_data" / "selected_routec_r1_source_or_r4_bn_basis_fill.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_source_provenance_or_basis_reduction_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_source_provenance_or_basis_reduction_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Source_Provenance_or_Basis_Reduction_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    aselected = load(ASELECTED_IMPORT)
    prov_cert = load(PROV_CERT)
    prov = load(PROV_DATA)
    phifin_bn_cert = load(PHIFIN_BN_CERT)
    phifin_bn = load(PHIFIN_BN_DATA)
    r1r4_cert = load(R1R4_CERT)
    r1r4 = load(R1R4_DATA)

    closed_now = {
        "conditional_weylpair_A_solve_imported": aselected["verdict"]["conditional_A_weylpair_built"],
        "provenance_support_stack_closed": prov_cert["support_closed"]["provenance_support_closed"],
        "basis_support_stack_closed": prov_cert["support_closed"]["basis_support_closed"],
        "no_hidden_matrix_or_dimension_obstruction": prov_cert["what_closes"]["no_hidden_matrix_or_dimension_obstruction"],
        "phifin_and_bn_emission_contracts_locked": (
            phifin_bn_cert["what_closes"]["selected_phifin_payload_contract_written"]
            and phifin_bn_cert["what_closes"]["selected_bn_basis_contract_written"]
        ),
        "dependency_order_locked": phifin_bn_cert["what_closes"]["dependency_order_locked"],
        "R1_fill_attempt_executed": r1r4_cert["what_closes"]["R1_fill_attempt_executed"],
        "R4_fill_attempt_executed": r1r4_cert["what_closes"]["R4_fill_attempt_executed"],
        "unemitted_selected_primitives_identified": r1r4_cert["what_closes"]["unemitted_selected_primitives_identified"],
        "target_fitting_excluded": (
            prov_cert["what_closes"]["target_fitting_excluded"]
            and phifin_bn_cert["what_closes"]["target_fitting_excluded"]
            and r1r4_cert["what_closes"]["target_fitting_excluded"]
        ),
    }

    still_open = {
        "Phi_fin_selected_payload": prov_cert["what_remains_open"]["Phi_fin_selected_payload"],
        "quotient_valid_BN_basis_certificate": prov_cert["what_remains_open"]["quotient_valid_BN_basis_certificate"],
        "R1_selected_source_certificate": r1r4_cert["what_remains_open"]["R1_selected_source_certificate"],
        "R2_selected_rhoE_metric_connection": r1r4_cert["what_remains_open"]["R2_selected_rhoE_metric_connection"],
        "R3_selected_operator_spectral_data": r1r4_cert["what_remains_open"]["R3_selected_operator_spectral_data"],
        "R4_selected_basis_data": r1r4_cert["what_remains_open"]["R4_selected_basis_data"],
        "R5_selected_C1_response": r1r4_cert["what_remains_open"]["R5_selected_C1_response"],
        "R6_replay_without_lifted_flags": r1r4_cert["what_remains_open"]["R6_replay_without_lifted_flags"],
        "selected_weylpair_source_provenance": aselected["still_open"]["prove_selected_weylpair_source_provenance"],
        "full_SM_or_no_knob_closure": r1r4_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
    }

    theorem = {
        "name": "RouteCSourceProvenanceOrBasisReductionImportTheorem",
        "proved": all(closed_now.values()),
        "statement": (
            "The Weyl-pair A solve has reduced the algebraic problem to source "
            "provenance. The sibling Route-C audits show that provenance and B_N "
            "basis support stacks are closed, but neither R1 selected source nor "
            "R4 selected basis can be filled from current artifacts. The missing "
            "objects are selected Phi_fin payload values or a quotient/deck-valid "
            "B_N basis certificate with selected operator action."
        ),
    }

    verdict = {
        "source_provenance_support_closed": True,
        "basis_support_closed": True,
        "R1_selected_source_closed": False,
        "R4_selected_basis_closed": False,
        "R6_honest_replay_ready": False,
        "selected_weylpair_source_provenance_proved": False,
        "next_required_artifact": "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1",
    }

    guardrails = {
        "does_not_claim_R1_or_R4_closed": True,
        "does_not_claim_A_selected_promoted": True,
        "does_not_claim_source_flags_promoted": True,
        "does_not_claim_honest_replay_ready": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    packet = {
        "theorem": theorem,
        "provenance_gate": prov["provenance_gate"],
        "basis_gate": prov["basis_gate"],
        "phifin_or_bn_contract": {
            "dependency_order": phifin_bn["dependency_order"],
            "closure_vector": phifin_bn["closure_vector"],
            "remaining_parts": phifin_bn["remaining_parts"],
        },
        "R1_source_certificate_attempt": r1r4["R1_source_certificate_attempt"],
        "R4_BN_basis_attempt": r1r4["R4_BN_basis_attempt"],
        "R6_honest_replay": r1r4["R6_honest_replay"],
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = """# Route-C Source Provenance or Basis Reduction Import v1

## Result

The conditional Weyl-pair solve has reduced the algebraic problem to selected
source provenance. The provenance and basis support stacks are closed, but the
actual R1/R4 gates are not.

R1 remains blocked by missing selected `Phi_fin` values from the selected
Strominger/HYM minimizer:

```text
rho_E, metric, connection, sector projectors, D_E, Riesz/Green, dotD,
finite C1 Hessian source, horizontal responses, primitive contractions
```

R4 remains blocked by missing quotient/deck-valid `B_N` basis data:

```text
selected deck/cover, scalar basis, bundle equivariance, metric quadrature,
Gram/stiffness entries, eigenpairs, selected D_E action
```

## Status

```text
ROUTEC_PROVENANCE_BASIS_SUPPORT_CLOSED_SELECTED_PRIMITIVES_OPEN
```

The next legal artifact is:

```text
MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_source_provenance_or_basis_reduction_import",
                "status": "ROUTEC_PROVENANCE_BASIS_SUPPORT_CLOSED_SELECTED_PRIMITIVES_OPEN",
                "input_certificates": {
                    "routec_weylpair_aselected_assembly_import": str(ASELECTED_IMPORT),
                    "selected_routec_source_provenance_or_basis_certificate": str(PROV_CERT),
                    "selected_phifin_payload_or_bn_basis_emission": str(PHIFIN_BN_CERT),
                    "selected_routec_r1_source_or_r4_bn_basis_fill": str(R1R4_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "still_open": still_open,
                "verdict": verdict,
                "guardrails": guardrails,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_PROVENANCE_BASIS_SUPPORT_CLOSED_SELECTED_PRIMITIVES_OPEN")


if __name__ == "__main__":
    main()
