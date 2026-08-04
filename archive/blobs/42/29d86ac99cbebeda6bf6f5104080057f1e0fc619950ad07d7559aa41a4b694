"""Audit higher-order/full-response flavor-splitting criterion."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
CERT = REPO / "certificates" / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    current = data["current_layer_no_go"]
    path_a = data["path_A_higher_order_criterion"]
    path_b = data["path_B_full_response_criterion"]
    diagnostics = current["diagnostics"]

    all_scalar = all(
        sector["YYstar_scalar_test"]["is_scalar_identity"] is True
        for sector in diagnostics.values()
    )
    all_rank3 = all(sector["rank_from_previous"] == 3 for sector in diagnostics.values())
    required_outputs = path_b["required_outputs"]

    checks = [
        check(
            "status",
            data["status"]
            == "MTT_SELECTED_ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_CRITERION_BUILT_VALUES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "repo updates checked",
            data["repo_update_check"]["action"] == "continue without reverting or cleaning accumulated artifacts",
            data["repo_update_check"],
        ),
        check("current layer no-go", current["proved"] is True and all_scalar and all_rank3, current),
        check(
            "higher-order criterion locked",
            path_a["proved"] is True
            and "traceless" in path_a["mass_splitting_condition"]
            and "commutator" in path_a["mixing_condition"]
            and path_a["current_values_available"] is False,
            path_a,
        ),
        check(
            "full-response criterion locked",
            path_b["proved"] is True
            and all(required_outputs.values())
            and path_b["current_values_available"] is False,
            path_b,
        ),
        check(
            "open selected values",
            data["what_remains_open"]["selected_higher_order_correction_matrices"] is True
            and data["what_remains_open"]["selected_full_response_matrices"] is True
            and data["what_remains_open"]["CKM_PMNS_CP_from_selected_matrices"] is True,
            data["what_remains_open"],
        ),
        check(
            "no closure claim or target fit",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "next artifact",
            data["next_required_artifact"]
            == "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records no-go and criteria",
            "Current-Layer No-Go" in note
            and "Higher-Order Criterion" in note
            and "Full-Response Criterion" in note
            and "does not compute selected correction values" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C higher-order/full-response flavor-splitting audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
