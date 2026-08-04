from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraleffectiveweightidentifiabilityreduction"
STATUS = "MTT_SELECTED_NEUTRAL_EFFECTIVE_WEIGHT_CLOSED_SEPARATE_AS_ROWS_RETIRED_PHYSICAL_SHAPE_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralPhysicalShapeOperatorAndAbsoluteScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_effective_weight_identifiability.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralEffectiveWeightIdentifiabilityReduction_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    gauge = packet["factorization_gauge"]
    require(gauge["separate_A_gamma_and_S_gamma_identifiable"] is False, "factorization overidentified")
    require(abs(gauge["before"]["effective_weight"] - gauge["after"]["effective_weight"]) < 1e-15, "gauge witness failed")
    effective = packet["selected_effective_internal_response"]
    require(effective["combined_internal_overlap_amplitude_closed"] is True, "effective response missing")
    require(effective["equals_Gamma_nu_I3_plus_X3"] is True, "Gamma identity missing")
    require(effective["same_source_provenance_fields"] == "7/7", "same-source fields changed")
    orbit = packet["conjugate_orbit_mass_equivalence"]
    require(orbit["representatives_are_complex_conjugates"] is True, "orbit not conjugate")
    require(orbit["mass_spectra_equal"] is True, "mass spectra differ")
    require(orbit["representative_selection_needed_for_mass_eigenvalues"] is False, "mass representative overrequired")
    require(orbit["representative_selection_needed_for_CP_sensitive_observables"] is True, "CP phase lost")
    cutset = packet["reduced_physical_cutset"]
    require(cutset["minimum_new_continuous_physical_coordinates_for_Dirac_shape_and_scale"] == 2, "cutset count changed")
    require(cutset["one_to_three_knob_policy_compatible"] is True, "knob policy mismatch")
    closes = packet["what_closes_here"]
    for key in ["effective_internal_action_weight_product", "A_gamma_S_gamma_factorization_nonidentifiability", "separate_A_gamma_S_gamma_obligations_retired", "conjugate_representative_mass_equivalence"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["physical_non_affine_shape_operator", "absolute_physical_scale", "dimensionful_M_D", "absolute_neutrino_mass_ontology"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical value overclaim")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["not separately identifiable", "I3+X3", "two identifiable ingredients", "one-to-three-knob", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"effective_weight_closed": cert["combined_internal_effective_weight_closed"], "separate_rows_retired": cert["separate_A_gamma_S_gamma_obligations_retired"], "minimum_coordinates": cert["minimum_new_continuous_physical_coordinates"], "next": NEXT}, indent=2))
    print("neutral effective-weight identifiability audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
