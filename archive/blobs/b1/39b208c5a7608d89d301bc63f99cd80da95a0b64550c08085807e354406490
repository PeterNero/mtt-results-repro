"""Audit the H radial norm-law / value-source derivation attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrgradialnormlaw_or_value_source_derivation"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def near(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    norm_law = read_json(f"candidate_data/{SLUG}/h_radial_norm_law.packet.json")
    route = read_json(f"candidate_data/{SLUG}/h_radial_value_source_route_audit.packet.json")
    scan = read_json(f"candidate_data/{SLUG}/h_radial_source_only_finite_invariant_scan.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["radial_norm_law_promoted"] is True, "radial norm law must be promoted")
    require(candidate["decision"]["numeric_radial_value_promoted"] is False, "numeric radial value must remain open")
    require(candidate["decision"]["strict_r_H_promoted"] is False, "strict r_H must remain open")
    require(candidate["decision"]["strict_Herm2_rows_promoted"] is False, "strict Herm2 rows must remain open")
    require(
        candidate["decision"]["frontier_reduced_to_numeric_radial_value_source"] is True,
        "frontier reduction mismatch",
    )
    require(candidate["next_target"] == "MTT_Selected_HRadialActionNormValue_or_HLambdaThresholdRow_v1", "next target")

    require(norm_law["decision"]["radial_norm_law_promoted"] is True, "norm law packet decision mismatch")
    require(norm_law["decision"]["numeric_radial_value_promoted"] is False, "norm law overpromoted value")
    require(norm_law["inputs_now_selected"]["phi_sign_promoted"] is True, "phase sign should be selected")
    checks = norm_law["derived_tracefree_unit_generator"]["normalization_checks"]
    require(near(checks["trace"], 0.0), "unit trace mismatch")
    require(near(checks["determinant"], -1.0), "unit determinant mismatch")
    require(checks["eigenvalues"] == [-1.0, 1.0], "unit eigenvalues mismatch")
    require(near(checks["frobenius_norm_squared"], 2.0), "unit Frobenius norm mismatch")
    require("sqrt(Tr(H_tf^2)/2)" in checks["radial_norm_identity"], "radial identity missing")

    require(route["decision"]["accepted_numeric_radial_value_sources"] == 0, "accepted route count must be zero")
    require(route["decision"]["numeric_radial_value_promoted"] is False, "route overpromoted value")
    require(route["routes"]["typed_HRG_value_map"]["accepted"] is False, "typed HRG route accepted unexpectedly")
    require(route["routes"]["typed_HRG_value_map"]["accepted_strict_source_count"] == 0, "typed HRG count")
    require(route["routes"]["H_lambda_K_threshold_row"]["accepted"] is False, "H lambda route accepted unexpectedly")
    require(route["routes"]["H_lambda_K_threshold_row"]["selected_K_threshold_row_count_present"] == 9, "K count")
    require(route["routes"]["H_lambda_K_threshold_row"]["selected_K_threshold_row_count_required"] == 10, "K required")
    require(route["routes"]["H_lambda_K_threshold_row"]["selected_H_lambda_payload_emitted"] is False, "H lambda emitted")
    require(route["routes"]["determinant_RG_radial_operator"]["accepted"] is False, "det/RG route accepted")
    require(route["routes"]["determinant_RG_radial_operator"]["operator_contract_defined"] is True, "operator contract")
    require(route["routes"]["determinant_RG_radial_operator"]["operator_value_emitted"] is False, "operator value emitted")
    require(
        route["underdetermination_guard"]["radial_positive_rescaling_modulus_survives_current_selected_constraints"]
        is True,
        "radial rescaling guard missing",
    )

    require(scan["accepted_as_source_identity_count"] == 0, "scan accepted identities")
    require(scan["decision"]["near_misses_promoted"] is False, "near miss promoted")
    require(scan["decision"]["exact_source_identity_found"] is False, "exact identity found unexpectedly")
    require(scan["best_candidates"][0]["accepted_as_source_identity"] is False, "best scan row promoted")

    require(cert["checks"]["radial_norm_law_promoted"] is True, "cert norm law")
    require(cert["checks"]["numeric_radial_value_promoted"] is False, "cert numeric value")
    require(cert["checks"]["frontier_reduced_to_numeric_radial_value_source"] is True, "cert frontier")

    print("selected_hrgradialnormlaw_or_value_source_derivation audit: PASS")


if __name__ == "__main__":
    main()
