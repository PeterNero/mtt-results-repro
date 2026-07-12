"""Audit q79 Route-C Phi_fin dotD/alpha1 source identity attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "attempt_q79_routec_phifin_dotd_alpha1_source_identity.py"
PACKET = ROOT / "candidate_data" / "q79_routec_phifin_dotd_alpha1_source_identity_attempt.candidate.json"
CERT = ROOT / "certificates" / "q79_routec_phifin_dotd_alpha1_source_identity_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_Attempt_v1.md"

STATUS = "Q79_ROUTEC_PHIFIN_DOTD_ALPHA1_SOURCE_IDENTITY_ATTEMPT_REDUCED_TO_RETARDED_SELECTOR"
NEXT = "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1"


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
    check("source identity checks pass", all(packet["source_identity_checks"].values()), packet["source_identity_checks"])
    check("reduction theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("dotD not closed", packet["verdict"]["dotD_source_identity_closed"] is False, packet["verdict"])
    check("next artifact", packet["verdict"]["next_required_artifact"] == NEXT, packet["verdict"])

    reduction = packet["reduction"]
    check(
        "D_E closed and dotD unselected",
        reduction["D_E_gap_layer_status"] == "closed_selected_source_identity"
        and reduction["dotD_value_packet_status"] == "same_basis_values_present_nonzero_but_source_unselected",
        reduction,
    )
    check(
        "antiunitary orbit not knob",
        reduction["antiunitary_status"] == "q79_q369_dotD_packets_equivalent_not_independent_knobs",
        reduction["antiunitary_status"],
    )
    check(
        "first variation blocker isolated",
        "retarded-overlap derivative formula for Phi_fin at the selected source"
        in reduction["missing_source_identity"]
        and packet["what_closes_now"]["first_variation_blocker_is_sharp"] is True,
        reduction["missing_source_identity"],
    )
    check(
        "open items retain retarded selector",
        packet["what_remains_open"]["retarded_overlap_derivative_formula"] is True
        and packet["what_remains_open"]["selected_visible_representative_or_source_origin"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "The `dotD/alpha1` gate did not close",
        "q79/q369 are antiunitarily equivalent",
        "selected first-variation source",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 Route-C Phi_fin dotD/alpha1 source identity attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
