"""Audit the heterotic projective-carrier or endomorphism-operator source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projective_carrier_or_endomorphism_operator_source_packet_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_endomorphism_threshold_value_packet.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveCarrier_or_EndomorphismOperator_SourcePacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVE_CARRIER_OR_ENDOMORPHISM_SOURCE_PACKET_BUILT_ENDOMORPHISM_VALUE_CONTRACT_OPEN"
NEXT = "Selected_Heterotic_Endomorphism_Threshold_ValuePacket_Fill_v1"


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
    projective = data["route_A_projective_carrier"]
    endomorphism = data["route_B_endomorphism_operator"]
    global_measure = data["route_C_global_measure"]
    decision = data["decision"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("projective algebra closed", projective["algebraic_carrier_certified"] is True and projective["minimal_dimension"] == 64, projective),
        check("projective not promoted", projective["selected_closure"] is False and decision["projective_carrier_selected_threshold_proof"] is False, projective),
        check("endomorphism contract built", endomorphism["selected_primary_route"] is True and "endomorphism_E" in endomorphism["operator_formula_contract"]["zero_order_block"], endomorphism),
        check("endomorphism values open", endomorphism["current_selected_source_found"] is False and decision["selected_values_available"] is False, endomorphism),
        check("global measure backup", global_measure["verdict"] == "BACKUP_ONLY_UNTIL_NO_DOUBLE_COUNT_PROOF", global_measure),
        check("template fields", template["operator_blocks"]["endomorphism_E_or_Weitzenbock_zero_order_block"] is None and template["normalization_and_output"]["computed_dimensionless_finite_part"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "exact U64 clock-shift" in note and "same-branch selected endomorphism_E" in note, NOTE),
    ]
    print("\nSelected heterotic projective-carrier or endomorphism-operator source packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
