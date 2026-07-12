"""Audit the stable-source sign convention gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_stable_source_sign_gate.py"
CANDIDATE = REPO / "candidate_data" / "visible_stable_source_sign_gate.candidate.json"
CERT = REPO / "certificates" / "visible_stable_source_sign_gate_certificate.json"
PAPER = ROOT / "Visible_Stable_Source_Sign_Convention_Gate_v1.md"


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


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    sign = cert.get("stable_hym_sign_package", {})
    wrong = cert.get("wrong_sign_branch", {})
    admissible = cert.get("admissible_stable_sign_branch", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status sign gate",
            "PASS"
            if cert.get("status")
            == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN"
            else "FAIL",
            str(cert.get("status")),
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
            "sign package",
            "PASS"
            if sign.get("bogomolov_li_yau_sign") == "integral_X c2(E) wedge J_G >= 0"
            and sign.get("chern_character_relation_when_c1_zero") == "ch2_math(E) = -c2(E)"
            and sign.get("antihermitian_trace_convention", {}).get("math_c2")
            == "+(1/(8*pi^2))*Tr(F wedge F)"
            else "FAIL",
            str(sign),
        ),
        Gate(
            "wrong sign rejected",
            "PASS"
            if wrong.get("math_ch2_coeff_alpha1") == 4
            and wrong.get("math_c2_coeff_alpha1") == -4
            and wrong.get("stable_hym_admissible") is False
            and calc.get("positive_math_ch2_interpretation_rejected_for_stable_hym")
            is True
            else "FAIL",
            str(wrong),
        ),
        Gate(
            "admissible sign retained",
            "PASS"
            if admissible.get("trace_coeff_alpha1") == 4
            and admissible.get("math_c2_coeff_alpha1") == 4
            and admissible.get("math_ch2_coeff_alpha1") == -4
            and admissible.get("stable_hym_sign_admissible") is True
            else "FAIL",
            str(admissible),
        ),
        Gate(
            "scope and open source",
            "OPEN"
            if calc.get("nonabelian_stable_source_constructed") is False
            and calc.get("route_c_source_constructed") is False
            and still_open.get("selected_nonabelian_stable_bundle_or_sheaf_with_c1_0_c2_4_alpha1")
            is True
            and still_open.get("selected_route_c_residual_solve_for_same_trace_row") is True
            else "FAIL",
            str({"calc": calc, "still_open": still_open}),
        ),
        Gate(
            "closes guardrail",
            "PASS"
            if closes.get("stable_source_sign_convention_guardrail") is True
            and closes.get("correct_nonabelian_target_is_positive_c2_not_positive_math_ch2")
            is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "integral_X c2(E) wedge J_G >= 0",
                    "ch2_math(E) = -c2(E)",
                    "c2(E)=+4 alpha_1",
                    "ch2_math(E)=-4 alpha_1",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible stable-source sign gate audit")
    print("=====================================")
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
