"""Audit the selected S3 class restriction / projector retention artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_s3_class_restriction_projector_retention_certificate.json"
DATA = REPO / "candidate_data" / "selected_s3_class_restriction_projector_retention.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_s3_class_restriction_projector_retention.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    restriction = data["restriction_packet"]
    projectors = data["projector_retention_packet"]
    imported = data["imported_results"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_S3_CLASS_RESTRICTION_PROJECTOR_RETENTION_BUILT_SMOOTH_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("previous frontier matches", imported["previous_frontier"]["next_required_artifact"] == "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1", imported["previous_frontier"]),
        check("W3 spinC imported", gates["W3_spinC_imported_closed"] is True and imported["visible_spinc_gate"]["W3_spinC_closed"] is True, imported["visible_spinc_gate"]),
        check("ordinary DD zero retained", gates["ordinary_DD_zero_for_S1_S2_Cij_imported"] is True and set(restriction["ordinary_DD_zero_stacks"]) == {"S1", "S2"} and set(restriction["ordinary_DD_zero_matter_curves"]) == {"C12", "C23", "C31"}, restriction),
        check("S3 rank two imported", gates["S3_rank_two_active_image_imported"] is True and restriction["S3_active_image_rank_over_F3"] == 2, restriction),
        check("ordinary S3 rejected", gates["ordinary_S3_DD_zero_rejected"] is True and restriction["ordinary_S3_DD_zero"] is False, restriction),
        check("twisted S3 cancellation imported", gates["finite_twisted_S3_CP_cancellation_imported"] is True and restriction["finite_total_twisted_DD_class_zero"] is True, restriction),
        check("finite projector retained", gates["finite_block_projector_architecture_retained"] is True and projectors["finite_block_factorized_sector_maps_valid"] is True, projectors),
        check("smooth source still open", gates["smooth_s3_source_constructed"] is False and imported["smooth_s3_lift_attempt"]["selected_smooth_S3_source_constructed"] is False, imported["smooth_s3_lift_attempt"]),
        check("smooth FW still open", gates["smooth_Freed_Witten_closed"] is False and imported["smooth_s3_lift_attempt"]["smooth_S3_Freed_Witten_closed"] is False, imported["smooth_s3_lift_attempt"]),
        check("smooth projector still open", gates["smooth_projector_retention_closed"] is False and projectors["smooth_projector_retention_verified"] is False, projectors),
        check("operator still open", gates["selected_DE_dotD_Riesz_Green_constructed"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1", data["next_required_artifact"]),
        check("note records theorem", "S3 has rank-two active F_3^2 image" in note and "smooth S3 twisted-source lift" in note, NOTE),
    ]
    print("\nMTT selected S3 class restriction projector retention audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
