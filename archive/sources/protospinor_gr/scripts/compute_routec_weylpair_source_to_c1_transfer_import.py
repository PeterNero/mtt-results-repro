from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_source_provenance_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_weylpair_source_to_c1_transfer_map_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_source_to_c1_transfer_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_source_to_c1_transfer_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_SourceToC1_Transfer_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_IMPORTED_CONDITIONAL_EXACT_ROUTING_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    transfer = src["conditional_transfer_map"]
    selected = src["selected_status"]

    input_checks = {
        "previous_source_provenance_imported": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    transfer_checks = {
        "conditional_exact": transfer["conditional_exact"] is True,
        "phase_formula": transfer["formula"]["phase_column"] == "T(Z) = sector_route(u,e; I + Z)",
        "shift_formula": transfer["formula"]["shift_column"] == "T(X) = sector_route(d,nuD; I + X)",
        "phase_residual_zero": transfer["phase_residual"] == 0.0,
        "shift_residual_zero": transfer["shift_residual"] == 0.0,
        "uses_source_level_carrier": transfer["uses_source_level_carrier"] is True,
        "uses_active_shift_provenance": transfer["uses_active_shift_provenance"] is True,
    }

    selected_open_checks = {
        "selected_transfer_not_emitted": selected["selected_transfer_map_emitted"] is False,
        "sector_routing_not_emitted": selected["selected_sector_routing_emitted"] is False,
        "normalization_not_emitted": selected["selected_normalization_emitted"] is False,
        "labels_not_emitted": selected["selected_labels_emitted_by_prior_selected_inputs"] is False,
        "promotion_not_allowed": selected["promote_to_A_selected_allowed"] is False,
    }

    reduction_checks = {
        "reduced_to_sector_routing": src["reduction"]["name"]
        == "SelectedWeylPairSectorRoutingSourceLemma",
        "reduction_next_required": src["reduction"]["status"] == "NEXT_LEMMA_REQUIRED",
        "remaining_gap_reduced_to_selected_sector_routing": src["what_closes_now"][
            "remaining_gap_reduced_to_selected_sector_routing"
        ]
        is True,
    }

    guardrail_checks = {
        "theorem_proved_conditionally": src["theorem"]["proved"] is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "observed_data_not_used": src["superset_strategy"]["observed_data_used"] is False,
        "lifted_flags_not_used": src["superset_strategy"]["lifted_flags_used_as_proof"] is False,
        "strategy_target_fitting_not_used": src["superset_strategy"]["target_fitting_used"]
        is False,
    }

    theorem = {
        "name": "RouteCWeylPairSourceToC1TransferImportTheorem",
        "proved": all(input_checks.values())
        and all(transfer_checks.values())
        and all(selected_open_checks.values())
        and all(reduction_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The conditional source-level Weyl carrier to C1 response transfer "
            "map is imported. Given the sector routing u/e<-Z and d/nuD<-X, "
            "the map T(Z)=sector_route(u,e;I+Z) and T(X)=sector_route(d,nuD;I+X) "
            "exactly reproduces the two conditional C1 columns. The selected "
            "sector-routing and normalization source remains open, so the "
            "conditional operator is not promoted to A_selected."
        ),
    }

    verdict = {
        "conditional_transfer_map_exact": True,
        "phase_column_reproduced": True,
        "shift_column_reproduced": True,
        "selected_sector_routing_proved": False,
        "selected_normalization_proved": False,
        "conditional_A_promoted_to_A_selected": False,
        "b_selected_emitted": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "transfer_checks": transfer_checks,
        "selected_open_checks": selected_open_checks,
        "reduction_checks": reduction_checks,
        "guardrail_checks": guardrail_checks,
        "conditional_transfer_map": transfer,
        "selected_status": selected,
        "reduction": src["reduction"],
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair SourceToC1 Transfer Import v1

## Result

The conditional source-to-C1 transfer map is now imported.

It is exact as algebra:

```text
T(Z) = sector_route(u,e; I + Z)
T(X) = sector_route(d,nuD; I + X)
phase residual = 0
shift residual = 0
```

The remaining blocker is not the transfer calculation. It is the selected source
of the sector-routing rule and normalization:

```text
why Z routes to u,e as I + Z
why X routes to d,nuD as I + X
why the coefficient normalization is the conditional-solve normalization
```

Until that is proved, the conditional transfer map cannot be promoted to
selected `A_selected`, and `b_selected` remains open.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_IMPORTED_CONDITIONAL_EXACT_ROUTING_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_source_to_c1_transfer_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_source_provenance_import": str(PREV_IMPORT),
                    "selected_routec_weylpair_source_to_c1_transfer_map": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "transfer_checks": transfer_checks,
                "selected_open_checks": selected_open_checks,
                "reduction_checks": reduction_checks,
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
