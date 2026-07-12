"""Audit the selected non-split rank-two or Route-C same-source packet artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"
CERT = REPO / "certificates" / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    mode = data["superset_mode"]
    rank2 = data["rank2_lane"]
    route_c = data["route_c_lane"]
    blocker = data["same_source_packet_contract"]["common_blocker"]

    checks = [
        check("status", data["status"] == "MTT_SELECTED_NONSPLIT_RANK2_OR_ROUTEC_SAME_SOURCE_PACKET_REDUCED_TO_SYMMETRY_BREAKING_SOURCE", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset mode", mode["classification"] == "SUPERSET_CONVERGENCE_WITH_PARALLEL_REPAIR", mode),
        check("no target fitting", data["target_fitting_used"] is False and mode["diagnostic_backfit_only"]["used"] is False, mode["diagnostic_backfit_only"]),
        check("rank2 lane primary", rank2["classification"] == "SUPERSET_CONVERGENCE_PRIMARY_FILL_LANE" and rank2["candidate_id"] == "rank2_non_split_extension_preferred_L_1_-2_0", rank2),
        check("rank2 closed scaffolds", all(rank2["closed"].values()), rank2["closed"]),
        check("rank2 blockers retained", rank2["blocked_by"]["selected_l2_cochain_packet_absent"] is True and rank2["blocked_by"]["base_swap_pic0_selector_obstruction"] is True, rank2["blocked_by"]),
        check("route c lane parallel", route_c["classification"] == "SUPERSET_REPAIR_PARALLEL_FILL_LANE", route_c),
        check("route c closed scaffolds", all(route_c["closed"].values()), route_c["closed"]),
        check("route c selected values open", route_c["blocked_by"]["actual_selected_rho_E_values"] is True and route_c["blocked_by"]["actual_source_residual_certificate"] is True, route_c["blocked_by"]),
        check("common blocker named", blocker["name"] == "SameSourceSymmetryBreakingSource.v1", blocker),
        check("common blocker requires pic0 and order", any("Pic0" in item for item in blocker["must_supply"]) and any("base-factor" in item for item in blocker["must_supply"]), blocker["must_supply"]),
        check("rank2 priority first", data["same_source_packet_contract"]["lane_priority"][0]["lane"] == "rank2_non_split_valpha", data["same_source_packet_contract"]["lane_priority"]),
        check("next artifact", cert["primary_next_artifact"] == "MTT_SameSource_SymmetryBreaking_Source_v1", cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["same_source_symmetry_breaking_source"] is True, cert),
        check("note records both lanes", "Rank-Two Lane" in note and "Route-C Lane" in note and "Common Blocker" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected non-split rank-two or Route-C same-source packet audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
