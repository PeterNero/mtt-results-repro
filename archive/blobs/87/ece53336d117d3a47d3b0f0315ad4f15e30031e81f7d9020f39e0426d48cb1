"""Audit the selected Route-C primitive emission search."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_primitive_emission_search.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_primitive_emission_search_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    results = data["search_results"]
    straight = data["superset_mode"]["straight_path"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "Phi_fin not emitted",
            results["Phi_fin_payload"]["selected_values_emitted"] is False
            and results["Phi_fin_payload"]["minimum_payload_fields_still_null"] is True,
            results["Phi_fin_payload"],
        ),
        check(
            "identity rhoE rejected",
            results["Phi_fin_payload"]["identity_smoke_rejected"] is True
            and results["Phi_fin_payload"]["selected_by_mtt"] is False,
            results["Phi_fin_payload"],
        ),
        check(
            "B_N not emitted",
            results["B_N_basis"]["minimum_basis_payload_fields_still_null"] is True
            and results["B_N_basis"]["required_success_gates_pass"] is False,
            results["B_N_basis"],
        ),
        check(
            "deck scaffold partial",
            results["B_N_basis"]["selected_deck_map_present"] is True
            and results["B_N_basis"]["selected_deck_is_partial_execution_scaffold"] is True,
            results["B_N_basis"],
        ),
        check(
            "formal lift not proof",
            results["formal_lift_diagnostic"]["can_validate_downstream_algebra"] is True
            and results["formal_lift_diagnostic"]["promotion_allowed"] is False,
            results["formal_lift_diagnostic"],
        ),
        check(
            "straight path blocked",
            straight["R1_promotes"] is False and straight["R4_promotes"] is False and straight["R6_ready"] is False,
            straight,
        ),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records result",
            "not emitted" in note and "formal-lift algebra" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C selected primitive emission search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
