"""Audit the equivariant embedding selector for the twisted S3 D7 stack."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_s3_equivariant_embedding_selector.py"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_d7_equivariant_embedding_selector.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_d7_equivariant_embedding_selector_certificate.json"
PAPER = ROOT / "Visible_Twisted_D7_Equivariant_Embedding_Selector_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run_constructor() -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def main() -> None:
    code, output = run_constructor()
    cert = load_json(CERT)
    paper = read(PAPER)
    source_hits = cert.get("source_hits", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    accepted = cert.get("accepted_assignments", [])
    rejected = cert.get("rejected_without_extra_source", [])
    principle = cert.get("principle", {})

    gates = [
        Gate("constructor exits 0", "PASS" if code == 0 else "FAIL", output[:900]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status closes minimal S3 selector",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_S3_CLOSED_SOURCE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "principle sources present",
            "PASS" if all(source_hits.values()) else "FAIL",
            str(source_hits),
        ),
        Gate(
            "equivariance principle explicit",
            "PASS"
            if principle.get("survivor_labels_are_symmetry_compatible") is True
            and principle.get("coordinate_artifacts_cannot_select_physical_branch") is True
            and principle.get("unbroken_automorphisms_must_be_respected_without_selected_breaking_source")
            is True
            else "FAIL",
            str(principle),
        ),
        Gate(
            "accepted assignments are S3 only",
            "PASS"
            if len(accepted) == 2
            and {item.get("twisted_projective_D7_stack_required") for item in accepted} == {"S3"}
            else "FAIL",
            str(accepted),
        ),
        Gate(
            "S1/S2 require extra source",
            "PASS"
            if len(rejected) == 4
            and {item.get("twisted_projective_D7_stack_required") for item in rejected}
            == {"S1", "S2"}
            and closes.get("S1_S2_retired_unless_extra_selected_source_breaks_qutrit_exchange")
            is True
            else "FAIL",
            str(rejected),
        ),
        Gate(
            "S3 source remains open",
            "PASS"
            if closes.get("minimal_equivariant_twisted_D7_stack_selector") == "S3"
            and closes.get("unconditional_selected_S3_Deligne_Cech_source") is False
            and still_open.get("construct_selected_S3_Deligne_Cech_or_worldvolume_flux_source")
            is True
            else "FAIL",
            str({"closes": closes, "still_open": still_open}),
        ),
        Gate(
            "guardrails prevent overclaim",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper states source still open",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "minimal equivariant twisted D7 stack = S3",
                    "not logically impossible",
                    "selected S3 source packet",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted D7 equivariant embedding selector audit")
    print("=======================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
