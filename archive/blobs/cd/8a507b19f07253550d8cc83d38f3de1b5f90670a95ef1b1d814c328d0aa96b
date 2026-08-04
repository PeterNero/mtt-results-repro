"""Audit the block-factorized twist route calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_block_factorized_twist_route_certificate.json"
PAPER = ROOT / "Iwasawa_Block_Factorized_Twist_Route_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_block_factorized_twist_route.py"
FILL_ATTEMPT = CERT_DIR / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"
GERBE_CANDIDATE = CERT_DIR / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json"


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


def run_script() -> dict[str, Any]:
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
    fill_attempt = load_json(FILL_ATTEMPT)
    gerbe_candidate = load_json(GERBE_CANDIDATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    report = run_script()
    results = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    rank3 = report.get("rank3_family_block", {})
    rank4 = report.get("naive_rank4_direct_sum", {})
    honest = report.get("honest_route", {})
    gates = [
        Gate(
            "certificate status",
            "OPEN"
            if cert.get("status") == "IWASAWA_BLOCK_FACTORIZED_TWIST_ROUTE_REQUIRED_SCHEMA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if fill_attempt.get("status")
            in {
                "IWASAWA_TWISTED_SOURCE_PACKET_PARTIAL_FILL_BLOCKED",
                "IWASAWA_TWISTED_SOURCE_PACKET_PARTIAL_FILL_BLOCKED_SELECTED_SOURCE",
            }
            and gerbe_candidate.get("verdict", {}).get("candidate_holonomy_map_closed") is True
            else "FAIL",
            "fill attempt plus gerbe candidate",
        ),
        Gate(
            "script checks direct sum",
            "PASS"
            if contains_all(
                script_text,
                [
                    "diag(X,1), diag(Z,1)",
                    "diag(omega I_3,1)",
                    "block_factorized_schema_needed",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "rank3 result",
            "PASS"
            if rank3.get("single_scalar_projective_gluing") is True
            and rank3.get("rank_one_projector_available") is False
            else "FAIL",
            str(rank3),
        ),
        Gate(
            "rank4 direct sum rejected",
            "PASS"
            if rank4.get("rank_one_H_projector_available") is True
            and rank4.get("single_scalar_projective_gluing") is False
            and rank4.get("centrality_error", 0.0) > 0.0
            else "FAIL",
            str(rank4),
        ),
        Gate(
            "honest route",
            "PASS"
            if honest.get("block_factorized_schema_needed") is True
            and honest.get("single_carrier_shortcut_allowed") is False
            else "FAIL",
            str(honest),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if results.get("rank3_family_projective_gluing_passes") is True
            and results.get("rank3_rank_one_H_projector_available") is False
            and results.get("naive_rank4_rank_one_H_projector_available") is True
            and results.get("naive_rank4_single_scalar_projective_gluing_passes") is False
            and results.get("block_factorized_schema_needed") is True
            else "FAIL",
            str(results),
        ),
        Gate(
            "what this closes",
            "PASS" if all(cert.get("what_this_closes", {}).values()) else "FAIL",
            str(cert.get("what_this_closes", {})),
        ),
        Gate(
            "still open",
            "OPEN" if all(cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open", {})),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("block_factorized_route_is_correct_next_architecture") is True
            and verdict.get("single_rank3_or_naive_rank4_route_blocked") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records route",
            "PASS"
            if contains_all(
                paper,
                [
                    "X_4 = diag(X,1)",
                    "diag(zeta_3 I_3, 1)",
                    "block-factorized packet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa block-factorized twist route audit")
    print("==========================================")
    print()
    print(f"rank4_centrality_error={rank4.get('centrality_error')}")
    print(f"block_factorized_schema_needed={honest.get('block_factorized_schema_needed')}")
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
