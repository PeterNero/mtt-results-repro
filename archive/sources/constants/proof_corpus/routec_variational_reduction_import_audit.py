"""Audit Route-C variational reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_variational_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "routec_variational_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_VariationalReduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_variational_reduction.py"

STATUS = "ROUTEC_VARIATIONAL_REDUCTION_IMPORTED_C1_DEFECT_SOURCE_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


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

    summary = data["variational_reduction_summary"]
    require(summary["finite_euler_projection_derived"] is True, "Euler projection missing")
    require(summary["orthogonal_completion_reduced_to_C1_defect_functional"] is True, "reduction missing")
    require(summary["selected_C1_defect_functional_proved"] is False, "functional overclaimed")
    require(summary["physical_PhiFinC1_application_rule_proved"] is False, "PhiFinC1 overclaimed")
    require(summary["independent_quadrature_hessian_solve_run"] is False, "quadrature overclaimed")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    upstream = data["upstream_candidate"]
    for key in [
        "finite_dimensional_variational_projection_derivation",
        "orthogonal_completion_principle_reduced_to_selected_C1_defect_functional",
        "independent_quadrature_hessian_solve_spec_ready",
        "sufficiency_of_either_route_proved",
        "observed_constants_excluded_as_selectors",
    ]:
        require(upstream["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "select_C1_defect_leakage_functional_from_MTT",
        "prove_physical_PhiFinC1_minimizes_selected_defect_functional",
        "fill_selected_zero_mode_basis_data",
        "fill_independent_primitive_quadrature_table",
        "fill_independent_hessian_source_vector",
        "run_independent_quadrature_hessian_solve",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    packets = data["upstream_packets"]
    require(packets["orthogonal_completion_variational_derivation"]["status"] == "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN", "variational status mismatch")
    require(packets["independent_quadrature_hessian_solve_spec"]["status"] == "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING", "quadrature status mismatch")
    require(packets["principle_or_solve_sufficiency_replay"]["status"] == "SUFFICIENCY_PROVED_ANTECEDENT_OPEN", "sufficiency status mismatch")
    require(packets["principle_or_solve_sufficiency_replay"]["antecedent_met_now"] is False, "antecedent overclaimed")

    for key in [
        "claims_selected_C1_defect_functional",
        "claims_physical_PhiFinC1_application_rule",
        "claims_independent_quadrature_hessian_solve",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("variational" in note and "source gap" in note, "note missing reduction summary")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
