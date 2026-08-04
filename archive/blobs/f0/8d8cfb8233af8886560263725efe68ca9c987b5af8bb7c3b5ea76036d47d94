"""Import the operator-level rho_E/B_N fill cut-set."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "nonidentity_rhoe_bn_fill_sourcelevel_attempt_certificate.json"
Q79_SECTOR_CERT = Q79 / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json"
Q79_SECTOR_PACKET = Q79 / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
QA_MATTER_PACKET = QA / "candidate_data" / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json"
SM_VISIBLE_CW_CERT = SM / "certificates" / "selected_visible_chern_weil_operator_source_certificate.json"
SM_SECTOR_CERT = SM / "certificates" / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json"

OUTPUT_PACKET = DATA / "operatorlevel_rhoe_bn_fill_cutset_matter_overlap_import.candidate.json"
OUTPUT_CERT = CERTS / "operatorlevel_rhoe_bn_fill_cutset_matter_overlap_import_certificate.json"
OUTPUT_NOTE = CORPUS / "OperatorLevel_RhoE_BN_Fill_Cutset_MatterOverlap_Import_v1.md"

STATUS = "OPERATORLEVEL_RHOE_BN_FILL_REDUCED_MATTERSLOT_OVERLAP_SOURCE_OPEN"
OLD_NEXT = "Selected_U1Y_RouteC_OperatorLevel_RhoE_BN_SectorCharge_and_C1_Fill_v1"
NEXT = "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    q79_sector = load(Q79_SECTOR_CERT)
    q79_packet = load(Q79_SECTOR_PACKET)
    qa_matter = load(QA_MATTER_PACKET)
    sm_visible = load(SM_VISIBLE_CW_CERT)
    sm_sector = load(SM_SECTOR_CERT)
    structural = qa_matter["structural_candidate"]
    clauses = {item["clause"]: item for item in qa_matter["theorem_clauses"]}

    checks = {
        "G0_previous_frontier_matches": previous["frontier_update"]["current_next"] == OLD_NEXT,
        "G1_q79_reduces_to_matter_overlap": q79_sector["status"]
        == "Q79_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE_OPEN"
        and q79_sector["next_required_artifact"]
        == "Q79_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1",
        "G2_structural_partition_matches": structural["matches_required_partition"] is True
        and sorted(structural["phase_route_from_10M"]) == ["e", "u"]
        and sorted(structural["shift_route_from_non10_plus_singlet"]) == ["d", "nuD"],
        "G3_no_selected_sector_or_transfer": q79_packet["sector_charge_reduction"]["decision"][
            "selected_sector_charge_or_chirality_table_proved"
        ]
        is False
        and q79_packet["sector_charge_reduction"]["decision"]["selected_transfer_normalization_proved"] is False
        and q79_packet["sector_charge_reduction"]["decision"]["selected_overlap_or_transfer_functor_proved"] is False,
        "G4_nuD_singlet_gap_open": structural["nuD_singlet_gap"] is True
        and structural["nuD_singlet_rule_closed"] is False
        and clauses["X_to_d_nuD"]["closed"] is False,
        "G5_conditional_route_exact_not_selected": qa_matter["decision"]["conditional_route_exact"] is True
        and qa_matter["decision"]["selected_source_independently_derives_route"] is False
        and clauses["selected_transfer_normalization"]["closed"] is False,
        "G6_visible_cw_operator_source_open": sm_visible["status"]
        == "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET"
        and sm_visible["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True
        and sm_visible["what_remains_open"]["primitive_C1_overlap_tensors"] is True,
        "G7_sm_sector_certificate_open": sm_sector["selected_certificate_closed"] is False
        and sm_sector["what_remains_open"]["selected_sector_charge_or_chirality_table"] is True
        and sm_sector["what_remains_open"]["selected_singlet_neutrino_shift_rule"] is True,
        "G8_no_targets_or_downstream_closure": qa_matter["target_fitting_used"] is False
        and q79_sector["target_fitting_used"] is False
        and sm_visible["target_fitting_used"] is False
        and qa_matter["guardrails"]["claims_A_selected"] is False
        and qa_matter["guardrails"]["claims_full_sm_closure"] is False,
    }

    return {
        "packet": "OperatorLevel_RhoE_BN_Fill_Cutset_MatterOverlap_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_sourcelevel_fill": str(PREVIOUS.relative_to(ROOT)),
            "q79_sector_charge_reduction": str(Q79_SECTOR_CERT),
            "qa_matter_overlap_source": str(QA_MATTER_PACKET),
            "sm_visible_cw_operator_source": str(SM_VISIBLE_CW_CERT),
            "sm_sector_charge_certificate": str(SM_SECTOR_CERT),
        },
        "theorem": {
            "name": "OperatorLevelRhoEBNFillCutsetMatterOverlapImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "After source-level projective rho_E is filled, the operator-level "
                "rho_E/B_N/C1 gate reduces to a same-source matter-slot overlap "
                "packet.  The SU(5)/E6 dictionary gives the required structural "
                "partition 10_M={u,e} and non-10/singlet={d,nuD}, and the conditional "
                "C1 route is exact.  The proof is still open because no selected "
                "source derives the 10_M clock slot, bar5_M plus 1_M shift slot, "
                "Dirac-neutrino singlet rule, transfer normalization, or overlap "
                "functor independently of locked target columns."
            ),
        },
        "checks": checks,
        "structural_partition": structural,
        "theorem_clauses": qa_matter["theorem_clauses"],
        "visible_operator_cutset": sm_visible["what_remains_open"],
        "sector_charge_open_items": q79_sector["still_open"],
        "frontier_update": {
            "old_next": OLD_NEXT,
            "current_next": NEXT,
            "why": (
                "The generic operator-level fill is sharpened to a hybrid Galerkin "
                "overlap source packet: it must derive matter-slot routing, transfer "
                "normalization, selected operator replay, and selected C1 emission in "
                "one same-source branch."
            ),
        },
        "guardrails": {
            "does_not_use_locked_target_columns_as_selector": True,
            "does_not_claim_selected_sector_charge": True,
            "does_not_claim_selected_transfer_normalization": True,
            "does_not_claim_selected_overlap_functor": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "verdict": {
            "what_closes_now": (
                "The next operator-level source is no longer broad: the matter-slot "
                "overlap cut-set is identified, and the SU(5)/E6 partition is the "
                "unique structural candidate."
            ),
            "what_remains": (
                "Build the hybrid Galerkin overlap source packet with selected "
                "HYM/Strominger or Route-C operator data, selected 10_M/bar5_M/1_M "
                "routing, selected transfer normalization, selected overlap functor, "
                "and selected C1 response."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "OperatorLevelRhoEBNFillCutsetMatterOverlapImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# OperatorLevel RhoE BN Fill Cutset MatterOverlap Import v1

## Result

Status: `{cert["status"]}`

The operator-level fill is reduced to the same-source matter-slot overlap
packet.  The structural partition is:

```json
{json.dumps(packet["structural_partition"], indent=2, sort_keys=True)}
```

## Frontier

The conditional route is exact, but not selected.  The next packet must emit
matter-slot routing, transfer normalization, selected operator replay, and C1
response from one same-source branch without locked target columns.

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```
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
