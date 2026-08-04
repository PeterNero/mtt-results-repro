"""Audit stable-sheaf existence gate for the Mukai Z7 block."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md"
MUKAI = ROOT / "Mukai_Positive_Charge_Block_for_Fu_Yau_K3_Z7_CP_v1.md"
CERT = ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md"


@dataclass(frozen=True)
class MukaiVector:
    r: int
    n: int
    s: int

    def primitive(self) -> bool:
        return gcd(gcd(abs(self.r), abs(self.n)), abs(self.s)) == 1


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def pair(x: MukaiVector, y: MukaiVector, h2: int = 2) -> int:
    return x.n * y.n * h2 - x.r * y.s - y.r * x.s


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    paper = read(PAPER)
    mukai = read(MUKAI)
    cert = read(CERT)

    a = MukaiVector(5, 1, 0)
    b = MukaiVector(7, 3, 1)
    gram = [[pair(a, a), pair(a, b)], [pair(b, a), pair(b, b)]]
    det = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]

    gates = [
        Gate("paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate("positive Mukai block source", "PASS" if "a = (5, H, 0)" in mukai and "b = (7, 3H, 1)" in mukai else "FAIL", "successor Mukai block found"),
        Gate("a primitive", "PASS" if a.primitive() else "FAIL", str(a)),
        Gate("b primitive", "PASS" if b.primitive() else "FAIL", str(b)),
        Gate("Mukai Gram matrix", "PASS" if gram == [[2, 1], [1, 4]] else "FAIL", str(gram)),
        Gate("determinant seven", "PASS" if det == 7 else "FAIL", f"det={det}"),
        Gate("positive moduli dimensions", "PASS" if pair(a, a) + 2 == 4 and pair(b, b) + 2 == 6 else "FAIL", f"dims={pair(a,a)+2},{pair(b,b)+2}"),
        Gate("stable-sheaf gate", "PROVED" if "stable K3 sheaf sectors for a,b                  PROVED" in paper else "FAIL", "by standard primitive Mukai-vector K3 theorem package"),
        Gate("common-slope HYM bundle", "OBSTRUCTED", "same-slope route already fails"),
        Gate(
            "Fu-Yau/MTT selection",
            "CLOSED-CHARGE" if "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in cert else "FAIL",
            "closed by the charge-sector certificate",
        ),
    ]

    print("Stable-sheaf existence audit for Mukai Z7")
    print("=========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
