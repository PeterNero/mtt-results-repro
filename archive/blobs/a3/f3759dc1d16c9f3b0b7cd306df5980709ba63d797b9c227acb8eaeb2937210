"""Audit the selected Route-C source selector and basis theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_source_selector_and_basis_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_routec_source_selector_and_basis_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    closes = data["what_closes_now"]
    open_items = data["what_remains_open"]
    comparison = data["calculation"]["root_vs_formal_payload_diff"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_SOURCE_SELECTOR_AND_BASIS_CALCULATION_LOCKED_SELECTOR_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "flag-only delta",
            comparison["all_differences_are_allowed_flags"] is True
            and comparison["changed_terminal_keys"]
            == ["alpha1_driver_verified", "selected_dotD_source_verified", "selected_source_verified"],
            comparison,
        ),
        check(
            "algebra conditionally passes",
            data["calculation"]["formal_lift_lower_validators_all_pass"] is True
            and data["calculation"]["formal_lift_de_response_promotion_passes"] is True,
            data["calculation"],
        ),
        check(
            "honest cutset retained",
            closes["honest_failure_cutset_identified"] is True
            and "route_c_residual" in data["calculation"]["honest_root_failures"],
            data["calculation"]["honest_root_failures"],
        ),
        check(
            "basis gap retained",
            closes["basis_gap_identified"] is True
            and data["calculation"]["basis_skeleton_verdict"]["closes_actual_basis_functions"] is False,
            data["calculation"]["basis_skeleton_verdict"],
        ),
        check(
            "locked conditions exact",
            set(data["locked_conditions"].keys()) == {"C1_source_selector_condition", "C2_basis_condition"}
            and "selected HYM/Strominger source theorem" in " ".join(data["superset_mode"]["superset_repair"]["required_objects"]),
            data["locked_conditions"],
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
            and open_items["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert["primary_next_artifact"],
        ),
        check(
            "note records theorem",
            "Total root/formal differences" in note
            and "Next artifact: `MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Route-C source selector and basis theorem audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
