"""Audit the selected heterotic R+ curvature payload fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_rplus_curvature_payload_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_rplus_curvature_payload_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_rplus_curvature_payload_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_RPlus_Curvature_Payload_Fill_v1.md"

STATUS = "HETEROTIC_RPLUS_CURVATURE_PAYLOAD_FILLED_BUNDLE_OPERATOR_OPEN"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("R+ filled", data["decision"]["R_plus_curvature_filled"] is True and cert["R_plus_curvature_filled"] is True, data["decision"])
    check("no E_Qa promotion", data["decision"]["E_Qa_computed"] is False and cert["E_Qa_computed"] is False, data["decision"])
    check("bundle still open", data["decision"]["bundle_tensor_payload_filled"] is False and cert["bundle_tensor_payload_filled"] is False, data["decision"])

    summary = data["rplus_payload"]["R_plus_summary"]
    check("curvature nonzero", summary["nonzero_ij_matrices"] > 0 and summary["nonzero_components"] > 0, summary)
    check("curvature bounded", 0 < summary["max_abs_component"] < 1.0, summary)
    check("formula recorded", "[Gamma_i,Gamma_j]" in data["rplus_payload"]["formula"], data["rplus_payload"]["formula"])

    tensors = data["filled_payload"]["geometric_tensors"]
    check("geometric tensors retained", tensors["Bismut_connection_coefficients"] and tensors["torsion_H_or_d_c_omega_components"], list(tensors))
    check("R+ components attached", isinstance(tensors["R_plus_curvature_components"], dict) and len(tensors["R_plus_curvature_components"]) == summary["nonzero_components"], summary)

    missing = set(data["missing_fields"])
    required_missing = {
        "connection_A_components",
        "curvature_F_A_components",
        "ad_bundle_representation",
        "trace_normalization",
        "E_Qa_matrix",
        "kernel_and_quotient_policy",
        "gamma_nk_inverse_table",
    }
    check("remaining bundle/operator fields", required_missing <= missing, sorted(missing))
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records theorem", "does not compute `E_Qa`" in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic R+ curvature payload fill audit")


if __name__ == "__main__":
    main()
