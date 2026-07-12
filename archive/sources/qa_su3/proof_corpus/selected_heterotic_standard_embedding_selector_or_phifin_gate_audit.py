"""Audit standard-embedding retirement and Phi_fin primary gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_standard_embedding_selector_or_phifin_gate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_standard_embedding_selector_or_phifin_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_StandardEmbeddingSelector_or_PhiFin_Gate_v1.md"

STATUS = "HETEROTIC_STANDARD_EMBEDDING_SELECTOR_RETIRED_PHIFIN_DIRECT_OPERATOR_PRIMARY"


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
    cert = load(CERT)

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("monad topology retained", data["monad_topology"]["c1_zero"] and data["monad_topology"]["c2_zero"] and data["monad_topology"]["c3_integral_equals_6"], data["monad_topology"])
    check("standard embedding retired only for current source", data["decision"]["standard_embedding_retired_as_current_proof_source"] is True and data["guardrails"]["declares_standard_embedding_false_in_general"] is False, data["standard_embedding_evaluation"])
    check("conditional route not promoted", data["standard_embedding_evaluation"]["conditional_packet_valid"] is True and data["standard_embedding_evaluation"]["selected_now"] is False, data["standard_embedding_evaluation"])
    check("phifin primary but open", data["decision"]["phifin_or_direct_operator_primary"] is True and data["phifin_direct_operator_evaluation"]["selected_now"] is False, data["phifin_direct_operator_evaluation"])
    check("operator still open", data["decision"]["E_Qa_computed"] is False and data["decision"]["direct_finite_operator_emitted"] is False, data["decision"])
    check("minimal payload includes finite operator", "D_E action on the selected quotient domain" in data["phifin_direct_operator_evaluation"]["minimal_payload"], data["phifin_direct_operator_evaluation"]["minimal_payload"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records primary route", "Phi_fin / direct finite operator emission" in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic standard-embedding selector or Phi_fin gate audit")


if __name__ == "__main__":
    main()
