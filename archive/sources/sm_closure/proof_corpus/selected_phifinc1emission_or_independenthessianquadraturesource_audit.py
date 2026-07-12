"""Audit selected_phifinc1emission_or_independenthessianquadraturesource."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_phifinc1emission_or_independenthessianquadraturesource.candidate.json"
ATTEMPT = ROOT / "candidate_data" / "selected_phifinc1emission_or_independenthessianquadraturesource" / "current_source_emission_attempt.packet.json"
CUTSET = ROOT / "candidate_data" / "selected_phifinc1emission_or_independenthessianquadraturesource" / "final_source_emission_cutset.packet.json"
CERT = ROOT / "certificates" / "selected_phifinc1emission_or_independenthessianquadraturesource_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1Emission_or_IndependentHessianQuadratureSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_PHIFINC1EMISSION_OR_INDEPENDENTHESSIANQUADRATURESOURCE_BUILT_FINAL_VALIDATOR_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "disjunction theorem not proved")
    require(attempt["support_closed"]["variation_operator_shape_compatibility"] is True, "variation support missing")
    require(attempt["support_closed"]["formal_hessian_target_identified"] is True, "hessian target missing")
    require(attempt["locked_target_values_used_as_source"] is False, "locked targets used")
    require(attempt["route_A_phifinc1_source_emission"]["physical_phifin_c1_action_emitted"] is False, "Route A overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["independent_hessian_quadrature_source_emitted"] is False, "Route B hessian overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["selected_basis_independent_of_residual_projector"] is True, "Route B basis support missing")
    require(attempt["route_B_independent_hessian_quadrature_source"]["quadrature_rule_independent_of_locked_target"] is True, "Route B quadrature support missing")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("neither narrowed Route A nor narrowed Route B validates" in line for line in proc.stderr.splitlines()), "missing final rejection")
    require(cutset["current_attempt_validates"] is False, "cutset should reject")
    require(cutset["remaining_route_A"]["same_source_b_selected_emitted"] is True, "Route A b gap missing")
    require(cutset["remaining_route_B"]["independent_hessian_quadrature_source_emitted"] is True, "Route B hessian gap missing")
    require(cert["validator_rejects_current_attempt"] is True, "cert should reject")
    require(cert["same_branch_phifin_source_closed"] is False, "cert Route A overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert Route B overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("current attempt is intentionally rejected" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
