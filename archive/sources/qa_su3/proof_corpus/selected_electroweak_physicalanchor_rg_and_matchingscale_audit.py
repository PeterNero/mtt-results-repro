"""Audit the electroweak physical-anchor, RG, and matching-scale gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_physicalanchor_rg_and_matchingscale.py"
DATA = ROOT / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"
CERT = ROOT / "certificates" / "selected_electroweak_physicalanchor_rg_and_matchingscale_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1.md"

STATUS = "ELECTROWEAK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_GAUGE_ANCHOR_RG_OPEN"
NEXT = "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1"


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
    decision = data["decision"]
    closed = data["closed_now"]
    routes = data["route_tests"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("internal lambda remains closed", closed["internal_lambda_12"] is True and abs(decision["internal_lambda_12_value"] - 2.6179362173268497) < 1e-12, decision),
        check("internal delta remains closed", abs(decision["internal_Delta_G12_value"] - 0.08450302790361214) < 1e-12, decision),
        check("omega convention closed but not anchor", closed["Omega0_symbol_convention_chi_equals_1"] is True and decision["physical_gauge_action_anchor_closed"] is False, closed),
        check("GR one-anchor not EW anchor", routes["GR_one_anchor_family"]["accepted_as_electroweak_anchor_now"] is False, routes["GR_one_anchor_family"]),
        check("Omega0 not mu_match", routes["Omega0_as_matching_scale"]["accepted_now"] is False, routes["Omega0_as_matching_scale"]),
        check("internal K not physical", routes["internal_K_gauge_equals_one"]["accepted_as_physical_anchor"] is False, routes["internal_K_gauge_equals_one"]),
        check("template requires source fields", template["status"] == "OPEN_SELECTED_PHYSICAL_GAUGE_ANCHOR_RG_REQUIRED" and template["must_emit"]["rg_scheme"]["scheme"] is None, template),
        check("physical closure still open", decision["matching_scale_closed"] is False and decision["RG_scheme_closed"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records next theorem", NEXT in note and "measured electroweak comparison" in note, NOTE),
    ]
    print("\nSelected electroweak physical-anchor/RG/matching-scale audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
