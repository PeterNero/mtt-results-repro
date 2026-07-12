from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
STATUS = "MTT_SELECTED_NEUTRAL_INTERNAL_DIMENSIONLESS_RESPONSE_CLOSED_PHYSICAL_UNIT_OPEN"
NEXT = "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_internal_dimensionless_response.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    require(abs(packet["neutral_internal_response"]["a_internal"] - 0.34195899479289005) < 1e-15, "a_internal changed")
    require(packet["neutral_internal_response"]["identity_H1_equals_dY_Y0dag_plus_Y0_dYdag"] is True, "response identity failed")
    require(packet["neutral_internal_response"]["six_nonzero_entries_equal_minus_2a"] is True, "nonzero pattern changed")
    require(packet["neutral_internal_response"]["three_exact_zero_entries"] is True, "zero pattern changed")
    require(packet["source_provenance"]["same_source_selected_field_count"] == packet["source_provenance"]["same_source_required_field_count"] == 7, "same-source fields changed")
    require(packet["internal_dimensionless_rows_closed"] == 9, "internal rows changed")
    require(all(row["selected_emitted"] and row["theorem_derived"] and row["same_source"] for row in packet["neutral_internal_H1_rows"]), "unselected row")
    require(all(not row["physical_unit_attached"] and not row["dimensionful_mass_entry"] for row in packet["neutral_internal_H1_rows"]), "physical row overclosed")

    closes = packet["what_closes_here"]
    for key in ["selected_internal_dimensionless_neutral_baseline_Y0", "selected_internal_dimensionless_neutral_correction_dY", "selected_internal_dimensionless_neutral_response_H1", "combined_internal_overlap_amplitude"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["decomposition_into_action_cost_S_gamma_and_prefactor_A_gamma", "same_scheme_physical_unit", "dimensionful_neutral_mass_matrix", "nil_anchor_projector", "Dirac_only_action_completeness"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["readiness_subfields_closed"] == 9 and packet["readiness_subfields_total"] == 14, "readiness changed")
    require(packet["neutral_overlap_OK_gates_closed"] == 6 and packet["neutral_overlap_OK_gates_total"] == 9, "OK count changed")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical values overclosed")
    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    for field in ["dimensionful_M_D_3x3_closed", "dimensionful_M_L_3x3_closed", "dimensionful_M_R_3x3_closed", "absolute_normalization_and_scheme_closed", "selected_neutral_operator_accepted", "U5_closed"]:
        require(packet[field] is False and cert[field] is False, f"overclosed: {field}")
    for phrase in ["a_int = 0.34195899479289005", "All nine `H1_nu` rows", "internal dimensionless normalization", "It is not a neutrino mass", "`9/14`", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"a_internal": packet["neutral_internal_response"]["a_internal"], "internal_rows": "9/9", "same_source_fields": "7/7", "readiness": "9/14", "neutral_OK_gates": "6/9", "physical_value_fields": 0, "next": NEXT}, indent=2))
    print("selected neutral internal dimensionless response audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
