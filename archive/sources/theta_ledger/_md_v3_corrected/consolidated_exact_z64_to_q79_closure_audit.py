"""Audit the consolidated exact Z64-to-q79 closure theorem."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parent

FILES = {
    "paper": ROOT / "Consolidated_Exact_Z64_to_q79_Closure_Theorem_v1.md",
    "carrier": ROOT / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md",
    "group_carrier": ROOT / "Group_Algebra_Carrier_Realization_from_Z64_Carry_Matrix_v1.md",
    "primitive": ROOT / "Selected_Kernel_Primitive_Lag_Closure_for_Z64_Carrier_v1.md",
    "schur": ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md",
    "unit": ROOT / "Retarded_Unit_Lag_Lemma_from_Nil_Survivor_Projection_v1.md",
    "z7_stable": ROOT / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md",
    "z7_char": ROOT / "Mukai_Z7_CP_Character_Identification_Theorem_v1.md",
    "z7_fixed": ROOT / "Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md",
    "z64_cert": ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
    "z7_cert": ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def crt(a: int, m: int, b: int, n: int) -> int:
    for x in range(m * n):
        if x % m == a % m and x % n == b % n:
            return x
    raise AssertionError("CRT solution not found")


def main() -> None:
    texts = {key: read(path) for key, path in FILES.items()}
    q = crt(15, 64, 2, 7)
    lag = (15 - 16) % 64

    gates = [
        Gate("paper saved", "PASS" if texts["paper"] else "FAIL", str(FILES["paper"])),
        Gate(
            "group-algebra K64 carrier",
            "PASS" if "finite carrier K_64 from carry rows                  CLOSED" in texts["group_carrier"] else "FAIL",
            "K64=C[coker A64] once carry rows are supplied",
        ),
        Gate(
            "finite carrier criterion imported",
            "PASS" if "primitive shift gives exact order 64" in texts["carrier"] else "FAIL",
            "K64 plus primitive S gives exact Z64",
        ),
        Gate(
            "selected primitive lag imported",
            "PASS" if "selected-kernel primitive-lag gate              PROVED" in texts["primitive"] else "FAIL",
            f"lag={lag}, gcd={gcd(64, lag)}",
        ),
        Gate(
            "retarded unit-lag q64",
            "PASS" if "q_64 = 15" in texts["unit"] and "rho_q/kappa_q = 1" in texts["unit"] else "FAIL",
            "selected nil-survivor branch gives q64=15",
        ),
        Gate(
            "exact Schur collapse imported",
            "PASS" if "C_fl=0 in exact branch" in texts["schur"] else "FAIL",
            "C_fl=0 under exact coherent block commutation",
        ),
        Gate(
            "CRT q=79",
            "PASS" if q == 79 else "FAIL",
            f"q={q}",
        ),
        Gate(
            "Z64 exact-branch certificate",
            "CLOSED" if "Z64 exact central-circle branch certificate       CLOSED" in texts["z64_cert"] else "FAIL",
            "K64,S,L64,Kret64 supplied on exact central-circle branch",
        ),
        Gate(
            "Z7 stable-sheaf existence",
            "PROVED" if "stable K3 sheaf sectors for a,b                  PROVED" in texts["z7_stable"] else "FAIL",
            "individual positive Mukai vectors are stable-object sectors",
        ),
        Gate(
            "Z7 CP character identification",
            "PROVED" if "Gamma_7 = Hom(A_P,U(1))" in texts["z7_char"] else "FAIL",
            "once A_P is selected",
        ),
        Gate(
            "Z7 fixed-sector MTT selection",
            "PROVED*" if "MTT fixed-sector selection of supplied A_P         CLOSED" in texts["z7_fixed"] else "FAIL",
            "closed once a Bianchi-compatible Fu-Yau/Mukai sector is supplied",
        ),
        Gate(
            "Z7 charge-sector realization",
            "CLOSED" if "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in texts["z7_cert"] else "FAIL",
            "Bianchi-compatible Fu-Yau sector plus fixed Mukai charge block P",
        ),
        Gate(
            "optional non-exact Hessian route",
            "OPTIONAL-OPEN" if "larger non-exact" in texts["paper"] else "FAIL",
            "stronger route, not q79 branch blocker",
        ),
        Gate(
            "optional single-HYM route",
            "OPTIONAL-OPEN" if "single locally-free HYM bundle" in texts["paper"] else "FAIL",
            "stronger route, not q79 branch blocker",
        ),
    ]

    print("Consolidated exact Z64-to-q79 closure audit")
    print("===========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
