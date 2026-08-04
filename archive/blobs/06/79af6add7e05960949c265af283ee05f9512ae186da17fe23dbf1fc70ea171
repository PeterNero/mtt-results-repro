"""Audit the selected electroweak kernel candidate threshold computation."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Kernel_Candidate_Computation_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_kernel_candidate_computation_certificate.json"
INTERFACE_CERT = REPO / "certificates" / "selected_electroweak_kernel_interface_certificate.json"
EXEC_THRESHOLD_CERT = REPO / "certificates" / "execution_i_threshold_profile_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def vector_approx(left: list[float], right: list[float], tol: float = 1e-12) -> bool:
    return len(left) == len(right) and all(approx(a, b, tol) for a, b in zip(left, right))


def threshold_direction(tau: list[float]) -> list[float]:
    logs = [math.log(x) for x in tau]
    mean = sum(logs) / len(logs)
    return [x - mean for x in logs]


def weak_angle(kappa: float, r12: float, mu: float, mz: float, T1: float = 0.0, T2: float = 0.0) -> float:
    zeta1 = 1.0 / r12
    zeta2 = 1.0
    b1 = 41.0 / 10.0
    b2 = -19.0 / 6.0
    run = math.log(mu / mz) / (8.0 * math.pi**2)
    G1 = kappa * zeta1 + T1 + b1 * run
    G2 = kappa * zeta2 + T2 + b2 * run
    gp_sq = (3.0 / 5.0) / G1
    g2_sq = 1.0 / G2
    return gp_sq / (gp_sq + g2_sq)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    interface = json.loads(read(INTERFACE_CERT))
    threshold_cert = json.loads(read(EXEC_THRESHOLD_CERT))
    note = read(NOTE)
    inputs = cert["inputs"]
    computed = cert["computed"]

    tau = [float(x) for x in inputs["tau"]]
    direction = threshold_direction(tau)
    bulk_alpha = [inputs["bulk_coefficient_delta"] * x for x in direction]
    exc_alpha = [float(x) for x in inputs["exceptional_alpha_inverse"]]
    candidate_alpha = [bulk_alpha[i] + exc_alpha[i] for i in range(3)]
    candidate_G = [x / (4.0 * math.pi) for x in candidate_alpha]
    exc_G = [x / (4.0 * math.pi) for x in exc_alpha]

    sin2 = {
        "no_threshold": weak_angle(
            inputs["diagnostic_kappa_EW"], inputs["theta_ratio_r12"], inputs["mu_Theta_GeV"], inputs["MZ_GeV"]
        ),
        "bulk_only": weak_angle(
            inputs["diagnostic_kappa_EW"],
            inputs["theta_ratio_r12"],
            inputs["mu_Theta_GeV"],
            inputs["MZ_GeV"],
            bulk_alpha[0] / (4.0 * math.pi),
            bulk_alpha[1] / (4.0 * math.pi),
        ),
        "exceptional_only": weak_angle(
            inputs["diagnostic_kappa_EW"],
            inputs["theta_ratio_r12"],
            inputs["mu_Theta_GeV"],
            inputs["MZ_GeV"],
            exc_G[0],
            exc_G[1],
        ),
        "bulk_plus_exceptional": weak_angle(
            inputs["diagnostic_kappa_EW"],
            inputs["theta_ratio_r12"],
            inputs["mu_Theta_GeV"],
            inputs["MZ_GeV"],
            candidate_G[0],
            candidate_G[1],
        ),
    }

    checks = [
        check(
            "certificate status",
            cert["status"] == "ELECTROWEAK_THRESHOLD_CANDIDATE_COMPUTED_DIRECT_IMPORT_REJECTED",
            cert["status"],
        ),
        check("bulk direction", vector_approx(direction, computed["bulk_direction"]), direction),
        check("bulk alpha", vector_approx(bulk_alpha, computed["bulk_alpha_inverse"]), bulk_alpha),
        check("candidate alpha", vector_approx(candidate_alpha, computed["candidate_alpha_inverse"]), candidate_alpha),
        check("candidate G", vector_approx(candidate_G, computed["candidate_G_inverse"]), candidate_G),
        check(
            "exceptional split",
            approx(exc_G[0] - exc_G[1], computed["exceptional_G_split_12"]),
            exc_G[0] - exc_G[1],
        ),
        check(
            "diagnostic weak angles",
            all(approx(sin2[key], computed["sin2_diagnostic"][key]) for key in sin2),
            sin2,
        ),
        check(
            "interface remains open",
            interface["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        ),
        check(
            "source threshold is structural not no-knob",
            threshold_cert["verdict"]["new_no_knob_prediction_certified"] is False
            and cert["classification"]["direct_import_as_electroweak_prediction"] is False,
            threshold_cert["verdict"],
        ),
        check(
            "note states direct import rejection",
            "The direct full import is therefore not viable as an electroweak prediction." in note
            and "exceptional/local electroweak threshold coefficients" in note,
            "rejection and next computation",
        ),
    ]

    print("\nSelected electroweak kernel candidate computation audit")
    print("======================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
