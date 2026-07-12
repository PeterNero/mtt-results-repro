"""Audit Route-C C1 partial-fill / basis-run import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_c1_partial_fill_basis_run_import.candidate.json"
CERT = ROOT / "certificates" / "routec_c1_partial_fill_basis_run_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_C1PartialFillBasisRun_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_c1_partial_fill_basis_run.py"

STATUS = "ROUTEC_C1_PARTIAL_FILL_BASIS_RUN_IMPORTED_TRACE_BASIS_VALUES_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


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

    summary = data["partial_fill_summary"]
    require(summary["route_A_certificate_accepted"] is False, "Route A overaccepted")
    require(summary["closed_formal_fields"] == {
        "hessian_or_coercivity": True,
        "normalization_compatibility": True,
    }, "formal field closure mismatch")
    require(summary["open_physical_fields"] == {
        "boundary_cancellation": False,
        "first_variation_identity": False,
        "selected_trace_map": False,
    }, "physical field open-state mismatch")
    require(summary["basis_row_count"] == 19, "basis row count mismatch")
    require(summary["selected_basis_row_count"] == 0, "selected row count mismatch")
    require(summary["can_advance_to_primitive_rows"] is False, "advanced to primitive too early")
    require(len(summary["basis_ids"]) == 19, "basis ids missing")
    require("selected HYM/Strominger finite trace" in summary["shared_missing_object"], "shared object mismatch")

    for key in [
        "formal_hessian_coercivity_on_residual_quotient",
        "normalization_scale_independence",
        "basis_row_stubs_emitted",
        "shared_trace_basis_cutset_identified",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_trace_map_values",
        "physical_first_variation_identity",
        "boundary_cancellation_for_selected_trace",
        "selected_basis_projector_gram_gap_values",
        "primitive_quadrature_rows",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    for key in [
        "claims_route_A_first_variation_certificate_accepted",
        "claims_route_B_basis_rows_accepted",
        "claims_route_B_can_advance_to_primitive_rows",
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

    require("Shared missing object" in note, "note missing shared object")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
