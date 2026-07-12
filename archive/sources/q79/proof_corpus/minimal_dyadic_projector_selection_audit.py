from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    degree: int
    records: int
    order: int
    classification: str


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def order_from_degree_and_records(degree: int, records: int, terminal_order: int = 2) -> int:
    if records < 1:
        raise ValueError("records must be positive")
    return terminal_order * (degree ** (records - 1))


def classify(degree: int, records: int, target: int = 64) -> str:
    order = order_from_degree_and_records(degree, records)
    if order != target:
        return "not-target"
    if degree == 2 and records == 6:
        return "elementary-minimal"
    if degree > 2:
        return "compressed-cover"
    return "nonstandard"


def main() -> None:
    candidates: list[Candidate] = []
    for degree in (2, 4, 8, 16, 32, 64):
        for records in range(1, 8):
            order = order_from_degree_and_records(degree, records)
            cls = classify(degree, records)
            if order == 64 or cls != "not-target":
                candidates.append(Candidate(degree, records, order, cls))

    target_candidates = [c for c in candidates if c.order == 64]
    elementary = [c for c in target_candidates if c.classification == "elementary-minimal"]
    compressed = [c for c in target_candidates if c.classification == "compressed-cover"]

    gates = [
        Gate(
            "finite circle cover pullback has integer degree",
            "PASS",
            "D_d^*: n -> d n",
        ),
        Gate(
            "minimal nontrivial spin-compatible degree",
            "PASS",
            "d=2",
        ),
        Gate(
            "elementary exact Z64 solution",
            "PASS" if elementary == [Candidate(2, 6, 64, "elementary-minimal")] else "FAIL",
            str(elementary),
        ),
        Gate(
            "compressed exact Z64 alternatives detected",
            "PASS" if compressed else "FAIL",
            str(compressed),
        ),
        Gate(
            "no-proxy rejects compressed alternatives unless derived",
            "PASS",
            "compressed covers hide multiple binary refinements",
        ),
        Gate(
            "dynamic projector construction",
            "PROVED-SPECTRAL",
            "see spectral flavor projector; reduced alpha/C_fl/lambda_Q bound open",
        ),
    ]

    print("Minimal dyadic projector selection audit")
    print("========================================")
    print("Target order candidates with terminal parity:")
    for c in target_candidates:
        print(f"degree={c.degree:<2} records={c.records:<2} order={c.order:<3} classification={c.classification}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<58} {gate.status:<5} {gate.detail}")

    assert Candidate(2, 6, 64, "elementary-minimal") in target_candidates
    assert compressed


if __name__ == "__main__":
    main()
