"""Construct the Selected_PhiFin_C1_Emission_Packet_v1 interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

SOURCE_TEMPLATE = CERTS / "selected_routec_c1_operator_source_rebuild.payload.template.json"
ITERATION_CERT = CERTS / "selected_c1_source_promotion_iteration_certificate.json"

OUTPUT_PACKET = DATA / "selected_phifin_c1_emission_packet.template.json"
OUTPUT_CERT = CERTS / "selected_phifin_c1_emission_packet_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_C1_Emission_Packet_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    template = load_json(SOURCE_TEMPLATE)
    iteration = load_json(ITERATION_CERT)
    emission_slots = {
        "S0_selected_source": {
            "origin": "selected Strominger/HYM minimizer on fixed q79/F,m=1 S3/GS sector",
            "fills_template_fields": ["selected_source_certificate"],
            "required_evidence": [
                "selected_by_mtt is theorem-derived",
                "branch is q79/F,m=1 S3/GS Route-C",
                "not fixture_only and not hypothetical_selected",
            ],
            "status": "OPEN",
        },
        "S1_transition_or_connection_trace": {
            "origin": "Phi_fin Cech/Galerkin trace of selected minimizer",
            "fills_template_fields": ["rhoE_or_connection"],
            "required_evidence": [
                "non-identity selected rho_E or equivalent selected connection",
                "metric compatibility",
                "preservation of S3/GS class and branch orientation",
            ],
            "status": "OPEN",
        },
        "S2_operator_blocks": {
            "origin": "same selected connection in the Route-C finite basis",
            "fills_template_fields": ["DE_Riesz_Green_dotD"],
            "required_evidence": [
                "D_E blocks for Q,u,d,L,e,N,H",
                "Riesz projectors and complement gaps",
                "reduced Green operators",
                "dotD_alpha1 matrices from the same branch",
                "finite truncation error controlled by the selected gap",
            ],
            "status": "OPEN",
        },
        "S3_alpha1_source_vector": {
            "origin": "retarded overlap derivative of the same branch",
            "fills_template_fields": ["alpha1.source_vector_b_selected"],
            "required_evidence": [
                "same_branch_driver_verified",
                "b_selected is not borrowed from a benchmark or observed flavor row",
                "nonzero source response where claimed",
            ],
            "status": "OPEN",
        },
        "S4_hessian_and_zero_modes": {
            "origin": "selected Hess_Xi and Galerkin zero-mode basis",
            "fills_template_fields": ["Hess_Xi", "zero_modes"],
            "required_evidence": [
                "finite Hessian blocks emitted",
                "gauge slice specified",
                "selected zero-mode bases emitted",
                "L2 Gram-Schmidt rule fixed from source metric",
            ],
            "status": "OPEN",
        },
        "S5_c1_contractions_and_response": {
            "origin": "primitive C1 overlaps in selected zero-mode basis",
            "fills_template_fields": ["primitive_C1", "sector_response_matrices"],
            "required_evidence": [
                "selected primitive C1 contractions emitted",
                "fiber-class policy fixed",
                "sector response matrices M_u, M_d, M_e, M_nuD emitted",
                "A_selected assembled from emitted response matrices",
            ],
            "status": "OPEN",
        },
    }
    return {
        "packet": "Selected_PhiFin_C1_Emission_Packet_v1",
        "status": "SELECTED_PHIFIN_C1_EMISSION_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        "purpose": (
            "Break the selected-source/C1-rebuild circularity by deriving every required "
            "finite operator slot as the image of one selected Phi_fin source."
        ),
        "source_template": str(SOURCE_TEMPLATE),
        "iteration_certificate": str(ITERATION_CERT),
        "selected_branch": "q79/F,m=1 S3/GS Route-C",
        "template_slots": list(template.keys()),
        "emission_slots": emission_slots,
        "assembly_order": list(emission_slots.keys()),
        "acceptance_tests": iteration["acceptance_tests_for_solution"],
        "closure_predicate": {
            "all_slots_status_closed": False,
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "selected_source_verified_without_lifted_flags": False,
            "routec_validators_pass_honestly": False,
        },
        "forbidden_shortcuts": [
            "copy hypothetical_selected packets into proof data",
            "flip selected_source_verified flags without a source theorem",
            "use observed masses, mixings, gauge constants, or benchmark residuals",
            "use diagnostic non-invariant C1 candidates as selected primitive data",
            "use principal-symbol-only Hess_Xi as finite Hessian blocks",
        ],
        "next_computation": {
            "name": "construct S0-S2 from selected Strominger/HYM Galerkin trace",
            "minimum_new_payload": [
                "selected source certificate",
                "selected rho_E/connection",
                "selected D_E blocks",
                "Riesz gaps and reduced Green operators",
                "same-branch dotD_alpha1",
            ],
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinC1EmissionPacket",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "non_circular_solution_interface_built": True,
            "all_required_payload_slots_named": True,
            "assembly_order_fixed": True,
            "forbidden_shortcuts_explicit": True,
        },
        "what_remains_open": {
            "S0_selected_source": True,
            "S1_transition_or_connection_trace": True,
            "S2_operator_blocks": True,
            "S3_alpha1_source_vector": True,
            "S4_hessian_and_zero_modes": True,
            "S5_c1_contractions_and_response": True,
            "A_selected": True,
            "b_selected": True,
        },
        "next_computation": packet["next_computation"],
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }


def render_note(packet: dict[str, Any], cert: dict[str, Any]) -> str:
    slots = "\n".join(
        f"- `{name}`: {row['origin']} -> {', '.join(row['fills_template_fields'])}"
        for name, row in packet["emission_slots"].items()
    )
    shortcuts = "\n".join(f"- {item}" for item in packet["forbidden_shortcuts"])
    minimum = "\n".join(f"- {item}" for item in packet["next_computation"]["minimum_new_payload"])
    return f"""# Selected PhiFin C1 Emission Packet v1

## Result

The non-circular solution interface is now built, but values are still open.
The packet says exactly what `Phi_fin` must emit before the C1 rebuild may
claim `A_selected` or `b_selected`.

Status: `{packet["status"]}`

## Emission Slots

{slots}

## Assembly Order

```text
{" -> ".join(packet["assembly_order"])}
```

## Forbidden Shortcuts

{shortcuts}

## Next Computation

`{packet["next_computation"]["name"]}`

Minimum new payload:

{minimum}

## Guardrail

This note does not claim selected source construction, `A_selected`, `b_selected`,
or SM closure.  It converts the search result into a finite payload interface.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(packet, cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
