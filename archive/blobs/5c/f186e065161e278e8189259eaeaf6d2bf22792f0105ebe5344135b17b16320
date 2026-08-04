"""Audit the heterotic HYM erratum/repair comparison gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_erratum_repair_comparison_gate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_erratum_repair_comparison_gate.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_erratum_repair_comparison_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_Erratum_Repair_Comparison_Gate_v1.md"

STATUS = "HETEROTIC_HYM_ERRATUM_REPAIR_COMPARISON_BUILT_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_HYM_RepairedPipeline_A_B_SourceSelection_or_Retirement_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    variants = data["variants"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("printed not integrable", decision["printed_integrable_under_standard_check"] is False and variants["printed_as_source"]["samples"][1]["integrability_residual_norm_squared"] == 3.0, variants["printed_as_source"]["samples"][1]),
        check("repair A integrable diagnostic", decision["repair_A_integrable"] is True and variants["repair_A_diagonal_B3"]["source_certified"] is False, variants["repair_A_diagonal_B3"]),
        check("repair B integrable diagnostic", decision["repair_B_integrable"] is True and variants["repair_B_one_entry_B2_move"]["source_certified"] is False, variants["repair_B_one_entry_B2_move"]),
        check("no repair selected", decision["any_repair_selected"] is False and decision["hym_route_retired_as_final_proof_source_until_repair_selection"] is True, decision),
        check("diagnostic blocks positive", all(v["samples"][1]["positive_modes"] >= 7 for v in variants.values()), variants),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records both repairs", "Repair A" in note and "Repair B" in note and "demoted" in note, NOTE),
    ]
    print("\nSelected heterotic HYM erratum repair comparison gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
