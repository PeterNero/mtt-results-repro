"""Audit the imported Qa/SU3 visible-source architecture bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_visible_source_architecture_import_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_qa_su3_visible_source_architecture_import.candidate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Visible_Source_Architecture_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_visible_source_architecture.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    statuses = cert["imported_statuses"]
    rec = cert["recommended_construction"]
    mapping = cert["mapping_to_q79_fusion_packet"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "SELECTED_QA_SU3_VISIBLE_ARCHITECTURE_IMPORTED_SAME_SOURCE_PACKET_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["recommended_construction"] == rec
            and computed["mapping_to_q79_fusion_packet"] == mapping
            and computed["not_closed"] == cert["not_closed"],
            computed["status"],
        ),
        check(
            "imports current sibling architecture",
            statuses["constants_architecture"]
            == "QA_SU3_VISIBLE_SOURCE_ARCHITECTURE_RANKED_SAME_SOURCE_BINDING_OPEN"
            and statuses["q79_same_source_fusion_attempt"]
            == "SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_ATTEMPT_OPEN_SELECTED_SOURCE_MISSING"
            and statuses["gr_stress_response_gate"]
            == "STRUCTURAL_STRESS_RESPONSE_CLOSED_PHYSICAL_NORMALIZATION_OPEN",
            statuses,
        ),
        check(
            "recommended construction is A plus B with C engine",
            rec["primary"] == "A_rank2_valpha_terminal_monad_primary"
            and rec["required_merge"] == "B_s3_green_schwarz_visible_support"
            and rec["execution_engine"] == "C_direct_hym_routec_solve",
            rec,
        ),
        check(
            "local template demands V_alpha/S3 same-source packet",
            template["schema"] == "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1"
            and template["status"]
            == "OPEN_SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_REQUIRED"
            and "terminal_monad_difference_L3_minus_K2_selector"
            in template["source_skeleton"],
            template,
        ),
        check(
            "mapping hits all q79 fusion groups",
            set(mapping) == {
                "A_rank2_valpha_terminal_monad_primary",
                "B_s3_green_schwarz_visible_support",
                "C_direct_hym_routec_solve",
            }
            and "operator_response.dotd_response_pass"
            in mapping["C_direct_hym_routec_solve"],
            mapping,
        ),
        check(
            "no overclaim",
            guardrails["claims_same_source_binding_proved"] is False
            and guardrails["claims_selected_visible_bundle_constructed"] is False
            and guardrails["claims_selected_D_E_constructed"] is False
            and guardrails["claims_full_SM_closure"] is False,
            guardrails,
        ),
        check(
            "note records sharpened next object",
            "Selected_Qa_SU3_Same_Source_VAlpha_S3_Operator_Packet_v1" in note
            and "Route C is the engine, not the source" in note
            and "physical GR stress-response result does not supply" in note
            and "SM source" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["guardrails"] == cert["guardrails"],
            candidate["status"],
        ),
    ]

    print("\nSelected Qa/SU3 visible-source architecture import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
