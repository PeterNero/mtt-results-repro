"""Audit the selected Route-C/Strominger Galerkin first-run manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_strominger_galerkin_first_run.candidate.json"
CERT = REPO / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    validation = data["validation"]
    interp = data["interpretation"]
    manifest = data["manifest"]
    formal = data["formal_lift_manifest"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_MANIFEST_FILLED_SELECTOR_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "manifest complete and exists",
            set(manifest.keys())
            == {
                "route_c_residual",
                "rhoE_mesh",
                "rhoE_metric",
                "sector_maps",
                "de_action",
                "riesz_gap",
                "reduced_green",
                "dotd_response",
                "spectral_galerkin_data",
                "c1_primitive_contractions",
            }
            and all(data["manifest_filled"].values())
            and all((REPO / path).exists() for path in manifest.values()),
            manifest,
        ),
        check(
            "formal manifest exists",
            set(formal.keys()) == set(manifest.keys()) and all((REPO / path).exists() for path in formal.values()),
            formal,
        ),
        check(
            "honest root remains unselected",
            data["root_payload"]["selected_source_verified"] is False
            and data["root_payload"]["claims_selected_source"] is False
            and validation["honest_root_all_pass"] is False,
            data["root_payload"],
        ),
        check(
            "formal lift algebra tested",
            validation["formal_lift_lower_validators_all_pass"] is True,
            validation["formal_lift_diagnostic"],
        ),
        check(
            "formal lift not proof",
            interp["proof_promotion_allowed"] is False
            and cert["proof_promotion_allowed"] is False
            and data["formal_lift_payload"]["claims_selected_source"] is False,
            interp,
        ),
        check(
            "target fitting excluded",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["observed_physical_data_used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "selector gap isolated",
            data["what_closes_now"]["selected_source_gap_isolated"] is True
            and data["what_remains_open"]["actual_selected_hym_strominger_source"] is True
            and data["what_remains_open"]["quotient_valid_selected_galerkin_basis_BN"] is True,
            data["what_remains_open"],
        ),
        check(
            "closure not claimed",
            cert["closure_claimed"] is False
            and data["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert["primary_next_artifact"],
        ),
        check(
            "note records diagnostic scope",
            "The first-run manifest is now filled" in note
            and "lifted flags are not promoted" in note
            and "Next artifact: `MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Route-C/Strominger Galerkin first-run audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
