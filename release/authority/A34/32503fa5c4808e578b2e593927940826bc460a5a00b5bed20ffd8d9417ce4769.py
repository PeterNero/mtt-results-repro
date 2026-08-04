from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralradialsecondvariationandvevcoordinatetheorem"
STATUS = "MTT_SELECTED_NEUTRAL_RADIAL_SECOND_VARIATION_CLOSED_HIGGS_INSERTION_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_radial_second_variation_and_vev_coordinate.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    radial = packet["radial_second_variation"]
    require(radial["second_variation_eigenvalues"] == [2.0, 2.0, 8.0] or all(abs(a-b)<1e-12 for a,b in zip(radial["second_variation_eigenvalues"],[2,2,8])), "second variation changed")
    require(radial["positive_semidefinite"] is True and radial["positive_definite"] is True, "positivity failed")
    require(radial["typed_as_physical_neutral_mass_Hessian"] is False, "Hessian overpromoted")
    hsource = packet["selected_H_sector_radial_source"]
    require(hsource["strict_tau_H_promoted"] is True and hsource["strict_r_H_promoted"] is True, "H radial source missing")
    require(hsource["H_to_neutral_insertion_map_emitted"] is False, "insertion overpromoted")
    require(hsource["identity_insertion_tau_H_accepted"] is False and hsource["identity_insertion_r_H_accepted"] is False, "identity shortcut accepted")
    require(packet["coordinate_trials"]["any_exact_selected_coordinate"] is False, "coordinate overselected")
    vev = packet["VEV_policy"]
    require(abs(vev["profile_standard_v_GeV"] - 246.21964023926205) < 1e-12, "profile VEV changed")
    require(vev["counts_as_neutrino_specific_parameter"] is False, "VEV double counted")
    require(vev["selected_by_strict_no_knob_MTT_source"] is False, "VEV overderived")
    closes = packet["what_closes_here"]
    for key in ["exact_positive_Gram_second_variation", "selected_H_radial_source_inventory", "direct_H_radial_identity_insertion_no_go", "VEV_as_shared_profile_baseline_policy"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["selected_H_to_neutral_insertion_functor", "selected_radial_coordinate_normalization", "physical_neutral_mass_Hessian", "dimensionless_Y_nu_physical_readout", "dimensionful_M_D"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["positive definite", "not a new", "neutrino-specific parameter", "typed insertion", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"second_variation_spectrum": cert["second_variation_eigenvalues"], "selected_tau_H": cert["selected_tau_H"], "selected_r_H": cert["selected_r_H"], "profile_v_GeV": cert["profile_v_GeV"], "next": NEXT}, indent=2))
    print("selected neutral radial second-variation/VEV audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
