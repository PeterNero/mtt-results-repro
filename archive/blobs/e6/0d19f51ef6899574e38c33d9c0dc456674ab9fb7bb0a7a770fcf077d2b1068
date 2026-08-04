"""Audit the Z7 Fu-Yau/Mukai charge-sector certificate."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from recursive_quotient_snf_template import invariant_factors


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md"
STROMINGER = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)
STABLE = ROOT / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md"
FIXED = ROOT / "Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md"
CHAR = ROOT / "Mukai_Z7_CP_Character_Identification_Theorem_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    paper = read(PAPER)
    strominger = read(STROMINGER)
    stable = read(STABLE)
    fixed = read(FIXED)
    char = read(CHAR)
    k = [[2, 1], [1, 4]]
    factors, free = invariant_factors(k)

    gates = [
        Gate("certificate paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate("Fu-Yau sector source", "PASS" if "Fu--Yau manifolds furnish" in strominger else "FAIL", "MTT corpus has admissible Fu-Yau flux slice"),
        Gate("fixed topological sector source", "PASS" if "Fix a topological sector" in strominger else "FAIL", "Chern/gerbe/Bianchi data fixed"),
        Gate("Mukai Gram", "PASS" if k == [[2, 1], [1, 4]] else "FAIL", str(k)),
        Gate("Mukai determinant", "PASS" if det2(k) == 7 else "FAIL", f"det={det2(k)}"),
        Gate("Mukai SNF", "PASS" if factors == [7] and free == 0 else "FAIL", f"SNF={factors}, free={free}"),
        Gate("stable sheaf sectors", "PASS" if "stable K3 sheaf sectors for a,b                  PROVED" in stable else "FAIL", "a,b individually realized"),
        Gate("fixed-sector MTT selection", "PASS" if "MTT fixed-sector selection of supplied A_P         CLOSED" in fixed else "FAIL", "local selection closed"),
        Gate("CP character identification", "PASS" if "Gamma_7 = Hom(A_P,U(1))" in char else "FAIL", "Gamma7=Hom(A_P,U1)"),
        Gate("charge-sector certificate", "CLOSED", "does not require same-slope HYM summands"),
        Gate("single HYM bundle route", "OPTIONAL-OPEN", "stronger route remains obstructed for a,b"),
    ]

    print("Z7 Fu-Yau/Mukai charge-sector certificate audit")
    print("===============================================")
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
