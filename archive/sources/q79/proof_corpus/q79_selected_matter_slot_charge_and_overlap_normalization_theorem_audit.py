"""Audit the q79 selected matter-slot charge and overlap-normalization theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP_SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_sector_charge_or_chirality_certificate.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_selected_matter_slot_charge_and_overlap_normalization_theorem.py"
CERT = ROOT / "certificates" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem"
    / "matter_slot_overlap_reduction_table.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

EXPECTED_STATUS = (
    "Q79_SELECTED_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_"
    "REDUCED_TO_SAMESOURCE_OPERATOR_PACKET_OPEN"
)
EXPECTED_NEXT = "Q79_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"

EXPECTED_Q79 = {
    "sector_charge_reduction": (
        "Q79_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE_OPEN"
    ),
    "source_provenance": (
        "Q79_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
    ),
    "conditional_weylpair_A": "Q79_ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
    "su5_matter_slot_transversality": "FINITE_SU5_MATTER_SLOT_TRANSVERSALITY_CLOSED_SOURCE_OPEN",
    "su5_source_attempt": "SELECTED_SU5_SOURCE_PROOF_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE",
}

EXPECTED_SM = {
    "matter_slot_overlap_theorem": (
        "MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET"
    ),
    "matter_slot_overlap_theorem_candidate": (
        "MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET"
    ),
    "same_source_operator_packet": (
        "MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN"
    ),
    "same_source_operator_packet_candidate": (
        "MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN"
    ),
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP_SCRIPT, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["matter_slot_overlap_reduction"], "reduction table mismatch", failures)
    require(cert["status"] == EXPECTED_STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    for name, status in EXPECTED_Q79.items():
        require(
            cert["q79_input_statuses"][name]["status"] == status,
            f"unexpected q79 status for {name}: {cert['q79_input_statuses'][name]['status']}",
            failures,
        )
    for name, status in EXPECTED_SM.items():
        require(
            cert["sm_input_statuses"][name]["status"] == status,
            f"unexpected SM status for {name}: {cert['sm_input_statuses'][name]['status']}",
            failures,
        )

    reduction = cert["matter_slot_overlap_reduction"]
    support = reduction["proved_imported_support"]
    charge = reduction["matter_slot_charge"]
    overlap = reduction["overlap_normalization"]
    packet = reduction["same_source_operator_packet"]
    decision = reduction["decision"]

    for key in (
        "source_level_weyl_carrier_closed",
        "conditional_source_to_c1_transfer_exact",
        "conditional_A_rank_and_solve_closed",
        "su5_e6_partition_matches_required_route",
        "finite_su5_transversality_under_source_hypothesis_closed",
        "conditional_routing_and_normalization_exact",
    ):
        require(support[key] is True, f"support flag false: {key}", failures)

    require(charge["desired_phase_route"] == ["u", "e"], "wrong phase route", failures)
    require(charge["desired_shift_route"] == ["d", "nuD"], "wrong shift route", failures)
    require(charge["routeA_matches_required_partition"] is True, "route A partition missing", failures)
    require(charge["routeB_current_selected_block_uniform"] is True, "route B uniformity missing", failures)
    require(charge["selected_charge_table_closed"] is False, "selected charge overclosed", failures)
    require(charge["singlet_1M_rule_present"] is False, "1M rule overclosed", failures)
    require(charge["all_su5_source_routes_blocked"] is True, "SU5 source blockage missing", failures)

    require(overlap["enriched_weyl_pair_conditionally_sufficient"] is True, "enriched sufficiency missing", failures)
    require(overlap["selected_overlap_functor_emitted"] is False, "selected overlap functor overclosed", failures)
    require(overlap["selected_normalization_emitted"] is False, "selected normalization overclosed", failures)
    require(
        overlap["canonical_overlap_lane_retired_for_nonzero"] is True,
        "canonical lane retirement missing",
        failures,
    )

    require(packet["contract_status"] == EXPECTED_SM["same_source_operator_packet_candidate"], "wrong packet status", failures)
    require(packet["next_required_artifact"] == "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1", "wrong imported packet next", failures)
    require(packet["field_counts"] == {"required": 7, "selected_emitted": 0, "support_present": 6}, "wrong field counts", failures)
    require(packet["packet_closed"] is False, "packet overclosed", failures)
    require(packet["selected_values_open"] is True, "selected values not marked open", failures)
    require(packet["source_level_support_broad"] is True, "support breadth missing", failures)
    require(packet["all_required_fields_selected"] is False, "all fields selected overclaim", failures)
    require(len(packet["required_fields"]) == 7, "expected seven required fields", failures)
    require("singlet_neutrino_rule" in packet["required_fields"], "missing singlet neutrino required field", failures)
    require(packet["support_fields"]["singlet_neutrino_rule"] is False, "singlet support should be false", failures)
    require(all(value is False for value in packet["selected_fields"].values()), "some field selected unexpectedly", failures)

    require(decision["finite_algebra_is_not_blocker"] is True, "finite algebra decision missing", failures)
    require(decision["same_source_operator_packet_required"] is True, "same-source requirement missing", failures)
    for key in (
        "selected_matter_slot_charge_closed",
        "selected_overlap_normalization_closed",
        "same_source_packet_values_emitted",
        "promote_conditional_A_to_A_selected",
        "emit_b_selected",
        "target_fitting_used",
        "full_SM_or_no_knob_closure",
    ):
        require(decision[key] is False, f"decision overclaim: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail false-map violated: {key}", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for key in (
        "fill_same_source_packet_values",
        "prove_selected_matter_slot_charge",
        "prove_selected_1M_neutrino_rule",
        "emit_selected_DE_dotD_Riesz_Green",
        "emit_selected_overlap_transfer_functor",
        "emit_selected_normalization_and_b_selected",
        "emit_selected_A_selected_and_b_selected",
        "full_SM_or_no_knob_closure",
    ):
        require(cert["still_open"][key] is True, f"open flag false: {key}", failures)

    for phrase in (
        "reduced, not closed",
        "same-source operator packet",
        "field counts",
        "singlet_neutrino_rule",
        "Q79SelectedMatterSlotChargeAndOverlapNormalizationReductionTheorem",
        EXPECTED_NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected matter-slot/overlap normalization audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected matter-slot/overlap normalization audit PASS")
    print(f"status: {cert['status']}")
    print(f"field counts: {packet['field_counts']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
