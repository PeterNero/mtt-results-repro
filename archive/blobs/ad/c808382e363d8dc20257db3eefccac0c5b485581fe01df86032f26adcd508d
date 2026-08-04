from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_source_to_c1_transfer_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_weylpair_sector_routing_source_lemma_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_sector_routing_source_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_sector_routing_source_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_SectorRouting_Source_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_SECTOR_ROUTING_IMPORTED_LOCKED_TARGET_UNIQUE_SOURCE_CERT_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    routing = src["routing_search"]
    current = src["current_selected_support"]
    lemma = src["lemma_attempt"]

    input_checks = {
        "previous_transfer_imported": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    routing_checks = {
        "six_two_two_routes_enumerated": len(routing["all_two_two_partitions_tested"]) == 6,
        "locked_target_selects_route": routing["target_columns_select_route"] is True,
        "one_exact_route_relative_to_locked_columns": len(routing["exact_rows_relative_to_locked_columns"])
        == 1,
        "exact_route_is_u_e_vs_d_nuD": routing["exact_rows_relative_to_locked_columns"][0][
            "phase_route"
        ]
        == ["u", "e"]
        and routing["exact_rows_relative_to_locked_columns"][0]["shift_route"] == ["d", "nuD"],
        "source_does_not_independently_select_route": routing[
            "source_data_independently_selects_route"
        ]
        is False,
    }

    support_checks = {
        "conditional_transfer_exact": current["conditional_transfer_exact"] is True,
        "sector_projectors_built": current["sector_projectors_built"] is True,
        "family_kernel_dimension_three_retained": current["family_kernel_dimension_three_retained"]
        is True,
        "selected_dotD_source_open": current["selected_dotD_source_verified_open"] is True,
        "alpha1_driver_open": current["alpha1_driver_verified_open"] is True,
        "representations_required_data": all(
            value == "SELECTED_SOURCE_DATA_REQUIRED"
            for value in current["representation_source_data_required"].values()
        ),
    }

    lemma_checks = {
        "lemma_not_fully_proved": lemma["fully_proved"] is False,
        "proved_by_locked_columns": lemma["proved_by_locked_columns"] is True,
        "not_proved_by_selected_source": lemma["proved_by_selected_source"] is False,
        "next_certificate_named": src["next_certificate"]["name"]
        == "SelectedWeylPairSectorChargeOrChiralityCertificate",
        "next_certificate_has_four_requirements": len(src["next_certificate"]["must_supply"]) == 4,
    }

    guardrail_checks = {
        "external_inspiration_not_proof": src["external_research_inspiration"]["used_as_proof"]
        is False,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "target_fitting_excluded": src["what_closes_now"]["target_fitting_excluded"] is True,
    }

    theorem = {
        "name": "RouteCWeylPairSectorRoutingSourceImportTheorem",
        "proved": all(input_checks.values())
        and all(routing_checks.values())
        and all(support_checks.values())
        and all(lemma_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The Weyl-pair sector-routing attempt is imported as a reduction. "
            "All two-two routes of {u,d,e,nuD} were enumerated; relative to the "
            "locked C1 columns, the intended routing Z->u/e and X->d/nuD is "
            "unique. This does not prove selected source routing, because current "
            "selected data do not independently emit the sector charge, chirality, "
            "or conjugation table that forces the partition."
        ),
    }

    verdict = {
        "all_two_two_routes_enumerated": True,
        "locked_columns_pick_intended_route_uniquely": True,
        "selected_source_sector_routing_proved": False,
        "selected_sector_charge_or_chirality_certificate_emitted": False,
        "conditional_A_promoted_to_A_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "routing_checks": routing_checks,
        "support_checks": support_checks,
        "lemma_checks": lemma_checks,
        "guardrail_checks": guardrail_checks,
        "routing_search": routing,
        "current_selected_support": current,
        "next_certificate": src["next_certificate"],
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair SectorRouting Source Import v1

## Result

The sector-routing source attempt is now imported.

Closed:

```text
all six two-two routes of {u,d,e,nuD} were enumerated
relative to the locked C1 columns, exactly one route is exact
Z -> u,e as I+Z
X -> d,nuD as I+X
```

Boundary:

```text
this is target-column uniqueness, not independent selected-source routing
```

Current selected artifacts still do not emit a theorem-derived sector charge,
chirality, or conjugation table that forces `{u,e}|{d,nuD}`. Sector projectors
retain the family kernels uniformly, while selected dotD/alpha1 source
verification remains open.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SECTOR_ROUTING_IMPORTED_LOCKED_TARGET_UNIQUE_SOURCE_CERT_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_sector_routing_source_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_source_to_c1_transfer_import": str(PREV_IMPORT),
                    "selected_routec_weylpair_sector_routing_source_lemma": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "routing_checks": routing_checks,
                "support_checks": support_checks,
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
