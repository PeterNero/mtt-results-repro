from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_matter_slot_blocksector_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_hybrid_matter_slot_galerkin_source_packet_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_hybrid_matter_slot_galerkin_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_hybrid_matter_slot_galerkin_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Hybrid_MatterSlot_Galerkin_Import_v1.md"

STATUS = "ROUTEC_HYBRID_MATTERSLOT_GALERKIN_IMPORTED_SOURCE_OVERLAP_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_HYBRID_MATTERSLOT_GALERKIN_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_AND_OVERLAP_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    honest = src["attempts"]["honest_routec_galerkin_fill"]
    fixture = src["attempts"]["conditional_su5_fixture_fill"]
    c1 = src["c1_overlap_boundary"]
    verdict_src = src["selection_verdict"]

    input_checks = {
        "previous_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    honest_checks = {
        "shape_scaffold_present": all(honest["fields_present"].values()),
        "selected_DE_source_false": honest["source_flags"]["selected_DE_source_verified"] is False,
        "selected_dotD_source_false": honest["source_flags"]["selected_dotD_source_verified"] is False,
        "alpha1_driver_false": honest["source_flags"]["alpha1_driver_verified"] is False,
        "matter_slot_source_false": honest["source_flags"]["matter_slot_source_verified"] is False,
        "family_bases_identical": honest["basis_transport"]["all_checked_family_bases_identical"] is True,
        "relative_transport_identity": honest["basis_transport"]["current_relative_transport"] == "I_3",
        "desired_transport_not_reached": honest["basis_transport"][
            "current_payload_reaches_desired_transport"
        ]
        is False,
    }

    fixture_checks = {
        "fixture_has_10M_clock": fixture["has_10M_clock"] is True,
        "fixture_has_bar5M_shift": fixture["has_bar5M_shift"] is True,
        "fixture_lacks_1M_rule": fixture["has_1M_singlet_neutrino_rule"] is False,
        "fixture_not_selected": fixture["selected_by_mtt"] is False,
        "fixture_only": fixture["fixture_only"] is True,
        "fixture_not_closing": fixture["closes_hybrid_packet"] is False,
    }

    c1_checks = {
        "smoke_dotD_not_enough": c1["route_c_smoke_dotD_alone_closes_ckm_heavy_link"] is False,
        "universal_tensor_zero": c1["universal_tensor_case_gives_Delta_t_zero"] is True,
        "five_unknowns_per_sector": c1["heavy_link_overlap_unknowns_per_sector"] == 5,
        "new_overlap_data_required": "sector-resolved trilinear overlap tensors T_s"
        in c1["new_required_selected_data"],
    }

    verdict_checks = {
        "hybrid_packet_not_selected": verdict_src["hybrid_packet_selected"] is False,
        "shape_scaffold_present": verdict_src["shape_scaffold_present"] is True,
        "selected_operator_source_absent": verdict_src["selected_operator_source_present"] is False,
        "selected_overlap_absent": verdict_src["selected_overlap_tensor_present"] is False,
        "best_next_object_matches": verdict_src["best_next_object"] == NEXT_ARTIFACT,
    }

    guardrail_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "target_fitting_excluded": src["what_closes_now"]["target_fitting_excluded"] is True,
    }

    theorem = {
        "name": "RouteCHybridMatterSlotGalerkinImportTheorem",
        "proved": all(input_checks.values())
        and all(honest_checks.values())
        and all(fixture_checks.values())
        and all(c1_checks.values())
        and all(verdict_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The hybrid matter-slot Galerkin packet attempt is imported. The "
            "honest Route-C/Galerkin shape scaffold is present, but selected "
            "D_E, dotD, alpha1, and matter-slot source flags remain false; "
            "checked family bases are identical and give identity transport. "
            "The conditional SU(5) fixture has the desired 10_M/bar5_M shape "
            "but is unselected and lacks the 1_M singlet-neutrino rule. The "
            "packet reduces to selected operator-source and overlap-tensor data."
        ),
    }

    verdict = {
        "hybrid_packet_schema_instantiated": True,
        "honest_shape_scaffold_present": True,
        "identity_transport_no_go_recorded": True,
        "conditional_su5_fixture_not_promoted": True,
        "selected_operator_source_present": False,
        "selected_overlap_tensor_present": False,
        "selected_matter_slot_transport_present": False,
        "conditional_A_promoted_to_A_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "honest_checks": honest_checks,
        "fixture_checks": fixture_checks,
        "c1_checks": c1_checks,
        "verdict_checks": verdict_checks,
        "guardrail_checks": guardrail_checks,
        "attempts": src["attempts"],
        "c1_overlap_boundary": c1,
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Hybrid MatterSlot Galerkin Import v1

## Result

The hybrid matter-slot Galerkin packet attempt is imported.

What is present:

```text
three-dimensional model zero cluster
positive complement gap
Riesz/reduced Green model
sector projectors
dotD alpha1 matrix shapes
```

What blocks selection:

```text
selected D_E source flag is false
selected dotD source flag is false
alpha1 driver flag is false
matter-slot source flag is false
checked family bases are identical
current relative transport is I_3
```

The conditional SU(5) fixture has `10_M` clock and `bar5_M` shift shape, but it
is not selected by MTT and lacks the selected `1_M` singlet-neutrino shift rule.

The next object is the selected operator-source and overlap-tensor packet.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_HYBRID_MATTERSLOT_GALERKIN_IMPORTED_SOURCE_OVERLAP_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_hybrid_matter_slot_galerkin_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_matter_slot_blocksector_import": str(PREV_IMPORT),
                    "selected_routec_hybrid_matter_slot_galerkin_source_packet": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "honest_checks": honest_checks,
                "fixture_checks": fixture_checks,
                "c1_checks": c1_checks,
                "verdict_checks": verdict_checks,
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
