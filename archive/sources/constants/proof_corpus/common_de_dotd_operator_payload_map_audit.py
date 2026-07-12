"""Audit the common D_E/dotD/Riesz/Green payload map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "common_de_dotd_riesz_green_payload_map_certificate.json"
TEMPLATE = REPO / "certificates" / "common_selected_operator_payload.template.json"
NOTE = REPO / "proof_corpus" / "Common_DE_dotD_Riesz_Green_Payload_Map_v1.md"
SCRIPT = REPO / "scripts" / "build_common_de_dotd_operator_payload_map.py"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    alignment = cert["repo_alignment"]
    decision = cert["path_decision"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "COMMON_DE_DOTD_RIESZ_GREEN_PAYLOAD_MAPPED_CW_SOURCE_FIRST",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["common_payload"] == cert["common_payload"]
            and computed["path_decision"] == decision
            and computed["guardrails"] == guardrails,
            computed["status"],
        ),
        check(
            "payload has full operator chain",
            cert["common_payload"]
            == [
                "selected_source_certificate",
                "selected_visible_bundle_sheaf_or_routec_source",
                "chern_weil_or_equivalent_operator_row_derivation",
                "coherent_spectral_zero_mode_projectors",
                "sector_D_E_action_matrices",
                "Riesz_projectors_and_gap_bounds",
                "reduced_Green_operators",
                "same_branch_dotD_alpha1_response",
                "primitive_C1_or_target_overlap_contractions",
            ],
            cert["common_payload"],
        ),
        check(
            "path decision points to current frontier",
            decision["construct_Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1_is_correct"]
            is True
            and cert["memory_checkpoint"]["next_artifact_to_build"]
            == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
            decision,
        ),
        check(
            "literal D_E/dotD repos align",
            alignment["mtt_nonsm_constants_no_knob"]["first_gate"]
            == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1"
            and alignment["mtt_sm_parity_closure"]["closed_support"][
                "validator_sequence_locked"
            ]
            is True
            and alignment["mtt_qa_su3_packet_proof"]["open_payload"][
                "selected_DE_dotD_response"
            ]
            is True
            and alignment["mtt_q79_proof_repro"]["open_payload"][
                "selected_D_E_constructed"
            ]
            is False,
            alignment,
        ),
        check(
            "protospinor is adjacent not same typed payload",
            alignment["mtt_protospinor_gr_response_proof"][
                "has_related_operator_vocab_hits"
            ]
            is True
            and alignment["mtt_protospinor_gr_response_proof"][
                "shares_sm_typed_payload"
            ]
            is False,
            alignment["mtt_protospinor_gr_response_proof"],
        ),
        check(
            "template forbids shortcut imports",
            template["schema"] == "CommonSelectedOperatorPayload.v1"
            and "Do not import lifted smoke flags as selected source proof."
            in template["forbidden_shortcuts"]
            and "selected_source_certificate" in template["payload_order"],
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_common_payload_constructed"] is False
            and guardrails["claims_selected_D_E_dotD_constructed"] is False
            and guardrails["claims_full_SM_or_nonSM_closure"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records memory checkpoint",
            "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1" in note
            and "baseline commit: 274d6eb" in note
            and "Validator shapes are reusable; selected-source flags are not." in note,
            NOTE,
        ),
    ]

    print("\nCommon D_E/dotD/Riesz/Green payload map audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
