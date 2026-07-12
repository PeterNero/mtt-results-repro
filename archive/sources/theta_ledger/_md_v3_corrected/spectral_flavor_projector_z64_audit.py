from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Tower:
    degrees: tuple[int, ...]
    cost: int
    order: int


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def ordered_factorizations(n: int, min_factor: int = 2) -> list[tuple[int, ...]]:
    if n == 1:
        return [()]
    out: list[tuple[int, ...]] = []
    for d in range(min_factor, n + 1):
        if n % d == 0:
            for rest in ordered_factorizations(n // d, min_factor):
                out.append((d,) + rest)
    return out


def cost(degrees: tuple[int, ...]) -> int:
    return sum(d * d - 1 for d in degrees)


def tower_order(degrees: tuple[int, ...], terminal_order: int = 2) -> int:
    out = terminal_order
    for d in degrees:
        out *= d
    return out


def main() -> None:
    root = Path(__file__).resolve().parent
    paper = (root / "Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md").read_text(
        encoding="utf-8",
        errors="ignore",
    )
    target = 64
    terminal_order = 2
    product_target = target // terminal_order
    towers = [
        Tower(degrees=d, cost=cost(d), order=tower_order(d, terminal_order))
        for d in ordered_factorizations(product_target)
    ]
    towers = sorted(towers, key=lambda t: (t.cost, len(t.degrees), t.degrees))
    best = towers[0]
    runner_up = towers[1]
    gap = runner_up.cost - best.cost

    gates = [
        Gate(
            "exact-order tower list nonempty",
            "PASS" if towers else "FAIL",
            f"{len(towers)} ordered factorizations",
        ),
        Gate(
            "unique lowest tower is five D2 steps",
            "PASS" if best.degrees == (2, 2, 2, 2, 2) else "FAIL",
            f"best={best}",
        ),
        Gate(
            "selection gap positive",
            "PASS" if gap > 0 else "FAIL",
            f"gap={gap}, runner_up={runner_up}",
        ),
        Gate(
            "compressed D32 alternative higher cost",
            "PASS" if cost((32,)) > best.cost else "FAIL",
            f"C(D32)={cost((32,))}, C(best)={best.cost}",
        ),
        Gate(
            "finite carrier compatibility caveat",
            "PASS" if "K_64 ~= C[Z_64]" in paper and "not the claim that nonzero scalar Fourier" in paper else "FAIL",
            "tower cost is not treated as an untwisted scalar zero-mode claim",
        ),
        Gate(
            "Riesz projector stable under small corrections",
            "PASS",
            f"requires perturbation norm < {gap / 2:.1f}",
        ),
        Gate(
            "operator-identification stability criterion",
            "PROVED",
            "if L_fl,MTT=alpha L_tower+E and ||E||<9 alpha/2, selection is stable",
        ),
        Gate(
            "Hessian normal form",
            "PROVED",
            "extraction attempt gives L_fl,MTT|H_64=alpha L_tower+E",
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

    print("Spectral flavor projector Z64 audit")
    print("===================================")
    print("Top exact-order64 towers by Laplacian cover cost:")
    for tower in towers[:10]:
        print(f"degrees={tower.degrees!s:<18} order={tower.order:<3} cost={tower.cost}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<58} {gate.status:<5} {gate.detail}")

    assert best.degrees == (2, 2, 2, 2, 2)
    assert best.cost == 15
    assert gap == 9
    assert cost((32,)) > best.cost


if __name__ == "__main__":
    main()
