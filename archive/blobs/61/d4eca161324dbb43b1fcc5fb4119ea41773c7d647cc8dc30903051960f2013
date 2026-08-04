"""Audit the determinant-functional source theorem or selected A_base emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_DeterminantFunctional_SourceTheorem_or_SelectedAbaseEmission_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_DETERMINANTFUNCTIONAL_OR_SELECTED_ABASE_EMISSION_GATE_BUILT_VALUES_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1"


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
    check("cert status", cert["status"] == EXPECTED_STATUS, cert["status"])
    check("next", candidate["decision"]["next_required_artifact"] == EXPECTED_NEXT, candidate["decision"])

    route_a = candidate["route_a_selected_abase_emission"]
    route_b = candidate["route_b_direct_bn_functional"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]
    payload = candidate["minimal_next_payload"]

    check("route A support present", route_a["already_available"]["matrix_constructed"] is True and route_a["already_available"]["Pperp_quotient_functor_closed_for_tensor_identity"] is True, route_a)
    check("route A still open", route_a["route_closed_now"] is False and route_a["missing_selected_fields"]["factorized_matrix_emitted_by_prior_source"] is False, route_a)
    check("route B support present", route_b["already_available"]["selected_27mode_DE_gap_trace_equality"] is True and route_b["already_available"]["Pperp_domain_policy_closed"] is True, route_b)
    check("route B still open", route_b["route_closed_now"] is False and route_b["missing_selected_fields"]["determinant_functional_source_theorem_found"] is False, route_b)
    check("recommended route B", candidate["route_comparison"]["recommended_next_route"] == "direct_selected_determinant_functional_on_BN", candidate["route_comparison"])

    check("payload written", decision["minimal_selected_finite_part_payload_written"] is True and payload["schema"].endswith(".v1"), payload)
    check("conditional logdet carried only", abs(decision["conditional_quotient_logdet_carried"] - 29.201650332199108) < 1e-12 and decision["conditional_quotient_logdet_promoted"] is False, decision)
    check("no closures", decision["route_a_selected_abase_emission_closed"] is False and decision["route_b_direct_bn_functional_closed"] is False, decision)
    check("no p/lambda closure", decision["selected_p_a_promoted"] is False and decision["lambda_12_closed"] is False, decision)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note route split", "Both legal closure routes" in note and "Route B is ranked" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack determinant-functional/A_base emission audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
