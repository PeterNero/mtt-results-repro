from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraltwoprimitiveprofilevalueclosure"
STATUS = "MTT_SELECTED_NEUTRAL_TWO_PRIMITIVE_PROFILE_VALUES_CLOSED_STRICT_SOURCE_AND_COVARIANCE_OPEN"
NEXT = "MTT_Selected_NeutralSmoothDeterminantLineHolonomyAndAnchoredScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_two_primitive_profile_values.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralTwoPrimitiveProfileValueClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require(packet["profile_policy"]["continuous_calibration_input_count"] == 2, "primitive count changed")
    values = packet["physical_values"]
    require(abs(values["mass_squared_eV2"][0]) < 1e-18, "m1 not zero")
    require(abs(values["mass_squared_eV2"][1]-7.49e-5) < 1e-17, "dm21 changed")
    require(abs(values["mass_squared_eV2"][2]-0.002513) < 1e-17, "dm31 changed")
    require(0.058 < values["sum_masses_eV"] < 0.060, "mass sum changed")
    require(packet["row_counts"]["total_rows_filled"] == cert["total_rows_filled"] == 36, "row count changed")
    for family in packet["filled_rows"].values():
        require(all(row["filled"] for row in family), "unfilled row")
    boundary = packet["closure_boundary"]
    for key in ["two_primitive_profile_numerical_closure", "absolute_neutrino_masses_filled_at_profile_tier", "Dirac_Yukawa_rows_filled_at_profile_tier"]:
        require(boundary[key] is True, f"not closed: {key}")
    for key in ["strict_MTT_source_for_phi_nu", "strict_MTT_source_for_A_nu_or_mu_nu", "Dirac_ontology_selected_by_MTT", "normal_ordering_selected_by_MTT", "Majorana_phases_or_0nu2beta", "uncertainty_covariance_propagated"]:
        require(boundary[key] is False, f"overclosed: {key}")
    require(packet["observed_data_used_as_selector"] is False, "geometry selected by data")
    require(packet["observed_data_used_as_profile_calibration"] is True and packet["target_fitting_used"] is True, "calibration hidden")
    for phrase in ["measured-profile closure", "All 36", "do not select", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"primitives": cert["continuous_profile_primitives"], "rows": cert["total_rows_filled"], "masses_eV": cert["masses_eV"], "sum_eV": cert["sum_masses_eV"], "next": NEXT}, indent=2))
    print("neutral two-primitive profile value audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
