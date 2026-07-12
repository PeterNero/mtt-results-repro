"""Audit the selected Qa/SU3 visible rank-two V_alpha source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_visible_rank2_valpha_source_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Visible_Rank2_VAlpha_Source_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_visible_rank2_valpha_source.py"


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
    ext = cert["validated_conditional_ext_packet"]
    closed = cert["closed_now"]
    open_items = cert["not_closed"]
    gate = cert["gate_result"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_VISIBLE_RANK2_VALPHA_SOURCE_ATTEMPT_CONDITIONAL_EXT_CLOSED_SELECTION_OPEN",
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
            "template demands selected source fields",
            template["status"] == "OPEN_SELECTED_QA_SU3_VISIBLE_RANK2_VALPHA_SOURCE_PACKET_REQUIRED"
            and template["must_supply_after_q79_conditional_packet"][
                "selected_branch_orientation_source_for_L_equals_1_minus2_0"
            ]
            is None
            and template["must_supply_after_q79_conditional_packet"]["same_source_D_E_dotD_Riesz_Green"]
            is None,
            template["must_supply_after_q79_conditional_packet"],
        ),
        check(
            "rank-two target fixed",
            cert["selected_rank2_route"]["target_branch_L"] == [1, -2, 0]
            and cert["selected_rank2_route"]["target_L_squared"] == [2, -4, 0]
            and cert["selected_rank2_route"]["c1_V_alpha"] == [0, 0, 0]
            and cert["selected_rank2_route"]["c2_V_alpha"] == [4, 0, 0]
            and cert["selected_rank2_route"]["shared_circle_degree"] == 0,
            cert["selected_rank2_route"],
        ),
        check(
            "conditional Ext packet validates",
            ext["validator_exit_code"] == 0
            and ext["candidate_role"] == "UNSELECTED_FIXTURE"
            and ext["h1"] == 8
            and ext["d1_d0_zero"] is True
            and ext["extension_class_closed"] is True
            and ext["extension_class_exact"] is False
            and ext["nonzero_ext_class"] is True,
            ext,
        ),
        check(
            "selection still blocked honestly",
            ext["selected_source_promotes"] is False
            and ext["promotes_to_non_split_V_alpha_input"] is False
            and open_items["selected_L2_packet"] is True
            and open_items["unique_MTT_branch_orientation_for_L"] is True
            and open_items["neutral_or_quotiented_Pic0_character"] is True,
            {"ext": ext, "open": open_items},
        ),
        check(
            "selector not Ext existence is the remaining gate",
            closed["conditional_h1_equals_8_and_nonzero_ext"] is True
            and closed["selector_obstruction_from_current_closed_invariants"] is True
            and gate["conditional_ext_math_closed"] is True
            and gate["remaining_gate_is_selector_not_ext_existence"] is True
            and gate["visible_rank2_valpha_source_closed"] is False,
            {"closed": closed, "gate": gate},
        ),
        check(
            "guardrails prevent overclaim",
            cert["guardrails"]["claims_selected_visible_valpha_source_constructed"] is False
            and cert["guardrails"]["claims_unique_L_branch_selected"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False
            and gate["target_fitting_used"] is False,
            {"guardrails": cert["guardrails"], "gate": gate},
        ),
        check(
            "note records next orientation source",
            "Selected_Pullback_L2_Branch_Orientation_Source.v1" in note
            and "remaining gate is selector, not Ext existence: yes" in note
            and "visible rank-two V_alpha source closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 visible rank-two V_alpha source attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
