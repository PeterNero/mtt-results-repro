"""Audit Selected_C1_Response_Operator_Emission_Audit_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_c1_response_operator_emission_audit_import_certificate.json"
SCRIPT = REPO / "scripts" / "import_selected_c1_response_operator_emission_audit.py"
NOTE = REPO / "proof_corpus" / "Selected_C1_Response_Operator_Emission_Audit_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    closed = cert["closed_now"]
    result = cert["audit_result"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "audit gate closes",
        closed["selected_response_operator_schema_audited"] is True
        and closed["A_selected_emission_blocker_identified"] is True
        and closed["target_fitting_excluded"] is True,
        closed,
    )
    ok &= check(
        "A and b remain absent",
        result["selected_operator_A_selected_emitted"] is False
        and result["selected_source_vector_b_selected_emitted"] is False
        and result["least_squares_now_computable"] is False
        and result["rank_test_now_computable"] is False,
        result,
    )
    ok &= check(
        "true finite blocks remain open",
        not_closed["emit_selected_A_selected"] is True
        and not_closed["emit_selected_b_selected"] is True
        and not_closed["selected_sector_response_matrices"] is True
        and not_closed["solve_or_reject_splitter_equation"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent solve overclaim",
        guards["claims_A_selected_emitted"] is False
        and guards["claims_b_selected_emitted"] is False
        and guards["claims_deltaTheta_C1_solved"] is False
        and guards["claims_flavor_closure"] is False,
        guards,
    )
    ok &= check(
        "note records rebuild gate",
        "Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1" in note
        and "A_selected emitted: no" in note,
        NOTE,
    )

    print("\nSelected C1 response-operator emission audit import")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
