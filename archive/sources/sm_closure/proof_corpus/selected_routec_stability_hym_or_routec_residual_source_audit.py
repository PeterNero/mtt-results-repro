"""Audit stability/HYM or Route-C residual source proof attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_stability_hym_or_routec_residual_source.candidate.json"
CERT = REPO / "certificates" / "selected_routec_stability_hym_or_routec_residual_source_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN"
NEXT = "MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    central = data["central_neutral_destabilizer_theorem"]
    ah = data["appell_humbert_promotion"]
    verdict = data["proof_verdict"]
    route_c = data["route_c_residual_lane"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no full closure claimed", data["closure_claimed"] is False and verdict["full_stability_proved"] is False, verdict),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check(
            "central-neutral lane closed",
            central["proved_for_lane"] is True
            and central["all_candidate_boundaries_injective"] is True
            and central["all_candidates_obstructed"] is True
            and central["candidate_count"] == 6,
            central,
        ),
        check(
            "AH promotion conditional not overclaimed",
            ah["all_degree_identities_hold"] is True
            and ah["all_reduced_boundaries_injective"] is True
            and ah["conditional_on_selected_AH_source"] is True
            and ah["still_open"]["MTT_selection_of_Appell_Humbert_representative"] is True,
            ah,
        ),
        check(
            "Route-C residual still open",
            route_c["finite_codomain_schema_closed"] is True
            and route_c["identity_rhoE_smoke_rejected"] is True
            and route_c["still_open"]["HYM_or_RouteC_selected_values"] is True,
            route_c,
        ),
        check(
            "remaining global theorem explicit",
            data["what_remains_open"]["global_rank_one_torsion_free_subsheaf_enumeration"] is True
            and data["what_remains_open"]["selected_RouteC_residual_values"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records subtheorem not full HYM",
            "Proven Subtheorem" in note and "does not close full stability/HYM" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C stability/HYM or Route-C residual source audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
