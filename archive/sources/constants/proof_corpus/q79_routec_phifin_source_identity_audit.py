"""Audit q79 Route-C Phi_fin source-identity packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_routec_phifin_source_identity.py"
PACKET = ROOT / "candidate_data" / "q79_routec_phifin_source_identity.candidate.json"
CERT = ROOT / "certificates" / "q79_routec_phifin_source_identity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1.md"

STATUS = "Q79_ROUTEC_PHIFIN_SOURCE_IDENTITY_D_E_GAP_LAYER_CLOSED_DOTD_OPEN"
NEXT = "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and certificate match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("all source-identity checks pass", all(packet["source_identity_checks"].values()), packet["source_identity_checks"])
    check("theorem proved without full closure", packet["theorem"]["proved"] is True, packet["theorem"])

    identity = packet["selected_source_identity"]
    check(
        "D_E and Riesz/Green identity closed",
        identity["D_E_source_flags_may_be_theorem_derived"] is True
        and identity["Riesz_Green_source_layer_closed"] is True
        and identity["basis_dimension"] == 27,
        identity,
    )
    check(
        "scope is gap layer only",
        identity["scope"] == "rho_E trace plus D_E/gap/Riesz/Green source identity only",
        identity["scope"],
    )
    check(
        "next blocker dotD",
        packet["what_remains_open"]["selected_dotD_alpha1_source_identity"] is True
        and packet["what_remains_open"]["retarded_overlap_derivative_formula"] is True
        and packet["verdict"]["next_required_artifact"] == NEXT,
        packet["what_remains_open"],
    )
    check(
        "full payload not claimed",
        packet["verdict"]["source_identity_gap_layer_closed"] is True
        and packet["verdict"]["full_operator_payload_closed"] is False,
        packet["verdict"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "gap/Riesz/Green layer",
        "does not close `dotD`, alpha1, C1, Yukawa",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 Route-C Phi_fin source identity audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
