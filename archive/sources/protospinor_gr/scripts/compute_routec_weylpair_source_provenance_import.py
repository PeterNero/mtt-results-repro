from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_frontier_reconciliation_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_weylpair_source_provenance_lemma_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_weylpair_source_provenance_lemma.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_source_provenance_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_source_provenance_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Source_Provenance_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_SOURCE_CARRIER_CLOSED_C1_TRANSFER_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    carrier = src["source_level_weyl_carrier"]
    active = src["active_shift_provenance"]
    transfer = src["c1_transfer_map"]
    lemma = src["lemma_attempt"]

    input_checks = {
        "previous_frontier_reconciled": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    carrier_checks = {
        "carrier_proved": carrier["proved"] is True,
        "g1_is_phase_Z": carrier["carrier_check"]["g1_equals_phase_Z_residual"] <= 1e-10,
        "g1_order3": carrier["carrier_check"]["g1_order3_residual"] <= 1e-9,
        "g2_is_shift_X": carrier["carrier_check"]["g2_equals_shift_X_residual"] <= 1e-10,
        "g2_order3": carrier["carrier_check"]["g2_order3_residual"] <= 1e-10,
        "central_cocycle_imported": carrier["carrier_check"][
            "projective_commutator_residual_imported"
        ]
        <= 1e-12,
        "source_level_selected": carrier["source_level_flags"][
            "source_level_projective_class_selected"
        ]
        is True,
        "operator_level_not_promoted": carrier["source_level_flags"][
            "operator_level_projective_rhoE_promoted"
        ]
        is False,
    }

    active_checks = {
        "active_shift_proved": active["proved"] is True,
        "unique_active_shift_1_1": active["nonzero_active_shifts"] == [[1, 1]],
    }

    transfer_open_checks = {
        "transfer_map_not_emitted": transfer["selected_source_to_C1_response_map_emitted"]
        is False,
        "phase_route_open": transfer["phase_Z_routed_to_u_e_I_plus_Z_column"] is False,
        "shift_route_open": transfer["shift_X_routed_to_d_nuD_I_plus_X_column"] is False,
        "A_selected_not_emitted": transfer["selected_A_selected_currently_emitted"] is False,
        "b_selected_not_emitted": transfer["selected_b_selected_currently_emitted"] is False,
        "normalization_not_transferred": transfer[
            "normalization_transferred_to_deltaTheta_coefficients"
        ]
        is False,
    }

    lemma_checks = {
        "lemma_not_fully_proved": lemma["fully_proved"] is False,
        "proved_sublemma_carrier_and_active_shift": lemma["proved_sublemma"]
        == "SelectedSourceLevelQutritWeylCarrierAndActiveShiftLemma",
        "open_sublemma_transfer_map": lemma["open_sublemma"]
        == "SelectedWeylPairSourceToC1TransferMapLemma",
    }

    guardrail_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "observed_data_not_used": src["superset_strategy"]["observed_data_used"] is False,
        "lifted_flags_not_used": src["superset_strategy"]["lifted_flags_used_as_proof"] is False,
        "strategy_target_fitting_not_used": src["superset_strategy"]["target_fitting_used"]
        is False,
    }

    theorem = {
        "name": "RouteCWeylPairSourceProvenanceImportTheorem",
        "proved": all(input_checks.values())
        and all(carrier_checks.values())
        and all(active_checks.values())
        and all(transfer_open_checks.values())
        and all(lemma_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The selected Route-C Weyl-pair source provenance lemma is imported "
            "as a reduction: the source-level qutrit Weyl carrier is closed "
            "with g1=Z, g2=X, period-three order, selected projective gerbe "
            "cocycle, and active shift (1,1). The full C1 provenance is not "
            "closed because the selected source-to-C1 transfer map has not "
            "been emitted."
        ),
    }

    verdict = {
        "source_level_phase_Z_carrier_provenance_closed": True,
        "source_level_shift_X_carrier_provenance_closed": True,
        "active_shift_1_1_provenance_closed": True,
        "operator_level_C1_transfer_map_emitted": False,
        "conditional_A_promoted_to_A_selected": False,
        "b_selected_emitted": False,
        "honest_selected_deltaTheta_solve_run": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "carrier_checks": carrier_checks,
        "active_checks": active_checks,
        "transfer_open_checks": transfer_open_checks,
        "lemma_checks": lemma_checks,
        "guardrail_checks": guardrail_checks,
        "source_level_weyl_carrier": carrier,
        "active_shift_provenance": active,
        "c1_transfer_map": transfer,
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair Source Provenance Import v1

## Result

The source-level Weyl-pair provenance is now imported.

Closed at source level:

```text
g1 = Z phase generator
g2 = X shift generator
both have order 3
the selected q79/F,m=1 S3/GS gerbe supplies the central cocycle
active shift (1,1) has selected active-shift provenance
```

This is a real reduction: the remaining blocker is not whether the selected
source has the Weyl carrier. It does. The remaining blocker is the transfer map
from that carrier into the exact C1 response columns.

Still open:

```text
Z -> u,e = I + Z phase column
X -> d,nuD = I + X shift column
normalization in the same B_N/projector/dotD/zero-mode basis
promotion of conditional A_weylpair to selected A_selected
emission of b_selected
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_SOURCE_CARRIER_CLOSED_C1_TRANSFER_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_source_provenance_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_frontier_reconciliation": str(PREV_IMPORT),
                    "selected_routec_weylpair_source_provenance_lemma": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "carrier_checks": carrier_checks,
                "active_checks": active_checks,
                "transfer_open_checks": transfer_open_checks,
                "lemma_checks": lemma_checks,
                "guardrail_checks": guardrail_checks,
                "verdict": verdict,
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
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
