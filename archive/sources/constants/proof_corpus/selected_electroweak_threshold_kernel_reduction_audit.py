"""Audit the selected electroweak threshold-kernel reduction."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Threshold_Kernel_Reduction_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_threshold_kernel_reduction_certificate.json"
BRIDGE_CERT = REPO / "certificates" / "electroweak_no_knob_bridge_audit_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def high_scale_sin2(r12: float) -> float:
    return (3.0 * r12) / (3.0 * r12 + 5.0)


def low_scale_sin2(r12: float, x: float, mu: float, mz: float, t1: float, t2: float) -> float:
    b1 = 41.0 / 10.0
    b2 = -19.0 / 6.0
    log_term = math.log(mu / mz) / (8.0 * math.pi**2)
    inv_g1 = 1.0 / (r12 * x) + b1 * log_term + t1
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
    bridge = json.loads(read(BRIDGE_CERT))
    note = read(NOTE)
    r12 = float(cert["theta_ratio"]["source_value"])
    expected = float(cert["numeric_diagnostic"]["high_scale_tree_sin2_from_r12"])

    sample_x = 0.63093**2
    sample_mu = 5000.0
    sample_mz = 91.1876
    tree_low = low_scale_sin2(r12, sample_x, sample_mu, sample_mz, 0.0, 0.0)
    shifted_low = low_scale_sin2(r12, sample_x, sample_mu, sample_mz, 0.02, -0.01)

    checks = [
        check(
            "certificate status",
            cert["status"] == "ELECTROWEAK_KERNEL_REDUCED_TO_NORMALIZATION_AND_THRESHOLD_VECTOR",
            cert["status"],
        ),
        check("high-scale diagnostic", approx(high_scale_sin2(r12), expected), high_scale_sin2(r12)),
        check(
            "low scale depends on normalization",
            abs(low_scale_sin2(r12, sample_x * 0.95, sample_mu, sample_mz, 0.0, 0.0) - tree_low) > 1e-4,
            tree_low,
        ),
        check(
            "low scale depends on thresholds",
            abs(shifted_low - tree_low) > 1e-4,
            {"tree": tree_low, "shifted": shifted_low},
        ),
        check(
            "note states missing kernel",
            "K_EW(selected MTT branch)" in note
            and "electroweak inverse-coupling corrections" in note,
            "K_EW reduction",
        ),
        check(
            "rho_UV direct threshold identification remains forbidden",
            cert["rho_uv_status"]["direct_identification_with_threshold"] is False
            and bridge["verdict"]["rho_uv_bridge_to_electroweak_closed"] is False,
            cert["rho_uv_status"],
        ),
        check(
            "next artifact named",
            cert["verdict"]["next_required_artifact"]
            == "Selected_Electroweak_Threshold_Kernel_Theorem_v1",
            cert["verdict"],
        ),
    ]

    print("\nSelected electroweak threshold-kernel reduction audit")
    print("====================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
