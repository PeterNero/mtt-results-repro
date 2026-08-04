"""Audit the source-certified A01 erratum or monad D_E exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_source_certified_a01_erratum_or_monad_de_operator_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Certified_A01_Erratum_or_Monad_DE_Operator_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_source_certified_a01_erratum_or_monad_de_operator.py"


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


def path_by_id(cert: dict, path_id: str) -> dict:
    for item in cert["exit_paths"]:
        if item["id"] == path_id:
            return item
    raise AssertionError(path_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    decision = cert["decision"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SOURCE_CERTIFIED_OPERATOR_EXIT_GATE_BUILT_NO_EXIT_CLOSED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["decision"] == cert["decision"]
            and computed["best_next_action"] == cert["best_next_action"],
            computed["decision"],
        ),
        check(
            "source scan distinguishes named maps from printed data",
            cert["source_scan"]["interpretation"]["monad_maps_named_but_not_printed"] is True
            and cert["source_scan"]["interpretation"]["finite_rhoE_or_cech_packet_printed"] is False,
            cert["source_scan"],
        ),
        check(
            "A01 erratum exit remains open",
            path_by_id(cert, "source_certified_a01_erratum")["status"] == "OPEN_NOT_SOURCE_CERTIFIED"
            and path_by_id(cert, "source_certified_a01_erratum")["can_close_now"] is False,
            path_by_id(cert, "source_certified_a01_erratum"),
        ),
        check(
            "direct monad D_E exit remains open with exact missing data",
            path_by_id(cert, "direct_monad_de_operator")["status"] == "OPEN_MISSING_TYPED_MONAD_MAPS_AND_OPERATOR"
            and "actual typed maps f,g are not printed" in path_by_id(cert, "direct_monad_de_operator")["blocking_data"],
            path_by_id(cert, "direct_monad_de_operator"),
        ),
        check(
            "rhoE exit remains open",
            path_by_id(cert, "finite_rhoE_transition_packet")["status"] == "OPEN_NO_PACKET"
            and path_by_id(cert, "finite_rhoE_transition_packet")["can_close_now"] is False,
            path_by_id(cert, "finite_rhoE_transition_packet"),
        ),
        check(
            "no closure claimed",
            decision["operator_packet_fillable_now"] is False
            and decision["endomorphism_E_computable_now"] is False
            and decision["determinant_computable_now"] is False
            and decision["qa_su3_closed"] is False
            and decision["target_fitting_used"] is False,
            decision,
        ),
        check(
            "best next action is typed monad data interface",
            cert["best_next_action"]["name"] == "typed monad / Dolbeault operator data request"
            and "explicit f and g maps with source/target line-bundle types" in cert["best_next_action"]["required_packet"],
            cert["best_next_action"],
        ),
        check(
            "note records typed monad interface next",
            "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1" in note
            and "Qa/SU3 closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 source-certified A01 erratum or monad D_E gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
