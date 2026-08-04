"""Audit BN27 source-owned logdet source theorem / kernel-trace ownership gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimal_emission_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_SourceTheorem_or_KernelTraceOwnership_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNED_LOGDET_THEOREM_PACKET_BUILT_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_MinimalEmissionPacket_Fill_or_SourceAmendment_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("minimal packet built", decision["sourceowned_logdet_minimal_packet_built"] is True and cert["sourceowned_logdet_minimal_packet_built"] is True, decision)
    check("known arithmetic retained", packet["known_exact_arithmetic"]["oriented_abs_sector_product"] == 92160000 and packet["known_exact_arithmetic"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", packet["known_exact_arithmetic"])
    check("three legal forms present", set(packet["legal_closing_forms"].keys()) == {"direct_source_theorem", "kernel_trace_ownership_export", "connection_or_smooth_quotient_source"}, packet["legal_closing_forms"].keys())
    check("direct source remains open", decision["direct_source_theorem_closed"] is False and packet["legal_closing_forms"]["direct_source_theorem"]["closed_now"] is False, packet["legal_closing_forms"]["direct_source_theorem"])
    check("kernel trace remains open", decision["kernel_trace_ownership_closed"] is False and packet["legal_closing_forms"]["kernel_trace_ownership_export"]["closed_now"] is False, packet["legal_closing_forms"]["kernel_trace_ownership_export"])
    check("connection/smooth remains open", decision["connection_or_smooth_source_closed"] is False and packet["legal_closing_forms"]["connection_or_smooth_quotient_source"]["closed_now"] is False, packet["legal_closing_forms"]["connection_or_smooth_quotient_source"])
    check("no source-owned logdet closure", decision["source_owned_logdet_closed"] is False and cert["source_owned_logdet_closed"] is False, decision)
    check("no BN27 identity closure", decision["BN27_source_identity_closed"] is False and cert["BN27_source_identity_closed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records packet", NEXT in note and str(PACKET.relative_to(ROOT)) in note and "oriented_logdet_promoted = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-owned logdet/kernel-trace audit passed")


if __name__ == "__main__":
    main()
