"""Audit the selected S3 differential-cohomology source certificate artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_s3_differential_cohomology_source_certificate.json"
DATA = REPO / "candidate_data" / "selected_s3_differential_cohomology_source_certificate.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_S3_Differential_Cohomology_Source_Certificate_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_s3_differential_cohomology_source_certificate.py"


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
    packet = data["selected_source_packet"]
    guardrails = data["guardrail_transfer"]
    imported = data["imported_results"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_S3_DIFFERENTIAL_COHOMOLOGY_SOURCE_CERTIFICATE_CLOSED_OPERATOR_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("previous frontier matches", imported["previous_frontier"]["next_required_artifact"] == "MTT_Selected_S3_Differential_Cohomology_Source_Certificate_v1", imported["previous_frontier"]),
        check("q79 closure imported", imported["q79_s3_class_restriction_closure"]["status"] == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN", imported["q79_s3_class_restriction_closure"]["status"]),
        check("selected flat class", gates["selected_s3_flat_Deligne_class_imported"] is True and packet["fixed_differential_cohomology_class"] is True, packet),
        check("pullback table", gates["selected_s3_pullback_table_imported"] is True and packet["S3_pullback_table_supplied"] is True, packet),
        check("central cocycle", gates["map_to_qutrit_central_cocycle_verified"] is True and packet["map_to_qutrit_central_cocycle_verified"] is True, packet),
        check("Freed-Witten closed", gates["smooth_Freed_Witten_cancellation_closed"] is True and packet["smooth_Freed_Witten_cancellation_verified"] is True, packet),
        check("block projectors retained", gates["block_projector_retention_closed"] is True and packet["block_sector_projector_retention_closed"] is True, packet),
        check("selected packet validator passes", gates["selected_packet_validator_passes"] is True and data["validator_result"]["exit_code"] == 0, data["validator_result"]),
        check("guardrails preserve operator frontier", guardrails["claims_selected_D_E_dotD_constructed"] is False and guardrails["claims_visible_operator_source_constructed"] is False, guardrails),
        check("guardrails no fitting", guardrails["uses_observed_flavor_data"] is False and guardrails["uses_benchmark_flavor_entries"] is False, guardrails),
        check("operator still open", gates["selected_visible_operator_source_constructed"] is False and cert["what_remains_open"]["selected_visible_Green_Schwarz_operator_source"] is True, cert),
        check("DE still open", gates["selected_DE_dotD_Riesz_Green_constructed"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Visible_Green_Schwarz_Operator_Source_v1", data["next_required_artifact"]),
        check("note records closure and frontier", "fixed differential-cohomology class: `True`" in note and "selected_visible_Green_Schwarz_operator_source" in note, NOTE),
    ]
    print("\nMTT selected S3 differential-cohomology source certificate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
