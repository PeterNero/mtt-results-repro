"""Audit the selected Route-C/HYM value-search closure attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_routec_hym_value_search_certificate.json"
DATA = REPO / "candidate_data" / "selected_routec_hym_value_search.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_HYM_Selected_Value_Search_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_routec_hym_value_search.py"


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
    attempts = data["closure_attempts"]
    gates = data["gate_results"]
    lemma = data["last_remaining_lemma"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_ROUTEC_HYM_VALUE_SEARCH_EXECUTED_SELECTED_SOURCE_ORIGIN_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("superset classification", cert["superset_mode"] == "SUPERSET_REPAIR_SEARCH_NOT_CLOSED" and superset["classification"] == "SUPERSET_REPAIR_SEARCH_NOT_CLOSED", superset),
        check("straight path rejected", superset["straight_path"]["succeeds"] is False and attempts["A_promote_smoke_values"]["status"] == "REJECTED_SOURCE_FLAG", attempts["A_promote_smoke_values"]),
        check("zero residual smoke exists", attempts["A_promote_smoke_values"]["residuals_all_zero"] is True and gates["zero_residual_smoke_exists"] is True, attempts["A_promote_smoke_values"]),
        check("smoke not promoted", attempts["A_promote_smoke_values"]["selected_source_verified"] is False and gates["zero_residual_smoke_promoted"] is False, attempts["A_promote_smoke_values"]),
        check("honest residual fails source flag", gates["honest_route_c_residual_validator_passes"] is False and attempts["A_promote_smoke_values"]["honest_validator_exit_codes"]["route_c_residual"] == 1, attempts["A_promote_smoke_values"]),
        check("honest downstream validators fail source flags", gates["honest_de_action_validator_passes"] is False and gates["honest_riesz_gap_validator_passes"] is False and gates["honest_reduced_green_validator_passes"] is False and gates["honest_dotd_response_validator_passes"] is False, gates),
        check("DE source hunt found no source", attempts["B_import_selected_DE_source_hunt"]["selected_D_E_source_found"] is False, attempts["B_import_selected_DE_source_hunt"]),
        check("orientation attempt source origin open", attempts["D_orientation_DE_dotD_source"]["selected_source_origin_constructed"] is False and attempts["D_orientation_DE_dotD_source"]["q79_finite_equations_blocked_only_by_source_flags"] is True, attempts["D_orientation_DE_dotD_source"]),
        check("L2 source absent", attempts["E_visible_L2_or_monad_source"]["selected_L2_cochain_packet_found"] is False and attempts["E_visible_L2_or_monad_source"]["must_construct_selected_L2_packet_from_geometry"] is True, attempts["E_visible_L2_or_monad_source"]),
        check("visible operator blocker unresolved", attempts["F_visible_operator_blocker"]["blocker_resolved_by_existing_data"] is False and attempts["F_visible_operator_blocker"]["first_blocking_layer"] == "selected_operator_source", attempts["F_visible_operator_blocker"]),
        check("selected origin not found", gates["selected_source_origin_found"] is False and lemma["currently_proved"] is False, lemma),
        check("selected values not closed", gates["selected_values_closed"] is False and cert["what_remains_open"]["actual_selected_RouteC_HYM_values"] is True, cert),
        check("DE/dotD not closed", gates["selected_D_E_dotD_Riesz_Green_closed"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("Qa/SU3 not closed", gates["selected_Qa_SU3_packet_closed"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and superset["diagnostic_backfit_only"]["used"] is False, superset),
        check("next artifact selected", data["next_required_artifact"] == "MTT_RouteC_Selected_Source_Origin_Lemma_v1", data["next_required_artifact"]),
        check("note records last lemma", "RouteCSelectedSourceOriginLemma" in note and "It cannot close from current data" in note, NOTE),
    ]
    print("\nMTT selected Route-C/HYM value-search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
