"""Audit the heterotic/Strominger electroweak threshold-kernel fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_strominger_electroweak_threshold_kernel.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_strominger_electroweak_threshold_kernel_certificate.json"
PAYLOAD = ROOT / "candidate_data" / "selected_heterotic_strominger_electroweak_threshold_kernel_minimal_payload.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_Strominger_Electroweak_Threshold_Kernel_v1.md"

STATUS = "HETEROTIC_STROMINGER_EW_KERNEL_FILL_ATTEMPT_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_Strominger_AnalyticTorsion_or_ThresholdOperator_Payload_v1"


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
    payload = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    tests = data["fill_tests"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("tree level slot filled", decision["tree_level_gauge_kinetic_slot_filled"] is True and tests["gauge_kinetic_payload"]["tree_level_universal_function"].startswith("f=S"), tests["gauge_kinetic_payload"]),
        check("kernel still open", decision["selected_heterotic_strominger_kernel_closed"] is False and decision["analytic_torsion_or_threshold_operator_closed"] is False, decision),
        check("internal lambda carried", abs(decision["internal_lambda_12_value"] - 2.6179362173268497) < 1e-12, decision),
        check("q79 not promoted", tests["q79_fuyau_import"]["charge_sector_closed"] is True and tests["q79_fuyau_import"]["usable_as_electroweak_threshold_kernel"] is False, tests["q79_fuyau_import"]),
        check("stack determinant values open", tests["threshold_payload"]["stack_determinant_source_certified"] is False and tests["threshold_payload"]["one_loop_or_analytic_torsion_operator_found"] is False, tests["threshold_payload"]),
        check("payload requires torsion/operator", payload["status"] == "OPEN_SELECTED_THRESHOLD_OPERATOR_OR_TORSION_REQUIRED" and payload["must_emit"]["threshold_operator_or_torsion"]["positive_spectrum_or_torsion_finite_part"] is None, payload),
        check("matching remains open", decision["matching_scale_closed"] is False and decision["RG_scheme_closed"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note names minimal payload", NEXT in note and "tree-level universal gauge kinetic slot" in note, NOTE),
    ]
    print("\nSelected heterotic/Strominger electroweak threshold-kernel audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
