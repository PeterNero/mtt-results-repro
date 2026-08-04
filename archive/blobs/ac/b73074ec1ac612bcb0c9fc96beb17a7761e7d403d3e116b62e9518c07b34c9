"""Audit selected Weyl-pair sector-routing source lemma attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_sector_routing_source_lemma_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    routing = data["routing_search"]
    current = data["current_selected_support"]
    lemma = data["lemma_attempt"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "external inspiration not proof",
            data["external_research_inspiration"]["used_as_proof"] is False,
            data["external_research_inspiration"],
        ),
        check(
            "all routes enumerated",
            len(routing["all_two_two_partitions_tested"]) == 6,
            routing["all_two_two_partitions_tested"],
        ),
        check(
            "locked columns pick intended route",
            routing["target_columns_select_route"] is True
            and len(routing["exact_rows_relative_to_locked_columns"]) == 1
            and routing["exact_rows_relative_to_locked_columns"][0]["is_intended_route"] is True,
            routing["exact_rows_relative_to_locked_columns"],
        ),
        check(
            "source does not independently select route",
            routing["source_data_independently_selects_route"] is False
            and current["selected_dotD_source_verified_open"] is True
            and current["alpha1_driver_verified_open"] is True,
            {"routing": routing, "current": current},
        ),
        check(
            "lemma not overclaimed",
            lemma["fully_proved"] is False
            and lemma["proved_by_locked_columns"] is True
            and lemma["proved_by_selected_source"] is False,
            lemma,
        ),
        check(
            "next certificate specified",
            data["next_certificate"]["name"] == "SelectedWeylPairSectorChargeOrChiralityCertificate"
            and len(data["next_certificate"]["must_supply"]) == 4,
            data["next_certificate"],
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records missing source certificate",
            "not independent selected-source selection" in note
            and "sector charge, chirality, or conjugation table" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair sector-routing audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
