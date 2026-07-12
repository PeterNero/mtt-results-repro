"""Audit BN27 direct finitepart functional / source-owned logdet theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceowned_logdet_theorem_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_DirectFinitePartFunctional_or_SourceOwnedLogdetTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_DIRECT_FINITEPART_ARITHMETIC_CLOSED_SOURCEOWNED_LOGDET_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_SourceTheorem_or_KernelTraceOwnership_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    payload = data["arithmetic_payload"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("arithmetic closed", decision["direct_finitepart_arithmetic_closed"] is True and payload["oriented_abs_sector_product"] == payload["plus_sector_product"] * payload["minus_sector_product"], payload)
    check("expected products", payload["plus_sector_product"] == 9600 and payload["minus_sector_product"] == 9600 and payload["oriented_abs_sector_product"] == 92160000, payload)
    check("logdet exact", payload["oriented_abs_sector_logdet_exact"] == "log(92160000)" and cert["direct_finitepart_arithmetic_closed"] is True, payload)
    check("source-owned still open", decision["source_owned_finitepart_functional_closed"] is False and cert["source_owned_finitepart_functional_closed"] is False, decision)
    check("kernel trace not source-owned", decision["kernel_trace_source_owned"] is False and data["lane_evaluation"]["kernel_trace_ownership"]["source_owned"] is False, data["lane_evaluation"]["kernel_trace_ownership"])
    check("source identity open", decision["source_object_named_S_QaSU3_BN27"] is False and decision["BN27_source_identity_closed"] is False, decision)
    check("contract required nulls", all(value is None for value in contract["must_emit"].values()), contract["must_emit"])
    check("contract preserves guardrails", all(contract["must_preserve"].values()), contract["must_preserve"])
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records result", NEXT in note and "direct_finitepart_arithmetic_closed = true" in note and "oriented_logdet_promoted = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 direct finitepart/source-owned logdet audit passed")


if __name__ == "__main__":
    main()
