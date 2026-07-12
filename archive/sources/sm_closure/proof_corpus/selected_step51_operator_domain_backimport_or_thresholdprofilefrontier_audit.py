"""Audit Step51 operator-domain backimport / threshold-profile frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step51_operator_domain_backimport_or_thresholdprofilefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKIMPORT = PACKET_DIR / "step51_operator_domain_backimport.packet.json"
OMEGA_RECHECK = PACKET_DIR / "step51_omega_value_frontier_recheck.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step51_next_threshold_profile_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step51_OperatorDomainBackimport_or_ThresholdProfileFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP51_OPERATOR_DOMAIN_BACKIMPORT_CLOSED_THRESHOLD_PROFILE_ROWS_OPEN"
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    backimport = load(BACKIMPORT)
    omega = load(OMEGA_RECHECK)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "backimport theorem not proved")

    for packet in [data, backimport, omega, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(backimport["supersedes_step50_old_cutset_for_rtheta_domain"] is True, "Step50 not superseded")
    require(backimport["operator_domain_closed_for_Rtheta_value_evaluator"] is True, "operator domain not closed")
    closed = backimport["closed_operator_domain_fields"]
    for key in [
        "Pi_Rtheta",
        "coefficient_functional_domain",
        "selected_dynamic_operator_source_owner",
        "stationary_sector_transfer",
        "selected_stationary_rho_s",
        "selected_sector_basis_projector_contract",
        "selected_Riesz_Green_stationary",
        "dotD_alpha1_transport_subgate",
        "dynamic_matter_overlap_operator_packet",
        "VSD01_source_assembly_subgate",
        "primitive_C1_overlap_contractions",
        "matter_slot_routing",
    ]:
        require(closed[key] is True, f"closed operator-domain field missing: {key}")

    require(omega["operator_domain_closed_for_Rtheta"] is True, "omega did not import operator domain")
    require(omega["selected_threshold_response_functional_instantiated"] is False, "threshold overclosed")
    require(omega["value_execution_readiness_present_count"] == 4, "readiness present mismatch")
    require(omega["value_execution_readiness_requirement_count"] == 9, "readiness requirement mismatch")
    require(omega["accepted_coefficient_value_count"] == 0, "coefficient rows overaccepted")
    require(omega["accepted_lambda_H_value"] is False, "lambda_H overaccepted")
    require(omega["omega_source_rows_accepted_now"] == 0, "omega source rows overaccepted")
    require(omega["blocking_failures"] == [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ], "blocking failures mismatch")
    for key in [
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(omega[key] is False, f"omega overclosed: {key}")

    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")
    require(
        frontier["recommended_next_from_threshold_packet"] == NEXT,
        "threshold packet next not imported",
    )
    still = frontier["ordered_remaining_blockers"]
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
    ]:
        require(still[key] is True, f"frontier missing blocker: {key}")

    decision = data["closure_decision"]
    for key in [
        "operator_domain_closed_for_Rtheta_value_evaluator",
        "Pi_Rtheta_closed",
        "selected_dynamic_operator_source_owner_closed",
        "coefficient_functional_domain_closed",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    for key in [
        "selected_lambda_H_row_closed",
        "threshold_profile_value_source_rows_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "operator domain closed for Rtheta      : true",
        "Pi_Rtheta closed                       : true",
        "selected dynamic operator owner closed : true",
        "accepted Rtheta coefficient rows       : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
