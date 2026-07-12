"""Audit the U1/Y quotient-determinant algebraic lemma gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_quotientdeterminant_lemma.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_quotientdeterminant_lemma_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_QuotientDeterminant_Lemma_v1.md"

STATUS = "ELECTROWEAK_U1Y_QUOTIENT_DETERMINANT_LEMMA_PROVED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Electroweak_U1Y_Factorized_ThresholdOperator_SourceEmission_or_SU2_Cancellation_v1"


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
    spectrum = data["quotient_positive_spectrum"]
    decision = data["decision"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("rank accounting", data["rank_accounting"]["rank3_carrier"] == 3 and data["rank_accounting"]["quotient_rank"] == 2 and data["rank_accounting"]["quotient_weight"] == "2/3", data["rank_accounting"]),
        check("quotient multiplicities", [row["quotient_multiplicity"] for row in spectrum] == [8, 8] and [row["rank3_multiplicity"] for row in spectrum] == [12, 12], spectrum),
        check("logdet value", abs(data["quotient_logdet"]["numeric"] - 29.201650332199108) < 1e-12 and data["quotient_logdet"]["equals_scalar_weighted_rank3_logdet"] is True, data["quotient_logdet"]),
        check("lemma proved algebraically", data["algebraic_lemma"]["proved"] is True and decision["algebraic_quotient_determinant_lemma_proved"] is True, data["algebraic_lemma"]),
        check("source still open", decision["factorized_threshold_operator_source_emitted"] is False and data["still_open"]["source_emits_factorized_threshold_operator"] is True, data["still_open"]),
        check("lambda still open", decision["lambda_12_closed"] is False and decision["same_scheme_SU2_row_or_cancellation_closed"] is False, decision),
        check("guardrails", all(value is False for value in guardrails.values()), guardrails),
        check("note records no overclaim", "does not prove" in note and "No electroweak data" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y quotient-determinant lemma audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
