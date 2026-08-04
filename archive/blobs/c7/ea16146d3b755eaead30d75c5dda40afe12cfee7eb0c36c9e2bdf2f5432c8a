"""Audit the external noninvariant C1 candidate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_external_noninvariant_c1_candidate_import.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_external_noninvariant_c1_candidate_import_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_External_NonInvariant_C1_Candidate_Import_v1.md"

STATUS = "U1Y_ROUTEC_EXTERNAL_NONINVARIANT_C1_CANDIDATES_IMPORTED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    facts = data["imported_facts"]
    state = data["selection_state"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("active shift imported", facts["minimal_active_shift_required"] == [1, 1] and cert["minimal_active_shift_required"] == [1, 1], facts),
        check("nonzero candidates imported", facts["nonzero_unselected_candidate_count"] == 4 and data["candidate_summary"]["candidate_count"] == 4, data["candidate_summary"]),
        check("fiber class reduction", facts["fixed_fiber_shifts_one_qutrit_gauge_class"] is True and facts["all_fiber_envelope_retired"] is True, facts),
        check("basis transport candidate", facts["basis_transport_heavy_link_candidate"] is True and cert["basis_transport_candidate_imported"] is True, facts),
        check("not selected", state["selected_noninvariant_primitive_source_proved"] is False and cert["selected_C1_closed"] is False, state),
        check("no downstream closure", cert["A_selected_computable"] is False and cert["b_selected_computable"] is False and cert["lambda_12_computable"] is False, cert),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records useful external clue", "other repos do help" in note and "fiber-origin" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C external noninvariant C1 candidate import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
