"""Audit the source-certified A01 erratum or monad D_E exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "source_certified_a01_erratum_or_monad_de_operator_certificate.json"
DATA = REPO / "candidate_data" / "source_certified_a01_erratum_or_monad_de_operator.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Certified_A01_Erratum_or_Monad_DE_Operator_v1.md"
SCRIPT = REPO / "scripts" / "build_source_certified_a01_erratum_or_monad_de_operator.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def path_by_id(data: dict[str, object], path_id: str) -> dict[str, object]:
    return next(row for row in data["exit_paths"] if row["id"] == path_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "QA_SU3_SOURCE_CERTIFIED_OPERATOR_EXIT_GATE_BUILT_NO_EXIT_CLOSED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("scan distinguishes data", data["source_scan"]["interpretation"]["monad_maps_named_but_not_printed"] is True and data["source_scan"]["interpretation"]["finite_rhoE_or_cech_packet_printed"] is False, data["source_scan"]),
        check("A01 exit open", path_by_id(data, "source_certified_a01_erratum")["status"] == "OPEN_NOT_SOURCE_CERTIFIED", path_by_id(data, "source_certified_a01_erratum")),
        check("monad DE best route open", path_by_id(data, "direct_monad_de_operator")["status"] == "OPEN_MISSING_TYPED_MONAD_MAPS_AND_OPERATOR" and data["best_next_action"]["name"] == "typed monad / Dolbeault operator data request", data["best_next_action"]),
        check("rhoE exit open", path_by_id(data, "finite_rhoE_transition_packet")["status"] == "OPEN_NO_PACKET", path_by_id(data, "finite_rhoE_transition_packet")),
        check("no closure", decision["operator_packet_fillable_now"] is False and decision["qa_su3_closed"] is False and cert["closure_claimed"] is False, decision),
        check("note records next", cert["next_required_artifact"] in note and "Qa/SU3 closed: no" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 source-certified A01 erratum or monad D_E gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
