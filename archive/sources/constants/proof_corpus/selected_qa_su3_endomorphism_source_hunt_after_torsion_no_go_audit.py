"""Audit the Qa/SU3 endomorphism source hunt after torsion no-go."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Endomorphism_Source_Hunt_After_Torsion_No_Go_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def route(cert: dict, route_id: str) -> dict:
    for item in cert["candidate_routes"]:
        if item["route"] == route_id:
            return item
    raise AssertionError(route_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["source_hunt_result"]
    direct = route(cert, "direct_selected_qa_su3_endomorphism_E")
    visible = route(cert, "visible_fuyau_strominger_template_transfer")

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_ENDOMORPHISM_SOURCE_HUNT_AFTER_TORSION_NO_GO_BUILT_SOURCE_STILL_MISSING",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["source_hunt_result"] == cert["source_hunt_result"]
            and computed["next_required_artifact"] == cert["next_required_artifact"],
            computed["source_hunt_result"],
        ),
        check(
            "direct endomorphism still missing",
            direct["status"] == "MISSING"
            and result["selected_endomorphism_E_found"] is False
            and result["selected_qa_su3_operator_source_found"] is False,
            {"direct": direct, "result": result},
        ),
        check(
            "visible Fu-Yau route scoped as template only",
            visible["status"] == "TEMPLATE_ONLY_NOT_QA_SU3_SOURCE"
            and result["visible_fuyau_template_found"] is True
            and result["visible_template_legally_transfers_to_qa_su3"] is False,
            {"visible": visible, "result": result},
        ),
        check(
            "closure not overclaimed",
            result["qa_su3_closed"] is False
            and result["full_sm_closure_achieved"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "source checks include visible blocker and Fu-Yau packet",
            cert["source_checks"]["visible_operator_source_blocker"]["present"] is True
            and cert["source_checks"]["z7_fuyau_mukai_charge_sector"]["present"] is True,
            cert["source_checks"],
        ),
        check(
            "forbidden shortcuts recorded",
            "Z7 Fu-Yau/Mukai charge-sector closure as Qa/SU3 determinant closure" in cert["do_not_use"]
            and "retired HYM matrix entries as endomorphism_E" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records next packet interface",
            "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1" in note
            and "visible Fu-Yau/Strominger material: construction template only" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 endomorphism source hunt after torsion no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
