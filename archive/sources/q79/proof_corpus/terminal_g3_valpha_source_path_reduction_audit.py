"""Audit the terminal-g3 V_alpha source path reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "reduce_terminal_g3_valpha_source_path.py"
CERT = REPO / "certificates" / "terminal_g3_valpha_source_path_reduction_certificate.json"
CANDIDATE = REPO / "candidate_data" / "terminal_g3_valpha_source_path_reduction.candidate.json"
PAPER = ROOT / "Terminal_G3_VAlpha_Source_Path_Reduction_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    paper = read(PAPER)

    reclass = cert.get("route_reclassification", {})
    critical = cert.get("critical_path_now", {})
    results = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status reduced open",
            "PASS"
            if cert.get("status")
            == "TERMINAL_G3_VALPHA_SOURCE_PATH_REDUCED_TO_SELECTED_SOURCE_PACKET_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == results
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "terminal route fixes sign",
            "PASS"
            if reclass.get("terminal_g3_route", {}).get("branch_sign_and_order_fixed") is True
            and reclass.get("terminal_g3_route", {}).get("selected_L") == [1, -2, 0]
            and reclass.get("terminal_g3_route", {}).get("selected_L2") == [2, -4, 0]
            else "FAIL",
            reclass.get("terminal_g3_route"),
        ),
        Gate(
            "finite route remains ambiguous",
            "PASS"
            if reclass.get("finite_qutrit_route", {}).get(
                "still_ambiguous_for_finite_only_selection"
            )
            is True
            else "FAIL",
            reclass.get("finite_qutrit_route"),
        ),
        Gate(
            "wall reclassified",
            "PASS"
            if reclass.get("gauduchon_wall_route", {}).get(
                "wall_search_no_longer_primary_for_sign"
            )
            is True
            and reclass.get("gauduchon_wall_route", {}).get("new_role")
            == "stability/HYM chamber witness after terminal g3 fixes L"
            else "FAIL",
            reclass.get("gauduchon_wall_route"),
        ),
        Gate(
            "critical packet named",
            "PASS"
            if critical.get("name") == "Selected_Terminal_G3_VAlpha_Source.v1"
            and len(critical.get("must_supply", [])) == 6
            and len(critical.get("cannot_reuse_as_proof", [])) == 4
            else "FAIL",
            critical,
        ),
        Gate(
            "results scoped",
            "PASS"
            if results.get("branch_sign_ambiguity_closed_for_terminal_g3_route") is True
            and results.get("sqrt2_radius_wall_no_longer_required_to_choose_sign_on_terminal_g3_path")
            is True
            and results.get("actual_terminal_g3_source_selection_still_open") is True
            else "FAIL",
            results,
        ),
        Gate(
            "closes reduction only",
            "PASS"
            if closes.get(
                "do_not_search_for_gauduchon_wall_as_primary_sign_selector_on_terminal_g3_path"
            )
            is True
            and still_open.get("actual_terminal_g3_source_selector") is True
            and still_open.get("selected_L2_cohomology_packet") is True
            else "FAIL",
            {"closes": closes, "still_open": still_open},
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "Selected_Terminal_G3_VAlpha_Source.v1",
                    "do not solve branch selection twice",
                    "Gauduchon wall is no longer the primary sign selector",
                    "stability/HYM chamber witness",
                    "does not prove that MTT selects g3",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Terminal-g3 V_alpha source path reduction audit")
    print("===============================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
