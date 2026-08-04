"""Audit the invariant Maurer-Cartan torsion branch gate."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import Any

from iwasawa_dolbeault_complex_extraction_audit import (
    Fraction,
    cohomology_dimensions,
    composition_nonzero_counts,
    ranks,
)


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "invariant_mc_torsion_branch_gate_certificate.json"
PAPER = ROOT / "Invariant_Maurer_Cartan_Torsion_Branch_Gate_for_Iwasawa_A01_v1.md"


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


def candidate_entries() -> list[tuple[int, int, tuple[int, ...]]]:
    return [
        (target, source, form)
        for target in range(3)
        for source in range(3)
        if target != source
        for form in [(1,), (2,), (3,)]
    ]


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)

    heisenberg = [
        (0, 1, Fraction(1), (1,)),
        (1, 2, Fraction(1), (2,)),
        (0, 2, Fraction(-1), (3,)),
    ]
    heisenberg_counts = composition_nonzero_counts(heisenberg)
    heisenberg_ranks = ranks(heisenberg)
    heisenberg_h = cohomology_dimensions(heisenberg_ranks)

    entries = candidate_entries()
    total_candidates = 0
    torsion_integrable_distribution: Counter[tuple[tuple[int, int, int], tuple[int, int, int, int]]] = Counter()
    torsion_h1_three = 0
    for combo in combinations(entries, 3):
        forms = tuple(sorted(form[0] for _target, _source, form in combo))
        for signs in product([1, -1], repeat=3):
            total_candidates += 1
            if 3 not in forms:
                continue
            connection = [
                (target, source, Fraction(sign), form)
                for (target, source, form), sign in zip(combo, signs)
            ]
            if composition_nonzero_counts(connection) != [0, 0]:
                continue
            h_values = tuple(cohomology_dimensions(ranks(connection)))
            torsion_integrable_distribution[(forms, h_values)] += 1
            if h_values[1] == 3:
                torsion_h1_three += 1

    cert_heisenberg = cert.get("canonical_heisenberg_candidate", {})
    cert_scan = cert.get("three_entry_torsion_support_scan", {})
    consequence = cert.get("consequence_for_sm_closure", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    torsion_integrable_count = sum(torsion_integrable_distribution.values())
    expected_distribution = {((1, 2, 3), (1, 2, 2, 1)): 48}

    gates = [
        Gate(
            "certificate status",
            "CLOSED"
            if cert.get("status") == "INVARIANT_MC_TORSION_BRANCH_GIVES_H1_TWO_IN_THREE_ENTRY_ANSATZ"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "MC equations recorded",
            "PASS"
            if contains_all(
                " ".join(cert.get("maurer_cartan_equations", {}).get("equations", [])),
                ["A3 + [A1,A2] = 0", "[A1,A3] = 0", "[A2,A3] = 0"],
            )
            else "FAIL",
            str(cert.get("maurer_cartan_equations", {})),
        ),
        Gate(
            "heisenberg integrable",
            "PASS"
            if heisenberg_counts == [0, 0] and cert_heisenberg.get("integrable") is True
            else "FAIL",
            str(heisenberg_counts),
        ),
        Gate(
            "heisenberg ranks",
            "PASS" if heisenberg_ranks == [2, 5, 2] == list(cert_heisenberg.get("map_ranks", {}).values()) else "FAIL",
            str(heisenberg_ranks),
        ),
        Gate(
            "heisenberg cohomology",
            "PASS"
            if heisenberg_h == [1, 2, 2, 1]
            and cert_heisenberg.get("cohomology_dimensions", {}).get("h1") == 2
            else "FAIL",
            str(heisenberg_h),
        ),
        Gate(
            "candidate count",
            "PASS" if total_candidates == 6528 == cert_scan.get("candidate_count_total") else "FAIL",
            str(total_candidates),
        ),
        Gate(
            "torsion scan distribution",
            "PASS" if dict(torsion_integrable_distribution) == expected_distribution else "FAIL",
            str(dict(torsion_integrable_distribution)),
        ),
        Gate(
            "torsion h1 three absent",
            "PASS"
            if torsion_integrable_count == 48
            and torsion_h1_three == 0
            and cert_scan.get("integrable_with_e3_support") == 48
            and cert_scan.get("integrable_with_e3_support_h1_three") == 0
            else "FAIL",
            f"torsion_integrable={torsion_integrable_count}, h1_three={torsion_h1_three}",
        ),
        Gate(
            "SM consequence",
            "PASS"
            if consequence.get("torsion_support_branch_supplies_three_family_basis") is False
            and consequence.get("requires_stronger_A01_or_typed_monad_or_noninvariant_modes") is True
            else "FAIL",
            str(consequence),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_no_selected_iwasawa_bundle_can_have_h1_three") is False
            and guardrails.get("claims_heisenberg_candidate_is_selected") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("finite_three_entry_torsion_branch_closed") is True
            and verdict.get("h1_three_requires_dropping_e3_in_this_ansatz") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "Invariant Maurer-Cartan Equations",
                    "A3 + [A1,A2] = 0",
                    "Heisenberg pattern",
                    "Every one of those integrable torsion-support candidates",
                    "supports only an integrable two-family invariant cohomology",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Invariant Maurer-Cartan torsion branch gate audit")
    print("=================================================")
    print()
    print(f"heisenberg_counts={heisenberg_counts}")
    print(f"heisenberg_ranks={heisenberg_ranks}")
    print(f"heisenberg_h={heisenberg_h}")
    print(f"torsion_integrable_distribution={dict(torsion_integrable_distribution)}")
    print(f"torsion_h1_three={torsion_h1_three}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
