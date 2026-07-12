"""Audit post-AH8 magnitude-bearing policy-tier import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_magnitudebearingrows_after_postah8_dynamicimport.py"

SLUG = "selected_magnitudebearingrows_after_postah8_dynamicimport"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MagnitudeBearingRowsAfterPostAH8DynamicImport_or_ThresholdResponseDerivation_v1.md"
POLICY_IMPORT = PACKET_DIR / "post_ah8_minimal_nineslot_flavor_value_import.packet.json"
STRICT_RECHECK = PACKET_DIR / "post_ah8_strict_noknob_flavor_recheck.packet.json"
NEXT_PACKET = PACKET_DIR / "next_ckm_pmns_orientation_or_strict_flavor_source_after_policy_values.packet.json"

STATUS = "MTT_SELECTED_MAGNITUDEBEARINGROWS_AFTER_POSTAH8_DYNAMICIMPORT_POLICY9_STRICT0"
NEXT = "MTT_Selected_FlavorOperatorPolicyUseAfterAH8_or_CKMPMNSOrientationBridge_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    policy = load(POLICY_IMPORT)
    strict = load(STRICT_RECHECK)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, policy, strict, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["post_AH8_dynamic_value_rows_imported"] is True, "dynamic rows not imported")
    require(decision["accepted_selected_dynamic_value_row_count"] == 2, "dynamic count")
    require(decision["selected_family_spectral_basis_closed"] is True, "spectral basis")
    require(decision["minimal_nine_slot_policy_adopted"] is True, "policy not adopted")
    require(decision["value_complete_at_minimal_policy_tier"] is True, "policy tier not complete")
    require(decision["policy_source_value_row_count"] == 9, "policy row count")
    require(decision["observed_profile_values_used_as_parameter_values"] is True, "policy value boundary missing")
    require(decision["accepted_selected_no_knob_coefficient_source_row_count"] == 0, "strict rows overaccepted")
    require(decision["selected_flavor_threshold_source_operator_closed"] is False, "flavor operator overclosed")
    require(decision["strict_no_knob_flavor_closure"] is False, "strict flavor overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(policy["value_complete_at_minimal_policy_tier"] is True, "policy packet completeness")
    require(policy["policy_source_value_row_count"] == 9, "policy packet count")
    require(policy["minimal_profile_replay_parameter_slots"] == 9, "policy parameter slots")
    require(policy["flavor_operator_values_emitted"] is True, "policy values not emitted")
    require(policy["observed_profile_values_used_as_parameter_values"] is True, "policy observed-value boundary")

    require(strict["accepted_selected_no_knob_coefficient_source_row_count"] == 0, "strict packet rows")
    require(strict["selected_flavor_threshold_source_operator_closed"] is False, "strict packet operator")
    require(strict["strict_no_knob_flavor_closure"] is False, "strict packet closure")
    require(strict["true_SM_equivalence_closed"] is False, "strict packet true SM")

    for item in [
        "AH-equivalent BN27 8/8 matrix row",
        "first selected dynamic non-scalar value rows",
        "selected family spectral response basis",
        "minimal nine-slot flavor policy value table",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    for item in [
        "selected flavor threshold/source operator emitting coefficient rows",
        "source-selected reduced-coefficient theorem",
        "CKM/PMNS orientation bridge using policy-tier operator values",
        "strict no-knob replacement for nine policy parameters",
    ]:
        require(item in next_packet["remaining_strict_targets"], f"target missing: {item}")

    require(cert["value_complete_at_minimal_policy_tier"] is True, "cert policy tier")
    require(cert["policy_source_value_row_count"] == 9, "cert policy count")
    require(cert["accepted_selected_no_knob_coefficient_source_row_count"] == 0, "cert strict rows")
    require(cert["strict_no_knob_flavor_closure"] is False, "cert strict closure")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("minimal nine-slot policy tier" in note, "note policy")
    require("accepted selected coefficient" in note, "note strict")
    require(NEXT in note, "note next")

    print("Post-AH8 magnitude-bearing policy-tier audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
