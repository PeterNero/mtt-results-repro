"""Audit the electroweak gauge-kinetic normalization and RG-scheme route gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_gaugekinetic_normalization_and_rg_scheme.py"
DATA = ROOT / "candidate_data" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json"
CERT = ROOT / "certificates" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_strominger_electroweak_threshold_kernel.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1.md"

STATUS = "ELECTROWEAK_GAUGEKINETIC_RG_ROUTE_SELECTED_VALUES_OPEN"
NEXT = "Selected_Heterotic_Strominger_Electroweak_Threshold_Kernel_v1"


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
    routes = data["routes"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("primary route selected", decision["strict_primary_route_selected"] == "B_flux_strominger_threshold" and routes["B_flux_strominger_threshold"]["accepted_as_no_knob_route"] is True, routes["B_flux_strominger_threshold"]),
        check("values still open", decision["gaugekinetic_normalization_closed"] is False and decision["matching_scale_closed"] is False and decision["RG_scheme_closed"] is False, decision),
        check("internal threshold carried", abs(decision["internal_lambda_12_value"] - 2.6179362173268497) < 1e-12 and abs(decision["internal_Delta_G12_value"] - 0.08450302790361214) < 1e-12, decision),
        check("m theory slot not promoted", routes["M_theory_shared_anchor"]["accepted_as_gauge_normalization_now"] is False, routes["M_theory_shared_anchor"]),
        check("theta scale rejected", routes["Theta_matching_scale"]["accepted_as_mu_match_now"] is False, routes["Theta_matching_scale"]),
        check("primitive not no-knob", routes["A_primitive_common_normalization"]["accepted_as_no_knob"] is False, routes["A_primitive_common_normalization"]),
        check("template exact", template["status"] == "OPEN_SELECTED_HETEROTIC_STROMINGER_EW_KERNEL_REQUIRED" and template["matching_payload"]["mu_match"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note names route", "heterotic/Strominger threshold-kernel route" in note and NEXT in note, NOTE),
    ]
    print("\nSelected electroweak gauge-kinetic/RG scheme route audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
