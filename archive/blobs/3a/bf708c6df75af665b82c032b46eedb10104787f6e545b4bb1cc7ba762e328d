"""Audit Route-C selected trace-map and basis-value import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_tracemap_basis_values_import.candidate.json"
CERT = ROOT / "certificates" / "routec_tracemap_basis_values_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_TraceMapBasisValues_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_tracemap_basis_values.py"

STATUS = "ROUTEC_TRACEMAP_BASIS_VALUES_IMPORTED_DYNAMIC_DOTD_BINDING_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


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

    summary = data["trace_basis_summary"]
    require(summary["stationary_trace_map_values_accepted"] is True, "stationary trace not accepted")
    require(summary["dynamic_C1_trace_accepted"] is False, "dynamic trace overaccepted")
    require(summary["dynamic_flags"]["selected_dotD_source_verified"] is False, "dotD oververified")
    require(summary["dynamic_flags"]["alpha1_driver_verified"] is False, "alpha1 oververified")
    require(summary["basis_row_count"] == 19, "basis row count mismatch")
    require(summary["selected_basis_row_count"] == 19, "selected basis count mismatch")
    require(summary["basis_stage_accepted"] is True, "basis stage not accepted")
    require(len(summary["basis_ids"]) == 19, "basis ids missing")
    require(summary["primitive_row_count"] == 72, "primitive count mismatch")
    require(summary["primitive_rows_executed"] is False, "primitive rows overexecuted")
    require("dynamic dotD trace binding" in " ".join(summary["primitive_blockers"]), "primitive blocker mismatch")

    for key in [
        "selected_trace_map_values_functional_stationary",
        "selected_basis_projector_gram_gap_values_stationary",
        "basis_stage_can_advance",
        "primitive_row_ids_locked",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_first_variation_identity",
        "boundary_cancellation_for_dynamic_C1_trace",
        "selected_dynamic_dotD_trace_binding",
        "primitive_quadrature_rows",
        "hessian_source_rows",
        "sector_matrix_rows",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    for key in [
        "claims_primitive_rows_executed",
        "claims_physical_first_variation_identity",
        "claims_boundary_cancellation_for_dynamic_C1_trace",
        "claims_selected_A",
        "claims_selected_b",
        "claims_selected_deltaTheta_C1",
        "claims_I10_proved",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("Accepted now" in note and "Primitive stage" in note, "note missing summary")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
