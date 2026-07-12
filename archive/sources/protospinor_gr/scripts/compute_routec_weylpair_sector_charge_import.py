from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_sector_routing_source_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_sector_charge_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_sector_charge_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_SectorCharge_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_SECTOR_CHARGE_IMPORTED_STRUCTURAL_MATCH_SOURCE_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_CERTIFICATE_BUILT_SOURCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    tests = src["current_mtt_data_tests"]
    paths = src["superset_paths"]
    route_a = paths["route_A"]
    route_b = paths["route_B"]
    result = src["certificate_result"]

    input_checks = {
        "previous_sector_routing_imported": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    route_a_checks = {
        "su5_transversality_closed": route_a["evidence"]["finite_su5_transversality_closed"]
        is True,
        "projection_tensor_closed_conditionally": route_a["evidence"][
            "conditional_projection_tensor_closed"
        ]
        is True,
        "required_partition_matches": route_a["sector_implication"][
            "matches_required_partition"
        ]
        is True,
        "clock_side_u_e": sorted(route_a["sector_implication"]["phase_like_clock_side_from_10M"])
        == ["e", "u"],
        "shift_side_d_nuD": route_a["sector_implication"]["non10_shift_side_candidate"]
        == ["d", "nuD"],
        "su5_source_not_selected": route_a["evidence"]["selected_su5_source_present"] is False,
        "fixture_not_selected": route_a["evidence"]["fixture_selected_by_mtt"] is False,
        "nuD_singlet_gap": "singlet" in route_a["sector_implication"]["nuD_caveat"],
    }

    route_b_checks = {
        "left_right_split_coherent": route_b["evidence"]["left_right_sector_split_coherent"]
        is True,
        "right_orientations_uniform": route_b["evidence"]["all_right_orientations_uniform"]
        is True,
        "projector_dotd_uniform": route_b["evidence"]["current_projector_dotd_payload_uniform"]
        is True,
        "right_orientation_value_singleton": route_b["evidence"]["right_orientation_values"] == [2],
    }

    current_data_checks = {
        "phifin_does_not_split": tests["phifin_distinguishes_u_e_from_d_N"] is False,
        "all_orientations_same": set(tests["phifin_right_sector_orientations"].values()) == {2},
        "projector_payload_identical": tests["projector_dotd_uniformity"][
            "all_right_family_payloads_identical"
        ]
        is True,
        "dotD_source_open": tests["selected_dotD_source_verified"] is False,
        "alpha1_driver_open": tests["alpha1_driver_verified"] is False,
        "representations_required": tests["representations_are_source_data_required"]
        == "SELECTED_SOURCE_DATA_REQUIRED",
    }

    certificate_checks = {
        "selected_certificate_open": result["selected_certificate_closed"] is False,
        "phase_route_required": result["phase_route_required"] == ["u", "e"],
        "shift_route_required": result["shift_route_required"] == ["d", "nuD"],
        "why_not_closed_has_four_reasons": len(result["why_not_closed"]) == 4,
        "combined_locked_target_not_promotion": paths["combined_locked_target_use"][
            "source_data_independently_selects_route"
        ]
        is False,
    }

    guardrail_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "external_heisenberg_not_proof": src["external_research_inspiration"][
            "finite_heisenberg_theta_weil"
        ]["used_as_proof"]
        is False,
        "external_heterotic_not_proof": src["external_research_inspiration"][
            "heterotic_yukawa_selection_rules"
        ]["used_as_proof"]
        is False,
        "target_fitting_excluded": src["what_closes_now"]["target_fitting_excluded"] is True,
    }

    theorem = {
        "name": "RouteCWeylPairSectorChargeImportTheorem",
        "proved": all(input_checks.values())
        and all(route_a_checks.values())
        and all(route_b_checks.values())
        and all(current_data_checks.values())
        and all(certificate_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The Weyl-pair sector charge/chirality certificate attempt is imported. "
            "The SU(5)/E6 matter-slot route structurally matches the required "
            "partition u/e versus d/nuD, but selected U_10/U_bar5 source data and "
            "the singlet-neutrino rule remain open. The current selected Phi_fin/"
            "Route-C block route is honest but uniform across u,d,e,N, so it does "
            "not independently force the pair split."
        ),
    }

    verdict = {
        "su5_e6_structural_match_identified": True,
        "selected_su5_source_proved": False,
        "selected_singlet_neutrino_shift_rule_proved": False,
        "selected_block_route_pair_split_proved": False,
        "sector_charge_certificate_closed": False,
        "conditional_A_promoted_to_A_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "route_a_checks": route_a_checks,
        "route_b_checks": route_b_checks,
        "current_data_checks": current_data_checks,
        "certificate_checks": certificate_checks,
        "guardrail_checks": guardrail_checks,
        "superset_paths": paths,
        "current_mtt_data_tests": tests,
        "certificate_result": result,
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair SectorCharge Import v1

## Result

The sector charge/chirality certificate attempt is now imported.

Route A, the high-scale SU(5)/E6 matter-slot path, gives the strongest
structural match:

```text
u,e   -> 10_M clock/phase side
d     -> bar5_M shift side
nuD   -> 1_M singlet, needing a selected Dirac-neutrino shift rule
```

Route B, the currently honest selected Phi_fin/Route-C block path, does not
split the right-family sectors at the checked layer:

```text
u,d,e,N carry uniform orientation
projector/dotD payloads are identical across checked right-family fields
```

So the certificate remains source-open. The next object must either promote the
matter-slot theorem with selected `10_M`, `bar5_M`, and `1_M` routing, or replace
it with a selected sector-resolved block theorem.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_SECTOR_CHARGE_IMPORTED_STRUCTURAL_MATCH_SOURCE_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_sector_charge_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_sector_routing_source_import": str(PREV_IMPORT),
                    "selected_routec_weylpair_sector_charge_or_chirality_certificate": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "route_a_checks": route_a_checks,
                "route_b_checks": route_b_checks,
                "current_data_checks": current_data_checks,
                "certificate_checks": certificate_checks,
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
