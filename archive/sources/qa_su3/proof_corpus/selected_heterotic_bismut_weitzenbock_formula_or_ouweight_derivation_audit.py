"""Audit the Bismut-Weitzenbock formula or OU-weight derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_bismut_weitzenbock_tensor_payload.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_BismutWeitzenbock_Formula_or_OUWeightDerivation_v1.md"

STATUS = "HETEROTIC_BISMUT_WEITZENBOCK_FORMULA_OR_OUWEIGHT_DERIVATION_BUILT_TENSOR_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1"


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
    contract = data["contract"]
    routes = data["route_tests"]
    decision = data["decision"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("known geometry carried", "eight_A_squared" in contract["known_inputs"] and contract["known_inputs"]["metric_weighted_logdet_monotone_on_samples"] is True, contract["known_inputs"]),
        check("tensor payload named", "Bismut connection coefficients Gamma^+" in contract["minimal_tensor_payload"] and "bundle connection A and curvature F_A in selected gauge" in contract["minimal_tensor_payload"], contract["minimal_tensor_payload"]),
        check("E and OU open", decision["E_Qa_computed"] is False and decision["OU_weights_computed"] is False and routes["bismut_weitzenbock_formula_lane"]["E_Qa_computed"] is False, decision),
        check("template open", template["operator_contract"]["E_Qa_matrix"] is None and template["ou_derivation_alternative"]["gamma_nk_inverse_table"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "Bismut/Weitzenbock zero-order block E_Qa" in note and "direct finite operator emission" in note, NOTE),
    ]
    print("\nSelected heterotic Bismut-Weitzenbock formula or OU-weight derivation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
