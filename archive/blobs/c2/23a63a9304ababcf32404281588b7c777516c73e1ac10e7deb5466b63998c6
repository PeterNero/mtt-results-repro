"""Audit D_E action on the smooth B_N scaffold."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
CERT = REPO / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    validation = data["validation"]
    matrix = validation["matrix_consistency"]
    straight = data["superset_mode"]["straight_path"]

    honest_text = "\n".join(validation["honest"]["output"])
    diagnostic_text = "\n".join(validation["diagnostic_source_lift"]["output"])

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_DE_ACTION_ON_SMOOTH_BN_MATRIX_BUILT_SOURCE_PROMOTION_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("payloads emitted", DATA.parent.joinpath("selected_routec_de_action_on_smooth_bn/de_action_on_smooth_bn.honest.json").exists(), data["payloads"]),
        check(
            "honest does not promote",
            validation["honest"]["exit_code"] == 1
            and "selected_source_verified is not true" in honest_text
            and straight["honest_validator_promotes"] is False,
            validation["honest"],
        ),
        check(
            "diagnostic passes",
            validation["diagnostic_source_lift"]["exit_code"] == 0
            and "D_E action validation PASS" in diagnostic_text
            and straight["diagnostic_lift_passes"] is True,
            validation["diagnostic_source_lift"],
        ),
        check(
            "matrix consistency",
            matrix["domain_dimension"] == 27
            and matrix["family_kernel_dimension"] == 3
            and matrix["higgs_kernel_dimension"] == 1
            and matrix["diagnostic_lift_validator_passes"] is True,
            matrix,
        ),
        check(
            "not full operator",
            data["what_remains_open"]["full_iwasawa_strominger_DE_action_not_only_model_active"] is True
            and data["what_remains_open"]["selected_D_E_source_promotion"] is True,
            data["what_remains_open"],
        ),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1",
            data["next_required_artifact"],
        ),
        check("note records caveat", "honest packet is still unpromoted" in note, NOTE),
    ]
    print("\nMTT selected Route-C DE action on smooth BN audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
