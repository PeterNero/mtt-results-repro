"""Audit the selected Phi_fin alpha1 payload attempt artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
CERT = REPO / "certificates" / "selected_phifin_alpha1_payload_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_PhiFin_Alpha1_Payload_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    summary = data["payload_summary"]
    support = summary["support_candidate_present"]
    selected = summary["selected_payload_flags"]
    gerbe = data["projective_gerbe_support"]
    open_items = data["what_remains_open"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check(
            "superset payload attempt",
            data["superset_mode"]["classification"] == "SUPERSET_REPAIR_PAYLOAD_ATTEMPT"
            and data["superset_mode"]["straight_path"]["classification"] == "STRAIGHT_PROMOTION_REJECTED",
            data["superset_mode"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check("all support shapes present", summary["all_support_shapes_present"] is True and all(support.values()), support),
        check(
            "selected values not emitted",
            summary["all_selected_values_emitted"] is False
            and all(value is False for value in selected.values())
            and open_items["selected_PhiFin_alpha1_payload_values"] is True,
            selected,
        ),
        check(
            "projective rhoE support not promoted",
            gerbe["central_twist_nontrivial"] is True
            and gerbe["projective_mismatch_count"] == 0
            and gerbe["operator_level_projective_rhoE_promoted"] is False
            and open_items["operator_level_projective_rhoE_promotion"] is True,
            gerbe,
        ),
        check(
            "selected spectral projector retention open",
            open_items["coherent_spectral_projector_retention"] is True
            and open_items["selected_D_E_Riesz_Green_dotD_values"] is True,
            open_items,
        ),
        check(
            "C1 values open",
            open_items["finite_C1_Hessian_and_deltaTheta"] is True
            and open_items["zero_mode_bases_and_primitive_contractions"] is True,
            open_items,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert,
        ),
        check(
            "closure not claimed",
            cert["closure_claimed"] is False and cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "note records rejected promotion",
            "Straight path: rejected" in note
            and "selected values are" in note
            and "Next artifact: `MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Phi_fin alpha1 payload audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
