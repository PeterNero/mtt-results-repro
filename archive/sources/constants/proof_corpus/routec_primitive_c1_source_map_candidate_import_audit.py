"""Audit Route-C primitive C1 source-map candidate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_primitive_c1_source_map_candidate_import.candidate.json"
CERT = ROOT / "certificates" / "routec_primitive_c1_source_map_candidate_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_PrimitiveC1_SourceMapCandidate_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_primitive_c1_source_map_candidate.py"

STATUS = "ROUTEC_PRIMITIVE_C1_SOURCE_MAP_CANDIDATE_IMPORTED_SELECTION_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


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

    summary = data["primitive_c1_source_map_summary"]
    require(summary["strict_real_coordinates"] == 72, "strict coordinate target mismatch")
    require(summary["Q_residual_rank"] == 6, "Q_residual rank mismatch")
    require(summary["phase_residual_norm_sq"] == 4.0, "phase residual norm mismatch")
    require(summary["shift_residual_norm_sq"] == 2.0, "shift residual norm mismatch")
    require(summary["conditional_b_norm_sq"] == 24.0, "conditional b norm mismatch")
    require(summary["if_selected_rank"] == 2, "if-selected rank mismatch")
    require(summary["if_selected_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "if-selected Gram mismatch")
    require(summary["if_selected_A_transpose_b"] == [12.0, 12.0], "if-selected ATb mismatch")
    require(summary["if_selected_deltaTheta_C1"] == [1.0, 1.0], "if-selected delta mismatch")
    require(summary["source_map_selected_by_MTT_now"] is False, "source map overselected")
    require(summary["selected_A_selected_emitted"] is False, "A_selected overemitted")
    require(summary["selected_b_selected_emitted"] is False, "b_selected overemitted")
    require(
        summary["honest_galerkin_selected_source_verified"] is False,
        "honest Galerkin source oververified",
    )

    upstream = data["upstream_primitive_c1_source_map_candidate"]
    decision = upstream["promotion_decision"]
    require(decision["source_map_candidate_constructed"] is True, "source map candidate not constructed")
    for key in [
        "source_map_selected_by_MTT_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "selected_phase_R_Z_source",
        "selected_shift_R_X_source",
        "selected_Hessian_or_b_source_vector",
        "selected_primitive_C1_tensor_values",
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

    guard = data["guardrails"]
    for key in [
        "claims_source_map_selected",
        "claims_A_selected",
        "claims_b_selected",
        "claims_deltaTheta_C1",
        "claims_sector_response_matrices",
        "claims_honest_Galerkin_C1",
        "claims_SM_parity_dynamic_packet_closure",
        "claims_full_no_knob_flavor_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("The primitive C1 frontier is now explicit" in note, "note missing frontier statement")
    require("This is still a candidate" in note, "note missing candidate caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
