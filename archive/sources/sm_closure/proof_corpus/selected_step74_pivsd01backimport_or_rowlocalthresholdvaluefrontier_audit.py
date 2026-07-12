"""Audit Step74 Pi/VSD01 backimport and row-local threshold-value frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKIMPORT_PACKET = PACKET_DIR / "step74_pi_vsd01_backimport.packet.json"
ROW_RECHECK_PACKET = PACKET_DIR / "step74_ten_rowlocal_frontier_recheck.packet.json"
VALUE_FRONTIER_PACKET = PACKET_DIR / "step74_threshold_value_frontier.packet.json"
CUTSET_PACKET = PACKET_DIR / "step74_next_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step74_PiVSD01Backimport_or_RowLocalThresholdValueFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STEP74_PIVSD01BACKIMPORT_OR_ROWLOCALTHRESHOLDVALUEFRONTIER_"
    "BUILT_SOURCE_SIDE_RETIRED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    backimport = load(BACKIMPORT_PACKET)
    row_recheck = load(ROW_RECHECK_PACKET)
    value_frontier = load(VALUE_FRONTIER_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("backimport", backimport),
        ("row_recheck", row_recheck),
        ("value_frontier", value_frontier),
        ("cutset", cutset),
    ]:
        guard(packet, label)
        require(packet.get("closure_claimed") is True, f"{label} should claim this frontier theorem")

    require(backimport["operator_domain_closed"] is True, "operator domain not closed")
    retired = backimport["retired_as_active_domain_blockers"]
    for key in [
        "Pi_Rtheta",
        "stationary_sector_transfer",
        "dotD_alpha1_transport",
        "matter_slot_routing",
        "primitive_C1_overlap_contractions",
        "VSD01_source_assembly",
        "VSD01_dynamic_overlap",
        "static_U10_Ubar5_1M_source",
    ]:
        require(retired[key] is True, f"domain blocker not retired: {key}")
    local = backimport["step73_local_flags_still_false"]
    for key in [
        "selected_HYM_projector_values_promoted",
        "selected_sector_transfer_values_emitted",
        "selected_retarded_overlap_derivative_rows_emitted",
    ]:
        require(local[key] is False, f"Step73 local flag overclosed: {key}")

    require(row_recheck["row_count"] == 10, "row count mismatch")
    require(row_recheck["operator_domain_ready_row_count"] == 10, "operator-ready row count mismatch")
    for key in [
        "accepted_rowlocal_source_row_count",
        "accepted_prefactor_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(row_recheck[key] == 0, f"row recheck overaccepted {key}")
    for row in row_recheck["rows"]:
        require(row["operator_domain_ready_after_backimport"] is True, f"operator domain not ready for {row['omega_id']}")
        require(row["rowlocal_numeric_prefactor_ready"] is False, f"prefactor overready for {row['omega_id']}")
        require(row["accepted_as_rowlocal_source_row"] is False, f"rowlocal accepted for {row['omega_id']}")
        require(row["accepted_as_prefactor_source_row"] is False, f"prefactor accepted for {row['omega_id']}")
        require(row["accepted_as_omega_source_row"] is False, f"Omega accepted for {row['omega_id']}")
        require("selected L_rowlocal row-local HYM/overlap prefactor" in row["missing_value_rows"], "missing L row guard")
        require("selected T_scheme threshold/scale/scheme prefactor" in row["missing_value_rows"], "missing T row guard")
    h_row = next(row for row in row_recheck["rows"] if row["omega_id"] == "Omega_H.lambda")
    require("lambda_H H-sector source value payload" in h_row["missing_value_rows"], "lambda_H guard missing")

    require(value_frontier["same_branch_scale_scheme_loop_convention_closed"] is True, "scheme convention not closed")
    require(value_frontier["threshold_matching_source_rows_closed_at_admitted_external_tier"] is True, "threshold external tier missing")
    require(value_frontier["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"] is True, "mass scheme external tier missing")
    require(value_frontier["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile missing")
    require(value_frontier["post_pi_external_replay_ready"] is True, "post-Pi replay not ready")
    require(value_frontier["Rtheta_readiness_present_count"] == 8, "readiness count mismatch")
    for key in [
        "selected_internal_Rtheta_threshold_mass_derivation_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
    ]:
        require(value_frontier[key] is False, f"value frontier overclosed: {key}")
    for key in [
        "accepted_coefficient_value_count",
        "selected_internal_value_emission_count",
        "selected_universal_parameter_count",
    ]:
        require(value_frontier[key] == 0, f"value frontier overaccepted {key}")

    for phrase in [
        "Pi_Rtheta/operator-domain source ownership",
        "stationary sector transfer and rho_s layer",
        "matter-slot routing/static U10-Ubar5-1M readout",
    ]:
        require(phrase in cutset["not_missing_anymore"], f"cutset not-missing missing {phrase}")
    for phrase in [
        "selected internal threshold response functional instantiation",
        "ten selected L_rowlocal HYM/overlap prefactor rows",
        "ten selected T_scheme threshold/scale rows",
        "lambda_H H-sector source value row",
        "strict Omega source row acceptance",
    ]:
        require(phrase in cutset["still_missing"], f"cutset still-missing missing {phrase}")
    for phrase in [
        "loop back to Step73 as if Pi_Rtheta/operator source ownership were still open",
        "promote admitted external threshold rows as no-knob internal rows",
        "use SM-parity replay prefactors as source selectors",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "step73_diagonal_hym_green_subsource_closed",
        "operator_domain_side_closed_after_backimport",
        "Pi_Rtheta_closed",
        "stationary_sector_transfer_closed",
        "dotD_alpha1_transport_subgate_closed",
        "matter_slot_routing_closed",
        "primitive_C1_overlap_contractions_closed",
        "VSD01_source_assembly_subgate_closed",
        "VSD01_dynamic_overlap_subgate_closed",
        "static_U10_Ubar5_1M_source_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "post_pi_external_replay_ready",
    ]:
        require(decision[key] is True, f"decision missing closure {key}")
        require(cert[key] is True, f"certificate missing closure {key}")
    for key in [
        "accepted_rowlocal_source_row_count",
        "accepted_prefactor_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")
    for key in [
        "selected_internal_threshold_response_functional_instantiated",
        "selected_internal_threshold_mass_derivation_closed",
        "selected_L_rowlocal_rows_emitted",
        "selected_T_scheme_rows_emitted",
        "lambda_H_value_row_emitted",
        "strict_omega_acceptance_closed",
        "selected_matrix_level_mixing_extension_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")

    for phrase in [
        "operator-domain side closed after backimport : true",
        "accepted row-local source rows              : 0",
        "selected L_rowlocal rows                    : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
