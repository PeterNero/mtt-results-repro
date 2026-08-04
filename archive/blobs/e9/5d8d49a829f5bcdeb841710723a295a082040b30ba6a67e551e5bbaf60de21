"""Audit Selected_C1_Operator_Source_Rebuild_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_c1_operator_source_rebuild_attempt_certificate.json"
SCRIPT = REPO / "scripts" / "attempt_selected_c1_operator_source_rebuild.py"
NOTE = REPO / "proof_corpus" / "Selected_C1_Operator_Source_Rebuild_Attempt_v1.md"


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
    closed = cert["what_closes_now"]
    summary = cert["slot_summary"]
    rejected = cert["illegal_or_diagnostic_sources_rejected"]
    not_closed = cert["what_remains_open"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_C1_OPERATOR_REBUILD_ATTEMPT_EXECUTED_SELECTED_BLOCKS_STILL_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "rebuild search executed",
        closed["rebuild_search_executed"] is True
        and closed["all_candidate_block_sources_classified"] is True
        and closed["minimal_rebuild_payload_specified"] is True,
        closed,
    )
    ok &= check(
        "no legal A or b emitted",
        summary["closure_possible_from_current_artifacts"] is False
        and cert["candidate_A_selected"] is None
        and cert["candidate_b_selected"] is None,
        summary,
    )
    ok &= check(
        "diagnostic sources rejected",
        rejected["diagnostic_noninvariant_C1_candidates"] is True
        and rejected["model_active_BN_DE_dotD_prefix"] is True
        and rejected["q79_template_principal_symbol_only"] is True,
        rejected,
    )
    ok &= check(
        "payload remains open",
        not_closed["emit_selected_A_selected"] is True
        and not_closed["emit_selected_b_selected"] is True
        and not_closed["selected_Hess_Xi_finite_blocks"] is True
        and not_closed["selected_sector_response_matrices"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails",
        guards["claims_A_selected_emitted"] is False
        and guards["claims_b_selected_emitted"] is False
        and guards["claims_flavor_closure"] is False,
        guards,
    )
    ok &= check(
        "note records template",
        "selected_routec_c1_operator_source_rebuild.payload.template.json" in note
        and "The attempt does not emit `A_selected` or `b_selected`." in note,
        NOTE,
    )

    print("\nSelected C1 operator-source rebuild attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
