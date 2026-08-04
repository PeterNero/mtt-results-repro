"""Audit the selected Route-C source provenance or basis certificate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
CERT = REPO / "certificates" / "selected_routec_source_provenance_or_basis_certificate_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    calc = data["calculation"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_PROVENANCE_AND_BASIS_ATTEMPT_SUPPORT_CLOSED_PRIMITIVES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "provenance support closed but gate open",
            calc["support_closed"]["provenance_support_closed"] is True
            and data["provenance_gate"]["closed"] is False
            and data["provenance_gate"]["minimal_missing_primitive"] == "Phi_fin_selected_payload",
            data["provenance_gate"],
        ),
        check(
            "basis support closed but gate open",
            calc["support_closed"]["basis_support_closed"] is True
            and data["basis_gate"]["closed"] is False
            and data["basis_gate"]["minimal_missing_primitive"] == "quotient_valid_B_N_basis_certificate",
            data["basis_gate"],
        ),
        check(
            "no hidden matrix obstruction",
            data["what_closes_now"]["no_hidden_matrix_or_dimension_obstruction"] is True
            and calc["newly_locked"]["basis_is_not_blocked_by_dimension_or_projector_shape"] is True,
            calc["newly_locked"],
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
            data["next_required_artifact"] == "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert["primary_next_artifact"],
        ),
        check(
            "note records both attempts",
            "selected `Phi_fin` payload" in note
            and "quotient/deck-valid `B_N` basis certificate" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Route-C source provenance or basis certificate audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
