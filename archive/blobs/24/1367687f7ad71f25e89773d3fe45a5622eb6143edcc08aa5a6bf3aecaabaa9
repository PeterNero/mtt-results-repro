"""Audit selected Weyl-pair sector charge/chirality certificate attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_CERTIFICATE_BUILT_SOURCE_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tests = data["current_mtt_data_tests"]
    paths = data["superset_paths"]
    route_a = paths["route_A"]
    route_b = paths["route_B"]
    result = data["certificate_result"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "external inspiration not proof",
            data["external_research_inspiration"]["heterotic_yukawa_selection_rules"]["used_as_proof"] is False
            and data["external_research_inspiration"]["finite_heisenberg_theta_weil"]["used_as_proof"] is False,
            data["external_research_inspiration"],
        ),
        check(
            "phifin right orientations are uniform",
            tests["phifin_distinguishes_u_e_from_d_N"] is False
            and set(tests["phifin_right_sector_orientations"].values()) == {2},
            tests["phifin_right_sector_orientations"],
        ),
        check(
            "projector dotD payload does not split right sectors",
            tests["projector_dotd_uniformity"]["all_right_family_payloads_identical"] is True,
            tests["projector_dotd_uniformity"]["right_family_pairs"],
        ),
        check(
            "route A structural but conditional",
            route_a["evidence"]["finite_su5_transversality_closed"] is True
            and route_a["evidence"]["conditional_projection_tensor_closed"] is True
            and route_a["evidence"]["selected_su5_source_present"] is False
            and route_a["sector_implication"]["matches_required_partition"] is True
            and "singlet" in route_a["sector_implication"]["nuD_caveat"],
            route_a,
        ),
        check(
            "route B honest but insufficient",
            route_b["evidence"]["left_right_sector_split_coherent"] is True
            and route_b["evidence"]["all_right_orientations_uniform"] is True
            and route_b["evidence"]["current_projector_dotd_payload_uniform"] is True,
            route_b,
        ),
        check(
            "locked target not promoted",
            paths["combined_locked_target_use"]["locked_columns_uniquely_pick_partition"] is True
            and paths["combined_locked_target_use"]["source_data_independently_selects_route"] is False
            and "Cannot promote" in paths["combined_locked_target_use"]["forbidden_use"],
            paths["combined_locked_target_use"],
        ),
        check(
            "certificate remains open",
            result["selected_certificate_closed"] is False
            and result["phase_route_required"] == ["u", "e"]
            and result["shift_route_required"] == ["d", "nuD"],
            result,
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records both paths and gap",
            "Route A" in note
            and "Route B" in note
            and "`nuD` is a singlet" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair sector charge/chirality certificate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
