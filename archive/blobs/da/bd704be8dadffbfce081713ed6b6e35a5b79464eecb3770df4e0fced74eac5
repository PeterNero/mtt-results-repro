"""Audit the Iwasawa abelian-row to nonabelian-source promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_iwasawa_abelian_row_to_nonabelian_source_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Abelian_Row_to_Nonabelian_Source_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_iwasawa_abelian_row_to_nonabelian_source_gate.py"


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


def by_id(cert: dict, route_id: str) -> dict:
    for item in cert["promotion_tests"]:
        if item["id"] == route_id:
            return item
    raise AssertionError(route_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    decision = cert["decision"]
    direct = by_id(cert, "direct_sum_line_bundle_promotion")
    stable = by_id(cert, "stable_su3_bundle_same_chern_row")
    extension = by_id(cert, "indecomposable_extension_promotion")
    projective = by_id(cert, "projective_clock_shift_carrier_promotion")

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_IWASAWA_ABELIAN_ROW_PROMOTION_GATE_BUILT_EXTENSION_ROUTE_PRIMARY",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["decision"] == cert["decision"]
            and computed["primary_route"] == cert["primary_route"],
            computed["decision"],
        ),
        check(
            "abelian row is support only",
            decision["abelian_row_promoted_to_selected_su3_source_now"] is False
            and decision["abelian_row_remains_valid_support_data"] is True,
            decision,
        ),
        check(
            "direct-sum route rejected",
            direct["status"] == "REJECT_AS_SELECTED_QA_SU3_SOURCE"
            and direct["blocking_tests"]["indecomposable_rank3_branch"] is False,
            direct,
        ),
        check(
            "stable route is live but not constructed",
            stable["status"] == "LIVE_BUT_UNCONSTRUCTED"
            and stable["blocking_tests"]["explicit_transition_functions"] is False,
            stable,
        ),
        check(
            "indecomposable route selected as primary research path",
            extension["status"] == "BEST_CURRENT_RESEARCH_ROUTE"
            and decision["indecomposable_extension_route_primary"] is True
            and extension["blocking_tests"]["extension_class_selected"] is False,
            extension,
        ),
        check(
            "projective carrier not overpromoted",
            projective["status"] == "AUXILIARY_ONLY_NOT_SELECTED_SOURCE"
            and decision["projective_clock_shift_route_source"] is False,
            projective,
        ),
        check(
            "closure not claimed",
            decision["determinant_computable_now"] is False
            and decision["qa_su3_closed"] is False
            and decision["target_fitting_used"] is False,
            decision,
        ),
        check(
            "note records next construction gate",
            "Selected_Qa_SU3_NonSplit_Extension_Source_Construction_v1" in note
            and "abelian row promoted to selected SU3 source now: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Iwasawa abelian-row promotion gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
