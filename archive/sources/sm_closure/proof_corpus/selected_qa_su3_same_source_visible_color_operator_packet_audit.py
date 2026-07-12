"""Audit the selected Qa/SU3 same-source visible/color operator packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_same_source_visible_color_operator_packet_certificate.json"
DATA = REPO / "candidate_data" / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Qa_SU3_Same_Source_Visible_Color_Operator_Packet_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_same_source_visible_color_operator_packet.py"


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
    packet = data["same_source_packet_attempt"]
    tests = data["promotion_tests"]
    gates = data["gate_results"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_QA_SU3_SAME_SOURCE_VISIBLE_COLOR_OPERATOR_PACKET_ATTEMPT_BUILT_PROMOTION_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("unique L3-K2 lift", packet["topological_candidate"]["ordered_difference"] == "L3_minus_K2" and packet["topological_candidate"]["unique_ordered_difference"] is True, packet["topological_candidate"]),
        check("closed S3/GS support", all(packet["closed_support"].values()) and tests["T2_S3_GS_support_closed"] is True, packet["closed_support"]),
        check("monad c2 mismatch rejected", packet["not_same_source_yet"]["monad_alone_realizes_visible_alpha1_source"] is False and gates["monad_c2_mismatch_rejected"] is True, packet["not_same_source_yet"]),
        check("ordered source still open", tests["T4_ordered_source_selected"] is False and "selected_ordered_integral_source_certificate" in packet["not_same_source_yet"]["ordered_source_still_open"], packet["not_same_source_yet"]["ordered_source_still_open"]),
        check("Pic0 still open", tests["T5_Pic0_selected_or_quotiented"] is False and cert["what_remains_open"]["Pic0_selection_or_quotient"] is True, cert),
        check("operator emission still open", tests["T7_transition_rhoE_or_DE_emitted"] is False and tests["T9_Riesz_Green_dotD_projector_retention"] is False, tests),
        check("finite determinant still open", tests["T10_finite_determinant_or_torsion_response"] is False, tests),
        check("not promoted", gates["operator_source_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Qa_SU3_Ordered_VAlpha_Pic0_Source_Repair_v1", data["next_required_artifact"]),
        check("note records no closure", "The result is not closure" in note and "Promotion is blocked" in note, NOTE),
    ]
    print("\nMTT selected Qa/SU3 same-source visible/color operator packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
