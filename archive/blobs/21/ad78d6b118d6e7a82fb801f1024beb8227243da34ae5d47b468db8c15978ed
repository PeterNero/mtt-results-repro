"""Audit the Appell-Humbert promotion of V_alpha Yoneda maps."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prove_valpha_appell_humbert_yoneda_promotion.py"
CERT = ROOT / "certificates" / "valpha_appell_humbert_yoneda_promotion_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "valpha_appell_humbert_yoneda_promotion"
    / "ah_boundary_factor_table.json"
)
PAPER = ROOT / "proof_corpus" / "VAlpha_Appell_Humbert_Yoneda_Promotion_v1.md"

EXPECTED_CANDIDATES = {
    (-4, 2, 0),
    (-3, 2, 0),
    (-2, 1, 0),
    (-2, 2, 0),
    (-1, 1, 0),
    (-1, 2, 0),
}


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
        cwd=ROOT,
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
    table = load(TABLE)
    paper = read(PAPER)

    embedded_table = cert.get("appell_humbert_yoneda_promotion", {})
    selection = cert.get("appell_humbert_selection_state", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    rows = table.get("candidate_rows", [])
    row_candidates = {tuple(row.get("M_abc", [])) for row in rows}

    expected_status = "VALPHA_APPELL_HUMBERT_YONEDA_PROMOTION_CONDITIONAL_SELECTION_OPEN"

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("table exists", "PASS" if TABLE.exists() else "FAIL", TABLE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate("table mirrors embedded", "PASS" if table == embedded_table else "FAIL", table.get("status")),
        Gate(
            "six candidates covered",
            "PASS" if row_candidates == EXPECTED_CANDIDATES else "FAIL",
            sorted(row_candidates),
        ),
        Gate(
            "all AH identities",
            "PASS"
            if table.get("all_degree_identities_hold") is True
            and table.get("all_central_degrees_zero") is True
            and table.get("all_reduced_boundaries_injective") is True
            and all(row.get("degree_addition_identity") is True for row in rows)
            and all(row.get("central_shared_circle_degree_zero") is True for row in rows)
            and all(row.get("reduced_boundary_injective") is True for row in rows)
            else "FAIL",
            rows,
        ),
        Gate(
            "selection remains open",
            "OPEN"
            if selection.get("mathematical_representative_constructed") is True
            and selection.get("selected_by_mtt") is False
            and selection.get("neutral_pic0_selected_by_mtt") is False
            and selection.get("target_branch_selected_by_mtt") is False
            else "FAIL",
            selection,
        ),
        Gate(
            "closed layer flags",
            "PASS"
            if closed.get("AH_factor_product_law_matches_yoneda_degree_addition") is True
            and closed.get("central_shared_circle_preserved_degree_zero") is True
            and closed.get("reduced_boundary_maps_promoted_to_AH_theta_multiplication_conditional")
            is True
            and closed.get("raw_good_cover_gap_reduced_to_optional_cover_refinement_if_AH_source_allowed")
            is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open guarded",
            "OPEN"
            if still_open.get("MTT_selection_of_Appell_Humbert_representative") is True
            and still_open.get("MTT_selection_or_quotient_of_Pic0_character") is True
            and still_open.get("literal_finite_good_cover_transition_table_if_required") is True
            and still_open.get("selected_hym_or_strominger_existence_certificate") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records promotion and caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Appell-Humbert Yoneda Promotion",
                    "a_d(gamma,z) * a_e(gamma,z) = a_{d+e}(gamma,z)",
                    "(Q-M) + L^2 = L-M",
                    "not a final selection theorem",
                    "literal finite good-cover transition",
                    "No full V_alpha stability",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha Appell-Humbert Yoneda promotion audit")
    print("=============================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
