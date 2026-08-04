"""Audit the selected U1/hypercharge operator-spectrum source packet gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1_hypercharge_operator_spectrum_source_packet.py"
DATA = REPO / "candidate_data" / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json"
CERT = REPO / "certificates" / "selected_u1_hypercharge_operator_spectrum_source_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Hypercharge_Operator_Spectrum_Source_Packet_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    tests = data["route_tests"]
    decision = data["decision"]

    check("status exact", data["status"] == "U1_HYPERCHARGE_OPERATOR_SPECTRUM_SOURCE_PACKET_BUILT_SPECTRUM_OPEN", data["status"])
    check("topology route rejected", tests["topology_only_hypercharge_embedding"]["status"] == "REJECTED_AS_SPECTRUM_SOURCE", tests["topology_only_hypercharge_embedding"])
    check("diagnostic spectral table rejected", tests["diagnostic_scalar_spectral_table"]["status"] == "REJECTED_PROXY_NOT_SELECTED_OPERATOR", tests["diagnostic_scalar_spectral_table"])
    check("qa logdet injection rejected", tests["qa_log2008_hypercharge_injection"]["status"] == "REJECTED_WRONG_SCHEME_AND_DOUBLE_PROMOTION", tests["qa_log2008_hypercharge_injection"])
    check("qa diagnostic is near but not used", 0 < tests["qa_log2008_hypercharge_injection"]["absolute_residual_to_witness"] < 0.25, tests["qa_log2008_hypercharge_injection"])
    check("primary packet open", tests["same_source_operator_spectrum_packet"]["status"] == "OPEN_PRIMARY_ROUTE" and len(tests["same_source_operator_spectrum_packet"]["required_fields"]) == 6, tests["same_source_operator_spectrum_packet"])
    check("decision refuses closure", decision["selected_U1_hypercharge_operator_spectrum_found"] is False and decision["selected_lambda_12_found"] is False and decision["target_fitting_used"] is False, decision)
    check("certificate agrees", cert["closed"]["acceptance_contract"] is True and cert["open"]["selected_positive_spectrum_and_multiplicities"] is True, cert)
    check("note records next object", "Selected_U1_Hypercharge_Section_Ring_or_Twisted_Module_Operator_Row_v1" in note and "target_fitting_used = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
