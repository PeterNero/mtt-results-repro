"""Audit rank-two L2 cohomology or Route-C residual fill checkpoint."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_rank2_l2_or_routec_residual_fill.candidate.json"
CERT = REPO / "certificates" / "selected_routec_rank2_l2_or_routec_residual_fill_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_RANK2_L2_COHOMOLOGY_FILL_CLOSED_STABILITY_OR_ROUTEC_RESIDUAL_OPEN"
NEXT = "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    l2 = data["rank2_l2_fill"]
    ordered = data["ordered_source_fill"]
    impact = data["operator_identity_impact"]
    remaining = data["what_remains_open"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False and impact["selected_operator_identity_closed"] is False, impact),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check(
            "l2 validator passes",
            l2["validator"]["exit_code"] == 0
            and l2["reported_cohomology"]["h1"] == 8
            and l2["closed_now"]["nonzero_ext_class_selected"] is True,
            l2,
        ),
        check(
            "ordered source validator passes",
            ordered["validator"]["exit_code"] == 0
            and ordered["closed_now"]["ordered_L_branch_selected_for_chern_h1_layer"] is True
            and ordered["closed_now"]["operator_layer_pic0_recheck_still_open"] is True,
            ordered,
        ),
        check(
            "stability and operator gates remain open",
            remaining["non_split_stability_or_hym_proved"] is True
            and remaining["same_source_D_E_rhoE_Riesz_Green_dotD"] is True
            and remaining["selected_operator_identity_closed"] is False,
            remaining,
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records partial closure",
            "rank-two arithmetic fill is no longer the blocker" in note
            and "selected" in note
            and "operator source is still open" in note.replace("\n", " "),
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C rank-two L2/Route-C residual fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
