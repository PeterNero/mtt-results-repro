"""Audit accepted Higgs decay covariance profile or first Qa/SU3 slot closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "accepted_higgs_decay_covariance_profile.packet.json"
FIRST_SLOT = PACKET_DIR / "first_qasu3_static_sector_route_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_profile_or_first_slot.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedHiggsDecayCovarianceProfile_or_FirstQaSU3SelectedSlotClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ACCEPTEDHIGGSDECAYCOVARIANCEPROFILE_OR_FIRSTQASU3SELECTEDSLOTCLOSURE_"
    "BUILT_SECTOR_PROFILE_AND_STATIC_SLOT_CLOSED_TRUE_EQUIV_OPEN"
)
NEXT = "MTT_Selected_HiggsProductionCovarianceProfile_or_DynamicQaSU3OperatorSlotClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    first_slot = load(FIRST_SLOT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    standard = profile["accepted_profile_standard"]
    require(profile["profile_scope"] == "Higgs_decay_sector_only", "profile scope mismatch")
    require(standard["required_rows"] == 9, "profile standard row count mismatch")
    require(standard["source_rows_and_labels_validated"] is True, "source label validation missing")
    require(standard["observed_data_forbidden_as_source_selector"] is True, "selector guard missing")
    validation = profile["linear_algebra_validation"]
    require(validation["row_count"] == 9, "profile row count mismatch")
    require(validation["correlation_symmetric"] is True, "correlation symmetry failed")
    require(validation["correlation_unit_diagonal"] is True, "correlation diagonal failed")
    require(validation["covariance_symmetric"] is True, "covariance symmetry failed")
    require(validation["positive_diagonal_variances"] is True, "positive variance check failed")
    require(validation["positive_semidefinite_with_tolerance"] is True, "PSD tolerance check failed")
    require(validation["covariance_min_eigenvalue_MeV2"] >= -standard["covariance_positive_semidefinite_with_tolerance"], "PSD bound failed")
    require(validation["covariance_rank_tol_1e_minus_14"] >= 8, "covariance rank unexpectedly low")
    acceptance = profile["acceptance_result"]
    require(acceptance["accepted_as_Higgs_decay_covariance_profile"] is True, "Higgs decay profile not accepted")
    require(acceptance["accepted_as_full_Higgs_likelihood_profile"] is False, "full Higgs likelihood overclaimed")
    require(acceptance["accepted_as_full_true_equivalence_profile"] is False, "true equivalence profile overclaimed")

    require(first_slot["slot_name"] == "static_QaSU3_sector_route_ZX_phase_shift_partition", "slot name mismatch")
    require(first_slot["slot_tier"] == "static_source_tier", "slot tier mismatch")
    value = first_slot["selected_slot_value"]
    require(value["Z_clock_phase_routes_to"] == ["u", "e"], "Z/clock route mismatch")
    require(value["X_shift_translation_routes_to"] == ["d", "nuD"], "X/shift route mismatch")
    require(value["matter_slot_partition"]["clock_phase_side"] == "10_M", "clock matter slot mismatch")
    require(value["matter_slot_partition"]["shift_non10_side"] == ["bar5_M", "1_M=N^c"], "shift matter slots mismatch")
    require("Dirac-neutrino" in value["oneM_Dirac_rule"], "1_M Dirac rule missing")
    proofs = first_slot["proof_inputs"]
    for key, closed in proofs.items():
        require(closed is True, f"slot proof input not closed: {key}")
    closure = first_slot["closure_result"]
    require(closure["first_selected_QaSU3_static_slot_closed"] is True, "first slot not closed")
    require(closure["selected_source_value_emitted"] is True, "selected source value not emitted")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic Qa/SU3 packet overclosed")

    require(decision["status"] == "HIGGS_DECAY_PROFILE_ACCEPTED_AND_FIRST_STATIC_QASU3_SLOT_CLOSED_TRUE_EQUIV_OPEN", "decision status mismatch")
    require(decision["route_A"]["accepted_Higgs_decay_covariance_profile_closed"] is True, "route A not closed")
    require(decision["route_A"]["full_Higgs_likelihood_profile_closed"] is False, "route A overclosed likelihood")
    require(decision["route_B"]["first_selected_QaSU3_static_slot_closed"] is True, "route B first slot not closed")
    require(decision["route_B"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "route B dynamic overclosed")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure_decision = data["closure_decision"]
    require(closure_decision["accepted_Higgs_decay_covariance_profile_closed"] is True, "candidate profile closure missing")
    require(closure_decision["first_selected_QaSU3_static_slot_closed"] is True, "candidate first slot closure missing")
    require(closure_decision["full_Higgs_likelihood_profile_closed"] is False, "candidate likelihood overclosed")
    require(closure_decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(closure_decision["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(closure_decision["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims full closure")
    require(data["what_closes_now"]["Higgs_decay_covariance_profile_sector_object"] is True, "profile close flag missing")
    require(data["what_closes_now"]["first_QaSU3_static_sector_route_slot"] is True, "slot close flag missing")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic gate missing")
    require(data["what_remains_open"]["true_SM_equivalence"] is True, "true equivalence gate missing")
    require("not a full Higgs likelihood function" in note, "note missing likelihood guard")
    require("static source-tier closure" in note, "note missing static-tier guard")

    for packet in [data, profile, first_slot, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
