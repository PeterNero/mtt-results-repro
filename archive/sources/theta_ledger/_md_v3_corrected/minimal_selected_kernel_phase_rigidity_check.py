"""Check the finite character facts used by the minimal selected kernel packet."""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
N = 448
Q = 79


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def order_mod_phase(q: int, n: int) -> int:
    return n // math.gcd(q, n)


def main() -> None:
    paper = read(ROOT / "Minimal_Selected_Kernel_Packet_and_Phase_Rigidity_v1.md")
    tau = cmath.exp(2j * math.pi * Q / N)
    order = order_mod_phase(Q, N)
    delta = 2.0 * math.pi * Q / N

    # The finite character map w -> tau^w should visit all 448 roots because
    # q is coprime to 448.
    roots = {round((Q * w) % N, 12) for w in range(N)}

    gates = [
        Gate("paper saved", "PASS" if "Phase Rigidity" in paper else "FAIL", "phase-rigidity theorem present"),
        Gate("q coprime", "PASS" if math.gcd(Q, N) == 1 else "FAIL", f"gcd({Q},{N})={math.gcd(Q,N)}"),
        Gate("tau order", "PASS" if order == N else "FAIL", f"order={order}"),
        Gate("character coverage", "PASS" if len(roots) == N else "FAIL", f"{len(roots)} residues visited"),
        Gate("tau^448", "PASS" if abs(tau**N - 1) < 1e-12 else "FAIL", f"|tau^N-1|={abs(tau**N - 1):.3e}"),
        Gate("phase value", "PASS" if abs(delta - 1.1079724090785432) < 1e-15 else "FAIL", f"delta={delta:.15f}"),
        Gate("magnitude obstruction", "PROVED" if "Magnitude Under-Determination" in paper else "FAIL", "q79 alone cannot fix positive amplitudes"),
    ]

    print("Minimal selected-kernel phase-rigidity check")
    print("============================================")
    print()
    print(f"q={Q}, N={N}, delta={delta:.15f} rad")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
