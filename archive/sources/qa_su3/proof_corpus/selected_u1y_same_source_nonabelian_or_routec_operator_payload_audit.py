"""Audit the selected U1/Y same-source nonabelian or Route-C payload attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_same_source_nonabelian_or_routec_operator_payload.py"
DATA = REPO / "candidate_data" / "selected_u1y_same_source_nonabelian_or_routec_operator_payload.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_same_source_nonabelian_or_routec_operator_payload_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Same_Source_Nonabelian_or_RouteC_Operator_Payload_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def lane(data: dict, lane_id: str) -> dict:
    for item in data["lane_attempts"]:
        if item["lane_id"] == lane_id:
            return item
    raise AssertionError(lane_id)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    routec = lane(data, "B_routec_finite_hym_strominger_c1_payload")
    projective = lane(data, "C_projective_gerbe_rhoE_packet")
    visible = lane(data, "A_nonabelian_visible_bundle_sheaf_chern_weil")

    check("status exact", data["status"] == "U1Y_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PAYLOAD_ATTEMPTED_OPERATOR_TABLES_OPEN", data["status"])
    check("three lanes present", len(data["lane_attempts"]) == 3, [item["lane_id"] for item in data["lane_attempts"]])
    check("projector support closed only as support", data["closed_support"]["u1_pperp_projector_index_policy"] is True and decision["selected_projector_compatibility_found"] is True, data["closed_support"])
    check("routec rejected for A/b", routec["accepted"] is False and "A_selected" in routec["missing_fields"] and "b_selected" in routec["missing_fields"], routec)
    check("projective rejected for operator tables", projective["accepted"] is False and "projective_rhoE_operator_tables" in projective["missing_fields"], projective)
    check("visible rejected for source/operator row", visible["accepted"] is False and "source_certificate" in visible["missing_fields"] and "selected_U1Y_bundle_sheaf_or_operator_row" in visible["missing_fields"], visible)
    check("closure refused", decision["selected_U1Y_same_source_payload_found"] is False and decision["lambda_12_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["three_lane_plan_executed"] is True and cert["open"]["selected_operator_tables"] is True and cert["accepted_lanes"] == [], cert)
    check("note records next object", "Selected_U1Y_RouteC_or_ProjectiveRhoE_Selected_Operator_Tables_v1" in note and "lambda_12_closed = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
