"""Audit the selected Qa/SU3 m=1 de_response target import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_deresponse_target_import_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_m1_selected_source_origin.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_DeResponse_Target_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_m1_deresponse_target.py"


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
    closed = cert["closed_now"]
    failures = cert["current_honest_packet_failures"]
    not_closed = cert["not_closed"]
    guardrails = cert["guardrails"]

    q79_failures = failures["q79_dotd_response_validator"]["failures"]
    q369_failures = failures["q369_dotd_response_validator"]["failures"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_M1_DERESPONSE_TARGET_IMPORTED_SELECTED_SOURCE_ORIGIN_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["current_honest_packet_failures"] == failures
            and computed["not_closed"] == not_closed,
            computed["status"],
        ),
        check(
            "m1 target is coherent conditionally",
            closed["m1_representative_fixed"] is True
            and closed["de_response_is_right_next_gate_on_m1"] is True
            and closed[
                "finite_validator_stack_has_no_additional_algebraic_blocker"
            ]
            is True
            and closed["conditional_lifted_hym_gate_passes"] is True
            and closed["conditional_lifted_promotion_passes"] is True,
            closed,
        ),
        check(
            "current honest packets still fail",
            closed["honest_current_hym_source_fails_without_selected_source"]
            is True
            and closed[
                "honest_current_promotion_fails_without_selected_source"
            ]
            is True
            and failures["selected_hym_operator_source_attempt_exit_code"] == 1
            and failures["selected_source_promotion_attempt_exit_code"] == 1,
            failures,
        ),
        check(
            "dotd failures localize to source flags",
            failures["q79_dotd_response_validator"]["exit_code"] == 1
            and failures["q369_dotd_response_validator"]["exit_code"] == 1
            and "Q selected_dotD_source_verified is not true" in q79_failures
            and "Q alpha1_driver_verified is not true" in q79_failures
            and "Q selected_dotD_source_verified is not true" in q369_failures
            and "Q alpha1_driver_verified is not true" in q369_failures,
            {"q79": q79_failures[:4], "q369": q369_failures[:4]},
        ),
        check(
            "source origin remains open",
            not_closed["selected_visible_SM_bundle_or_twisted_source"] is True
            and not_closed["Freed_Witten_and_projector_retention"] is True
            and not_closed["repo_level_selected_D_E_dotD_data"] is True
            and not_closed["selected_C1_primitive_contractions"] is True
            and not_closed["full_SM_closure"] is True,
            not_closed,
        ),
        check(
            "template requires genuine source origin",
            template["schema"] == "SelectedQaSU3M1SelectedSourceOrigin.v1"
            and template["must_supply"][
                "selected_visible_SM_bundle_or_twisted_source"
            ]
            is None
            and "Do not copy temporary lifted selected-source flags into repo data without a source certificate."
            in template["forbidden_shortcuts"],
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_selected_source_constructed"] is False
            and guardrails["claims_repo_level_selected_D_E_dotD_data"] is False
            and guardrails["claims_lifted_flags_are_physical_proof"] is False
            and guardrails["claims_full_SM_closure"] is False,
            guardrails,
        ),
        check(
            "note records source-origin frontier",
            "source origin" in note
            and "selected_dotD_source_verified" in note
            and "alpha1_driver_verified" in note
            and "temporary lifted" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 de_response target import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
