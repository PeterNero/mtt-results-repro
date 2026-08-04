"""Audit first correction matrix search / Galerkin run."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
CERT = REPO / "certificates" / "selected_routec_first_correction_search_or_galerkin_run_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    lane_a = data["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]
    lane_b = data["parallel_lanes"]["lane_B_galerkin_replay"]
    rep = lane_a["representative"]
    combined = data["combined_result"]

    checks = [
        check(
            "status",
            data["status"]
            == "MTT_SELECTED_ROUTEC_FIRST_CORRECTION_SEARCH_AND_GALERKIN_RUN_EXECUTED_DIAGNOSTIC_SPLITTER_FOUND_SELECTED_VALUES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "lane A diagnostic splitter",
            lane_a["diagnostic_splitter_found"] is True
            and lane_a["candidate_count"] > 0
            and rep["ckm_commutator_norm_sq"] > 0
            and rep["pmns_commutator_norm_sq"] > 0
            and abs(rep["cp_odd_trace_commutator_cubed_imag"]) > 0
            and lane_a["selected_by_mtt"] is False,
            lane_a,
        ),
        check(
            "lane B Galerkin replay scoped",
            lane_b["manifest_filled"] is True
            and lane_b["honest_root_all_pass"] is False
            and lane_b["formal_lift_lower_validators_all_pass"] is True
            and lane_b["formal_lift_is_diagnostic_only"] is True
            and lane_b["selected_correction_matrices_emitted"] is False,
            lane_b,
        ),
        check(
            "combined no promotion",
            combined["diagnostic_qutrit_correction_can_break_degeneracy"] is True
            and combined["selected_correction_promoted"] is False
            and combined["honest_galerkin_selected_values_emit_correction"] is False,
            combined,
        ),
        check(
            "no closure claim or target fit",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining selected source",
            data["what_remains_open"]["selected_correction_matrix_source"] is True
            and data["what_remains_open"]["selected_galerkin_values"] is True
            and data["what_remains_open"]["promoted_CKM_PMNS_CP"] is True,
            data["what_remains_open"],
        ),
        check(
            "next artifact",
            data["next_required_artifact"]
            == "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records both lanes",
            "Lane A: Qutrit/Weyl Correction Search" in note
            and "Lane B: Galerkin Replay" in note
            and "diagnostic only" in note
            and "without lifted flags or observed flavor targets" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C first correction search / Galerkin run audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
