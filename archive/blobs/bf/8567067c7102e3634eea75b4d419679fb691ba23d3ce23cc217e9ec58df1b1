from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

REDUCTION_IMPORT = ROOT / "certificates" / "routec_source_provenance_or_basis_reduction_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_selected_primitive_emission_search_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_selected_primitive_emission_search.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_selected_primitive_emission_search_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_selected_primitive_emission_search_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Selected_Primitive_Emission_Search_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    reduction = load(REDUCTION_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    results = src["search_results"]
    straight = src["superset_mode"]["straight_path"]

    closed_now = {
        "previous_reduction_support_closed": reduction["theorem"]["proved"],
        "primitive_search_executed": src_cert["what_closes"]["primitive_search_executed"],
        "selected_deck_scaffold_identified": src_cert["what_closes"]["selected_deck_scaffold_identified"],
        "formal_lift_rejected_as_proof": src_cert["what_closes"]["formal_lift_rejected_as_proof"],
        "identity_rhoE_rejected_as_selected_payload": src_cert["what_closes"]["identity_rhoE_rejected_as_selected_payload"],
        "R1_R4_not_promoted_by_existing_artifacts": src_cert["what_closes"]["R1_R4_not_promoted_by_existing_artifacts"],
        "target_fitting_excluded": src["target_fitting_used"] is False,
    }

    blockers = {
        "Phi_fin_selected_payload_not_emitted": (
            results["Phi_fin_payload"]["selected_values_emitted"] is False
            and results["Phi_fin_payload"]["minimum_payload_fields_still_null"] is True
        ),
        "identity_rhoE_is_unselected_smoke": (
            results["Phi_fin_payload"]["identity_smoke_rejected"] is True
            and results["Phi_fin_payload"]["selected_by_mtt"] is False
        ),
        "B_N_basis_payload_not_emitted": (
            results["B_N_basis"]["minimum_basis_payload_fields_still_null"] is True
            and results["B_N_basis"]["required_success_gates_pass"] is False
        ),
        "selected_deck_is_partial_scaffold_only": (
            results["B_N_basis"]["selected_deck_map_present"] is True
            and results["B_N_basis"]["selected_deck_is_partial_execution_scaffold"] is True
        ),
        "formal_lift_can_validate_but_cannot_promote": (
            results["formal_lift_diagnostic"]["can_validate_downstream_algebra"] is True
            and results["formal_lift_diagnostic"]["promotion_allowed"] is False
        ),
        "straight_R1_R4_R6_path_blocked": (
            straight["R1_promotes"] is False
            and straight["R4_promotes"] is False
            and straight["R6_ready"] is False
        ),
    }

    theorem = {
        "name": "RouteCSelectedPrimitiveEmissionSearchImportTheorem",
        "proved": all(closed_now.values()) and all(blockers.values()),
        "statement": (
            "The selected primitive emission search has been imported. Existing "
            "artifacts contain selected-deck scaffolding and diagnostic formal-lift "
            "algebra, but no legal selected Phi_fin payload and no quotient-valid "
            "B_N basis payload. R1/R4/R6 therefore remain honestly open."
        ),
    }

    verdict = {
        "selected_primitives_found": False,
        "R1_promotes": False,
        "R4_promotes": False,
        "R6_ready": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    guardrails = {
        "does_not_promote_formal_lift": True,
        "does_not_promote_identity_rhoE": True,
        "does_not_claim_B_N_selected_basis": True,
        "does_not_claim_R1_R4_R6_closed": True,
        "does_not_use_target_fitting": True,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "search_results": results,
        "superset_mode": src["superset_mode"],
        "closed_now": closed_now,
        "blockers": blockers,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Selected Primitive Emission Search Import v1

## Result

The selected primitive emission search has been imported from the sibling
Route-C/SM proof repository.

It closes the question of whether the current artifacts merely needed wiring:
they do not. The selected deck scaffold exists and formal-lift algebra can
validate downstream shapes, but neither is legal selected proof data.

Still absent:

```text
selected Phi_fin payload values
selected non-identity rho_E payload
quotient/deck-valid B_N scalar basis payload
selected operator action and quadrature
honest R6 replay without lifted flags
```

## Status

```text
ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND
```

The next required artifact is:

```text
MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_selected_primitive_emission_search_import",
                "status": "ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND",
                "input_certificates": {
                    "routec_source_provenance_or_basis_reduction_import": str(REDUCTION_IMPORT),
                    "selected_routec_selected_primitive_emission_search": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "blockers": blockers,
                "what_remains_open": src["what_remains_open"],
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
    print("STATUS: ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND")


if __name__ == "__main__":
    main()
