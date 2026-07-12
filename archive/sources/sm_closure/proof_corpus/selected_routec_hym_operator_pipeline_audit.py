"""Audit the selected Route-C/HYM operator pipeline gate artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_routec_hym_operator_pipeline_certificate.json"
DATA = REPO / "candidate_data" / "selected_routec_hym_operator_pipeline.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_HYM_Operator_Pipeline_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_routec_hym_operator_pipeline.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    superset = data["superset_mode"]
    gates = data["gate_results"]
    pipeline = data["pipeline_evaluation"]
    imported = data["imported_results"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_ROUTEC_HYM_OPERATOR_PIPELINE_BUILT_SELECTED_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("superset classification", cert["superset_mode"] == "SUPERSET_REPAIR_WITH_EXECUTABLE_PIPELINE" and superset["classification"] == "SUPERSET_REPAIR_WITH_EXECUTABLE_PIPELINE", superset),
        check("straight path rejected", superset["straight_path"]["succeeds"] is False and gates["honest_operator_pipeline_pass"] is False, superset["straight_path"]),
        check("visible gate imported", imported["visible_gate"]["next_required_artifact"] == "MTT_Selected_RouteC_HYM_Operator_Pipeline_v1", imported["visible_gate"]),
        check("scaffold built", gates["route_c_scaffold_built"] is True and imported["route_c_scaffold"]["status"] == "IWASAWA_ROUTE_C_FINITE_SOLVE_SCAFFOLD_FORMULATED_SELECTED_VALUES_OPEN", imported["route_c_scaffold"]),
        check("smoke executed", gates["branch_aware_smoke_executed"] is True and imported["route_c_smoke"]["status"] == "BRANCH_AWARE_SMALL_N_SMOKE_ALGEBRA_PASSES_SELECTION_OPEN", imported["route_c_smoke"]["status"]),
        check("honest mesh metric sector passes", gates["honest_mesh_metric_sector_pass"] is True and pipeline["honest_mesh_metric_sector_pass"] is True, pipeline),
        check("lifted flags pass", gates["lifted_selected_flags_pipeline_pass"] is True and pipeline["lifted_flags_operator_pipeline_pass"] is True, pipeline),
        check("honest selected pipeline fails", gates["honest_operator_pipeline_pass"] is False and pipeline["honest_operator_pipeline_pass"] is False, pipeline),
        check("selected HYM still false", gates["selected_hym_operator_source_verified"] is False and imported["hym_attempt"]["calculation_results"]["selected_hym_operator_source_verified"] is False, imported["hym_attempt"]),
        check("selected source still false", gates["selected_source_verified"] is False and imported["promotion_attempt"]["selected_source_verified"] is False, imported["promotion_attempt"]),
        check("actual values not supplied", gates["actual_selected_route_c_values_supplied"] is False and cert["what_remains_open"]["actual_selected_RouteC_HYM_values"] is True, cert),
        check("DE/dotD still open", gates["actual_selected_D_E_dotD_Riesz_Green_supplied"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("C1 still open", gates["primitive_C1_contractions_supplied"] is False and cert["what_remains_open"]["primitive_C1_overlap_tensors"] is True, cert),
        check("Qa/SU3 still open", gates["selected_Qa_SU3_packet_closed"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and superset["diagnostic_backfit_only"]["used"] is False, superset),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_RouteC_HYM_Selected_Value_Search_v1", data["next_required_artifact"]),
        check("note records smoke distinction", "lifted-selected-flags smoke" in note and "honest failure" in note, NOTE),
    ]
    print("\nMTT selected Route-C/HYM operator pipeline audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
