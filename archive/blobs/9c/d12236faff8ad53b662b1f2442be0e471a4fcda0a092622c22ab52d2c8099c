"""Audit the selected Qa/SU3 Route C source solve gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_routec_source_solve.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_RouteC_Source_Solve_Gate_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_routec_source_solve_gate.py"


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
    open_items = cert["not_closed"]
    routes = cert["route_status"]
    next_object = cert["next_object"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_ROUTEC_SOURCE_SOLVE_GATE_CURRENT_SOURCE_EXHAUSTED_NEW_SOURCE_REQUIRED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == cert["closed_now"]
            and computed["not_closed"] == cert["not_closed"]
            and computed["route_status"] == routes,
            computed["status"],
        ),
        check(
            "template names required source",
            template["status"] == "OPEN_SELECTED_QA_SU3_ROUTEC_SOURCE_SOLVE_REQUIRED"
            and "selected_visible_sm_bundle_or_sheaf_model" in template["must_supply"]
            and "route_c_residual_packet_with_selected_source_verified"
            in template["must_supply"],
            template,
        ),
        check(
            "current routes exhausted",
            closed["current_route_exhaustion_proved"] is True
            and routes["R1_corrected_non_invariant_Dolbeault_operator"] == "BLOCKED"
            and routes["R2_typed_monad_sections"] == "BLOCKED"
            and routes["R3_direct_selected_HYM_solve"] == "ABSTRACT_EXISTENCE_ONLY"
            and routes["twisted_S3_packet"] == "PARTIAL_PROMOTION_OPEN",
            routes,
        ),
        check(
            "promotion and validators ready",
            closed["promotion_contract_ready"] is True
            and closed["finite_validator_pipeline_ready_from_previous_gate"] is True,
            closed,
        ),
        check(
            "first new object identified",
            closed["first_new_object_identified"] is True
            and next_object["name"]
            == "Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1",
            next_object,
        ),
        check(
            "remaining blockers explicit",
            open_items["selected_visible_sm_bundle_or_sheaf_model"] is True
            and open_items["selected_D_E_source"] is True
            and open_items["route_c_residual_solve"] is True
            and open_items["primitive_C1_or_Yukawa_contractions"] is True,
            open_items,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_selected_visible_operator_source_constructed"] is False
            and cert["guardrails"]["claims_selected_D_E_constructed"] is False
            and cert["guardrails"]["promotes_route_c_smoke"] is False
            and cert["guardrails"]["promotes_abstract_hym_existence_to_matrix"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records proof frontier",
            "Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1" in note
            and "current q79 evidence exhausts" in note
            and "not a different arrangement of already closed certificates" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Route C source solve gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
