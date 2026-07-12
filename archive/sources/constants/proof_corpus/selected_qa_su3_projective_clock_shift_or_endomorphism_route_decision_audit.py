"""Audit the Qa/SU3 projective clock-shift or endomorphism route decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Projective_Clock_Shift_or_Endomorphism_Route_Decision_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision.py"


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


def by_route(cert: dict, route: str) -> dict:
    for item in cert["route_decisions"]:
        if item["route"] == route:
            return item
    raise AssertionError(route)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    projective = by_route(cert, "nonabelian_projective_clock_shift_representation")
    endomorphism = by_route(cert, "source_certified_endomorphism_E_full_operator")
    decision = cert["decision"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_PROJECTIVE_CLOCK_SHIFT_OR_ENDOMORPHISM_DECISION_BUILT_ENDOMORPHISM_PRIMARY",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["selected_phase"] == cert["selected_phase"]
            and computed["decision"] == cert["decision"],
            computed["decision"],
        ),
        check(
            "q64 phase retained as order 64",
            cert["selected_phase"]["q64"] == 15
            and cert["selected_phase"]["modulus"] == 64
            and cert["selected_phase"]["order"] == 64,
            cert["selected_phase"],
        ),
        check(
            "rank-one and SU3 center no-gos imported",
            cert["selected_phase"]["not_rank_one_nil_character"] is True
            and cert["selected_phase"]["not_su3_scalar_center"] is True,
            cert["selected_phase"],
        ),
        check(
            "projective carrier exists but is not selected proof source",
            projective["decision"] == "KEEP_AS_CONDITIONAL_AUXILIARY_BRANCH_NOT_SELECTED_PROOF_SOURCE"
            and projective["mathematical_carrier"]["minimal_irreducible_clock_shift_dimension"] == 64
            and projective["source_support"]["qa_su3_operator_support"] == "Missing.",
            projective,
        ),
        check(
            "projective source scope is separated",
            "qutrit/F3^2" in projective["source_support"]["visible_projective_support"]
            and "order-3 visible-sector" in projective["source_support"]["visible_projective_support"]
            and "rather than order-64 Qa/SU3 threshold data" in projective["source_support"]["visible_projective_support"],
            projective["source_support"],
        ),
        check(
            "endomorphism route primary but open",
            endomorphism["decision"] == "PRIMARY_NEXT_QA_SU3_ROUTE"
            and endomorphism["current_status"] == "OPEN_SOURCE_MISSING",
            endomorphism,
        ),
        check(
            "closure not overclaimed",
            decision["qa_su3_closed"] is False
            and decision["full_sm_closure_achieved"] is False
            and decision["target_fitting_used"] is False,
            decision,
        ),
        check(
            "forbidden shortcuts recorded",
            "qutrit/F3^2 projective Chan-Paton results as q64/U64 Qa/SU3 closure" in cert["do_not_use"]
            and "U64 clock-shift determinant as SU3 threshold determinant without an operator-domain theorem" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records decision",
            "endomorphism/operator source hunt is primary: yes" in note
            and "projective q64 route selected as proof source: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 projective clock-shift or endomorphism route decision audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
