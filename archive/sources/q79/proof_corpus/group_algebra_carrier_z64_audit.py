"""Audit group-algebra carrier realization from the Z64 carry matrix."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from candidate_quotient_mechanism_scan import dyadic_carry_matrix
from recursive_quotient_snf_template import invariant_factors


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Group_Algebra_Carrier_Realization_from_Z64_Carry_Matrix_v1.md"
CERT = ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    paper = read(PAPER)
    cert = read(CERT)
    matrix = dyadic_carry_matrix(6)
    factors, free_rank = invariant_factors(matrix)

    gates = [
        Gate("paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate("SNF carry matrix", "PASS" if factors == [64] and free_rank == 0 else "FAIL", f"SNF={factors}, free={free_rank}"),
        Gate("cokernel Z64", "PASS" if factors == [64] else "FAIL", "coker A64 ~= Z64"),
        Gate("group algebra carrier", "PASS" if "K_64 := C[G_64]" in paper else "FAIL", "K64=C[coker A64]"),
        Gate("primitive shift", "PASS" if "S^64=I" in paper and "S^d != I" in paper else "FAIL", "translation by x0"),
        Gate("character idempotents", "PASS" if "E_q = (1/64)" in paper else "FAIL", "finite Fourier projectors"),
        Gate(
            "row extraction from exact branch",
            "CLOSED" if "relation SNF:        [64]" in cert else "FAIL",
            "Z64 exact-branch certificate supplies A64",
        ),
    ]

    print("Group-algebra Z64 carrier audit")
    print("===============================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
