"""Audit the selected C1-to-electroweak coefficient bridge attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_C1_Coefficient_Bridge_Attempt_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_c1_coefficient_bridge_attempt_certificate.json"
RHO_CERT = REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
LOCAL_CERT = REPO / "certificates" / "selected_electroweak_local_projection_gate_certificate.json"
Q79_C1_SUPPORT = Q79 / "certificates" / "c1_iwasawa_rplus_support_certificate.json"
Q79_C1_RESPONSE = Q79 / "certificates" / "selected_c1_response_extraction_attempt_certificate.json"
Q79_C1_FINITE = Q79 / "certificates" / "c1_finite_response_matrix_reduction_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def delta_g_12(v1: float, m1: float, m2: float) -> float:
    return v1 * (2.0 * m1 - m2) / (4.0 * math.pi)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    rho = load_json(RHO_CERT)
    local = load_json(LOCAL_CERT)
    c1_support = load_json(Q79_C1_SUPPORT)
    c1_response = load_json(Q79_C1_RESPONSE)
    c1_finite = load_json(Q79_C1_FINITE)
    note = read(NOTE)

    selected = cert["selected_values"]
    v1 = float(selected["v1_tilde"])
    diagnostic = cert["execution_i_diagnostic_response"]
    c1 = float(diagnostic["c1"])
    c2 = float(diagnostic["c2"])
    m1_required = c1 / v1
    m2_required = c2 / v1
    lambda_required = 2.0 * m1_required - m2_required
    diagnostic_delta_g = delta_g_12(v1, m1_required, m2_required)

    witness_checks = []
    for item in cert["underdetermination_witness"]["maps"]:
        m1, m2 = [float(x) for x in item["m"]]
        witness_checks.append(approx(delta_g_12(v1, m1, m2), float(item["Delta_G_12"])))

    checks = [
        check(
            "certificate status",
            cert["status"] == "C1_ELECTROWEAK_COEFFICIENT_BRIDGE_REDUCED_RESPONSE_MAP_OPEN",
            cert["status"],
        ),
        check(
            "rho branch supplies v1_tilde",
            approx(v1, float(rho["selected_values"]["v1_tilde"]))
            and approx(float(selected["rho_UV"]), float(rho["selected_values"]["rho_UV"]))
            and approx(v1 * v1, float(selected["rho_UV"])),
            selected,
        ),
        check(
            "C1 alpha1 support closed",
            c1_support["status"] == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
            and c1_support["rplus_support"]["alpha_2_component"] == 0
            and c1_support["rplus_support"]["alpha_3_component"] == 0,
            c1_support["rplus_support"],
        ),
        check(
            "local projection imported",
            local["status"] == "ELECTROWEAK_LOCAL_PROJECTION_FORMULA_CLOSED_COEFFICIENTS_OPEN"
            and local["verdict"]["projection_algebra_closed"] is True,
            local["status"],
        ),
        check(
            "diagnostic response ratios",
            approx(m1_required, float(diagnostic["m1_required"]))
            and approx(m2_required, float(diagnostic["m2_required"]))
            and approx(lambda_required, float(diagnostic["lambda_12_required"])),
            [m1_required, m2_required, lambda_required],
        ),
        check(
            "diagnostic Delta_G",
            approx(diagnostic_delta_g, float(diagnostic["Delta_G_12"])),
            diagnostic_delta_g,
        ),
        check("underdetermination witness maps recompute", all(witness_checks), witness_checks),
        check(
            "C1 response data still absent",
            c1_response["attempt_result"]["M_C1_alpha1_entries_computed"] is False
            and c1_response["attempt_result"]["safe_to_use_C1_as_numeric_no_proxy_weight"] is False
            and c1_finite["verdict"]["closes_numeric_C1_response_matrices"] is False,
            c1_response["attempt_result"],
        ),
        check(
            "note states response map gate",
            "compute P_EW(alpha_1) = (m1,m2)" in note
            and "C1_ELECTROWEAK_COEFFICIENT_BRIDGE_REDUCED_RESPONSE_MAP_OPEN" in note,
            "response map gate",
        ),
        check(
            "numeric electroweak closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
    ]

    print("\nSelected electroweak C1 coefficient bridge attempt audit")
    print("=========================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

