"""Audit Iwasawa monad vs visible alpha_1 source role separation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_iwasawa_monad_visible_source_role.py"
CANDIDATE = REPO / "candidate_data" / "iwasawa_monad_visible_source_role.candidate.json"
CERT = REPO / "certificates" / "iwasawa_monad_visible_source_role_certificate.json"
PAPER = ROOT / "Iwasawa_Monad_vs_Visible_Alpha1_Source_Role_Separation_v1.md"


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

    monad_role = cert.get("monad_role", {})
    visible_role = cert.get("visible_source_role", {})
    comparison = cert.get("role_comparison", {})
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
            "status role separation",
            "PASS"
            if cert.get("status") == "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_SEPARATED"
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
            "monad topology",
            "PASS"
            if monad_role.get("c1_zero") is True
            and monad_role.get("ch2_zero") is True
            and monad_role.get("c2_coeff_alpha1") == 0
            and monad_role.get("integral_c3") == 6
            else "FAIL",
            str(monad_role),
        ),
        Gate(
            "visible c2 target",
            "PASS"
            if visible_role.get("required_c2_coeff_alpha1") == 4
            and visible_role.get("required_math_ch2_coeff_alpha1") == -4
            else "FAIL",
            str(visible_role),
        ),
        Gate(
            "class mismatch",
            "PASS"
            if comparison.get("monad_c2_minus_required_c2_coeff_alpha1") == -4
            and comparison.get("monad_alone_realizes_visible_alpha1_source") is False
            and comparison.get("monad_can_still_be_matter_zero_mode_source") is True
            else "FAIL",
            str(comparison),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("monad_topology_loaded") is True
            and calc.get("visible_c2_target_loaded") is True
            and calc.get("printed_monad_not_visible_alpha1_source") is True
            and calc.get("printed_monad_retained_as_matter_seed_candidate") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("typed_monad_sections_for_matter_zero_modes") is True
            and still_open.get("selected_nonabelian_visible_source_with_c2_4_alpha1") is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "closes guardrail",
            "PASS"
            if closes.get("do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source") is True
            and closes.get("matter_seed_role_separated_from_visible_curvature_source_role")
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
                    "c2(E) = 0",
                    "c2(V_visible) = +4 alpha_1",
                    "three-family monad alone != visible alpha_1 Chern-Weil source",
                    "larger visible bundle",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa monad visible-source role audit")
    print("=======================================")
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
