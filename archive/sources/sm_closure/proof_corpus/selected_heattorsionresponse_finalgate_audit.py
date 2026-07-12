"""Audit selected finite heat/torsion response final-gate artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_heattorsionresponse_finalgate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESPONSE = PACKET_DIR / "selected_finite_heat_spectrum_response.packet.json"
SLOT_CLOSURE = PACKET_DIR / "finite_determinant_heat_torsion_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_eight_slot_true_equivalence_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HeatTorsionResponse_FinalGate_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HEATTORSIONRESPONSE_FINALGATE_BUILT_FINAL_OPERATOR_SLOT_CLOSED"
NEXT = "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1"
SLOT = "finite_determinant_heat_spectrum_or_torsion_response"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(a: float, b: float, message: str) -> None:
    require(math.isclose(a, b, rel_tol=0.0, abs_tol=1e-12), message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    response = load(RESPONSE)
    slot = load(SLOT_CLOSURE)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    for key, value in response["proof_inputs"].items():
        require(value is True, f"proof input false: {key}")
    require(response["slot"] == SLOT and response["slot_closes"] is True, "response does not close slot")
    require(response["source_contract"]["basis_dimension_per_sector"] == 27, "basis dimension mismatch")
    require(response["source_contract"]["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"], "sector order mismatch")
    require(response["source_contract"]["family_sectors"] == ["Q", "u", "d", "L", "e", "N"], "family sectors mismatch")
    require(response["source_contract"]["zero_cluster_indices"] == [12, 13, 14], "zero cluster mismatch")

    model_gap = 4.0 * math.pi * math.pi / 9.0
    scalar = response["finite_spectrum_convention"]["scalar_F3xF3_positive_eigenvalues"]
    close(scalar[0]["eigenvalue"], model_gap, "scalar gap mismatch")
    close(scalar[1]["eigenvalue"], 2.0 * model_gap, "scalar double gap mismatch")
    require(scalar[0]["multiplicity"] == 4 and scalar[1]["multiplicity"] == 4, "scalar multiplicity mismatch")

    family = response["finite_spectrum_convention"]["family_sector_positive_eigenvalues"]
    h_sector = response["finite_spectrum_convention"]["H_sector_positive_eigenvalues"]
    close(family[0]["eigenvalue"], model_gap, "family gap mismatch")
    close(family[1]["eigenvalue"], 2.0 * model_gap, "family double gap mismatch")
    require(family[0]["multiplicity"] == 12 and family[1]["multiplicity"] == 12, "family multiplicity mismatch")
    require(h_sector[0] == {"eigenvalue": 1.0, "multiplicity": 2}, "H eta spectrum mismatch")
    close(h_sector[1]["eigenvalue"], model_gap, "H gap mismatch")
    close(h_sector[2]["eigenvalue"], 2.0 * model_gap, "H double gap mismatch")

    inv = response["finite_invariants"]
    require(inv["family_sector_kernel_dimension"] == 3, "family kernel mismatch")
    require(inv["family_sector_positive_dimension"] == 24, "family positive dimension mismatch")
    require(inv["H_sector_kernel_dimension"] == 1, "H kernel mismatch")
    require(inv["H_sector_positive_dimension"] == 26, "H positive dimension mismatch")
    require(inv["total_sector_count"] == 7, "sector count mismatch")
    require(inv["total_dimension"] == 189, "total dimension mismatch")
    require(inv["total_kernel_dimension"] == 19, "total kernel mismatch")
    require(inv["total_positive_dimension"] == 170, "total positive mismatch")
    require(inv["finite_spectral_zeta_at_0_positive_count"] == 170, "zeta count mismatch")

    total_positive = [model_gap] * 84 + [2.0 * model_gap] * 84 + [1.0, 1.0]
    close(inv["total_reduced_heat_trace_t1"], sum(math.exp(-x) for x in total_positive), "total reduced heat mismatch")
    close(inv["total_heat_trace_t1"], 19 + sum(math.exp(-x) for x in total_positive), "total heat mismatch")
    close(inv["total_log_pseudodeterminant"], sum(math.log(x) for x in total_positive), "total logdet mismatch")
    require(inv["total_reduced_heat_trace_t1"] > 0, "heat not positive")
    require(inv["total_log_pseudodeterminant"] > 0, "logdet not positive")

    for guard in [
        "smooth analytic torsion",
        "continuum zeta-regularized determinant beyond the selected finite Galerkin layer",
        "selected dotD_alpha1 source identity",
        "actual dynamic Qa/SU3 operator packet",
        "no-knob constants derivation",
    ]:
        require(guard in response["scope"]["does_not_close"], f"missing guard: {guard}")

    require(slot["filled_slot"] == SLOT, "slot closure filled wrong slot")
    result = slot["closure_result"]
    require(result["finite_determinant_heat_spectrum_or_torsion_response_closed"] is True, "slot not closed")
    require(result["finite_heat_spectrum_response_emitted"] is True, "finite heat missing")
    require(result["finite_positive_complement_pseudodeterminant_emitted"] is True, "pseudodeterminant missing")
    require(result["smooth_analytic_torsion_closed"] is False, "analytic torsion overclosed")
    require(result["full_S2_value_emission_closed"] is False, "full S2 overclosed")
    require(result["selected_dotD_alpha1_source_identity_closed"] is False, "dotD overclosed")
    require(result["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")
    status = slot["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(status["filled_operator_slot_count"] == 8, "filled slot count mismatch")
    require(status["remaining_missing_slot_count"] == 0, "remaining slot count mismatch")
    require(status["missing_slots"] == [], "missing slots should be empty")
    require(SLOT in status["filled_slots"], "heat slot not filled")

    require(frontier["operator_source_slots_closed"] == 8, "frontier closed count mismatch")
    require(frontier["operator_source_slots_remaining"] == 0, "frontier remaining count mismatch")
    require(frontier["remaining_slots"] == [], "frontier remaining mismatch")
    require(frontier["source_slot_layer_closed"] is True, "source layer not closed")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")
    require("actual dynamic Qa/SU3 operator packet" in frontier["true_SM_equivalence_still_requires"], "dynamic frontier missing")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 8, "candidate closed count mismatch")
    require(closure["operator_source_slots_remaining"] == 0, "candidate remaining count mismatch")
    require(closure["finite_determinant_heat_spectrum_or_torsion_response_closed"] is True, "candidate slot not closed")
    require(closure["all_operator_source_slots_closed"] is True, "candidate all slots not closed")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["closure_claimed"] is True, "candidate should claim finite slot closure")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic blocker missing")

    require("finite positive-complement heat trace and pseudodeterminant" in note, "note finite response missing")
    require("This closes all eight operator-source slots" in note, "note count missing")
    require("It does not close smooth analytic torsion" in note, "note guard missing")
    require(NEXT in note, "note next missing")

    for packet in [data, response, slot, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
