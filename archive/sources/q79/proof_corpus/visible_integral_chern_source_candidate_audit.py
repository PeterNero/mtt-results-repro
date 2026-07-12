"""Audit the visible integral Chern-character source candidate packet."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "audit_visible_integral_chern_source_candidate.py"
CANDIDATE = REPO / "candidate_data" / "visible_integral_chern_source_candidate.candidate.json"
CERT = REPO / "certificates" / "visible_integral_chern_source_candidate_certificate.json"
PAPER = ROOT / "Visible_Integral_Chern_Source_Candidate_and_HYM_Gate_v1.md"


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
    corpus = cert.get("corpus_support", {})
    integral = cert.get("integral_candidate", {})
    hym = cert.get("hym_primitivity_gate", {})
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
            "status integral candidate closed",
            "PASS"
            if cert.get("status")
            == "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_CLOSED_HYM_SOURCE_OPEN"
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
        Gate("corpus support", "PASS" if all(corpus.values()) else "FAIL", str(corpus)),
        Gate(
            "integral row computed",
            "PASS"
            if integral.get("pair_products")
            == {"sum_n1n2": 4, "sum_n1n3": 0, "sum_n2n3": 0}
            and integral.get("standard_chern_character_label", {}).get("row") == [4, 0, 0]
            and integral.get("matches_required_alpha1_integral_row") is True
            else "FAIL",
            str(integral),
        ),
        Gate(
            "split HYM shortcut rejected",
            "OPEN"
            if hym.get("individual_primitivity_impossible_for_positive_radii") is True
            and hym.get("total_pairwise_cancellation_occurs") is True
            and hym.get("split_abelian_candidate_selected_hym_source") is False
            else "FAIL",
            str(hym),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("integral_chern_character_candidate_exists") is True
            and calc.get("split_abelian_hym_primitivity_gate_passes") is False
            and closes.get("split_abelian_shortcut_rejected_as_HYM_source") is True
            else "FAIL",
            str({"calc": calc, "closes": closes}),
        ),
        Gate(
            "selected source remains open",
            "OPEN"
            if still_open.get("selected_visible_nonabelian_stable_bundle_or_sheaf_with_ch2_4_alpha1")
            is True
            and still_open.get("same_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "standard label 4",
                    "split abelian shortcut fails",
                    "individual summands",
                    "nonabelian stable bundle",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible integral Chern source candidate audit")
    print("=============================================")
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
