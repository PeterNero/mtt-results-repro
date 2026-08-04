"""Audit the central-neutral V_alpha destabilizer reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "prove_valpha_central_neutral_destabilizer_reduction.py"
CERT = ROOT / "certificates" / "valpha_central_neutral_destabilizer_reduction_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_central_neutral_destabilizer_reduction.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "valpha_central_neutral_destabilizer_reduction"
    / "reduced_destabilizer_table.json"
)
PAPER = CORPUS / "VAlpha_Central_Neutral_Destabilizer_Reduction_v1.md"

EXPECTED_CANDIDATES = [
    [-4, 2, 0],
    [-3, 2, 0],
    [-2, 1, 0],
    [-2, 2, 0],
    [-1, 1, 0],
    [-1, 2, 0],
]


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


def rows_by_m(table: dict[str, Any]) -> dict[tuple[int, int, int], dict[str, Any]]:
    return {tuple(row["M_abc"]): row for row in table.get("candidate_rows", [])}


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = read(PAPER)

    embedded_table = cert.get("central_neutral_destabilizer_table", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    row_map = rows_by_m(table)

    expected_status = (
        "VALPHA_CENTRAL_NEUTRAL_DESTABILIZERS_OBSTRUCTED_REDUCED_MODEL_GLOBAL_ENUMERATION_OPEN"
    )
    expected_ranks = {
        (-4, 2, 0): 3,
        (-3, 2, 0): 2,
        (-2, 1, 0): 1,
        (-2, 2, 0): 1,
        (-1, 1, 0): 1,
        (-1, 2, 0): 1,
    }
    expected_statuses = {
        (-4, 2, 0): "EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY",
        (-3, 2, 0): "EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY",
        (-2, 1, 0): "EXCLUDED_BY_PROVED_REDUCED_KUNNETH_YONEDA_SCALAR",
        (-2, 2, 0): "EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY",
        (-1, 1, 0): "EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY",
        (-1, 2, 0): "EXCLUDED_BY_NON_SPLIT_EXTENSION_BOUNDARY",
    }

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
            "finite candidate list",
            "PASS"
            if table.get("inequality_reduction", {}).get("candidate_list") == EXPECTED_CANDIDATES
            else "FAIL",
            table.get("inequality_reduction", {}).get("candidate_list"),
        ),
        Gate(
            "bounded scan agrees",
            "PASS"
            if table.get("bounded_scan_check", {}).get("hom_to_L_nonnegative_slope_hits") == []
            and table.get("bounded_scan_check", {}).get("hom_to_Q_nonnegative_slope_hits")
            == EXPECTED_CANDIDATES
            and table.get("bounded_scan_check", {}).get("matches_inequality_candidate_list")
            is True
            else "FAIL",
            table.get("bounded_scan_check"),
        ),
        Gate(
            "extra Hom candidates recorded",
            "PASS"
            if table.get("prior_branch_list_diagnostic", {}).get(
                "extra_hom_destabilizer_candidates"
            )
            == [[-4, 2, 0], [-3, 2, 0], [-2, 2, 0], [-1, 1, 0]]
            else "FAIL",
            table.get("prior_branch_list_diagnostic"),
        ),
        Gate(
            "all boundary ranks",
            "PASS"
            if set(row_map) == set(expected_ranks)
            and all(
                row_map[line]["boundary_map"]["rank"] == rank
                and row_map[line]["boundary_map"]["injective_on_hom"] is True
                for line, rank in expected_ranks.items()
            )
            else "FAIL",
            {str(line): row_map.get(line, {}).get("boundary_map", {}).get("rank") for line in expected_ranks},
        ),
        Gate(
            "all statuses",
            "PASS"
            if all(row_map[line]["status"] == status for line, status in expected_statuses.items())
            else "FAIL",
            {str(line): row_map.get(line, {}).get("status") for line in expected_statuses},
        ),
        Gate(
            "closed layer flags",
            "PASS"
            if closed.get("central_neutral_hom_to_L_destabilizers_empty") is True
            and closed.get("central_neutral_hom_to_Q_nonnegative_candidates_finite_six") is True
            and closed.get("selected_ext_lowest_basis_confirmed") is True
            and closed.get("all_six_candidate_boundaries_injective") is True
            and closed.get("all_six_candidates_obstructed_in_reduced_kunneth_model") is True
            and closed.get("central_neutral_base_pullback_line_destabilizers_obstructed") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open guarded",
            "OPEN"
            if still_open.get("global_rank_one_torsion_free_subsheaf_enumeration") is True
            and still_open.get(
                "prove_all_destabilizers_have_central_neutral_base_pullback_reflexive_hull"
            )
            is True
            and still_open.get(
                "promote_reduced_kunneth_to_raw_good_cover_cech_or_appell_humbert_multiplication"
            )
            is True
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
            "paper records theorem and caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Central-Neutral Destabilizer Reduction",
                    "six classes",
                    "Hom(M,L)",
                    "Hom(M,Q)",
                    "Boundary Table",
                    "old finite branch list",
                    "not the full V_alpha stability theorem",
                    "No HYM existence",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha central-neutral destabilizer reduction audit")
    print("====================================================")
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
