"""Audit the damping Hessian to Z64 exact-branch block identification."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from functools import reduce
from math import gcd
from operator import mul
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "damping_hessian_z64_block_identification_certificate.json"
PAPER = ROOT / "Damping_Hessian_Z64_Block_Identification_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def approx_equal(left: float, right: float, rel: float = 1e-12, abs_tol: float = 1e-12) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def ordered_factorizations(n: int, minimum: int = 2) -> list[tuple[int, ...]]:
    if n == 1:
        return [()]
    out: list[tuple[int, ...]] = []
    for d in range(minimum, n + 1):
        if n % d == 0:
            for tail in ordered_factorizations(n // d, minimum):
                out.append((d, *tail))
    return out


def tower_cost(degrees: tuple[int, ...]) -> int:
    return sum(d * d - 1 for d in degrees)


def shift_order(n: int, step: int) -> int:
    return n // gcd(n, step)


def r1_exact(n: int, lambda_star: float = 15.0) -> float:
    return math.sqrt(math.log(n) / lambda_star)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    source_text = {key: read(path) for key, path in sources.items()}
    data = cert["exact_branch_data"]
    verdict = cert["verdict"]

    towers = sorted(ordered_factorizations(32), key=lambda t: (tower_cost(t), t))
    best = towers[0]
    runner_up = towers[1]
    gap = tower_cost(runner_up) - tower_cost(best)

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "EXACT_BRANCH_HESSIAN_KERNEL_IDENTIFICATION_CERTIFIED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "Z64 exact source has Hessian/kernel",
            "PASS"
            if contains_all(
                source_text["z64_exact_branch"],
                ["L_64 = alpha L_tower", "K_ret,64 = S^{-1}", "E_Schur = 0", "q_64=15"],
            )
            else "FAIL",
            str(sources["z64_exact_branch"]),
        ),
        Gate(
            "operator source has tower gap",
            "PASS"
            if contains_all(source_text["z64_operator"], ["lambda_* = 15 alpha", "lambda_next = 24 alpha", "Delta = lambda_next - lambda_* = 9 alpha"])
            else "FAIL",
            str(sources["z64_operator"]),
        ),
        Gate(
            "Schur source collapses exact branch",
            "PASS"
            if contains_all(source_text["exact_schur"], ["C_fl=0 in exact branch", "E_Schur=0 in exact branch", "C_fl/(alpha lambda_Q)<9/2 in exact branch"])
            else "FAIL",
            str(sources["exact_schur"]),
        ),
        Gate(
            "projector compatibility caveat retained",
            "PASS"
            if contains_all(source_text["projector_compatibility"], ["twisted/equivariant central-circle", "Ran(P_fl) subset Ran(Pi_coh)", "MTT Hessian selects exact Z_64 carrier"])
            else "FAIL",
            str(sources["projector_compatibility"]),
        ),
        Gate("primitive shift", "PASS" if shift_order(64, 63) == 64 else "FAIL", "S^-1 has order 64"),
        Gate("selected tower", "PASS" if list(best) == data["selected_tower"] else "FAIL", f"best={best}"),
        Gate("selected cost", "PASS" if tower_cost(best) == data["selected_cost"] else "FAIL", str(tower_cost(best))),
        Gate("next cost", "PASS" if tower_cost(runner_up) == data["next_cost"] else "FAIL", str(tower_cost(runner_up))),
        Gate("tower gap", "PASS" if gap == data["gap"] else "FAIL", str(gap)),
        Gate("Schur correction zero", "PASS" if data["schur_correction"] == 0 else "FAIL", str(data["schur_correction"])),
    ]

    for item in cert["tested_cases"]:
        n = int(item["N"])
        actual = r1_exact(n)
        gates.extend(
            [
                Gate(
                    f"N={n} exact-branch R1",
                    "PASS" if approx_equal(actual, float(item["R1_normalized_exact_branch"])) else "FAIL",
                    f"{actual:.16g}",
                ),
                Gate(
                    f"N={n} closes R1<=2",
                    "PASS" if actual <= 2.0 else "FAIL",
                    f"{actual:.16g} <= 2",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "exact branch only",
                "PASS"
                if verdict.get("exact_branch_hessian_kernel_identified") is True
                and verdict.get("stronger_full_mixed_hessian_extraction_closed") is False
                and verdict.get("numeric_absolute_normalization_closed") is False
                and verdict.get("remaining_premise_count") == 1
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "paper forbids overclaim",
                "PASS"
                if contains_all(
                    paper,
                    [
                        "does not derive the exact branch from the full mixed MTT Hessian",
                        "physical action-normalization certificate for G10 and alpha",
                        "Do not choose `alpha`, `G10`",
                    ],
                )
                else "FAIL",
                str(PAPER),
            ),
        ]
    )

    print("Damping Hessian Z64 block identification audit")
    print("==============================================")
    print()
    print(f"tested_cases={len(cert['tested_cases'])}")
    print(f"remaining_premise_count={verdict.get('remaining_premise_count')}")
    print()

    width = max(len(gate.label) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
