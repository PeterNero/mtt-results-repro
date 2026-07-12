"""Audit the electroweak Qa-stack quotient-functor/A_base identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_quotient_functor_and_abase_identity.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_quotient_functor_and_abase_identity.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_quotient_functor_and_abase_identity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_QuotientFunctor_and_AbaseIdentity_Theorem_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_QUOTIENT_FUNCTOR_CONDITIONAL_ABASE_IDENTITY_SOURCE_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_DeterminantFunctional_SourceTheorem_or_SelectedAbaseEmission_v1"


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

    alg = candidate["algebraic_functor"]
    tests = candidate["source_tests"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]

    check("Pperp closed", alg["Pperp_policy_closed_index_only"] is True and alg["shared_vector_selected"] is True, alg)
    check("quotient lemma closed", alg["tensor_identity_quotient_lemma_proved"] is True, alg)
    check("matrix packet present", alg["factorized_matrix_constructed"] is True and alg["quotient_matrix_constructed"] is True, alg)
    check("conditional logdet stable", abs(alg["quotient_logdet"] - 29.201650332199108) < 1e-12, alg)

    check("BN functor remains open", tests["selected_BN_to_tensor_identity_functor"]["passed"] is False, tests)
    check("A_base emission remains open", tests["exact_A_base_tensor_I3_emitted_by_source"]["passed"] is False, tests)
    check("Pperp same-source support only", tests["same_source_Pperp_domain"]["passed"] is True, tests)
    check("determinant theorem open", tests["determinant_functional_source_theorem"]["passed"] is False, tests)
    check("weights scale open", tests["Qa_stack_weights_and_scale"]["passed"] is False, tests)

    check("conditional functor closed", decision["tensor_identity_quotient_functor_closed"] is True, decision)
    check("selected identity not closed", decision["selected_BN_to_threshold_functor_closed"] is False and decision["A_base_tensor_I3_identity_closed"] is False, decision)
    check("no p/lambda closure", decision["selected_p_a_promoted"] is False and decision["lambda_12_closed"] is False, decision)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note does not overpromote", "does not yet prove" in note and "not promoted as selected" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack quotient functor/A_base identity audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
