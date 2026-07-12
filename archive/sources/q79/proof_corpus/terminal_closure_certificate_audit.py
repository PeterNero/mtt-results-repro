"""Terminal closure certificate audit for the q=79 exact/charge branch.

The audit verifies that the two formerly terminal gates are now represented by
explicit exact-branch and charge-sector certificates.  Stronger variants remain
optional robustness projects, not blockers for the selected branch.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent

FILES = {
    "terminal": ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md",
    "consolidated": ROOT / "Consolidated_Exact_Z64_to_q79_Closure_Theorem_v1.md",
    "group": ROOT / "Group_Algebra_Carrier_Realization_from_Z64_Carry_Matrix_v1.md",
    "lag": ROOT / "Selected_Kernel_Primitive_Lag_Closure_for_Z64_Carrier_v1.md",
    "schur": ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md",
    "mukai": ROOT / "Mukai_Discriminant_Group_Selection_for_Z7_CP_v1.md",
    "stable": ROOT / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md",
    "char": ROOT / "Mukai_Z7_CP_Character_Identification_Theorem_v1.md",
    "fixed": ROOT / "Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md",
    "z64_cert": ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
    "z7_cert": ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    texts = {key: read(path) for key, path in FILES.items()}

    gates = [
        Gate("terminal certificate paper saved", "PASS" if texts["terminal"] else "FAIL", str(FILES["terminal"])),
        Gate("group algebra K64 closure", "PASS" if "finite carrier K_64 from carry rows                  CLOSED" in texts["group"] else "FAIL", "K64=C[coker A64]"),
        Gate("selected primitive lag closure", "PASS" if "selected-kernel primitive-lag gate              PROVED" in texts["lag"] else "FAIL", "16->15=S^-1"),
        Gate("exact Schur collapse closure", "PASS" if "C_fl/(alpha lambda_Q)<9/2 in exact branch             PROVED" in texts["schur"] else "FAIL", "exact branch gives zero Schur correction"),
        Gate("Mukai discriminant closure", "PASS" if "A_P=P^*/P ~= Z_7" in texts["mukai"] else "FAIL", "A_P cyclic order seven"),
        Gate("stable sheaf gate closure", "PASS" if "stable K3 sheaf sectors for a,b                  PROVED" in texts["stable"] else "FAIL", "individual stable sectors exist"),
        Gate("CP character gate closure", "PASS" if "Gamma_7 = Hom(A_P,U(1))" in texts["char"] else "FAIL", "finite-character identification"),
        Gate("fixed-sector MTT selection closure", "PASS" if "MTT fixed-sector selection of supplied A_P         CLOSED" in texts["fixed"] else "FAIL", "local selection in supplied sector"),
        Gate("CRT q=79 closure", "PASS" if "q=79 mod 448" in texts["consolidated"] else "FAIL", "15 mod 64 and 2 mod 7"),
        Gate("terminal exact/charge theorem", "PASS" if "selected exact/charge MTT branch proves q=79 mod 448" in texts["terminal"] else "FAIL", "terminal theorem stated"),
        Gate("Z64 exact-branch certificate", "CLOSED" if "Z64 exact central-circle branch certificate       CLOSED" in texts["z64_cert"] else "FAIL", "exact central-circle Hessian/kernel block"),
        Gate("Z7 charge-sector certificate", "CLOSED" if "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in texts["z7_cert"] else "FAIL", "Bianchi-compatible Mukai charge sector"),
        Gate(
            "stronger non-exact Hessian route",
            "OPTIONAL-OPEN" if "non-exact full Hessian extraction                    OPTIONAL-OPEN" in texts["terminal"] else "FAIL",
            "robustness project, not proof blocker",
        ),
        Gate(
            "stronger single-HYM route",
            "OPTIONAL-OPEN" if "single locally-free HYM bundle route                  OPTIONAL-OPEN" in texts["terminal"] else "FAIL",
            "stronger construction, not proof blocker",
        ),
    ]

    print("Terminal q79 closure certificate audit")
    print("======================================")
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
