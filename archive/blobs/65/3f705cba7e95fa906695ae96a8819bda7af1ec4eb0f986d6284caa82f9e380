"""Audit the selected Qa/SU3 visible operator-source packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_visible_operator_source_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Visible_Operator_Source_Packet_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_visible_operator_source_packet.py"


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
    gate = cert["gate_result"]
    open_items = cert["not_closed"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_VISIBLE_OPERATOR_SOURCE_PACKET_ATTEMPT_BUILT_SELECTED_BUNDLE_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == cert["closed_now"]
            and computed["not_closed"] == cert["not_closed"]
            and computed["gate_result"] == cert["gate_result"],
            computed["gate_result"],
        ),
        check(
            "template is source-demanding",
            template["status"] == "OPEN_SELECTED_QA_SU3_VISIBLE_OPERATOR_SOURCE_PACKET_REQUIRED"
            and template["must_supply"]["selected_visible_bundle_or_sheaf_model"] is None
            and template["must_supply"]["selected_D_E_constructed"] is None,
            template["must_supply"],
        ),
        check(
            "prior support closed",
            closed["selected_s3_gerbe_fw_projector_support"] is True
            and closed["visible_green_schwarz_curvature_row"] is True
            and closed["projective_and_block_factorized_non_source_blockers_reduced"] is True,
            closed,
        ),
        check(
            "current HYM attempt rejected honestly",
            closed["current_attempt_rejected_honestly"] is True
            and cert["validator_result"]["exit_code"] == 1
            and "source.selected_by_mtt must be true" in cert["validator_result"]["failures"],
            cert["validator_result"]["failures"],
        ),
        check(
            "selected source fields remain open",
            open_items["selected_visible_bundle_or_sheaf_model"] is True
            and open_items["Chern_Weil_row_derived_from_selected_source"] is True
            and open_items["HYM_or_Route_C_residual_for_visible_source"] is True
            and open_items["selected_D_E_dotD_Riesz_Green"] is True,
            open_items,
        ),
        check(
            "no false closure",
            cert["guardrails"]["claims_selected_visible_operator_source_constructed"] is False
            and cert["guardrails"]["promotes_visible_gs_row_insertion_to_source"] is False
            and gate["visible_operator_source_packet_closed"] is False
            and gate["remaining_gate_is_selected_bundle_or_operator_source"] is True
            and gate["target_fitting_used"] is False,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records minimal next object",
            "selected_q79_visible_bundle_or_route_c_operator_source" in note
            and "visible operator-source packet closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 visible operator-source packet attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
