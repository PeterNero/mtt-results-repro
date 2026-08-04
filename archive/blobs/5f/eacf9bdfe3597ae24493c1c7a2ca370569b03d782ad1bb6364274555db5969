"""Audit the Theta-selected scaffold for no-proxy flavor closure.

This audit does not claim that Yukawa magnitudes are derived.  It verifies the
closed scaffold data that any later no-proxy Yukawa certificate must use.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def load_certificate() -> dict:
    if not CERT.exists():
        return {}
    return json.loads(CERT.read_text(encoding="utf-8"))


def main() -> None:
    theta_i = read(ROOT / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md")
    theta_ii = read(ROOT / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md")
    terminal = read(ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    holonomy = read(ROOT / "Holonomy_Quotient_and_Majorana_Admissibility_for_No_Proxy_Flavor_Closure_in_MTT_v1.md")
    scaffold = read(ROOT / "Theta_Selected_Overlap_Kernel_Skeleton_for_No_Proxy_Flavor_v1.md")
    cert = load_certificate()

    r1_values = [1.0, 2.0]
    target_i2 = 0.560
    target_i3 = 0.229
    lambda_floor = 0.25
    endpoint_lens_gap = 2.0 / (0.280 * 2.0)
    endpoint_c = 1.439 * 2.0
    endpoint_nil_gap = 2.0 * math.pi + 4.0 * math.pi**2 / endpoint_c**2

    ratio_checks: list[tuple[float, float, float, float, float]] = []
    for r1 in r1_values:
        i1 = 2.0 * math.pi * r1
        lens_sq = 0.280 * r1
        i2 = 4.0 * math.pi * lens_sq
        c = 1.439 * r1
        i3 = c
        ratio_checks.append((r1, i2 / i1, i3 / i1, 2.0 / lens_sq, c))

    cert_status = cert.get("status")
    cert_scale = cert.get("scale", {}).get("mu_theta_TeV")
    cert_q = cert.get("cp_character", {}).get("q_mod_448")

    gates = [
        Gate(
            "Theta scale",
            "PASS" if r"\mu_\Theta = 5~\mathrm{TeV}" in theta_i and cert_scale == 5.0 else "FAIL",
            "mu_Theta=5 TeV fixed before flavor comparison",
        ),
        Gate(
            "Gauge overlap targets",
            "PASS" if "0.560" in theta_i and "0.229" in theta_i else "FAIL",
            "Theta I fixes I2/I1 and I3/I1 targets",
        ),
        Gate(
            "Shared circle domain",
            "PASS" if "I_1 = 2\\pi R_1" in theta_ii and "R_1\\le 2" in theta_ii else "FAIL",
            "I1=2*pi*R1 with R1<=2",
        ),
        Gate(
            "Direct lens normalization",
            "PASS" if "(f_2R_{\\mathrm{lens}})^2 = 0.280\\,R_1" in theta_ii else "FAIL",
            "I2=4*pi*(f2 R_lens)^2 implies lens_sq=0.280 R1",
        ),
        Gate(
            "Direct nil normalization",
            "PASS" if "c = 1.439\\,R_1" in theta_ii and "I_3^{(0)} = c" in theta_ii else "FAIL",
            "I3=c with c=1.439 R1",
        ),
        Gate(
            "Lens ratio arithmetic",
            "PASS" if all(abs(row[1] - target_i2) < 1e-12 for row in ratio_checks) else "FAIL",
            ", ".join(f"R1={row[0]:.0f}: I2/I1={row[1]:.6f}" for row in ratio_checks),
        ),
        Gate(
            "Nil ratio arithmetic",
            "PASS" if all(abs(row[2] - target_i3) < 5e-5 for row in ratio_checks) else "FAIL",
            ", ".join(f"R1={row[0]:.0f}: I3/I1={row[2]:.6f}" for row in ratio_checks),
        ),
        Gate(
            "Lens gap",
            "PASS" if endpoint_lens_gap > lambda_floor and "lambda_lens >= 3.571" in scaffold else "FAIL",
            f"endpoint R1=2 gives lambda_lens={endpoint_lens_gap:.6f} > {lambda_floor}",
        ),
        Gate(
            "Nil gap",
            "PASS" if endpoint_nil_gap > lambda_floor and "11.05" in theta_ii else "FAIL",
            f"endpoint c={endpoint_c:.3f} gives lambda_nil_bound={endpoint_nil_gap:.6f} > {lambda_floor}",
        ),
        Gate(
            "q79 CP character",
            "CLOSED" if "selected exact/charge MTT branch proves q=79 mod 448" in terminal and cert_q == 79 else "FAIL",
            "q=79 read from terminal exact/charge certificate",
        ),
        Gate(
            "Yukawa kernel formula",
            "DEFINED" if contains_all(holonomy, ["Y_abc(Theta)", "A_gamma", "S_gamma", "chi_gamma"]) else "FAIL",
            "generic selected channel sum is present in the no-proxy criterion",
        ),
        Gate(
            "Scaffold certificate",
            "SCAFFOLD_CLOSED" if cert_status == "SCAFFOLD_CLOSED_KERNEL_DATA_OPEN" else "FAIL",
            str(cert_status),
        ),
        Gate(
            "Zero-mode/channel data",
            "OPEN",
            "family basis, channels, actions, prefactors, and kinetic metrics remain to be computed",
        ),
        Gate(
            "No-proxy mass closure",
            "OPEN",
            "Yukawa magnitudes and CKM angle magnitudes are not yet derived",
        ),
    ]

    print("Theta-selected overlap-kernel scaffold audit")
    print("============================================")
    print()
    print(f"endpoint_lens_gap={endpoint_lens_gap:.12f}")
    print(f"endpoint_nil_gap={endpoint_nil_gap:.12f}")
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
