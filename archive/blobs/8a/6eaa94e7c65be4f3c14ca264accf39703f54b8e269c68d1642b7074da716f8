"""Audit the terminal monad lane / Pic0 quotient source artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_terminal_monad_lane_pic0_quotient_source_certificate.json"
DATA = REPO / "candidate_data" / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Terminal_Monad_Lane_Pic0_Quotient_Source_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_terminal_monad_lane_pic0_quotient_source.py"


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
    terminal = data["terminal_lane_audit"]
    imported = data["imported_results"]
    routes = {row["id"]: row for row in data["pic0_route_audit"]}
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_TERMINAL_MONAD_LANE_PIC0_QUOTIENT_SOURCE_AUDITED_PIC0_GATE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("previous frontier matches", imported["previous_frontier"]["next_required_artifact"] == "MTT_Selected_Terminal_Monad_Lane_Pic0_Quotient_Source_v1", imported["previous_frontier"]),
        check("terminal conditional uniqueness imported", gates["terminal_lane_conditional_uniqueness_imported"] is True and terminal["selected_ordered_difference"] == "L3-K2", terminal),
        check("strict ordered validator dependency kept", terminal["strict_ordered_validator_would_pass_after_source_and_pic0"] is True and gates["L3_K2_inside_lane_forced"] is True, terminal),
        check("source lane still absent", gates["source_lane_selector_absent"] is True and terminal["source_lane_selected_by_mtt"] is False, terminal),
        check("base/lattice still absent", gates["standard_lattice_base_order_absent"] is True and terminal["base_factor_order_selected"] is False, terminal),
        check("naive Pic0 quotient rejected", gates["naive_pic0_quotient_rejected"] is True and routes["naive_physical_pic0_quotient"]["status"] == "REJECTED_UNPROVED", routes["naive_physical_pic0_quotient"]),
        check("neutral Pic0 absent", gates["neutral_pic0_selection_absent"] is True and routes["neutral_pic0_holonomy_selection"]["status"] == "OPEN_ABSENT", routes["neutral_pic0_holonomy_selection"]),
        check("finite gerbe route live", gates["finite_gerbe_torsion_route_live"] is True and routes["finite_gerbe_torsion_replacement"]["status"] == "LIVE_PARTIAL", routes["finite_gerbe_torsion_replacement"]),
        check("q79 gerbe m=1 imported", imported["fixed_gerbe_representative"]["q79_torsion_label_m"] == 1 and imported["fixed_gerbe_representative"]["q79_orientation"] == "F", imported["fixed_gerbe_representative"]),
        check("deck quotient imported", imported["finite_deck_cech_lift"]["deck_quotient_target"] == "F_3^2" and imported["finite_deck_cech_lift"]["active_quotient_delta_zero"] is True, imported["finite_deck_cech_lift"]),
        check("smooth source still open", gates["smooth_gerbe_source_still_open"] is True and imported["smooth_s3_lift_attempt"]["selected_smooth_S3_source_constructed"] is False, imported["smooth_s3_lift_attempt"]),
        check("operator selector still open", gates["same_source_operator_selector_still_open"] is True and imported["hym_operator_attempt"]["selected_hym_operator_source_verified"] is False, imported["hym_operator_attempt"]),
        check("terminal Pic0 source not promoted", gates["selected_terminal_lane_pic0_source_proved"] is False and cert["what_remains_open"]["Pic0_invariance_or_neutral_selection_theorem"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Pic0_Invariance_or_Gerbe_Twisted_DE_Source_v1", data["next_required_artifact"]),
        check("note records rejection and live route", "REJECTED_UNPROVED" in note and "finite_gerbe_torsion_replacement" in note, NOTE),
    ]
    print("\nMTT selected terminal monad lane Pic0 quotient source audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
