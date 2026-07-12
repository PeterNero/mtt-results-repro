"""Audit CONST-EW-02 B32 dual-path home-stretch artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b32_dual_path_home_stretch"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DUAL_FILL = BASE / "dual_path_actual_fill_import.packet.json"
CONDITIONAL = BASE / "conditional_exit_acceptance_import.packet.json"
TABLE = BASE / "routeb_source_table_shape_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b32_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B32_DualPathHomeStretch_v1.md"

STATUS = "MTT_CONST_EW_02_B32_DUAL_PATH_HOME_STRETCH_BUILT"


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
    dual_fill = load(DUAL_FILL)
    conditional = load(CONDITIONAL)
    table = load(TABLE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("dual_fill", dual_fill),
        ("conditional", conditional),
        ("table", table),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["both_actual_paths_tried"] is True, "both paths")
    require(candidate["actual_route_A_validates"] is False, "Route A overvalidated")
    require(candidate["actual_route_B_validates"] is False, "Route B overvalidated")
    require(candidate["route_A_conditional_validates"] is True, "Route A conditional")
    require(candidate["route_B_conditional_validates"] is True, "Route B conditional")
    require(candidate["route_B_table_shape_ready"] is True, "table shape")
    require(candidate["source_promotion_contract_built"] is True, "contract")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(dual_fill["validator_ok"] is False, "dual validator overaccepted")
    require("ERROR Route A missing" in dual_fill["validator_errors"][0], "Route A error missing")
    require("ERROR Route B missing" in dual_fill["validator_errors"][1], "Route B error missing")
    require(dual_fill["route_A_actual"]["same_branch"] is True, "Route A same-branch support")
    require(dual_fill["route_A_actual"]["physical_phifin_c1_action_emitted"] is False, "Route A action overemitted")
    require(dual_fill["route_A_actual"]["same_source_b_selected_emitted"] is False, "b overemitted")
    require(dual_fill["route_B_actual"]["all_72_primitive_rows_executed"] is True, "Route B rows missing")
    require(dual_fill["route_B_actual"]["source_independent_of_residual_projector_replay"] is False, "Route B source overclosed")

    require(conditional["current_export_validator_ok"] is False, "current export overaccepted")
    require(conditional["route_A_conditional_validator_ok"] is True, "Route A conditional flag")
    require(conditional["route_B_conditional_validator_ok"] is True, "Route B conditional flag")
    require(conditional["route_A_conditional_result_ok"] is True, "Route A conditional result")
    require(conditional["route_B_conditional_result_ok"] is True, "Route B conditional result")
    require(conditional["acceptance_contract"]["shared_locked_target_policy"]["observed_constants_are_forbidden_selectors"] is True, "observed guard")

    require(table["route_B_table_shape_ready"] is True, "table ready")
    require(table["route_B_table_independent"] is False, "table independence overclosed")
    require(table["strict_validator_ok"] is False, "table validator")
    require(table["what_closes_now"]["route_B_current_table_shape_audited"] is True, "table audited")
    require(table["what_remains_open"]["route_B_independent_row_kernel_source_ids"] is True, "row ids gap")

    require(boundary["closed_or_sharpened_now"]["both_actual_paths_tried"] is True, "boundary paths")
    require(boundary["closed_or_sharpened_now"]["both_conditional_exits_validate"] is True, "boundary conditional")
    require(boundary["closed_or_sharpened_now"]["numerical_row_search_removed_as_primary_blocker"] is True, "row search not removed")
    require(boundary["still_open"]["route_A_I10_or_physical_PhiFinC1_action_identity"] is True, "Route A open")
    require(boundary["still_open"]["route_B_selected_row_kernel_source_ids"] is True, "Route B open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle open")
    require("not a conditional closure claim" in boundary["anti_cycle_delta_from_B31"]["not_repeated"], "anti-cycle guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["actual_route_A_validates"] is False, "cert Route A")
    require(cert["actual_route_B_validates"] is False, "cert Route B")
    require(cert["route_A_conditional_validates"] is True, "cert conditional A")
    require(cert["route_B_conditional_validates"] is True, "cert conditional B")
    require(cert["source_promotion_closed_now"] is False, "cert source promotion")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B33-ROUTEA-I10-PHIFIN-ACTION-IDENTITY", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B33-ROUTEB-INDEPENDENT-SOURCE-ID-TABLE", "next parallel")
    require("Tried Both Paths" in note, "note missing tried paths")
    require("Home-Stretch Contract" in note, "note missing contract")

    print("CONST-EW-02 B32 dual-path home-stretch audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
