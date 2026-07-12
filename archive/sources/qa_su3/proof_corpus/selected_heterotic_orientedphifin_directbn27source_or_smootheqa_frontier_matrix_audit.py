"""Audit direct BN27 source versus smooth E_Qa frontier matrix."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_payload_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectBN27Source_or_SmoothEQa_FrontierMatrix_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_OR_SMOOTHEQA_FRONTIER_REDUCED_SELECTED_A_OR_DIRECT_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SelectedBundleConnectionA_or_DirectBN27SourceEmission_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    direct = data["routes"]["direct_BN27_source_theorem"]
    smooth = data["routes"]["smooth_E_Qa_quotient"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("projective lift retired", decision["projective_rhoE_lift_retired_for_BN27_threshold"] is True and cert["projective_rhoE_lift_retired_for_BN27_threshold"] is True, decision)
    check("direct support present but source absent", direct["support"]["full_BN27_table_materialized"] is True and direct["missing"]["direct_selected_carrier_packet_found_in_corpus"] is False, direct)
    check("direct source remains open", direct["closed"] is False and direct["missing"]["same_source_BN27_source_theorem"] is False, direct)
    check("smooth geometry present", smooth["support"]["bismut_geometry_payload_filled"] is True and smooth["support"]["R_plus_curvature_filled"] is True, smooth)
    check("smooth A absent", smooth["closed"] is False and smooth["missing"]["smooth_selected_bundle_A_packet_found_in_corpus"] is False and smooth["missing"]["selected_A_or_rhoE"] is False, smooth)
    check("contract has two payload lanes", set(contract) >= {"direct_BN27_source_payload", "smooth_EQa_payload", "acceptance_tests"}, contract)
    check("contract keeps values open", all(value is None for value in contract["direct_BN27_source_payload"].values()) and all(value is None for value in contract["smooth_EQa_payload"].values()), contract)
    check("no closures", decision["direct_BN27_source_closed"] is False and decision["smooth_EQa_quotient_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records frontier", NEXT in note and str(CONTRACT.relative_to(ROOT)) in note and "projective_rhoE_lift_retired_for_BN27_threshold = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct BN27 or smooth E_Qa frontier audit passed")


if __name__ == "__main__":
    main()
