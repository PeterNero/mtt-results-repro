"""Audit the time-oriented m=1 finite gerbe period table."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "construct_time_oriented_m1_gerbe_period_table.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_gerbe_period_table.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Gerbe_Period_Table_v1.md"


@dataclass
class Gate:
    name: str
    passed: bool
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_constructor() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run_constructor()
    gates: list[Gate] = [
        Gate("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        Gate("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        Gate("certificate exists", CERT.exists(), str(CERT)),
        Gate("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if CANDIDATE.exists() and CERT.exists() and PAPER.exists():
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        table = candidate.get("finite_period_table", {})
        conjugate = candidate.get("antiunitary_conjugate_table_retained", {}).get(
            "period_table", {}
        )
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")

        gates.extend(
            [
                Gate(
                    "status closed finite table only",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
                    cert.get("status", ""),
                ),
                Gate(
                    "selected branch q79 F m1",
                    cert.get("selected_branch", {}).get("q") == 79
                    and cert.get("selected_branch", {}).get("orientation") == "F"
                    and cert.get("selected_branch", {}).get("torsion_label_m") == 1,
                    str(cert.get("selected_branch")),
                ),
                Gate(
                    "m1 table cocycle and bianchi",
                    table.get("normalized_two_cocycle") is True
                    and table.get("all_coboundary_deltas_zero") is True
                    and table.get("coboundary_delta_checked_triples") == 729
                    and table.get("nonzero_coboundary_deltas_mod3") == {},
                    str(
                        {
                            "normalized": table.get("normalized_two_cocycle"),
                            "delta_zero": table.get("all_coboundary_deltas_zero"),
                            "triples": table.get("coboundary_delta_checked_triples"),
                        }
                    ),
                ),
                Gate(
                    "m1 qutrit commutator",
                    table.get("commutator_matrix_mod3_on_basis_e1_e2")
                    == [[0, 1], [2, 0]]
                    and table.get("commutator_rank_over_F3") == 2
                    and table.get("ordinary_bundle_coboundary_possible") is False,
                    str(table.get("commutator_matrix_mod3_on_basis_e1_e2")),
                ),
                Gate(
                    "period table has concrete entries",
                    table.get("period_table_mod3", {}).get("01|10") == 2
                    and table.get("holonomy_table", {}).get("01|10") == "zeta_3^2",
                    str(
                        {
                            "period": table.get("period_table_mod3", {}).get("01|10"),
                            "holonomy": table.get("holonomy_table", {}).get("01|10"),
                        }
                    ),
                ),
                Gate(
                    "antiunitary m2 retained",
                    conjugate.get("commutator_matrix_mod3_on_basis_e1_e2")
                    == [[0, 2], [1, 0]]
                    and calc.get("antiunitary_m2_table_retained") is True,
                    str(conjugate.get("commutator_matrix_mod3_on_basis_e1_e2")),
                ),
                Gate(
                    "finite table closes not source",
                    closes.get("actual_finite_B_field_period_table_on_selected_quotient")
                    is True
                    and closes.get("m1_source_is_not_just_a_flag_lift") is True
                    and still_open.get("repo_level_selected_D_E_dotD_Riesz_Green")
                    is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                Gate(
                    "guardrails no overclaim",
                    guardrails.get("claims_full_geometric_Deligne_Cech_representative")
                    is False
                    and guardrails.get("claims_Freed_Witten_verified") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                Gate(
                    "paper records remaining bridge",
                    "finite selected period table" in paper
                    and "selected D_E/dotD/Riesz/Green files" in paper,
                    "bridge text present",
                ),
            ]
        )

    for gate in gates:
        status = "PASS" if gate.passed else "FAIL"
        print(f"[{status}] {gate.name}: {gate.detail}")

    return 0 if all(gate.passed for gate in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
