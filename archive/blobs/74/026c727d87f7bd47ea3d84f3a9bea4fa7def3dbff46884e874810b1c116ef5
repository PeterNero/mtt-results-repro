"""Audit selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "pre_residual_variation_hessian_source_kernel.strict_template.json"
CURRENT = PACKET_DIR / "current_pre_residual_variation_hessian_source_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_source_kernel_witness.packet.json"
TRIAGE = PACKET_DIR / "three_route_source_kernel_triage.packet.json"
AXIOM = PACKET_DIR / "minimal_action_axiom_or_theorem.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PreResidualVariation_HessianSourceKernel_Attempt_or_ActionAxiom_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_preresidual_variation_hessian_source_kernel.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    template = load(TEMPLATE)
    current = load(CURRENT)
    witness = load(WITNESS)
    triage = load(TRIAGE)
    axiom = load(AXIOM)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PRERESIDUALVARIATION_HESSIANSOURCEKERNEL_ATTEMPT_BUILT_ACTION_AXIOM_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "kernel reduction theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional only")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(len(template["required_fields"]) == 4, "required field count mismatch")
    require(template["validator"].endswith("validate_selected_preresidual_variation_hessian_source_kernel.py"), "validator mismatch")

    require(current["selected_variation_functional"] is False, "current variation source should remain false")
    require(current["same_source_hessian"] is False, "current Hessian source should remain false")
    require(current["sector_functor"] is False, "current sector functor should remain false")
    require(current["independence_certificate"] is False, "current independence should remain false")
    require(current["closure_claimed"] is False, "current closure overclaimed")

    require(witness["selected_variation_functional"] is True, "witness variation source missing")
    require(witness["same_source_hessian"] is True, "witness Hessian source missing")
    require(witness["sector_functor"] is True, "witness sector functor missing")
    require(witness["independence_certificate"] is True, "witness independence missing")
    require(witness["conditional_only"] is True, "witness should be conditional")
    require(witness["closure_claimed"] is False, "witness closure overclaimed")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(triage["routes"]["route_A_physical_action"]["promoted_now"] is False, "Route A should remain open")
    require(triage["routes"]["route_B_independent_galerkin"]["current_independent_values_emitted"] == 0, "Route B emitted values unexpectedly")
    require(triage["routes"]["route_C_new_weyl_variation_principle"]["promoted_now"] is False, "Route C should remain open")
    require(axiom["proved_here"] is False, "minimal action axiom should not be proved here")
    require(axiom["must_not_be_used_as_free_patch"] is True, "axiom guard missing")
    require(cert["current_attempt_rejected"] is True, "cert should record current rejection")
    require(cert["conditional_witness_passes"] is True, "cert should record witness pass")
    require("current source-kernel attempt validates   = False" in note, "note missing current-fail statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
