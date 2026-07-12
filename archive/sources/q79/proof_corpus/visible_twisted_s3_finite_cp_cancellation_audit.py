"""Audit finite S3 twisted Chan-Paton cancellation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_visible_twisted_s3_finite_cp_cancellation.py"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_s3_finite_cp_cancellation.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json"
PAPER = ROOT / "Visible_Twisted_S3_Finite_Chan_Paton_Cancellation_v1.md"
S3_SOURCE_VALIDATOR = REPO / "scripts" / "validate_visible_twisted_s3_source_packet.py"
S3_SOURCE_ATTEMPT = REPO / "certificates" / "visible_twisted_s3_source_packet.attempt.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)
    source_proc = run([sys.executable, str(S3_SOURCE_VALIDATOR), str(S3_SOURCE_ATTEMPT)])

    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    reports = cert.get("s3_cancellation_reports", [])
    inputs = cert.get("finite_cancellation_inputs", {})

    gates = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status closes finite cancellation",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_CLOSED_SMOOTH_SOURCE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "finite inputs match q79 m1",
            "PASS"
            if inputs.get("selector_closes_stack_S3") is True
            and inputs.get("m1_period_table_q") == 79
            and inputs.get("m1_period_table_torsion_label") == 1
            and inputs.get("finite_projective_module_matches_m1_twist") is True
            else "FAIL",
            str(inputs),
        ),
        Gate(
            "two S3 cancellation reports",
            "PASS"
            if len(reports) == 2
            and all(item.get("twisted_projective_D7_stack_required") == "S3" for item in reports)
            and all(item.get("finite_total_twisted_DD_class_zero") is True for item in reports)
            and all(item.get("ordinary_DD_gate_for_S3") is False for item in reports)
            else "FAIL",
            str(reports),
        ),
        Gate(
            "ordinary matter curves retained",
            "PASS"
            if calc.get("matter_curves_remain_ordinary_DD_zero") is True
            and all(item.get("ordinary_DD_zero_matter_curves") == ["C12", "C23", "C31"] for item in reports)
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes finite not smooth",
            "PASS"
            if closes.get("finite_rank_two_S3_DD_obstruction_is_cancellable_by_twisted_CP")
            is True
            and still_open.get("selected_smooth_S3_Deligne_Cech_or_worldvolume_flux_source")
            is True
            and still_open.get("twisted_projector_retention") is True
            else "FAIL",
            str({"closes": closes, "still_open": still_open}),
        ),
        Gate(
            "source packet still rejected",
            "PASS"
            if source_proc.returncode == 1
            and "source_evidence.source_selected_by_mtt must be true" in source_proc.stdout
            else "FAIL",
            source_proc.stdout.strip(),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "paper records finite-only result",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "finite S3 twisted Chan-Paton cancellation",
                    "not the smooth selected source theorem",
                    "ordinary S3 DD-zero route still fails",
                    "projector retention remains open",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible twisted S3 finite Chan-Paton cancellation audit")
    print("=======================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
