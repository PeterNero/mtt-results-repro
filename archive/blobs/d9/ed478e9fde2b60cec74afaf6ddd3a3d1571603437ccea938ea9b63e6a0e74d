"""Audit the selected PhiFin S2 finite trace morphism scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_phifin_s2_finite_trace_morphism_scaffold.py"
PACKET = DATA / "selected_phifin_s2_finite_trace_morphism_scaffold.candidate.json"
CERT = CERTS / "selected_phifin_s2_finite_trace_morphism_scaffold_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_PhiFin_S2_Finite_Trace_Morphism_Scaffold_v1.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load_json(PACKET)
    cert = load_json(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    expected_status = "FINITE_TRACE_MORPHISM_SCAFFOLD_REDUCED_OPERATOR_IDENTIFICATION_OPEN"
    check("certificate status", cert["status"] == expected_status, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check(
        "closed prefix faces",
        cert["closed_prefix_faces"]
        == [
            "F0_selected_smooth_source",
            "F1_abstract_functorial_trace_exists",
            "F2_selected_projective_rhoE_trace_partial",
            "F3_same_BN_basis_and_finite_algebra",
        ],
        cert["closed_prefix_faces"],
    )
    check(
        "open faces honest",
        cert["open_faces"] == ["F4_operator_entry_identification", "F5_honest_replay_without_lifted_flags"],
        cert["open_faces"],
    )
    gate = packet["operator_identification_gate"]
    check("gate named", gate["name"] == "SelectedTraceEqualsEmitted27ModeDE", gate)
    check(
        "eta conditional ready",
        packet["conditional_consequence_ready"]["eta_N_if_gate_closes"] == 1.0
        and packet["conditional_consequence_ready"]["passes_threshold"]
        and not packet["conditional_consequence_ready"]["selected_eta_emitted_now"],
        packet["conditional_consequence_ready"],
    )
    sectors = packet["sector_matrix_checks"]
    check(
        "all sectors same finite domain",
        all(item["shape"] == [27, 27] and item["same_gram_identity"] for item in sectors.values()),
        sectors,
    )
    check(
        "selected flags remain false",
        all(not item["selected_source_verified"] for item in sectors.values()),
        sectors,
    )
    check(
        "operator identification not claimed",
        not packet["morphism_faces"]["F4_operator_entry_identification"]["closed"]
        and not packet["guardrails"]["does_not_claim_operator_identification"] is False,
        packet["morphism_faces"]["F4_operator_entry_identification"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records gate", "SelectedTraceEqualsEmitted27ModeDE" in note, NOTE)

    print("\nSelected PhiFin S2 finite trace morphism scaffold audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
