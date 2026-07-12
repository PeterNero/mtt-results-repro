"""Audit CONST-EW-02 B43 threshold-vector or minimal-threshold policy packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DECOMPOSITION = BASE / "threshold_vector_decomposition.packet.json"
STRICT_AUDIT = BASE / "strict_threshold_source_audit.packet.json"
MINIMAL_POLICY = BASE / "minimal_threshold_replay_policy.packet.json"
CONDITIONAL_VALUE = BASE / "conditional_minimal_threshold_weak_angle.packet.json"
BOUNDARY = BASE / "weak_mixing_b43_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B43_ThresholdVector_or_MinimalPolicy_v1.md"

STATUS = "MTT_CONST_EW_02_B43_THRESHOLD_VECTOR_OR_MINIMAL_POLICY_BUILT_STRICT_VECTOR_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    decomposition = load(DECOMPOSITION)
    strict_audit = load(STRICT_AUDIT)
    minimal_policy = load(MINIMAL_POLICY)
    conditional_value = load(CONDITIONAL_VALUE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("decomposition", decomposition),
        ("strict_audit", strict_audit),
        ("minimal_policy", minimal_policy),
        ("conditional_value", conditional_value),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["threshold_decomposition_closed"] is True, "decomposition")
    require(candidate["strict_threshold_vector_source_emitted"] is False, "strict vector overemitted")
    require(candidate["minimal_threshold_replay_policy_closed"] is True, "minimal policy")
    require(abs(candidate["conditional_minimal_threshold_sin2"] - 0.2315309482915084) < 1e-15, "conditional sin2")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict overclosed")

    dec = decomposition["decision"]
    require(dec["internal_weaksplit_prefix_closed"] is True, "internal prefix")
    require(dec["flat_FP_extra_threshold_closed_zero"] is True, "flat FP")
    require(dec["full_physical_threshold_vector_closed"] is False, "physical vector overclosed")
    require(dec["residual_threshold_vector_may_be_set_zero_without_policy"] is False, "implicit zero residual")
    require(decomposition["decomposition"]["closed_flat_FP_piece"]["extra_fp_threshold_term"] == 0.0, "FP value")

    strict_decision = strict_audit["decision"]
    require(strict_decision["strict_threshold_vector_source_emitted"] is False, "strict source emitted")
    require(strict_decision["current_source_nogo_for_strict_vector"] is True, "current source no-go")
    require(strict_decision["mathematical_impossibility_claimed"] is False, "impossibility overclaim")
    require(strict_decision["diagnostic_threshold_witness_forbidden_as_proof"] is True, "diagnostic guardrail")
    statuses = strict_audit["source_packet_statuses"]
    require(statuses["physical_threshold_vector_closed"] is False, "QA physical vector")
    require(statuses["qastack_full_threshold_formula_closed"] is False, "QA qastack formula")
    require(statuses["projective_rhoe_physical_threshold_normalization_closed"] is False, "QA rhoE")

    policy_decision = minimal_policy["decision"]
    require(policy_decision["minimal_threshold_replay_policy_closed"] is True, "policy closed")
    require(policy_decision["strict_threshold_vector_closed"] is False, "policy strict vector")
    require(policy_decision["physical_weak_angle_closure"] is False, "policy weak angle")
    admissibility = minimal_policy["admissibility"]
    require(admissibility["observed_weak_angle_used_to_set_thresholds"] is False, "weak angle threshold selector")
    require(admissibility["adds_new_weak_angle_knob"] is False, "new weak knob")
    require(admissibility["allowed_as_replay_lane"] is True, "replay lane")
    require(admissibility["allowed_as_strict_source_vector"] is False, "strict lane")

    classification = conditional_value["classification"]
    require(classification["conditional_replay_value"] is True, "conditional classification")
    require(classification["physical_weak_angle_prediction"] is False, "physical prediction overclaim")
    require(classification["strict_no_knob_value"] is False, "strict value overclaim")
    require(classification["precision_SM_effective_angle"] is False, "precision angle overclaim")
    computed_value = conditional_value["computed"]
    require(computed_value["matches_B22_conditional_sin2"] is True, "B22 value mismatch")
    require(abs(computed_value["sin2_minimal_threshold_replay"] - 0.2315309482915084) < 1e-15, "conditional value")

    closed = boundary["closed_or_decided_now"]
    require(closed["threshold_decomposition"] is True, "boundary decomposition")
    require(closed["strict_source_selected_threshold_vector_currently_not_emitted"] is True, "boundary strict")
    require(closed["minimal_no_additional_threshold_replay_policy"] is True, "boundary minimal")
    require(closed["conditional_minimal_threshold_weak_angle_value_emitted"] is True, "boundary value")
    require(boundary["still_open"]["strict_source_selected_threshold_vector"] is True, "strict open")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "weak angle open")
    require("not using diagnostic threshold witnesses as proof inputs" in boundary["anti_cycle_delta_from_B42"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B44-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-EXECUTION-PACKET", "next parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["strict_threshold_vector_source_emitted"] is False, "cert strict")
    require(cert["minimal_threshold_replay_policy_closed"] is True, "cert policy")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require("B43" in note and "conditional replay sin2" in note and "not a precision physical" in note, "note")

    print("CONST-EW-02 B43 threshold-vector/minimal-policy audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
