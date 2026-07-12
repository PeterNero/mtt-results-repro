"""Audit the Route-C R1 source or R4 B_N basis fill attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_r1_source_or_r4_bn_basis_fill.candidate.json"
CERT = REPO / "certificates" / "selected_routec_r1_source_or_r4_bn_basis_fill_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    r1 = data["R1_source_certificate_attempt"]
    r4 = data["R4_BN_basis_attempt"]
    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_R1_R4_FILL_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_PRIMITIVES",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "R1 attempted strict",
            r1["closed"] is False
            and r1["fillable_from_current_artifacts"]["strominger_selection_support"] is True
            and r1["blocking_missing_fields"]["Phi_fin_selected_values"] is True,
            r1,
        ),
        check(
            "R4 attempted strict",
            r4["closed"] is False
            and r4["fillable_from_current_artifacts"]["candidate_deck_generators"] is True
            and r4["blocking_missing_fields"]["scalar_basis_functions_phi_m"] is True,
            r4,
        ),
        check(
            "honest replay blocked",
            data["R6_honest_replay"]["ready"] is False
            and data["what_remains_open"]["R6_replay_without_lifted_flags"] is True,
            data["R6_honest_replay"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["observed_physical_data_used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "closure not claimed",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert["primary_next_artifact"],
        ),
        check(
            "note records blocks",
            "R1 is blocked by the missing selected `Phi_fin` payload" in note
            and "R4 is blocked by missing selected quotient/deck" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Route-C R1 source or R4 B_N basis fill audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
