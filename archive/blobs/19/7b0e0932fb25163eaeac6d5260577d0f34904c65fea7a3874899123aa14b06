"""Audit what remains before no-proxy Yukawa and mass closure.

This is intentionally a status audit.  It distinguishes the closed q79 CP
phase bridge from the still-open task of deriving Yukawa magnitudes and mass
ratios from selected overlap kernels.
"""

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
    status = read(ROOT / "CKM_Phase_Bridge_and_No_Proxy_Flavor_Closure_Status_v1.md")
    terminal = read(ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    execution = read(ROOT / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md")

    gates = [
        Gate(
            "finite CP quotient",
            "CLOSED" if "selected exact/charge MTT branch proves q=79 mod 448" in terminal else "FAIL",
            "q79 exact/charge branch closed",
        ),
        Gate(
            "CKM phase bridge",
            "COMPATIBLE" if "J_MTT = P sin(delta_MTT)" in status else "FAIL",
            "q=79 gives CKM-compatible Jarlskog invariant",
        ),
        Gate(
            "real benchmark reproducibility",
            "BENCHMARK" if "reproduces the real benchmark" in execution and "Y_uY_u^T" in execution else "FAIL",
            "Execution II matrices are reproducible but not no-proxy",
        ),
        Gate(
            "quark CKM angle magnitudes",
            "OPEN",
            "derive s12,s13,s23 from selected zero-mode overlaps",
        ),
        Gate(
            "quark Yukawa singular values",
            "OPEN",
            "derive Yu,Yd magnitudes from selected overlap actions and normalizations",
        ),
        Gate(
            "charged-lepton Yukawas",
            "OPEN",
            "derive Ye from the same selected geometry rather than diagonal benchmark entries",
        ),
        Gate(
            "neutrino masses",
            "OPEN",
            "derive Dirac matrix and neutral real/Majorana or Dirac mechanism",
        ),
        Gate(
            "selected overlap-kernel certificate",
            "REQUIRED",
            "matter curves, bundles, zero modes, finite channels, kinetic metrics, RG matching",
        ),
    ]

    print("No-proxy flavor mass-gap audit")
    print("==============================")
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
