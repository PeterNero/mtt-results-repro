"""Audit CONST-HIGGS-01 H7A3 selected nonlinear zero-mode potential theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SEARCH = BASE / "selected_zero_mode_potential_search.packet.json"
UNDERDETERMINATION = BASE / "analytic_zero_mode_potential_underdetermination_proof.packet.json"
ROUTE_DECISION = BASE / "route_a_decision_after_h7a3.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7A3_SelectedNonlinearZeroModePotentialTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7A3_ZERO_MODE_POTENTIAL_UNDERDETERMINED_ROUTEA_PARKED"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    search = load(SEARCH)
    under = load(UNDERDETERMINATION)
    decision = load(ROUTE_DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("search", search),
        ("under", under),
        ("decision", decision),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["selected_analytic_zero_mode_potential_found"] is False, "potential found")
    require(candidate["current_closed_data_underdetermine_K4"] is True, "underdetermined")
    require(candidate["route_A_parked_pending_new_source_theorem"] is True, "route A parked")
    require(candidate["route_B_promoted_as_near_term_primary"] is True, "route B primary")
    require(candidate["same_source_H_sector_fourth_variation_row_emitted"] is False, "K4 emitted")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")
    require(candidate["new_Higgs_specific_parameters"] == 0, "params")

    require(search["selected_analytic_zero_mode_potential_found"] is False, "search potential")
    for item in search["searched_candidate_classes"].values():
        require(item["found"] is True, "candidate class found")
        require(item["accepted_as_Veff"] is False, "candidate accepted")

    fixed = under["closed_data_held_fixed"]
    require(fixed["Higgs_coordinate_index"] == 12, "H coord")
    require(fixed["quartic_row_address"] == [12, 12, 12, 12], "row address")
    require(fixed["same_source_trace_and_H_projector_support"] is True, "same source support")
    family = under["countermodel_family"]
    require(family["V_0"]["agrees_with_closed_data"] is True, "V0 closed")
    require(family["V_1"]["agrees_with_closed_data"] is True, "V1 closed")
    require(family["V_0"]["K_H_4_row"] != family["V_1"]["K_H_4_row"], "different K4")
    require(family["same_closed_data_different_K4"] is True, "same data different K4")
    logic = under["logical_consequence"]
    require(logic["K4_unique_from_current_closed_data"] is False, "K4 unique")
    require(logic["K4_theorem_derived_now"] is False, "K4 derived")
    require(logic["requires_extra_selected_source_rule"] is True, "extra source")
    guard = under["guardrail"]
    require(guard["does_not_deny_future_zero_mode_potential_theorem"] is True, "future theorem")
    require(guard["denies_only_current_derivation_from_existing_closed_packets"] is True, "current only")

    route = decision["route_A_status"]
    require(route["intrinsic_K4_row_address_ready"] is True, "route row")
    require(route["current_K4_derivation_underdetermined"] is True, "route under")
    require(route["route_A_strict_closure"] is False, "route A closure")
    dec = decision["decision"]
    require(dec["park_route_A_as_active_waiting_for_new_source_theorem"] is True, "park A")
    require(dec["promote_route_B_as_near_term_primary"] is True, "promote B")
    require("H7B-UV-BETA" in dec["route_B_label"], "route B label")
    require(decision["superset_strategy"]["paths_combined_as_free_parameters"] is False, "superset params")

    require("H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM" in next_work["primary_next"]["label"], "next B")
    require("H7A4-NEW-ZERO-MODE-POTENTIAL-SOURCE-RULE" in next_work["parked_route_A_resume_condition"]["label"], "resume A")
    require(cert["status"] == STATUS, "cert status")
    require(cert["current_closed_data_underdetermine_K4"] is True, "cert under")
    require(cert["route_A_parked_pending_new_source_theorem"] is True, "cert A")
    require(cert["route_B_promoted_as_near_term_primary"] is True, "cert B")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("V_c(a_H)" in note and "H7B-UV-BETA" in note, "note")

    print("CONST-HIGGS-01 H7A3 selected nonlinear zero-mode potential audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
