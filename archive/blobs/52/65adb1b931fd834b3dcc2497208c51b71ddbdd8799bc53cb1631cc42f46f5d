"""Audit the selected Qa/SU3 typed monad data fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "typed_monad_data_fill_attempt_certificate.json"
DATA = REPO / "candidate_data" / "typed_monad_data_fill_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "build_typed_monad_data_fill_attempt.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    fill = data["fill_result"]
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_BLOCKED_TYPED_MAPS_MISSING", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("topology filled", fill["topological_monad_data_filled"] is True and data["fillable_from_source"]["c3_integral"] == 6, data["fillable_from_source"]),
        check("typed maps missing", fill["typed_maps_filled"] is False and gates["typed_f_g_maps"] == "FAIL_SOURCE_PRINTED_GENERIC_ONLY", gates),
        check("operator absent", fill["de_operator_packet_filled"] is False and fill["rhoE_packet_filled"] is False, fill),
        check("validator open", fill["validator_on_open_template_exit_2"] is True, data["template_validator_result"]),
        check("no closure", fill["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "typed maps filled: no" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 typed monad data fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
