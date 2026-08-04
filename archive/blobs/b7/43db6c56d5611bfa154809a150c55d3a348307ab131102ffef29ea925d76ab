"""Audit the finite Iwasawa Dolbeault complex extraction attempt."""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_dolbeault_complex_extraction_certificate.json"
PAPER = ROOT / "Iwasawa_Dolbeault_Complex_Extraction_Attempt_v1.md"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


FORMS = {degree: list(combinations((1, 2, 3), degree)) for degree in range(4)}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def wedge(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    seq = list(left) + list(right)
    if len(set(seq)) < len(seq):
        return None
    inversions = sum(
        1
        for i in range(len(seq))
        for j in range(i + 1, len(seq))
        if seq[i] > seq[j]
    )
    sign = -1 if inversions % 2 else 1
    return sign, tuple(sorted(seq))


def dbar_form(form: tuple[int, ...]) -> dict[tuple[int, ...], Fraction]:
    """Use dbar e1=dbar e2=0, dbar e3=e1 wedge e2."""

    out: dict[tuple[int, ...], Fraction] = {}
    for position, item in enumerate(form):
        if item != 3:
            continue
        before = form[:position]
        after = form[position + 1 :]
        first = wedge(before, (1, 2))
        if first is None:
            continue
        sign1, middle = first
        second = wedge(middle, after)
        if second is None:
            continue
        sign2, result = second
        out[result] = out.get(result, Fraction(0)) + Fraction(((-1) ** position) * sign1 * sign2)
    return out


LITERAL_A01 = [
    (0, 1, Fraction(1), (3,)),
    (0, 2, Fraction(1), (1,)),
    (2, 0, Fraction(-1), (2,)),
]

REPAIR_A32_MINUS = [
    (0, 1, Fraction(1), (3,)),
    (0, 2, Fraction(1), (1,)),
    (2, 1, Fraction(-1), (2,)),
]


def build_map(degree: int, connection: list[tuple[int, int, Fraction, tuple[int, ...]]]) -> list[list[Fraction]]:
    domain = [(vector, form) for vector in range(3) for form in FORMS[degree]]
    codomain = [(vector, form) for vector in range(3) for form in FORMS[degree + 1]]
    codomain_index = {basis: index for index, basis in enumerate(codomain)}
    matrix = [[Fraction(0) for _ in domain] for __ in codomain]

    for column, (vector, form) in enumerate(domain):
        for dform, coefficient in dbar_form(form).items():
            matrix[codomain_index[(vector, dform)]][column] += coefficient
        for target, source, coefficient, one_form in connection:
            if source != vector:
                continue
            product = wedge(one_form, form)
            if product is None:
                continue
            sign, result = product
            matrix[codomain_index[(target, result)]][column] += sign * coefficient
    return matrix


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank_value = 0
    col = 0
    while rank_value < rows and col < cols:
        pivot = None
        for row in range(rank_value, rows):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            col += 1
            continue
        work[rank_value], work[pivot] = work[pivot], work[rank_value]
        pivot_value = work[rank_value][col]
        work[rank_value] = [value / pivot_value for value in work[rank_value]]
        for row in range(rows):
            if row == rank_value or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[rank_value][idx]
                for idx in range(cols)
            ]
        rank_value += 1
        col += 1
    return rank_value


def composition_nonzero_counts(connection: list[tuple[int, int, Fraction, tuple[int, ...]]]) -> list[int]:
    counts: list[int] = []
    for degree in (0, 1):
        first = build_map(degree, connection)
        second = build_map(degree + 1, connection)
        count = 0
        for row in range(len(second)):
            for col in range(len(first[0])):
                value = sum(second[row][mid] * first[mid][col] for mid in range(len(first)))
                if value != 0:
                    count += 1
        counts.append(count)
    return counts


def ranks(connection: list[tuple[int, int, Fraction, tuple[int, ...]]]) -> list[int]:
    return [rank(build_map(degree, connection)) for degree in range(3)]


