"""Audit the selected U1/Y Chern-Weil or projective rho_E operator-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_chern_weil_or_projective_rhoe_operator_row_source.py"
DATA = REPO / "candidate_data" / "selected_u1y_chern_weil_or_projective_rhoe_operator_row_source.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_chern_weil_or_projective_rhoe_operator_row_source_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Chern_Weil_or_Projective_RhoE_Operator_Row_Source_v1.md"


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
    imports = data["imported_reductions"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1Y_CHERN_WEIL_OR_PROJECTIVE_RHOE_ROW_SOURCE_GATE_BUILT_SAME_SOURCE_PAYLOAD_OPEN", data["status"])
    check("visible cw reduction imported", imports["selected_visible_cw_source"]["status"] == "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET", imports["selected_visible_cw_source"])
    check("routec c1 emission still open", imports["routec_c1_operator_emission"]["what_remains_open"]["emit_selected_A_selected"] is True and imports["routec_c1_operator_emission"]["what_remains_open"]["emit_selected_b_selected"] is True, imports["routec_c1_operator_emission"])
    check("zero dotd values open", imports["zero_mode_dotd_interface"]["completion_gates"]["all_D_operators_supplied"] is False and imports["zero_mode_dotd_interface"]["completion_gates"]["all_dotD_alpha1_operators_supplied"] is False, imports["zero_mode_dotd_interface"])
    check("payload has seven rows", len(data["required_payload"]) == 7, data["required_payload"])
    check("decision refuses closure", decision["selected_U1Y_chern_weil_or_projective_rhoE_row_found"] is False and decision["lambda_12_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["same_source_payload_cut_set_identified"] is True and cert["open"]["selected_source_certificate"] is True, cert)
    check("note records next object", "Selected_U1Y_Same_Source_Nonabelian_or_RouteC_Operator_Payload_v1" in note and "target_fitting_used = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
