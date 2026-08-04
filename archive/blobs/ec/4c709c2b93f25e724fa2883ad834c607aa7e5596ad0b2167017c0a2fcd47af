"""Audit Route-C Strominger trace C1 execution-plan import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_strominger_execution_plan_import.candidate.json"
CERT = ROOT / "certificates" / "routec_strominger_execution_plan_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_StromingerExecutionPlan_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_strominger_execution_plan.py"

STATUS = "ROUTEC_STROMINGER_EXECUTION_PLAN_IMPORTED_C1_FILL_OR_QUADRATURE_ROWS_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    plan = data["execution_plan"]
    require(plan["route_A_verified_now"] is False, "Route A oververified")
    require(plan["route_A_required_first_variation_fields"] == [
        "selected_trace_map",
        "first_variation_identity",
        "hessian_or_coercivity",
        "boundary_cancellation",
        "normalization_compatibility",
    ], "Route A field list mismatch")
    require(plan["route_B_expected_row_counts"] == {
        "zero_mode_basis_rows": 19,
        "primitive_contraction_rows": 72,
        "hessian_source_rows": 2,
        "sector_matrix_rows": 36,
    }, "Route B row counts mismatch")
    require(plan["route_B_accepted_now"] is False, "Route B overaccepted")
    require(plan["row_execution_order"] == [
        "basis",
        "primitive_contractions",
        "hessian_source",
        "sector_matrices",
    ], "execution order mismatch")
    require(plan["next_executable_stage"] == "basis", "next executable stage mismatch")
    require(plan["locked_target"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(plan["locked_target"]["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(plan["locked_target"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    for key in [
        "selected_trace_map_values",
        "first_variation_identity_verified",
        "hessian_or_coercivity_verified",
        "boundary_cancellation_verified",
        "quadrature_rows_executed",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    for key in [
        "claims_route_A_first_variation_certificate_accepted",
        "claims_route_B_quadrature_execution_accepted",
        "claims_I10_proved",
        "claims_selected_A",
        "claims_selected_b",
        "claims_selected_deltaTheta_C1",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("now executable, but not closed" in note, "note missing open status")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
