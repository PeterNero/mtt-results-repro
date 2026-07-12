"""Audit Weyl-pair source-to-C1 transfer map gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_source_to_c1_transfer_map_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    strategy = data["superset_strategy"]
    transfer = data["conditional_transfer_map"]
    selected = data["selected_status"]
    reduction = data["reduction"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "superset guardrails",
            strategy["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and strategy["observed_data_used"] is False
            and strategy["lifted_flags_used_as_proof"] is False
            and strategy["target_fitting_used"] is False,
            strategy,
        ),
        check(
            "conditional transfer exact",
            transfer["conditional_exact"] is True
            and transfer["phase_residual"] <= 1e-10
            and transfer["shift_residual"] <= 1e-10
            and transfer["uses_source_level_carrier"] is True
            and transfer["uses_active_shift_provenance"] is True,
            transfer,
        ),
        check(
            "selected routing still open",
            selected["selected_transfer_map_emitted"] is False
            and selected["selected_sector_routing_emitted"] is False
            and selected["selected_normalization_emitted"] is False
            and selected["promote_to_A_selected_allowed"] is False,
            selected,
        ),
        check(
            "sector routing next",
            reduction["name"] == "SelectedWeylPairSectorRoutingSourceLemma"
            and reduction["status"] == "NEXT_LEMMA_REQUIRED",
            reduction,
        ),
        check(
            "theorem conditional only",
            data["theorem"]["proved"] is True
            and data["what_closes_now"]["remaining_gap_reduced_to_selected_sector_routing"] is True
            and data["what_remains_open"]["prove_selected_sector_routing_source"] is True,
            {"theorem": data["theorem"], "open": data["what_remains_open"]},
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records sector-routing gap",
            "transfer is exact as an algebraic map" in note
            and "do not emit the sector-routing rule itself" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair source-to-C1 transfer audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
