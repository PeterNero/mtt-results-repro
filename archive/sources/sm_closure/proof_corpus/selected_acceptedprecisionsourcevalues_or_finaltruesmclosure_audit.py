"""Audit accepted precision source-values / final true-SM closure frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedprecisionsourcevalues_or_finaltruesmclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "accepted_source_value_frontier_ledger.packet.json"
REPLAY = PACKET_DIR / "replay_tier_precision_value_sources.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_payload_source_value_status.packet.json"
CUTSET = PACKET_DIR / "source_value_promotion_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedPrecisionSourceValues_or_FinalTrueSMClosure_v1.md"

STATUS = (
    "MTT_SELECTED_ACCEPTEDPRECISIONSOURCEVALUES_OR_FINALTRUESMCLOSURE_"
    "REPLAY_SOURCE_VALUES_LOCKED_PROMOTION_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_ValueSourcePromotionExecution_or_FinalProfilePayloadClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    ledger = load(LEDGER)
    replay = load(REPLAY)
    dynamic = load(DYNAMIC)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("ledger", ledger),
        ("replay", replay),
        ("dynamic", dynamic),
        ("cutset", cutset),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "AcceptedPrecisionSourceValuesOrFinalTrueSMClosureTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(cutset["next_required_artifact"] == NEXT_ARTIFACT, "cutset next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(ledger["status"] == "REPLAY_SOURCE_VALUE_LAYERS_LOCKED_TRUE_PRECISION_PROMOTION_OPEN", "ledger status")
    require(ledger["frontier_attack_executed"] is True, "frontier attack")
    require(ledger["closed_replay_source_value_class_count"] == 8, "closed replay classes")
    require(ledger["accepted_true_precision_source_value_class_count"] == 0, "true precision overclaim")
    require(ledger["accepted_true_equivalence_precision_rows"] == 0, "true rows overclaim")
    require(ledger["transport_easy_win_count"] == 19, "transport easy-win count")
    for item in ledger["replay_classes"]:
        require(item["closed"] is True, f"replay class not closed: {item['class']}")
        require(item["true_precision_closed"] is False, f"true precision overclosed: {item['class']}")

    common = replay["common_scale_values"]
    require(common["accepted_for_SM_parity"] is True, "common scale parity")
    require(common["accepted_for_true_precision"] is False, "common scale true precision")
    require(common["diagonal_profile_execution_layer_closed"] is True, "diagonal profile")
    require(common["full_profile_likelihood_closed"] is False, "full profile overclosed")

    higgs = replay["higgs_imported_profile_replay"]
    require(higgs["accepted_as_SM_parity_covariance_replay"] is True, "Higgs replay parity")
    require(higgs["imported_profile_replay_closed"] is True, "Higgs profile replay")
    require(higgs["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overclaimed")
    require(higgs["precision_branching_ratios_closed"] is False, "BR overclosed")
    require(higgs["precision_total_width_closed"] is False, "width overclosed")

    flavor = replay["flavor_threshold_policy"]
    require(flavor["minimal_nine_slot_policy_adopted"] is True, "nine-slot policy")
    require(flavor["policy_source_value_row_count"] == 9, "flavor row count")
    require(flavor["minimal_profile_replay_parameter_slots"] == 9, "profile slots")
    require(flavor["accepted_selected_no_knob_coefficient_source_row_count"] == 0, "no-knob coefficient overclaim")
    require(flavor["strict_no_knob_flavor_closure"] is False, "strict flavor overclosed")

    source = dynamic["operator_source_slot_layer"]
    require(source["source_slot_layer_closed"] is True, "source slot layer")
    require(source["operator_source_slots_closed"] == 8, "source slot count")
    require(source["operator_source_slots_remaining"] == 0, "source slot remaining")
    require(source["minimal_local_QFT_value_suite_filled"] is True, "minimal local QFT suite")
    require(source["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic payload overclosed")

    first = dynamic["dynamic_first_response"]
    require(first["dynamic_QaSU3_first_response_layer_replayed"] is True, "first response")
    require(first["actual_QaSU3_operator_packet_no_longer_absent_at_first_response_layer"] is True, "first response absent")
    require(first["qualitative_non_scalar_flavor_tests_preserved"] is True, "qualitative tests")

    partial = dynamic["partial_payload"]
    require(partial["partial_QaSU3_payload_filled"] is True, "partial payload")
    require(partial["best_qasu3_payload_lane_selected"] is True, "best lane")
    require(partial["partial_same_source_payload_emitted"] is True, "same-source partial payload")
    require(partial["actual_QaSU3_packet_promoted"] is False, "partial promoted overclaim")
    require(partial["profile_workspace_imported"] is False, "workspace overimported")

    require(cutset["status"] == "PROMOTION_CUTSET_SHARPENED", "cutset status")
    require(cutset["remaining_promotion_count"] == 7, "promotion count")
    require(cutset["surrogate_profile_matrix_reconstructed"] is True, "surrogate profile")
    require(cutset["accepted_as_full_profile"] is False, "full profile accepted overclaim")
    require(cutset["actual_QaSU3_packet_found_in_full_profile_search"] is False, "QaSU3 found overclaim")
    require(cutset["selected_threshold_response_functional_instantiated"] is False, "threshold instantiated overclaim")
    require(cutset["external_likelihood_workspace_acquired"] is False, "workspace acquired overclaim")

    decision = candidate["closure_decision"]
    require(decision["accepted_precision_source_value_frontier_attacked"] is True, "decision attacked")
    require(decision["closed_replay_source_value_class_count"] == 8, "decision replay count")
    require(decision["accepted_true_precision_source_value_class_count"] == 0, "decision true precision count")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "decision true rows")
    require(decision["flavor_policy_source_value_row_count"] == 9, "decision flavor rows")
    require(decision["operator_source_slots_closed"] == 8, "decision source slots")
    require(decision["dynamic_QaSU3_first_response_layer_replayed"] is True, "decision first response")
    require(decision["partial_QaSU3_payload_filled"] is True, "decision partial payload")
    for key in [
        "accepted_common_scale_values_for_true_precision",
        "full_profile_likelihood_closed",
        "accepted_as_official_LHCHXSWG_likelihood",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_as_full_profile",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "replay/source-value classes locked                 8",
        "accepted true-precision source-value classes       0",
        "operator source slots closed                       8",
        "actual dynamic Qa/SU3 payload                      false",
        "threshold response functional instantiated         false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
