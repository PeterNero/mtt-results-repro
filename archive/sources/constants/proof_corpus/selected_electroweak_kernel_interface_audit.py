"""Audit the selected electroweak kernel interface theorem."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Kernel_Interface_Theorem_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_kernel_interface_certificate.json"
SOURCE_EXHAUSTION_CERT = REPO / "certificates" / "electroweak_no_knob_source_exhaustion_certificate.json"
RHO_CERT = REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"

Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
ROADMAP = Q79 / "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v2.md"
THETA_III = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md"
THETA_V = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md"
EXECUTION_I = Q79 / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
HETEROTIC = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def weak_angle_from_inverse_entries(G1: float, G2: float) -> float:
    gp_sq = (3.0 / 5.0) / G1
    g2_sq = 1.0 / G2
    return gp_sq / (gp_sq + g2_sq)


def run_inverse(G: float, b: float, mu: float, mz: float) -> float:
    return G + b / (8.0 * math.pi**2) * math.log(mu / mz)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    exhaustion = json.loads(read(SOURCE_EXHAUSTION_CERT))
    rho = json.loads(read(RHO_CERT))
    note = read(NOTE)
    roadmap = read(ROADMAP)
    theta_iii = read(THETA_III)
    theta_v = read(THETA_V)
    execution_i = read(EXECUTION_I)
    heterotic = read(HETEROTIC)

    # Diagnostic only: with zeta_2=1, zeta_1=1/r12 and no thresholds, different
    # kappa values still give different low-scale weak angles.
    r12 = 0.56027
    zeta1 = 1.0 / r12
    zeta2 = 1.0
    mu = 5000.0
    mz = 91.1876
    kappas = [2.2, 2.514, 3.0]
    angles = []
    for kappa in kappas:
        G1 = run_inverse(kappa * zeta1, 41.0 / 10.0, mu, mz)
        G2 = run_inverse(kappa * zeta2, -19.0 / 6.0, mu, mz)
        angles.append(weak_angle_from_inverse_entries(G1, G2))

    checks = [
        check(
            "certificate status",
            cert["status"] == "ELECTROWEAK_KERNEL_INTERFACE_BUILT_NUMERIC_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "kernel formula recorded",
            "G_a(MZ)=kappa_EW*zeta_a+Delta_a^sel+b_a/(8*pi^2)*log(mu_Theta/MZ)"
            == cert["kernel"]["prediction_map"],
            cert["kernel"],
        ),
        check(
            "Theta ratio source supports zeta ratios",
            contains_all(theta_v, ["g_1^2(\\mu_\\Theta)", "I_2(\\Theta)", "I_1(\\Theta)"])
            and cert["source_supported"]["zeta_ratios"] is True,
            "Theta V",
        ),
        check(
            "Theta III supports relative normalization",
            contains_all(theta_iii, ["overlap normalization", "twistor--action", "normalization convention"])
            and cert["source_supported"]["relative_overlap_normalization"] is True,
            "Theta III",
        ),
        check(
            "roadmap supports K slot but ratio caveat",
            contains_all(roadmap, ["K", "zeta_r", "only ratios"])
            and cert["not_source_selected_yet"]["kappa_EW"] is True,
            "roadmap K caveat",
        ),
        check(
            "Execution I supports threshold slot not no-knob value",
            contains_all(execution_i, ["threshold", "calibrated common scale", "K ="])
            and cert["not_source_selected_yet"]["Delta_sel"] is True,
            "Execution I",
        ),
        check(
            "heterotic supports gauge kinetic threshold home",
            contains_all(heterotic, ["g^{-2}=\\mathrm{Re}\\,S", "threshold corrections"])
            and cert["source_supported"]["tree_gauge_kinetic_slot"] is True,
            "heterotic",
        ),
        check(
            "rho_UV available but unmapped",
            abs(rho["selected_values"]["rho_UV"] - 0.164530397543639) < 1e-15
            and cert["not_source_selected_yet"]["rho_UV_to_EW_map"] is True,
            rho["selected_values"],
        ),
        check(
            "kernel does not claim numeric closure",
            cert["verdict"]["kernel_interface_built"] is True
            and cert["verdict"]["numeric_electroweak_closure"] is False
            and exhaustion["verdict"]["full_electroweak_no_knob_closure_proved"] is False,
            cert["verdict"],
        ),
        check(
            "kappa diagnostic nonunique",
            max(angles) - min(angles) > 0.002,
            [f"{angle:.12f}" for angle in angles],
        ),
        check(
            "note names repair paths",
            contains_all(note, ["Path A", "Path B", "Path C", "compute selected (kappa_EW, Delta^sel, mu_Theta)"]),
            "repair paths",
        ),
    ]

    print("\nSelected electroweak kernel interface audit")
    print("===========================================")
    print(f"angles_from_kappa_variation={angles}")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
