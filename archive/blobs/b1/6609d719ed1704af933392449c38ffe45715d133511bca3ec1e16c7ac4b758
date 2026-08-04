"""Audit full-S2/no-proxy value rows or strict PEW/direct-K exit packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
REPLAY = BASE / "first_value_row_post_step10_replay.packet.json"
ACCEPTED = BASE / "accepted_first_selected_dynamic_value_row.packet.json"
FULLS2_GAP = BASE / "fulls2_no_proxy_remaining_gap.packet.json"
NEXT_PACKET = BASE / "next_after_first_selected_value_row.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullS2NoProxyValueRows_or_StrictPEWDirectKExit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FULLS2NOPROXYVALUEROWS_OR_STRICTPEWDIRECTKEXIT_"
    "FIRST_SELECTED_DYNAMIC_ROW_ACCEPTED_FULL_VALUES_OPEN"
)
NEXT = "MTT_Selected_YukawaMagnitudeRowsFromSelectedDynamicPacket_or_ValueFunctionalGap_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure guard")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    replay = load(REPLAY)
    accepted = load(ACCEPTED)
    fulls2 = load(FULLS2_GAP)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("replay", replay),
        ("accepted", accepted),
        ("fulls2", fulls2),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "FirstSelectedDynamicValueRowAfterStep10Theorem", "theorem name")

    decision = data["closure_decision"]
    for key in [
        "old_first_row_rejection_superseded",
        "first_selected_dynamic_matter_overlap_value_row_accepted",
        "VSD_01_first_response_subrow_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    require(decision["accepted_selected_dynamic_value_row_count"] == 2, "accepted row count")
    for key in [
        "VSD_01_full_yukawa_magnitude_rows_closed",
        "full_S2_value_rows_closed",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed",
        "strict_P_EW_source_theorem_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["strict_P_EW_source_rows"] == 0, "strict rows")
    require(decision["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct rows")

    require(replay["status"] == "OLD_FIRST_ROW_REJECTION_REPLAYED_AFTER_STEP10", "replay status")
    require(replay["internal_source_failures_resolved_by_active_ledger"] is True, "internal source")
    require(replay["route_A_source_rule_replaces_honest_Galerkin_requirement_here"] is True, "route A")
    require(replay["external_import_still_absent"] is True, "external absent")
    require(replay["same_source_packet_validator_ok"] is True, "validator")
    require(replay["same_source_packet_all_fields_selected"] is True, "all fields")
    require(replay["post_step10_resolution"]["selected_dynamic_source_to_C1_transfer_emitted"] is True, "transfer")
    require(replay["post_step10_resolution"]["selected_Hessian_blocks_emitted"] is True, "hessian")
    require(replay["post_step10_resolution"]["selected_b_selected_emitted"] is True, "b")
    require(replay["post_step10_resolution"]["honest_Galerkin_C1_contractions_emitted"] is False, "galerkin")

    require(accepted["status"] == "FIRST_SELECTED_DYNAMIC_MATTER_OVERLAP_VALUE_ROW_ACCEPTED", "accepted status")
    require(accepted["accepted_row_count"] == 2, "accepted rows")
    require(
        accepted["accepted_row_ids"]
        == [
            "VSD-01.phase.I_plus_Z.u.first_dynamic_row",
            "VSD-01.phase.I_plus_Z.e.first_dynamic_row",
        ],
        "row ids",
    )
    require(accepted["selected_by_MTT"] is True, "selected")
    require(accepted["target_obligation"] == "VSD-01-selected-overlap-value-kernel", "obligation")
    basis = accepted["acceptance_basis"]
    for key in [
        "same_source_dynamic_matter_overlap_packet_validates",
        "selected_dynamic_QaSU3_first_response_layer_closed",
        "same_source_packet_validator_ok",
        "all_packet_fields_same_source_selected_theorem_derived",
        "step10_route_A_source_rule_closed",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
    ]:
        require(basis[key] is True, f"basis {key}")
    require(accepted["qualitative_tests"]["current_layer_flavor_tests_pass_conditionally"] is True, "quality")
    require(accepted["qualitative_tests"]["cp_odd_invariant_nonzero"] is True, "cp")
    require(accepted["u_first_response"]["invariants"]["non_scalar"] is True, "u non-scalar")
    require(accepted["e_first_response"]["invariants"]["non_scalar"] is True, "e non-scalar")

    require(fulls2["status"] == "FIRST_DYNAMIC_ROW_ACCEPTED_BUT_FULLS2_AND_NOPROXY_VALUES_OPEN", "gap status")
    require(fulls2["closed_value_source_obligation_rows_after"] == 1, "closed obligation row")
    require(fulls2["VSD_01_first_response_subrow_closed"] is True, "subrow")
    for key in [
        "VSD_01_full_yukawa_magnitude_rows_closed",
        "full_S2_value_rows_closed",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed",
        "accepted_Yukawa_magnitudes_closed",
        "running_mass_ratios_closed",
        "CKM_PMNS_measured_value_closure_closed",
        "RO_value_source_derived",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(fulls2[key] is False, f"gap false {key}")
    require(fulls2["strict_P_EW_source_rows"] == 0, "gap strict")
    require(fulls2["direct_K_threshold_Omega_H_lambda_rows"] == 0, "gap direct")

    nums = data["key_numbers"]
    require(nums["accepted_row_count"] == 2, "numbers count")
    require(nums["u_traceless_norm_sq"] > 0, "u norm")
    require(nums["e_traceless_norm_sq"] > 0, "e norm")
    require(nums["cp_odd_trace_commutator_cubed_imag"] != 0, "cp imag")
    require(nums["ckm_commutator_norm_sq"] > 0, "ckm")
    require(nums["pmns_commutator_norm_sq"] > 0, "pmns")

    for key in [
        "theorem_proved",
        "old_first_row_rejection_superseded",
        "first_selected_dynamic_matter_overlap_value_row_accepted",
        "VSD_01_first_response_subrow_closed",
    ]:
        require(cert[key] is True, f"cert true {key}")
    require(cert["accepted_selected_dynamic_value_row_count"] == 2, "cert count")
    for key in [
        "VSD_01_full_yukawa_magnitude_rows_closed",
        "full_S2_value_rows_closed",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
    ]:
        require(cert[key] is False, f"cert false {key}")

    for phrase in [
        "FirstSelectedDynamicValueRowAfterStep10Theorem",
        "first selected dynamic matter/overlap value row accepted = true",
        "accepted selected dynamic value row count = 2",
        "VSD-01 full Yukawa magnitude rows closed = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: first selected dynamic matter/overlap value rows are "
        "accepted after Step10; full S2/no-proxy values and strict PEW/direct-K "
        "remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
