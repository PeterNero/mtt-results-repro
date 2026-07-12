"""Audit Route-C I10 fill cutset import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_i10_fill_cutset_import.candidate.json"
CERT = ROOT / "certificates" / "routec_i10_fill_cutset_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_I10FillCutset_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_i10_fill_cutset.py"

STATUS = "ROUTEC_I10_FILL_CUTSET_IMPORTED_STROMINGER_TRACE_OR_QUADRATURE_PLAN_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


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

    summary = data["i10_fill_cutset_summary"]
    require(summary["route_A_accepted"] is False, "Route A overaccepted")
    require(summary["route_B_accepted"] is False, "Route B overaccepted")
    require(summary["route_A_minimal_cutset"] == [
        "selected_minimizer_trace_payload_verified",
        "selected_c1_response_payload_verified",
        "defect_functional_minimizer_payload_verified",
    ], "Route A cutset mismatch")
    require(summary["route_B_minimal_cutset"] == [
        "zero_mode_basis_rows",
        "primitive_contraction_rows",
        "hessian_source_rows",
        "sector_matrix_rows",
    ], "Route B cutset mismatch")
    require(all(value == 0 for value in summary["route_B_table_counts"].values()), "Route B rows unexpectedly filled")
    require(summary["no_observed_data_as_selector"] is True, "observed-data guardrail missing")
    require(summary["no_patched_replay_copying"] is True, "patched-copy guardrail missing")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    upstream = data["upstream_candidate"]
    for key in [
        "selected_minimizer_trace_payload_verified",
        "selected_c1_response_payload_verified",
        "defect_functional_minimizer_payload_verified",
        "independent_quadrature_values_filled",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    for key in [
        "claims_route_A_accepted",
        "claims_route_B_accepted",
        "claims_I10_proved",
        "claims_unpatched_A_selected",
        "claims_unpatched_b_selected",
        "claims_unpatched_deltaTheta_C1",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("Neither route is accepted yet" in note, "note missing non-acceptance")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
