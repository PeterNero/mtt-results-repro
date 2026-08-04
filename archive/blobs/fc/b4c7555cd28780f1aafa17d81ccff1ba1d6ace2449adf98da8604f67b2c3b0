"""Audit the electroweak Qa-stack source-identity test from terminal/gerbe support."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SourceIdentity_From_TerminalMonad_or_GerbeSource_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_SOURCEIDENTITY_TERMINAL_GERBE_TESTED_THRESHOLD_ROW_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_ThresholdOperator_From_NonIdentityRhoE_QuotientBN_Fill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object = "") -> None:
    if not condition:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    check("script reruns", proc.returncode == 0, proc.stdout)

    candidate = load(OUTPUT_DATA)
    cert = load(OUTPUT_CERT)
    note = OUTPUT_NOTE.read_text(encoding="utf-8")

    check("status", candidate["status"] == EXPECTED_STATUS, candidate["status"])
    check("cert", cert["status"] == EXPECTED_STATUS, cert["status"])
    check("next", candidate["decision"]["next_required_artifact"] == EXPECTED_NEXT, candidate["decision"])

    support = candidate["support_upgrades"]
    req = candidate["threshold_identity_requirements"]
    routes = candidate["route_tests"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]

    check("terminal support imported", support["terminal_ordered_orientation_closed"] is True and support["functional_operator_emission_closed"] is True, support)
    check("alpha support imported", support["alpha1_driver_verified"] is True and support["honest_dotD_alpha1_validator_closed"] is True, support)
    check("threshold row still missing", req["exact_A_base_tensor_I3_emitted_as_threshold_operator"] is False, req)
    check("Pic0 and nonidentity still open", req["operator_layer_Pic0_or_torsion_gerbe_closed"] is False and req["nonidentity_rhoE_quotient_valid_BN_filled"] is False, req)
    check("source selection still open", req["selected_factorized_rank3_carrier"] is False and req["selected_sector_maps_and_shared_line"] is False, req)
    check("route tests not accepted", all(route["accepted"] is False for route in routes.values()), routes)
    check("best next route", decision["best_next_route"] == "nonidentity_rhoE_quotientBN_route", decision)
    check("no closure", decision["source_identity_closed"] is False and decision["lambda_12_closed"] is False, decision)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note boundary", "functional matter-slot operators" in note and "gauge-threshold row" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack source-identity from terminal/gerbe audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
