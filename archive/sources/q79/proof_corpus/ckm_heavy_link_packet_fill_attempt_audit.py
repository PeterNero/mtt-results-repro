"""Audit the CKM heavy-link packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "ckm_heavy_link_packet_fill_attempt_certificate.json"
ATTEMPT = REPO / "certificates" / "selected_ckm_heavy_link_packet.attempt.json"
PAPER = ROOT / "CKM_Heavy_Link_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_ckm_heavy_link_packet.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_attempt() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    attempt_file = load_json(ATTEMPT)
    attempt = run_attempt()
    paper = read(PAPER)
    script_text = read(SCRIPT)

    source_hunt = attempt.get("source_hunt", {})
    fill = attempt.get("fill_attempt", {})
    can_compute = attempt.get("can_compute_now", {})
    guardrails = attempt.get("guardrails", {})
    computed = cert.get("computed_result", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    cert_guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "CKM_HEAVY_LINK_PACKET_FILL_ATTEMPT_BLOCKED_SELECTED_SOURCES_MISSING"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "selected_c1_missing_primitive_matrices",
                    "selected_c6_support_files_present",
                    "external_direct_entry_token_hits",
                    "missing_heavy_link_entries",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "attempt packet written",
            "PASS"
            if ATTEMPT.exists()
            and attempt_file.get("status") == "BLOCKED_SELECTED_HEAVY_LINK_SOURCES_MISSING"
            else "FAIL",
            str(ATTEMPT),
        ),
        Gate(
            "script matches packet",
            "PASS"
            if attempt.get("status") == attempt_file.get("status")
            and attempt.get("fill_attempt", {}).get("missing_heavy_link_entries")
            == attempt_file.get("fill_attempt", {}).get("missing_heavy_link_entries")
            else "FAIL",
            "script output compared with committed attempt packet",
        ),
        Gate(
            "primitive absence",
            "PASS"
            if source_hunt.get("selected_c1_primitive_contractions_complete") is False
            and source_hunt.get("selected_c1_missing_primitive_matrices") == 24
            and source_hunt.get("selected_c1_response_delta_v") is None
            else "FAIL",
            str(source_hunt),
        ),
        Gate(
            "c6 support absence",
            "PASS"
            if source_hunt.get("selected_c6_support_files_present") == []
            and len(source_hunt.get("selected_c6_support_files_expected", [])) == 5
            else "FAIL",
            str(source_hunt.get("selected_c6_support_files_present")),
        ),
        Gate(
            "external corpus scanned",
            "PASS"
            if source_hunt.get("external_corpus_available") is True
            and source_hunt.get("external_direct_entry_token_hits") == []
            else "FAIL",
            str(source_hunt.get("external_direct_entry_token_hits")),
        ),
        Gate(
            "missing entries",
            "PASS"
            if len(fill.get("missing_heavy_link_entries", [])) == 8
            and fill.get("Delta_v_computable") is False
            and fill.get("character_trivial_entries_filled") is False
            and fill.get("c6_entries_filled") is False
            else "FAIL",
            str(fill),
        ),
        Gate(
            "cannot compute claims",
            "PASS" if all(value is False for value in can_compute.values()) else "FAIL",
            str(can_compute),
        ),
        Gate(
            "attempt guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "certificate computed result",
            "PASS"
            if computed.get("selected_c1_missing_primitive_matrices") == 24
            and computed.get("selected_c6_support_files_present") == 0
            and computed.get("missing_heavy_link_entries") == 8
            and computed.get("Delta_v_computable") is False
            else "FAIL",
            str(computed),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "certificate guardrails",
            "PASS" if all(value is False for value in cert_guardrails.values()) else "FAIL",
            str(cert_guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("fill_attempt_complete") is True
            and verdict.get("selected_packet_values_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "BLOCKED_SELECTED_HEAVY_LINK_SOURCES_MISSING",
                    "24 missing primitive 3x3 matrices",
                    "Delta_v_ud = null",
                    "No selected C6 support file is present",
                    "Delta_v = Delta_t + chi_q Delta_c",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("CKM heavy-link packet fill-attempt audit")
    print("========================================")
    print()
    print(f"status={attempt.get('status')}")
    print(f"missing_heavy_link_entries={len(fill.get('missing_heavy_link_entries', []))}")
    print(f"external_hits={source_hunt.get('external_direct_entry_token_hits')}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
