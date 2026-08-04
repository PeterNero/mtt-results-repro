from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization"
STATUS = "MTT_SELECTED_NEUTRAL_HIGGS_INSERTION_AND_RADIAL_NORMALIZATION_CLOSED_ACTION_WEIGHT_OPEN"
NEXT = "MTT_Selected_NeutralActionWeightedHiggsResponseAndDimensionfulDiracReadout_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_higgs_insertion_and_radial_normalization.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require(packet["selected_H_line"]["rank"] == 1, "H line is not rank one")
    require(packet["selected_H_line"]["basis_label"] == "H:h0", "H carrier changed")
    require(packet["selected_H_line"]["insertion_magnitude"] == 1.0, "normalization changed")
    insertion = packet["insertion_functor"]
    require(insertion["same_source_H_carrier_and_neutral_channel"] is True, "same-source join failed")
    require(insertion["selected_radial_coordinate_normalization"] is True, "radial normalization failed")
    require(insertion["row_count"] == 9 and cert["dimensionless_derivative_rows_closed"] == 9, "row count changed")
    require(insertion["Gamma_nu_channel_matrix"] == [[1.0, 1.0, 0.0], [0.0, 1.0, 1.0], [1.0, 0.0, 1.0]], "Gamma changed")
    require(insertion["carrier_phase_selected"] is False, "unphysical phase selected")
    phase = packet["phase_quotient_proof"]
    require(phase["phase_independent"] is True and phase["positive_definite"] is True, "phase quotient failed")
    require(all(abs(a-b) < 1e-12 for a,b in zip(phase["curvature_eigenvalues"], [2,2,8])), "curvature changed")
    boundary = packet["typing_boundary"]
    require(boundary["C1_matter_routing_relabelled_as_Higgs"] is False, "C1 matter/Higgs typing violated")
    for key in ["physical_action_costs_S_gamma_attached", "physical_prefactors_A_gamma_attached", "retarded_character_sign_attached", "same_scheme_dimensionful_VEV_selected", "Dirac_only_or_Majorana_action_completeness_closed"]:
        require(boundary[key] is False, f"overclosed: {key}")
    closes = packet["what_closes_here"]
    for key in ["same_source_H_to_neutral_insertion_functor", "selected_dimensionless_radial_coordinate_normalization", "phase_invariant_positive_neutral_Gram_curvature", "dimensionless_dYnu_dhH_rows"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["physical_action_weighted_Y_nu", "dimensionful_M_D", "M_L_or_M_R", "absolute_neutrino_mass_ontology"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical value overclaim")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["one-dimensional orthogonal line", "I3 + X3", "insertion magnitude to one", "does not relabel", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"H_carrier": cert["H_carrier"], "insertion_magnitude": cert["insertion_magnitude"], "rows_closed": cert["dimensionless_derivative_rows_closed"], "curvature": cert["curvature_eigenvalues"], "next": NEXT}, indent=2))
    print("selected neutral-Higgs insertion/radial-normalization audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
