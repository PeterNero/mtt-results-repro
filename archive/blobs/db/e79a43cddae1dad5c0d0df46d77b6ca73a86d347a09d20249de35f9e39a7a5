"""Audit the ordered V_alpha / Pic0 source repair artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_ordered_valpha_pic0_source_repair_certificate.json"
DATA = REPO / "candidate_data" / "selected_qa_su3_ordered_valpha_pic0_source_repair.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Qa_SU3_Ordered_VAlpha_Pic0_Source_Repair_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_ordered_valpha_pic0_source_repair.py"


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
    gates = data["gate_results"]
    imported = data["imported_results"]
    template = data["strict_repair_packet_template"]
    live_route_ids = {row["id"] for row in data["repair_decision"]["live_routes"]}
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_QA_SU3_ORDERED_VALPHA_PIC0_SOURCE_REPAIR_BUILT_SELECTOR_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("selector obstruction imported", gates["selector_obstruction_imported"] is True and data["obstruction_scan"]["all_terms_found"] is True, data["obstruction_scan"]),
        check("sufficiency imported", gates["sufficiency_theorem_imported"] is True and imported["sufficiency"]["hypothetical_selected_validation_exit_code"] == 0, imported["sufficiency"]),
        check("conditional uniqueness imported", gates["conditional_uniqueness_imported"] is True and imported["conditional_uniqueness"]["selected_candidate"]["label"] == "L3-K2", imported["conditional_uniqueness"]),
        check("unconditional still open", gates["unconditional_selection_still_open"] is True and imported["unconditional_attempt"]["proved"] is False, imported["unconditional_attempt"]),
        check("invariant selector retired", data["repair_decision"]["exhausted_route"]["status"] == "RETIRED_AS_SELECTOR", data["repair_decision"]["exhausted_route"]),
        check("live routes complete", {"selected_terminal_monad_lane_plus_pic0_quotient", "selected_nonabelian_routec_gauduchon_wall", "gerbe_twisted_de_source"}.issubset(live_route_ids), live_route_ids),
        check("strict template built", template["ordered_difference"] == "L3_minus_K2" and template["source_status"] == "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED", template),
        check("Pic0 remains open", cert["what_remains_open"]["Pic0_selection_or_quotient_theorem"] is True and template["pic0_resolution_rule"] is None, template),
        check("operator exit remains open", cert["what_remains_open"]["same_source_operator_exit"] is True and template["same_source_operator_exit"] is None, template),
        check("not promoted", gates["ordered_source_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Terminal_Monad_Lane_Pic0_Quotient_Source_v1", data["next_required_artifact"]),
        check("note records repair theorem", "Closed topology, cohomology, curvature" in note and "Selected_Terminal_Monad_Lane_Pic0_Quotient_Source" in note, NOTE),
    ]
    print("\nMTT selected Qa/SU3 ordered VAlpha Pic0 source repair audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
