"""Audit the HYM full-quotient spectrum / OU-Hessian fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_FillAttempt_v1.md"

STATUS = "HETEROTIC_HYM_FULLQUOTIENT_OR_OUHESSIAN_FILLATTEMPT_PARTIAL_SUPPORT_SOURCEIDENTITY_OPEN"
NEXT = "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    report = load(REPORT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    lane_A = report["lane_A_fill"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and report["status"] == "PARTIAL_SUPPORT_VALUES_OPEN", (data["status"], cert["status"], report["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("fill attempt built", decision["fill_attempt_built"] is True and decision["lane_A_advanced_by_importing_rejection_evidence"] is True, decision)
    check("support imported", report["source_backed_support"]["positive_logdet_prime"] == "log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))" and report["source_backed_support"]["R_plus_nonzero_components"] == 68, report["source_backed_support"])
    check("lane A remains open", decision["full_quotient_spectrum_closed"] is False and len(report["open_leaves"]) == 9 and report["filled_leaves"] == [], report["open_leaves"])
    check("invariant block not promoted", lane_A["proof_invariant_EndC3_block_is_or_is_not_complete_domain"]["filled"] is False and data["guardrails"]["does_not_promote_invariant_block_to_full_domain"] is True, lane_A["proof_invariant_EndC3_block_is_or_is_not_complete_domain"])
    check("Rplus not promoted", lane_A["bundle_curvature_F_A_components"]["filled"] is False and data["guardrails"]["does_not_promote_Rplus_to_FA"] is True, lane_A["bundle_curvature_F_A_components"])
    check("standard embedding retired", decision["standard_embedding_selected_now"] is False and decision["standard_embedding_retired_as_current_proof_source"] is True and report["rejected_shortcuts"]["standard_embedding"]["retired_as_current_proof_source"] is True, report["rejected_shortcuts"]["standard_embedding"])
    check("PhiFin support not promoted", decision["D_E_Riesz_Green_gap_support_imported"] is True and decision["heterotic_QaSU3_source_identity_proved"] is False and report["rejected_shortcuts"]["phifin_import"]["heterotic_QaSU3_source_identity_proved"] is False, report["rejected_shortcuts"]["phifin_import"])
    check("no operator closure", decision["explicit_bundle_connection_solved"] is False and decision["E_Qa_computed"] is False and decision["computed_threshold_value"] is False, decision)
    check("other lanes remain legal open", report["other_lanes"]["lane_B_OU_or_Strominger_Hessian_scale"]["legal"] is True and report["other_lanes"]["lane_C_local_system_torsion"]["closed_now"] is False, report["other_lanes"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and decision["closure_claimed"] is False, cert)
    check("note records theorem", NEXT in note and str(REPORT.relative_to(ROOT)) in note and "Theorem" in note, NOTE)

    print("\nSelected heterotic HYM full-quotient / OU-Hessian fill-attempt audit")


if __name__ == "__main__":
    main()
