"""Check the B_q up/down stiffness Hessian extraction target."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    paper = read(ROOT / "Bq_UpDown_Stiffness_Hessian_Extraction_Target_v1.md")
    orientation = read(ROOT / "Bq_Retarded_Predecessor_Orientation_Lock_v1.md")
    gap = read(ROOT / "Bq_No_Double_Counting_Gap_Selection_Lemma_v1.md")
    color = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")

    gates = [
        Gate("paper saved", "PASS" if "Hessian Extraction Definition" in paper else "FAIL", "stiffness target paper present"),
        Gate("orientation fixed", "PASS" if "sigma = -1" in paper and "sigma = -1" in orientation else "FAIL", "predecessor branch imported"),
        Gate("gap fixed", "PASS" if "lambda_lens - lambda_nil" in paper and "lambda_lens - lambda_nil" in gap else "FAIL", "reduced gap imported"),
        Gate("color source fixed", "PASS" if "1/2" in paper and "delta^2/2" in color else "FAIL", "Schur color coefficient imported"),
        Gate("mu definition", "PASS" if "<e_J, H_x^cl e_J>" in paper and "H_anchor" in paper else "FAIL", "mu_x is a Hessian ratio"),
        Gate("no-proxy condition", "PASS" if "no CKM angle, quark mass, or Yukawa singular value used as input" in paper else "FAIL", "proxy inputs excluded"),
        Gate("actual Hessian blocks", "OPEN", "H_u^cl, H_d^cl, H_anchor still need to be supplied"),
    ]

    print("B_q up/down stiffness Hessian extraction target check")
    print("=====================================================")
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

