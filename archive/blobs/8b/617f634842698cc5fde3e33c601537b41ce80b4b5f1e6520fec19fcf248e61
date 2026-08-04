"""Audit the selected Qa/SU3 VAlpha/S3 integral-lift gap import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_valpha_s3_integral_lift_gap_import_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_VAlpha_S3_Integral_Lift_Gap_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_valpha_s3_integral_lift_gap.py"


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
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    closed = cert["closed_now"]
    obstruction = cert["selector_obstruction"]
    cohomology = cert["cohomology_after_source"]
    not_closed = cert["not_closed"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_VALPHA_S3_INTEGRAL_LIFT_GAP_IMPORTED_SOURCE_SELECTOR_REQUIRED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["selector_obstruction"] == obstruction
            and computed["not_closed"] == not_closed,
            computed["status"],
        ),
        check(
            "integral candidate exists",
            closed["explicit_integral_appell_humbert_model_exists"] is True
            and closed["ordinary_integral_c1_matrix_realized"] is True
            and cert["selected_integral_candidate"]["target_L2_degrees"]
            == [2, -4, 0],
            cert["selected_integral_candidate"],
        ),
        check(
            "cohomology is not the blocker after source",
            closed[
                "h1_8_packet_has_no_remaining_algebraic_obstruction_after_source"
            ]
            is True
            and cohomology["h1"] == 8
            and cohomology["candidate_role_now"] == "UNSELECTED_FIXTURE"
            and cohomology["conditional_promoted_exit_code"] == 0
            and cohomology["conditional_promoted_selected_source_promotes"] is True,
            cohomology,
        ),
        check(
            "mod3 bridge cannot select branch",
            closed[
                "finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift"
            ]
            is True
            and cert["relation_to_previous_gate"][
                "this_import_says_mod3_bridge_cannot_be_the_selector"
            ]
            is True,
            cert["relation_to_previous_gate"],
        ),
        check(
            "selector obstruction imported",
            closed[
                "no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data"
            ]
            is True
            and obstruction["theorem"]
            == "No current closed selector can uniquely select L=(1,-2,0)"
            and obstruction[
                "target_and_swapped_degenerate_under_current_closed_invariants"
            ]
            is True,
            obstruction,
        ),
        check(
            "Pic0 gap remains real",
            closed[
                "pic0_neutrality_not_selected_by_current_curvature_topology_data"
            ]
            is True
            and obstruction[
                "pic0_needs_holonomy_sensitive_source_or_gauge_fixing"
            ]
            is True
            and not_closed["selected_or_quotiented_Pic0_character"] is True,
            not_closed,
        ),
        check(
            "next source options are concrete",
            "selected ordered integral Cech/automorphy/D_E source"
            in cert["next_source_options"]
            and "same-source D_E/dotD/Hessian term ordering the base factors"
            in cert["next_source_options"],
            cert["next_source_options"],
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_integral_source_selected"] is False
            and cert["guardrails"]["claims_target_selector_proved"] is False
            and cert["guardrails"]["claims_neutral_pic0_selected"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records source-selector frontier",
            "h1=8" in note
            and "source-selector theorem" in note
            and "target-vs-swapped" in note
            and "Pic0" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 VAlpha/S3 integral-lift gap import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
