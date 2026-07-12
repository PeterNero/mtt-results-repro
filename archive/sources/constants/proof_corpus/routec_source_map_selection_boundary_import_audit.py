"""Audit Route-C source-map selection boundary import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_source_map_selection_boundary_import.candidate.json"
CERT = ROOT / "certificates" / "routec_source_map_selection_boundary_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_SourceMapSelectionBoundary_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_source_map_selection_boundary.py"

STATUS = "ROUTEC_SOURCE_MAP_SELECTION_BOUNDARY_IMPORTED_DYNAMIC_APPLICATION_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


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

    summary = data["selection_boundary_summary"]
    require(summary["static_support_closed"] is True, "static support not closed")
    require(summary["dynamic_application_open"] is True, "dynamic application not marked open")
    for key in [
        "phase_R_Z_selected_now",
        "shift_R_X_selected_now",
        "b_source_emitted_now",
        "physical_projector_application_promoted_now",
    ]:
        require(summary[key] is False, f"dynamic antecedent overclaimed: {key}")
    require(summary["if_selected_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "if-selected ATA mismatch")
    require(summary["if_selected_A_transpose_b"] == [12.0, 12.0], "if-selected ATb mismatch")
    require(summary["if_selected_deltaTheta_C1"] == [1.0, 1.0], "if-selected delta mismatch")

    upstream = data["upstream_source_map_selection_boundary"]
    for key in [
        "selected_differentiated_PhiFinC1_applies_Q_residual",
        "selected_phase_R_Z_source",
        "selected_shift_R_X_source",
        "selected_Hessian_or_b_source_vector",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "selected_sector_response_matrices",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "selection_theorem_proved_now",
        "source_map_selected_by_MTT_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "honest_Galerkin_C1_value_run_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(upstream["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selection_theorem",
        "claims_source_map_selected",
        "claims_A_selected",
        "claims_b_selected",
        "claims_deltaTheta_C1",
        "claims_honest_Galerkin_C1",
        "claims_SM_parity_dynamic_packet_closure",
        "claims_full_no_knob_flavor_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("The source-map selection boundary is now sharp" in note, "note missing boundary statement")
    require("This is not source-map selection" in note, "note missing caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
