"""Audit the sparse corrected-A01 candidate scan."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import Any

from iwasawa_dolbeault_complex_extraction_audit import (
    Fraction,
    LITERAL_A01,
    cohomology_dimensions,
    composition_nonzero_counts,
    ranks,
)


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "corrected_a01_candidate_scan_certificate.json"
PAPER = ROOT / "Corrected_A01_Candidate_Scan_for_Iwasawa_Three_Family_Complex_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def candidate_entries() -> list[tuple[int, int, tuple[int, ...]]]:
    return [
        (target, source, form)
        for target in range(3)
        for source in range(3)
        if target != source
        for form in [(1,), (2,), (3,)]
    ]


def support(connection: list[tuple[int, int, Fraction, tuple[int, ...]]]) -> set[tuple[int, int, tuple[int, ...]]]:
    return {(target, source, form) for target, source, _coefficient, form in connection}


def sorted_connection(connection: list[tuple[int, int, Fraction, tuple[int, ...]]]) -> list[tuple[int, int, int, tuple[int, ...]]]:
    return sorted(
        (target, source, int(coefficient), form)
        for target, source, coefficient, form in connection
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)

    entries = candidate_entries()
    literal_support = support(LITERAL_A01)
    candidate_count = 0
    integrable_distribution: Counter[tuple[int, int, int, int]] = Counter()
    h1_three_form_multisets: Counter[tuple[int, int, int]] = Counter()
    h1_three_support_distances: list[int] = []
    h1_three_with_all_forms = 0
    example_h1_three: list[tuple[int, int, int, tuple[int, ...]]] | None = None
    example_h1_three_cohomology: list[int] | None = None

    for combo in combinations(entries, 3):
        for signs in product([1, -1], repeat=3):
            candidate_count += 1
            connection = [
                (target, source, Fraction(sign), form)
                for (target, source, form), sign in zip(combo, signs)
            ]
            if composition_nonzero_counts(connection) != [0, 0]:
                continue
            rank_values = ranks(connection)
            h_values = cohomology_dimensions(rank_values)
            h_tuple = tuple(h_values)
            integrable_distribution[h_tuple] += 1
            if h_values[1] != 3:
                continue
            h1_three_form_multisets[tuple(sorted(form[0] for *_slot, form in combo))] += 1
            h1_three_support_distances.append(len(support(connection) ^ literal_support))
            if sorted(form[0] for *_slot, form in combo) == [1, 2, 3]:
                h1_three_with_all_forms += 1
            if example_h1_three is None:
                example_h1_three = sorted_connection(connection)
                example_h1_three_cohomology = h_values

    cert_search = cert.get("search_space", {})
    cert_dist = cert.get("integrable_distribution", {})
    cert_h1 = cert.get("h1_three_candidates", {})
    cert_consequence = cert.get("consequence_for_sm_closure", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    total_integrable = sum(integrable_distribution.values())
    h1_three_count = sum(
        count for h_values, count in integrable_distribution.items() if h_values[1] == 3
    )
    min_distance = min(h1_three_support_distances)

    expected_distribution = {
        (1, 2, 2, 1): 240,
        (1, 3, 3, 1): 192,
        (1, 4, 5, 2): 96,
        (2, 5, 4, 1): 96,
        (0, 0, 0, 0): 32,
    }
    expected_form_multisets = {
        (1, 1, 1): 48,
        (1, 1, 2): 48,
        (1, 2, 2): 48,
        (2, 2, 2): 48,
    }

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "CORRECTED_A01_SCAN_CANDIDATES_EXIST_SELECTION_UNDETERMINED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate count",
            "PASS" if candidate_count == 6528 == cert_search.get("candidate_count") else "FAIL",
            str(candidate_count),
        ),
        Gate(
            "integrable distribution",
            "PASS" if dict(integrable_distribution) == expected_distribution else "FAIL",
            str(dict(integrable_distribution)),
        ),
        Gate(
            "certificate distribution",
            "PASS"
            if cert_dist.get("total_integrable") == total_integrable == 656
            and cert_dist.get("h_1_3_3_1") == 192
            else "FAIL",
            str(cert_dist),
        ),
        Gate(
            "h1 three count",
            "PASS" if h1_three_count == 192 == cert_h1.get("count") else "FAIL",
            str(h1_three_count),
        ),
        Gate(
            "h1 three support distance",
            "PASS"
            if min_distance == 4
            and cert_h1.get("minimum_support_symmetric_distance_from_literal") == 4
            and cert_h1.get("one_entry_repair_exists") is False
            else "FAIL",
            str(min_distance),
        ),
        Gate(
            "h1 three form multisets",
            "PASS"
            if dict(h1_three_form_multisets) == expected_form_multisets
            and cert_h1.get("uses_e1_e2_e3_once_each") is False
            else "FAIL",
            str(dict(h1_three_form_multisets)),
        ),
        Gate(
            "no h1 three all-form candidate",
            "PASS" if h1_three_with_all_forms == 0 else "FAIL",
            str(h1_three_with_all_forms),
        ),
        Gate(
            "example candidate",
            "PASS"
            if example_h1_three_cohomology == [1, 3, 3, 1]
            and cert_h1.get("example_cohomology_dimensions", {}).get("h1") == 3
            else "FAIL",
            str(example_h1_three),
        ),
        Gate(
            "SM consequence",
            "PASS"
            if cert_consequence.get("can_silently_correct_printed_A01") is False
            and cert_consequence.get("can_select_unique_corrected_A01_from_sparse_scan") is False
            and cert_consequence.get("requires_corrected_source_A01_or_typed_monad_maps") is True
            else "FAIL",
            str(cert_consequence),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_example_candidate_is_selected") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("sparse_h1_three_candidates_exist") is True
            and verdict.get("nearby_typo_repair_for_h1_three_exists") is False
            and verdict.get("torsion_form_e3_absent_from_h1_three_sparse_candidates") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records scan",
            "PASS"
            if contains_all(
                paper,
                [
                    "choose(18,3) * 2^3 = 6528",
                    "There are no integrable `h1=3` candidates",
                    "minimum support symmetric distance",
                    "not obtained by changing one printed",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Corrected A01 candidate scan audit")
    print("==================================")
    print()
    print(f"candidate_count={candidate_count}")
    print(f"total_integrable={total_integrable}")
    print(f"integrable_distribution={dict(integrable_distribution)}")
    print(f"h1_three_count={h1_three_count}")
    print(f"h1_three_form_multisets={dict(h1_three_form_multisets)}")
    print(f"h1_three_min_literal_support_distance={min_distance}")
    print(f"h1_three_with_e1_e2_e3_once_each={h1_three_with_all_forms}")
    print(f"example_h1_three={example_h1_three}")
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
