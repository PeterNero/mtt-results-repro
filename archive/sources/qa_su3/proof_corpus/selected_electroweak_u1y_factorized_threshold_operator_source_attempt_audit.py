"""Audit the factorized U1/Y threshold-operator source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_factorized_threshold_operator_source_attempt.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt_certificate.json"
MATRIX = REPO / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_Attempt_v1.md"

STATUS = "ELECTROWEAK_U1Y_FACTORIZED_THRESHOLD_OPERATOR_CONSTRUCTED_SELECTION_PROVENANCE_OPEN"
NEXT = "Selected_Electroweak_U1Y_HyperchargeIndexWeights_and_TypedConventionMap_v1"


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
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("matrix dimensions", matrix["raw_operator"]["dimension"] == 24 and matrix["quotient_operator"]["dimension"] == 16, (matrix["raw_operator"]["dimension"], matrix["quotient_operator"]["dimension"])),
        check("factorization matches", decision["factorization_matches_27mode_spectrum"] is True and matrix["factorization_checks"]["quotient_multiplicities"] == [8, 8], matrix["factorization_checks"]),
        check("logdet exact", abs(decision["quotient_logdet"] - 29.201650332199108) < 1e-12, decision["quotient_logdet"]),
        check("operator constructed not promoted", decision["factorized_operator_matrix_constructed"] is True and decision["selected_source_emission_closed"] is False, decision),
        check("source identity precise", data["source_identity"]["operator_prefix_selected_by_mtt"] is True and data["source_identity"]["factorized_matrix_emitted_by_prior_source"] is False, data["source_identity"]),
        check("weights and convention open", decision["hypercharge_index_Dynkin_weights_closed"] is False and decision["typed_convention_map_closed"] is False, decision),
        check("lambda open", decision["lambda_12_closed"] is False and cert["open"]["lambda_12"] is True, decision),
        check("guardrails", all(value is False for value in guardrails.values()), guardrails),
        check("note records provenance blocker", "provenance and typing" in note and "does not close" in note.lower(), NOTE),
    ]
    print("\nSelected electroweak U1/Y factorized threshold-operator source attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
