"""Audit the local recomputation of sparse A01 repair candidates."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "a01_repair_guardrail_local_recompute_certificate.json"
DATA = REPO / "candidate_data" / "a01_repair_guardrail_local_recompute.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_A01_Repair_Guardrail_Local_Recompute_v1.md"
SCRIPT = REPO / "scripts" / "build_a01_repair_guardrail_local_recompute.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def by_label(data: dict[str, object], label: str) -> dict[str, object]:
    for item in data["local_recompute"]:
        if item["label"] == label:
            return item
    raise KeyError(label)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    printed = by_label(data, "printed_A01")
    repair_a = by_label(data, "repair_A_diagonal_B3")
    repair_b = by_label(data, "repair_B_move_B2_to_minus_E32")
    checks = [
        check("status", cert["status"] == "QA_SU3_A01_REPAIR_GUARDRAIL_LOCAL_RECOMPUTED_REPAIR_B_FULL_MC_PASSES_NOT_SOURCE_CERTIFIED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("printed fails full MC", printed["full_maurer_cartan_passes"] is False and printed["reduced_F12_passes"] is False, printed),
        check("repair A reduced only", repair_a["reduced_F12_passes"] is True and repair_a["full_maurer_cartan_passes"] is False, repair_a),
        check("repair B full MC passes", repair_b["reduced_F12_passes"] is True and repair_b["full_maurer_cartan_passes"] is True, repair_b),
        check("repair B is not source certified", data["decisions"]["repair_B_source_certified"] is False and data["decisions"]["repair_B_accepted_as_operator_exit"] is False, data["decisions"]),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", data["next_required_artifact"] in note and "Repair B is not source-certified" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 A01 repair guardrail local recompute audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
