"""Audit selected_finalsourceemission_bestcurrentfill_or_nogowitness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_finalsourceemission_bestcurrentfill_or_nogowitness.candidate.json"
ATTEMPT = ROOT / "candidate_data" / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "best_current_source_emission_fill_attempt.packet.json"
WITNESS = ROOT / "candidate_data" / "selected_finalsourceemission_bestcurrentfill_or_nogowitness" / "final_source_emission_nogo_witness.packet.json"
CERT = ROOT / "certificates" / "selected_finalsourceemission_bestcurrentfill_or_nogowitness_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalSourceEmission_BestCurrentFill_or_NoGoWitness_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    witness = load(WITNESS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_FINALSOURCEEMISSION_BESTCURRENTFILL_BUILT_NOGO_WITNESS_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "no-go theorem not proved")
    require(attempt["route_A_phifinc1_source_emission"]["physical_phifin_c1_action_emitted"] is False, "Route A overclosed")
    require(attempt["route_A_phifinc1_source_emission"]["same_source_b_selected_emitted"] is False, "Route A b overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["independent_hessian_quadrature_source_emitted"] is False, "Route B hessian overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["selected_b_vector_source"] is False, "Route B b overclosed")
    require(proc.returncode == 1, "validator should reject best current fill")
    require(any("neither narrowed Route A nor narrowed Route B validates" in line for line in proc.stderr.splitlines()), "missing validator rejection")
    require(witness["validator_rejects_best_current_fill"] is True, "witness should reject")
    require(witness["route_A_best_support"]["physical_action_identity_promoted"] is False, "Route A witness overclosed")
    require(witness["route_B_best_support"]["independent_execution_now"] is False, "Route B witness overclosed")
    require(witness["route_B_best_support"]["selected_quadrature_engine_or_rule_missing"] is True, "quadrature rule gap missing")
    require(cert["validator_rejects_best_current_fill"] is True, "cert should reject")
    require(cert["same_branch_phifin_source_closed"] is False, "cert Route A overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert Route B overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("Current artifacts provide replay and" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
