"""Audit selected_i10bindingstack_gate_or_firstvariationcertificate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i10bindingstack_gate_or_firstvariationcertificate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "i10_binding_stack.strict_template.json"
CURRENT = PACKET_DIR / "current_i10_binding_stack_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_i10_binding_stack_witness.packet.json"
PARTIALS = PACKET_DIR / "i1_i5_partial_support_ledger.packet.json"
NEXT_CERT = PACKET_DIR / "next_first_variation_certificate.packet.json"
ACTION_BRIDGE = PACKET_DIR / "conditional_action_kernel_bridge.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I10BindingStack_Gate_or_FirstVariationCertificate_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"


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
    partials = load(PARTIALS)
    next_cert = load(NEXT_CERT)
    action_bridge = load(ACTION_BRIDGE)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I10BINDINGSTACK_GATE_BUILT_FIRSTVARIATION_CERTIFICATE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "I10 binding stack theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(len(template["required_fields"]) == 7, "template required field count mismatch")
    for field in template["required_fields"]:
        require(current[field] is False, f"current unexpectedly verifies {field}")
        require(witness[field] is True, f"witness missing {field}")
    require(current["free_axiom_patch_used"] is False, "current uses free patch")
    require(witness["conditional_only"] is True, "witness should be conditional")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(partials["I1"]["stationary_component_available"] is True, "I1 stationary partial missing")
    require(partials["I1"]["full_dynamic_payload_verified"] is False, "I1 dynamic payload overpromoted")
    require(partials["I5"]["source_component_available"] is True, "I5 source partial missing")
    require(partials["I5"]["full_c1_response_payload_verified"] is False, "I5 C1 payload overpromoted")
    require(next_cert["theorem_slot"] == "I11_strominger_trace_c1_first_variation", "I11 slot mismatch")
    require(len(next_cert["must_fill"]) == 5, "I11 fill field count mismatch")
    require(action_bridge["validation_returncode"] == 0, "action-kernel bridge should validate conditionally")
    require(cert["current_attempt_rejected"] is True, "cert should record current rejection")
    require(cert["conditional_witness_passes"] is True, "cert should record witness pass")
    require(cert["action_kernel_bridge_checked"] is True, "cert should record action bridge")
    require("current I10 binding attempt validates = False" in note, "note missing current-fail statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
