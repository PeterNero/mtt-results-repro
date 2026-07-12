"""Audit the visible additive source-factor route."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_additive_source_factor_route.py"
CANDIDATE = REPO / "candidate_data" / "visible_additive_source_factor_route.candidate.json"
CERT = REPO / "certificates" / "visible_additive_source_factor_route_certificate.json"
PAPER = ROOT / "Visible_Additive_Source_Factor_Route_v1.md"


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

    route = cert.get("route_definition", {})
    accounting = cert.get("chern_class_accounting", {})
    hym = cert.get("hym_polystability_contract", {})
    warning = cert.get("sm_operator_warning", {})
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
            "status additive route",
            "PASS"
            if cert.get("status")
            == "VISIBLE_ADDITIVE_SOURCE_FACTOR_TOPOLOGY_FORMULATED_SELECTION_OPEN"
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
            "route target",
            "PASS"
            if route.get("total_bundle_schema") == "E_total = E_matter_monad direct_sum V_alpha"
            and route.get("source_factor_minimal_target", {}).get("c1") == [0, 0, 0]
            and route.get("source_factor_minimal_target", {}).get("c2") == [4, 0, 0]
            and route.get("source_factor_minimal_target", {}).get("c3") == 0
            else "FAIL",
            str(route),
        ),
        Gate(
            "chern accounting",
            "PASS"
            if accounting.get("matter_monad", {}).get("c2") == [0, 0, 0]
            and accounting.get("source_factor", {}).get("c2") == [4, 0, 0]
            and accounting.get("total", {}).get("c1") == [0, 0, 0]
            and accounting.get("total", {}).get("c2") == [4, 0, 0]
            and accounting.get("total", {}).get("c3") == 6
            and accounting.get("topological_accounting_passes") is True
            else "FAIL",
            str(accounting),
        ),
        Gate(
            "hym conditional",
            "OPEN"
            if hym.get("current_status") == "conditional only"
            and "typed monad maps" in hym.get("missing_for_E_matter", [])
            and "selected nonabelian stable/sheaf construction" in hym.get("missing_for_V_alpha", [])
            else "FAIL",
            str(hym),
        ),
        Gate(
            "operator warning",
            "PASS"
            if warning.get("topology_is_not_operator_closure") is True
            and warning.get("hidden_sector_only_would_not_close_visible_operator_source") is True
            and warning.get("direct_sum_can_make_dotD_block_diagonal") is True
            else "FAIL",
            str(warning),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("topological_additive_route_formulated") is True
            and calc.get("total_c3_preserves_three_net_families") is True
            and calc.get("source_factor_constructed") is False
            and calc.get("same_source_D_E_dotD_Riesz_Green_constructed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("construct_selected_V_alpha_with_c1_0_c2_4_alpha1_c3_0")
            is True
            and still_open.get("protect_or_recompute_E8_commutant_and_SM_sector_dictionary")
            is True
            and still_open.get("derive_same_total_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "closes route accounting",
            "PASS"
            if closes.get("additive_c2_accounting_for_matter_plus_source") is True
            and closes.get("hidden_or_block_diagonal_shortcut_flagged") is True
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
                    "E_total = E_matter direct_sum V_alpha",
                    "c2(E_total) = +4 alpha_1",
                    "Topological additivity is not SM matrix closure",
                    "adding a nonabelian factor can change the E8 commutant",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible additive source-factor route audit")
    print("==========================================")
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
