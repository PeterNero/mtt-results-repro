"""Audit the invariant A01 repair obstruction for selected D_E."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any

from iwasawa_dolbeault_complex_extraction_audit import (
    LITERAL_A01,
    cohomology_dimensions,
    ranks,
)


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_invariant_a01_repair_obstruction_certificate.json"
PAPER = ROOT / "Iwasawa_Invariant_A01_Repair_Obstruction_v1.md"
DOLBEAULT = CERT_DIR / "iwasawa_dolbeault_complex_extraction_certificate.json"
SCAN = CERT_DIR / "corrected_a01_candidate_scan_certificate.json"
TORSION = CERT_DIR / "invariant_mc_torsion_branch_gate_certificate.json"
SELECTED_DE = CERT_DIR / "iwasawa_selected_de_construction_attempt_certificate.json"


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


PAIR_INDEX = {(1, 2): 0, (1, 3): 1, (2, 3): 2}


def wedge_one(left: int, right: int) -> tuple[int, int] | None:
    if left == right:
        return None
    if left < right:
        return 1, PAIR_INDEX[(left, right)]
    return -1, PAIR_INDEX[(right, left)]


RawEntry = tuple[int, int, int, int]


def curvature_zero(raw_connection: list[RawEntry]) -> bool:
    """Check dbar A + A wedge A = 0 for invariant one-form entries."""

    entries: dict[tuple[int, int], list[tuple[int, int]]] = {
        (row, col): [] for row in range(3) for col in range(3)
    }
    for row, col, coefficient, form in raw_connection:
        entries[(row, col)].append((coefficient, form))

    curvature: dict[tuple[int, int], list[int]] = {
        (row, col): [0, 0, 0] for row in range(3) for col in range(3)
    }

    for row, col, coefficient, form in raw_connection:
        if form == 3:
            curvature[(row, col)][0] += coefficient

    for row in range(3):
        for col in range(3):
            for mid in range(3):
                for left_coefficient, left_form in entries[(row, mid)]:
                    for right_coefficient, right_form in entries[(mid, col)]:
                        product_form = wedge_one(left_form, right_form)
                        if product_form is None:
                            continue
                        sign, pair_index = product_form
                        curvature[(row, col)][pair_index] += (
                            sign * left_coefficient * right_coefficient
                        )

    return all(value == [0, 0, 0] for value in curvature.values())


def all_entries() -> list[tuple[int, int, int]]:
    return [
        (row, col, form)
        for row in range(3)
        for col in range(3)
        for form in (1, 2, 3)
    ]


def literal_raw() -> list[RawEntry]:
    return [
        (row, col, int(coefficient), form[0])
        for row, col, coefficient, form in LITERAL_A01
    ]


def literal_completion_counts() -> tuple[dict[int, int], dict[int, int]]:
    literal_support = {(row, col, form) for row, col, _coefficient, form in literal_raw()}
    available = [entry for entry in all_entries() if entry not in literal_support]
    tested: dict[int, int] = {}
    integrable: dict[int, int] = {}

    for extra_count in range(1, 5):
        tested[extra_count] = 0
        integrable[extra_count] = 0
        for combo in combinations(available, extra_count):
            for signs in product((1, -1), repeat=extra_count):
                tested[extra_count] += 1
                raw = literal_raw() + [
                    (row, col, sign, form)
                    for (row, col, form), sign in zip(combo, signs)
                ]
                if curvature_zero(raw):
                    integrable[extra_count] += 1

    return tested, integrable


def raw_to_connection(raw: list[RawEntry]) -> list[tuple[int, int, Fraction, tuple[int, ...]]]:
    return [
        (row, col, Fraction(coefficient), (form,))
        for row, col, coefficient, form in raw
    ]


def torsion_support_distribution() -> tuple[dict[int, int], dict[int, Counter[tuple[int, int, int, int]]]]:
    tested: dict[int, int] = {}
    distributions: dict[int, Counter[tuple[int, int, int, int]]] = {}

    entries = all_entries()
    for entry_count in range(1, 6):
        tested[entry_count] = 0
        distributions[entry_count] = Counter()
        for combo in combinations(entries, entry_count):
            if not any(form == 3 for _row, _col, form in combo):
                continue
            for signs in product((1, -1), repeat=entry_count):
                tested[entry_count] += 1
                raw = [
                    (row, col, sign, form)
                    for (row, col, form), sign in zip(combo, signs)
                ]
                if not curvature_zero(raw):
                    continue
                cohomology = tuple(cohomology_dimensions(ranks(raw_to_connection(raw))))
                distributions[entry_count][cohomology] += 1

    return tested, distributions


def cert_key(prefix: str, count: int) -> str:
    return f"{prefix}_{count}"


def main() -> None:
    cert = load_json(CERT)
    dolbeault = load_json(DOLBEAULT)
    scan = load_json(SCAN)
    torsion = load_json(TORSION)
    selected_de = load_json(SELECTED_DE)
    paper = read(PAPER)

    completion_tested, completion_integrable = literal_completion_counts()
    torsion_tested, torsion_dist = torsion_support_distribution()

    cert_completion = cert.get("literal_completion_search", {})
    cert_torsion = cert.get("torsion_support_search", {})
    consequence = cert.get("selected_de_consequence", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    expected_completion_tested = {1: 48, 2: 1104, 3: 16192, 4: 170016}
    expected_completion_integrable = {1: 0, 2: 0, 3: 0, 4: 0}
    expected_torsion_tested = {
        1: 18,
        2: 792,
        3: 16872,
        4: 231840,
        5: 2309184,
    }
    expected_torsion_dist = {
        1: Counter(),
        2: Counter(),
        3: Counter({(1, 2, 2, 1): 48}),
        4: Counter({(1, 2, 2, 1): 384}),
        5: Counter({(1, 2, 2, 1): 960}),
    }

    cert_completion_tested = {
        count: cert_completion.get("tested_candidates", {}).get(cert_key("extra", count))
        for count in range(1, 5)
    }
    cert_completion_integrable = {
        count: cert_completion.get("integrable_completions_found", {}).get(
            cert_key("extra", count)
        )
        for count in range(1, 5)
    }
    cert_torsion_tested = {
        count: cert_torsion.get("tested_candidates", {}).get(cert_key("entries", count))
        for count in range(1, 6)
    }
    cert_torsion_h13 = {
        count: cert_torsion.get("integrable_h1_equals_three_count", {}).get(
            cert_key("entries", count)
        )
        for count in range(1, 6)
    }

    h1_three_total = sum(
        value
        for dist in torsion_dist.values()
        for cohomology, value in dist.items()
        if cohomology[1] == 3
    )

    gates = [
        Gate(
            "certificate status",
            "RETIRED"
            if cert.get("status")
            == "INVARIANT_A01_REPAIR_PATH_RETIRED_TYPED_OR_NONINVARIANT_REQUIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependency statuses",
            "PASS"
            if dolbeault.get("literal_integrability_result", {}).get("integrable") is False
            and scan.get("status") == "CORRECTED_A01_SCAN_CANDIDATES_EXIST_SELECTION_UNDETERMINED"
            and torsion.get("status")
            == "INVARIANT_MC_TORSION_BRANCH_GIVES_H1_TWO_IN_THREE_ENTRY_ANSATZ"
            and selected_de.get("status")
            == "SELECTED_D_E_CONSTRUCTION_BLOCKED_BY_MISSING_CONNECTION_DATA_DIAGNOSTIC_PIPELINE_READY"
            else "FAIL",
            "prior gates imported",
        ),
        Gate(
            "literal completion tested counts",
            "PASS"
            if completion_tested == expected_completion_tested
            and cert_completion_tested == expected_completion_tested
            else "FAIL",
            str(completion_tested),
        ),
        Gate(
            "literal completion obstruction",
            "PASS"
            if completion_integrable == expected_completion_integrable
            and cert_completion_integrable == expected_completion_integrable
            else "FAIL",
            str(completion_integrable),
        ),
        Gate(
            "torsion support tested counts",
            "PASS"
            if torsion_tested == expected_torsion_tested
            and cert_torsion_tested == expected_torsion_tested
            else "FAIL",
            str(torsion_tested),
        ),
        Gate(
            "torsion support distribution",
            "PASS" if torsion_dist == expected_torsion_dist else "FAIL",
            str({key: dict(value) for key, value in torsion_dist.items()}),
        ),
        Gate(
            "no torsion h1 three",
            "PASS"
            if h1_three_total == 0
            and all(value == 0 for value in cert_torsion_h13.values())
            else "FAIL",
            str(h1_three_total),
        ),
        Gate(
            "selected D_E consequence",
            "PASS"
            if consequence.get("corrected_invariant_A01_route_closed_as_current_proof_source")
            is True
            and consequence.get("typed_monad_cech_route_remains_primary") is True
            and consequence.get("non_invariant_spectral_galerkin_route_remains_fallback")
            is True
            and consequence.get("selected_D_E_still_requires_new_non_invariant_or_typed_source")
            is True
            else "FAIL",
            str(consequence),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_no_iwasawa_bundle_can_have_three_families") is False
            and guardrails.get("claims_no_non_invariant_D_E_can_work") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("uses_signed_invariant_search_as_HYM_proof") is False
            and guardrails.get("uses_diagnostic_h1_three_candidate_as_selected") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("selected_D_E_constructed") is False
            and "retire invariant A01 repair" in verdict.get("fix_achieved", "")
            and "typed monad/Cech" in verdict.get("next_step", "")
            and "non-invariant spectral Galerkin" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records obstruction",
            "PASS"
            if contains_all(
                paper,
                [
                    "not fixed by adding up to four signed invariant entries",
                    "integrable + e3 support -> h1 = 2",
                    "R1 corrected invariant A01: retired",
                    "construct selected cohomology by typed monad/Cech methods",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa invariant A01 repair obstruction audit")
    print("==============================================")
    print()
    print(f"literal_completion_tested={completion_tested}")
    print(f"literal_completion_integrable={completion_integrable}")
    print(f"torsion_support_tested={torsion_tested}")
    print(
        "torsion_support_distribution="
        f"{ {key: dict(value) for key, value in torsion_dist.items()} }"
    )
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
