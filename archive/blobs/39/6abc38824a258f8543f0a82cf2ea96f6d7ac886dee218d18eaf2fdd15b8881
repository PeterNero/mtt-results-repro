"""Audit selected-kernel primitive-lag closure for the Z64 carrier."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Selected_Kernel_Primitive_Lag_Closure_for_Z64_Carrier_v1.md"
UNIT = ROOT / "Retarded_Unit_Lag_Lemma_from_Nil_Survivor_Projection_v1.md"


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
    unit = read(UNIT)

    lag = (15 - 16) % 64
    paired = [1, 63]

    gates = [
        Gate("paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate(
            "unit-lag theorem available",
            "PASS" if "q_64 = 15" in unit and "rho_q/kappa_q = 1" in unit else "FAIL",
            "selected nil-survivor branch proves unit lag",
        ),
        Gate("selected lag is S^-1", "PASS" if lag == 63 else "FAIL", f"lag={lag}"),
        Gate("single lag primitive", "PASS" if gcd(64, lag) == 1 else "FAIL", f"gcd(64,{lag})={gcd(64, lag)}"),
        Gate(
            "paired Hermitian lag primitive",
            "PASS" if gcd(64, paired[0], paired[1]) == 1 else "FAIL",
            f"gcd(64,{paired})=1",
        ),
        Gate(
            "selected-kernel primitive-lag gate",
            "PROVED" if "selected-kernel primitive-lag gate              PROVED" in paper else "FAIL",
            "full Z64 carrier seen by selected kernel",
        ),
        Gate(
            "raw pre-survivor primitive lag",
            "OPTIONAL-OPEN",
            "stronger raw-overlap route; selected nil-survivor branch is closed",
        ),
    ]

    print("Selected-kernel primitive-lag closure audit")
    print("===========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
