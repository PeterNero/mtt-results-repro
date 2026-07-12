"""Audit selected correction/full-response frontier import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_selected_correction_fullresponse_frontier.py"
PACKET = ROOT / "candidate_data" / "selected_correction_fullresponse_frontier_import.candidate.json"
CERT = ROOT / "certificates" / "selected_correction_fullresponse_frontier_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Correction_FullResponse_Frontier_Import_v1.md"

STATUS = "SELECTED_CORRECTION_FULLRESPONSE_FRONTIER_REDUCED_RHOE_BN_DELTATHETA_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    upstream = packet["upstream_packet"]
    red = upstream["reduction"]
    diag = upstream["diagnostic_representative_support_only"]
    check(
        "diagnostic splitter remains support only",
        red["diagnostic_splitter_exists"] is True
        and red["diagnostic_splitter_not_promoted"] is True
        and packet["upstream_certificate"]["diagnostic_splitter_recorded_support_only"] is True,
        red,
    )
    check(
        "diagnostic tests are nonzero",
        all(value > 0.0 for value in diag["mass_split_traceless_norm_sq"].values())
        and diag["ckm_commutator_norm_sq"] > 0.0
        and diag["pmns_commutator_norm_sq"] > 0.0
        and diag["cp_odd_trace_commutator_cubed_imag"] != 0.0,
        diag,
    )
    check(
        "primitive/formal routes rejected",
        red["primitive_only_span_counterexample"] is True
        and red["strict_primitive_search_found_no_legal_emission"] is True
        and red["formal_lift_rejected_as_proof"] is True,
        red,
    )
    check(
        "selected emission remains open",
        packet["upstream_certificate"]["selected_correction_matrix_source_closed"] is False
        and packet["upstream_certificate"]["selected_full_response_emission_closed"] is False,
        packet["upstream_certificate"],
    )
    check(
        "payload contract complete",
        set(packet["required_payload"])
        == {
            "selected_source_certificate",
            "nonidentity_rho_E",
            "quotient_valid_B_N",
            "selected_D_E_Riesz_Green_dotD",
            "selected_deltaTheta_C1_solution",
            "primitive_C1_contractions_or_full_response_matrices",
            "b_selected_or_homogeneous_zero_theorem",
        }
        and all(item["current_status"] == "open" for item in packet["required_payload"].values()),
        packet["required_payload"],
    )
    check(
        "frontier advances to rhoE/BN",
        packet["frontier_update"]["old_next"]
        == "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"
        and packet["frontier_update"]["current_next"] == NEXT,
        packet["frontier_update"],
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in ("support only", "selected non-identity", "quotient-valid `B_N`", "deltaTheta/C1"):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nSelected correction/full-response frontier import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
