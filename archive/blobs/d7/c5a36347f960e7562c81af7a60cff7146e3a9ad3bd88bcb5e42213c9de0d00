"""Audit the selected U1/Y Route-C or projective rhoE operator-table gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_or_projective_rhoe_selected_operator_tables.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_or_ProjectiveRhoE_Selected_Operator_Tables_v1.md"


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
    routec = data["routec_operator_table"]
    projective = data["projective_rhoE_table"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1Y_ROUTEC_OR_PROJECTIVE_RHOE_OPERATOR_TABLES_CONSTRUCTED_CONDITIONAL_SELECTED_TABLES_OPEN", data["status"])
    check("routec conditional table exact", routec["shape"] == [72, 2] and routec["rank"] == 2 and routec["relative_residual"] < 1e-12, routec)
    check("routec not selected", routec["selected_operator_table_emitted"] is False and routec["promote_to_A_selected"] is False and routec["promote_to_b_selected"] is False, routec)
    check("routec validator no-go imported", len(routec["validator_errors"]) >= 7 and any("source_identity" in item for item in routec["validator_errors"]), routec["validator_errors"])
    check("projective validator present but not selected", projective["mesh_validator_ready"] is True and projective["projective_mismatch_count"] == 0 and projective["selected_operator_table_emitted"] is False, projective)
    check("projective operator level open", projective["source_level_projective_gerbe_promoted"] is True and projective["operator_level_projective_rhoE_promoted"] is False, projective)
    check("closure refused", decision["selected_operator_tables_emitted"] is False and decision["lambda_12_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["routec_conditional_A_table_constructed"] is True and cert["open"]["selected_DE_dotD_Riesz_Green_values"] is True, cert)
    check("note records next object", "Selected_U1Y_Stability_HYM_or_RouteC_Residual_Source_v1" in note and "lambda_12_closed = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
