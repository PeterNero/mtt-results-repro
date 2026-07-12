"""Import q79 sector-charge reduction and End0 value-route frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "routec_weylpair_source_provenance_reduction_import_certificate.json"
Q79_SECTOR = Q79 / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
SM_SECTOR = SM / "candidate_data" / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
SM_GRAM = SM / "candidate_data" / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
Q79_END0 = Q79 / "candidate_data" / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"

OUTPUT_PACKET = DATA / "q79_sectorcharge_end0_value_route_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_sectorcharge_end0_value_route_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_SectorCharge_End0_ValueRoute_Import_v1.md"

STATUS = "Q79_SECTORCHARGE_END0_VALUE_ROUTE_IMPORTED_MATTERSLOT_OVERLAP_OPEN"
PREVIOUS_STATUS = "ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
NEXT = "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    q79_sector = load(Q79_SECTOR)
    sm_sector = load(SM_SECTOR)
    sm_gram = load(SM_GRAM)
    q79_end0 = load(Q79_END0)

    sector_reduction = q79_sector["sector_charge_reduction"]
    end0_route = q79_end0["route_B_end0_to_sector_routing"]
    route_a = q79_end0["route_A_source_normalization"]

    checks = {
        "K0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "K1_sector_charge_reduced_not_closed": q79_sector["status"]
        == "Q79_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE_OPEN"
        and q79_sector["closure_claimed"] is False
        and q79_sector["target_fitting_used"] is False
        and sector_reduction["decision"]["su5_e6_partition_matches_required_route"] is True
        and sector_reduction["decision"]["selected_sector_charge_or_chirality_table_proved"] is False
        and sector_reduction["decision"]["selected_transfer_normalization_proved"] is False,
        "K2_su5_e6_structural_candidate_matches_route": sector_reduction["su5_e6_structural_candidate"][
            "matches_required_partition"
        ]
        is True
        and sector_reduction["su5_e6_structural_candidate"]["phase_route_from_10M"] == ["e", "u"]
        and sector_reduction["su5_e6_structural_candidate"]["shift_route_from_non10_plus_singlet"]
        == ["d", "nuD"]
        and sector_reduction["su5_e6_structural_candidate"]["nuD_singlet_rule_closed"] is False,
        "K3_sm_sector_certificate_keeps_open": sm_sector["certificate_result"]["selected_certificate_closed"]
        is False
        and sm_sector["superset_paths"]["route_A"]["sector_implication"]["matches_required_partition"]
        is True
        and sm_sector["superset_paths"]["route_B"]["evidence"]["current_projector_dotd_payload_uniform"]
        is True
        and sm_sector["target_fitting_used"] is False,
        "K4_gram_transfer_conditionally_fixed_source_open": sm_gram["gram_transfer_packet"][
            "conditional_gram_theorem_proved"
        ]
        is True
        and sm_gram["gram_transfer_packet"]["physical_transfer_normalization_selected"] is False
        and sm_gram["minimal_open_fields"]["selected_1M_Dirac_neutrino_rule"]["closed"] is False
        and sm_gram["minimal_open_fields"]["selected_sector_charge_or_chirality_table"]["closed"] is False
        and sm_gram["minimal_open_fields"]["selected_zero_mode_bases_K_s"]["closed"] is False,
        "K5_naive_source_normalization_rejected": route_a["closed_as_nogo"] is True
        and route_a["naive_Ext_scale_to_alpha1_source_normalization_rejected"] is True
        and route_a["does_not_vary_integral_c2_alpha1"] is True
        and route_a["central_shared_circle_retained"] is True,
        "K6_end0_route_is_next_open_packet": q79_end0["decision"]["best_next_object"] == NEXT
        and q79_end0["decision"]["sector_routing_route_remains_primary"] is True
        and q79_end0["decision"]["selected_End0_to_sector_routing_values_extracted"] is False
        and end0_route["End0_row_response_available"] is True
        and end0_route["same_basis_dotD_matrices_exist"] is True
        and end0_route["conditional_weyl_transfer_exact"] is True
        and end0_route["selected_End0_to_sector_functor_values_extracted"] is False,
        "K7_guardrails_no_overclaim": q79_end0["guardrails"]["claims_A_selected_or_b_selected"] is False
        and q79_end0["guardrails"]["claims_C1_response_emitted"] is False
        and q79_end0["guardrails"]["claims_selected_End0_to_sector_routing"] is False
        and q79_end0["guardrails"]["claims_selected_transfer_normalization"] is False
        and q79_end0["guardrails"]["uses_observed_or_benchmark_inputs"] is False
        and q79_sector["guardrails"]["uses_locked_target_columns_as_selector"] is False
        and q79_sector["guardrails"]["uses_observed_masses_or_ckm_inputs"] is False,
    }

    return {
        "packet": "Q79_SectorCharge_End0_ValueRoute_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "q79_sector_charge": str(Q79_SECTOR),
            "sm_sector_charge": str(SM_SECTOR),
            "sm_gram_transfer": str(SM_GRAM),
            "q79_end0_value_route": str(Q79_END0),
        },
        "theorem": {
            "name": "Q79SectorChargeEnd0ValueRouteImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The sector-charge/chirality gate reduces to a same-source "
                "matter-slot charge and overlap-normalization theorem. SU(5)/E6 "
                "structurally matches the required partition, but selected source "
                "data still do not prove the 10M clock slot, bar5M/singlet shift "
                "slot, Dirac-neutrino singlet rule, or selected transfer "
                "normalization. The naive Ext-scale-to-alpha1 normalization route "
                "is rejected; the legal next route is an End0-to-sector functor "
                "source/value packet."
            ),
        },
        "checks": checks,
        "q79_sector_charge_reduction": q79_sector,
        "sm_sector_charge_certificate": sm_sector,
        "sm_gram_transfer_packet": sm_gram,
        "q79_end0_value_route": q79_end0,
        "structural_partition": {
            "phase_route": sector_reduction["required_route"]["phase_Z_to"],
            "shift_route": sector_reduction["required_route"]["shift_X_to"],
            "su5_e6_matches_required_partition": True,
            "selected_sector_charge_or_chirality_table_proved": False,
            "selected_transfer_normalization_proved": False,
            "nuD_singlet_rule_closed": False,
        },
        "end0_next_contract": q79_end0["next_end0_sector_functor_value_packet_contract"],
        "what_closes_now": {
            "sector_charge_reduced_to_matter_slot_overlap": True,
            "su5_e6_structural_partition_imported": True,
            "nuD_singlet_gap_identified": True,
            "conditional_gram_transfer_scalar_imported": True,
            "naive_Ext_scale_to_alpha1_source_normalization_rejected": True,
            "End0_sector_functor_route_selected_as_next_legal_object": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_End0_to_sector_functor_values": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "selected_transfer_normalization": True,
            "selected_dotD_source_theorem": True,
            "same_branch_alpha1_driver_theorem": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_sector_charge_or_chirality_table": False,
            "claims_selected_transfer_normalization": False,
            "claims_selected_End0_to_sector_routing": False,
            "claims_A_selected_or_b_selected": False,
            "claims_C1_response_emitted": False,
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79SectorChargeEnd0ValueRouteImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "structural_partition": packet["structural_partition"],
        "end0_next_contract_status": packet["end0_next_contract"]["status"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    part = cert["structural_partition"]
    return f"""# Q79 SectorCharge End0 ValueRoute Import v1

Status: `{cert["status"]}`.

The sector-charge/chirality gate is reduced, not closed.  The SU(5)/E6
matter-slot dictionary structurally matches the required route:

```text
phase Z -> {part["phase_route"]}
shift X -> {part["shift_route"]}
```

But the selected source still has to prove the sector-charge table, the
`1_M` Dirac-neutrino/singlet rule, and transfer normalization.  The naive route
that identifies continuous Ext-scale variation with the integral `alpha1`
source row is rejected; the legal route is now the selected End0-to-sector
functor/source/value packet.

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
