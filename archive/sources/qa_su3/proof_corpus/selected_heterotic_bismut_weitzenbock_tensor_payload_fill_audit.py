"""Audit the Bismut-Weitzenbock tensor payload fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_bismut_weitzenbock_tensor_payload_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1.md"

STATUS = "HETEROTIC_BISMUT_WEITZENBOCK_TENSOR_PAYLOAD_PARTIAL_GEOMETRY_FILLED_BUNDLE_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_BundleCurvature_RepresentationTrace_or_DirectFiniteOperator_Fill_v1"


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
    payload = data["filled_payload"]
    summary = data["computed_summary"]
    flags = data["required_flags"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("structure equations", payload["geometric_tensors"]["supporting_structure_equations"]["de5"]["13"] > 0 and payload["geometric_tensors"]["supporting_structure_equations"]["de6"]["23"] > 0, payload["geometric_tensors"]["supporting_structure_equations"]),
        check("torsion filled", flags["torsion_H"] is True and "136" in payload["geometric_tensors"]["torsion_H_or_d_c_omega_components"], payload["geometric_tensors"]["torsion_H_or_d_c_omega_components"]),
        check("bismut coefficients filled", flags["Bismut_connection_coefficients"] is True and summary["nonzero_bismut_connection_coefficients"] > 0 and summary["all_bismut_coefficients_are_half_A_magnitude"] is True, summary),
        check("bundle/operator still open", flags["connection_A_components"] is False and flags["E_Qa_matrix"] is False and data["decision"]["E_Qa_computed"] is False, flags),
        check("missing bundle fields", {"R_plus_curvature_components", "connection_A_components", "curvature_F_A_components", "E_Qa_matrix"}.issubset(set(data["missing_fields"])), data["missing_fields"]),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "does not compute E_Qa" in note, NOTE),
    ]
    print("\nSelected heterotic Bismut-Weitzenbock tensor payload fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
