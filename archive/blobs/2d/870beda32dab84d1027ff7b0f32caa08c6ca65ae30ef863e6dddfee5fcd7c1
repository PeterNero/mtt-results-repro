"""Audit the selected Qa/SU3 m=1 Chern-Weil operator-source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_m1_rank2_ext_h1_source_data.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_m1_cw_operator_source.py"


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
    not_closed = cert["not_closed"]
    attempt = cert["attempt_result"]
    ranking = cert["source_route_ranking"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_M1_CW_OPERATOR_SOURCE_ATTEMPT_RANK2_EXT_H1_DATA_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["not_closed"] == not_closed
            and computed["source_route_ranking"] == ranking,
            computed["status"],
        ),
        check(
            "usable Chern-Weil prefix closed",
            closed["formal_trace_free_CW_row_realizable"] is True
            and closed["no_current_integrality_contradiction"] is True
            and closed["standard_chern_character_label_for_candidate"] is True
            and closed["split_abelian_shortcut_rejected_as_HYM_source"] is True
            and closed["rank2_extension_c2_arithmetic_viable"] is True
            and closed["rank2_h1_finite_input_format_defined"] is True,
            closed,
        ),
        check(
            "rank2 extension is primary route",
            ranking[0]["route"] == "non_split_rank2_V_alpha_extension"
            and ranking[0]["status"] == "PRIMARY_LIVE_SOURCE_ROUTE"
            and ranking[0]["next_required_data"]["l_vector_abc"] == [1, -2, 0]
            and ranking[0]["next_required_data"]["c1_L_squared_vector_abc"]
            == [2, -4, 0],
            ranking[0],
        ),
        check(
            "operator source not overpromoted",
            attempt["cw_operator_source_constructed"] is False
            and attempt["selected_visible_bundle_or_sheaf_model"] is False
            and attempt["sector_D_E_action_matrices"] is False
            and attempt["same_branch_dotD_alpha1_response"] is False,
            attempt,
        ),
        check(
            "remaining gate is H1 and selected Ext source",
            not_closed["compute_H1_X_L_squared_for_preferred_rank2_target"] is True
            and not_closed["select_nonzero_extension_class"] is True
            and not_closed["prove_non_split_extension_stability"] is True
            and not_closed["derive_same_total_source_D_E_dotD_Riesz_Green"] is True,
            not_closed,
        ),
        check(
            "template asks for finite cochain data",
            template["schema"] == "SelectedQaSU3M1Rank2ExtH1SourceData.v1"
            and template["preferred_first_target"]["l_vector_abc"] == [1, -2, 0]
            and template["must_supply"]["d0_matrix"] is None
            and template["must_supply"]["closed_non_exact_extension_vector_eta"]
            is None
            and "Do not claim h1 from topology-only c1 data."
            in template["forbidden_shortcuts"],
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_selected_visible_operator_source_constructed"]
            is False
            and guardrails["claims_selected_D_E_dotD_constructed"] is False
            and guardrails["claims_h1_value_computed"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records next finite target",
            "L = (1,-2,0)" in note
            and "L^2 = (2,-4,0)" in note
            and "d1*d0=0" in note
            and "closed non-exact" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 Chern-Weil operator-source attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
