"""Audit closure of the m=1 visible Green-Schwarz curvature packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "close_time_oriented_m1_visible_gs_curvature.py"
VALIDATOR = REPO / "scripts" / "validate_time_oriented_m1_visible_green_schwarz_curvature.py"
PACKET = REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature.selected.json"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_visible_green_schwarz_curvature_closure.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Visible_Green_Schwarz_Curvature_Closure_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: str) -> tuple[str, bool, str]:
    return name, condition, detail


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run_script()
    checks: list[tuple[str, bool, str]] = [
        check("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        check("packet exists", PACKET.exists(), str(PACKET)),
        check("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        check("certificate exists", CERT.exists(), str(CERT)),
        check("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if PACKET.exists() and CERT.exists() and CANDIDATE.exists() and PAPER.exists():
        packet = load_json(PACKET)
        cert = load_json(CERT)
        candidate = load_json(CANDIDATE)
        validator_proc = run_validator(PACKET)
        source = cert.get("selected_curvature_source", {})
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")

        checks.extend(
            [
                check(
                    "status curvature closed operator open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN"
                    and candidate.get("status") == cert.get("status"),
                    str(cert.get("status")),
                ),
                check(
                    "selected packet validates",
                    validator_proc.returncode == 0
                    and "visible Green-Schwarz curvature PASS" in validator_proc.stdout,
                    validator_proc.stdout.strip(),
                ),
                check(
                    "symbolic packet exact rows",
                    packet.get("coefficient_domain") == "symbolic_iwasawa_alpha_rows"
                    and packet.get("tr_F_visible_squared_coefficients")
                    == ["8*r3^2/(r1^2*r2^2) + 4*r3^2", "0", "0"]
                    and packet.get("bianchi_residual_coefficients") == ["0", "0", "0"]
                    and packet.get("bianchi_residual_zero") is True,
                    str(packet),
                ),
                check(
                    "curvature source selected but operator open",
                    source.get("coherent_projection_context") is True
                    and source.get("iwasawa_bianchi_component_support") is True
                    and source.get("operator_source_constructed") is False,
                    str(source),
                ),
                check(
                    "calculation closes curvature only",
                    calc.get("visible_green_schwarz_curvature_verified") is True
                    and calc.get("selected_visible_operator_source_verified") is False
                    and calc.get("projector_retention_verified") is False,
                    str(calc),
                ),
                check(
                    "what closes and remains",
                    closes.get("selected_visible_GS_curvature_packet") is True
                    and closes.get("zero_Bianchi_residual_for_required_symbolic_row") is True
                    and still_open.get("selected_visible_SM_operator_source") is True
                    and still_open.get("primitive_C1_contractions") is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "guardrails no operator overclaim",
                    guardrails.get("claims_selected_visible_operator_source") is False
                    and guardrails.get("claims_projector_retention") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records closure scope",
                    "curvature level" in paper
                    and "operator source D_E/dotD: open" in paper
                    and "TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN" in paper,
                    "paper scope present",
                ),
            ]
        )

    print("Time-oriented m=1 visible Green-Schwarz curvature closure audit")
    print("================================================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:55} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
