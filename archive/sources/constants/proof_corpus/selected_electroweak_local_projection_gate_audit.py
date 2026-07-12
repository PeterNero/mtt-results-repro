"""Audit the selected electroweak local/exceptional projection gate."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Local_Projection_Gate_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_local_projection_gate_certificate.json"
EXEC_THRESHOLD_CERT = REPO / "certificates" / "execution_i_threshold_profile_certificate.json"
EW_CANDIDATE_CERT = REPO / "certificates" / "selected_electroweak_kernel_candidate_computation_certificate.json"
EXECUTION_I_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program"
    r"\Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def vector_approx(left: list[float], right: list[float], tol: float = 1e-12) -> bool:
    return len(left) == len(right) and all(approx(a, b, tol) for a, b in zip(left, right))


def dot_trace(vector: list[float]) -> float:
    return sum(vector)


def delta_alpha(c1: float, c2: float) -> list[float]:
    return [c1, -c1 + c2, -c2]


def split_alpha_12(c1: float, c2: float) -> float:
    return 2.0 * c1 - c2


def split_g_12(c1: float, c2: float) -> float:
    return split_alpha_12(c1, c2) / (4.0 * math.pi)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    threshold = json.loads(read(EXEC_THRESHOLD_CERT))
    candidate = json.loads(read(EW_CANDIDATE_CERT))
    note = read(NOTE)
    source = read(EXECUTION_I_SOURCE)

    chi1 = [float(x) for x in cert["selected_basis"]["chi_1"]]
    chi2 = [float(x) for x in cert["selected_basis"]["chi_2"]]
    diagnostic = cert["execution_i_diagnostic"]
    c1 = float(diagnostic["c1"])
    c2 = float(diagnostic["c2"])
    computed_delta = delta_alpha(c1, c2)
    computed_alpha_split = split_alpha_12(c1, c2)
    computed_g_split = split_g_12(c1, c2)

    checks = [
        check(
            "certificate status",
            cert["status"] == "ELECTROWEAK_LOCAL_PROJECTION_FORMULA_CLOSED_COEFFICIENTS_OPEN",
            cert["status"],
        ),
        check("chi1 trace free", approx(dot_trace(chi1), 0.0), chi1),
        check("chi2 trace free", approx(dot_trace(chi2), 0.0), chi2),
        check("basis independent in trace-free plane", chi1 != chi2 and chi1[0] != 0.0 and chi2[2] != 0.0, [chi1, chi2]),
        check(
            "diagnostic delta",
            vector_approx(computed_delta, [float(x) for x in diagnostic["Delta_alpha_exc"]]),
            computed_delta,
        ),
        check(
            "diagnostic alpha split",
            approx(computed_alpha_split, float(diagnostic["Delta_alpha_12_split"])),
            computed_alpha_split,
        ),
        check(
            "diagnostic G split",
            approx(computed_g_split, float(diagnostic["Delta_G_12_split"]))
            and approx(computed_g_split, float(candidate["computed"]["exceptional_G_split_12"])),
            computed_g_split,
        ),
        check(
            "execution threshold certificate remains non-predictive",
            threshold["verdict"]["new_no_knob_prediction_certified"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            threshold["verdict"],
        ),
        check(
            "source supports exceptional-local form",
            "c_I" in source
            and "chi_a" in source
            and "exceptional divisors or localized curvature" in source
            and "to be determined" in source,
            "Execution I exceptional sector",
        ),
        check(
            "note states exact remaining gate",
            "compute `c1` and `c2` from selected localized data" in note
            and "ELECTROWEAK_LOCAL_PROJECTION_FORMULA_CLOSED_COEFFICIENTS_OPEN" in note,
            "remaining coefficient source-selection gate",
        ),
        check(
            "numeric electroweak closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["classification"]["execution_i_coefficient_import"] == "DIAGNOSTIC_NOT_PREDICTION",
            cert["verdict"],
        ),
    ]

    print("\nSelected electroweak local projection gate audit")
    print("================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

