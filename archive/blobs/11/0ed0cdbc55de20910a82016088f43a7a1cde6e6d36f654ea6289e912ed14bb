"""Audit selected Route-C operator-source identity subpacket reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_operatorsourceidentity_subpacket.candidate.json"
CERT = REPO / "certificates" / "selected_routec_operatorsourceidentity_subpacket_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_IDENTITY_SUBPACKET_REDUCED_TO_RANK2_OR_ROUTEC_FILL_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    support = data["source_level_support"]
    verdict = data["operator_identity_verdict"]
    lanes = data["lane_evaluation"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False and verdict["subpacket_closed"] is False, verdict),
        check("no target fitting", data["target_fitting_used"] is False and verdict["target_fitting_used"] is False, verdict),
        check(
            "source-level support separated",
            support["selected_s3_gerbe_source_level"] is True
            and support["source_level_projective_gerbe_rhoE_promoted"] is True
            and support["operator_level_projective_rhoE_promoted"] is False
            and support["visible_operator_source_closed"] is False,
            support,
        ),
        check(
            "rank2 and Route-C lanes both live",
            "rank2_non_split_valpha" in lanes
            and "route_c_finite_hym_strominger" in lanes
            and lanes["rank2_non_split_valpha"]["priority"] == 1
            and lanes["route_c_finite_hym_strominger"]["priority"] == 2,
            lanes,
        ),
        check(
            "fill templates recorded",
            lanes["rank2_non_split_valpha"]["first_fill_template"].endswith("visible_rank2_l2_cohomology_data.template.json")
            and lanes["route_c_finite_hym_strominger"]["first_fill_template"] == "iwasawa_route_c_residuals.template.json",
            lanes,
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records source/operator distinction",
            "source-level support" in note and "operator-level identity" in note and "not `A_selected`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C operator-source identity subpacket audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
