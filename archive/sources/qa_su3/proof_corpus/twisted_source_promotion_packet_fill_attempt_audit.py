"""Audit the twisted-source promotion packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "twisted_source_promotion_packet_fill_attempt_certificate.json"
DATA = REPO / "candidate_data" / "twisted_source_promotion_packet_fill_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_twisted_source_promotion_packet.py"


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
    fill = data["fill_result"]
    packet = data["partial_packet"]
    open_fields = cert["what_remains_open"]
    checks = [
        check("status", cert["status"] == "QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_FILL_ATTEMPT_PARTIAL_SOURCE_CONTEXT_BLOCKED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source context filled", fill["source_family_selected"] is True and fill["fixed_differential_class_context_found"] is True, fill),
        check("Bianchi and twist context filled", fill["global_bianchi_context_found"] is True and fill["twist_cancellation_table_available"] is True, fill),
        check("central support and validator available", fill["primitive_central_support_available"] is True and fill["projective_validator_pattern_available"] is True, fill),
        check("selected representative missing", fill["selected_Qa_SU3_representative_found"] is False and packet["source_evidence"]["Deligne_Cech_or_B_field_representative"] is None, packet["source_evidence"]),
        check("central map missing", fill["central_cocycle_map_verified"] is False and packet["source_evidence"]["map_to_central_cocycle_verified"] is False, packet["source_evidence"]),
        check("admissibility not promoted", fill["mapped_Freed_Witten_verified"] is False and packet["admissibility"]["Freed_Witten_verified"] is False, packet["admissibility"]),
        check("rhoE tables missing", fill["projective_rhoE_tables_supplied"] is False and packet["projective_rhoE"]["projective_mesh_tables"] is None, packet["projective_rhoE"]),
        check("operator response missing", fill["selected_D_E_dotD_response_supplied"] is False and all(value is None for value in packet["operator_response"].values()), packet["operator_response"]),
        check("monad bridge not numeric", fill["monad_bridge_numeric_gf_zero_checked"] is False and packet["monad_bridge"]["same_source_bridge_to_operator"] is False, packet["monad_bridge"]),
        check("remaining fields all open", all(value is False for value in open_fields.values()), open_fields),
        check("no shortcut promotion", "q79/S3 finite Deligne or Cech tables as Qa/SU3 source values" in data["what_does_not_promote"], data["what_does_not_promote"]),
        check("no closure", cert["closure_claimed"] is False and fill["qa_su3_packet_closed"] is False, fill),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False and fill["target_fitting_used"] is False, fill),
        check("note records next", data["next_required_artifact"] in note and "central-cocycle map" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 twisted-source promotion packet fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
