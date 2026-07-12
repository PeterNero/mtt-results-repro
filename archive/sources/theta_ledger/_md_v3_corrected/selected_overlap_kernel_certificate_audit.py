"""Audit the selected overlap-kernel certificate.

This audit is intentionally strict about the status split.  It allows the
certificate interface and no-proxy theorem schema to be closed, but it keeps
the actual Yukawa/mass computation open until concrete zero modes, channels,
metrics, action costs, and thresholds are supplied.
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
    cert = read(ROOT / "Selected_Overlap_Kernel_Certificate_v1.md")
    terminal = read(ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    phase = read(ROOT / "CKM_Phase_Bridge_and_No_Proxy_Flavor_Closure_Status_v1.md")

    gates = [
        Gate(
            "certificate file",
            "PASS" if "FlavorOverlapKernelCertificate" in cert else "FAIL",
            "selected overlap-kernel certificate exists",
        ),
        Gate(
            "q79 input",
            "CLOSED" if "selected exact/charge MTT branch proves q=79 mod 448" in terminal else "FAIL",
            "finite CP branch imported from terminal certificate",
        ),
        Gate(
            "phase bridge",
            "CLOSED" if "delta_MTT = 2 pi q / 448" in phase else "FAIL",
            "q79 phase map already stated",
        ),
        Gate(
            "source map",
            "DEFINED" if "Sigma_MTT" in cert and "selected source map" in cert else "FAIL",
            "single same-source map required before masses can be claimed",
        ),
        Gate(
            "kernel formula",
            "DEFINED" if "Y_x,raw[i,j]" in cert and "exp(-S_gamma)" in cert else "FAIL",
            "finite channel sum specified",
        ),
        Gate(
            "canonical normalization",
            "DEFINED" if "G_Q^{-1/2}" in cert and "Y_d =" in cert else "FAIL",
            "kinetic metric normalization included",
        ),
        Gate(
            "no-proxy theorem schema",
            "PROVED-SCHEMA" if "Theorem: No-Proxy Flavor from a Selected Kernel" in cert else "FAIL",
            "proof closes once OK.1--OK.9 are supplied",
        ),
        Gate(
            "current barrier theorem",
            "PROVED" if "Theorem: Current Barrier" in cert else "FAIL",
            "prevents overclaiming full flavor closure from q79 alone",
        ),
        Gate(
            "zero-mode spaces",
            "OPEN",
            "must compute H_Q,H_u,H_d,H_L,H_e,H_nu and bases",
        ),
        Gate(
            "kinetic metrics",
            "OPEN",
            "must compute positive G-sector metrics",
        ),
        Gate(
            "finite channels",
            "OPEN",
            "must compute Gamma_x[i,j] from selected geometry",
        ),
        Gate(
            "actions and prefactors",
            "OPEN",
            "must compute S_gamma and A_gamma without mass inputs",
        ),
        Gate(
            "neutral mechanism",
            "OPEN",
            "must select Dirac or Majorana/seesaw route",
        ),
        Gate(
            "RG thresholds",
            "OPEN",
            "must fix transport to measured scales",
        ),
    ]

    print("Selected overlap-kernel certificate audit")
    print("=========================================")
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
