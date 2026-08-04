"""Audit the first measured reference-data values fill."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_reference_data_values_fill.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_reference_data_values_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Reference_Data_Values_Fill_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_reference_data_values_fill.py"

STATUS = "MTT_SM_EQUIVALENCE_REFERENCE_DATA_VALUES_FILL_BUILT_PARTIAL_REPLAY_SEED"
NEXT = "MTT_SM_Equivalence_Tree_Level_Replay_Seed_v1"
TOL = 1e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mass_gev(value: dict) -> float:
    if value["units"] == "MeV":
        return value["central_value"] / 1000.0
    if value["units"] == "GeV":
        return value["central_value"]
    raise AssertionError(f"bad mass unit: {value['units']}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["retrieval_date"] == "2026-05-25", "retrieval date mismatch")

    values = data["reference_values"]
    masses = values["masses"]
    constants = values["constants"]
    yuks = values["diagonal_yukawa_magnitudes"]
    for key in ["e", "mu", "tau", "u", "d", "s", "c", "b", "t", "H", "W", "Z"]:
        require(key in masses, f"mass missing: {key}")
        require(masses[key]["source_key"] == "PDG_2025", f"wrong mass source: {key}")
        require(masses[key]["used_as_source_selector"] is False, f"mass source selector: {key}")
        require(masses[key]["units"] in ["MeV", "GeV"], f"bad units: {key}")
        require(masses[key]["uncertainty"]["plus"] >= 0, f"uncertainty missing: {key}")

    for key in ["G_F", "alpha", "v_from_G_F"]:
        require(key in constants, f"constant missing: {key}")
        require(constants[key]["used_as_source_selector"] is False, f"constant selector: {key}")

    expected_v = 1.0 / math.sqrt(math.sqrt(2.0) * constants["G_F"]["central_value"])
    require(abs(constants["v_from_G_F"]["central_value"] - expected_v) <= TOL, "v formula mismatch")

    for key in ["u", "c", "t", "d", "s", "b", "e", "mu", "tau"]:
        require(key in yuks, f"Yukawa missing: {key}")
        expected = math.sqrt(2.0) * mass_gev(masses[key]) / constants["v_from_G_F"]["central_value"]
        require(abs(yuks[key]["central_value"] - expected) <= TOL, f"Yukawa formula mismatch: {key}")
        require(yuks[key]["used_as_source_selector"] is False, f"Yukawa selector: {key}")

    slots = data["slot_values"]
    require(slots["yukawa.Y_u_Y_d_Y_e"]["status"] == "PARTIAL_FILLED_DIAGONAL_MAGNITUDE_SEED", "Yukawa status mismatch")
    require(slots["higgs.v_mh_lambda_or_potential"]["status"] == "PARTIAL_FILLED", "Higgs status mismatch")
    require(slots["gauge.alpha_1_alpha_2_alpha_3"]["status"] == "PARTIAL_FILLED_LOW_ENERGY_ANCHORS_ONLY", "gauge status mismatch")
    for key in ["mixing.CKM", "mixing.PMNS", "neutrino.yukawa_or_mass_splittings"]:
        require(slots[key]["status"] == "OPEN_NOT_FILLED_IN_FIRST_PACKET", f"slot overfilled: {key}")

    quality = data["quality_flags"]
    require(quality["values_filled"] is True, "values not filled")
    require(quality["partial_packet"] is True, "partial status missing")
    require(quality["all_values_have_sources"] is True, "source flag missing")
    require(quality["correlation_matrices_included"] is False, "correlations overclaimed")
    require(quality["common_RG_scale_transport_done"] is False, "RG overclaimed")
    require(quality["full_complex_Yukawa_matrices_filled"] is False, "Yukawa overclaimed")
    require(quality["CKM_filled"] is False, "CKM overclaimed")
    require(quality["PMNS_filled"] is False, "PMNS overclaimed")
    require(quality["gauge_running_triplet_filled"] is False, "gauge triplet overclaimed")

    closes = data["what_closes_now"]
    for key in [
        "first_reference_values_packet_frozen",
        "charged_fermion_and_quark_mass_seed_filled",
        "Higgs_W_Z_mass_seed_filled",
        "CODATA_alpha_and_G_F_anchor_filled",
        "tree_level_diagonal_yukawa_seed_computed",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "full_CKM_reference_packet",
        "full_PMNS_and_neutrino_reference_packet",
        "gauge_running_triplet_alpha1_alpha2_alpha3",
        "common_RG_scale_transport",
        "full_complex_Yukawa_matrices",
        "numeric_tree_level_replay",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("intentionally partial" in note, "note partial guard missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
