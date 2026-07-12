"""Audit Step68 theta exponent weights / prefactor-threshold frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INDEX_IMPORT_PACKET = PACKET_DIR / "step68_qutrit_quotient_index_import.packet.json"
EXPONENT_PACKET = PACKET_DIR / "step68_selected_theta_exponent_weight_rows.packet.json"
OMEGA_REDUCTION_PACKET = PACKET_DIR / "step68_omega_clause_reduction_after_exponent_weights.packet.json"
CUTSET_PACKET = PACKET_DIR / "step68_prefactor_threshold_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step68_ThetaExponentWeights_or_PrefactorThresholdFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP68_THETA_EXPONENT_WEIGHTS_CLOSED_PREFACTOR_THRESHOLD_FRONTIER_OPEN"
NEXT = "MTT_Selected_HYMThresholdPrefactorRows_or_OmegaScalarExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    index_import = load(INDEX_IMPORT_PACKET)
    exponent = load(EXPONENT_PACKET)
    omega = load(OMEGA_REDUCTION_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, index_import, exponent, omega, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(index_import["selected_qutrit_quotient_index"] == "2/3", "qutrit index mismatch")
    require(index_import["selected_shared_line_index"] == "1/3", "shared line mismatch")
    require(index_import["closed_as_dimensionless_index"] is True, "qutrit index not closed")
    require(index_import["not_a_positive_spectrum"] is True, "2/3 overpromoted as spectrum")
    require(index_import["not_a_threshold_matching_row"] is True, "2/3 overpromoted as threshold")
    require(index_import["not_a_mass_scheme_row"] is True, "2/3 overpromoted as mass scheme")

    require(abs(exponent["epsilon_theta"] - math.exp(-2 * math.pi)) < 1e-18, "epsilon mismatch")
    require(exponent["family_gap_ratios"] == [-2, -1, 1], "family gap ratios mismatch")
    require(exponent["charged_exponent_weight_row_count"] == 9, "charged row count mismatch")
    require(exponent["all_10_exponent_weight_rows_constructed"] is True, "ten exponent shell mismatch")
    require(exponent["magnitude_bearing_projection_weights_closed_at_exponent_tier"] is True, "exponent weights not closed")
    require(exponent["generation_resolved_exponent_rows_closed"] is True, "generation exponent rows not closed")
    require(exponent["accepted_full_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(exponent["accepted_internal_scalar_value_row_count"] == 0, "scalar values overaccepted")
    require(exponent["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")

    rows = exponent["charged_exponent_weight_rows"]
    by_key = {(row["sector"], row["generation"]): row for row in rows}
    expected = {
        ("u", 1): "2",
        ("u", 2): "1",
        ("u", 3): "0",
        ("d", 1): "2",
        ("d", 2): "1",
        ("d", 3): "2/3",
        ("e", 1): "2",
        ("e", 2): "1",
        ("e", 3): "2/3",
    }
    for key, value in expected.items():
        row = by_key[key]
        require(row["theta_exponent"] == value, f"wrong exponent for {key}")
        require(row["accepted_as_exponent_weight_row"] is True, f"exponent not accepted for {key}")
        require(row["accepted_as_full_omega_source_row"] is False, f"Omega overaccepted for {key}")
        require(row["accepted_as_internal_scalar_value"] is False, f"value overaccepted for {key}")
    require(by_key[("d", 3)]["qutrit_quotient_floor"] == "2/3", "d qutrit floor missing")
    require(by_key[("e", 3)]["qutrit_quotient_floor"] == "2/3", "e qutrit floor missing")
    require(by_key[("u", 3)]["qutrit_quotient_floor"] == "0", "u floor overapplied")

    higgs = exponent["higgs_exponent_weight_row"]
    require(higgs["theta_exponent"] == "1/3", "Higgs exponent mismatch")
    require(higgs["accepted_as_higgs_exponent_weight"] is True, "Higgs exponent not accepted")
    require(higgs["lambda_H_value_row_emitted"] is False, "Higgs value overemitted")

    require(omega["closed_now"]["magnitude_bearing_projection_weights"] is True, "Omega clause not closed")
    require(omega["closed_now"]["generation_resolved_exponent_weight_rows"] is True, "generation clause not closed")
    require(
        "magnitude_bearing_projection_weights" not in omega["still_missing_value_bearing_clauses"],
        "magnitude clause still listed as missing",
    )
    for key in [
        "accepted_vsd02_source_rows",
        "generation_resolved_threshold_source_rows",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "true_precision_scale_scheme_loop_convention",
        "full_profile_likelihood",
        "selected_higher_response_operator_payload",
        "sector_prefactor_rows",
        "lambda_H_prefactor_row",
    ]:
        require(omega["not_closed_by_step68"][key] is True, f"overclosed: {key}")
    require(omega["accepted_full_omega_source_row_count"] == 0, "Omega accepted rows overclosed")
    require(omega["value_rows_execute"] is False, "value rows executed too early")

    for phrase in [
        "selected HYM/threshold prefactor rows multiplying the exponent weights",
        "selected sector/full-S2 operator payload promotable to Omega rows",
        "selected same-branch threshold matching source rows",
        "selected same-branch mass-scheme conversion source rows",
        "selected lambda_H prefactor/value row",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing: {phrase}")
    for phrase in [
        "use diagnostic order-one factors as selected prefactors",
        "treat the 2/3 index as a positive determinant spectrum",
        "treat exponent weights as full scalar values",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "theta_overlap_anchor_closed",
        "qutrit_quotient_index_imported",
        "selected_family_exponent_ladder_closed",
        "generation_resolved_exponent_weight_rows_closed",
        "magnitude_bearing_projection_weights_closed_at_exponent_tier",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "hym_threshold_prefactor_rows_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "selected_higher_response_operator_payload_closed",
        "lambda_H_value_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_full_omega_source_row_count"] == 0, "decision Omega rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "decision scalar rows overaccepted")

    for phrase in [
        "qutrit quotient floor                 : 2/3",
        "Higgs shared-line exponent shell      : 1/3",
        "charged exponent rows emitted         : 9",
        "accepted Omega source rows            : 0",
        "accepted internal scalar values        : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
