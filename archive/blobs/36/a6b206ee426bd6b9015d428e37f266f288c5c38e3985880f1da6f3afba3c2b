"""Audit the HYM repair source-selection or retirement theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_repair_source_selection_or_retirement.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_repair_source_selection_or_retirement.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_repair_source_selection_or_retirement_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_post_hym_retirement_operator_or_torsion_source.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_Repair_SourceSelection_or_Retirement_v1.md"

STATUS = "HETEROTIC_HYM_REPAIR_SOURCE_SELECTION_CURRENT_SOURCE_RETIREMENT_PROVED"
NEXT = "Selected_Heterotic_LocalSystemTorsion_or_NewOperatorSource_Attack_v1"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    resolution = data["repair_resolution"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("printed retired", decision["printed_hym_matrix_route_retired_current_source"] is True and resolution["printed_matrix"]["status"] == "BLOCKED_NONINTEGRABLE", resolution["printed_matrix"]),
        check("repair A retired", decision["repair_A_retired_current_branch"] is True and resolution["repair_A"]["extra_noncentral_stabilizer"] is True and resolution["repair_A"]["source_certified"] is False, resolution["repair_A"]),
        check("repair B current no-go", decision["repair_B_current_source_no_go"] is True and resolution["repair_B"]["current_source_no_go"] is True and resolution["repair_B"]["source_certified"] is False, resolution["repair_B"]),
        check("strict route still live but shifted", decision["strict_no_knob_heterotic_route_still_live"] is True and decision["primary_next_route"] == "local_system_torsion_or_new_operator_source", decision),
        check("template forbids shortcuts", "promote Repair A under the selected indecomposable rank-3 branch" in template["forbidden"] and template["primary_non_hym_route"]["selected_compact_nil_or_iwasawa_character"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "Repair B" in note and "current corpus does not emit" in note and "Post-Retirement" in note, NOTE),
    ]
    print("\nSelected heterotic HYM repair source-selection or retirement audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
