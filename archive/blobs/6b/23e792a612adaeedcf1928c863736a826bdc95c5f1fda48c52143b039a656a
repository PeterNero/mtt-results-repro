"""Audit Yukawa source bridge / magnitude projection no-go theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_BRIDGE = PACKET_DIR / "same_source_yukawa_source_bridge.packet.json"
NO_GO = PACKET_DIR / "sector_blind_magnitude_projection_nogo.packet.json"
PROJECTION_REQUIREMENT = PACKET_DIR / "projection_kernel_requirement.packet.json"
DECISION = PACKET_DIR / "yukawa_source_bridge_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_yukawa_source_bridge.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaSourceBridge_or_MagnitudeProjectionNoGoTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_YUKAWASOURCEBRIDGE_OR_MAGNITUDEPROJECTIONNOGOTHEOREM_"
    "BUILT_SOURCE_LAYER_CLOSED_MAGNITUDES_REQUIRE_PROJECTION"
)
NEXT = "MTT_Selected_YukawaMagnitudeProjectionKernel_or_RThetaThresholdResponseExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source = load(SOURCE_BRIDGE)
    nogo = load(NO_GO)
    projection = load(PROJECTION_REQUIREMENT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(source["status"] == "YUKAWA_SOURCE_LAYER_BRIDGED_TO_SELECTED_DYNAMIC_OVERLAP", "source status mismatch")
    require(source["closure_claimed"] is True, "source bridge should close locally")
    closure = source["source_layer_closure"]
    for key in [
        "same_source_fields_closed",
        "same_source_validator_ok",
        "selected_dynamic_overlap_tensor_promoted",
        "primitive_C1_first_response_layer_emitted",
        "dynamic_QaSU3_first_response_layer_replayed",
        "symbolic_transport_source_gate_closed",
        "alpha1_dotd_retired",
    ]:
        require(closure[key] is True, f"source layer not closed: {key}")
    for field_id, field in source["source_fields"].items():
        require(field["same_source"] is True, f"field not same source: {field_id}")
        require(field["selected_emitted"] is True, f"field not selected emitted: {field_id}")
        require(field["theorem_derived"] is True, f"field not theorem derived: {field_id}")
    require(source["observed_data_used_as_selector"] is False, "source selector guard missing")
    require(source["target_fitting_used"] is False, "source target-fitting guard missing")

    require(
        nogo["status"] == "SECTOR_BLIND_FIRST_RESPONSE_MAGNITUDE_DERIVATION_REJECTED",
        "no-go status mismatch",
    )
    require(nogo["theorem"]["proved"] is True, "no-go theorem not proved")
    evidence = nogo["evidence"]
    require(evidence["H1_u_equals_H1_e"] is True, "u/e H1 equality missing")
    require(evidence["H1_d_equals_H1_nuD"] is True, "d/nuD H1 equality missing")
    require(evidence["all_trace_norm_invariant_tuples_identical"] is True, "invariants not degenerate")
    require(evidence["u_e_magnitude_distinct"] is True, "u/e magnitude distinction missing")
    require(evidence["u_d_e_magnitudes_not_all_equal"] is True, "magnitude distinction missing")
    frob = evidence["accepted_common_scale_frobenius_magnitudes"]
    require(frob["u"] > frob["d"] > frob["e"], "unexpected Frobenius magnitude ordering")
    require(nogo["observed_data_used_as_selector"] is False, "no-go selector guard missing")
    require(nogo["target_fitting_used"] is False, "no-go target-fitting guard missing")

    require(
        projection["status"] == "MAGNITUDE_DERIVATION_REDUCED_TO_SELECTED_PROJECTION_AND_THRESHOLD_RESPONSE",
        "projection requirement status mismatch",
    )
    require(projection["current_rtheta_state"]["solve_contract_closed"] is True, "Rtheta contract not closed")
    for key in ["selected_routec_galerkin_solve_closed", "Pi_Rtheta_closed", "profile_response_closed"]:
        require(projection["current_rtheta_state"][key] is False, f"Rtheta state overclosed: {key}")
    require(
        projection["current_value_profile_state"]["accepted_common_scale_values_for_SM_parity"] is True,
        "SM-parity values missing",
    )
    require(
        projection["current_value_profile_state"]["accepted_common_scale_values_for_true_precision"] is False,
        "true precision overaccepted",
    )
    require(
        projection["current_value_profile_state"]["surrogate_precision_scaffold_closed"] is True,
        "surrogate precision scaffold missing",
    )
    require(
        projection["current_value_profile_state"]["accepted_for_true_precision_equivalence"] is False,
        "precision equivalence overaccepted",
    )
    require(projection["closure_claimed"] is False, "projection requirement overclaimed")

    require(decision["status"] == "SOURCE_LAYER_CLOSED_MAGNITUDE_LAYER_OPEN", "decision status mismatch")
    require(decision["same_source_yukawa_source_layer_closed"] is True, "decision source layer not closed")
    require(decision["sector_blind_first_response_magnitude_no_go_proved"] is True, "decision no-go missing")
    require(decision["dynamic_QaSU3_first_response_layer_closed"] is True, "decision dynamic layer missing")
    require(decision["accepted_common_scale_values_for_SM_parity"] is True, "decision SM-parity missing")
    for key in [
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "Pi_Rtheta_or_equivalent_projection_kernel_closed",
        "threshold_mass_scheme_profile_response_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["minimal_next_actions"]) == 3, "decision next-action count mismatch")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["same_source_yukawa_source_layer"] is True, "cutset source missing")
    require(cutset["closed_now"]["sector_blind_first_response_no_go"] is True, "cutset no-go missing")
    require(cutset["closed_now"]["dynamic_QaSU3_first_response_imported"] is True, "cutset dynamic import missing")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["same_source_yukawa_source_layer_closed"] is True, "candidate final source missing")
    require(final["sector_blind_first_response_magnitude_no_go_proved"] is True, "candidate final no-go missing")
    for key in [
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "Pi_Rtheta_or_equivalent_projection_kernel_closed",
        "threshold_mass_scheme_profile_response_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["same_source_yukawa_source_layer_closed"] is True, "certificate source missing")
    require(cert["sector_blind_first_response_magnitude_no_go_proved"] is True, "certificate no-go missing")
    require(cert["accepted_Yukawa_magnitudes_as_no_knob_predictions"] is False, "certificate magnitudes overclosed")
    require("same-source Yukawa source layer closed : true" in note, "note missing source closure")
    require("accepted magnitudes no-knob closed     : false" in note, "note missing magnitude guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
