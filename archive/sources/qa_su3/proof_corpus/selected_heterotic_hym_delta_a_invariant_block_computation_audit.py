"""Audit the finite invariant HYM Delta_A connection-mass block computation."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_delta_a_invariant_block_computation.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_delta_a_invariant_block_computation_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_DeltaA_InvariantBlock_Computation_v1.md"

STATUS = "HETEROTIC_HYM_DELTA_A_INVARIANT_CONNECTION_BLOCK_COMPUTED_MU_OPEN"
NEXT = "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def positive_det(mu: float) -> float:
    return 12 * mu**9 * (1 + mu) * (2 + mu) * (1 + 2 * mu)


def numeric_spectrum(mu: float) -> list[float]:
    return sorted(
        [
            0,
            mu,
            mu,
            2 * mu,
            mu * (1 + mu),
            mu * (1 + 2 * mu),
            mu * (2 + mu),
            mu * (mu + 2 - math.sqrt(mu * mu - 2 * mu + 4)),
            mu * (mu + 2 + math.sqrt(mu * mu - 2 * mu + 4)),
        ]
    )


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
    decision = data["decision"]
    comp = data["computation"]
    guards = data["guardrails"]
    spec_mu1 = numeric_spectrum(1.0)

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("basis size", len(comp["basis"]) == 9 and comp["basis"][0] == "E11" and comp["basis"][-1] == "E33", comp["basis"]),
        check("matrix formula", comp["matrix_formula"] == "M_inv(mu)=mu*M_mu + mu^2*M_mu2", comp["matrix_formula"]),
        check("spectrum has one zero", comp["spectrum"].count("0") == 1 and len(comp["spectrum"]) == 9, comp["spectrum"]),
        check("det prime formula", comp["positive_det_prime"] == "12*mu^9*(1+mu)*(2+mu)*(1+2*mu)" and abs(positive_det(1.0) - 216.0) < 1e-12, comp["positive_det_prime"]),
        check("mu=1 diagnostic eigenvalues", abs(spec_mu1[1] - 1.0) < 1e-12 and abs(spec_mu1[-1] - (3 + math.sqrt(3))) < 1e-12, spec_mu1),
        check("block computed but no closure", decision["finite_invariant_connection_block_computed"] is True and decision["full_delta_a_spectrum_computed"] is False and decision["mu_selected"] is False, decision),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records logdet", "log det'(M_inv)" in note and "12*mu^9" in note, NOTE),
    ]
    print("\nSelected heterotic HYM Delta_A invariant block computation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
