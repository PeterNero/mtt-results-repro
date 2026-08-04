"""Audit the U1/Y minimal source-amendment or direct-operator-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.py"
DATA = REPO / "candidate_data" / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json"
CERT = REPO / "certificates" / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Hypercharge_Minimal_Source_Amendment_or_Direct_Operator_Row_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    tests = data["direct_operator_row_tests"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1_HYPERCHARGE_MINIMAL_SOURCE_AMENDMENT_GATE_BUILT_OPERATOR_ROW_OPEN", data["status"])
    check("six amendment fields audited", len(data["source_amendment_fields"]) == 6, data["source_amendment_fields"])
    check("projective route partial only", tests["projective_s3_gerbe_promotion"]["promoted_now"] is True and tests["projective_s3_gerbe_promotion"]["operator_level_promoted"] is False, tests["projective_s3_gerbe_promotion"])
    check("twisted route operator open", tests["twisted_gerbe_fill_attempt"]["operator_exit_available"] is False and tests["twisted_gerbe_fill_attempt"]["determinant_computable_now"] is False, tests["twisted_gerbe_fill_attempt"])
    check("valpha conditional only", tests["visible_rank2_valpha_lane"]["conditional_h1"] == 8 and tests["visible_rank2_valpha_lane"]["selected_source_promotes"] is False, tests["visible_rank2_valpha_lane"])
    check("integral lift selector required", tests["integral_lift_gap"]["status"] == "SELECTOR_REQUIRED_NOT_OPERATOR_ROW", tests["integral_lift_gap"])
    check("decision refuses closure", decision["direct_operator_row_found"] is False and decision["source_amendment_currently_sufficient"] is False and decision["lambda_12_closed"] is False, decision)
    check("certificate agrees", cert["closed"]["strongest_live_route_identified"] is True and cert["open"]["selected_U1Y_operator_row"] is True, cert)
    check("note records next object", "Selected_U1Y_Chern_Weil_or_Projective_RhoE_Operator_Row_Source_v1" in note and "target_fitting_used = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
