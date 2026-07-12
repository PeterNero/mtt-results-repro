"""Build the same-source matter-slot/overlap operator packet contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
ORIENTATION_DE_DOTD = DATA / "selected_orientation_carrying_de_dotd_source.candidate.json"
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
OPERATOR_OVERLAP = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"

OUTPUT = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
CERT = CERTS / "selected_routec_samesource_matter_slot_overlap_operator_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    phifin = load(PHIFIN_ALPHA1)
    orientation = load(ORIENTATION_DE_DOTD)
    visible = load(VISIBLE_CW)
    operator_overlap = load(OPERATOR_OVERLAP)

    required_fields = {
        "source_identity": {
            "required": "selected q79/F,m=1 visible Route-C or V_alpha/gerbe source identity",
            "current_support": visible["closed_support"]["selected_s3_gerbe_source_level"],
            "selected_emitted": visible["open_gates"]["selected_visible_operator_source_closed"],
        },
        "matter_slot_charge": {
            "required": "selected charge table: 10_M -> u/e, non-10 plus 1_M -> d/nuD",
            "current_support": previous["matter_slot_charge"]["routeA_matches_required_partition"],
            "selected_emitted": previous["matter_slot_charge"]["selected_charge_table_closed"],
        },
        "singlet_neutrino_rule": {
            "required": "selected 1_M Dirac-neutrino routing rule",
            "current_support": False,
            "selected_emitted": previous["matter_slot_charge"]["singlet_1M_rule_present"],
        },
        "operator_values": {
            "required": "selected D_E/dotD/Riesz/Green values from the same branch",
            "current_support": phifin["payload_summary"]["all_support_shapes_present"],
            "selected_emitted": phifin["payload_summary"]["all_selected_values_emitted"],
        },
        "overlap_transfer": {
            "required": "selected source-to-C1 overlap functor T_selected",
            "current_support": operator_overlap["selected_overlap_transport"]["conditional_source_to_C1_transfer_exact"],
            "selected_emitted": operator_overlap["selected_overlap_transport"]["selected_sector_routing_emitted"],
        },
        "normalization": {
            "required": "selected trace/inner-product/Hessian normalization for A_selected and b_selected",
            "current_support": previous["overlap_normalization"]["conditional_residual_norm"] < 1e-12,
            "selected_emitted": previous["overlap_normalization"]["selected_normalization_emitted"],
        },
        "primitive_contractions": {
            "required": "selected primitive C1/Yukawa overlap contractions",
            "current_support": phifin["payload_summary"]["support_candidate_present"]["primitive_C1_contractions"],
            "selected_emitted": phifin["payload_summary"]["selected_payload_flags"]["primitive_C1_contractions"],
        },
    }

    all_selected = all(item["selected_emitted"] for item in required_fields.values())
    support_count = sum(1 for item in required_fields.values() if item["current_support"])
    selected_count = sum(1 for item in required_fields.values() if item["selected_emitted"])

    validator_contract = {
        "promotion_rule": "Promote conditional Weyl-pair A to A_selected only if all required fields are emitted by one same-source packet.",
        "required_existing_validators": [
            "selected D_E action validator",
            "selected reduced Green/Riesz validator",
            "selected dotD alpha1 validator",
            "selected C1 response operator emission audit",
            "selected sector-routing and normalization audit",
        ],
        "new_validator_needed": "validate_samesource_matter_slot_overlap_operator_packet",
        "must_reject": [
            "lifted selected-source flags",
            "unselected SU(5) fixture promotion",
            "locked-target route selection as proof",
            "observed masses, CKM, PMNS, CP phase, or benchmark matrices",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSameSourceMatterSlotOverlapOperatorPacket",
        "status": STATUS,
        "inputs": {
            "previous_matter_slot_overlap_theorem": rel(PREVIOUS),
            "selected_phifin_alpha1_payload": rel(PHIFIN_ALPHA1),
            "orientation_carrying_de_dotd_source": rel(ORIENTATION_DE_DOTD),
            "visible_cw_operator_source": rel(VISIBLE_CW),
            "operator_overlap_packet": rel(OPERATOR_OVERLAP),
        },
        "required_fields": required_fields,
        "field_counts": {
            "required": len(required_fields),
            "support_present": support_count,
            "selected_emitted": selected_count,
        },
        "same_source_status": {
            "packet_closed": all_selected,
            "source_level_support_broad": support_count >= 5,
            "selected_values_open": selected_count < len(required_fields),
            "first_missing_selected_fields": [
                name for name, item in required_fields.items() if not item["selected_emitted"]
            ],
        },
        "validator_contract": validator_contract,
        "route_decision": {
            "finite_algebra_route": "closed as conditional support",
            "straight_existing_payload_route": "blocked by selected flags and missing primitive contractions",
            "best_next_route": "fill or reject one same-source operator packet against the validator contract",
            "fallback": "full selected Galerkin/HYM replay with sector-resolved matter-slot bases",
        },
        "what_closes_now": {
            "single_packet_contract_built": True,
            "required_fields_enumerated": True,
            "support_vs_selected_counts_recorded": True,
            "promotion_validator_contract_defined": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "fill_same_source_packet_values": True,
            "prove_selected_matter_slot_charge": True,
            "prove_selected_1M_neutrino_rule": True,
            "emit_selected_DE_dotD_Riesz_Green": True,
            "emit_selected_overlap_transfer_functor": True,
            "emit_selected_normalization_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "mode": "CONTRACT_ONLY_CONSTRAINED_SUPERSET",
            "using_one_straight_path": False,
            "paths_combined": [
                "finite SU(5) transversality",
                "selected S3/GS source-level support",
                "Route-C D_E/dotD/Galerkin scaffold",
                "conditional Weyl-pair C1 transfer",
            ],
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C SameSource MatterSlot Overlap Operator Packet

Status: `MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN`

This artifact builds the single packet contract needed to promote the
conditional Weyl-pair C1 operator to selected data.

## Required Fields

The packet must emit, from one selected q79/F,m=1 source:

- selected source identity,
- selected matter-slot charge: `10_M -> u/e`,
- selected `1_M` Dirac-neutrino routing with the shift side,
- selected `D_E`, dotD, Riesz, and Green values,
- selected overlap-transfer functor `T_selected`,
- selected trace/inner-product/Hessian normalization,
- selected primitive C1/Yukawa contractions.

## Current Status

Most support shapes exist, but selected values do not.  The finite SU(5) and
conditional C1 algebra are no longer the blocker.  The blocker is filling this
same-source packet without lifted flags, unselected fixtures, or observed SM
data.

Next artifact: `MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
