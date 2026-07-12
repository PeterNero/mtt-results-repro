"""Audit the Qa/SU3 alternative operator/projector source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_alternative_operator_or_projector_source_hunt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Alternative_Operator_or_Projector_Source_Hunt_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_alternative_operator_or_projector_source_hunt.py"


def check(name: str, ok: bool, detail: object) -> None:
    if not ok:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)

    check(
        "certificate status",
        cert["status"] == "QA_SU3_ALTERNATIVE_OPERATOR_OR_PROJECTOR_SOURCE_HUNT_CERTIFIED_OPEN",
        cert["status"],
    )
    check(
        "script agrees with certificate",
        computed["ranking"] == cert["ranking"]
        and computed["input_obstruction"] == cert["input_obstruction"],
        computed["ranking"],
    )
    routes = {route["id"]: route for route in cert["candidate_routes"]}
    check(
        "local FP quotient not reused",
        routes["local_fp_brs_quotient_jacobian"]["status"] == "EXHAUSTED_ALREADY_COUNTED"
        and routes["local_fp_brs_quotient_jacobian"]["legal_as_extra_correction"] is False,
        routes["local_fp_brs_quotient_jacobian"],
    )
    check(
        "best next route selected as open gate",
        cert["ranking"]["best_next_route"]
        == "nontrivial_su3_color_bundle_connection_endomorphism"
        and routes["nontrivial_su3_color_bundle_connection_endomorphism"]["status"]
        == "BEST_NEXT_OPEN_GATE",
        cert["ranking"],
    )
    check(
        "no target fitting",
        cert["verdict"]["target_fitting_used"] is False
        and cert["verdict"]["full_SM_closure_achieved"] is False,
        cert["verdict"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check(
        "note records next determinant gate",
        "Selected_Qa_SU3_Color_Bundle_Connection_or_Global_Section_Determinant_v1" in note
        and "nontrivial SU3 color-bundle" in note,
        NOTE,
    )
    print("\nSelected Qa/SU3 alternative operator or projector source-hunt audit")


if __name__ == "__main__":
    main()
