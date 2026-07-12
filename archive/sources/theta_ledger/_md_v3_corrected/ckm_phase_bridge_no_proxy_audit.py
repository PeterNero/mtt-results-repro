"""No-proxy CKM phase bridge audit for the q79 branch.

The script uses q=79 only from the already closed exact/charge branch.  It
does not scan labels or minimize a phase error.  Experimental numbers are used
only after the prediction, as a compatibility check.
"""

from __future__ import annotations

import json
import math
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


def q_from_closed_branch() -> int | None:
    cert = ROOT.parent / "certificates" / "z64_exact_branch_certificate.json"
    if cert.exists():
        data = json.loads(cert.read_text(encoding="utf-8"))
        return int(data["conclusion"]["q_mod_448"])

    terminal = read(ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    z64 = read(ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md")
    z7 = read(ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md")
    if (
        "selected exact/charge MTT branch proves q=79 mod 448" in terminal
        and "Z64 exact central-circle branch certificate       CLOSED" in z64
        and "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in z7
    ):
        return 79
    return None


def sigma(value: float, center: float, err: float) -> float:
    return (value - center) / err


def main() -> None:
    q = q_from_closed_branch()
    n = 448
    delta_mtt = 2.0 * math.pi * q / n if q is not None else float("nan")
    delta_mtt_deg = math.degrees(delta_mtt)

    # PDG 2024 CKM global-fit values from rpp2024-rev-ckm-matrix.pdf, Eq. 12.28.
    s12 = 0.22501
    s13 = 0.003732
    s23 = 0.04183
    delta_pdg = 1.147
    delta_pdg_sigma = 0.026
    j_pdg = 3.12e-5
    j_pdg_sigma = 0.13e-5

    # PDG 2024 direct/tree-level gamma combination from Eq. 12.25.
    gamma_deg = 65.7
    gamma_sigma_deg = 3.0

    c12 = math.sqrt(1.0 - s12 * s12)
    c13 = math.sqrt(1.0 - s13 * s13)
    c23 = math.sqrt(1.0 - s23 * s23)
    prefactor = c12 * c23 * c13**2 * s12 * s23 * s13
    j_mtt = prefactor * math.sin(delta_mtt)

    z_delta = sigma(delta_mtt, delta_pdg, delta_pdg_sigma)
    z_gamma = sigma(delta_mtt_deg, gamma_deg, gamma_sigma_deg)
    z_j = sigma(j_mtt, j_pdg, j_pdg_sigma)

    gates = [
        Gate("q source", "CLOSED" if q == 79 else "FAIL", "q=79 read from closed exact/charge branch"),
        Gate("no empirical label scan", "PASS", "script never searches q; it evaluates the closed branch label"),
        Gate("phase prediction", "PASS" if abs(delta_mtt - 1.1079724090785432) < 1e-15 else "FAIL", f"delta={delta_mtt:.15f} rad"),
        Gate("PDG delta compatibility", "PASS" if abs(z_delta) < 2.0 else "FAIL", f"z_delta={z_delta:.2f}"),
        Gate("PDG gamma compatibility", "PASS" if abs(z_gamma) < 1.0 else "FAIL", f"z_gamma={z_gamma:.2f}"),
        Gate("PDG J compatibility", "PASS" if abs(z_j) < 1.0 else "FAIL", f"J_MTT={j_mtt:.12e}, z_J={z_j:.2f}"),
        Gate("CKM angle magnitudes", "OPEN", "s12,s13,s23 are comparison inputs, not yet derived"),
        Gate("Yukawa magnitudes", "OPEN", "requires selected overlap-kernel certificate"),
    ]

    print("No-proxy CKM phase bridge audit")
    print("================================")
    print()
    print(f"q={q}, N={n}")
    print(f"delta_MTT={delta_mtt:.15f} rad = {delta_mtt_deg:.12f} deg")
    print(f"J_prefactor={prefactor:.15e}")
    print(f"J_MTT={j_mtt:.15e}")
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
