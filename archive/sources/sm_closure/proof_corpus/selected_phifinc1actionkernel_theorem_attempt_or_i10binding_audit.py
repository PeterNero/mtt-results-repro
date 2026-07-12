"""Audit selected_phifinc1actionkernel_theorem_attempt_or_i10binding."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "phifinc1_preresidual_action_kernel_theorem.strict_template.json"
CURRENT = PACKET_DIR / "current_action_kernel_theorem_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_i10_action_kernel_witness.packet.json"
DEPENDENCIES = PACKET_DIR / "i10_dependency_chain.packet.json"
REMAINING = PACKET_DIR / "remaining_i10_binding_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
KERNEL_WITNESS = PACKET_DIR / "conditional_source_kernel_validation_bridge.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1ActionKernel_TheoremAttempt_or_I10Binding_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"


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
    deps = load(DEPENDENCIES)
    remaining = load(REMAINING)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    kernel_witness = load(KERNEL_WITNESS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PHIFINC1ACTIONKERNEL_THEOREM_ATTEMPT_BUILT_I10_BINDING_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "I10 reduction theorem not proved")
    require(data["conditional_only"] is True, "candidate must be conditional only")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(len(template["required_fields"]) == 4, "template required field count mismatch")
    require(current["physical_action_equals_c1_defect_functional"] is False, "current action binding should remain false")
    require(current["physical_boundary_source_terms_vanish"] is False, "current physical boundary should remain false")
    require(current["same_source_rz_rx_bselected_emitted"] is False, "current same-source emission should remain false")
    require(current["free_axiom_patch_used"] is False, "current should not use free patch")
    require(current["closure_claimed"] is False, "current closure overclaimed")

    require(witness["physical_action_equals_c1_defect_functional"] is True, "witness action binding missing")
    require(witness["admissible_differentiated_variations_fixed"] is True, "witness variation class missing")
    require(witness["physical_boundary_source_terms_vanish"] is True, "witness boundary missing")
    require(witness["same_source_rz_rx_bselected_emitted"] is True, "witness same-source emission missing")
    require(witness["conditional_only"] is True, "witness must be conditional")
    require(witness["closure_claimed"] is False, "witness closure overclaimed")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(deps["depends_on"]["I10_PhiFinC1_minimizes_defect_functional"]["proved"] is False, "I10 unexpectedly proved")
    require(deps["depends_on"]["I1_selected_minimizer_to_PhiFin_trace"]["proved"] is False, "I1 unexpectedly proved")
    require(deps["depends_on"]["I5_selected_dotD_C1_response"]["proved"] is False, "I5 unexpectedly proved")
    require(deps["depends_on"]["physical_boundary_promotion"]["proved"] is False, "physical boundary unexpectedly promoted")
    require(deps["depends_on"]["same_source_RZ_RX_bselected_emission"]["proved"] is False, "same-source emission unexpectedly promoted")

    require("physical Phi_fin^C1 equals the defect functional" in remaining["not_enough_for"], "remaining frontier missing physical binding")
    require(kernel_witness["validation_returncode"] == 0, "source-kernel bridge should validate conditionally")
    require(cert["current_attempt_rejected"] is True, "cert should record current rejection")
    require(cert["conditional_i10_witness_passes"] is True, "cert should record witness pass")
    require(cert["source_kernel_bridge_checked"] is True, "cert should record source bridge")
    require("conditional I10 witness validates       = True" in note, "note missing conditional witness statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
