"""Audit the q79 Weyl-pair sector charge/chirality reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP_SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_source_provenance_lemma.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_sector_charge_or_chirality_certificate.py"
CERT = ROOT / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_routec_weylpair_sector_charge_or_chirality_certificate"
    / "sector_charge_reduction_table.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1.md"

EXPECTED_STATUS = (
    "Q79_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_REDUCED_TO_"
    "MATTERSLOT_OVERLAP_SOURCE_OPEN"
)
EXPECTED_NEXT = "Q79_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"

EXPECTED_Q79 = {
    "source_provenance": (
        "Q79_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
    ),
    "e6_dictionary": "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN",
    "time_oriented_branch": "TIME_ORIENTED_Q79_F_BRANCH_SELECTED_ORDERED_SU5_PACKET_OPEN",
    "su5_matter_slot_transversality": "FINITE_SU5_MATTER_SLOT_TRANSVERSALITY_CLOSED_SOURCE_OPEN",
    "su5_block_orientation_route_split": "SU5_BLOCK_ORIENTATION_ROUTE_SPLIT_DETECTED_SOURCE_OPEN",
    "su5_projection_tensor": "FINITE_PROJECTION_TENSOR_DERIVED_CONDITIONALLY_SELECTION_OPEN",
    "selected_su5_source_attempt": "SELECTED_SU5_SOURCE_PROOF_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE",
    "selected_su5_qutrit_packet_attempt": (
        "SELECTED_SU5_QUTRIT_POLARIZATION_PACKET_ATTEMPT_FINITE_PASS_SELECTION_OPEN"
    ),
}

EXPECTED_SM = {
    "sector_charge_or_chirality": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_CERTIFICATE_BUILT_SOURCE_OPEN"
    ),
    "matter_slot_or_blocksector": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET"
    ),
    "hybrid_matter_slot_galerkin": (
        "MTT_SELECTED_ROUTEC_HYBRID_MATTERSLOT_GALERKIN_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_AND_OVERLAP_OPEN"
    ),
    "selected_operator_overlap_packet": (
        "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_OVERLAP_PACKET_AUDITED_SOURCE_LEVEL_CARRIER_CLOSED_SELECTED_C1_ROUTING_OPEN"
    ),
    "selected_c1_routing_normalization_overlap": (
        "MTT_SELECTED_ROUTEC_C1_ROUTING_NORMALIZATION_OVERLAP_SOURCE_ATTEMPT_BUILT_SELECTION_STILL_OPEN"
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
    require(table == cert["sector_charge_reduction"], "sector charge table mismatch", failures)
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

    reduction = cert["sector_charge_reduction"]
    required = reduction["required_route"]
    structural = reduction["su5_e6_structural_candidate"]
    finite = reduction["q79_finite_packet_evidence"]
    sm = reduction["sm_parity_reductions"]
    decision = reduction["decision"]

    require(required["phase_Z_to"] == ["u", "e"], "wrong required phase route", failures)
    require(required["shift_X_to"] == ["d", "nuD"], "wrong required shift route", failures)
    require(
        required["locked_target_columns_used_as_selector"] is False,
        "locked target columns used as selector",
        failures,
    )

    require(structural["phase_route_from_10M"] == ["e", "u"], "wrong 10M phase route", failures)
    require(
        structural["shift_route_from_non10_plus_singlet"] == ["d", "nuD"],
        "wrong non10/singlet shift route",
        failures,
    )
    require(structural["matches_required_partition"] is True, "structural partition mismatch", failures)
    require(structural["nuD_singlet_rule_closed"] is False, "nuD singlet rule overclosed", failures)
    require(structural["nuD_singlet_gap"] is True, "nuD singlet gap missing", failures)
    require(
        structural["rank_one_seed_sector_assignment_open"] is True,
        "rank-one sector assignment must remain open",
        failures,
    )

    require(finite["retarded_q79_branch_selects_F"] is True, "retarded q79/F evidence missing", failures)
    require(finite["finite_su5_transversality_closed"] is True, "finite transversality missing", failures)
    require(finite["conditional_projection_tensor_closed"] is True, "conditional tensor missing", failures)
    for key in (
        "selected_mtt_source_present",
        "selected_ordered_su5_packet_closed",
        "selected_projection_tensor_promoted",
        "selected_su5_source_present",
        "selected_su5_packet_promotes",
        "block_route_distinguishes_required_pair_split",
    ):
        require(finite[key] is False, f"finite packet overclaim: {key}", failures)

    require(sm["sector_certificate_closed"] is False, "SM sector certificate overclosed", failures)
    require(sm["conditional_route_exact"] is True, "SM conditional route exactness missing", failures)
    require(sm["selected_c1_routing_closed"] is False, "selected C1 routing overclosed", failures)
    require(sm["selected_overlap_source_closed"] is False, "selected overlap source overclosed", failures)
    require(
        sm["selected_transfer_normalization_closed"] is False,
        "selected normalization overclosed",
        failures,
    )
    require(
        sm["best_next_object"] == "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1",
        "wrong imported best next object",
        failures,
    )

    require(
        decision["source_level_weyl_carrier_and_conditional_transfer_imported"] is True,
        "source/transfer import missing",
        failures,
    )
    require(
        decision["su5_e6_partition_matches_required_route"] is True,
        "SU5/E6 structural match missing",
        failures,
    )
    for key in (
        "selected_sector_charge_or_chirality_table_proved",
        "selected_singlet_neutrino_shift_rule_proved",
        "selected_overlap_or_transfer_functor_proved",
        "selected_transfer_normalization_proved",
        "promote_conditional_A_to_A_selected",
        "target_fitting_used",
    ):
        require(decision[key] is False, f"decision overclaim: {key}", failures)

    closed = cert["closed_by_this_attempt"]
    for key in (
        "q79_source_provenance_imported",
        "su5_e6_partition_identified_as_unique_structural_candidate",
        "sm_later_packets_imported_to_refine_frontier",
        "selected_source_gap_separated_from_locked_target_columns",
        "target_fitting_excluded",
    ):
        require(closed[key] is True, f"closed flag false: {key}", failures)

    still_open = cert["still_open"]
    for key in (
        "selected_sector_charge_or_chirality_table",
        "selected_1M_singlet_neutrino_shift_rule",
        "selected_overlap_or_transfer_functor",
        "selected_transfer_normalization",
        "promote_conditional_A_to_A_selected",
        "emit_theorem_derived_b_selected",
        "full_SM_or_no_knob_closure",
    ):
        require(still_open[key] is True, f"open flag false: {key}", failures)

    require(all(value is False for value in cert["guardrails"].values()), "guardrail false-map violated", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "reduced, not closed",
        "10_M",
        "1_M",
        "same-source matter-slot charge",
        "Q79WeylPairSectorChargeOrChiralityReductionTheorem",
        EXPECTED_NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 Weyl-pair sector charge/chirality audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 Weyl-pair sector charge/chirality audit PASS")
    print(f"status: {cert['status']}")
    print("structural partition: Z -> u/e, X -> d/nuD")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
