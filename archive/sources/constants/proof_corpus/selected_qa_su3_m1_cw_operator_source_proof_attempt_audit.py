"""Audit Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Proof_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"
SCRIPT = REPO / "scripts" / "attempt_prove_selected_qa_su3_m1_cw_operator_source.py"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Proof_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    prefix = cert["closed_prefix"]
    blockers = cert["remaining_theorem_blockers"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "CW_OPERATOR_SOURCE_PREFIX_CLOSED_FULL_THEOREM_SOURCE_CERTIFICATE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check("full theorem is not proved", cert["theorem_proved"] is False, cert["theorem_proved"])
    ok &= check("closed prefix is all true", all(prefix.values()), prefix)
    ok &= check(
        "source/C1 blockers remain",
        blockers["selected_visible_source_certificate"] is True
        and blockers["quotient_valid_BN_basis_certificate"] is True
        and blockers["honest_manifest_without_lifted_flags"] is True
        and blockers["selected_D_E_source_promotion"] is True
        and blockers["selected_dotD_source_verified"] is True
        and blockers["selected_noninvariant_C1_primitive_or_vertex"] is True
        and blockers["nonzero_C1_response_matrices"] is True,
        blockers,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_full_CW_operator_source_theorem"] is False
        and guards["claims_selected_source_promotion"] is False
        and guards["claims_selected_D_E_dotD"] is False
        and guards["claims_nonzero_C1_response"] is False
        and guards["claims_full_SM_closure"] is False,
        guards,
    )
    ok &= check(
        "note records maximal theorem and blockers",
        "The full theorem is not proved yet" in note
        and "Selected_Source_Provenance_or_BN_Basis_Certificate_then_C1_Primitive_v1" in note,
        NOTE,
    )

    print("\nSelected Qa/SU3 m1 Chern-Weil operator source proof attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
