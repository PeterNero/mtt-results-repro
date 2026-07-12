"""Audit the torsional-endomorphism or OU-mode-weights value attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_torsional_endomorphism_or_ou_mode_weights.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_TorsionalEndomorphism_or_OU_ModeWeights_v1.md"

STATUS = "HETEROTIC_TORSIONAL_ENDOMORPHISM_OR_OU_MODEWEIGHTS_ATTEMPT_PARTIAL_GEOMETRY_FILLED_E_OU_OPEN"
NEXT = "Selected_Heterotic_BismutWeitzenbock_Formula_or_OUWeightDerivation_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


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
    note = NOTE.read_text(encoding="utf-8")
    inv = data["computed_invariants"]
    flags = data["required_flags"]
    decision = data["decision"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("8A2 computed", close(inv["eight_A_squared"], 0.405623467693425, 1e-12) and close(cert["eight_A_squared"], inv["eight_A_squared"], 1e-15), inv),
        check("weights computed", inv["relative_one_form_weights"]["bar_omega_1_norm_sq"] > 0 and inv["weight_anisotropy"] > 0, inv["relative_one_form_weights"]),
        check("metric block positive and monotone", flags["metric_weighted_positive_su3_samples"] is True and flags["sample_logdet_monotone_no_mu_selection"] is True, flags),
        check("E and OU open", decision["Weitzenbock_E_computed"] is False and decision["OU_weights_computed"] is False and decision["mu_selected"] is False, decision),
        check("missing fields named", {"Weitzenbock_E_Qa", "OU_gamma_nk_weights", "finite_heat_zeta_torsion_part"}.issubset(set(data["missing_fields"])), data["missing_fields"]),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records theorem", "arbitrary OU weights would be a knob" in note, NOTE),
    ]
    print("\nSelected heterotic torsional-endomorphism or OU-mode-weights audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
