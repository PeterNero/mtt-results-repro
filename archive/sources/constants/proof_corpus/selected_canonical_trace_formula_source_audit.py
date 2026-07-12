"""Audit the selected canonical trace formula source payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_canonical_trace_formula_source.py"
PACKET = DATA / "selected_canonical_trace_formula_source.candidate.json"
TEMPLATE = DATA / "selected_canonical_trace_formula_source.payload.template.json"
CERT = CERTS / "selected_canonical_trace_formula_source_certificate.json"
NOTE = ROOT / "proof_corpus" / "SelectedCanonicalTraceFormulaSource_v1.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load_json(PACKET)
    template = load_json(TEMPLATE)
    cert = load_json(CERT)
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

    expected = "MISSING_SOURCE_PAYLOAD_ADDED_TRACE_EQUALITY_STILL_OPEN"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("template open", template["status"] == "OPEN_FILL_REQUIRED", template)
    required = template["required_fields"]
    check(
        "required payload fields",
        set(required)
        == {
            "canonical_active_metric_normalization_source",
            "projective_flat_connection_to_DE_source",
            "H_rank_two_shift_source",
            "same_source_no_substitution_certificate",
        },
        required,
    )
    slots = packet["slots"]
    check(
        "closed source prefix retained",
        slots["T0_selected_smooth_source"]["status"] == "CLOSED"
        and slots["T1_functorial_trace_domain"]["status"] == "CLOSED",
        slots,
    )
    check(
        "formula closed but source open",
        slots["T3_canonical_fourier_metric_formula"]["status"]
        == "FORMULA_CLOSED_SOURCE_SELECTION_OPEN"
        and slots["T4_H_rank_two_zero_cluster_shift"]["status"]
        == "FORMULA_CLOSED_SOURCE_SELECTION_OPEN",
        slots,
    )
    check(
        "same source binding open",
        slots["T5_same_source_binding"]["status"] == "OPEN",
        slots["T5_same_source_binding"],
    )
    check(
        "source lemma not overclaimed",
        not packet["source_lemma"]["proved"]
        and cert["guardrails"]["does_not_claim_source_lemma_proved"],
        packet["source_lemma"],
    )
    check(
        "closure consequence exact",
        packet["closure_if_payload_supplied"]["selected_eta_N"] == 1.0
        and packet["closure_if_payload_supplied"]["gap_layer_closes"]
        and packet["closure_if_payload_supplied"]["dotD_C1_still_separate"],
        packet["closure_if_payload_supplied"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records missing payload", "same_source_no_substitution_certificate" in note, NOTE)

    print("\nSelected canonical trace formula source audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
