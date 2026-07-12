"""Audit the post-HYM local-system torsion or new-operator attack packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_local_system_torsion_or_new_operator_attack.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_local_system_torsion_or_new_operator_attack.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_local_system_torsion_or_new_operator_attack_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_projective_or_endomorphism_operator_source.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_LocalSystemTorsion_or_NewOperatorSource_Attack_v1.md"

STATUS = "HETEROTIC_LOCAL_SYSTEM_TORSION_OR_NEW_OPERATOR_ATTACK_BUILT_ENDOMORPHISM_PRIMARY"
NEXT = "Selected_Heterotic_ProjectiveCarrier_or_EndomorphismOperator_SourcePacket_v1"


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
    routes = data["route_tests"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("rank one closed negative", routes["ordinary_rank_one_local_system"]["passes"] is False and decision["ordinary_rank_one_torsion_route_closed_negative_for_q64"] is True, routes["ordinary_rank_one_local_system"]),
        check("su3 scalar closed negative", routes["scalar_su3_center"]["passes"] is False, routes["scalar_su3_center"]),
        check("q64 bridge partial", routes["q64_bridge_to_Qa_SU3"]["bridge_closed"] is False and "torsion_finite_part" in routes["q64_bridge_to_Qa_SU3"]["missing_bridge_requirements"], routes["q64_bridge_to_Qa_SU3"]),
        check("projective auxiliary", routes["projective_clock_shift"]["mathematical_possibility"] is True and decision["q64_projective_route_open_auxiliary"] is True, routes["projective_clock_shift"]),
        check("endomorphism primary", decision["selected_primary_route"] == "source_certified_endomorphism_E_full_operator" and routes["new_endomorphism_operator_source"]["status"] == "PRIMARY_NEXT_ROUTE_SOURCE_MISSING", decision),
        check("template has two main routes", template["route_A_projective_carrier"]["minimal_clock_shift_dimension"] == 64 and template["route_B_endomorphism_operator"]["endomorphism_E_or_Weitzenbock_zero_order_block"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "Heisenberg center" in note and "source-certified endomorphism_E" in note, NOTE),
    ]
    print("\nSelected heterotic local-system torsion or new-operator attack audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
