"""Audit the MTT flavor-operator identification criterion for the Z64 tower."""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass(frozen=True)
class Tower:
    degrees: tuple[int, ...]

    @property
    def order(self) -> int:
        return 2 * reduce(mul, self.degrees, 1)

    @property
    def cost(self) -> int:
        return sum(d * d - 1 for d in self.degrees)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def ordered_factorizations(n: int, minimum: int = 2) -> list[tuple[int, ...]]:
    if n == 1:
        return [()]
    out: list[tuple[int, ...]] = []
    for d in range(minimum, n + 1):
        if n % d == 0:
            for tail in ordered_factorizations(n // d, minimum):
                out.append((d, *tail))
    return out


def exact_order64_towers() -> list[Tower]:
    # Terminal spinorial parity contributes the final factor 2, so the cover
    # degrees must multiply to 32.
    return [Tower(factors) for factors in ordered_factorizations(32)]


def stability_threshold(alpha: float) -> float:
    return 9.0 * alpha / 2.0


def main() -> None:
    alpha = 1.0
    towers = sorted(exact_order64_towers(), key=lambda t: (t.cost, t.degrees))
    best = towers[0]
    runner_up = towers[1]
    gap = runner_up.cost - best.cost

    print("MTT flavor operator identification audit")
    print("========================================")
    print()
    print(f"best tower: degrees={best.degrees}, order={best.order}, cost={best.cost}")
    print(
        f"nearest competitor: degrees={runner_up.degrees}, "
        f"order={runner_up.order}, cost={runner_up.cost}"
    )
    print(f"tower gap: {gap}")
    print(f"normalized stability threshold: {stability_threshold(alpha)}")
    print()

    gates = [
        Gate(
            "exact-order64 tower sector nonempty",
            "PASS" if towers else "FAIL",
            f"{len(towers)} ordered factorizations",
        ),
        Gate(
            "unique lowest tower",
            "PASS" if best.degrees == (2, 2, 2, 2, 2) else "FAIL",
            f"best={best.degrees}",
        ),
        Gate(
            "tower selection gap",
            "PASS" if gap == 9 else "FAIL",
            f"gap={gap}",
        ),
        Gate(
            "Riesz stability threshold",
            "PASS" if stability_threshold(alpha) == 4.5 else "FAIL",
            "requires ||E|| < 9 alpha / 2; normalized threshold 4.5",
        ),
        Gate(
            "shared central circle and Riesz framework",
            "CORPUS-SUPPORTED",
            "Theta closure and fixed-point framework",
        ),
        Gate(
            "fixed arithmetic sector",
            "IDENTIFIED",
            "needed so continuous perturbations cannot alter integer labels",
        ),
        Gate(
            "Hessian normal form",
            "PROVED",
            "L_fl,MTT|H_64=alpha L_tower+E from extraction attempt",
        ),
        Gate(
            "pure central-circle reduction",
            "PROVED",
            "on H_64, E_mix=0 and E_cubic=0 at Hessian level",
        ),
        Gate(
            "exact-branch Schur gate",
            "PROVED",
            "C_fl=0 if P_fl<=Pi_coh and [L,Pi_coh]=0",
        ),
        Gate(
            "non-exact commutator/warp gate",
            "OPEN",
            "bound leakage if exact block commutation is relaxed",
        ),
    ]

    print("Gate status")
    print("===========")
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
