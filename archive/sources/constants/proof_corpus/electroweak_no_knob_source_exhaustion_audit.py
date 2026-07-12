"""Audit source exhaustion for no-knob electroweak closure."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Electroweak_No_Knob_Closure_Source_Exhaustion_Theorem_v1.md"
CERT = REPO / "certificates" / "electroweak_no_knob_source_exhaustion_certificate.json"
KERNEL_CERT = REPO / "certificates" / "selected_electroweak_threshold_kernel_reduction_certificate.json"
RHO_CERT = REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"

Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
THETA_I = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
THETA_II = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"
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


def low_scale_sin2(r: float, x: float, mu: float, mz: float, t1: float = 0.0, t2: float = 0.0) -> float:
    b1 = 41.0 / 10.0
    b2 = -19.0 / 6.0
    log_term = math.log(mu / mz) / (8.0 * math.pi**2)
    inv_g1 = 1.0 / (r * x) + b1 * log_term + t1
    inv_g2 = 1.0 / x + b2 * log_term + t2
    g1_sq = 1.0 / inv_g1
    g2_sq = 1.0 / inv_g2
    gp_sq = (3.0 / 5.0) * g1_sq
    return gp_sq / (gp_sq + g2_sq)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    kernel_cert = json.loads(read(KERNEL_CERT))
    rho_cert = json.loads(read(RHO_CERT))
    note = read(NOTE)
    theta_i = read(THETA_I)
    theta_ii = read(THETA_II)
    theta_iii = read(THETA_III)
    theta_v = read(THETA_V)
    execution_i = read(EXECUTION_I)
    heterotic = read(HETEROTIC)
    under = cert["underdetermination"]
    r = float(under["fixed_ratio"])
    mu = float(under["mu_Theta_GeV"])
    mz = float(under["MZ_GeV"])
    examples = [float(x) for x in under["example_x_values"]]
    angles = [low_scale_sin2(r, x, mu, mz) for x in examples]

    checks = [
        check(
            "certificate status",
            cert["status"] == "CURRENT_CORPUS_ELECTROWEAK_NO_KNOB_CLOSURE_REFUTED_REPAIR_EXACT",
            cert["status"],
        ),
        check(
            "Theta I is target extraction",
            contains_all(
                theta_i,
                [
                    "experimentally measured couplings",
                    "first-principles prediction",
                    "gauge data are used",
                ],
            ),
            "Theta I source",
        ),
        check(
            "Theta II realizes inherited targets",
            contains_all(theta_ii, ["matched exactly", "Theta$--targets extracted from Standard Model gauge couplings", "No claim"]),
            "Theta II source",
        ),
        check(
            "Theta III fixes relative overlap normalization",
            contains_all(theta_iii, ["overlap normalization", "Yukawa couplings or flavor structure", "normalization convention"]),
            "Theta III source",
        ),
        check(
            "Theta V remains conditional",
            contains_all(theta_v, ["G_F", "m_W", "\\Delta r_{\\mathrm{eff}}", "requires computing"]),
            "Theta V source",
        ),
        check(
            "Execution I uses calibrated K",
            contains_all(execution_i, ["calibrated common scale", "K =", "Choosing the standard normalization"]),
            "Execution I source",
        ),
        check(
            "heterotic thresholds not computed",
            contains_all(heterotic, ["g^{-2}=\\mathrm{Re}\\,S", "one-loop thresholds", "do not attempt to compute"]),
            "heterotic source",
        ),
        check(
            "rho internal branch remains closed",
            rho_cert["status"] == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED"
            and abs(rho_cert["selected_values"]["rho_UV"] - 0.164530397543639) < 1e-15,
            rho_cert["selected_values"],
        ),
        check(
            "kernel reduction already names missing object",
            kernel_cert["verdict"]["exact_missing_object"]
            == "K_EW(selected MTT branch) -> (mu_Theta, x, T1, T2, scheme)",
            kernel_cert["verdict"],
        ),
        check(
            "same ratio not unique",
            max(angles) - min(angles) > 0.002,
            [f"{angle:.12f}" for angle in angles],
        ),
        check(
            "note closes negatively",
            contains_all(note, ["current electroweak branch is closed negatively", "exactly K_EW"]),
            "negative closure verdict",
        ),
        check(
            "verdict is exact repair",
            cert["verdict"]["current_gate_closed_negatively"] is True
            and cert["verdict"]["full_electroweak_no_knob_closure_proved"] is False
            and cert["verdict"]["exact_repair_object"] == "Selected_Electroweak_Threshold_Kernel_Theorem_v1",
            cert["verdict"],
        ),
    ]

    print("\nElectroweak no-knob source exhaustion audit")
    print("===========================================")
    print(f"angles_from_same_ratio={angles}")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
