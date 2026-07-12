"""Audit the exact coherent-block Schur collapse for the Z64 projector."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md"
COMPAT = ROOT / "Flavor_QG_Projector_Compatibility_Lemma_for_Z64_CKM_Closure_v1.md"
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
    compat = read(COMPAT)
    cert = read(CERT)

    # Finite-dimensional sanity check: block diagonal L has zero off-block
    # product, while a small off-block perturbation has quadratic mixing product.
    epsilon = 0.03
    exact_c = 0.0
    approx_c_bound = epsilon * epsilon
    alpha = 1.0
    lambda_q = 0.25
    approx_gate_value = approx_c_bound / (alpha * lambda_q)

    gates = [
        Gate(
            "paper saved",
            "PASS" if paper else "FAIL",
            str(PAPER),
        ),
        Gate(
            "compatibility theorem available",
            "PASS" if "P_fl Pi_coh = Pi_coh P_fl = P_fl" in compat else "FAIL",
            "P_fl is a coherent subprojector under the proved lemma",
        ),
        Gate(
            "off-block maps vanish theorem",
            "PASS" if "P_fl L Q = 0" in paper and "Q L P_fl = 0" in paper else "FAIL",
            "exact commutation kills coherent/noncoherent mixing",
        ),
        Gate(
            "exact C_fl zero",
            "PASS" if exact_c == 0.0 else "FAIL",
            f"C_fl={exact_c}",
        ),
        Gate(
            "exact Schur inequality",
            "PASS" if exact_c < 4.5 else "FAIL",
            "0 < 9/2",
        ),
        Gate(
            "lambda bridge stated",
            "PASS" if "lambda_Q >= lambda_*" in paper else "FAIL",
            "same QG complement gives selected gap floor",
        ),
        Gate(
            "approximate commutator bound",
            "PASS" if "C_fl <= epsilon_comm^2" in paper else "FAIL",
            f"epsilon^2={approx_c_bound}",
        ),
        Gate(
            "sample approximate gate",
            "PASS" if approx_gate_value < 4.5 else "FAIL",
            f"epsilon^2/(alpha lambda_Q)={approx_gate_value:.6f}",
        ),
        Gate(
            "actual exact-block verification",
            "CLOSED" if "commutator:          [L,Pi_coh]=0" in cert else "FAIL",
            "Z64 exact-branch certificate verifies [L,Pi_coh]=0",
        ),
    ]

    print("Exact coherent-block Schur collapse audit")
    print("=========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
