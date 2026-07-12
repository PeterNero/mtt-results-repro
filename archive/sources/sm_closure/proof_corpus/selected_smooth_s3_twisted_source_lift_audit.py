"""Audit the selected smooth S3 twisted-source lift artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_smooth_s3_twisted_source_lift_certificate.json"
DATA = REPO / "candidate_data" / "selected_smooth_s3_twisted_source_lift.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_smooth_s3_twisted_source_lift.py"


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
    imported = data["imported_results"]
    contract = data["smooth_lift_packet_contract"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    required = set(contract["must_supply_now"])
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_SMOOTH_S3_TWISTED_SOURCE_LIFT_BUILT_SOURCE_CERTIFICATE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("previous frontier matches", imported["previous_frontier"]["next_required_artifact"] == "MTT_Selected_Smooth_S3_Twisted_Source_Lift_v1", imported["previous_frontier"]),
        check("finite prerequisites assembled", gates["finite_prerequisites_assembled"] is True and imported["finite_s3_cp"]["finite_S3_CP_cancellation_closed"] is True, imported["finite_s3_cp"]),
        check("good cover not knob", gates["good_cover_not_physical_knob"] is True and imported["cover_reduction"]["good_cover_execution_scaffold"] is True, imported["cover_reduction"]),
        check("validator confirms open", gates["template_validator_confirms_open"] is True and data["template_validator_result"]["exit_code"] == 2, data["template_validator_result"]),
        check("smooth source still unselected", gates["smooth_source_selected"] is False and imported["smooth_lift_attempt"]["selected_smooth_S3_source_constructed"] is False, imported["smooth_lift_attempt"]),
        check("fixed differential class absent", gates["fixed_differential_cohomology_class_supplied"] is False and imported["s3_source_packet_attempt"]["selected_S3_source_constructed"] is False, imported["s3_source_packet_attempt"]),
        check("smooth FW/projector still open", gates["smooth_S3_Freed_Witten_closed"] is False and gates["smooth_projector_retention_closed"] is False, gates),
        check("DE bridge still open", gates["selected_DE_dotD_Riesz_Green_constructed"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("contract has required source fields", {"source_selected_by_mtt", "fixed_differential_cohomology_class", "restricts_to_selected_S3_worldvolume", "map_to_qutrit_central_cocycle_verified"}.issubset(required), contract),
        check("downstream listed", "selected D_E" in contract["downstream_after_lift"] and "selected dotD_alpha1" in contract["downstream_after_lift"], contract["downstream_after_lift"]),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_S3_Differential_Cohomology_Source_Certificate_v1", data["next_required_artifact"]),
        check("note records source certificate", "selected smooth differential-cohomology" in note and "exit_code=2" in note, NOTE),
    ]
    print("\nMTT selected smooth S3 twisted-source lift audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
