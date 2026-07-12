"""Audit the selected orientation-carrying D_E/dotD source artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_orientation_carrying_de_dotd_source.candidate.json"
CERT = REPO / "certificates" / "selected_orientation_carrying_de_dotd_source_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    audit = data["finite_payload_audit"]
    open_items = data["what_remains_open"]
    pair = data["superset_mode"]["superset_convergence"]["antiunitary_pair"]

    checks = [
        check("status", data["status"] == "MTT_SELECTED_ORIENTATION_CARRYING_DE_DOTD_SOURCE_REDUCED_TO_SOURCE_ORIGIN_AND_ALPHA1_DRIVER", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset mode", data["superset_mode"]["classification"] == "SUPERSET_CONVERGENCE_PRIMARY_REDUCTION", data["superset_mode"]),
        check("no target fitting", data["target_fitting_used"] is False and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False, data["superset_mode"]["diagnostic_backfit_only"]),
        check("q79 residual smoke zero", audit["q79_residuals_zero"] is True, audit),
        check("positive smoke gates", all(audit["q79_positive_gates"].values()), audit["q79_positive_gates"]),
        check("de/green/dotd finite shapes present", audit["q79_de_action_flags"]["boundary_conditions_verified"] is True and audit["q79_reduced_green_flags"]["riesz_gap_verified"] is True and audit["q79_dotd_response_flags"]["horizontal_gauge_verified"] is True, audit),
        check("source flags not promoted", audit["q79_de_action_flags"]["selected_source_verified"] is False and audit["q79_dotd_response_flags"]["selected_dotD_source_verified"] is False, audit),
        check("alpha1 driver still open", audit["q79_dotd_response_flags"]["alpha1_driver_verified"] is False and open_items["alpha1_driver_provenance"] is True, audit["q79_dotd_response_flags"]),
        check("q369 conjugate present", audit["q369_conjugate_shape_present"] is True and pair["sector_orientation_sum_mod3_zero"] is True, pair),
        check("source origin open", open_items["selected_source_origin"] is True and open_items["same_branch_derivative_verified"] is True, open_items),
        check("next packet", data["next_required_artifact"] == "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1" and cert["primary_next_artifact"] == data["next_required_artifact"], cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["selected_source_origin"] is True, cert),
        check("note records source reduction", "alpha_1 driver provenance" in note and "Validator Blockers" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected orientation-carrying D_E/dotD source audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
