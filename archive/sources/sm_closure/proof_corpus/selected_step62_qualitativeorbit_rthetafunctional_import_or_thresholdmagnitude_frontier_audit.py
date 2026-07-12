"""Audit Step62 qualitative-orbit/Rtheta-functional import frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step62_qualitativeorbit_rthetafunctional_import_or_thresholdmagnitude_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step62_qualitative_orbit_rtheta_import.packet.json"
CUTSET = PACKET_DIR / "step62_threshold_magnitude_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step62_QualitativeOrbitRThetaFunctionalImport_or_ThresholdMagnitudeFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STEP62_QUALITATIVE_ORBIT_RTHETA_FUNCTIONAL_IMPORTED_"
    "THRESHOLD_MAGNITUDE_FRONTIER_OPEN"
)
NEXT = "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    packet = load(IMPORT_PACKET)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, packet, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    closed = packet["closed_now"]
    for key in [
        "chain_integrity_no_loopback",
        "diagonal_End0_HYM_payload_support_closed",
        "identity_free_unscaled_pure_Weyl_rows_closed",
        "lambda_static_orbit_selected",
        "second_order_orbit_matrix_packet_closed",
        "qualitative_SM_orbit_closure_closed",
        "Rtheta_scalar_value_functional_source_domain_closed",
        "ten_scalar_row_codomain_aligned",
    ]:
        require(closed[key] is True, f"closed flag missing: {key}")

    counts = packet["still_open_counts"]
    require(counts["accepted_numerical_scalar_rows"] == 0, "numerical scalar rows overaccepted")
    require(counts["no_knob_numerical_rows_emitted"] is False, "no-knob rows overemitted")
    require(counts["selected_Rtheta_scalar_rows_emitted"] is False, "Rtheta scalar rows overemitted")

    frontier = cutset["frontier_interpretation"]
    require(frontier["not_a_loopback"] is True, "frontier loopback guard missing")
    require(frontier["primitive_route_has_advanced_to_qualitative_orbit"] is True, "primitive advance missing")
    require(frontier["Rtheta_functional_domain_ready_but_values_absent"] is True, "Rtheta domain/value distinction missing")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    remains = cutset["still_open"]
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "magnitude_bearing_projection_weights",
        "selected_threshold_response_functional_instantiation",
        "accepted_numerical_Yukawa_rows",
        "lambda_H_value",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    decision = data["closure_decision"]
    for key in [
        "qualitative_orbit_imported",
        "Rtheta_scalar_value_functional_source_domain_closed",
        "ten_scalar_row_codomain_aligned",
        "diagonal_End0_HYM_payload_support_closed",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
        require(cert[key] is True, f"certificate close missing: {key}")

    for key in [
        "HYM_selected_sector_payload_closed",
        "no_knob_numerical_rows_emitted",
        "selected_Rtheta_scalar_rows_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_numerical_scalar_rows"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_numerical_scalar_rows"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "identity-free pure Weyl rows closed           : true",
        "qualitative three-family / CP layer closed    : true",
        "Rtheta scalar functional source/domain closed : true",
        "accepted numerical scalar rows                : 0",
        "selected Rtheta scalar rows emitted           : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