def cohomology_dimensions(rank_values: list[int]) -> list[int]:
    dims = [3, 9, 9, 3]
    return [
        dims[0] - rank_values[0],
        dims[1] - rank_values[1] - rank_values[0],
        dims[2] - rank_values[2] - rank_values[1],
        dims[3] - rank_values[2],
    ]


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    flux = read(FLUX)

    literal_ranks = ranks(LITERAL_A01)
    literal_counts = composition_nonzero_counts(LITERAL_A01)
    repair_ranks = ranks(REPAIR_A32_MINUS)
    repair_counts = composition_nonzero_counts(REPAIR_A32_MINUS)
    repair_h = cohomology_dimensions(repair_ranks)

    cert_literal = cert.get("literal_integrability_result", {})
    cert_repair = cert.get("minimal_repair_candidate", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "IWASAWA_DOLBEAULT_EXTRACTION_LITERAL_A01_FAILS_INTEGRABILITY_REPAIR_CANDIDATE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source A01 present",
            "PASS"
            if "\\mathcal{A}^{(0,1)}" in flux
            and "\\mu\\,\\bar\\omega^3" in flux
            and "-\\sqrt{\\mu}\\,\\bar\\omega^2" in flux
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "source dbar rule present",
            "PASS"
            if "\\bar\\partial\\bar\\omega^3=\\bar\\omega^1\\wedge\\bar\\omega^2" in flux
            else "FAIL",
            "Iwasawa anti-holomorphic differential checked",
        ),
        Gate(
            "literal ranks computed",
            "PASS" if literal_ranks == [3, 6, 2] == list(cert_literal.get("map_ranks", {}).values()) else "FAIL",
            str(literal_ranks),
        ),
        Gate(
            "literal compositions fail",
            "PASS"
            if literal_counts == [4, 4]
            and cert_literal.get("integrable") is False
            and cert_literal.get("cohomology_dimensions_valid") is False
            else "FAIL",
            str(literal_counts),
        ),
        Gate(
            "literal defect recorded",
            "PASS"
            if "A + A wedge A" in cert_literal.get("curvature_defect", "")
            and "e1 wedge e2" in cert_literal.get("curvature_defect", "")
            else "FAIL",
            cert_literal.get("curvature_defect", ""),
        ),
        Gate(
            "repair not selected",
            "PASS" if cert_repair.get("selected") is False else "FAIL",
            str(cert_repair),
        ),
        Gate(
            "repair integrable",
            "PASS" if repair_counts == [0, 0] and cert_repair.get("integrable") is True else "FAIL",
            str(repair_counts),
        ),
        Gate(
            "repair ranks",
            "PASS" if repair_ranks == [2, 5, 2] == list(cert_repair.get("map_ranks", {}).values()) else "FAIL",
            str(repair_ranks),
        ),
        Gate(
            "repair cohomology",
            "PASS"
            if repair_h == [1, 2, 2, 1]
            and cert_repair.get("cohomology_dimensions", {}).get("h1") == 2
            and cert_repair.get("three_family_slot_fill") is False
            else "FAIL",
            str(repair_h),
        ),
        Gate(
            "SM closure consequence",
            "PASS"
            if cert.get("consequence_for_sm_closure", {}).get(
                "literal_A01_can_fill_zero_mode_slots"
            )
            is False
            and cert.get("consequence_for_sm_closure", {}).get(
                "primitive_C1_blocks_computable_from_this_extraction"
            )
            is False
            else "FAIL",
            str(cert.get("consequence_for_sm_closure", {})),
        ),
        Gate(
            "guardrails forbid repair overclaim",
            "PASS"
            if guardrails.get("silently_corrects_source_A01") is False
            and guardrails.get("uses_repair_candidate_as_selected") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict identifies next step",
            "PASS"
            if verdict.get("literal_source_passes_integrability") is False
            and verdict.get("diagnostic_repair_exists") is True
            and verdict.get("diagnostic_repair_h1") == 2
            and "full monad maps" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records obstruction",
            "PASS"
            if "Literal Integrability Check" in paper
            and "Minimal Index-Repair Candidate" in paper
            and "h1 = 2" in paper
            else "FAIL",
            "paper contains literal defect and diagnostic repair",
        ),
    ]

    print("Iwasawa Dolbeault complex extraction audit")
    print("==========================================")
    print()
    print(f"literal_ranks={literal_ranks}")
    print(f"literal_composition_nonzero_counts={literal_counts}")
    print(f"repair_ranks={repair_ranks}")
    print(f"repair_cohomology_dimensions={repair_h}")
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
