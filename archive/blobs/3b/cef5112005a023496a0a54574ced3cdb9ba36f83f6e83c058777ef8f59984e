"""Audit the selected U1 carrier/projector or SU2 spectrum promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum_certificate.json"
DATA = REPO / "candidate_data" / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Threshold_Carrier_Projector_or_SU2_Operator_Spectrum_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def test_by_id(items: list[dict[str, object]], tid: str) -> dict[str, object]:
    return next(item for item in items if item["id"] == tid)


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
    rq = data["rank_quotient_replay"]
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "U1_THRESHOLD_CARRIER_PROJECTOR_GATE_REDUCED_SU2_WEAK_SPLIT_CLOSED_U1_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("rank three replay", rq["raw_rank_from_candidate_carrier"] == 3 and rq["raw_projector_trace"] == 3, rq),
        check("would give 2/3", rq["would_give_U1_weight"] == "2/3" and rq["matches_source_theorem_weight"] is True, rq),
        check("rank shape found but not promotable", test_by_id(data["u1_promotion_tests"], "rank_three_projective_carrier_shape")["passes_shape"] is True and test_by_id(data["u1_promotion_tests"], "rank_three_projective_carrier_shape")["promotable"] is False, data["u1_promotion_tests"]),
        check("identity is not quotient projector", test_by_id(data["u1_promotion_tests"], "sector_projector_shape")["passes_shape"] is True and test_by_id(data["u1_promotion_tests"], "sector_projector_shape")["promotable"] is False, data["u1_promotion_tests"]),
        check("same-source fusion still open", test_by_id(data["u1_promotion_tests"], "same_source_operator_fusion")["promotable"] is False, test_by_id(data["u1_promotion_tests"], "same_source_operator_fusion")),
        check("SU2 flat branch now selectable for weak split", test_by_id(data["su2_promotion_tests"], "flat_background_universal_fp_branch")["promotable"] is True, data["su2_promotion_tests"]),
        check("SU2 flatness closed", test_by_id(data["su2_promotion_tests"], "selected_su2_threshold_background_flatness")["promotable"] is True, data["su2_promotion_tests"]),
        check("SU2 FP quotient policy closed", test_by_id(data["su2_promotion_tests"], "selected_flat_fp_quotient_policy")["promotable"] is True, data["su2_promotion_tests"]),
        check("hypotheses reduced", data["theorem_hypothesis_status_after_gate"]["H1_three_direction_u1_threshold_carrier"] == "SHAPE_FOUND_NOT_SELECTED" and data["theorem_hypothesis_status_after_gate"]["H3_physical_quotient_removes_shared_mode"] == "PROJECTOR_MISSING" and data["theorem_hypothesis_status_after_gate"]["H4_SU2_unit_index_or_selected_spectrum"].startswith("CLOSED_FOR_WEAK_SPLIT"), data["theorem_hypothesis_status_after_gate"]),
        check("no promotion", decision["promoted_to_selected_threshold_index"] is False and decision["current_source_no_go"] is True, decision),
        check("remaining blocker is U1", decision["su2_unit_index_or_spectrum_found"] is True and decision["source_selected_u1_carrier_found"] is False and decision["quotient_projector_P_perp_found"] is False, decision),
        check("target not used", decision["target_fitting_used"] is False and data["target_fitting_used"] is False, decision),
        check("note records minimal packet", "Minimal Packet That Would Close This Gate" in note and "quotient projector P_perp" in note, NOTE),
    ]
    print("\nSelected U1 threshold carrier/projector or SU2 spectrum audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
