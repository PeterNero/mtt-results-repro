"""Audit the MTT empirical equivalence ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "empirical_equivalence_ledger_certificate.json"
DATA = REPO / "candidate_data" / "empirical_equivalence_ledger.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Empirical_Equivalence_Ledger_v1.md"
SCRIPT = REPO / "scripts" / "build_empirical_equivalence_ledger.py"

REQUIRED_DOMAINS = {
    "QM measurement and records",
    "local QFT observables",
    "SM gauge and representation sector",
    "Yukawa, CP, and Higgs phenomenology",
    "GR and stress-energy coupling",
    "units and dimensionful constants",
}
REQUIRED_ROW_FIELDS = {
    "domain",
    "accepted_reference",
    "mtt_parity_requirement",
    "measured_inputs_allowed",
    "must_reproduce",
    "not_allowed",
    "status",
    "no_knob_target",
}


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    rows = data["ledger_rows"]
    domains = {row["domain"] for row in rows}
    rows_have_fields = all(REQUIRED_ROW_FIELDS.issubset(row.keys()) for row in rows)
    all_have_reproduction = all(row["must_reproduce"] and row["measured_inputs_allowed"] and row["not_allowed"] for row in rows)
    forbidden_text = " ".join(" ".join(row["not_allowed"]) for row in rows).lower()
    checks = [
        check("status", cert["status"] == "MTT_EMPIRICAL_EQUIVALENCE_LEDGER_BUILT_ACTUAL_AUDIT_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("domains complete", REQUIRED_DOMAINS.issubset(domains), domains),
        check("row fields complete", rows_have_fields, rows),
        check("reproduction obligations present", all_have_reproduction, rows),
        check("reference practice declared", gates["accepted_reference_practice_declared"] is True, gates),
        check("measured downstream", gates["measured_inputs_classified_downstream"] is True, gates),
        check("must reproduce obligations", gates["must_reproduce_obligations_declared"] is True, gates),
        check("forbidden shortcuts declared", gates["forbidden_empirical_shortcuts_declared"] is True, gates),
        check("no numeric equivalence claim", gates["actual_numeric_equivalence_computed"] is False, gates),
        check("no selected packet claim", gates["actual_selected_sm_packet_supplied"] is False, gates),
        check("no no-knob constants claim", gates["no_knob_constants_derived"] is False, gates),
        check("forbids empirical source selection", "select" in forbidden_text and "source" in forbidden_text, forbidden_text),
        check("forbids fitted thresholds", "fitting thresholds" in forbidden_text or "fitted" in forbidden_text, forbidden_text),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records open status", "does not compute the actual numerical empirical equivalence" in note and "does not claim full SM-parity closure" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_No_Knob_Upgrade_Backlog_v1", data["next_required_artifact"]),
    ]
    print("\nMTT empirical equivalence ledger audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
