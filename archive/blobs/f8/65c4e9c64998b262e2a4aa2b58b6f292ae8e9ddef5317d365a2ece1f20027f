"""Audit the heterotic source-certificate or direct-operator-emission search gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_sourcecertificate_or_direct_operator_emission_search.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_SourceCertificate_or_DirectOperatorEmission_Search_v1.md"

STATUS = "HETEROTIC_SOURCECERTIFICATE_OR_DIRECT_OPERATOR_EMISSION_SEARCH_BUILT_TORSIONAL_E_OR_OU_NEXT"
NEXT = "Selected_Heterotic_TorsionalEndomorphism_or_OU_ModeWeights_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    routes = data["route_tests"]
    scans = data["source_scans"]
    decision = data["decision"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("source certificate not found", decision["source_certificate_found"] is False and routes["A_source_certificate_search"]["closes_now"] is False, routes["A_source_certificate_search"]),
        check("direct operator not found", decision["direct_operator_emission_found"] is False and routes["B_direct_operator_emission"]["closes_now"] is False, routes["B_direct_operator_emission"]),
        check(
            "torsional route primary",
            decision["primary_next_route"] == "torsional_endomorphism_or_OU_mode_weights"
            and any("torsional Weitzenbock endomorphism" in item for item in routes["B_direct_operator_emission"]["must_compute_next"]),
            decision,
        ),
        check("diagonal payload only support", routes["C_diagonal_rank2_import"]["closes_now"] is False and decision["diagonal_rank2_support_imported"] is True, routes["C_diagonal_rank2_import"]),
        check("source scans see OU clue", scans["hym_ou_completion"]["terms"]["OU weights"] is True and scans["hym_ou_completion"]["terms"]["mu selected: no"] is True, scans["hym_ou_completion"]),
        check("template open", template["torsional_endomorphism_lane"]["Weitzenbock_E_Qa_on_uE_one_forms"] is None and template["ou_mode_weight_lane"]["gamma_nk_weights"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "torsional Weitzenbock endomorphism or OU mode-weight packet" in note, NOTE),
    ]
    print("\nSelected heterotic source-certificate or direct-operator-emission search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
