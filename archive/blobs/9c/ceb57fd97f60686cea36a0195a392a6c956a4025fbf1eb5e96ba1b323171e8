"""Audit the selected correction-source or full-response emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    red = data["reduction"]
    diag = data["diagnostic_representative_support_only"]
    payload = data["required_payload"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("diagnostic splitter support", red["diagnostic_splitter_exists"] is True and red["diagnostic_splitter_not_promoted"] is True and diag["candidate_count"] > 0, red),
        check("diagnostic tests nonzero", diag["ckm_commutator_norm_sq"] > 0 and diag["pmns_commutator_norm_sq"] > 0 and diag["cp_odd_trace_commutator_cubed_imag"] != 0, diag),
        check("primitive route retired", red["primitive_only_span_counterexample"] is True and red["strict_primitive_search_found_no_legal_emission"] is True, red),
        check("selected emission open", cert["selected_correction_matrix_source_closed"] is False and cert["selected_full_response_emission_closed"] is False, cert),
        check("payload interface complete", set(payload) == {"selected_source_certificate", "nonidentity_rho_E", "quotient_valid_B_N", "selected_D_E_Riesz_Green_dotD", "selected_deltaTheta_C1_solution", "primitive_C1_contractions_or_full_response_matrices", "b_selected_or_homogeneous_zero_theorem"} and all(item["current_status"] == "open" for item in payload.values()), payload),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records nonidentity rhoE BN", "non-identity `rho_E`" in note and "quotient-valid non-invariant `B_N`" in note and "support only" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C selected correction-source/full-response emission audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
