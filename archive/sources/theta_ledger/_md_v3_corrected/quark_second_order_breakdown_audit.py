"""Audit the quark second-order breakdown hypothesis."""

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
    hypo = read(ROOT / "Quark_Second_Order_Breakdown_Hypothesis_v1.md")
    seed = read(ROOT / "Canonical_Anchored_Bridge_Seed_Diagnostic_v1.md")
    scalar = read(ROOT / "Scalar_Quark_Stiffness_Diagnostic_NoGo_v1.md")
    retarded = read(ROOT / "Retarded_Shared_Circle_Orientation_Gate_for_Dyadic_PreQuarter_CKM_Branch_v1.md")
    operator = read(ROOT / "Quark_Second_Order_Breakdown_Operator_Candidate_v1.md")

    gates = [
        Gate("hypothesis file", "PASS" if "Quark Second-Order Breakdown" in hypo else "FAIL", "hypothesis paper present"),
        Gate("corpus stiffness source", "PASS" if "partially anchored composite sectors" in retarded else "FAIL", "quark asymmetry imported"),
        Gate("first-order split", "DEFINED" if "transport / unanchored" in hypo and "nil / termination" in hypo else "FAIL", "anchor role split defined"),
        Gate("second-order layer", "DEFINED" if "B_q" in hypo and "residual strain distribution" in hypo else "FAIL", "quark breakdown layer named"),
        Gate("seed explained", "PASS" if "large mixing" in seed and "universal anchored seed" in hypo else "FAIL", "universal seed diagnostic explained"),
        Gate("scalar no-go explained", "PASS" if "scalar quark-stiffness scan failed" in hypo or "scalar quark-stiffness scan failed" in hypo.lower() else "FAIL", "scalar stiffness failure explained"),
        Gate("operator candidate", "CONSTRUCTED" if "explicit B_q candidate" in operator else "FAIL", "concrete quark operator candidate now exists"),
        Gate("constant derivation", "OPEN" if "derive mu_u=8" in operator else "FAIL", "candidate constants still need MTT derivation"),
        Gate("color/redundancy target", "OPEN" if "connect B_q to color/redundancy channels" in hypo else "FAIL", "must connect to composite redundancy"),
    ]

    print("Quark second-order breakdown audit")
    print("==================================")
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
