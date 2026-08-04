"""Audit the selected source-origin and alpha1-driver reduction artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json"
CERT = REPO / "certificates" / "selected_source_origin_and_alpha1_driver_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    source = data["source_origin_audit"]
    alpha = data["alpha1_driver_audit"]
    payload = data["unified_payload_contract"]
    closed = data["what_closes_now"]
    open_items = data["what_remains_open"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_SOURCE_ORIGIN_AND_ALPHA1_DRIVER_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check(
            "superset mode",
            data["superset_mode"]["classification"] == "SUPERSET_REPAIR_WITH_STRAIGHT_SUPPORT"
            and data["superset_mode"]["superset_repair"]["repair_object"] == "SelectedPhiFinAlpha1Payload",
            data["superset_mode"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check("source support closed", all(source["support_closed"].values()), source["support_closed"]),
        check(
            "selected source flags still open",
            all(value is False for value in source["selected_flags"].values())
            and open_items["source_origin_selected_flags"] is True,
            source["selected_flags"],
        ),
        check("Phi_fin shape built", all(source["finite_phifin_shape_gates"].values()), source["finite_phifin_shape_gates"]),
        check(
            "Phi_fin selected payload still open",
            any(value is False for value in source["phifin_selected_payload_flags"].values())
            and open_items["selected_PhiFin_alpha1_payload"] is True,
            source["phifin_selected_payload_flags"],
        ),
        check(
            "alpha1 support imported",
            all(alpha["operator_level_support"].values())
            and closed["alpha1_driver_row_and_operator_level_source_imported"] is True,
            alpha["operator_level_support"],
        ),
        check(
            "alpha1 selected values still open",
            all(value is False for value in alpha["selected_values"].values())
            and open_items["finite_C1_source_vector_and_Hessian_blocks"] is True,
            alpha["selected_values"],
        ),
        check(
            "unified payload contract",
            payload["name"] == "SelectedPhiFinAlpha1Payload"
            and "selected dotD_alpha1 as the same-branch derivative of selected D_E" in payload["must_emit"]
            and "no observed masses, CKM phase, or benchmark entries are used as inputs" in payload["acceptance"],
            payload,
        ),
        check(
            "closure not claimed",
            cert["closure_claimed"] is False
            and cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_PhiFin_Alpha1_Payload_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert,
        ),
        check(
            "note records reduction",
            "SelectedPhiFinAlpha1Payload" in note
            and "Diagnostic/backfit: not used as proof" in note
            and "Next artifact: `MTT_Selected_PhiFin_Alpha1_Payload_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected source-origin and alpha1-driver audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
